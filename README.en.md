# ChatGPT-Customer-Service

[中文](README.md) | English

[![license](https://img.shields.io/pypi/l/ansicolortags.svg)](LICENSE) [![Release](https://img.shields.io/github/v/release/TheExplainthis/ChatGPT-Customer-Service)](https://github.com/TheExplainthis/ChatGPT-Customer-Service/releases/)


## Introduction
This project demonstrates how to build an intelligent customer service chatbot using the FAQ from Taoyuan Airport. The data can be replaced and modified as needed.
![Demo](https://explainthis.s3-ap-northeast-1.amazonaws.com/b335fcf999ff44eeab50d07319725edf.gif)

## Installation
### Obtaining Tokens
1. Obtain the API Token from OpenAI:
    1. Register/login to an account on the [OpenAI](https://beta.openai.com/) platform
    2. Click on the avatar in the upper right corner and select `View API keys`
    3. Click on`Create new secret key` in the middle -> the generated key is the `OPENAI_API_KEY` (which will be used later)
    - Note: Each API has a free quota and restrictions, see [OpenAI Pricing](https://openai.com/api/pricing/) for details. 
2. Obtain the Line Token:
    1. Login to [Line Developer](https://developers.line.biz/zh-hant/)
    2. Create a bot:
        1. Create a `Provider` -> Click `Create`
        2. Create a `Channel` -> Select `Create a Messaging API channel`
        3. Enter the required basic information
        4. After completing the input, there is a Channel Secret under `Basic Settings` -> Click `Issue`, the generated key is the `LINE_CHANNEL_SECRET` (which will be used later)
        5. Under `Messaging API`, there is a `Channel access token` -> Click `Issue`, the generated key is the `LINE_CHANNEL_ACCESS_TOKEN` (which will be used later)

### Project Setup
1. Fork the Github project:
    1. Register/login to a [GitHub](https://github.com/) account
    2. Go to [ChatGPT-Customer-Service](https://github.com/TheExplainthis/ChatGPT-Customer-Service) 
    3. Click `Star` to support the developer
    4. Click `Fork` to copy all the code to your repository
2. Deploy (free space):
    1. Go to [replit](https://replit.com/)
    2. Register/login to an account
    3. Fork the [ChatGPT-Customer-Service-HyperDB](https://replit.com/@TheExplainthis/ChatGPT-Customer-Service-HyperDB)

### Project Execution
1. Environment variable settings
    1. After completing the `Fork` in the previous step, click on `Secrets` on the left bottom corner of the project management page in `Replit`.
    2. Click `Got it` on the right to add environment variables, including:
        1. The selected model:
            - key: `OPENAI_API_KEY`
            - value: `[Obtained from step 1]`  
        2. Line Channel Secret:
            - key: `LINE_CHANNEL_SECRET`
            - value: `[Obtained from step 1]`
        3. Line Channel Access Token:
            - key: `LINE_CHANNEL_ACCESS_TOKEN`
            - value: `[Obtained from step 1]`
2. Execution:
    1. Click on `Run` on the top
    2. After successful execution, the message `Hello World` will be displayed on the right side of the screen, and the **URL on the top of the screen should be copied**
    3. Go back to the Line Developer, paste the URL obtained in the previous step above `Webhook URL` under `Messaging API`, and add `/callback`. For example: `https://ChatGPT-Customer-Service-HyperDB.explainthis.repl.co/callback`
    4. Open `Use webhook` below
    5. Turn off `Auto-reply messages` below
    - Note: If there is no request within one hour, the program will stop, so the next step is necessary.
3. CronJob sends requests regularly
    1. Register/Login to [cron-job.org](https://cron-job.org/en/)
    2. Select `CREATE CRONJOB` in the upper right corner of the dashboard
    3. Enter `ChatGPT-Line-Bot` in the `Title` and enter the URL from the previous step. For example: `https://ChatGPT-Customer-Service-HyperDB.explainthis.repl.co/`
    4. Set to run every `5 minutes` below
    5. Click  `CREATE`

## How to customize and modify?
Currently, the project will read the `taoyuan-airport-faq` file, which has the following format:

| category | question | answer |
| ----- | ----- | ----- |
| 違禁品 | 安檢時碰到不得上機之危險（安）物品及違禁品，應如何處理？ | 不得上機之危險（安）物品﹕例如超過100ml容器液體、防風型打火機、水果刀…等），需丟棄或改託運；違法違禁品（槍、武士刀、扁鑽、毒品…等），將遭航空警察局移送法辦。|
| 違禁品 | 請問樂器該如何上飛機? | 大型樂器需託運，小型可置於機上隨身物品放置箱者可隨身攜帶。 |
| 違禁品 | 請問出境安檢手提行李的規定 （刮鬍刀、刮鬍泡... | 出境安檢手提行李規定：1. 電動刮鬍刀可以攜帶登機，丟棄式刮鬍刀、摺疊式刮鬍刀等有刀片外露形式者，禁止攜帶登機。 2. 刮鬍泡、容器... |

You can directly modify this file with the same format. After modifying the file, remember to delete the `hyperdb.pickle.gz` file that was originally on the Replit website before running it again. The purpose of this file is to pre-process and store the file in Embedding. Therefore, when switching to a new dataset, the old file needs to be deleted.


## What if the data is not in CSV format?
You can try modifying the `data_preprocessing` function in `src/utils`.

## Support Us
If you like this project and would like to [support us](https://www.buymeacoffee.com/explainthis), you can buy us a coffee. This will be the driving force for us to continue moving forward!

[<a href="https://www.buymeacoffee.com/explainthis" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/v2/default-yellow.png" height="45px" width="162px" alt="Buy Me A Coffee"></a>](https://www.buymeacoffee.com/explainthis)

## Related Projects
- [hyperDB](https://github.com/jdagdelen/hyperDB)

## License
[MIT](LICENSE)