from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *

import pygsheets
import pandas as pd
#authorization
gc = pygsheets.authorize(service_file='modern-cubist-410609-ffea03f0c8fc.json')
sht = gc.open_by_url('https://docs.google.com/spreadsheets/d/1V2NvacvjFJyQbn1RcL2wMe7rjzv-7xZehuxTtY_3sA4/edit#gid=0')
wks_list = sht.worksheets()
print(wks_list)
wks = sht.worksheet_by_title("cpbl")
cpbl = pd.DataFrame(wks.get_all_records())
print(cpbl)

wks1 = sht.worksheet_by_title("2023_1_standing")
firststanding = pd.DataFrame(wks1.get_all_records())
print(firststanding)

wks2 = sht.worksheet_by_title("2023_2_standing")
laststanding = pd.DataFrame(wks2.get_all_records())
print(laststanding)

wks3 = sht.worksheet_by_title("2023_all_standing")
allstanding = pd.DataFrame(wks3.get_all_records())
print(allstanding)

wks4 = sht.worksheet_by_title("cpbl_player")
player = pd.DataFrame(wks4.get_all_records())
print(player)

wks5 = sht.worksheet_by_title("national_player")
nationalplayer = pd.DataFrame(wks5.get_all_records())
print(nationalplayer)

#中職球隊
def brotherFlex_Message():
    message= FlexSendMessage(
        alt_text="中華職棒",
        contents={
  "type": "carousel",
  "contents": [
    {
      "type": "bubble",
      "hero": {
        "type": "image",
        "size": "full",
        "aspectRatio": "20:13",
        "aspectMode": "cover",
        "url": "https://media.zenfs.com/ko/news_ttv_com_tw_433/7060bc71326e28ffce730c8b5b33712d"
      },
      "body": {
        "type": "box",
        "layout": "vertical",
        "spacing": "sm",
        "contents": [
          {
            "type": "text",
            "text": "查詢賽事比分",
            "wrap": True,
            "weight": "bold",
            "size": "xl"
          },
          {
            "type": "box",
            "layout": "baseline",
            "flex": 1,
            "contents": [
              {
                "type": "text",
                "text": "請選擇日期來查詢比數",
                "wrap": True,
                "weight": "bold",
                "size": "md",
                "flex": 0
              }
            ]
          },
          {
            "type": "text",
            "text": "若無賽程跑出，說明該日期無賽程",
            "wrap": True,
            "size": "sm",
            "margin": "md",
            "color": "#ff5551",
            "flex": 0
          }
        ]
      },
      "footer": {
        "type": "box",
        "layout": "vertical",
        "spacing": "sm",
        "contents": [
          {
            "type": "button",
            "flex": 2,
            "style": "primary",
            "color": "#aaaaaa",
            "action": {
              "type": "datetimepicker",
              "label": "日期選擇",
              "data": "中信兄弟賽程",
              "mode": "date",
              "max": "2024-03-30",
              "min": "2023-04-01",
              "initial": "2023-11-12"
            }
          },
          {
            "type": "button",
            "action": {
              "type": "uri",
              "label": "完整賽程表",
              "uri": "https://www.cpbl.com.tw/files/file_pool/1/0N062592789821266339/2023%E4%B8%80%E8%BB%8D%E8%B3%BD%E7%A8%8B%E8%A1%A8_A4OUT.pdf"
            }
          }
        ]
      }
    },
    {
      "type": "bubble",
      "hero": {
        "type": "image",
        "size": "full",
        "aspectRatio": "20:13",
        "aspectMode": "cover",
        "url": "https://img.ltn.com.tw/Upload/sports/page/800/2023/10/05/php9GD9vO.png"
      },
      "body": {
        "type": "box",
        "layout": "vertical",
        "spacing": "sm",
        "contents": [
          {
            "type": "text",
            "text": "年度戰績",
            "wrap": True,
            "weight": "bold",
            "size": "xl"
          },
          {
            "type": "box",
            "layout": "baseline",
            "contents": [
              {
                "type": "text",
                "text": "了解今年的球隊戰績(目前:2023)",
                "wrap": True,
                "weight": "bold",
                "size": "md",
                "flex": 0
              }
            ]
          }
        ]
      },
      "footer": {
        "type": "box",
        "layout": "vertical",
        "spacing": "sm",
        "contents": [
          {
            "type": "button",
            "style": "secondary",
            "action": {
              "type": "postback",
              "label": "中信兄弟上半季",
              "data": "中信兄弟上半季"
            }
          },
          {
            "type": "button",
            "action": {
              "type": "postback",
              "label": "中信兄弟下半季",
              "data": "中信兄弟下半季"
            },
            "style": "secondary"
          },
          {
            "type": "button",
            "style": "primary",
            "action": {
              "type": "postback",
              "label": "中信兄弟全年戰績",
              "data": "中信兄弟全年戰績"
            }
          }
        ]
      }
    },
    {
      "type": "bubble",
      "hero": {
        "type": "image",
        "size": "full",
        "aspectRatio": "20:13",
        "aspectMode": "cover",
        "url": "https://ucarer.tw/img/patient/learn_more_btn_mouseover.png"
      },
      "body": {
        "type": "box",
        "layout": "vertical",
        "spacing": "sm",
        "contents": [
          {
            "type": "text",
            "text": "了解更多",
            "wrap": True,
            "weight": "bold",
            "size": "xl"
          }
        ]
      },
      "footer": {
        "type": "box",
        "layout": "vertical",
        "spacing": "sm",
        "contents": [
          {
            "type": "button",
            "action": {
              "type": "uri",
              "label": "新聞公告",
              "uri": "https://www.cpbl.com.tw/news"
            },
            "style": "secondary"
          },
          {
            "type": "button",
            "action": {
              "type": "uri",
              "label": "了解現役球員",
              "uri": "https://www.cpbl.com.tw/player"
            },
            "style": "secondary"
          },
          {
            "type": "button",
            "style": "primary",
            "action": {
              "type": "uri",
              "label": "前往官網了解更多",
              "uri": "https://www.cpbl.com.tw/"
            }
          }
        ]
      }
    }
    ]
    }
    )
    return message

