import feature_select_lib as fsl

# Load the counts dataframe and preprocess
transposed_counts = fsl.preprocess_dataframe()
# Check that gene names are columns (gene1-geneX) & the index is cell types (A-I)
transposed_counts

# Define parameters & scale the data
parameters = fsl.model_parameters(transposed_counts)

# Loop over feature selection-classifier pipeline, fit the model,
# evaluate with accuracy scores, classificatin reports, confusion matrix plots
fsl.run_model(parameters)

# Plot a UMAP that shows trajectory
fsl.plot_umap(transposed_counts, parameters)
