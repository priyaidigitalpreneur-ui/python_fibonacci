# Car Rental System (MSE800 Assessment 1)

## Developer & Course Information
- **Developer Name:** PRIYA
- **Student ID:** 270930154
- **Course:** MSE800 Professional Software Engineering
- **Institution:** Yoobee College of Creative Innovation
- **Licensing:** Open-Source Academic License

---

## Project Overview & Purpose
This application is an automated Command-line User Interface (CUI) Car Rental Management System developed in Python. It streamlines the rental process by digitizing customer registrations, vehicle inventory tracking, dynamic fee calculations based on driving safety scores, and administrative rental request management.

---

## Key Features & Technologies
- **Language:** Python 3.x
- **Data Persistence:** JSON-based persistent database storage (`database.json`) handled via Python standard libraries (`json`, `os`)
- **Object-Oriented Programming (OOP):** Encapsulation, Abstraction, Inheritance, and Polymorphism
- **Design Patterns:** Singleton Pattern (`DatabaseManager`) & Factory Method Pattern (`UserFactory`)
- **Innovation:** IoT Telematics Driver Safety Score integration with a 5% Dynamic Discount and automated maintenance lockouts

---

## Project File Structure & Explanation
- `main.py`: Primary executable source code containing business logic, CUI menus, and OOP domain models.
- `database.json`: Auto-generated database storing persistent user accounts, car inventory, and rental bookings.
- `requirements.txt`: Package dependency manifest file.
- `README.md`: User and programmer documentation covering setup, usage, and architectural details.
- `Design_and_Architecture.pdf`: Technical system documentation containing Class, Use Case, and Sequence Diagrams along with innovation architecture details.
- `Maintenance_and_Support.pdf`: Software evolution document outlining maintenance strategies, semantic versioning (`v1.0.0`), and database backward compatibility plans.

---

## Setup, Installation & How to Run
No manual database setup or external configuration is required to run this application.

1. Open a terminal or command prompt in the project root directory.
2. Verify dependency requirements:
   ```bash
   pip install -r requirements.txt