def monkeyFlex_Message():
    message= FlexSendMessage(
        alt_text="中華職棒",
        contents={
  "type": "carousel",
  "contents": [
    {
      "type": "bubble",
      "hero": {
        "type": "image",
        "size": "full",
        "aspectRatio": "20:13",
        "aspectMode": "cover",
        "url": "https://storage.googleapis.com/hhg-images/news/16/1679369941.jpg"
      },
      "body": {
        "type": "box",
        "layout": "vertical",
        "spacing": "sm",
        "contents": [
          {
            "type": "text",
            "text": "查詢賽事比分",
            "wrap": True,
            "weight": "bold",
            "size": "xl"
          },
          {
            "type": "box",
            "layout": "baseline",
            "flex": 1,
            "contents": [
              {
                "type": "text",
                "text": "請選擇日期來查詢比數",
                "wrap": True,
                "weight": "bold",
                "size": "md",
                "flex": 0
              }
            ]
          },
          {
            "type": "text",
            "text": "若無賽程跑出，說明該日期無賽程",
            "wrap": True,
            "size": "sm",
            "margin": "md",
            "color": "#ff5551",
            "flex": 0
          }
        ]
      },
      "footer": {
        "type": "box",
        "layout": "vertical",
        "spacing": "sm",
        "contents": [
          {
            "type": "button",
            "flex": 2,
            "style": "primary",
            "color": "#aaaaaa",
            "action": {
              "type": "datetimepicker",
              "label": "日期選擇",
              "data": "樂天桃猿賽程",
              "mode": "date",
              "max": "2024-03-30",
              "min": "2023-04-01",
              "initial": "2023-11-12"
            }
          },
          {
            "type": "button",
            "action": {
              "type": "uri",
              "label": "完整賽程表",
              "uri": "https://www.cpbl.com.tw/files/file_pool/1/0N062592789821266339/2023%E4%B8%80%E8%BB%8D%E8%B3%BD%E7%A8%8B%E8%A1%A8_A4OUT.pdf"
            }
          }
        ]
      }
    },
    {
      "type": "bubble",
      "hero": {
        "type": "image",
        "size": "full",
        "aspectRatio": "20:13",
        "aspectMode": "cover",
        "url": "https://img.ltn.com.tw/Upload/sports/page/800/2023/10/05/php9GD9vO.png"
      },
      "body": {
        "type": "box",
        "layout": "vertical",
        "spacing": "sm",
        "contents": [
          {
            "type": "text",
            "text": "年度戰績",
            "wrap": True,
            "weight": "bold",
            "size": "xl"
          },
          {
            "type": "box",
            "layout": "baseline",
            "contents": [
              {
                "type": "text",
                "text": "了解今年的球隊戰績(目前:2023)",
                "wrap": True,
                "weight": "bold",
                "size": "md",
                "flex": 0
              }
            ]
          }
        ]
      },
      "footer": {
        "type": "box",
        "layout": "vertical",
        "spacing": "sm",
        "contents": [
          {
            "type": "button",
            "style": "secondary",
            "action": {
              "type": "postback",
              "label": "樂天桃猿上半季",
              "data": "樂天桃猿上半季"
            }
          },
          {
            "type": "button",
            "action": {
              "type": "postback",
              "label": "樂天桃猿下半季",
              "data": "樂天桃猿下半季"
            },
            "style": "secondary"
          },
          {
            "type": "button",
            "style": "primary",
            "action": {
              "type": "postback",
              "label": "樂天桃猿全年戰績",
              "data": "樂天桃猿全年戰績"
            }
          }
        ]
      }
    },
    {
      "type": "bubble",
      "hero": {
        "type": "image",
        "size": "full",
        "aspectRatio": "20:13",
        "aspectMode": "cover",
        "url": "https://ucarer.tw/img/patient/learn_more_btn_mouseover.png"
      },
      "body": {
        "type": "box",
        "layout": "vertical",
        "spacing": "sm",
        "contents": [
          {
            "type": "text",
            "text": "了解更多",
            "wrap": True,
            "weight": "bold",
            "size": "xl"
          }
        ]
      },
      "footer": {
        "type": "box",
        "layout": "vertical",
        "spacing": "sm",
        "contents": [
          {
            "type": "button",
            "action": {
              "type": "uri",
              "label": "新聞公告",
              "uri": "https://www.cpbl.com.tw/news"
            },
            "style": "secondary"
          },
          {
            "type": "button",
            "action": {
              "type": "uri",
              "label": "了解現役球員",
              "uri": "https://www.cpbl.com.tw/player"
            },
            "style": "secondary"
          },
          {
            "type": "button",
            "style": "primary",
            "action": {
              "type": "uri",
              "label": "前往官網了解更多",
              "uri": "https://www.cpbl.com.tw/"
            }
          }
        ]
      }
    }
    ]
    }
    )
    return message

