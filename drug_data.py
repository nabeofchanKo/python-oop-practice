class Drug:
    """
    Represents a pharmaceutical drug entity.
    医薬品の実体を表すクラスです。
    """

    def __init__(self, name: str, drug_id: str, is_approved: bool) -> None:
        """
        Initialize a new Drug instance.
        新しい医薬品インスタンスを初期化します。

        Args:
            name (str): The commercial or generic name of the drug. (薬品名)
            drug_id (str): Unique identifier for the drug. (薬品ID)
            is_approved (bool): Approval status by regulatory bodies like FDA/PMDA. (承認済みかどうか)
        """
        self.name = name
        self.drug_id = drug_id  # Avoid using built-in 'id'
        self.is_approved = is_approved

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

# --- Execution Block (実行ブロック) ---

if __name__ == "__main__":
    # Create instances (インスタンスの生成)
    aspirin = Drug(name="Aspirin", drug_id="DRUG-001", is_approved=True)
    new_drug = Drug(name="X-Compound", drug_id="EXP-999", is_approved=False)

    # Output results (結果の出力)
    print(aspirin.get_info())
    print(new_drug.get_info())