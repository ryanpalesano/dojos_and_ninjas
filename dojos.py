from flask import render_template, redirect, request
from flask_app import app
from flask_app.models.dojo import Dojo


@app.route('')
def index():
    return redirect('/dojos')


@app.route('/dojos')
def dojos():
    dojos = Dojo.get_all()
    print(dojos[0].name)
    return render_template("index.html", all_dojos=dojos)


@app.route('/create/dojo', methods=['POST'])
def create_dojo():
    Dojo.save(request.form)
    return redirect('/dojos')


@app.route('/dojo/<int:id>')
def show_dojo(id):
    data = {
        "id": id
    }
    return render_template('dojo.html', dojo=Dojo.get_one_with_ninjas(data))

@app.route('/delete/<int:id>')
def delete(id):
    banana = {
        "id": id
    }
    Dojo.delete(banana)
    return redirect('/dojos')