def lionFlex_Message():
    message= FlexSendMessage(
        alt_text="中華職棒",
        contents={
  "type": "carousel",
  "contents": [
    {
      "type": "bubble",
      "hero": {
        "type": "image",
        "size": "full",
        "aspectRatio": "20:13",
        "aspectMode": "cover",
        "url": "https://s.yimg.com/ny/api/res/1.2/ToZud0x_YQFdJ11EIaG9Gw--/YXBwaWQ9aGlnaGxhbmRlcjt3PTY0MDtoPTM2MA--/https://media.zenfs.com/ko/tsna.com.tw/483ff5064ef0c5ab711c08bc1d6cf83b"
      },
      "body": {
        "type": "box",
        "layout": "vertical",
        "spacing": "sm",
        "contents": [
          {
            "type": "text",
            "text": "查詢賽事比分",
            "wrap": True,
            "weight": "bold",
            "size": "xl"
          },
          {
            "type": "box",
            "layout": "baseline",
            "flex": 1,
            "contents": [
              {
                "type": "text",
                "text": "請選擇日期來查詢比數",
                "wrap": True,
                "weight": "bold",
                "size": "md",
                "flex": 0
              }
            ]
          },
          {
            "type": "text",
            "text": "若無賽程跑出，說明該日期無賽程",
            "wrap": True,
            "size": "sm",
            "margin": "md",
            "color": "#ff5551",
            "flex": 0
          }
        ]
      },
      "footer": {
        "type": "box",
        "layout": "vertical",
        "spacing": "sm",
        "contents": [
          {
            "type": "button",
            "flex": 2,
            "style": "primary",
            "color": "#aaaaaa",
            "action": {
              "type": "datetimepicker",
              "label": "日期選擇",
              "data": "統一獅賽程",
              "mode": "date",
              "max": "2024-03-30",
              "min": "2023-04-01",
              "initial": "2023-11-12"
            }
          },
          {
            "type": "button",
            "action": {
              "type": "uri",
              "label": "完整賽程表",
              "uri": "https://www.cpbl.com.tw/files/file_pool/1/0N062592789821266339/2023%E4%B8%80%E8%BB%8D%E8%B3%BD%E7%A8%8B%E8%A1%A8_A4OUT.pdf"
            }
          }
        ]
      }
    },
    {
      "type": "bubble",
      "hero": {
        "type": "image",
        "size": "full",
        "aspectRatio": "20:13",
        "aspectMode": "cover",
        "url": "https://img.ltn.com.tw/Upload/sports/page/800/2023/10/05/php9GD9vO.png"
      },
      "body": {
        "type": "box",
        "layout": "vertical",
        "spacing": "sm",
        "contents": [
          {
            "type": "text",
            "text": "年度戰績",
            "wrap": True,
            "weight": "bold",
            "size": "xl"
          },
          {
            "type": "box",
            "layout": "baseline",
            "contents": [
              {
                "type": "text",
                "text": "了解今年的球隊戰績(目前:2023)",
                "wrap": True,
                "weight": "bold",
                "size": "md",
                "flex": 0
              }
            ]
          }
        ]
      },
      "footer": {
        "type": "box",
        "layout": "vertical",
        "spacing": "sm",
        "contents": [
          {
            "type": "button",
            "style": "secondary",
            "action": {
              "type": "postback",
              "label": "統一獅上半季",
              "data": "統一獅上半季"
            }
          },
          {
            "type": "button",
            "action": {
              "type": "postback",
              "label": "統一獅下半季",
              "data": "統一獅下半季"
            },
            "style": "secondary"
          },
          {
            "type": "button",
            "style": "primary",
            "action": {
              "type": "postback",
              "label": "統一獅全年戰績",
              "data": "統一獅全年戰績"
            }
          }
        ]
      }
    },
    {
      "type": "bubble",
      "hero": {
        "type": "image",
        "size": "full",
        "aspectRatio": "20:13",
        "aspectMode": "cover",
        "url": "https://ucarer.tw/img/patient/learn_more_btn_mouseover.png"
      },
      "body": {
        "type": "box",
        "layout": "vertical",
        "spacing": "sm",
        "contents": [
          {
            "type": "text",
            "text": "了解更多",
            "wrap": True,
            "weight": "bold",
            "size": "xl"
          }
        ]
      },
      "footer": {
        "type": "box",
        "layout": "vertical",
        "spacing": "sm",
        "contents": [
          {
            "type": "button",
            "action": {
              "type": "uri",
              "label": "新聞公告",
              "uri": "https://www.cpbl.com.tw/news"
            },
            "style": "secondary"
          },
          {
            "type": "button",
            "action": {
              "type": "uri",
              "label": "了解現役球員",
              "uri": "https://www.cpbl.com.tw/player"
            },
            "style": "secondary"
          },
          {
            "type": "button",
            "style": "primary",
            "action": {
              "type": "uri",
              "label": "前往官網了解更多",
              "uri": "https://www.cpbl.com.tw/"
            }
          }
        ]
      }
    }
    ]
    }
    )
    return message

