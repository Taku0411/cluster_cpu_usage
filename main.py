from flask import Flask, render_template, jsonify
import ssh_handler
import toml

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/hosts')
def hosts():
    toml_dict = toml.load(open("config.toml"))
    return jsonify(toml_dict["hosts"])

@app.route('/cpu_usage')
def cpu_usage():
    toml_dict = toml.load(open("config.toml"))
    print(toml_dict["command"])
    res = []
    for host in toml_dict["hosts"]:
        print(host)
        instance = ssh_handler.ssh_login(host, toml_dict["user"], toml_dict["password"], toml_dict["command"])
        aaa = instance.run()
        res.append(aaa[1:-1])
    print(res)
    return jsonify(res)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=12322)
