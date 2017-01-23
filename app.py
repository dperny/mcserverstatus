from flask import Flask
from flask import render_template
from mcstatus import MinecraftServer
app = Flask(__name__)

@app.route("/")
def status():
    server = MinecraftServer.lookup("vanilla-mc.dperny.net")
    try:
        status = server.status()
    except:
        status = None
    # return render_template('status.html', query=query)
    return render_template('status.html', status=status)

if __name__=='__main__':
    app.run(debug=False,host='0.0.0.0')
