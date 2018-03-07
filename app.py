import os

from flask import Flask, render_template, request

import genCode as gc
import uploadFile as uploadFile
import testPandas as tPS
import json
from request import requestNexus

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


@app.route('/upload', methods=['GET'])
def upload():
    return render_template('upload.html')


app.config['UPLOAD_FOLDER'] = '/pythonGP1/'
app.config['MAX_CONTENT_LENGTH'] = 2 * 1024 * 1024


@app.route('/uploadFile', methods=['POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        if file and uploadFile.allowed_file(file.filename):
            filename = '1.xls'
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

    result = tPS.readExcel()

    return render_template('upload.html', m=result)


@app.route('/transString', methods=['POST', 'GET'])
def transString():
    if request.method == 'GET':
        return render_template('tranString.html')
    else:
        str1 = request.form['str1']
        sign = request.form['sign']
        result = str1.replace(sign, '\n')
        return result


@app.route('/nexusJarURL', methods=['POST', 'GET'])
def nexusJarURL():
    if request.method == 'GET':
        return render_template('nexusUrl.html')
    else:
        dx_name = request.form['dxName']
        list = requestNexus.getUrl(dx_name)
        return json.dumps(list)


if __name__ == "__main__":
    app.run()