def fubonFlex_Message():
    message= FlexSendMessage(
        alt_text="中華職棒",
        contents={
  "type": "carousel",
  "contents": [
    {
      "type": "bubble",
      "hero": {
        "type": "image",
        "size": "full",
        "aspectRatio": "20:13",
        "aspectMode": "cover",
        "url": "https://obs.line-scdn.net/0hd_J4WZUmO3B3TSkOFkxEJ08bNwFEKyF5VS4hQ1ZNYkQPYXUhHnxoE1BObFxTfSwjV39zEwZKZUANLSskSA/w644"
      },
      "body": {
        "type": "box",
        "layout": "vertical",
        "spacing": "sm",
        "contents": [
          {
            "type": "text",
            "text": "查詢賽事比分",
            "wrap": True,
            "weight": "bold",
            "size": "xl"
          },
          {
            "type": "box",
            "layout": "baseline",
            "flex": 1,
            "contents": [
              {
                "type": "text",
                "text": "請選擇日期來查詢比數",
                "wrap": True,
                "weight": "bold",
                "size": "md",
                "flex": 0
              }
            ]
          },
          {
            "type": "text",
            "text": "若無賽程跑出，說明該日期無賽程",
            "wrap": True,
            "size": "sm",
            "margin": "md",
            "color": "#ff5551",
            "flex": 0
          }
        ]
      },
      "footer": {
        "type": "box",
        "layout": "vertical",
        "spacing": "sm",
        "contents": [
          {
            "type": "button",
            "flex": 2,
            "style": "primary",
            "color": "#aaaaaa",
            "action": {
              "type": "datetimepicker",
              "label": "日期選擇",
              "data": "富邦悍將賽程",
              "mode": "date",
              "max": "2024-03-30",
              "min": "2023-04-01",
              "initial": "2023-11-12"
            }
          },
          {
            "type": "button",
            "action": {
              "type": "uri",
              "label": "完整賽程表",
              "uri": "https://www.cpbl.com.tw/files/file_pool/1/0N062592789821266339/2023%E4%B8%80%E8%BB%8D%E8%B3%BD%E7%A8%8B%E8%A1%A8_A4OUT.pdf"
            }
          }
        ]
      }
    },
    {
      "type": "bubble",
      "hero": {
        "type": "image",
        "size": "full",
        "aspectRatio": "20:13",
        "aspectMode": "cover",
        "url": "https://img.ltn.com.tw/Upload/sports/page/800/2023/10/05/php9GD9vO.png"
      },
      "body": {
        "type": "box",
        "layout": "vertical",
        "spacing": "sm",
        "contents": [
          {
            "type": "text",
            "text": "年度戰績",
            "wrap": True,
            "weight": "bold",
            "size": "xl"
          },
          {
            "type": "box",
            "layout": "baseline",
            "contents": [
              {
                "type": "text",
                "text": "了解今年的球隊戰績(目前:2023)",
                "wrap": True,
                "weight": "bold",
                "size": "md",
                "flex": 0
              }
            ]
          }
        ]
      },
      "footer": {
        "type": "box",
        "layout": "vertical",
        "spacing": "sm",
        "contents": [
          {
            "type": "button",
            "style": "secondary",
            "action": {
              "type": "postback",
              "label": "富邦悍將上半季",
              "data": "富邦悍將上半季"
            }
          },
          {
            "type": "button",
            "action": {
              "type": "postback",
              "label": "富邦悍將下半季",
              "data": "富邦悍將下半季"
            },
            "style": "secondary"
          },
          {
            "type": "button",
            "style": "primary",
            "action": {
              "type": "postback",
              "label": "富邦悍將全年戰績",
              "data": "富邦悍將全年戰績"
            }
          }
        ]
      }
    },
    {
      "type": "bubble",
      "hero": {
        "type": "image",
        "size": "full",
        "aspectRatio": "20:13",
        "aspectMode": "cover",
        "url": "https://ucarer.tw/img/patient/learn_more_btn_mouseover.png"
      },
      "body": {
        "type": "box",
        "layout": "vertical",
        "spacing": "sm",
        "contents": [
          {
            "type": "text",
            "text": "了解更多",
            "wrap": True,
            "weight": "bold",
            "size": "xl"
          }
        ]
      },
      "footer": {
        "type": "box",
        "layout": "vertical",
        "spacing": "sm",
        "contents": [
          {
            "type": "button",
            "action": {
              "type": "uri",
              "label": "新聞公告",
              "uri": "https://www.cpbl.com.tw/news"
            },
            "style": "secondary"
          },
          {
            "type": "button",
            "action": {
              "type": "uri",
              "label": "了解現役球員",
              "uri": "https://www.cpbl.com.tw/player"
            },
            "style": "secondary"
          },
          {
            "type": "button",
            "style": "primary",
            "action": {
              "type": "uri",
              "label": "前往官網了解更多",
              "uri": "https://www.cpbl.com.tw/"
            }
          }
        ]
      }
    }
    ]
    }
    )
    return message

