"""
MSE800 Assessment 1 - Car Rental System
Author: PRIYA
Student ID: 270930154
"""

import json
import os
from abc import ABC, abstractmethod
from datetime import datetime


# ==========================================
# DESIGN PATTERN: SINGLETON (Database Manager)
# ==========================================
class DatabaseManager:
    _instance = None
    DB_FILE = "database.json"

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(DatabaseManager, cls).__new__(cls)
            cls._instance._init_db()
        return cls._instance

    def _init_db(self):
        # Auto-create default database if missing or empty
        if not os.path.exists(self.DB_FILE) or os.path.getsize(self.DB_FILE) == 0:
            initial_data = {
                "users": [
                    {"username": "admin", "password": "adminpassword", "role": "admin"},
                    {"username": "priya", "password": "1234password", "role": "customer"},
                    {"username": "john_doe", "password": "userpassword", "role": "customer"}
                ],
                "cars": [
                    {
                        "id": 101, "make": "Toyota", "model": "Corolla", "year": 2022,
                        "mileage": 15000, "available_now": True, "min_rent": 1, "max_rent": 14,
                        "daily_rate": 60.0, "needs_maintenance": False
                    },
                    {
                        "id": 102, "make": "Tesla", "model": "Model 3", "year": 2023,
                        "mileage": 8000, "available_now": True, "min_rent": 2, "max_rent": 30,
                        "daily_rate": 110.0, "needs_maintenance": False
                    }
                ],
                "bookings": []
            }
            self.save_data(initial_data)

    def load_data(self):
        try:
            with open(self.DB_FILE, "r") as f:
                return json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            return {"users": [], "cars": [], "bookings": []}

    def save_data(self, data):
        with open(self.DB_FILE, "w") as f:
            json.dump(data, f, indent=4)


# ==========================================
# OOP: ABSTRACTION & INHERITANCE (User System)
# ==========================================
class User(ABC):
    def __init__(self, username, password, role):
        self._username = username
        self._password = password
        self._role = role

    @property
    def username(self):
        return self._username

    def verify_password(self, password):
        return self._password == password

    @abstractmethod
    def get_role_permissions(self):
        pass


class Customer(User):
    def __init__(self, username, password):
        super().__init__(username, password, "customer")

    def get_role_permissions(self):
        return ["view_cars", "book_car", "view_my_bookings"]


class Admin(User):
    def __init__(self, username, password):
        super().__init__(username, password, "admin")

    def get_role_permissions(self):
        return ["view_cars", "manage_cars", "manage_bookings"]


# ==========================================
# DESIGN PATTERN: FACTORY METHOD
# ==========================================
class UserFactory:
    @staticmethod
    def create_user(username, password, role="customer"):
        if role.lower() == "admin":
            return Admin(username, password)
        elif role.lower() == "customer":
            return Customer(username, password)
        else:
            raise ValueError(f"Unknown user role: {role}")


# ==========================================
# DOMAIN MODEL & INNOVATION (IoT Dynamic Rate)
# ==========================================
class Car:
    def __init__(self, id, make, model, year, mileage, available_now, min_rent, max_rent, daily_rate, needs_maintenance=False):
        self.id = id
        self.make = make
        self.model = model
        self.year = year
        self.mileage = mileage
        self.available_now = available_now
        self.min_rent = min_rent
        self.max_rent = max_rent
        self.daily_rate = daily_rate
        self.needs_maintenance = needs_maintenance

    def calculate_innovative_rate(self, days, telemetry_safety_score=100):
        if self.needs_maintenance:
            raise ValueError("IoT Lockout: Vehicle requires immediate safety maintenance.")
        
        if not (0 <= telemetry_safety_score <= 100):
            raise ValueError("Telemetry safety score must be between 0 and 100.")

        base_cost = self.daily_rate * days
        # Innovation: 5% Dynamic Discount for safe drivers (Score >= 90)
        if telemetry_safety_score >= 90:
            base_cost *= 0.95
        return base_cost


