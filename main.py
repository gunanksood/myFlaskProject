from flask import Flask
from flask import render_template
from flask import request
import models as dbHandler

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def main():
    if request.method == 'GET':
        users = dbHandler.retrieveTable()
        return render_template('startbootstrap-4-col-portfolio/index.html', users = users)
    elif request.method == 'POST':
        kwargs = {
            'title': request.form['title'],
            'content': request.form['content'],
        }
        dbHandler.insertTable(kwargs['title'], kwargs['content'])
        users = dbHandler.retrieveTable()
        print(kwargs['title'], kwargs['content'])
        return render_template(
            'startbootstrap-4-col-portfolio/index.html', users = users)

@app.route('/hey/<id>/<title>/<content>/')
def function(id,title,content):
    print(id)
    print(title)
    print(content)
    dbHandler.updateTable(id,title,content)
    users = dbHandler.retrieveTable()
    return render_template('startbootstrap-4-col-portfolio/index.html', users=users)

if __name__ == '__main__':
    app.run(debug = True)
