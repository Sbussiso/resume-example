from flask import Flask, request, send_file, render_template
import os
import zipfile

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/download')
def download():
    # Path to the scripts folder and zip file
    scripts_folder = 'scripts'
    zip_path = 'scripts.zip'

    # Zip the entire scripts folder
    with zipfile.ZipFile(zip_path, 'w') as zipf:
        for root, dirs, files in os.walk(scripts_folder):
            for file in files:
                # Add file to zip, maintaining the folder structure
                zipf.write(os.path.join(root, file),
                           os.path.relpath(os.path.join(root, file),
                           os.path.join(scripts_folder, '..')))
    
    # Serve the zip file
    return send_file(zip_path, as_attachment=True)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
