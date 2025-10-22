from flask import Flask, render_template, request, jsonify, send_from_directory
import os
from datetime import datetime
from werkzeug.utils import secure_filename

app = Flask(__name__)

# Use environment variable for secret key
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'dev-key-123')

# For Render, we need to handle file uploads differently since file system is ephemeral
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024

# Create upload directory if it doesn't exist
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

# Your existing AI responses and user data remain the same
ai_responses = {
    'list files': 'You have several files in your storage including documents, images, and archives.',
    'largest file': 'Your largest file is currently the vacation photos archive.',
    'recent files': 'Your most recent upload was the project presentation.',
    'documents': 'You have multiple document files including reports and proposals.',
    'storage': 'You have used 6.5 GB of your 10 GB storage capacity.',
    'default': "I can help you manage your cloud storage. Ask me about your files, storage usage, or help with file operations."
}

user_data = {
    'name': 'MD TAYEF ALI',
    'storage_used': 6.5,
    'storage_total': 10,
    'files': [
        {'id': 1, 'name': 'Project_Proposal.docx', 'type': 'doc', 'size': '2.4 MB', 'date': '2023-05-15'},
        {'id': 2, 'name': 'Financial_Report.pdf', 'type': 'pdf', 'size': '1.8 MB', 'date': '2023-06-22'},
        {'id': 3, 'name': 'Vacation_Photos.zip', 'type': 'zip', 'size': '145 MB', 'date': '2023-07-10'},
        {'id': 4, 'name': 'Meeting_Notes.docx', 'type': 'doc', 'size': '0.8 MB', 'date': '2023-07-18'},
        {'id': 5, 'name': 'Dashboard_Design.png', 'type': 'img', 'size': '3.2 MB', 'date': '2023-07-20'}
    ]
}

# All your routes remain exactly the same
@app.route('/')
def index():
    return render_template('index.html', user=user_data)

@app.route('/ai_chat', methods=['POST'])
def ai_chat():
    data = request.get_json()
    message = data.get('message', '').lower()
    
    response = ai_responses['default']
    for key in ai_responses:
        if key in message:
            response = ai_responses[key]
            break
    
    if 'tayef' in message or 'md' in message:
        response = f"Hello {user_data['name']}! {response}"
    
    return jsonify({'response': response})

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'error': 'No file selected'}), 400
    
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No file selected'}), 400
    
    if file:
        filename = secure_filename(file.filename)
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(file_path)
        
        file_info = {
            'id': len(user_data['files']) + 1,
            'name': filename,
            'type': filename.split('.')[-1],
            'size': f"{os.path.getsize(file_path) / (1024*1024):.1f} MB",
            'date': datetime.now().strftime('%Y-%m-%d')
        }
        user_data['files'].append(file_info)
        
        return jsonify({'message': f'File {filename} uploaded successfully', 'file': file_info})
    
    return jsonify({'error': 'Upload failed'}), 500

@app.route('/delete/<int:file_id>', methods=['DELETE'])
def delete_file(file_id):
    file_to_delete = None
    for file in user_data['files']:
        if file['id'] == file_id:
            file_to_delete = file
            break
    
    if file_to_delete:
        user_data['files'] = [f for f in user_data['files'] if f['id'] != file_id]
        
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], file_to_delete['name'])
        if os.path.exists(file_path):
            os.remove(file_path)
            
        return jsonify({'message': f'File {file_to_delete["name"]} deleted successfully'})
    
    return jsonify({'error': 'File not found'}), 404

@app.route('/download/<int:file_id>')
def download_file(file_id):
    file_to_download = None
    for file in user_data['files']:
        if file['id'] == file_id:
            file_to_download = file
            break
    
    if file_to_download:
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], file_to_download['name'])
        if os.path.exists(file_path):
            return send_from_directory(app.config['UPLOAD_FOLDER'], file_to_download['name'], as_attachment=True)
    
    return jsonify({'error': 'File not found'}), 404

# Add this for production
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)