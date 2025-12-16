# Import modules
import pandas as pd
import string
import seaborn as sns
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier, AdaBoostClassifier
from sklearn.metrics import confusion_matrix, classification_report, accuracy_score
from sklearn.pipeline import Pipeline
from sklearn.feature_selection import SelectFromModel
import matplotlib.pyplot as plt
import matplotlib.cm as cm


def preprocess_dataframe():
    """
    Input: CSV counts matrix from scMultiSim
    Load the counts matrix, remove 0 counts, standardise gene labels & cell labels, transpose dataframe.
    Output: preprocessed & transposed panda data frame
    """
    # Load counts matrix as panda data frame
    counts = pd.read_csv(
        "scMultiSim_counts_SIMPLE.csv",
        index_col=0,
        dtype=str
    )

    # Remove any genes that are all 0 counts
    counts = counts.drop(counts[(counts == 0).all(axis=1)].index)

    # Remove any cells that have no gene expression
    counts = counts.drop(columns=counts.columns[(counts == 0).all()])

    # Standardise gene labels so 'gene' precedes each number
    counts.index = [
        num if num.startswith("gene") else "gene" + num
        for num in counts.index
    ]

    # Treat cells as samples, genes as features - need to transpose the panda dataframe
    transposed_counts = counts.T

    # Split the cell labels at the first "."
    transposed_counts.index = [cell.split(".")[0] for cell in transposed_counts.index]

    # Change cell labels from '#_#' to 'A', 'B', 'C', etc.
    cell_types = transposed_counts.index.unique()
    cell_labels = {
        cell_types: letter
        for cell_types, letter in zip(cell_types, string.ascii_uppercase)
    }

    transposed_counts.index = transposed_counts.index.map(cell_labels)

    return transposed_counts


def model_parameters(transposed_counts):
    """
    INPUT: Transposed_counts (panda dataframe OUTPUT from preprocess_dataframe())
    Set up the parameters for training the models.
    OUTPUT: A list of all of the parameters
    """
    # Define genes (columns) as features
    X = transposed_counts

    # Define cell IDs (row index) as targets
    y = transposed_counts.index

    # Check that the lengths match
    print(f"Feature length = {len(X)}")
    print(f"Sample/target length = {len(y)}")

    # Set up scale for the model
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=1)

    scaler = StandardScaler()
    scaler.fit(X_train)
    X_train_scaled = scaler.transform(X_train)
    X_test_scaled = scaler.transform(X_test)

    parameters = [X, y, X_train, X_test, y_train, y_test, scaler, X_train_scaled, X_test_scaled]

    return parameters


def run_model(parameters):
    """
    INPUT: The parameters list (OUTPUT from model_parameters())
    List the models to test, loop over feature selection - classifier, fit and evaluate the model.
    OUTPUT: Model accuracy score, Classification report, Confusion matrices.
    """
    # List all the models to be tested
    models = {
        "Random Forest": RandomForestClassifier(n_estimators=1000, random_state=42),
        "Gradient Boosting": GradientBoostingClassifier(random_state=42),
        "AdaBoost": AdaBoostClassifier(random_state=42),
    }

    # Cell labels are unique characters taken from parameters[1] = y
    cell_types = parameters[1].unique()

    # Number of models
    n_models = len(models)

    # Create empty subplots (1 row, n_models columns)
    fig, axes = plt.subplots(1, n_models, figsize=(6 * n_models, 6))

    results = {}

    # Loop over each model
    for ax, (name, model) in zip(axes, models.items()):
        print(f"Training {name}")

        # Feature selection-classifier pipeline
        pipeline = Pipeline([
            ('feature_selection', SelectFromModel(
                estimator=model,
                threshold="median"
            )),
            ('classifier', model)
        ])

        # Fit the model: parameters[2] = X_train, parameters[4] = y_train
        pipeline.fit(parameters[2], parameters[4])
        y_pred = pipeline.predict(parameters[3])

        # Evaluate the accuracy of each model: parameters[5] = y_test
        accuracy = accuracy_score(parameters[5], y_pred)
        report = classification_report(parameters[5], y_pred)

        # Results
        results[name] = {
            "Accuracy": accuracy,
            "Classification Report": report
        }

        # Print the accuracy scores and classification reports
        print(f"{name} Accuracy: {accuracy:.4f}")
        print(f"{name} Classification Report:\n{report}")

        # Fill the empty subplots with confusion matrices
        cm = confusion_matrix(parameters[5], y_pred)
        sns.heatmap(
            cm,
            annot=True,
            fmt='d',
            cmap='Blues',
            ax=ax,
            xticklabels=cell_types,
            yticklabels=cell_types
        )
        ax.set_title(f'{name} Confusion Matrix')
        ax.set_xlabel('Predicted cell type')
        ax.set_ylabel('Actual cell type')

    # Show the final plot with the confusion matrices for each model
    plt.tight_layout()
    plt.show()