# ==========================================
# MAIN APPLICATION LOGIC (CUI Interface)
# ==========================================
class CarRentalSystem:
    def __init__(self):
        self.db = DatabaseManager()
        self.current_user = None

    def start(self):
        print("\n=== Welcome to Automated Car Rental System ===")
        while True:
            if not self.current_user:
                print("\n1. Login\n2. Register\n3. Exit")
                choice = input("Select option (1-3): ").strip()
                if choice == "1":
                    self.login()
                elif choice == "2":
                    self.register()
                elif choice == "3":
                    print("Thank you for using Car Rental System!")
                    break
                else:
                    print("Error: Invalid choice. Please select 1, 2, or 3.")
            else:
                permissions = self.current_user.get_role_permissions()
                if "manage_cars" in permissions:
                    self.admin_menu()
                else:
                    self.customer_menu()

    def login(self):
        username = input("Username: ").strip()
        password = input("Password: ").strip()
        data = self.db.load_data()
        
        for u in data["users"]:
            if u["username"] == username and u["password"] == password:
                self.current_user = UserFactory.create_user(u["username"], u["password"], u["role"])
                print(f"\nSuccess: Logged in as {self.current_user.username} ({u['role'].upper()})")
                return
        print("Error: Invalid username or password.")

    def register(self):
        username = input("Choose Username: ").strip()
        password = input("Choose Password: ").strip()
        
        if not username or not password:
            print("Error: Username and Password cannot be empty.")
            return

        data = self.db.load_data()
        if any(u["username"] == username for u in data["users"]):
            print("Error: Username already exists.")
            return

        data["users"].append({"username": username, "password": password, "role": "customer"})
        self.db.save_data(data)
        print("Success: Account created successfully! Please login.")

    # ---------------- CUSTOMER WORKFLOW ----------------
    def customer_menu(self):
        print(f"\n--- Customer Menu [{self.current_user.username}] ---")
        print("1. View Available Cars\n2. Book a Car\n3. View My Bookings\n4. Logout")
        choice = input("Select option (1-4): ").strip()
        if choice == "1":
            self.view_cars()
        elif choice == "2":
            self.book_car()
        elif choice == "3":
            self.view_my_bookings()
        elif choice == "4":
            print(f"Logged out from {self.current_user.username}.")
            self.current_user = None

    def view_cars(self):
        data = self.db.load_data()
        print("\n--- Cars Inventory ---")
        for c in data["cars"]:
            status = "Available" if c["available_now"] and not c.get("needs_maintenance", False) else "Unavailable/Locked"
            print(f"ID: {c['id']} | {c['year']} {c['make']} {c['model']} | Rate: ${c['daily_rate']}/day | Status: {status}")

    def view_my_bookings(self):
        data = self.db.load_data()
        my_bookings = [b for b in data["bookings"] if b["username"] == self.current_user.username]
        
        print(f"\n--- My Bookings ({self.current_user.username}) ---")
        if not my_bookings:
            print("No bookings found.")
            return

        for b in my_bookings:
            print(f"Booking ID: {b['booking_id']} | Car ID: {b['car_id']} | Start: {b.get('start_date', 'N/A')} | Days: {b['days']} | Total: ${b['total_fee']:.2f} | Status: {b['status']}")

    def book_car(self):
        self.view_cars()
        try:
            car_id = int(input("\nEnter Car ID to book: "))
            start_date_str = input("Enter start date (YYYY-MM-DD): ").strip()
            start_date = datetime.strptime(start_date_str, "%Y-%m-%d").date()
            
            days = int(input("Enter rental duration in days: "))
            if days <= 0:
                print("Error: Rental duration must be at least 1 day.")
                return

            safety_score_input = input("Enter IoT Driving Score (0-100, default 100): ").strip()
            safety_score = int(safety_score_input) if safety_score_input else 100
        except ValueError as e:
            print(f"Error: Invalid input format ({e}).")
            return

        data = self.db.load_data()
        car_data = next((c for c in data["cars"] if c["id"] == car_id), None)

        if not car_data:
            print("Error: Selected Car ID does not exist.")
            return

        car = Car(**car_data)
        if not car.available_now:
            print("Error: Car is currently marked unavailable.")
            return

        if days < car.min_rent or days > car.max_rent:
            print(f"Error: Duration must be between {car.min_rent} and {car.max_rent} days.")
            return

        try:
            total_fee = car.calculate_innovative_rate(days, safety_score)
        except ValueError as e:
            print(f"Error: {e}")
            return

        booking = {
            "booking_id": len(data["bookings"]) + 1,
            "username": self.current_user.username,
            "car_id": car_id,
            "start_date": str(start_date),
            "days": days,
            "total_fee": round(total_fee, 2),
            "status": "PENDING"
        }
        data["bookings"].append(booking)
        self.db.save_data(data)
        print(f"\nBooking Request Submitted! Cost: ${total_fee:.2f} (Status: PENDING Admin Approval)")

    # ---------------- ADMIN WORKFLOW ----------------
    def admin_menu(self):
        print(f"\n--- Admin Menu [{self.current_user.username}] ---")
        print("1. View/Add/Manage Cars\n2. Manage Booking Requests\n3. Logout")
        choice = input("Select option (1-3): ").strip()
        if choice == "1":
            self.manage_cars()
        elif choice == "2":
            self.manage_bookings()
        elif choice == "3":
            print(f"Logged out from {self.current_user.username}.")
            self.current_user = None

    def manage_cars(self):
        print("\n1. View Cars\n2. Add New Car\n3. Delete Car\n4. Update Car Rate\n5. Toggle Maintenance Lock")
        c = input("Option: ").strip()
        data = self.db.load_data()

        if c == "1":
            self.view_cars()
        elif c == "2":
            try:
                new_id = int(input("Car ID: "))
                if any(car["id"] == new_id for car in data["cars"]):
                    print("Error: Car ID already exists.")
                    return

                make = input("Make: ").strip()
                model = input("Model: ").strip()
                year = int(input("Year: "))
                mileage = int(input("Mileage: "))
                daily_rate = float(input("Daily Rate ($): "))
                min_r = int(input("Min Rent Days: "))
                max_r = int(input("Max Rent Days: "))

                if min_r > max_r or daily_rate <= 0:
                    print("Error: Invalid Min/Max Rent or Daily Rate.")
                    return
            except ValueError:
                print("Error: Invalid numeric input.")
                return

            data["cars"].append({
                "id": new_id, "make": make, "model": model, "year": year,
                "mileage": mileage, "available_now": True, "min_rent": min_r,
                "max_rent": max_r, "daily_rate": daily_rate, "needs_maintenance": False
            })
            self.db.save_data(data)
            print("Success: New car added.")
        elif c == "3":
            try:
                car_id = int(input("Car ID to delete: "))
            except ValueError:
                print("Error: Invalid input.")
                return
            
            initial_count = len(data["cars"])
            data["cars"] = [car for car in data["cars"] if car["id"] != car_id]
            if len(data["cars"]) < initial_count:
                self.db.save_data(data)
                print("Success: Car deleted.")
            else:
                print("Error: Car ID not found.")
        elif c == "4":
            try:
                car_id = int(input("Car ID to update rate: "))
                new_rate = float(input("New Daily Rate ($): "))
                if new_rate <= 0:
                    print("Error: Rate must be positive.")
                    return
            except ValueError:
                print("Error: Invalid numeric input.")
                return
            
            found = False
            for car in data["cars"]:
                if car["id"] == car_id:
                    car["daily_rate"] = new_rate
                    found = True
                    break
            if found:
                self.db.save_data(data)
                print("Success: Rate updated.")
            else:
                print("Error: Car ID not found.")
        elif c == "5":
            try:
                car_id = int(input("Car ID to toggle maintenance: "))
            except ValueError:
                print("Error: Invalid input.")
                return
            
            found = False
            for car in data["cars"]:
                if car["id"] == car_id:
                    car["needs_maintenance"] = not car.get("needs_maintenance", False)
                    found = True
                    print(f"Success: Maintenance lock set to {car['needs_maintenance']}")
                    break
            if found:
                self.db.save_data(data)

    def manage_bookings(self):
        data = self.db.load_data()
        pending = [b for b in data["bookings"] if b["status"] == "PENDING"]

        if not pending:
            print("\nNo pending booking requests.")
            return

        print("\n--- Pending Booking Requests ---")
        for b in pending:
            print(f"Booking ID: {b['booking_id']} | User: {b['username']} | Car ID: {b['car_id']} | Start: {b.get('start_date', 'N/A')} | Days: {b['days']} | Fee: ${b['total_fee']:.2f}")

        try:
            b_id = int(input("\nEnter Booking ID to process: "))
            action = input("Approve (A) or Reject (R): ").strip().upper()
        except ValueError:
            print("Error: Invalid input.")
            return

        found = False
        for b in data["bookings"]:
            if b["booking_id"] == b_id:
                found = True
                if action == "A":
                    b["status"] = "APPROVED"
                    for c in data["cars"]:
                        if c["id"] == b["car_id"]:
                            c["available_now"] = False
                    print(f"Success: Booking ID {b_id} APPROVED.")
                elif action == "R":
                    b["status"] = "REJECTED"
                    print(f"Success: Booking ID {b_id} REJECTED.")
                else:
                    print("Error: Invalid action selected.")
                    return
                break
        
        if found:
            self.db.save_data(data)
        else:
            print("Error: Booking ID not found.")


if __name__ == "__main__":
    app = CarRentalSystem()
    app.start()