import sqlite3

def init_database():
    conn = sqlite3.connect("logistics.db")
    cursor = conn.cursor()
    
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS driver_registry (
        driver_id INTEGER PRIMARY KEY,
        driver_name TEXT NOT NULL,
        delivery_hub TEXT NOT NULL,
        vehicle_type TEXT NOT NULL
    )
    """)
    
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS shipment_logs (
        shipment_id INTEGER PRIMARY KEY,
        driver_id INTEGER,
        package_weight_kg REAL,
        delivery_time_mins REAL,
        status TEXT NOT NULL,
        FOREIGN KEY (driver_id) REFERENCES driver_registry(driver_id)
    )
    """)
    
    drivers = [
        (10, "Musa", "Riyadh Hub", "Heavy Truck"),
        (20, "Ziyad", "Jeddah Hub", "Light Van"),
        (30, "Fahad", "Dammam Hub", "Heavy Truck"),
        (40, "Sultan", "Riyadh Hub", "Light Van")
    ]
    cursor.executemany("INSERT OR IGNORE INTO driver_registry VALUES (?, ?, ?, ?)", drivers)
    
    shipments = [
        (501, 10, 450.5, 120.0, 'Delivered'),
        (502, 20, 12.2, 45.0, 'Delivered'),
        (503, 10, None, 140.0, 'Pending'),       
        (504, 30, 850.0, 980.0, 'Delivered'),     
        (505, 20, 15.0, 50.0, 'Delivered'),
        (506, 40, 95.4, 65.0, 'Pending')
    ]
    cursor.executemany("INSERT OR IGNORE INTO shipment_logs VALUES (?, ?, ?, ? , ?)", shipments)
    
    conn.commit()
    conn.close()
    print("[SUCCESS] logistics.db initialized.")

if __name__ == "__main__":
    init_database()