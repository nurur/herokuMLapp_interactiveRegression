
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
import statsmodels.api as sm


def fit_sklearn(data, select_range):
	# Generate Dynamic Data and Fit
	dynamic_range  = np.array( select_range )
	dynamic_filter = np.where((data[:,0] >= dynamic_range[0]) & (data[:,0] <= dynamic_range[1]))
	dynamic_data   = data[ dynamic_filter ]

	X_dynamic = dynamic_data[:,0].reshape(dynamic_data.shape[0],-1)
	y_dynamic = dynamic_data[:,1]

	model = LinearRegression()
	model.fit(X_dynamic, y_dynamic)

	a = model.intercept_
	b = model.coef_

	x_fit = dynamic_data[:,0]
	y_fit = a + b*dynamic_data[:,0]

	paramCols = np.array(['Selected X Range', 'Intercept', 'Model Coefficient','R-squared','Adj. R-squared'])
	paramVals = np.array([ str(select_range),round(a,2),round(b[0],2), 'NA', 'NA'])
	theData   = np.column_stack( (paramCols, paramVals) )
	theCols   = ["Parameters", "Values"]
	theRes    = pd.DataFrame(theData, columns=theCols)
	theRes['emptyString'] = ""
	theRes.set_index('emptyString', inplace=True)
	theRes.index.name=None

	return a,b,x_fit,y_fit,theRes




def fit_statsmodels(data, select_range):
	# Generate Dynamic Data and fit
	dynamic_range  = np.array( select_range )
	dynamic_filter = np.where((data[:,0] >= dynamic_range[0]) & (data[:,0] <= dynamic_range[1]))
	dynamic_data   = data[ dynamic_filter ]

	X_dynamic = dynamic_data[:,0].reshape(dynamic_data.shape[0],-1)
	y_dynamic = dynamic_data[:,1]

	X_dynamic = sm.add_constant(X_dynamic)
	
	model = sm.OLS(y_dynamic,X_dynamic)
	results = model.fit()
	
	a = results.params[0]
	b = results.params[1]
	Rs = results.rsquared
	aRs = results.rsquared_adj
	Pval = results.pvalues


	x_fit = dynamic_data[:,0]
	y_fit = a + b*dynamic_data[:,0]

	paramCols = np.array(['Selected X Range', 'Intercept', 'Model Coefficient','R-squared','Adj. R-squared'])
	paramVals = np.array([ str(select_range),round(a,2),round(b,2),round(Rs,2),round(aRs,2)])
	theData   = np.column_stack( (paramCols, paramVals) )
	theCols   = ["Parameters", "Values"]
	theRes    = pd.DataFrame(theData, columns=theCols)
	theRes['emptyString'] = ""
	theRes.set_index('emptyString', inplace=True)
	theRes.index.name=None

	return a,b,x_fit,y_fit,theRes


