# Import Drug class from drug_data.py
# (同じフォルダにある drug_data.py から Drug クラスを読み込む)
from drug_data import Drug

class Vaccine(Drug):
    """
    Represents a Vaccine, requiring specific temperature control.
    Drugクラスを継承し、温度管理機能を追加したクラス。
    """
    def __init__(self, name: str, drug_id: str, is_approved: bool, storage_temp: float) -> None:
        # Call the parent class's constructor to handle basic attributes
        # 親クラス(Drug)のコンストラクタを呼び出し、基本属性を初期化
        super().__init__(name, drug_id, is_approved)
        
        # Initialize vaccine-specific attribute
        # ワクチン固有の属性(保管温度)を初期化
        self.storage_temp = storage_temp

    def get_info(self) -> str:
        """
        Overrides the parent method to include temperature info.
        親クラスのメソッドを上書きし、温度情報を含める。
        """
        # Get basic info from parent class
        # 親クラスから基本情報を取得
        base_info = super().get_info()
        
        # Append temperature information
        # 温度情報を追加して返す
        return f"{base_info} | Storage Temp: {self.storage_temp}°C"

# --- Execution Block ---
if __name__ == "__main__":
    # Create a Vaccine instance (e.g., Pfizer/BioNTech Comirnaty)
    covid_vax = Vaccine(name="Comirnaty", drug_id="VAX-999", is_approved=True, storage_temp=-70.0)
    
    print(covid_vax.get_info())