def dragonFlex_Message():
    message= FlexSendMessage(
        alt_text="中華職棒",
        contents={
  "type": "carousel",
  "contents": [
    {
      "type": "bubble",
      "hero": {
        "type": "image",
        "size": "full",
        "aspectRatio": "20:13",
        "aspectMode": "cover",
        "url": "https://www.wdragons.com/wp-content/uploads/2023/10/%E5%91%B3%E5%85%A8%E9%BE%8DTS%E4%B8%BB%E8%A6%96%E8%A6%BA_0.jpg"
      },
      "body": {
        "type": "box",
        "layout": "vertical",
        "spacing": "sm",
        "contents": [
          {
            "type": "text",
            "text": "查詢賽事比分",
            "wrap": True,
            "weight": "bold",
            "size": "xl"
          },
          {
            "type": "box",
            "layout": "baseline",
            "flex": 1,
            "contents": [
              {
                "type": "text",
                "text": "請選擇日期來查詢比數",
                "wrap": True,
                "weight": "bold",
                "size": "md",
                "flex": 0
              }
            ]
          },
          {
            "type": "text",
            "text": "若無賽程跑出，說明該日期無賽程",
            "wrap": True,
            "size": "sm",
            "margin": "md",
            "color": "#ff5551",
            "flex": 0
          }
        ]
      },
      "footer": {
        "type": "box",
        "layout": "vertical",
        "spacing": "sm",
        "contents": [
          {
            "type": "button",
            "flex": 2,
            "style": "primary",
            "color": "#aaaaaa",
            "action": {
              "type": "datetimepicker",
              "label": "日期選擇",
              "data": "味全龍賽程",
              "mode": "date",
              "max": "2024-03-30",
              "min": "2023-04-01",
              "initial": "2023-11-12"
            }
          },
          {
            "type": "button",
            "action": {
              "type": "uri",
              "label": "完整賽程表",
              "uri": "https://www.cpbl.com.tw/files/file_pool/1/0N062592789821266339/2023%E4%B8%80%E8%BB%8D%E8%B3%BD%E7%A8%8B%E8%A1%A8_A4OUT.pdf"
            }
          }
        ]
      }
    },
    {
      "type": "bubble",
      "hero": {
        "type": "image",
        "size": "full",
        "aspectRatio": "20:13",
        "aspectMode": "cover",
        "url": "https://img.ltn.com.tw/Upload/sports/page/800/2023/10/05/php9GD9vO.png"
      },
      "body": {
        "type": "box",
        "layout": "vertical",
        "spacing": "sm",
        "contents": [
          {
            "type": "text",
            "text": "年度戰績",
            "wrap": True,
            "weight": "bold",
            "size": "xl"
          },
          {
            "type": "box",
            "layout": "baseline",
            "contents": [
              {
                "type": "text",
                "text": "了解今年的球隊戰績(目前:2023)",
                "wrap": True,
                "weight": "bold",
                "size": "md",
                "flex": 0
              }
            ]
          }
        ]
      },
      "footer": {
        "type": "box",
        "layout": "vertical",
        "spacing": "sm",
        "contents": [
          {
            "type": "button",
            "style": "secondary",
            "action": {
              "type": "postback",
              "label": "味全龍上半季",
              "data": "味全龍上半季"
            }
          },
          {
            "type": "button",
            "action": {
              "type": "postback",
              "label": "味全龍下半季",
              "data": "味全龍下半季"
            },
            "style": "secondary"
          },
          {
            "type": "button",
            "style": "primary",
            "action": {
              "type": "postback",
              "label": "味全龍全年戰績",
              "data": "味全龍全年戰績"
            }
          }
        ]
      }
    },
    {
      "type": "bubble",
      "hero": {
        "type": "image",
        "size": "full",
        "aspectRatio": "20:13",
        "aspectMode": "cover",
        "url": "https://ucarer.tw/img/patient/learn_more_btn_mouseover.png"
      },
      "body": {
        "type": "box",
        "layout": "vertical",
        "spacing": "sm",
        "contents": [
          {
            "type": "text",
            "text": "了解更多",
            "wrap": True,
            "weight": "bold",
            "size": "xl"
          }
        ]
      },
      "footer": {
        "type": "box",
        "layout": "vertical",
        "spacing": "sm",
        "contents": [
          {
            "type": "button",
            "action": {
              "type": "uri",
              "label": "新聞公告",
              "uri": "https://www.cpbl.com.tw/news"
            },
            "style": "secondary"
          },
          {
            "type": "button",
            "action": {
              "type": "uri",
              "label": "了解現役球員",
              "uri": "https://www.cpbl.com.tw/player"
            },
            "style": "secondary"
          },
          {
            "type": "button",
            "style": "primary",
            "action": {
              "type": "uri",
              "label": "前往官網了解更多",
              "uri": "https://www.cpbl.com.tw/"
            }
          }
        ]
      }
    }
    ]
    }
    )
    return message

