#Flaskとrender_template（HTMLを表示させるための関数）をインポート
from flask import Flask,render_template
from supabase import create_client,Client
import os

url: str = os.environ.get("supabase")
key: str = os.environ.get("supabase-apikey")

supabase: Client = create_client(url, key)

def find_all_data():
    data = supabase.table("brewery").select("*").execute()
    return data


#Flaskオブジェクトの生成
app = Flask(__name__)



#「/index」へアクセスがあった場合に、「index.html」を返す
@app.route("/")
def index():
    hoge = find_all_data()
    return render_template("index.html",data=hoge)


#おまじない
if __name__ == "__main__":
    app.run(debug=True)
