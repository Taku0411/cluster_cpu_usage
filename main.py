from flask import Flask, render_template, jsonify
import ssh_handler

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/cpu_usage')
def cpu_usage():
    host_prefix = ""
    user = "hoge"
    password = "pass"
    command = "aaaa"
    hosts = [f"{host_prefix}_{str(i)}" for i in range(1,3)]
    res = []
    for host in hosts:
        print(host)
        instance = ssh_handler.ssh_login(host, user, password, command)
        aaa = instance.run()
        res.append(aaa)
    print(res)
    return jsonify(res)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=12322)
