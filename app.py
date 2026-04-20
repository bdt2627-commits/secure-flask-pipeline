from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "<html><body><h1 style='color:blue; text-align:center;'>🛡️ DevSecOps Project Live!</h1><p style='text-align:center;'>Build by Binty Tandel</p></body></html>"

if __name__ == '__main__':
    
    app.run(host='127.0.0.1', port=5000, debug=True)