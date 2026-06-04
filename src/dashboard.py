import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from pipeline import extract_and_clean_logistics

def generate_performance_dashboard(db_path):
    df = extract_and_clean_logistics(db_path)
    
    sns.set_theme(style="whitegrid")
    plt.figure(figsize=(8, 4))
    
    # Building our statistical box plot
    sns.boxplot(data=df, x="delivery_time_mins", color="coral", flierprops={"markerfacecolor":"red", "marker":"D"})
    
    plt.title("LogiTrack Distribution Audit: Delivery Cycle Bottlenecks", fontsize=12, fontweight='bold')
    plt.xlabel("Delivery Duration (Minutes)", fontsize=10)
    
    # Save the output directly to your folder automatically!
    plt.savefig("delivery_bottlenecks.png", dpi=300, bbox_inches='tight')
    print("[SUCCESS] Dashboard chart exported as 'delivery_bottlenecks.png'.")
    plt.close()

if __name__ == "__main__":
    generate_performance_dashboard("logistics.db")