from flask import Flask, render_template, request

app = Flask(__name__)
# from netaddr import *

@app.route('/')
def vpnbldr():
    return render_template('vpnbldr.html')

@app.route('/vpnbldr_results')
def vpnbldr_results():
    asideip = request.args.get('asideip')
    asidevrf = request.args.get('asidevrf')
    asidesite = request.args.get('asidesite')
    psk = request.args.get('psk')
    zsideip = request.args.get('zsideip')
    zsidevrf = request.args.get('zsidevrf')
    zsidesite = request.args.get('zsidesite')
    tunnumb = request.args.get('tunnumb')

    return render_template('vpnbldr_results.html',
        asideip=asideip,
        asidevrf=asidevrf,
        asidesite=asidesite,
        psk=psk,
        zsideip=zsideip,
        zsidevrf=zsidevrf,
        zsidesite=zsidesite,
        tunnumb=tunnumb)


if __name__ == '__main__':
    app.run(host='0.0.0.0')
