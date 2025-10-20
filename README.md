# 🎓 EduManage

EduManage is a **Django-based college management system** that allows you to manage **students** and **courses** efficiently. It provides a clean, responsive, and modern UI for viewing, adding, and editing records.

---

## ✨ Features

### 🧑‍🎓 Student Management
- Add, edit, and delete students
- Upload student images
- Assign multiple courses to a student
- Display students in a **card layout** with courses as badges

### 📚 Course Management
- Add, edit, and delete courses
- Display courses in a list or card layout

### 🎨 UI & UX
- Fully **responsive design** using CSS Flexbox
- Consistent color theme and hover effects
- **Badges** for courses in student cards
- Neatly aligned checkboxes in forms

---

## 🗂 Project Structure

```
EduManage/
├── collage/                    # Main project folder
│   ├── settings.py
│   ├── urls.py
│   ├── templates/
│   │   └── home.html
│   └── static/
│       └── css/
├── course/                     # Course app
│   ├── models.py
│   ├── views.py
│   ├── templates/
│   │   ├── course_form_manual.html
│   │   └── course_list.html
│   └── static/
│       └── css/
│           └── course.css
├── student/                    # Student app
│   ├── models.py
│   ├── views.py
│   ├── templates/
│   │   ├── student_form.html
│   │   └── student_list.html
│   └── static/
│       └── css/
│           └── student.css
├── media/                      # User uploaded files
├── db.sqlite3                  # SQLite database
├── manage.py
├── Pipfile
└── Pipfile.lock
```

---

## ⚡ Tech Stack

**Backend:**
- Python 3.13
- Django 4.x

**Frontend:**
- HTML5
- CSS3 (Flexbox)
- Django Templates

**Database:**
- SQLite

**Other:**
- Pillow (Image handling)
- Pipenv (Environment management)

---

## 🛠 Setup Instructions

Follow these steps to set up the EduManage project locally:

### 1. Install Pipenv

If you don't have Pipenv installed:

```bash
pip install pipenv
```

### 2. Clone the Repository

```bash
git clone <your-repo-url>
cd EduManage
```

### 3. Create and Activate Virtual Environment

```bash
pipenv shell
```

### 4. Install Dependencies

```bash
pipenv install django pillow
```

### 5. Apply Database Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 6. Create a Superuser (Optional)

For admin panel access:

```bash
python manage.py createsuperuser
```

Follow the prompts to set username, email, and password.

### 7. Run the Development Server

```bash
python manage.py runserver
```

### 8. Access the Application

Open your browser and navigate to:

```
http://127.0.0.1:8000/
```

**Admin Panel:**

```
http://127.0.0.1:8000/admin/
```

---

## 💡 Usage Guide

1. **Navigate to Students** - View, add, edit, or delete students
2. **Navigate to Courses** - Manage all available courses
3. **Assign Courses** - Use checkboxes to assign multiple courses to students
4. **View Cards** - Courses display as colorful badges on student cards

---

## 📌 Important Configuration

### Media Files Setup

Ensure these settings are in your `settings.py` for image uploads:

```python
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'
```

### URL Configuration

Add this to your main `urls.py`:

```python
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # your url patterns
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```

### Static Files (Production)

For production deployment, collect static files:

```bash
python manage.py collectstatic
```

---

## 🔄 Working on the Project Later

Whenever you return to work on the project:

```bash
cd EduManage
pipenv shell
python manage.py runserver
```

To deactivate the virtual environment:

```bash
exit
```

---

## 🐛 Troubleshooting

**Problem:** `ModuleNotFoundError: No module named 'PIL'`  
**Solution:** Run `pipenv install pillow`

**Problem:** Images not displaying  
**Solution:** Check MEDIA_URL and MEDIA_ROOT settings in `settings.py`

**Problem:** Static files not loading  
**Solution:** Run `python manage.py collectstatic`

**Problem:** Database errors  
**Solution:** Delete `db.sqlite3` and run migrations again

**Problem:** Port already in use  
**Solution:** Run `python manage.py runserver 8001` (use a different port)

---

## 📚 Future Enhancements

- [ ] Add user authentication and role-based access
- [ ] Implement attendance tracking
- [ ] Add grade management system
- [ ] Export student/course data to CSV/PDF
- [ ] Add search and filter functionality
- [ ] Implement email notifications
- [ ] Add pagination for large datasets
- [ ] Create dashboard with statistics

---

## 📄 License

This project is open-source and available for educational purposes.

---

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

**Steps to contribute:**

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## ❤️ Acknowledgements

- Built with **Django** - The web framework for perfectionists with deadlines
- Styled with modern **CSS3** techniques
- Inspired by educational management systems

---

## 📧 Contact

For questions or suggestions, please open an issue on GitHub.

---

**Made with ❤️ for educational purposes**