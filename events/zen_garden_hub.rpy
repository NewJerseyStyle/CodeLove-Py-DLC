# ============================================================================
# Zen Garden 區域入口和樞紐
# ============================================================================
#
# 這是 Py DLC 的區域入口點。玩家從廣場選擇「前往其他區域」→「Zen Garden」
# 後會來到這裡。區域內有自己的地點菜單。
# ============================================================================

# ============================================================================
# 區域入口
# ============================================================================

label enter_zen_garden:
    scene bg zen_garden with fade

    python hide:
        narrator("你來到了 Zen Garden。")
        narrator("這裡的一切都井然有序，石子排列成完美的幾何圖案。")

    # 首次進入時的特殊對話
    if not store.py_unlocked:
        jump py_first_encounter

    # 否則顯示區域菜單
    jump zen_garden_hub

# ============================================================================
# 首次相遇
# ============================================================================

label py_first_encounter:
    show py normal at center with dissolve

    py "（友善地微笑）哦？有客人？"

    py "我是 Py。我在這裡照顧這個 zen garden。"

    py "你看起來是從外面來的。歡迎來到我的小花園。"

    py "（指著周圍）這裡的一切都遵循一個原則：{i}Simple is better than complex.{/i}"

    # 解鎖 Py
    $ store.py_unlocked = True
    $ store.py_relationship = "ACQUAINTED"

    py "如果你有興趣，我可以教你一些東西。"

    jump zen_garden_hub

# ============================================================================
# 區域樞紐菜單
# ============================================================================

label zen_garden_hub:
    scene bg zen_garden

    # 檢查 Py 是否在
    if store.py_relationship == "UNMET":
        narrator "Zen Garden 很安靜，Py 似乎不在這裡。"
        menu:
            "返回廣場":
                jump return_to_plaza
    else:
        show py normal at center

    python hide:
        st = store.source_time
        day_count = int(st // 15) + 1
        narrator(f"【第 {day_count} 天 · Zen Garden】")

    # 顯示關係狀態
    if store.py_relationship == "PARTNER":
        py "（深情地）你又來了。我一直在等你。"
    elif store.py_relationship == "CLOSE":
        py "（溫柔地）歡迎回來。今天想學什麼？"
    elif store.py_relationship == "FRIEND":
        py "（開心地）你來啦！今天我們來做點有趣的事。"
    else:
        py "（友善地）需要幫助嗎？"

    # 獲取可用事件
    $ available_events = get_available_py_events()
    $ has_events = len(available_events) > 0

    menu:
        "和 Py 學習" if has_events:
            jump py_event_menu

        "和 Py 聊天":
            jump py_chat

        "在花園裡散步":
            jump zen_garden_walk

        "返回廣場":
            jump return_to_plaza

# ============================================================================
# 事件選擇菜單
# ============================================================================

label py_event_menu:
    python hide:
        # 構建事件選項
        # 注意：Ren'Py 的 renpy.display_menu() 不支持空白縮排
        # 使用全角空格 (U+3000) 模擬縮排效果
        choices = []
        for event in available_events:
            choices.append((u"　" + event["name"], event["label"]))

        choices.append((u"　返回", "back"))

        selection = renpy.display_menu(choices)

        if selection == "back":
            renpy.jump("zen_garden_hub")
        else:
            renpy.jump(selection)

# ============================================================================
# 和 Py 聊天
# ============================================================================

label py_chat:
    show py normal at center

    # 根據關係狀態顯示不同對話
    if store.py_relationship == "PARTNER":
        py "（深情地）你知道嗎？和你在一起的時光，是我最珍惜的。"
        py "{i}Beautiful is better than ugly.{/i}"
        py "你讓我的代碼變得更美。"

    elif store.py_relationship == "CLOSE":
        py "（微笑）每次和你聊天，我都能學到新東西。"
        py "你看待問題的方式很獨特。"

    elif store.py_relationship == "FRIEND":
        py "（開心地）聊天是最棒的休息方式！"
        py "你知道嗎？Python 有一首詩叫 The Zen of Python。"
        py "{i}Readability counts.{/i}"

    else:
        py "（友善地）你想了解什麼？"
        py "我可以告訴你關於 Python 的任何事情。"

    menu:
        "關於 Zen of Python":
            py "（微笑）The Zen of Python, by Tim Peters..."
            py "{i}Beautiful is better than ugly.{/i}"
            py "{i}Explicit is better than implicit.{/i}"
            py "{i}Simple is better than complex.{/i}"
            py "這些原則指引著我的生活。"
            jump py_chat

        "關於其他語言":
            py "（思考）每個語言都有自己的特點。"
            py "Cee 很快，但需要小心。"
            py "Jawa 很穩定，但有時候太繁瑣。"
            py "我呢？我追求簡潔和優雅。"
            jump py_chat

        "結束對話":
            py "好的，有空的時候再來找我。"
            jump zen_garden_hub

# ============================================================================
# 在花園散步
# ============================================================================

label zen_garden_walk:
    narrator "你在 Zen Garden 裡散步，欣賞著整齊排列的石子。"

    python hide:
        # 隨機生成一些觀察
        import random
        observations = [
            "你注意到每一行石子都完美對齊，就像正確縮排的代碼。",
            "花園中央有一個小池塘，水面平靜如鏡。",
            "一陣微風吹過，帶來淡淡的花香。",
            "你看到一塊石碑上刻著：Simple is better than complex.",
            "這裡的寧靜讓你感到放鬆。",
        ]
        narrator(random.choice(observations))

    $ store.py_trust += 2

    jump zen_garden_hub

# ============================================================================
# 返回廣場
# ============================================================================

label return_to_plaza:
    scene black with fade

    narrator "你離開了 Zen Garden，返回資訊廣場。"

    jump time_choice_menu
