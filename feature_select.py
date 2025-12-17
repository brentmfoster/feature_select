import feature_select_lib as fsl
import pandas as pd

# Load the counts dataframe
print(f"Loading counts dataframe")
counts = pd.read_csv(
    "scMultiSim_counts_SIMPLE.csv",
    index_col=0,
    dtype=str
)

# Preprocess the counts dataframe
print(f"\nPreprocessing counts dataframe")
transposed_counts = fsl.preprocess_dataframe(counts)

# Check that gene names are columns (gene1-geneX) & the index is cell types (A-I)
transposed_counts

# Define parameters & scale the data
print(f"\nDefining model parameters & scaling data")
parameters = fsl.model_parameters(transposed_counts)

# Loop over feature selection-classifier pipeline, fit the model,
# evaluate with accuracy scores, classificatin reports, confusion matrix plots
print(f"\nComparing model accuracy scores, classification reports & confusion matrices\n")
fsl.run_model(parameters)

# Plot a UMAP that shows cell trajectory
print(f"\nPlotting cell trajectory UMAP")
fsl.plot_umap(transposed_counts, parameters)

print(f"\nFeature select is finished running!\n")
