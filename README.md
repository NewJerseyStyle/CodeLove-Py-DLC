# CodeLove-Py-DLC

源界 (Source Realm) 的 Python 語言角色 DLC。這是一個完整的可運行範例，展示如何為源界創建 DLC。

## 架構說明

### 區域導向設計

本 DLC 採用**區域導向**設計：

```
廣場（主線樞紐）
    └── [前往其他區域]
            │
            └── Zen Garden（Py DLC 區域）
                    │
                    ├── 和 Py 學習（事件）
                    ├── 和 Py 聊天
                    ├── 在花園散步
                    └── 返回廣場
```

**優點**：
- DLC 有自己的區域，不干擾主線
- 區域內部自己管理事件和解鎖條件
- 玩家可以自由進出，不強制時間對齊

## 角色：Py (Python)

### 語言特性映射

| Python 特性 | 角色表現 |
|------------|---------|
| 動態型別 | 不要求事先定義型別，但會「感覺」到型別不合適 |
| 縮排語法 | 對格式非常敏感，混亂的格式會讓她不適 |
| GIL | 可以同時做很多事，但某個時刻只能專注一件事 |
| Zen of Python | 追求簡潔、優雅、明確 |
| "Batteries included" | 總是帶著很多工具 |
| 鴨子型別 | 「如果它走起來像鴨子，叫起來像鴨子...」 |

### 關係進程

```
UNMET → ACQUAINTED → FRIEND → CLOSE → PARTNER
```

## 章節內容

| 章節 | 教學重點 | 解鎖條件 |
|------|---------|---------|
| PY_01 | 縮排與格式 | 完成 C_01 |
| PY_02 | 列表推導式 | Py 關係達 FRIEND |
| PY_03 | GIL 與並發 | Py 關係達 CLOSE |

## 安裝

1. 在 Release 下載 ZIP：https://github.com/NewJerseyStyle/CodeLove-Py-DLC/releases
2. 用戶解壓到 `game/`

將整個 `CodeLove-Py-DLC` 資料夾複製到主遊戲的以下位置：

```
SourceRealm/
└── game/        ← 複製到這個文件夾裡任何地方就可以
    └── CodeLove-Py-DLC
```

## 驗證安裝

1. 啟動遊戲
2. 完成序章和 C_01
3. 在廣場選擇「前往其他區域」
4. 應該看到「Zen Garden」選項

## 文件結構

```
CodeLove-Py-DLC/
├── README.md                    # 本文件
├── config.rpy                   # DLC 配置和區域註冊
├── characters.rpy               # Py 角色定義
├── endings.rpy                  # 結局定義
└── events/
    ├── zen_garden_hub.rpy       # 區域入口和樞紐菜單
    └── PY_01_indentation.rpy    # 第一章：縮排教學
```

## 開發指南

### 創建新區域

1. 在 `config.rpy` 中使用 `register_dlc_region()` 註冊區域：

```python
register_dlc_region("your_region", {
    "name": "Your Region Name",
    "description": "區域描述",
    "dlc_id": "your_dlc",
    "entry_label": "enter_your_region",  # 入口 label
    "unlock_condition": lambda: True,      # 解鎖條件
})
```

2. 創建入口 label 和區域樞紐：

```renpy
label enter_your_region:
    scene bg your_region with fade
    narrator "你來到了 Your Region。"
    jump your_region_hub

label your_region_hub:
    # 區域內的菜單
    menu:
        "做某事":
            jump do_something
        "返回廣場":
            jump return_to_plaza
```

### 添加新事件

1. 在 `config.rpy` 的 `py_region_events` 中添加事件定義
2. 創建對應的 label
3. 事件結束後跳轉回區域樞紐

## 授權

MIT License
