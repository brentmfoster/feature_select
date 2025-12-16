# feature_select

## Introduction
Single-cell RNA sequencing (scRNA-seq) captures active transcripts at a cellular resolution. While extremely useful, scRNA-seq datasets can be extremely large, with tens to hundreds of thousands of genes (features) expressed in each individual cell (sample). Such high-dimensional datasets present a major challenge for evolutionary and developmental biologists who are interested in distinguishing genes that are most informative of distinct cell types from general housekeeping genes and/or experimental noise. One key assumption of scRNA-seq is that a relatively small number of expressed genes are sufficient to predict specific cell types (Ramskold et al., 2009). If we accept this assumption, then the dimensionality problem can be viewed as a feature sorting/selection problem, where genes are features and cell identity is the classifier target (Radley et al., 2023).

For the purposes of this assignment, I have generated a synthetic dataset consisting of 500 genes and 1000 cells representing 9 cell types (Li et al., 2025). I then apply a basic machine learning pipeline that selects important features prior to classification.

### Files
- 'feature_select.py' - A script that selects important features and classifies cell type. 
- 'scMultiSim_counts.csv' - A counts matrix
- 'requirements.txt' - Version and dependency information

## Methods
Synthetic data was generated with via the scMultiSim software (Li et al., 2025) in R Studio (Posit team, 2025). The resulting CSV matrix consists of the simulated transcript counts, with genes as rows and cells as columns. This matrix was shared in Jupyter Notebook.

The code loads the CSV counts matrix as a panda data frame. This is then filtered and transposed such that genes (i.e. features) are columns and cells (i.e. targets) are rows. Feature selection and classification were encoded using the instructions from ‘Feature selection as part of a pipeline’ (scikit-learn, 1.13.6). Code adapted from my group’s presentation loops through the following three classifier models for final evaluation: Random Forest, Gradient Boosting, and AdaBoost. Please note that the code may take a few minutes to run.

## Results
Random Forest and Gradient Boosting classifiers performed much better than AdaBoost at predicting the simulated cell type from (Figure 1).

## Conclusions

## References
Ramsköld, D., Wang, E.T., Burge, C.B., and Sandberg, R. (2009). An abundance of ubiquitously expressed genes revealed by tissue transcriptome data. PLoS Comput. Biol. https://doi.org/10.1371/journal.pcbi.1000598.

Radley, A., Corujo-Simon, E., Nichols, J., Smith, A., Dunn, S.J. (2023). Entropy sorting of single-cell RNA sequencing data reveals the inner cell mass in the human pre-implantation embryo. Stem Cell Reports. https://doi.org/10.1016/j.stemcr.2022.09.007

Li, H., Zhang, Z., Squires, M., Chen, X., Zhang, X. (2025). scMultiSim: simulation of single-cell multi-omics and spatial data guided by gene regulatory networks and cell-cell interactions. Nature Methods. https://doi.org/10.1038/s41592-025-02651-0

Posit team (2025). RStudio: Integrated Development Environment for R. Posit Software, PBC, Boston, MA. URL http://www.posit.co/.
