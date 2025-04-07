from typing import List, Dict, Optional

def calculate_sum(numbers: List[int]) -> int:
    """与えられた数値リストの合計を計算します。

    Args:
        numbers: 合計を計算する整数のリスト

    Returns:
        リスト内の数値の合計
    """
    return sum(numbers)

def find_user(users: List[Dict[str, str]], name: str) -> Optional[Dict[str, str]]:
    """ユーザーリストから指定された名前のユーザーを検索します。

    Args:
        users: ユーザー情報を含む辞書のリスト
        name: 検索するユーザー名

    Returns:
        ユーザーが見つかった場合はユーザー情報の辞書、見つからない場合はNone
    """
    try:
        return next((user for user in users if user["name"] == name), None)
    except KeyError:
        return None

if __name__ == "__main__":
    # 定数は上部で定義
    MAX_LIST_SIZE = 5
    ITERATION_COUNT = 100

    # ローカルスコープでデータを管理
    data = []
    
    if len(data) > MAX_LIST_SIZE:
        print("リストが最大サイズを超えています")
    
    # 効率的な文字列連結
    result = "".join(str(i) for i in range(ITERATION_COUNT))
    
    # 意味のある変数名を使用
    total_sum = calculate_sum([1, 2, 3])
    print(f"合計: {total_sum}")
