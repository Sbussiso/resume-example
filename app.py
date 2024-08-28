from flask import Flask, request, send_file, render_template
import os

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/download')
def download():
    # Path to the install folder ZIP file
    zip_path = os.path.join('scripts', 'install.zip')
    
    # Serve the install.zip file
    return send_file(zip_path, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
