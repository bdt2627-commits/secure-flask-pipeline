from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return """
    <html>
        <head>
            <title>DevSecOps Portfolio</title>
            <style>
                body { font-family: Arial, sans-serif; text-align: center; background-color: #f4f4f4; padding: 50px; }
                .container { background: white; padding: 30px; border-radius: 15px; box-shadow: 0px 0px 20px rgba(0,0,0,0.1); display: inline-block; }
                h1 { color: #2c3e50; }
                p { color: #7f8c8d; }
                .status { color: #27ae60; font-weight: bold; border: 2px solid #27ae60; padding: 10px; border-radius: 5px; display: inline-block; }
            </style>
        </head>
        <body>
            <div class="container">
                <h1>🛡️ My Professional DevSecOps Pipeline</h1>
                <p>Welcome! This application was built with a fully automated security pipeline.</p>
                <div class="status">✅ Security Scan: Passed</div>
                <p style="margin-top:20px;">Built by a Future DevSecOps Expert</p>
            </div>
        </body>
    </html>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)