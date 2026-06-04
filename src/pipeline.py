import pandas as pd
import sqlite3

def extract_and_clean_logistics(db_path):
    conn = sqlite3.connect(db_path)
    query = """
    SELECT 
        dr.driver_name,
        dr.delivery_hub,
        sl.package_weight_kg,
        sl.delivery_time_mins,
        sl.status
    FROM driver_registry dr
    INNER JOIN shipment_logs sl
    ON dr.driver_id = sl.driver_id;
    """
    logistic_df = pd.read_sql_query(query, conn)
    package_weight_kg_median = logistic_df["package_weight_kg"].median()
    logistic_df["package_weight_kg"] = logistic_df["package_weight_kg"].fillna(package_weight_kg_median)
    conn.close()
    return logistic_df

if __name__ == "__main__":
    print("[INFO] Running ETL Pipeline...")
    print(extract_and_clean_logistics("logistics.db"))