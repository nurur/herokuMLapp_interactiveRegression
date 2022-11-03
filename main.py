
import numpy as np
import pandas as pd
import re
import plotly.graph_objects as go
from sklearn.linear_model import LinearRegression


import streamlit as st
st.set_page_config(layout = "wide")
pd.set_option("display.precision", 2)
pd.set_option("display.float_format", lambda x: "%.2f" % x)
pd.set_option('display.max_colwidth', None)


########################################################################### Data Loading
y = [3,2,3,4,1,3,5,8,9,11,14,13,12,11,10,12,12,17,20,21,22,23,22,24,22]
y = np.array(y) 

X = np.arange( len(y) ) + 1
X = X.reshape(len(y), -1)
Xmin = int( X.min() )
Xmax = int( X.max() )

data = np.column_stack((X,y))


########################################################################### Sidebar Designing 
st.sidebar.subheader("Select a ML Library")
select_tool = st.sidebar.selectbox('Select between SKLearn and StatsModels', 
	['Click to Select','ScikitLearn','StatsModels'], 0 )

if select_tool != "Click to Select":
	st.sidebar.subheader("Select a Range for the X-Axis")
	select_range = st.sidebar.slider('Select Xmin & Xmax', Xmin, Xmax, (4,10) )


########################################################################### Build the Main Page
# st.write("""
# 	# Interactive Linear Regression App
# 	### Using Python, Plotly, and Streamlit
# 	#### Created by Nurur Rahman
# 	""")
mkdtext = """
		# Interactive Regression App 
		### Using Python, Plotly, and Streamlit
		<font color='red'> Created by Nurur Rahman </font>
		"""
st.markdown(mkdtext, unsafe_allow_html=True)


# Call Utility Functions
if select_tool == 'Click to Select':
	pass
elif select_tool == 'ScikitLearn': 
	from libraryURL import url_sklearn
	url_sklearn()
else:
	from libraryURL import url_statsmodels
	url_statsmodels()
st.write(" ")
st.write(" ")

###########################################################################

if select_tool == 'Click to Select':
	pass
elif select_tool == 'ScikitLearn':
	from fittedModel import fit_sklearn
	a,b,x_fit,y_fit,res = fit_sklearn(data, select_range)
else:
	from fittedModel import fit_statsmodels
	a,b,x_fit,y_fit,res = fit_statsmodels(data, select_range)


if select_tool != 'Click to Select':
	try:
		col1,col2 = st.columns((1,1))
		with col1:
			st.text("Showing Model Inputs and Outputs")
			#col1.subheader("Showing Model Inputs and Outputs")
			st.table( res )
		with col2:
			st.text("Showing Interactive Regression")
			#col2.subheader("Showing Interactive Regression")
			from plotlyplot_results import plot_mainResults
			theFig = plot_mainResults(X,y,x_fit,y_fit)
			st.plotly_chart( theFig )
	except NameError:
		print("There is no Fit or Result")


