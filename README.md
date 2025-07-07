# SIH Hackathon Project - Educational Content Management Platform

## 📋 Project Overview

This is a Django-based web application developed for the Smart India Hackathon (SIH). The platform serves as an educational content management system that facilitates file processing, user management, and content delivery for educational institutions.

## 🚀 Features

### Core Functionality
- **User Management**: Separate login systems for Students, Teachers, and Site Administrators
- **File Processing**: Support for multiple file formats including PDF, Excel (.xlsx), and BibTeX (.bib)
- **Content Management**: Chapter and topic organization system
- **File Upload System**: Secure file upload with storage management
- **RESTful API**: Django REST Framework integration for API endpoints

### User Roles
1. **Students**: Access to educational content and materials
2. **Teachers**: Content upload, chapter/topic management, and dashboard access
3. **Site Administrators**: Platform administration and oversight

### File Processing Capabilities
- **PDF Processing**: Text extraction and conversion to CSV format
- **Excel Support**: Reading and processing .xlsx files
- **BibTeX Parsing**: Academic reference processing
- **Automated CSV Generation**: Convert processed content to structured data

## 🛠️ Technology Stack

### Backend
- **Framework**: Django 5.1
- **Database**: SQLite (with dual database support)
- **API**: Django REST Framework 3.15.2
- **File Processing**: PyPDF2, pandas, bibtexparser

### Frontend
- **Templates**: Django Template System
- **Styling**: Custom CSS
- **Media Handling**: Django Static Files

### Dependencies
```
Django==5.1
djangorestframework==3.15.2
PyPDF2==3.0.1
pandas==2.2.2
bibtexparser==1.4.1
mysql-connector-python==9.0.0
gunicorn==23.0.0
```

## 📁 Project Structure

```
HPmain/
├── HPmain/                 # Main project configuration
│   ├── settings.py         # Django settings
│   ├── urls.py            # Main URL configuration
│   └── wsgi.py            # WSGI application
├── homepage/              # Landing page app
├── login_page/            # Authentication system
├── teacher/               # Teacher functionality
│   ├── models.py          # Chapter, Topic, UploadedFile models
│   ├── views.py           # Teacher dashboard, file upload
│   ├── forms.py           # File upload forms
│   └── serializers.py     # API serializers
├── student/               # Student portal
├── sadmin/                # Site administration
├── testing/               # Testing/development features
├── file_processing_test/  # File processing utilities
├── templates/             # HTML templates
├── static/               # Static files (CSS, JS)
├── media/                # User uploaded files
└── requirements.txt      # Python dependencies
```

## 🔧 Installation & Setup

### Prerequisites
- Python 3.8+
- pip (Python package manager)

### Installation Steps

1. **Clone the repository**
```bash
git clone <repository-url>
cd HPmain
```

2. **Create virtual environment** (recommended)
```bash
python -m venv venv
```

3. **Activate virtual environment**
```bash
# Windows
venv\Scripts\activate

# Linux/Mac
source venv/bin/activate
```

4. **Install dependencies**
```bash
pip install -r requirements.txt
```

5. **Database setup**
```bash
python manage.py makemigrations
python manage.py migrate
```

6. **Create superuser** (optional)
```bash
python manage.py createsuperuser
```

7. **Run development server**
```bash
python manage.py runserver
```

The application will be available at `http://localhost:8000`

## 🌐 API Endpoints

### Authentication
- `GET /login/` - Login page
- `POST /login/teachinfo/` - Teacher login processing

### Teacher Features
- `GET /teacher/teachinfo/` - Teacher dashboard
- `POST /teacher/media/upload/` - File upload endpoint
- `GET /teacher/api/chapters/` - List chapters (API)
- `POST /teacher/api/chapters/` - Create chapter (API)

### Student Features
- `GET /student/` - Student portal

### File Processing
The application supports processing of:
- PDF files → Text extraction → CSV conversion
- Excel files → Direct CSV conversion
- BibTeX files → Reference data → CSV format

## 🗃️ Database Schema

### Core Models

**Teacher Model**
- name: CharField(max_length=100)
- email: EmailField(unique=True)
- password: CharField(max_length=128)

**Student Model**
- name: CharField(max_length=100)
- email: EmailField(unique=True)
- password: CharField(max_length=128)

**Chapter Model**
- name: CharField(max_length=255)
- topics: ManyToManyField(Topic)

**Topic Model**
- topic_name: CharField(max_length=255)
- topic_doc: CharField(max_length=255)
- topic_desc: CharField(max_length=255)
- topic_time: CharField(max_length=10)

**UploadedFile Model**
- file: FileField(upload_to='HPmain/media/uploads/')
- uploaded_at: DateTimeField(auto_now_add=True)

## 🔐 Configuration

### Environment Variables
The application uses environment variables for configuration:
- `SECRET_KEY`: Django secret key
- `DEBUG`: Debug mode (True/False)
- `ALLOWED_HOSTS`: Comma-separated list of allowed hosts

### Database Configuration
- Primary Database: SQLite (`db.sqlite3`)
- Secondary Database: SQLite (`userDB.sqlite3`)
- Support for PostgreSQL (commented configuration available)

## 📚 Usage

### For Teachers
1. Access the teacher portal at `/teacher/teachinfo/`
2. Upload educational content through the file upload system
3. Organize content into chapters and topics
4. Monitor uploaded files through the dashboard

### For Students
1. Access the student portal at `/student/`
2. Browse available educational content
3. Access organized chapters and topics

### For Administrators
1. Access admin panel at `/admin/`
2. Manage users, content, and system settings

## 🧪 Testing

The project includes a testing module with video player functionality for content preview.

```bash
# Run tests
python manage.py test

# Access testing interface
http://localhost:8000/testing/
```

## 🚀 Deployment

### Production Checklist
- [ ] Set `DEBUG = False` in settings
- [ ] Configure proper `SECRET_KEY`
- [ ] Set up production database
- [ ] Configure static file serving
- [ ] Set up media file handling
- [ ] Configure allowed hosts

### Using Gunicorn
```bash
gunicorn HPmain.wsgi:application
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## 📄 License

This project was developed for the Smart India Hackathon. Please refer to the competition guidelines for usage rights.

## 👥 Team

Developed for Smart India Hackathon by [Team Name]

## 📞 Support

For support and questions, please contact the development team or refer to the project documentation.

---

**Note**: This is a hackathon project and may require additional security measures and optimizations for production use.
