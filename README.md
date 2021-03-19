# Factor Analysis Transformers

*fa_transformer* is a small Python package which makes available two Factor Analyzer Transformers that are ideal for use in scikit-learn pipelines

## Possible Use Cases

* **Dimensionality reduction**: The package can be used to convert n features with underlying factors into a single feature.
* **Composite Score generation**: The package also facilitates creation of Composite scores that are either a 1-factor score or a dot product of transformed factor scores and their respective eigenvalues.

## Classes

### class FATransformerInPlace(BaseEstimator, TransformerMixin):

This class takes a DataFrame and converts a subet of features into a single feature 
using 1-Factor Analysis.

#### Attributes

* **feature_names (list)**: A list of features that need to be condensed
* **composite_feature_name (str)**: Name of the new feature column
* **rotation (str)**: The rotation to be used by the Factor Analyzer
* **method (str)**: The method to be used by the Factor Analyzer


### class CompositeFATransformer(BaseEstimator, TransformerMixin):

This class takes a DataFrame and performs n-factor analysis, producing a weighted
composite score as well as n-factors.

#### Attributes

* **num_factors (int)**: The number of factors to be used for Factor Analysis
* **rotation (str)**: The rotation to be used by the Factor Analyzer
* **method (str)**: The method to be used by the Factor Analyzer


