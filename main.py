from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from datetime import datetime, timedelta

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

# Simulated session
user_session = {"logged_in": False, "email": None}

# Participants with simulated availability
participants = {"Alice": [], "Bob": [], "Charlie": []}

# Initialize next 3 days with free slots
today = datetime.today()
for i in range(3):
    day = (today + timedelta(days=i)).strftime("%Y-%m-%d")
    for start_hour in ["09:00", "10:00", "11:00", "14:00", "15:00"]:
        end_hour = str(int(start_hour[:2]) + 1).zfill(2) + ":00"
        for p in participants:
            participants[p].append((day, start_hour, end_hour))

# Booked meetings
booked_meetings = []

# Generate smart slots with priority
def generate_smart_slots():
    slots = []
    for i in range(3):
        day = (today + timedelta(days=i)).strftime("%Y-%m-%d")
        for start_hour in ["09:00", "10:00", "11:00", "14:00", "15:00"]:
            end_hour = str(int(start_hour[:2]) + 1).zfill(2) + ":00"
            count_available = sum(
                1 for p in participants.values() if (day, start_hour, end_hour) in p
            )
            score = count_available + (2 if start_hour < "12:00" else 0)
            if any(b["start"] == start_hour and b["date"] == day for b in booked_meetings):
                continue
            slots.append({"date": day, "start": start_hour, "end": end_hour, "score": score})
    return sorted(slots, key=lambda x: (x["date"], -x["score"]))

# Home page
@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    if not user_session["logged_in"]:
        return templates.TemplateResponse("index.html", {
            "request": request,
            "auth_url": "/login",
            "slots": [],
            "booked": [],
            "message": None
        })
    slots = generate_smart_slots()
    return templates.TemplateResponse("index.html", {
        "request": request,
        "auth_url": None,
        "slots": slots,
        "booked": booked_meetings,
        "message": f"Logged in as {user_session['email']}"
    })

# Login form
@app.get("/login", response_class=HTMLResponse)
def login_form(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})

# Login submission
@app.post("/login", response_class=RedirectResponse)
def login_submit(email: str = Form(...)):
    user_session["logged_in"] = True
    user_session["email"] = email
    return RedirectResponse("/", status_code=303)

# Logout
@app.post("/logout")
def logout():
    user_session["logged_in"] = False
    user_session["email"] = None
    return RedirectResponse("/", status_code=303)

# Book a meeting
@app.post("/book", response_class=HTMLResponse)
def book(request: Request, date: str = Form(...), start: str = Form(...), end: str = Form(...)):
    booked_meetings.append({"date": date, "start": start, "end": end, "email": user_session["email"]})
    print(f"[Simulated Email] Meeting booked for {user_session['email']} on {date} from {start} to {end}")
    slots = generate_smart_slots()
    return templates.TemplateResponse("index.html", {
        "request": request,
        "auth_url": None,
        "slots": slots,
        "booked": booked_meetings,
        "message": f"Meeting booked on {date} from {start} to {end}. Email sent!"
    })