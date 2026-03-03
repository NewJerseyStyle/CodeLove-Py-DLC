# ============================================================================
# PY_01: 縮排的藝術 (The Art of Indentation)
# ============================================================================
#
# 教學重點：
# - Python 使用縮排而非大括號來定義代碼塊
# - 縮排必須一致（建議 4 空格）
# - 縮排錯誤會導致 IndentationError
#
# 場景：Zen Garden 內部
# ============================================================================

label PY_01:
    # 設置場景
    scene bg zen_garden with fade

    show py normal at center

    py "今天我們來學習 Python 最獨特的地方。"

    jump PY_01_indentation_tutorial

# ============================================================================
# 縮排教學
# ============================================================================

label PY_01_indentation_tutorial:
    py "你知道嗎？我對格式很敏感。"

    py "有些語言用大括號來標記代碼塊，但我... 不一樣。"

    py "我用的是{b}縮排{/b}。"

    # Py 展示 zen garden
    py "看看這個 zen garden。每一行石子都是對齊的。"

    py "如果有一行歪了，整個畫面就不協調了。"

    py "我的代碼也是一樣。縮排不對，我就... 會很難受。"

    # 互動：幫 Py 整理 zen garden
    py "能幫我整理一下這塊區域嗎？"

    py "把這些石子按照正確的層級排好。"

    jump PY_01_indentation_game

# ============================================================================
# 縮排小遊戲
# ============================================================================

label PY_01_indentation_game:
    python hide:
        narrator("Py 給你展示了三個區域，需要選擇正確的排列方式。")

    py "第一個：一個簡單的問候函數"

    menu:
        "選擇排列方式："

        "方式 A（無縮排）：\ndef greet():\nprint('Hello')":
            py "（皺眉）這樣... 不太對。"
            py "print 應該在 def 裡面，需要縮排。"
            $ store.py_indentation_mistakes += 1
            jump PY_01_indentation_retry_1

        "方式 B（正確縮排）：\ndef greet():\n    print('Hello')":
            py "（滿意地點頭）對！四個空格，剛剛好。"
            jump PY_01_indentation_game_2

label PY_01_indentation_retry_1:
    py "再試一次？"

    menu:
        "方式 A（無縮排）：\ndef greet():\nprint('Hello')":
            py "還是不對哦。"
            py "在 Python 裡，這樣會報 IndentationError。"
            $ store.py_indentation_mistakes += 1
            jump PY_01_indentation_game_2

        "方式 B（正確縮排）：\ndef greet():\n    print('Hello')":
            py "（開心）對了！你學得很快。"
            jump PY_01_indentation_game_2

label PY_01_indentation_game_2:
    py "第二個：帶條件的函數"

    menu:
        "選擇排列方式："

        "方式 A：\ndef check(x):\n    if x > 0:\n        return True\n    return False":
            py "（微笑）完美！兩層縮排，每層四個空格。"
            jump PY_01_indentation_game_3

        "方式 B：\ndef check(x):\nif x > 0:\nreturn True\nreturn False":
            py "（搖頭）這樣完全不行。"
            py "if 和 return 都需要在函數內部。"
            $ store.py_indentation_mistakes += 1
            jump PY_01_indentation_retry_2

label PY_01_indentation_retry_2:
    py "再想想？"

    menu:
        "方式 A（正確）：\ndef check(x):\n    if x > 0:\n        return True\n    return False":
            py "很好！你理解了。"
            jump PY_01_indentation_game_3

        "方式 B（錯誤）：\ndef check(x):\nif x > 0:\nreturn True\nreturn False":
            py "（嘆氣）還是不對。"
            py "記住：每一層代碼塊都需要縮排。"
            $ store.py_indentation_mistakes += 1
            jump PY_01_indentation_game_3

label PY_01_indentation_game_3:
    py "最後一個：混合縮排"

    py "有時候會有人混用空格和 tab..."

    py "（嚴肅地）這是{b}絕對禁止{/b}的。"

    menu:
        "你會怎麼處理這種情況？"

        "統一使用 tab":
            py "（思考）嗯... tab 也可以，但在團隊中容易出問題。"
            py "不同的編輯器可能把 tab 顯示成不同的寬度。"
            py "（微笑）但至少你保持一致了。"
            jump PY_01_complete

        "統一使用 4 空格":
            py "（開心地）這是最好的選擇！"
            py "PEP 8 建議使用 4 空格。"
            py "（溫柔地）你很細心呢。"
            $ store.py_trust += 10
            jump PY_01_complete

        "混用也可以吧？":
            py "（驚訝）不行不行！"
            py "混用空格和 tab 會導致很難發現的錯誤！"
            py "（認真地）記住：{i}Consistency matters.{/i}"
            $ store.py_indentation_mistakes += 1
            jump PY_01_complete

# ============================================================================
# 章節完成
# ============================================================================

label PY_01_complete:
    # 根據表現調整關係
    python hide:
        if store.py_indentation_mistakes == 0:
            store.py_trust += 15
            store.py_update_relationship("FRIEND")
        elif store.py_indentation_mistakes <= 2:
            store.py_trust += 5
        # 不更新關係，保持 ACQUAINTED

    py "今天的課程就到這裡！"

    if store.py_indentation_mistakes == 0:
        py "（開心地）你全對了！你真的很適合學 Python。"
        py "{i}Beautiful is better than ugly.{/i}"
        py "你寫的代碼很漂亮。"
    elif store.py_indentation_mistakes <= 2:
        py "（鼓勵地）你學得很快。繼續練習就好！"
    else:
        py "（友善地）縮排需要時間習慣。沒關係，慢慢來。"

    py "下次來的時候，我們可以學更有趣的東西。"

    py "（微笑）列表推導式。那是我最喜歡的技巧之一。"

    # 標記章節完成
    $ store.py_01_status = "completed"

    # 返回區域樞紐
    jump zen_garden_hub
