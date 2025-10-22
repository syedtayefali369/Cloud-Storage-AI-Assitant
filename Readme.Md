# Cloud Storage AI Assistant

A full-stack web application that combines cloud storage management with an AI assistant. Built with Python Flask backend and modern HTML/CSS/JavaScript frontend.

## Features

### 🗂️ File Management
- **Upload Files**: Drag & drop or click to upload files
- **Download Files**: One-click download for any file
- **Delete Files**: Remove files with confirmation
- **Storage Tracking**: Visual storage usage indicator

### 🤖 AI Assistant
- **Natural Language Processing**: Ask questions about your files in plain English
- **File Information**: Get details about file sizes, types, and recent uploads
- **Personalized Responses**: AI recognizes user by name (MD TAYEF ALI)
- **Real-time Chat**: Interactive chat interface with typing indicators

### 👤 User Experience
- **Responsive Design**: Works seamlessly on desktop and mobile
- **Modern UI**: Clean, Google-inspired interface
- **Real-time Notifications**: Success and error feedback
- **Personalized Dashboard**: Welcome message and user-specific content

## Technology Stack

### Backend
- **Python 3.8+**
- **Flask** - Web framework
- **Werkzeug** - File upload security
- **OS module** - File system operations

### Frontend
- **HTML5** - Semantic markup
- **CSS3** - Modern styling with CSS Grid and Flexbox
- **JavaScript ES6+** - Interactive features
- **Fetch API** - Backend communication

## Project Structure
cloud-storage-ai-assistant/
│
├── app.py # Main Flask application
├── uploads/ # Directory for uploaded files (auto-created)
├── templates/
│ └── index.html # Main frontend template
├── README.md # Project documentation
└── requirements.txt # Python dependencies

text

### File Descriptions

- **app.py**: Main Flask application with all backend routes and logic
- **templates/index.html**: Complete frontend with HTML, CSS, and JavaScript
- **uploads/**: Directory where uploaded files are stored
- **requirements.txt**: Python package dependencies

## Installation & Setup

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)

### Step-by-Step Installation

1. **Clone or Download the Project**
   ```bash
   # Create project directory
   mkdir cloud-storage-ai-assistant
   cd cloud-storage-ai-assistant
Create Virtual Environment (Recommended)

bash
python -m venv venv

# On Windows:
venv\Scripts\activate

# On macOS/Linux:
source venv/bin/activate
Install Dependencies

bash
pip install flask werkzeug
Or create a requirements.txt file:

txt
Flask==2.3.3
Werkzeug==2.3.7
Then install:

bash
pip install -r requirements.txt
Create Project Structure

bash
mkdir templates
mkdir uploads
Add the Application Files

Save app.py in the root directory

Save index.html in the templates directory

Run the Application

bash
python app.py
Access the Application
Open your web browser and navigate to:

text
http://localhost:5000
Usage Guide
File Management
Uploading Files

Click the "Upload Files" button or the upload area

Select files from your device

Files will appear in your storage list

Downloading Files

Click the "Download" button next to any file

File will download to your default downloads folder

Deleting Files

Click the "Delete" button next to any file

Confirm the deletion in the popup

File will be permanently removed

AI Assistant
Asking Questions

Type your question in the chat input

Press Enter or click "Send"

Examples of questions you can ask:

"What files do I have?"

"What's my largest file?"

"Show me my recent files"

"How much storage do I have left?"

Personalized Interaction

The AI recognizes "MD TAYEF ALI" by name

Provides personalized responses based on your files

API Endpoints
Method	Endpoint	Description
GET	/	Serves the main application page
POST	/ai_chat	Processes AI chat messages
POST	/upload	Handles file uploads
DELETE	/delete/<file_id>	Deletes specified file
GET	/download/<file_id>	Downloads specified file
Configuration
Default Settings
Upload Folder: uploads/ (auto-created)

Max File Size: 16MB

Storage Limit: 10GB (configurable)

Port: 5000

Customization Options
You can modify these settings in app.py:

python
# Change storage limit
user_data['storage_total'] = 20  # 20GB limit

# Change upload size limit
app.config['MAX_CONTENT_LENGTH'] = 32 * 1024 * 1024  # 32MB

# Change upload folder
app.config['UPLOAD_FOLDER'] = 'my_uploads'
AI Response Customization
Edit the ai_responses dictionary in app.py to add new AI capabilities:

python
ai_responses = {
    'your keyword': 'Your custom response',
    'search files': 'I can help you search through your files. What are you looking for?',
    # Add more responses here
}
Troubleshooting
Common Issues
Port Already in Use

text
Error: That port is already in use
Solution: Kill the process using port 5000 or change the port in app.py:

python
if __name__ == '__main__':
    app.run(debug=True, port=5001)  # Use different port
Upload Fails

text
Error: Upload failed
Solution: Check file size (max 16MB) and ensure uploads directory exists

Module Not Found

text
ModuleNotFoundError: No module named 'flask'
Solution: Ensure Flask is installed: pip install flask

Permission Denied

text
PermissionError: [Errno 13] Permission denied: 'uploads/'
Solution: Create uploads directory manually or check folder permissions

Debug Mode
For development, run with debug mode enabled:

python
if __name__ == '__main__':
    app.run(debug=True)
This provides:

Automatic reloading on code changes

Detailed error messages

Debugger PIN for browser-based debugging

Browser Compatibility
✅ Chrome 90+

✅ Firefox 88+

✅ Safari 14+

✅ Edge 90+

Security Notes
File names are sanitized using secure_filename()

Maximum file size limits prevent abuse

Basic validation on all endpoints

For production use, consider adding:

User authentication

HTTPS encryption

Rate limiting

SQL database instead of in-memory storage

Future Enhancements
Potential features for future versions:

User authentication system

Database integration (SQLite/PostgreSQL)

Real AI integration (OpenAI API, etc.)

File preview functionality

File sharing capabilities

Advanced search and filtering

Mobile app version

Contributing
Fork the project

Create a feature branch

Make your changes

Test thoroughly

Submit a pull request

License
This project is open source and available under the MIT License.

Support
For questions or issues:

Check the troubleshooting section above

Review the code comments for implementation details

Create an issue in the project repository

Developed for MD TAYEF ALI 🙂

text

## Complete File Structure
```
cloud-storage-ai-assistant/
│
├── app.py # Main Flask application (backend)
├── requirements.txt # Python dependencies
├── README.md # Project documentation
│
├── uploads/ # Directory for uploaded files (auto-created)
│ ├── Project_Proposal.docx
│ ├── Financial_Report.pdf
│ └── ... (other uploaded files)
│
└── templates/ # Frontend templates
└── index.html # Main application interface
```
text

### requirements.txt
```txt
Flask==2.3.3
Werkzeug==2.3.7
```

