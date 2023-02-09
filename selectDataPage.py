from flask import Flask, render_template

application = Flask(__name__)


@application.route('/', methods=['GET'])
def index():
    """
    selectData page 서버 실행
    :return: render_template()
    """
    return render_template('selectData.html')

if __name__ == "__main__":
    application.run(port=8051)
