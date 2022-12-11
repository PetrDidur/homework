from flask import Flask

from utlis import load_candidates, get_all, get_by_pk, get_by_skill

app = Flask(__name__)


@app.route("/")
def index():
    candidates = get_all()
    result = '<br>'
    for candidate in candidates:
        result += candidate['name'] + '<br>'
        result += candidate['position'] + '<br>'
        result += candidate['skills'] + '<br>'
        result += '<br>' + '<br>'

    return f'<pre> {result} </pre>'





@app.route('/candidate/<int:pk>')
def get_candidate(pk):
    candidate = get_by_pk(pk)
    if not candidate:
        return "Кандидиат не найден!"

    result = '<br>'
    result += candidate['name'] + '<br>'
    result += candidate['position'] + '<br>'
    result += candidate['skills'] + '<br>'
    result += '<br>'

    return f'''
        <img src = {candidate['picture']}>
        <pre> {result} </pre>
'''




@app.route('/candidate/<skill>')
def get_candidates_by_skills(skill):
    candidates = get_by_skill(skill)
    result = '<br>'
    for candidate in candidates:
        result += candidate['name'] + '<br>'
        result += candidate['position'] + '<br>'
        result += candidate['skills'] + '<br>'
        result += '<br>' + '<br>'

    return f'<pre> {result} </pre>'

if __name__ == '__main__':
  pass

  app.run(debug=True)