def eagleFlex_Message():
    message= FlexSendMessage(
        alt_text="中華職棒",
        contents={
  "type": "carousel",
  "contents": [
    {
      "type": "bubble",
      "hero": {
        "type": "image",
        "size": "full",
        "aspectRatio": "20:13",
        "aspectMode": "cover",
        "url": "https://pgw.udn.com.tw/gw/photo.php?u=https://uc.udn.com.tw/photo/2024/01/04/realtime/28652134.jpg&x=0&y=0&sw=0&sh=0&sl=W&fw=800&exp=3600"
      },
      "body": {
        "type": "box",
        "layout": "vertical",
        "spacing": "sm",
        "contents": [
          {
            "type": "text",
            "text": "查詢賽事比分",
            "wrap": True,
            "weight": "bold",
            "size": "xl"
          },
          {
            "type": "box",
            "layout": "baseline",
            "flex": 1,
            "contents": [
              {
                "type": "text",
                "text": "請選擇日期來查詢比數",
                "wrap": True,
                "weight": "bold",
                "size": "md",
                "flex": 0
              }
            ]
          },
          {
            "type": "text",
            "text": "若無賽程跑出，說明該日期無賽程",
            "wrap": True,
            "size": "sm",
            "margin": "md",
            "color": "#ff5551",
            "flex": 0
          }
        ]
      },
      "footer": {
        "type": "box",
        "layout": "vertical",
        "spacing": "sm",
        "contents": [
          {
            "type": "button",
            "flex": 2,
            "style": "primary",
            "color": "#aaaaaa",
            "action": {
              "type": "datetimepicker",
              "label": "日期選擇",
              "data": "台鋼雄鷹賽程",
              "mode": "date",
              "max": "2024-03-30",
              "min": "2023-04-01",
              "initial": "2023-11-12"
            }
          },
          {
            "type": "button",
            "action": {
              "type": "uri",
              "label": "完整賽程表",
              "uri": "https://www.cpbl.com.tw/files/file_pool/1/0N062592789821266339/2023%E4%B8%80%E8%BB%8D%E8%B3%BD%E7%A8%8B%E8%A1%A8_A4OUT.pdf"
            }
          }
        ]
      }
    },
    {
      "type": "bubble",
      "hero": {
        "type": "image",
        "size": "full",
        "aspectRatio": "20:13",
        "aspectMode": "cover",
        "url": "https://img.ltn.com.tw/Upload/sports/page/800/2023/10/05/php9GD9vO.png"
      },
      "body": {
        "type": "box",
        "layout": "vertical",
        "spacing": "sm",
        "contents": [
          {
            "type": "text",
            "text": "年度戰績",
            "wrap": True,
            "weight": "bold",
            "size": "xl"
          },
          {
            "type": "box",
            "layout": "baseline",
            "contents": [
              {
                "type": "text",
                "text": "了解今年的球隊戰績(目前:2023)",
                "wrap": True,
                "weight": "bold",
                "size": "md",
                "flex": 0
              }
            ]
          }
        ]
      },
      "footer": {
        "type": "box",
        "layout": "vertical",
        "spacing": "sm",
        "contents": [
          {
            "type": "button",
            "style": "secondary",
            "action": {
              "type": "postback",
              "label": "台鋼雄鷹上半季",
              "data": "台鋼雄鷹上半季"
            }
          },
          {
            "type": "button",
            "action": {
              "type": "postback",
              "label": "台鋼雄鷹下半季",
              "data": "台鋼雄鷹下半季"
            },
            "style": "secondary"
          },
          {
            "type": "button",
            "style": "primary",
            "action": {
              "type": "postback",
              "label": "台鋼雄鷹全年戰績",
              "data": "台鋼雄鷹全年戰績"
            }
          }
        ]
      }
    },
    {
      "type": "bubble",
      "hero": {
        "type": "image",
        "size": "full",
        "aspectRatio": "20:13",
        "aspectMode": "cover",
        "url": "https://ucarer.tw/img/patient/learn_more_btn_mouseover.png"
      },
      "body": {
        "type": "box",
        "layout": "vertical",
        "spacing": "sm",
        "contents": [
          {
            "type": "text",
            "text": "了解更多",
            "wrap": True,
            "weight": "bold",
            "size": "xl"
          }
        ]
      },
      "footer": {
        "type": "box",
        "layout": "vertical",
        "spacing": "sm",
        "contents": [
          {
            "type": "button",
            "action": {
              "type": "uri",
              "label": "新聞公告",
              "uri": "https://www.cpbl.com.tw/news"
            },
            "style": "secondary"
          },
          {
            "type": "button",
            "action": {
              "type": "uri",
              "label": "了解現役球員",
              "uri": "https://www.cpbl.com.tw/player"
            },
            "style": "secondary"
          },
          {
            "type": "button",
            "style": "primary",
            "action": {
              "type": "uri",
              "label": "前往官網了解更多",
              "uri": "https://www.cpbl.com.tw/"
            }
          }
        ]
      }
    }
    ]
    }
    )
    return message

