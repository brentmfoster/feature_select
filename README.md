# Feature Select
#### *Brent Foster, 2025*

## Introduction
Single-cell RNA sequencing (scRNA-seq) captures active transcripts at a cellular resolution. While extremely useful, scRNA-seq datasets can be extremely large, with tens to hundreds of thousands of genes (features) expressed in each individual cell (sample). Such high-dimensional datasets present a major challenge for biologists who are interested in distinguishing genes that are most informative of distinct cell types from general housekeeping genes and/or experimental noise. One key assumption of scRNA-seq is that a relatively small number of expressed genes are sufficient to predict specific cell types (Ramsköld et al., 2009). If we accept this assumption, then the dimensionality problem can be viewed as a feature selection problem, where genes are features and cell identity is the classifier target (Radley et al., 2023).

For the purposes of this assignment, I have generated a simplified synthetic dataset consisting of 500 genes and 1000 cells representing 9 cell types. I then apply a basic machine learning pipeline that selects important features prior to classification and plot a basic UMAP.

## Methods
### *Files*
- 'feature_select.py' - A script that selects important features and classifies cell type. 'scMultiSim_counts.csv' is loaded as a panda data frame, then filtered and transposed such that genes (i.e. features) are columns and cells (i.e. targets) are rows. Feature selection and classification were encoded using the instructions from ‘Feature selection as part of a pipeline’ (scikit-learn, 1.13.6). Code adapted from my group’s presentation loops through a feature selection-classifier pipeline using the following three models for final evaluation: Random Forest, Gradient Boosting, and AdaBoost.
- 'feature_selection_lib.py' - A library containing the necessary modules to import and definitions of functions used in the script.
- 'requirements.txt' - Jupyter Lab version and dependency information
- 'scMultiSim_counts_SIMPLE.csv' - Synthetic scRNA-seq counts generated with scMultiSim software (Li et al., 2025) in R Studio (Posit team, 2025). Note that in the original dataframe, genes are rows and cells are columns.

#### Please note that scripts have been saved as python files. 

### *Installation*
In your terminal, create feature_select directory (or a name of your choice). Change to that new directory and run the following:
- uv init --bare
- uv add jupyterlab numpy pandas scikit-learn seaborn umap-learn (check the requirements.txt file for dependency versions)
- uv run jupyter lab
- Add 'feature_select.py', 'feature_selection_lib.py', and 'scMultiSim_counts_SIMPLE.csv' to the same working directory in Jupyter Lab 

## Results
<img width="1760" height="590" alt="download" src="https://github.com/user-attachments/assets/25cffc3d-ee43-4b94-a893-cb9efcbddc48" />
Figure 1. Random Forest and Gradient Boosting classifiers performed better than AdaBoost at predicting the simulated cell type (accuracy scores: Random Forest (0.9880), Gradient Boosting (0.9840), Adaboost (0.6920)). A-I are labels for the 9 cell types from the original dataframe.


<img width="650" height="440" alt="download" src="https://github.com/user-attachments/assets/0fda6e75-e3dd-4dfb-9982-709541360047" />

Figure 2. Simulated cells show a distinct developmental trajectory.

## Summary
When running 'feature_select.py', there is a warning that recommends updating jupyter and ipywidgets to view a progress bar while the UMAP is loading. Since the script is functional, I elected to ignore this warning.

The feature selection-classifier pipeline appears to yield 'accurate' cell type predictions (Figure 1; see also the accuracy score and classification report outputs). However, this dataset is likely grossly oversimplified, as there appears to be very little biological noise in the UMAP (Figure 2). It would be interesting to see if I get the same results with more complex simulations or real-world scRNA-seq data. I would also be interested in working out a feature ranking algorithm that gives me X number of top-ranked genes for each cell type.

## References
Ramsköld, D., Wang, E.T., Burge, C.B., and Sandberg, R. (2009). An abundance of ubiquitously expressed genes revealed by tissue transcriptome data. PLoS Comput. Biol. https://doi.org/10.1371/journal.pcbi.1000598.

Radley, A., Corujo-Simon, E., Nichols, J., Smith, A., Dunn, S.J. (2023). Entropy sorting of single-cell RNA sequencing data reveals the inner cell mass in the human pre-implantation embryo. Stem Cell Reports. https://doi.org/10.1016/j.stemcr.2022.09.007

Li, H., Zhang, Z., Squires, M., Chen, X., Zhang, X. (2025). scMultiSim: simulation of single-cell multi-omics and spatial data guided by gene regulatory networks and cell-cell interactions. Nature Methods. https://doi.org/10.1038/s41592-025-02651-0

Posit team (2025). RStudio: Integrated Development Environment for R. Posit Software, PBC, Boston, MA. URL http://www.posit.co/.
