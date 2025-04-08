from typing import List, Dict, Optional

def calculate_sum(numbers: List[int]) -> int:
    return sum(numbers)

def find_user(users_list: List[Dict[str, str]], name: str) -> Optional[Dict[str, str]]:
    for user in users_list:
        if user["name"] == name:
            return user
    return None

if __name__ == "__main__":
    # グローバル変数の使用を避ける
    global_data = []
    
    # マジックナンバーを定数に置き換える
    MAX_SIZE = 5
    if len(global_data) > MAX_SIZE:
        print("リストが大きすぎます")
    
    # 効率的な文字列連結
    result = "".join(str(i) for i in range(100))
    
    # 意味のある変数名
    total_sum = calculate_sum([1, 2, 3])
    print(total_sum)