#中職球隊排名
def standing_Message(row):
    message= FlexSendMessage(
        alt_text="中華職棒排名",
        contents={
  "type": "bubble",
  "hero": {
    "type": "image",
    "url": "https://media.zenfs.com/zh-tw/rti.org.tw/99743e41744fce863f87edbda97c0c67",
    "size": "full",
    "aspectRatio": "20:13",
    "aspectMode": "cover"
  },
  "body": {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "text",
        "text": f"{row['真排名']}",
        "size": "xxl",
        "weight": "bold"
      },
      {
        "type": "text",
        "text": f"{row['勝-和-敗']}",
        "size": "xl",
        "weight": "bold"
      },
      {
        "type": "box",
        "layout": "vertical",
        "margin": "lg",
        "spacing": "sm",
        "contents": [
          {
            "type": "box",
            "layout": "baseline",
            "spacing": "sm",
            "contents": [
              {
                "type": "text",
                "text": "對戰兄弟",
                "color": "#aaaaaa",
                "size": "sm",
                "flex": 1
              },
              {
                "type": "text",
                "text": f"{row['中信兄弟']}",
                "wrap": True,
                "color": "#666666",
                "size": "sm",
                "flex": 3
              }
            ]
          },
          {
            "type": "box",
            "layout": "baseline",
            "spacing": "sm",
            "contents": [
              {
                "type": "text",
                "text": "對戰桃猿",
                "color": "#aaaaaa",
                "size": "sm",
                "flex": 1
              },
              {
                "type": "text",
                "text": f"{row['樂天桃猿']}",
                "wrap": True,
                "color": "#666666",
                "size": "sm",
                "flex": 3
              }
            ]
          },
          {
            "type": "box",
            "layout": "baseline",
            "spacing": "sm",
            "contents": [
              {
                "type": "text",
                "text": "對戰統一",
                "color": "#aaaaaa",
                "size": "sm",
                "flex": 1
              },
              {
                "type": "text",
                "text": f"{row['統一獅']}",
                "wrap": True,
                "color": "#666666",
                "size": "sm",
                "flex": 3
              }
            ]
          },
          {
            "type": "box",
            "layout": "baseline",
            "spacing": "sm",
            "contents": [
              {
                "type": "text",
                "text": "對戰悍將",
                "color": "#aaaaaa",
                "size": "sm",
                "flex": 1
              },
              {
                "type": "text",
                "text": f"{row['富邦悍將']}",
                "wrap": True,
                "color": "#666666",
                "size": "sm",
                "flex": 3
              }
            ]
          },
          {
            "type": "box",
            "layout": "baseline",
            "spacing": "sm",
            "contents": [
              {
                "type": "text",
                "text": "對戰味全",
                "color": "#aaaaaa",
                "size": "sm",
                "flex": 1
              },
              {
                "type": "text",
                "text": f"{row['味全龍']}",
                "wrap": True,
                "color": "#666666",
                "size": "sm",
                "flex": 3
              }
            ]
          },
          {
            "type": "box",
            "layout": "baseline",
            "spacing": "sm",
            "contents": [
              {
                "type": "text",
                "text": "對戰雄鷹",
                "color": "#aaaaaa",
                "size": "sm",
                "flex": 1
              },
              {
                "type": "text",
                "text": f"{row['台鋼雄鷹']}",
                "wrap": True,
                "color": "#666666",
                "size": "sm",
                "flex": 3
              }
            ]
          }
        ]
      }
    ]
  },
  "footer": {
    "type": "box",
    "layout": "vertical",
    "spacing": "sm",
    "contents": [
      {
        "type": "button",
        "style": "link",
        "height": "sm",
        "action": {
          "type": "uri",
          "label": "完整戰績",
          "uri": "https://www.cpbl.com.tw/standings/season"
        }
      },
      {
        "type": "box",
        "layout": "vertical",
        "contents": [],
        "margin": "sm"
      }
    ],
    "flex": 0
    }
    }
    )
    return message

#中職賽事比數
def cpblFlex_Message(row):
    message= FlexSendMessage(
        alt_text="中華職棒比數",
        contents={
  "type": "bubble",
  "hero": {
    "type": "image",
    "url": "https://sw.cool3c.com/user/100672/2023/8aadf1ec-49f9-409a-9116-57a7e0f0ff11.jpg?fit=max&w=1400&q=80",
    "size": "full",
    "aspectRatio": "20:13",
    "aspectMode": "cover",
    "action": {
      "type": "uri",
      "uri": "http://linecorp.com/"
    }
  },
  "body": {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "box",
        "layout": "baseline",
        "spacing": "sm",
        "contents": [
          {
            "type": "text",
            "text": "勝隊",
            "size": "xxl",
            "flex": 1,
            "weight": "bold"
          },
          {
            "type": "text",
            "text": f"{row['勝隊']}",
            "wrap": True,
            "size": "xxl",
            "flex": 3,
            "weight": "bold"
          }
        ]
      },
      {
        "type": "text",
        "text": f"{row['比分']}",
        "weight": "bold",
        "size": "xl"
      },
      {
        "type": "box",
        "layout": "vertical",
        "margin": "lg",
        "spacing": "sm",
        "contents": [
          {
            "type": "box",
            "layout": "baseline",
            "spacing": "sm",
            "contents": [
              {
                "type": "text",
                "text": "場次",
                "color": "#aaaaaa",
                "size": "sm",
                "flex": 1
              },
              {
                "type": "text",
                "text": f"{row['比賽場次']}",
                "wrap": True,
                "color": "#666666",
                "size": "sm",
                "flex": 5
              }
            ]
          },
          {
            "type": "box",
            "layout": "baseline",
            "spacing": "sm",
            "contents": [
              {
                "type": "text",
                "text": "日期",
                "color": "#aaaaaa",
                "size": "sm",
                "flex": 1
              },
              {
                "type": "text",
                "text": f"{row['日期']}",
                "wrap": True,
                "color": "#666666",
                "size": "sm",
                "flex": 5
              }
            ]
          },
          {
            "type": "box",
            "layout": "baseline",
            "spacing": "sm",
            "contents": [
              {
                "type": "text",
                "text": "地點",
                "color": "#aaaaaa",
                "size": "sm",
                "flex": 1
              },
              {
                "type": "text",
                "text": f"{row['地點']}",
                "wrap": True,
                "color": "#666666",
                "size": "sm",
                "flex": 5
              }
            ]
          }
        ]
      }
    ]
  },
  "footer": {
    "type": "box",
    "layout": "vertical",
    "spacing": "sm",
    "contents": [
      {
        "type": "box",
        "layout": "vertical",
        "contents": [],
        "margin": "sm"
      },
      {
        "type": "box",
        "layout": "baseline",
        "spacing": "sm",
        "contents": [
          {
            "type": "text",
            "text": "比賽時間",
            "color": "#aaaaaa",
            "size": "sm",
            "flex": 1
          },
          {
            "type": "text",
            "text": f"{row['比賽時間']}",
            "wrap": True,
            "color": "#666666",
            "size": "sm",
            "flex": 3
          }
        ]
      }
    ],
    "flex": 0
    }
    }
    )
    return message

