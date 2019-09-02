from flask import render_template
from base import app,db
from forms import FAQform
from base.models import FAQ


@app.route('/', methods = ['GET' , 'POST'])
def login():
    form = FAQform()
    if form.validate_on_submit():
        Q = FAQ(question = form.Question.data, answer = form.Answer.data)
        db.session.add(Q)
        db.session.commit()
    return render_template('form.html', title='Upload', form=form)