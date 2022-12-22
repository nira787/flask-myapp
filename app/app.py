#Flaskとrender_template（HTMLを表示させるための関数）をインポート
from flask import Flask,render_template
from supabase import create_client,Client
import os

url: str = os.environ.get("SUPABASE_KEY")
key: str = os.environ.get("SUPABASE_URL")

supabase: Client = create_client(url, key)

#Flaskオブジェクトの生成
app = Flask(__name__)

#「/index」へアクセスがあった場合に、「index.html」を返す
@app.route("/")
def index():
    data = "hogefuga"
    return render_template("index.html",data=data)


#おまじない
if __name__ == "__main__":
    app.run(debug=True)
