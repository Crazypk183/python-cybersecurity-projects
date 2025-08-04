## ⚙️ Setup Instructions

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/vulnerable-flask-app.git
   python -m venv venv
   
   Create a virtual environment (optional but recommended)
   python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

Install dependencies:
pip install -r requirements.txt

Generate the SQLite database:
python setup_db.py

Run the app:
python app.py

Default login: admin / admin123

yaml
---

### 🔁 Summary:

| File            | Push to GitHub? | Notes |
|-----------------|------------------|-------|
| `users.db`      | ❌ No            | Add to `.gitignore`, generated via script |
| `setup_db.py`   | ✅ Yes           | To generate the DB |
| `README.md`     | ✅ Yes           | Instructions to use script |
| `.gitignore`    | ✅ Yes           | To ignore `users.db` |

---

