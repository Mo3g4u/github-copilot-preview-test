def calculate_sum(l):
    s = 0
    for i in range(len(l)):
        s = s + l[i]
    return s

def find_user(users_list, name):
    try:
        for i in range(len(users_list)):
            if users_list[i]["name"] == name:
                return users_list[i]
    except:
        pass
    return None

if __name__ == "__main__":
    # グローバル変数の使用
    GLOBAL_DATA = []
    
    # マジックナンバーの使用
    if len(GLOBAL_DATA) > 5:
        print("リストが大きすぎます")
    
    # 非効率な文字列連結
    result = ""
    for i in range(100):
        result = result + str(i)
    
    # 意味のない変数名
    x = calculate_sum([1, 2, 3])
    print(x)
