from flask import Flask, request, send_file, render_template
import os
import zipfile
import platform

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/download')
def download():
    # Determine the user's operating system
    user_os = platform.system()
    
    # Set the appropriate folder based on the OS
    if user_os == 'Windows':
        scripts_folder = 'windows'
    elif user_os == 'Linux':
        scripts_folder = 'linux'
    else:
        return "Unsupported OS", 400

    # Path to the zip file
    zip_path = f'{scripts_folder}.zip'

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
