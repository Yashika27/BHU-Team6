from flask import Flask, render_template, request
from forms import AddFilterForm
from graph import func

app = Flask(__name__)
app.config['SECRET_KEY'] = 'IITBHU_Team6'

@app.route('/')
def filters():
    form = AddFilterForm()
    # if form.is_submitted():
    #     result = request.form
    #     return render_template('addFilter.html', result = result)
    return render_template('addFilter.html', form = form )

@app.route('/handle_data', methods=['POST'])
def handle_data():
    fsymbol  = request.form['fsymbol']
    charttype = request.form['charttype']
    print(fsymbol, charttype, type(charttype))
    func(fsymbol, charttype)
    return render_template('show_graph.html' )

if __name__=="__main__":
    app.run(debug=True)

