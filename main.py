from drug_data import Drug
from vaccine_data import Vaccine

def main():
    # Prepare sample data of both Drug and Vaccine
    # DrugとVaccineの両方のサンプル
    inventory = [
        Drug("Aspirin", "DRUG-001", True, 10.50),
        Vaccine("Pfizer-BioNTech", "VAX-555", True, -70.0), # Price will be 0.0 (default)
        Drug("Ibuprofen", "DRUG-002", True, 8.00)
    ]

    print("--- Hospital Inventory System ---")

    for item in inventory:
        # Check if Drug and Vaccine class both have the same method
        # どちらのクラスも同じメソッドが呼べるか (Polymorphism)
        print(item.get_info())

        # Check if encapsulated data is available
        # カプセル化された値も取得できるか
        print(f"  > Price: ${item.get_price()}")

# --- Execution Block ---
if __name__ == "__main__":
    main()