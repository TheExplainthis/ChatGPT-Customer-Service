# ChatGPT-Customer-Service

中文 | [English](README.en.md)

[![license](https://img.shields.io/pypi/l/ansicolortags.svg)](LICENSE) [![Release](https://img.shields.io/github/v/release/TheExplainthis/ChatGPT-Customer-Service)](https://github.com/TheExplainthis/ChatGPT-Customer-Service/releases/)


## 介紹
這個專案會示範利用桃園機場的 FAQ 來做智能客服機器人，而資料都是可以替換的，歡迎自行修改。

![Demo](https://github.com/TheExplainthis/ChatGPT-Customer-Service/blob/main/demo/demo.gif)


## 安裝步驟
### Token 取得
1. 取得 OpenAI 給的 API Key：
    1. [OpenAI](https://beta.openai.com/) 平台中註冊/登入帳號
    2. 右上方有一個頭像，點入後選擇 `View API keys`
    3. 點選中間的 `Create new secret key` -> 生成後即為 `OPENAI_API_KEY` （稍晚會用到）
    - 注意：每隻 API 有免費額度，也有其限制，詳情請看 [OpenAI Pricing](https://openai.com/api/pricing/)
2. 取得 LINE Token：
    1. 登入 [LINE Developer](https://developers.line.biz/zh-hant/)
    2. 創建機器人：
        1. 創建 `Provider` -> 按下 `Create`
        2. 創建 `Channel` -> 選擇 `Create a Messaging API channel`
        3. 輸入完必填的基本資料
        4. 輸入完成後，在 `Basic Settings` 下方，有一個 `Channel Secret` -> 按下 `Issue`，生成後即為 `LINE_CHANNEL_SECRET` （稍晚會用到）
        5. 在 `Messaging API` 下方，有一個 `Channel access token` -> 按下 `Issue`，生成後即為 `LINE_CHANNEL_ACCESS_TOKEN` （稍晚會用到）

### 專案設置
1. Fork Github 專案：
    1. 註冊/登入 [GitHub](https://github.com/)
    2. 進入 [ChatGPT-Customer-Service](https://github.com/TheExplainthis/ChatGPT-Customer-Service)
    3. 點選 `Star` 支持開發者
    4. 點選 `Fork` 複製全部的程式碼到自己的倉庫
2. 部署（免費空間）：
    1. 進入 [replit](https://replit.com/)
    2. 註冊登入一個帳號
    3. 將 [專案](https://replit.com/@TheExplainthis/ChatGPT-Customer-Service-HyperDB) Fork 回去 

### 專案執行
1. 環境變數設定
    1. 接續上一步 `Fork` 完成後在 `Replit` 的專案管理頁面左下方 `Tools` 點擊 `Secrets`。
    2. 右方按下 `Got it` 後，即可新增環境變數，需新增：
        1. 欲選擇的模型：
            - key: `OPENAI_API_KEY`
            - value: `[由步驟一取得]`  
        2. Line Channel Secret:
            - key: `LINE_CHANNEL_SECRET`
            - value: `[由步驟一取得]`
        3. Line Channel Access Token:
            - key: `LINE_CHANNEL_ACCESS_TOKEN`
            - value: `[由步驟一取得]`
2. 開始執行
    1. 點擊上方的 `Run`
    2. 成功後右邊畫面會顯示 `Hello World`，並將畫面中上方的**網址複製**下來
    3. 回到 Line Developer，在 `Messaging API` 下方的 `Webhook URL` 江上方網址貼過來，並加上 `/callback` 例如：`https://ChatGPT-Customer-Service-HyperDB.explainthis.repl.co/callback`
    4. 打開下方的 `Use webhook`
    5. 將下方 `Auto-reply messages` 關閉
    - 注意：若一小時內沒有任何請求，則程式會中斷，因此需要下步驟
3. CronJob 定時發送請求
    1. 註冊/登入 [cron-job.org](https://cron-job.org/en/)
    2. 進入後面板右上方選擇 `CREATE CRONJOB`
    3. `Title` 輸入 `ChatGPT-Customer-Service-HyperDB`，網址輸入上一步驟的網址，例如：`https://ChatGPT-Customer-Service-HyperDB.explainthis.repl.co/`
    4. 下方則每 `5 分鐘` 打一次
    5. 按下 `CREATE`

## 如何客製化修改？
目前專案會讀取 `taoyuan-airport-faq` 這份文件，檔案格式如下:

| category | question | answer |
| ----- | ----- | ----- |
| 違禁品 | 安檢時碰到不得上機之危險（安）物品及違禁品，應如何處理？ | 不得上機之危險（安）物品﹕例如超過100ml容器液體、防風型打火機、水果刀…等），需丟棄或改託運；違法違禁品（槍、武士刀、扁鑽、毒品…等），將遭航空警察局移送法辦。|
| 違禁品 | 請問樂器該如何上飛機? | 大型樂器需託運，小型可置於機上隨身物品放置箱者可隨身攜帶。 |
| 違禁品 | 請問出境安檢手提行李的規定 （刮鬍刀、刮鬍泡... | 出境安檢手提行李規定：1. 電動刮鬍刀可以攜帶登機，丟棄式刮鬍刀、摺疊式刮鬍刀等有刀片外露形式者，禁止攜帶登機。 2. 刮鬍泡、容器... |

可以直接針對這份文件做修正，利用一樣地格式即可，修改完檔案要重新執行時，記得刪除原本在 Replit 網站上面的 `hyperdb.pickle.gz` 這份文件，這份文件目的是預先將文件做 Embedding 處理並儲存，所以換新的資料集後要把舊的刪除。

## 如果資料不是 csv 的格式呢？
可以嘗試修改 `src/utils` 裡面的 `data_preprocessing` 函式。

## 支持我們
如果你喜歡這個專案，願意[支持我們](https://www.buymeacoffee.com/explainthis)，可以請我們喝一杯咖啡，這會成為我們繼續前進的動力！

[<a href="https://www.buymeacoffee.com/explainthis" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/v2/default-yellow.png" height="45px" width="162px" alt="Buy Me A Coffee"></a>](https://www.buymeacoffee.com/explainthis)

## 相關專案
- [hyperDB](https://github.com/jdagdelen/hyperDB)

## 授權
[MIT](LICENSE)