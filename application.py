from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route("/")
def index():
  return render_template('index.html')

@app.route("/save", methods=['POST'])
def save():
  source = request.form['source']
  f = open('source.py', 'w')
  f.write(source)
  f.close()
  return redirect(url_for('index'))

if __name__ == "__main__":
  app.run(host='0.0.0.0',debug=True)
