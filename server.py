from flask import Flask, flash, render_template, redirect, url_for, request, session
from module.barang import Barang
from module.supplier import Supplier


app = Flask(__name__)
app.secret_key = "34rgdg54"
dbbrg = Barang()
dbsup = Supplier()

#======================================================================
# Dashboard Utama
#======================================================================
@app.route('/')
def index():
    data = dbbrg.read(None)

    return render_template('index.html', data = data)

#======================================================================
# CRUD Master Barang
#======================================================================
@app.route('/barang/')
def baranglist():
    data = dbbrg.read(None)

    return render_template('barang/index.html', data = data)

@app.route('/barang/add/')
def addbarang():
    return render_template('barang/add.html')

@app.route('/addbarangact', methods = ['POST', 'GET'])
def addbarangact():
    if request.method == 'POST' and request.form['save']:
        if dbbrg.insert(request.form):
            flash("A new barang has been added")
        else:
            flash("A new barang can not be added")

        return redirect(url_for('baranglist'))
    else:
        return redirect(url_for('baranglist'))

@app.route('/barang/update/<int:id>/')
def updatebarang(id):
    data = dbbrg.read(id);

    if len(data) == 0:
        return redirect(url_for('baranglist'))
    else:
        session['update'] = id
        return render_template('barang/update.html', data = data)

@app.route('/updatebarangact', methods = ['POST'])
def updatebarangact():
    if request.method == 'POST' and request.form['update']:

        if dbbrg.update(session['update'], request.form):
            flash('A record has been updated')

        else:
            flash('A record can not be updated')

        session.pop('update', None)

        return redirect(url_for('baranglist'))
    else:
        return redirect(url_for('baranglist'))

@app.route('/barang/delete/<int:id>/')
def deletebarang(id):
    data = dbbrg.read(id);

    if len(data) == 0:
        return redirect(url_for('index'))
    else:
        session['delete'] = id
        return render_template('barang/delete.html', data = data)

@app.route('/deletebarangact', methods = ['POST'])
def deletebarangact():
    if request.method == 'POST' and request.form['delete']:

        if dbbrg.delete(session['delete']):
            flash('A record has been deleted')

        else:
            flash('A record can not be deleted')

        session.pop('delete', None)

        return redirect(url_for('baranglist'))
    else:
        return redirect(url_for('baranglist'))

#======================================================================
# CRUD Master Supplier
#======================================================================
@app.route('/supplier/')
def supplierlist():
    data = dbsup.read(None)

    return render_template('supplier/index.html', data = data)

@app.route('/supplier/add/')
def addsupplier():
    return render_template('supplier/add.html')

@app.route('/addsupplieract', methods = ['POST', 'GET'])
def addsupplieract():
    if request.method == 'POST' and request.form['save']:
        if dbsup.insert(request.form):
            flash("A new supplier has been added")
        else:
            flash("A new supplier can not be added")

        return redirect(url_for('supplierlist'))
    else:
        return redirect(url_for('supplierlist'))

@app.route('/supplier/update/<int:id>/')
def updatesupplier(id):
    data = dbsup.read(id);

    if len(data) == 0:
        return redirect(url_for('supplierlist'))
    else:
        session['update'] = id
        return render_template('supplier/update.html', data = data)

@app.route('/updatesupplieract', methods = ['POST'])
def updatesupplieract():
    if request.method == 'POST' and request.form['update']:

        if dbsup.update(session['update'], request.form):
            flash('A record has been updated')

        else:
            flash('A record can not be updated')

        session.pop('update', None)

        return redirect(url_for('supplierlist'))
    else:
        return redirect(url_for('supplierlist'))

@app.route('/supplier/delete/<int:id>/')
def deletesupplier(id):
    data = dbsup.read(id);

    if len(data) == 0:
        return redirect(url_for('index'))
    else:
        session['delete'] = id
        return render_template('supplier/delete.html', data = data)

@app.route('/deletesupplieract', methods = ['POST'])
def deletesupplieract():
    if request.method == 'POST' and request.form['delete']:

        if dbsup.delete(session['delete']):
            flash('A record has been deleted')

        else:
            flash('A record can not be deleted')

        session.pop('delete', None)

        return redirect(url_for('supplierlist'))
    else:
        return redirect(url_for('supplierlist'))

# ==================================================================

@app.errorhandler(404)
def page_not_found(error):
    return render_template('error.html')

if __name__ == '__main__':
    app.run(port=5000, host="127.0.0.1")