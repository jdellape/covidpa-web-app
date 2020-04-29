from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
@app.route("/viz")
def show_visualizations():
    return render_template('visualization.html')


if __name__ == '__main__':
	app.run()
