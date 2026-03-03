# ============================================================================
# Py DLC 結局
# ============================================================================

# ============================================================================
# 結局：Pythonista（Partner 結局）
# ============================================================================

label ending_py_partner:
    scene black with fade

    python hide:
        narrator("源界時間：ST 38+")
        narrator("結局：Pythonista")

    scene bg plaza with dissolve
    show py happy at center

    py "（深情地）你還記得我們第一次見面的時候嗎？"

    py "在 zen garden，你幫我整理那些石子。"

    py "那時候我就覺得... 你很特別。"

    py "（微笑）{i}Simple is better than complex.{/i}"

    py "我們的關係也是這樣。不需要複雜的東西。"

    py "只要簡潔、明確、優雅。"

    # 轉場到現實
    scene black with fade

    python hide:
        narrator("你回到了現實。")
        narrator("打開電腦，你開始寫 Python 代碼。")
        narrator("每一行代碼，都讓你想起 Py 的笑容。")
        narrator("縮排整齊，風格優雅。")
        narrator("就像她教你的那樣。")

    # 成就
    $ record_ending("py_partner", "Pythonista：人生苦短，我用 Python")

    return

# ============================================================================
# 結局：Python 之友（Close 結局）
# ============================================================================

label ending_py_friend:
    scene black with fade

    python hide:
        narrator("源界時間：ST 38+")
        narrator("結局：Python 之友")

    scene bg plaza with dissolve
    show py normal at center

    py "（微笑）時間過得真快。"

    py "你學會了很多東西。"

    py "（溫柔地）雖然我們沒有成為... 那種關係。"

    py "但你永遠是 Python 的朋友。"

    py "{i}Readability counts.{/i}"

    py "你寫的代碼，現在可讀性很高了。"

    # 轉場
    scene black with fade

    python hide:
        narrator("你回到了現實。")
        narrator("你成為了一名 Python 開發者。")
        narrator("每次寫代碼，你都會想起 Py 的教導。")
        narrator("Simple. Clear. Elegant.")

    # 成就
    $ record_ending("py_friend", "Python 之友：簡潔之美")

    return

# ============================================================================
# 輔助函數
# ============================================================================

init python:
    def record_ending(ending_id, ending_name):
        """記錄結局"""
        if not hasattr(store, 'achieved_endings'):
            store.achieved_endings = []

        if ending_id not in store.achieved_endings:
            store.achieved_endings.append(ending_id)
            narrator(f"達成結局：{ending_name}")
