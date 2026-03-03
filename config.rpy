# ============================================================================
# CodeLove-Py-DLC - Python 語言角色 DLC
# ============================================================================
#
# 區域架構：
# - Zen Garden 是 Py 的專屬區域
# - 從廣場可以前往此區域
# - 區域內有自己的地點菜單和事件管理
# ============================================================================

# ============================================================================
# 1. DLC 配置
# ============================================================================

init python:
    # DLC 基本資訊
    py_dlc_config = {
        "id": "py_dlc",
        "name": "Python 擴展包",
        "version": "1.0.0",
        "author": "CodeLove Community",
        "description": "添加 Python 語言角色 Py 及其專屬區域 Zen Garden。",
    }

    # 註冊 DLC
    register_dlc(py_dlc_config)

# ============================================================================
# 2. 區域註冊
# ============================================================================

init python:
    def py_region_unlock_condition():
        """Py 區域的解鎖條件"""
        # 條件：完成 C_01（指標教學）後解鎖
        return store.c_01_status == "completed"

    # 註冊 Zen Garden 區域
    register_dlc_region("zen_garden", {
        "name": "Zen Garden",
        "description": "Py 的禪意花園，一個追求簡潔與優雅的地方",
        "dlc_id": "py_dlc",
        "entry_label": "enter_zen_garden",
        "unlock_condition": py_region_unlock_condition,
        "hub_bg": "bg zen_garden"
    })

# ============================================================================
# 3. 區域時間線（內部管理）
# ============================================================================

init python:
    # Py 區域內部的事件時間線
    # 這是區域自己的時間線，不和主線強制對齊
    py_region_events = {
        "PY_01": {
            "name": "縮排的藝術",
            "label": "PY_01",
            "unlock_condition": lambda: True,  # 永遠可用
            "repeatable": False
        },
        "PY_02": {
            "name": "列表推導式",
            "label": "PY_02",
            "unlock_condition": lambda: store.py_relationship in ["FRIEND", "CLOSE", "PARTNER"],
            "repeatable": False
        },
        "PY_03": {
            "name": "GIL 與並發",
            "label": "PY_03",
            "unlock_condition": lambda: store.py_relationship in ["CLOSE", "PARTNER"],
            "repeatable": False
        }
    }

    def get_available_py_events():
        """獲取當前可用的 Py 事件"""
        available = []
        for event_id, event_info in py_region_events.items():
            # 檢查解鎖條件
            if event_info["unlock_condition"]():
                # 檢查是否已完成（非可重複事件）
                status_var = f"py_{event_id.lower()}_status"
                if hasattr(store, status_var):
                    status = getattr(store, status_var)
                    if status == "completed" and not event_info["repeatable"]:
                        continue
                available.append(event_info)
        return available

# ============================================================================
# 4. 結局定義
# ============================================================================

init python:
    def py_dlc_check_ending():
        """檢查 Py DLC 結局條件"""
        if store.py_relationship == "PARTNER":
            return "ending_py_partner"
        elif store.py_relationship == "CLOSE":
            return "ending_py_friend"
        return None

    # 註冊結局檢查器
    py_dlc_config["ending_checker"] = py_dlc_check_ending

    # 結局資訊
    py_dlc_config["endings"] = {
        "ending_py_partner": {
            "name": "Pythonista：人生苦短，我用 Python",
            "condition": lambda: store.py_relationship == "PARTNER"
        },
        "ending_py_friend": {
            "name": "Python 之友：簡潔之美",
            "condition": lambda: store.py_relationship == "CLOSE"
        }
    }
