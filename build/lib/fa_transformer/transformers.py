import numpy as np
import pandas as pd
from factor_analyzer import FactorAnalyzer   
from sklearn.base import BaseEstimator, TransformerMixin

class FATransformerInPlace(BaseEstimator, TransformerMixin):
	"""
	This class takes a DataFrame and converts a subet of features into a single feature 
	using 1-Factor Analysis.

	Attributes
	---
	feature_names (list): A list of features that need to be condensed
	composite_feature_name (str): Name of the new feature column
	rotation (str): The rotation to be used by the Factor Analyzer
	method (str): The method to be used by the Factor Analyzer
	"""

	def __init__(self, 
				 feature_names, 
				 composite_feature_name ,
				 rotation='varimax', 
				 method='principal'):
		self.feature_names = feature_names
		self.rotation = rotation
		self.method = method
		self.composite_feature_name = composite_feature_name

	def fit(self, X, y = None):
		fa_df = X[self.feature_names]
		self.fa = FactorAnalyzer(1, rotation=self.rotation, method=self.method)
		self.fa.fit(fa_df)

		return self

	def transform(self, X):
		X_fa = X[self.feature_names]
		lf = pd.DataFrame(self.fa.transform(X_fa))
		lf.index = X.index
		lf.columns = [self.composite_feature_name]

		df = X.drop(self.feature_names, axis = 1)
		df = df.join(lf, how = 'left')
		return df


class CompositeFATransformer(BaseEstimator, TransformerMixin):
	"""
	This class takes a DataFrame and performs n-factor analysis, producing a weighted
	composite score as well as n-factors.

	Attributes
	---
	num_factors (int): The number of factors to be used for Factor Analysis
	rotation (str): The rotation to be used by the Factor Analyzer
	method (str): The method to be used by the Factor Analyzer
	"""

	def __init__(self, num_factors, rotation='varimax', method='principal'):
		self.num_factors = num_factors
		self.rotation = rotation
		self.method = method

	def get_ev(self, X):
		num_features = len(X.columns)
		fa = FactorAnalyzer(num_features, rotation=None, method=self.method)
		fa.fit(X)

		ev, v = fa.get_eigenvalues()
		return ev

	def fit(self, X, y = None):
		ev = self.get_ev(X)
		self.weighted_ev = ev[:self.num_factors] / sum(ev[:self.num_factors])

		self.fa = FactorAnalyzer(self.num_factors, self.rotation, self.method)
		self.fa.fit(X)

		return self

	def transform(self, X):
		lf = pd.DataFrame(self.fa.transform(X))
		lf.columns = ['factor_%i' % (int(x) + 1) for x in lf.columns]
		lf['composite_score'] = lf.apply(lambda x: np.dot(self.weighted_ev, np.array(x)), axis = 1)
		lf.index = X.index
		return lf












