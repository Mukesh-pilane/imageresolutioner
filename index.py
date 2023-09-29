from flask import Flask, request, send_file, render_template
import os

app = Flask(__name__)

# Define the folder where uploaded images will be stored
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def index():
    # Render the 'index.html' template
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    # Ensure the 'uploads' folder exists
    if not os.path.exists(app.config['UPLOAD_FOLDER']):
        os.makedirs(app.config['UPLOAD_FOLDER'])

    uploaded_file = request.files.get('file')

    if uploaded_file:
        # Save the uploaded file to the 'uploads' folder
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], uploaded_file.filename)
        uploaded_file.save(file_path)

        # You can perform additional processing here if needed.

        # Send the uploaded file back as a response
        return send_file(file_path, mimetype='image/jpeg')
    else:
        # Respond with an error if no file was uploaded
        return "No file uploaded", 400

if __name__ == '__main__':
    app.run(debug=True)
