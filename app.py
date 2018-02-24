from flask import Flask, render_template, request
import genCode as gc

app = Flask(__name__)
application = app


@app.route("/")
def hello():
    return render_template('index.html')


@app.route('/getBeanHtml')
def getBeanHtml():
    return render_template('genBean.html')


@app.route('/genBeanCode', methods=['POST'])
def genBeanCode():
    name = request.form['name']
    desc = request.form['desc']

    template = gc.genCode(name, desc)

    return template


if __name__ == "__main__":
    app.run()
