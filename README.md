# ✨ CalcVerse

### Calculate Smarter. Explore More.

A modern, responsive multi-tool web application built with **Django**, designed to provide a collection of useful calculators and everyday utility tools in one place.

🔗 **Live Demo:** https://calcverse-cqj8.onrender.com/

---

## 🚀 Features

CalcVerse includes a growing collection of interactive tools:

### 🧮 Mathematical Calculators

- **Basic Calculator**  
  Perform everyday arithmetic operations quickly and easily.

- **Scientific Calculator**  
  Advanced mathematical calculations with scientific functions and calculation history.

- **Integration Calculator**  
  Solve mathematical integration problems by entering a function and selecting the integration type.

- **Quadratic Equation Calculator**  
  Solve quadratic equations and view calculated roots and solutions.

---

### 🛠️ Utility Tools

- **Word Counter**  
  Instantly count:
  - Words
  - Characters
  - Characters without spaces
  - Sentences
  - Paragraphs
  - Lines
  - Estimated reading time

- **Text Case Converter**  
  Convert text between different letter cases quickly.

- **Coin Toss**  
  Select your prediction, toss the coin, and get an instant result with a win/loss experience.

---

## 📱 Responsive Design

CalcVerse is designed to work across different screen sizes.

- 💻 Desktop friendly
- 📱 Mobile responsive
- 🖥️ Clean and modern interface
- ⚡ Interactive calculations
- 🎨 Consistent dark-themed UI

Special attention has been given to the **Scientific Calculator mobile layout** to ensure that users can access calculator controls comfortably on smaller screens.

---

## 🧰 Tech Stack

| Technology | Usage |
|---|---|
| **Python** | Backend programming |
| **Django** | Web framework |
| **HTML5** | Page structure |
| **CSS3** | Styling and responsive design |
| **JavaScript** | Interactive functionality |
| **Gunicorn** | Production WSGI server |
| **WhiteNoise** | Static file handling |
| **SQLite** | Development database |
| **Render** | Deployment |
| **Git & GitHub** | Version control and source hosting |

---

## 📂 Project Structure

```text
CalcVerse/
│
├── calculators/          # Main Django application
│   ├── static/           # CSS, JavaScript and other static files
│   ├── templates/        # HTML templates
│   ├── views.py          # Application views
│   ├── urls.py           # Application URLs
│   └── ...
│
├── config/               # Django project configuration
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── ...
│
├── manage.py
├── requirements.txt
└── README.md
```
---

## ⚙️ Installation & Setup

### 1. Clone the repository

```bash
git clone https://github.com/debnathsoumili782-ui/CalcVerse.git
```

### 2. Navigate to the project folder

```bash
cd CalcVerse
```

### 3. Create a virtual environment

```bash
python -m venv .venv
```

### 4. Activate the virtual environment

**Windows PowerShell:**

```powershell
.venv\Scripts\Activate.ps1
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

### 6. Run database migrations

```bash
python manage.py migrate
```

### 7. Start the development server

```bash
python manage.py runserver
```

Open the application in your browser:

```text
http://127.0.0.1:8000/
```

---

## 🌐 Deployment

The project is deployed on **Render**.

### Production Build Command

```bash
pip install -r requirements.txt && python manage.py collectstatic --noinput
```

### Production Start Command

```bash
gunicorn config.wsgi:application
```

### Environment Variables

```text
SECRET_KEY=your-secret-key
DEBUG=False
```

---

## 🔐 Security Notes

Sensitive configuration is handled using environment variables in production.

- `SECRET_KEY` should not be hard-coded in production.
- `DEBUG=False` should be used in production.
- Sensitive information should never be committed to the GitHub repository.

---

## 🎯 Project Goals

CalcVerse was built to gain practical experience in:

- Building a multi-page Django application
- Developing mathematical and utility tools
- Creating interactive user experiences
- Designing responsive layouts
- Improving mobile usability
- Working with HTML, CSS and JavaScript
- Managing a project using Git and GitHub
- Deploying a Django application to production

---

## 🔮 Future Improvements

Possible future additions include:

- More mathematical calculators
- Unit conversion tools
- Currency converter
- Dark and light theme switching
- Persistent calculation history
- User accounts
- Saved calculations
- Additional text utilities
- More interactive tools

---

## 👩‍💻 Author

**Soumili Debnath**

GitHub: https://github.com/debnathsoumili782-ui

---

## ⭐ Support

If you found this project useful or interesting, consider giving the repository a **star ⭐**.

---

<p align="center">
  Made with ❤️ using Django
</p>