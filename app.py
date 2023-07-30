from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [{
  'id': 1,
  'title': "Data Analyst",
  'location': "Philippines",
  'experience': "4 years",
}, {
  'id': 2,
  'title': "Programmer",
  'location': "Philippines",
  'experience': "4 years",
}, {
  'id': 3,
  'title': "Front End Developer",
  'location': "Remote",
}]


@app.route("/")
def hello_webint():
  return render_template('home.html', jobs=JOBS)


@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
