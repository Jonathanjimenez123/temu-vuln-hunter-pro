from flask import Flask, request, redirect, render_template_string

app = Flask(__name__)

@app.route("/")
def index():
    return "<h1>Temu Vuln Hunter Pro</h1><p>Servidor activo.</p>"

@app.route("/redirect")
def vuln_redirect():
    url = request.args.get("url")
    if url:
        return redirect(url)
    return "Falta el parámetro 'url'", 400

@app.route("/xss")
def xss():
    payload = request.args.get("q", "")
    return render_template_string(f"<h1>PoC</h1><script>{payload}</script>")

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")


