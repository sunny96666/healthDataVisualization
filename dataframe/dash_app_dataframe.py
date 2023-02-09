import plotly.express as px
import component.pandas_example001 as pandas_example001


# ---------------------------------------------------------------------
# fig setup
def fig_data():
    df = px.data.iris()
    fig = px.scatter(df, x="sepal_length", y="sepal_width",
                     color="species")
    return fig

