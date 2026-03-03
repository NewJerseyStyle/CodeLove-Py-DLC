# ============================================================================
# Py (Python) - 角色定義
# ============================================================================
#
# Python 語言特性映射：
# - 動態型別：Py 不要求事先定義型別，但她會「感覺」到型別不合適
# - 縮排語法：Py 對格式非常敏感，混亂的格式會讓她不適
# - GIL：Py 可以同時做很多事，但某個時刻只能專注一件事
# - Zen of Python：Py 追求簡潔、優雅、明確
# - "Batteries included"：Py 總是帶著很多工具
# ============================================================================

# ============================================================================
# 1. 角色定義
# ============================================================================

define py = Character(
    "Py",                  # 顯示名稱
    color="#3776AB",       # Python 官方藍色
    what_prefix="「",
    what_suffix="」"
)

# ============================================================================
# 2. 角色關係變量
# ============================================================================

# 關係狀態進程
# UNMET → ACQUAINTED → FRIEND → CLOSE → PARTNER
default py_relationship = "UNMET"

# 角色專用變量
default py_trust = 0              # 信任度 (0-100)
default py_unlocked = False       # 是否解鎖
default py_indentation_mistakes = 0  # 縮排錯誤計數

# 章節狀態
default py_01_status = "unlocked"   # PY_01: 縮排與格式
default py_02_status = "locked"     # PY_02: 列表推導式
default py_03_status = "locked"     # PY_03: GIL 與並發

# ============================================================================
# 3. 角色語言特性
# ============================================================================

init python:
    py_traits = {
        "language": "Python",
        "has_gc": True,                 # 有垃圾回收
        "strong_typing": False,         # 動態型別
        "memory_safety": True,          # 記憶體安全
        "concurrency_model": "gil",     # GIL 並發模型
        "execution_speed": "moderate",  # 中等執行速度
        "learning_curve": "easy",       # 學習曲線平緩

        # 角色性格特點
        "personality": {
            "formal": False,            # 不拘小節
            "helpful": True,            # 非常樂於助人
            "cautious": False,          # 不謹慎（動態型別）
            "efficient": True,          # 追求簡潔效率
            "zen": True,                # 追求禪意
        },

        # Python 特殊特性
        "special": {
            "indentation_sensitive": True,  # 縮排敏感
            "batteries_included": True,     # 自帶豐富標準庫
            "duck_typing": True,            # 鴨子型別
            "list_comprehension": True,     # 列表推導式
        }
    }

    # 註冊角色到 DLC 系統
    register_dlc_character("py", {
        "name": "Py",
        "color": "#3776AB",
        "language": "Python",
        "traits": py_traits,
        "relationship_states": ["UNMET", "ACQUAINTED", "FRIEND", "CLOSE", "PARTNER"]
    })

# ============================================================================
# 4. 角色專用函數
# ============================================================================

init python:
    def py_update_relationship(new_state):
        """更新 Py 的關係狀態"""
        old_state = store.py_relationship
        store.py_relationship = new_state

        if old_state != new_state:
            if new_state == "FRIEND":
                store.py_trust += 20
                # 解鎖 PY_02
                store.py_02_status = "unlocked"
            elif new_state == "CLOSE":
                store.py_trust += 30
                # 解鎖 PY_03
                store.py_03_status = "unlocked"
            elif new_state == "PARTNER":
                store.py_trust = 100

    def py_can_interact():
        """檢查是否可以與 Py 互動"""
        return (
            store.py_unlocked and
            store.py_relationship != "UNMET"
        )

    def py_check_indentation(code_text):
        """檢查縮排是否正確（遊戲化版本）"""
        # 簡化的縮排檢查邏輯
        lines = code_text.split('\n')
        indent_stack = [0]

        for line in lines:
            if line.strip() == '':
                continue

            # 計算縮排
            indent = len(line) - len(line.lstrip())

            # 檢查是否為 4 的倍數
            if indent % 4 != 0:
                return False, "縮排必須是 4 的倍數"

            # 檢查縮排層級是否合理
            if indent > indent_stack[-1] + 4:
                return False, "縮排跳躍過大"

            # 更新縮排堆疊
            if indent > indent_stack[-1]:
                indent_stack.append(indent)
            elif indent < indent_stack[-1]:
                while indent_stack and indent_stack[-1] > indent:
                    indent_stack.pop()

        return True, "縮排正確"

# ============================================================================
# 5. 角色登場條件
# ============================================================================

init python:
    def py_unlock_condition():
        """
        Py 的解鎖條件

        返回: True 如果角色應該解鎖
        """
        # 條件：完成 C_01（指標教學）後，玩家在 ST_05+ 會在資訊廣場遇到 Py
        return (
            store.c_01_status == "completed" and
            store.source_time >= 5
        )

# ============================================================================
# 6. 角色對話風格
# ============================================================================

# Py 的對話風格：
# - 友善、熱情、樂於助人
# - 喜歡用簡潔的方式解決問題
# - 會引用 Zen of Python 的格言
# - 對格式問題很敏感（縮排）
# - 不喜歡繁瑣的東西

# 對話示例：
#
# if py_relationship == "UNMET":
#     py "（友善地微笑）你好！我是 Py。你看上去需要幫助？"
# elif py_relationship == "ACQUAINTED":
#     py "又見面了！有什麼想學的嗎？我這裡有很多工具哦。"
# elif py_relationship == "FRIEND":
#     py "（開心地）你來啦！今天我們來學點有趣的東西吧。"
# elif py_relationship == "CLOSE":
#     py "（溫柔地）和你一起寫代碼的時光，是我最喜歡的時光。"
# elif py_relationship == "PARTNER":
#     py "（深情地）Simple is better than complex. 就像我們的關係一樣。"
