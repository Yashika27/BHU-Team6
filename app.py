from flask import Flask, render_template, request
from forms import AddFilterForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'IITBHU_Team6'

@app.route('/')
def filters():
    form = AddFilterForm()
    if form.is_submitted():
        result = request.form
        return render_template('addFilter.html', result = result)
    return render_template('addFilter.html', form = form )