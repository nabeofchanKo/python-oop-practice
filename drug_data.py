class Drug:
    """
    Represents a pharmaceutical drug entity.
    医薬品の実体を表すクラスです。
    """

    def __init__(self, name: str, drug_id: str, is_approved: bool, price: float = 0.0) -> None:
        """
        Initialize a new Drug instance.
        新しい医薬品インスタンスを初期化します。

        Args:
            name (str): The commercial or generic name of the drug. (薬品名)
            drug_id (str): Unique identifier for the drug. (薬品ID)
            is_approved (bool): Approval status by regulatory bodies like FDA/PMDA. (承認済みかどうか)
            price (float): Price of the drug. (薬価)
        """
        self.name = name
        self.drug_id = drug_id  # Avoid using built-in 'id'
        self.is_approved = is_approved
        self.__price = price

    def get_info(self) -> str:
        """
        Returns a formatted string containing drug details.
        薬品の詳細情報を含むフォーマット済み文字列を返します。
        
        Returns:
            str: Formatted string like "[ID] Name : Status"
        """
        # Determine status string based on approval flag
        # 承認フラグに基づいてステータス文字列を決定
        status = "Approved" if self.is_approved else "Experimental"
        
        return f"[{self.drug_id}] {self.name} : {status}"
    
def get_price(self) -> float:
        """
        Returns the private attribute 'price'.
        プライベート属性である薬価を返します。
        """
        # Just return price
        return self.__price
    
def set_price(self, new_price: float) -> None:
    """
    Sets a new value to the private attribute 'price'.
    薬価のプライベート属性に新しい値を設定します。
    """
    # Show an error if new_price < 0
    # 0未満（マイナス）なら警告
    if new_price < 0:
        print("Error: Price cannot be negative.")
    else:
        self.__price = new_price

# --- Execution Block (実行ブロック) ---

if __name__ == "__main__":
    aspirin = Drug("Aspirin", "DRUG-001", True, 10.50)
    
    # テスト1: 正しく価格が取れるか？
    print(f"Price: ${aspirin.get_price()}")
    
    # テスト2: 外部から無理やり書き換えようとしてエラーになるか？
    # print(aspirin.__price) # <- これのコメントを外して実行するとエラーになるはず（確認用）

    # テスト3: Setterを使って正しい値をセット
    aspirin.set_price(12.00)
    print(f"New Price: ${aspirin.get_price()}")

    # テスト4: 不正な値（マイナス）を弾くか？
    aspirin.set_price(-5.00)
    print(f"After invalid set: ${aspirin.get_price()}")