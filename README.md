# Potify Investment Pots — Django Starter

## Features
- User dashboard matching the requested UI
- My Pots: In Process / Completed / Canceled
- Monthly overview and investment summary
- Profile / Contact Details / KYC status
- Upcoming Events with Join buttons
- Django Admin dashboard for users, profiles, pots, events and activities
- SQLite database for development

## Run locally

```bash
python -m venv venv
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate

pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py seed_demo
python manage.py runserver
```

Open:
- User app: http://127.0.0.1:8000/
- Admin: http://127.0.0.1:8000/admin/

Demo user after `seed_demo`:
- Username: abhiram
- Password: demo12345

## Production checklist
- Change SECRET_KEY
- Set DEBUG=False
- Configure ALLOWED_HOSTS
- Use PostgreSQL/MySQL
- Configure HTTPS, secure cookies and CSRF settings
- Add real KYC provider and payment/investment compliance controls
- Never store raw Aadhaar/PAN documents without appropriate legal/security controls
