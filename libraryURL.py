
import streamlit as st


def url_sklearn():
	st.markdown(
	    """
	    Linear Regression API Reference :
	    <a href="https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LinearRegression.html">
	    sklearn.linear_model.LinearRegression </a>
	    """, 
	    unsafe_allow_html=True)


def url_statsmodels():
	st.markdown(
	    """
	    Linear Regression API Reference :
	    <a href="https://www.statsmodels.org/stable/generated/statsmodels.regression.linear_model.OLS.html#statsmodels.regression.linear_model.OLS">
	    statsmodels.regression.linear_model.OLS</a>
	    """, 
	    unsafe_allow_html=True)