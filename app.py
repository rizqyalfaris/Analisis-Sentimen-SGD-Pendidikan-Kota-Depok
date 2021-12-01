from flask import Flask, render_template
import pandas as pd
app = Flask(__name__)

@app.route("/")
def main():
    return render_template('index.html')

@app.route("/home")
def home():
    return render_template('home.html',submenu='home')
    
@app.route("/analisis", methods=['GET','POST'])
def analisis():
    # Load dataset
    def load_data():
        data = pd.read_csv('static/hasil_label.csv')
        return data
    tweet_df = load_data()
    return render_template("analisis.html", column_names=tweet_df.columns.values, row_data=list(tweet_df.values.tolist()), zip=zip)

@app.route("/visual")
def visual():
    return render_template('visual.html',submenu='visual')

if __name__ == "__main__":
    app.run(debug = True)