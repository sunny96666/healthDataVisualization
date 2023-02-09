from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd
from flask import Flask

import aboutData
import graphPageLayout
import graphSummary

application = Flask(__name__)

external_stylesheets=["/static/css/graph_style.css"]

app1 = Dash(__name__, server=application, url_base_pathname='/고혈압/음주여부/', title="고혈압",external_stylesheets = external_stylesheets)
app2 = Dash(__name__, server=application, url_base_pathname='/당뇨/음주여부/', title="당뇨",external_stylesheets = external_stylesheets)
app3 = Dash(__name__, server=application, url_base_pathname='/고지혈증/음주여부/', title="고지혈증",external_stylesheets = external_stylesheets)
app4 = Dash(__name__, server=application, url_base_pathname='/빈혈/음주여부/', title="빈혈",external_stylesheets = external_stylesheets)
app5 = Dash(__name__, server=application, url_base_pathname='/신장/음주여부/', title="신장",external_stylesheets = external_stylesheets)
app6 = Dash(__name__, server=application, url_base_pathname='/간/음주여부/', title="간",external_stylesheets = external_stylesheets)

def graph(graph_ydatas):
    """
    '음주 여부' 관련 그래프 생성 및 리턴
    :param graph_ydatas: 각 질병마다 출력할 검진명 리스트
    :return: list
    """
    data_a = aboutData.preprocessing()
    # 그래프와 검진명을 담을 리스트 생성
    L1=[]
    L2=[]
    for graph_ydata in graph_ydatas:
        # 각 수치마다 필요한 정상수치 기준선 가져오기
        y0, y1 = aboutData.standard(graph_ydata)

        #음주 여부에 따라 연령대별 남성들의 검진 수치 평균을 구하여 dataframe 만들기
        y_male_s1 = data_a[(data_a["성별"] == "남")&(data_a["음주여부"] == '마신다')].groupby(["연령"])[graph_ydata].mean()
        y_male_s1 = pd.DataFrame(y_male_s1)
        y_male_s1["성별 및 음주여부"] = "남-마심"

        y_male_s2 = data_a[(data_a["성별"] == "남")&(data_a["음주여부"] =='마시지 않는다')].groupby(["연령"])[graph_ydata].mean()
        y_male_s2 = pd.DataFrame(y_male_s2)
        y_male_s2["성별 및 음주여부"] = "남-마시지 않음"

        #음주 여부에 따라 연령대별 남성들의 검진 수치 평균을 구하여 dataframe 만들기
        y_female_s1 = data_a[(data_a["성별"] == "여")&(data_a["음주여부"] =='마신다')].groupby(["연령"])[graph_ydata].mean()
        y_female_s1 = pd.DataFrame(y_female_s1)
        y_female_s1["성별 및 음주여부"] = "여-마심"

        y_female_s2 = data_a[(data_a["성별"] == "여")&(data_a["음주여부"] =='마시지 않는다')].groupby(["연령"])[graph_ydata].mean()
        y_female_s2 = pd.DataFrame(y_female_s2)
        y_female_s2["성별 및 음주여부"] = "여-마시지 않음"

        # 남녀 dataframe 합치기
        df = pd.concat([y_male_s1,y_male_s2, y_female_s1,y_female_s2])
        df.reset_index(inplace=True)

        # 그래프 그리기
        fig = px.line(df, y=graph_ydata, x="연령",  color="성별 및 음주여부", markers=True)

        # 그래프에 수평선(정상수치 기준선) 추가하기
        fig.add_hline(y=y0, line_width=3, line_dash="dash", line_color="green")

        # 정상수치 기준선이 2개인 경우(y1이 0이 아닌 경우) 수평선 추가하기
        if y1 != 0:
            fig.add_hline(y=y1, line_width=3, line_dash="dot", line_color="green")

        fig.update_layout(
            font=dict(
                size=13)
        )

        # 검진명과 그래프 리스트에 담기
        L1.append(graph_ydata)
        L2.append(fig)
    return L1, L2

def chart_layout(title):
    """
    각 검진별 그래프 layout 리턴
    :param title: dash.flask.title
    :return: dash layout
    """

    # app.title로 검진명 리스트 값 받기
    ydatas = aboutData.change_ydata(title)

    # 그래프와 검진명 값 받기
    L1,L2 = graph(ydatas)

    # topbar layout 가져오기
    children = graphPageLayout.topBar()

    # 그래프 및 설명 텍스트 layout 추가하기
    for a, b in zip(L1,L2):
        children += [
            html.Br(),
            html.Br(),
            html.Br(),
            html.Br(),
            html.Br(),
            html.Br(),
            html.Br(),
            html.Br(),
            html.Br(),
            html.H1(children="연령별 남녀 및 음주 여부에 따른 평균 " + a + "  수치"
                    , style={'textAlign':'center', 'color':'#000066','font-weight': 'bold','font-size':'30px'}),
            html.Br(),
            html.Br(),
            html.Br(),
            dcc.Markdown(children=
                     graphSummary.graphData(a),
                     style={'textAlign': 'center', 'color': '#000066', 'font-weight': 'bold','font-size':'20px'}
                     ),
            html.Br(),
            html.Br(),
            dcc.Graph(
                id=a,
                figure=b
            ),
            html.Br(),
            html.Br(),
            html.Br(),
            html.Br(),
            html.Br(),
            html.Div(
                dcc.Markdown(children=
                             graphSummary.graph_drinking(a)
                             ,
                             style={'color': '#333300', 'font-weight': 'bold', 'font-size': '22px', 'textAlign': 'left',
                                    'display': 'inline-block',
                                    'border': '1.5px solid ', 'padding': '10px'})
                , style={'margin': 'auto', 'display': 'flex', 'justify-content': 'center'}),

            html.Br(),
            html.Br(),
            html.Br(),
            html.Br()]

        # bottombar layout 추가하기
    children += graphPageLayout.bottomBar()
    sample_layout = html.Div(children)
    return sample_layout

app1.layout = chart_layout(app1.title)
app2.layout = chart_layout(app2.title)
app3.layout = chart_layout(app3.title)
app4.layout = chart_layout(app4.title)
app5.layout = chart_layout(app5.title)
app6.layout = chart_layout(app6.title)


if __name__ == '__main__':
    application.run(port=8054)