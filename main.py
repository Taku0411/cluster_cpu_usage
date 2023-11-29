from flask import Flask, render_template, jsonify, request
import ssh_handler
import toml

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/hosts')
def hosts():
    toml_dict = toml.load(open("config.toml"))
    print(toml_dict)
    return jsonify(toml_dict["hosts"])


@app.route('/cpu_usage', methods=['GET'])
def cpu_usage():
    host = request.args.get('host')
    toml_dict = toml.load(open("config.toml"))
    print("log!!!!")
    print(host)
    instance = ssh_handler.ssh_login(
        str(host), toml_dict["user"], toml_dict["password"], toml_dict["command"])
    res = instance.run().replace("'", '"')
    print(res)
    return jsonify(res)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=12322)
