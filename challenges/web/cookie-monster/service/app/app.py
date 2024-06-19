from flask import Flask, request, make_response, render_template, send_from_directory
import base64

app = Flask(__name__)

def set_cookie(response, key, value, secure=True, httponly=True):
    response.set_cookie(key, value, secure=secure, httponly=httponly)
    return response

@app.route('/')
def index():
    response = make_response(render_template('index.html'))
    if not request.cookies.get('admin'):
        cookie_encoded = base64.b64encode(b'false').decode('utf-8')
        response = set_cookie(response, 'admin', cookie_encoded)
    return response

@app.route('/robots.txt', methods=['GET'])
def robots_txt():
    return send_from_directory(app.static_folder, request.path[1:])

@app.route('/admin')
def admin():
    admin_status = request.cookies.get('admin')
    
    if admin_status == 'dHJ1ZQ==':
      return render_template('admin.html')
    else:
        return render_template('nonAdmin.html')

if __name__ == '__main__':
    app.run(host="0.0.0.0")
