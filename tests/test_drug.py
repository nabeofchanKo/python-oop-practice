import pytest
from drug_data import Drug
from vaccine_data import Vaccine

# Test1: Initialization and get_info works correctly?
# テスト1: 薬の初期化と情報の取得が正しくできるか？
def test_drug_initialization():
    aspirin = Drug("Aspirin", "DRUG-001", True, 10.5)
    assert aspirin.name == "Aspirin"
    assert aspirin.get_price() == 10.5
    assert "Approved" in aspirin.get_info()

# Test2: Validation works correctly?
# テスト2: カプセル化（バリデーション）が機能しているか？
def test_drug_price_validation():
    aspirin = Drug("Aspirin", "DRUG-001", True, 10.0)
    
    # Check with minus value
    # マイナスの価格を入れてみる
    aspirin.set_price(-5.0)
    
    # Check if the value remains
    # 【重要】価格が変わっていない（10.0のまま）であることを確認する
    # もしバリデーションがザルなら、ここが -5.0 になってテスト失敗する
    assert aspirin.get_price() == 10.0

# Test3: Check inheritance in Vaccine class
# テスト3: ワクチンの継承とポリモーフィズム
def test_vaccine_inheritance():
    vax = Vaccine("Comirnaty", "VAX-555", True, -70.0)
    
    # Check if methods from Parent class work
    # 親クラス(Drug)の機能が使えるか
    assert vax.name == "Comirnaty"
    
    # Check if methods from Child class work
    # 子クラス(Vaccine)独自の機能が使えるか
    assert "-70.0" in vax.get_info()