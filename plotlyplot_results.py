
import plotly.graph_objects as go

def plot_mainResults(X,y,xfit,yfit):
	fig = go.Figure()
	fig.add_trace( go.Scatter(x=X.ravel(), y=y, name="Data", mode='markers', marker_size=6, marker_color='red', text='X') ) 
	fig.add_trace( go.Scatter(x=xfit, y=yfit, name="Model Fit", mode='lines', marker_color='blue', line_width=4) )

	fig.update_layout(
	showlegend=True, 
	legend=dict(yanchor="top", y=0.98, xanchor="left", x=0.02),
	autosize=False,
	width=500, height=355,
	margin=dict(l=0,r=0,b=0,t=0,pad=0),
	xaxis=dict(title='X', showgrid=True, zeroline=False), 
	yaxis=dict(title='Y', showgrid=True, zeroline=None))

	return fig 