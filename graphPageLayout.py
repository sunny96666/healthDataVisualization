from dash import dcc, html

def topBar():
    """
    graphBasic, graphSmoking, graphDrinking, graphBMI layout에 공통적으로 들어갈 top bar html 코드 리턴
    :return: list
    """
    children = [
        html.Div(
            html.Header(
                html.Div([
                    html.H1(
                        dcc.Link(html.Img(src="/static/images/blogo22222.png"), href="http://127.0.0.1:8050", refresh=True),
                        className="logo"
                    ),
                    html.Nav(
                        html.Ul([
                            html.Li([
                                dcc.Link("데이터 보기", href="#", refresh=True),
                                html.Ul([
                                    html.Li(
                                        dcc.Link("고혈압", href="http://127.0.0.1:8052/고혈압/", refresh=True),
                                    ),
                                    html.Li(
                                        dcc.Link("당뇨", href="http://127.0.0.1:8052/당뇨/", refresh=True),
                                    ),
                                    html.Li(
                                        dcc.Link("고지혈증", href="http://127.0.0.1:8052/고지혈증/", refresh=True),
                                    ),
                                    html.Li(
                                        dcc.Link("빈혈", href="http://127.0.0.1:8052/빈혈/", refresh=True),
                                    ),
                                    html.Li(
                                        dcc.Link("신장", href="http://127.0.0.1:8052/신장/", refresh=True),
                                    ),
                                    html.Li(
                                        dcc.Link("간", href="http://127.0.0.1:8052/간/", refresh=True),
                                    )], className="submenu"
                                )]
                            ),
                            html.Li([
                                dcc.Link("흡연 상태", href="#", refresh=True),
                                html.Ul([
                                    html.Li(
                                        dcc.Link("고혈압", href="http://127.0.0.1:8053/고혈압/흡연상태/", refresh=True),
                                    ),
                                    html.Li(
                                        dcc.Link("당뇨", href="http://127.0.0.1:8053/당뇨/흡연상태/", refresh=True),
                                    ),
                                    html.Li(
                                        dcc.Link("고지혈증", href="http://127.0.0.1:8053/고지혈증/흡연상태/", refresh=True),
                                    ),
                                    html.Li(
                                        dcc.Link("빈혈", href="http://127.0.0.1:8053/빈혈/흡연상태/", refresh=True),
                                    ),
                                    html.Li(
                                        dcc.Link("신장", href="http://127.0.0.1:8053/신장/흡연상태/", refresh=True),
                                    ),
                                    html.Li(
                                        dcc.Link("간", href="http://127.0.0.1:8053/간/흡연상태/", refresh=True),
                                    )], className="submenu"
                                )]
                            ),
                            html.Li([
                                dcc.Link("음주 여부", href="#", refresh=True),
                                html.Ul([
                                    html.Li(
                                        dcc.Link("고혈압", href="http://127.0.0.1:8054/고혈압/음주여부/", refresh=True),
                                    ),
                                    html.Li(
                                        dcc.Link("당뇨", href="http://127.0.0.1:8054/당뇨/음주여부/", refresh=True),
                                    ),
                                    html.Li(
                                        dcc.Link("고지혈증", href="http://127.0.0.1:8054/고지혈증/음주여부/", refresh=True),
                                    ),
                                    html.Li(
                                        dcc.Link("빈혈", href="http://127.0.0.1:8054/빈혈/음주여부/", refresh=True),
                                    ),
                                    html.Li(
                                        dcc.Link("신장", href="http://127.0.0.1:8054/신장/음주여부/", refresh=True),
                                    ),
                                    html.Li(
                                        dcc.Link("간", href="http://127.0.0.1:8054/간/음주여부/", refresh=True),
                                    )], className="submenu"
                                )]
                            ),
                            html.Li([
                                dcc.Link("BMI 단계", href="#", refresh=True),
                                html.Ul([
                                    html.Li(
                                        dcc.Link("고혈압", href="http://127.0.0.1:8055/고혈압/BMI단계/", refresh=True),
                                    ),
                                    html.Li(
                                        dcc.Link("당뇨", href="http://127.0.0.1:8055/당뇨/BMI단계/", refresh=True),
                                    ),
                                    html.Li(
                                        dcc.Link("고지혈증", href="http://127.0.0.1:8055/고지혈증/BMI단계/", refresh=True),
                                    ),
                                    html.Li(
                                        dcc.Link("빈혈", href="http://127.0.0.1:8055/빈혈/BMI단계/", refresh=True),
                                    ),
                                    html.Li(
                                        dcc.Link("신장", href="http://127.0.0.1:8055/신장/BMI단계/", refresh=True),
                                    ),
                                    html.Li(
                                        dcc.Link("간", href="http://127.0.0.1:8055/간/BMI단계/", refresh=True),
                                    )], className="submenu"
                                )]
                            )
                        ]), className="gnb fl"
                    ),
                    html.Nav(
                        html.Ul(html.Li(dcc.Link("서비스구독", href="#"))
                                ), className="tnb"
                    )
                ], className="innerheader"
                ),
            ), id="wrap"
        )
    ]
    return children

def bottomBar():
    """
    graphBasic, graphSmoking, graphDrinking, graphBMI layout에 공통적으로 들어갈 bottom bar html 코드 리턴
    :return: list
    """
    children = [
        html.Br(),
        html.Br(),
        html.Br(),
        html.Div(
            html.Footer(
                html.Div([
                    html.Div(
                        html.Img(src="/static/images/blogo999.png", alt="하단로고")
                        , className="blogo"
                    ),
                    html.Div(
                        html.P(["01234 서울특별시 강남구 논현로 99 픽데이터 빌딩 Copyright 2023",
                               dcc.Link("Pick Data.", href="mailto:pickdata@pickdata.com"),
                               "All right reserved."])
                        , className="copyright"),
                    html.Div(
                        html.Ul([
                            html.Li(dcc.Link("온라인구매시스템", href="#")),
                            html.Li(dcc.Link("고객문의", href="#")),
                            html.Li(dcc.Link("뉴스 & 공지사항", href="#")),
                            html.Li(dcc.Link("개인정보처리방침", href="#"))
                        ])
                        , className="blist")]
                    , className="footerInner"))
            , id="wrapp")]
    return children