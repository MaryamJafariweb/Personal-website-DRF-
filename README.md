
Overview
This project is a personal website API built using Django Rest Framework (DRF). It provides a structured backend to manage blog posts, portfolio projects, resume details, work experience, education history, and a contact form. This API allows easy content management for a personal website.

Features
User Authentication: Secure login and registration (if required)
Resume & Work Experience: Store and retrieve professional experiences
Education History: Manage academic background details
Portfolio Showcase: Add and display past projects
Blog System: Publish and manage blog posts
Contact Form: Store and process user inquiries
Admin Panel: Manage all data via Django admin
Technologies Used
Backend: Django, Django Rest Framework (DRF)
Database: SQLite
Version Control: Git & GitHub
Installation & Setup  
1. Clone the repository:  
   `bash
   git clone https://github.com/your-username/your-repo.git
   cd your-repo
.2 Create and activate a virtual environment:
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
.3 Install dependencies:
pip install -r requirements.txt
.4 Run migrations and start the server:
python manage.py migrate
python manage.py runserver

