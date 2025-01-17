# 🎓 **EduCourses - Flask-Based Educational Platform**

EduCourses is a comprehensive Flask-based web application designed to manage and showcase educational courses and lessons. It provides a user-friendly interface for users to register, log in, manage their profiles, and create or explore courses and lessons. The application integrates **Bootstrap** for responsive design and **SQLAlchemy** for database management, ensuring a seamless user experience.

---

## 🌟 Features

### 👤 **User Management**

- **📝 User Registration**:  
  Users can register with their first name, last name, username, email, and password. Passwords must meet specific complexity requirements.

- **🔐 User Login**:  
  Secure login with email and password validation, including a "Remember Me" option for convenience.

- **🖼️ Profile Updates**:  
  Users can update their username, email, bio, and profile picture. Validation ensures that usernames and emails are unique.

---

### 📚 **Course and Lesson Management**

- **➕ Create Courses**:  
  Users can create courses with a title, description, and an icon. Validation prevents duplicate course names.

- **📖 Create Lessons**:  
  Users can add lessons to courses, including a title, slug, content (with **CKEditor** for rich text editing), and a thumbnail image.

- **↔️ Lesson Navigation**:  
  Users can navigate between lessons within a course using "Previous" and "Next" buttons.

---

### ✅ **Enhanced Validation**

- **🔍 Custom Validators**:  
  - Ensures username and email uniqueness.
  - Enforces secure password requirements.
  - Provides dynamic course selection for lessons using `QuerySelectField`.

- **📁 File Upload Restrictions**:  
  Only specific file types (e.g., JPG, PNG) are allowed for profile pictures, course icons, and lesson thumbnails.

---

### 🎨 **Frontend Design**

- **🖥️ Bootstrap Integration**:  
  Responsive and modern design for all pages, ensuring compatibility across devices.

- **💡 Dynamic Tooltips**:  
  Interactive tooltips for navigation buttons to enhance user experience.

---

## 🆕 Recent Updates

### 📄 **Lesson Page Layout**

- Structured layout using the **Bootstrap grid system**.
- Sidebar displaying course-related information and a list of lessons.
- Dynamic navigation buttons for moving between lessons.

---

### 📝 **Form Updates**

- Refactored form classes with improved validation logic.
- Integrated `QuerySelectField` for dynamic course selection.
- Added **CKEditor** support for rich text content in lessons.

---

### 📂 **File Handling**

- Improved file validation to accept only JPG and PNG formats for images.

---

### ⚙️ **Backend Enhancements**

- Validation to prevent duplicate usernames, emails, and course titles.
- Added placeholder guidance for slug creation in lesson forms.

---

#### 🚀 Installation

### Step 1: Clone the Repository

```bash
______________________________________________________________________________________________________

git clone https://github.com/yousefxElsalahawy/EduCorses-Webstack-Portfolio-Project
cd EduCourses-Webstack-Portfolio-Project

Step 2: Create a Virtual Environment
python -m venv .venv

on mac :source .venv/bin/activate  
On Windows: .venv\Scripts\activate

Step 3: Install Dependencies
pip install -r requirements.txt


Step 4: Set Up the Database

Initialize the database:
flask db init

Create the initial migration:
flask db migrate -m "Initial migration"

Apply the migrations:
flask db upgrade

Step 5: Run the Application

$env:FLASK_APP = "app.py"
python app.py

or

flask run (with Vertial Environment)

Access the application at: http://127.0.0.1:5000.

______________________________________________________________________________________________________


🛠️ Technologies Used
Backend
🐍 Flask: Web framework.

📝 Flask-WTF: Form validation.

🔐 Flask-Login: User authentication.

📝 Flask-CKEditor: Rich text editor integration.

🗄️ SQLAlchemy: Database management.

🔒 Flask-Bcrypt: Password hashing and security.

🖼️ Pillow (PIL): Image processing.

🛠️ Werkzeug: File handling and utilities.

Frontend
🎨 Bootstrap: Responsive design and styling.

💡 Dynamic Tooltips: Interactive user interface elements.

Validation
✅ WTForms: Form handling and validation.

🔍 Custom Validators: For unique usernames, emails, and secure passwords.

🔮 Future Improvements
📄 Pagination:
Add pagination for lessons and courses to improve navigation.

🔍 Search Functionality:
Implement search functionality for users and courses.

📊 User Dashboard:
Enhance the user dashboard with analytics and personalized recommendations.

🔐 Advanced Authentication:
Integrate role-based access control (e.g., admin, instructor, student).

🎥 Video Upload Support:
Allow users to upload and stream video lessons directly on the platform.

💬 Social Features:
Add comments, ratings, and sharing options for courses and lessons.

🤝 Contributing
We welcome contributions! Please follow these steps:

Fork the repository.

Create a new branch:

git checkout -b feature-branch-name
Make your changes and commit them:


git commit -m "Description of changes"
Push to your fork:


git push origin feature-branch-name
Open a Pull Request for review.

📄 License
This project is licensed under the MIT License. See the LICENSE file for details.

______________________________________________________________________________________________________


📂 File Structure:

EduCourses-Webstack-Portfolio-Project/
├── static/
│   ├── css/              # CSS files
│   ├── js/               # JavaScript files
│   ├── images/           # Image assets
│   ├── course_icons/     # Course icons
│   ├── lesson_thumbnails/ # Lesson thumbnails
│   ├── lesson_videos/    # Lesson videos
│   └── user_pics/        # User profile pictures
├── templates/
│   ├── base.html         # Base template
│   ├── home.html         # Homepage
│   ├── register.html     # Registration page
│   ├── login.html        # Login page
│   ├── profile.html      # Profile page
│   ├── course.html       # Course page
│   ├── lesson.html       # Lesson page
│   ├── new_lesson.html   # Create new lesson page
│   ├── courses.html      # All courses page
│   └── user_lessons.html # User's lessons page
├── app.py                # Main application logic
├── forms.py              # WTForms for user and course management
├── models.py             # SQLAlchemy models for database
├── routes.py             # Application routes
├── utils.py              # Helper functions (e.g., file uploads)
├── requirements.txt      # Python dependencies
└── README.md             # Project documentation

______________________________________________________________________________________________________


🛠️ Common Issues
❌ Error: "Directory migrations already exists and is not empty"
Solution: Ignore this error if migrations have already been set up.

❌ Error: "Target database is not up to date"
Solution: Run the following command:


flask db upgrade
❌ Error: "duplicate column name"
Solution: Check the database schema for duplicate columns and adjust the migrations accordingly.

______________________________________________________________________________________________________

📞 Contact
For any questions or feedback, feel free to reach out:
📧 Email: yousefacademy2580@example.com
🌐 GitHub: yousefxElsalahawy

Developed by: yousef Elsalahawy
Version: 1.0.0
