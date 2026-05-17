# OPEN_ENDED_LAB-07

# NexaStudio 🚀

A modern digital agency website built with **Flask** and vanilla HTML/CSS. NexaStudio showcases services, a project gallery, team information, and includes a full contact and authentication flow.

---

## Pages

| Route | Page | Description |
|-------|------|-------------|
| `/` | Home | Hero section, stats, services overview, CTA |
| `/about` | About | Company story and team members |
| `/services` | Services | Service cards with pricing |
| `/gallery` | Gallery | Project portfolio grid |
| `/contact` | Contact | Contact form with info panel |
| `/login` | Login | User sign-in form |
| `/register` | Register | New account creation form |

---

## Project Structure

```
nexastudio/
├── app.py                  # Flask application & routes
├── requirements.txt        # Python dependencies
├── templates/
│   ├── index.html
│   ├── about.html
│   ├── services.html
│   ├── gallery.html
│   ├── contact.html
│   ├── login.html
│   └── register.html
└── static/
    └── css/
        ├── style.css       # Global styles & navbar
        ├── home.css
        ├── about.css
        ├── services.css
        ├── gallery.css
        ├── contact.css
        └── auth.css
```

---

## Getting Started

### Prerequisites

- Python 3.8+
- pip

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/nexastudio.git
   cd nexastudio
   ```

2. **Create and activate a virtual environment**
   ```bash
   python -m venv venv

   # Windows
   venv\Scripts\activate

   # macOS / Linux
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the development server**
   ```bash
   python app.py
   ```

5. Open your browser and navigate to `http://127.0.0.1:5000`

---

## Tech Stack

- **Backend:** Python, Flask
- **Frontend:** HTML5, CSS3 (vanilla)
- **Templating:** Jinja2
- **Styling:** Custom CSS with CSS Grid & Flexbox

---

## Features

- Responsive design — works on desktop, tablet, and mobile
- Flash messages for form feedback (contact, login, register)
- Smooth hover animations on cards and gallery items
- 404 error handler redirects to home

---

## Authors

- Hussain Alam Mirza (035)
- M. Ahsan Abid (040)
- Zunaira Arshad (029)
- Unaiza Rehman (024)

---

## License

This project is for educational purposes.
