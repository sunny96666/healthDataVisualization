import dash
import dash_core_components as dcc
import dash_html_components as html

app = dash.Dash(__name__)

markdown_text = '''
#### Dash 와 마크다운

**Dash** 앱은 마크다운으로 작성할 수 있습니다.\n,\n
Dash 는 [CommonMark](http://commonmark.org/) 사양을 기준으로 사용합니다.\n
만약, 마크다운 문서작성이 처음이시라면
마크다운 튜토리얼 [60 Second Markdown Tutorial](http://commonmark.org/help/) 을 확인해 보세요!
'''

app.layout = html.Div([
    dcc.Markdown(children=
                 markdown_text)
])

if __name__ == '__main__':
    app.run(port="9000")