#國際比賽球星
def nationalteamplayer(locat,game):
  df1 = nationalplayer[((nationalplayer['身份'] == locat) & (nationalplayer['代表'] == game))].reset_index(drop = True)

  nationalplayerdata={
      "type": "carousel",
      "contents" : []
  }

  for a in range(len(df1)):
    review = {
  "type": "bubble",
  "hero": {
    "type": "image",
    "url": f"{df1['圖片'][a]}",
    "size": "full",
    "aspectRatio": "20:13",
    "aspectMode": "cover"
  },
  "body": {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "text",
        "text": f"{df1['人名'][a]}",
        "size": "xxl",
        "weight": "bold"
      },
      {
        "type": "text",
        "text": f"{df1['守備位置'][a]}",
        "size": "xl",
        "weight": "bold"
      },
      {
        "type": "box",
        "layout": "vertical",
        "margin": "lg",
        "spacing": "sm",
        "contents": [
          {
            "type": "box",
            "layout": "baseline",
            "spacing": "sm",
            "contents": [
              {
                "type": "text",
                "text": "所屬球隊",
                "color": "#aaaaaa",
                "size": "sm",
                "flex": 1
              },
              {
                "type": "text",
                "text": f"{df1['球隊'][a]}",
                "wrap": True,
                "color": "#666666",
                "size": "sm",
                "flex": 3
              }
            ]
          },
          {
            "type": "box",
            "layout": "baseline",
            "spacing": "sm",
            "contents": [
              {
                "type": "text",
                "text": "負責位置",
                "color": "#aaaaaa",
                "size": "sm",
                "flex": 1
              },
              {
                "type": "text",
                "text": f"{df1['身份'][a]}",
                "wrap": True,
                "color": "#666666",
                "size": "sm",
                "flex": 3
              }
            ]
          },
          {
            "type": "box",
            "layout": "baseline",
            "spacing": "sm",
            "contents": [
              {
                "type": "text",
                "text": "生涯成績",
                "color": "#aaaaaa",
                "size": "sm",
                "flex": 1
              },
              {
                "type": "text",
                "text": f"{df1['生涯成績'][a]}",
                "wrap": True,
                "color": "#666666",
                "size": "sm",
                "flex": 3
              }
            ]
          }
        ]
      }
    ]
  },
  "footer": {
    "type": "box",
    "layout": "vertical",
    "spacing": "sm",
    "contents": [
      {
        "type": "button",
        "style": "link",
        "height": "sm",
        "action": {
          "type": "uri",
          "label": "詳細個人資料",
          "uri": f"{df1['個人資料'][a]}"
        }
      },
      {
        "type": "box",
        "layout": "vertical",
        "contents": [],
        "margin": "sm"
      }
    ],
    "flex": 0
    }
    }
    nationalplayerdata["contents"].append(review)

  message= FlexSendMessage(
      alt_text="中華隊人員",
      contents=nationalplayerdata)
  return message

#傳奇球星
def cpblplayer(country):

  df1 = player[((player['旅外一'] == country) | (player['旅外二'] == country))].reset_index(drop = True)

  playerdata={
      "type": "carousel",
      "contents" : []
  }

  for a in range(len(df1)):
    review = {
  "type": "bubble",
  "hero": {
    "type": "image",
    "url": f"{df1['圖片'][a]}",
    "size": "full",
    "aspectRatio": "20:13",
    "aspectMode": "cover"
  },
  "body": {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "text",
        "text": f"{df1['人名'][a]}",
        "size": "xxl",
        "weight": "bold"
      },
      {
        "type": "text",
        "text": f"{df1['外號'][a]}",
        "size": "xl",
        "weight": "bold"
      },
      {
        "type": "box",
        "layout": "vertical",
        "margin": "lg",
        "spacing": "sm",
        "contents": [
          {
            "type": "box",
            "layout": "baseline",
            "spacing": "sm",
            "contents": [
              {
                "type": "text",
                "text": "生涯球隊",
                "color": "#aaaaaa",
                "size": "sm",
                "flex": 1
              },
              {
                "type": "text",
                "text": f"{df1['球隊'][a]}",
                "wrap": True,
                "color": "#666666",
                "size": "sm",
                "flex": 3
              }
            ]
          },
          {
            "type": "box",
            "layout": "baseline",
            "spacing": "sm",
            "contents": [
              {
                "type": "text",
                "text": "現在職務",
                "color": "#aaaaaa",
                "size": "sm",
                "flex": 1
              },
              {
                "type": "text",
                "text": f"{df1['現職'][a]}",
                "wrap": True,
                "color": "#666666",
                "size": "sm",
                "flex": 3
              }
            ]
          },
          {
            "type": "box",
            "layout": "baseline",
            "spacing": "sm",
            "contents": [
              {
                "type": "text",
                "text": "生涯成就",
                "color": "#aaaaaa",
                "size": "sm",
                "flex": 1
              },
              {
                "type": "text",
                "text": f"{df1['生涯成就'][a]}",
                "wrap": True,
                "color": "#666666",
                "size": "sm",
                "flex": 3
              }
            ]
          }
        ]
      }
    ]
    }
    }
    playerdata["contents"].append(review)

  message= FlexSendMessage(
      alt_text="中華職棒比數",
      contents=playerdata)
  return message
