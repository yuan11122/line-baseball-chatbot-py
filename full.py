from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *

items=[
                    QuickReplyButton(
                        action=PostbackAction(label="國內職業比賽", text="我想了解國內的職業比賽", data="國內職業比賽")
                    ),
                    QuickReplyButton(
                        action=PostbackAction(label="國際比賽", text="我想了解臺灣的國際比賽", data="國際比賽")
                    ),
                    QuickReplyButton(
                        action=PostbackAction(label="學生棒球", text="我想了解學生棒球", data="學生棒球")
                    ),
                    QuickReplyButton(
                        action=PostbackAction(label="傳奇球星", text="我想了解傳奇球星", data="傳奇球星")
                    ),
                    QuickReplyButton(
                        action=PostbackAction(label="棒球場", text="我想了解棒球場", data="棒球場")
                    ),
                    QuickReplyButton(
                        action=PostbackAction(label="棒球Menu", text="回到棒球Menu", data="棒球Menu")
                    )
]

def follow():
    message=TextSendMessage(
                text="歡迎加入棒球百科，我會提供您台灣棒球的最新資訊，可以輸入「選單」或「棒球Menu」進行互動，或打其他關鍵字進行互動")
    return message
    

def main_message():
    message= FlexSendMessage(
        alt_text="黑豹旗",
        contents={
  "type": "bubble",
  "hero": {
    "type": "image",
    "url": "https://i.imgur.com/4rsxO7y.jpg",
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
        "text": "棒球Menu",
        "weight": "bold",
        "size": "xxl"
      },
      {
        "type": "text",
        "text": "請選擇賽事",
        "weight": "bold",
        "size": "lg"
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
          "type": "postback",
          "label": "國內職業比賽",
          "data": "國內職業比賽",
          "displayText": "我想了解國內的職業比賽"
        }
      },
      {
        "type": "button",
        "style": "link",
        "height": "sm",
        "action": {
          "type": "postback",
          "label": "國際比賽",
          "data": "國際比賽",
          "displayText": "我想了解臺灣的國際比賽"
        }
      },
      {
        "type": "button",
        "style": "link",
        "height": "sm",
        "action": {
          "type": "postback",
          "label": "學生棒球(黑豹旗)",
          "data": "學生棒球",
          "displayText": "我想了解黑豹旗"
        }
      },
      {
        "type": "button",
        "style": "link",
        "height": "sm",
        "action": {
          "type": "postback",
          "label": "傳奇球星",
          "data": "傳奇球星",
          "displayText": "我想了解傳奇球星"
        }
      },
      {
        "type": "button",
        "style": "link",
        "height": "sm",
        "action": {
          "type": "postback",
          "label": "臺灣棒球場",
          "data": "棒球場",
          "displayText": "我想了解臺灣的棒球場"
        }
      }
    ],
    "flex": 0
    }
    } 
    )
    return message

def player_message():
    message=TemplateSendMessage(
                            alt_text='傳奇球星',
                            template=ButtonsTemplate(
                                thumbnail_image_url='https://upload.wikimedia.org/wikipedia/zh/3/39/%E5%8F%B0%E7%81%A3%E6%A3%92%E7%90%83%E5%90%8D%E4%BA%BA%E5%A0%82.jpg',
                                title='傳奇球星',
                                text='請選擇職棒聯盟，會帶您了解曾經打過該聯盟的傳奇球星',
                                actions=[
                                    PostbackTemplateAction(
                                        label='美國職棒大聯盟(MLB)',
                                        text='我想了解曾經打過美國職棒大聯盟的傳奇球星',
                                        data='美國職棒大聯盟'
                                    ),
                                    PostbackTemplateAction(
                                        label='日本職棒(NPB)',
                                        text='我想了解曾經打過日本職棒的傳奇球星',
                                        data='日本職棒'
                                    ),
                                    PostbackTemplateAction(
                                        label='中華職棒(CPBL)',
                                        text='我想了解曾經打過中華職棒的傳奇球星',
                                        data='中華職棒'
                                    )
                                ]
                            )
                        )
    return message

def wbcnationalplayer_message():
    message=TemplateSendMessage(
                            alt_text='選擇想了解的中華隊位置',
                            template=ButtonsTemplate(
                                thumbnail_image_url='https://pgw.udn.com.tw/gw/photo.php?u=https://uc.udn.com.tw/photo/2023/03/11/realtime/20552000.jpg&x=0&y=0&sw=0&sh=0&sl=W&fw=800&exp=3600',
                                title='選擇位置',
                                text='請選擇位置，會帶您了解該位置，世界棒球經典賽，中華隊的人員',
                                actions=[
                                    PostbackTemplateAction(
                                        label='投手',
                                        text='我想了解世界棒球經典賽，中華隊的投手',
                                        data='WBC投手'
                                    ),
                                    PostbackTemplateAction(
                                        label='打者',
                                        text='我想了解世界棒球經典賽，中華隊的打者',
                                        data='WBC打者'
                                    ),
                                    PostbackTemplateAction(
                                        label='教練',
                                        text='我想了解世界棒球經典賽，中華隊的教練',
                                        data='WBC教練'
                                    )
                                ]
                            )
                        )
    return message

def twelvenationalplayer_message():
    message=TemplateSendMessage(
                            alt_text='選擇想了解的中華隊位置',
                            template=ButtonsTemplate(
                                thumbnail_image_url='https://img.sportsv.net/img/article/cover/5/68945/fit-In5vD6Q1gG-945x495.jpg',
                                title='選擇位置',
                                text='請選擇位置，會帶您了解該位置，世界棒球12強，中華隊的人員',
                                actions=[
                                    PostbackTemplateAction(
                                        label='投手',
                                        text='我想了解世界棒球12強，中華隊的投手',
                                        data='12投手'
                                    ),
                                    PostbackTemplateAction(
                                        label='打者',
                                        text='我想了解世界棒球12強，中華隊的打者',
                                        data='12打者'
                                    ),
                                    PostbackTemplateAction(
                                        label='教練',
                                        text='我想了解世界棒球12強，中華隊的教練',
                                        data='12教練'
                                    )
                                ]
                            )
                        )
    return message

def Image_Carousel_message():
    message=TemplateSendMessage(
                            alt_text='台灣職棒球隊',
                            template=ImageCarouselTemplate(
                                columns=[
                                    ImageCarouselColumn(
                                        image_url='https://upload.wikimedia.org/wikipedia/zh/d/d2/Cpbl-stats-chinatrust-brothers.png',
                                        action=MessageAction(
                                            label='中信兄弟',
                                            text='中信兄弟'
                                        )
                                    ),
                                    ImageCarouselColumn(
                                        image_url='https://upload.wikimedia.org/wikipedia/zh/e/e2/Rakuten_Monkeys_logo.png',
                                        action=MessageAction(
                                            label='樂天桃猿',
                                            text='樂天桃猿'
                                        )
                                    ),
                                    ImageCarouselColumn(
                                        image_url='https://upload.wikimedia.org/wikipedia/zh/1/11/Cpbl-stats-uni-president-7-ele.png',
                                        action=MessageAction(
                                            label='統一獅',
                                            text='統一獅'
                                        )
                                    ),
                                    ImageCarouselColumn(
                                        image_url='https://upload.wikimedia.org/wikipedia/zh/f/f6/Cpbl-stats-fubon-guardians-201.png',
                                        action=MessageAction(
                                            label='富邦悍將',
                                            text='富邦悍將'
                                        )
                                    ),
                                    ImageCarouselColumn(
                                        image_url='https://upload.wikimedia.org/wikipedia/zh/3/30/Wei_Chuan_Dragons_logo.png',
                                        action=MessageAction(
                                            label='味全龍',
                                            text='味全龍'
                                        )
                                    ),
                                    ImageCarouselColumn(
                                        image_url='https://imgs.tsna.com/article/1654666163_byd6g.jpg',
                                        action=MessageAction(
                                            label='台鋼雄鷹',
                                            text='台鋼雄鷹'
                                        )
                                    )
                                ]
                            )
                            
                        )
    return message

def international_Template():
    message= FlexSendMessage(
        alt_text="國際賽事",
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
        "url": "https://www.sportstravelmagazine.com/wp-content/uploads/2016/08/World_Baseball_Classic_logo.svg_.png"
      },
      "body": {
        "type": "box",
        "layout": "vertical",
        "spacing": "sm",
        "contents": [
          {
            "type": "text",
            "text": "WBC選單",
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
                "text": "帶您了解世界棒球經典賽中，有關中華隊以及賽事相關資訊",
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
          # {
          #   "type": "button",
          #   "action": {
          #     "type": "datetimepicker",
          #     "label": "本屆賽事比數",
          #     "data": "wbc比數",
          #     "mode": "date",
          #     "max": "2024-12-31",
          #     "min": "2024-01-01",
          #     "initial": "2024-01-01"
          #   }
          # },
          {
            "type": "button",
            "action": {
              "type": "message",
              "label": "本屆賽事比數",
              "text": "今年並沒有該賽事，下屆賽事將在2026舉辦，敬請期待"
            }
          },
          {
            "type": "button",
            "action": {
              "type": "postback",
              "label": "比賽地點",
              "data": "世界棒球經典賽地點"
            }
          },
          {
            "type": "button",
            "action": {
              "type": "postback",
              "label": "了解本屆中華隊球員",
              "data": "wbc中華隊球員",
              "displayText": "我想了解本屆wbc中華隊球員"
            }
          },
          {
            "type": "button",
            "style": "primary",
            "action": {
              "type": "uri",
              "label": "WBC官網",
              "uri": "https://www.mlb.com/world-baseball-classic"
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
        "url": "https://upload.wikimedia.org/wikipedia/zh/thumb/a/a0/2019_WBSC_Premier_12_logo.svg/1200px-2019_WBSC_Premier_12_logo.svg.png"
      },
      "body": {
        "type": "box",
        "layout": "vertical",
        "spacing": "sm",
        "contents": [
          {
            "type": "text",
            "text": "世界棒球12強賽選單",
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
                "text": "帶您了解世界棒球12強賽選單中，有關中華隊以及賽事相關資訊",
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
          # {
          #   "type": "button",
          #   "action": {
          #     "type": "datetimepicker",
          #     "label": "本屆賽事比數",
          #     "data": "12強比數",
          #     "mode": "date",
          #     "max": "2024-11-24",
          #     "min": "2024-11-10",
          #     "initial": "2024-11-10"
          #   }
          # },
          {
            "type": "button",
            "action": {
              "type": "message",
              "label": "本屆賽事比數",
              "text": "今年的賽事將於11月10日開始，11月24日結束，敬請期待"
            }
          },
          {
            "type": "button",
            "action": {
              "type": "postback",
              "label": "比賽地點",
              "data": "世界棒球12強地點"
            }
          },
          {
            "type": "button",
            "action": {
              "type": "postback",
              "label": "了解本屆中華隊球員",
              "data": "十二強中華隊球員",
              "displayText": "我想了解本屆十二強中華隊球員"
            }
          },
          {
            "type": "button",
            "style": "primary",
            "action": {
              "type": "uri",
              "label": "賽程介紹",
              "uri": "https://zh.wikipedia.org/zh-tw/%E4%B8%96%E7%95%8C%E6%A3%92%E7%90%8312%E5%BC%B7%E8%B3%BD"
            }
          }
        ]
      }
    }
    ]
    } 
    )
    return message

def Flex_Message():
    message= FlexSendMessage(
        alt_text="黑豹旗",
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
        "url": "https://img.ltn.com.tw/Upload/sports/page/800/2023/10/15/105.jpg"
      },
      "body": {
        "type": "box",
        "layout": "vertical",
        "spacing": "sm",
        "contents": [
          {
            "type": "text",
            "text": "參賽隊伍",
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
                "text": "了解2023年參賽的所有球隊",
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
            "style": "primary",
            "action": {
              "type": "uri",
              "label": "點我了解今年參賽球隊",
              "uri": "https://blackpanthercup.tw/teams_north2023/"
            }
          },
          {
            "type": "button",
            "action": {
              "type": "uri",
              "label": "了解歷屆隊伍",
              "uri": "https://blackpanthercup.tw/team_past/"
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
        "url": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQqAR35Jf7PRANKpq_AY0N7k_PQnBU2IqeP-A&usqp=CAU"
      },
      "body": {
        "type": "box",
        "layout": "vertical",
        "spacing": "sm",
        "contents": [
          {
            "type": "text",
            "text": "賽事比分",
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
                "text": "請依照圖片上的日期區間來選擇你想查詢的比賽",
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
            "flex": 2,
            "style": "primary",
            "color": "#aaaaaa",
            "action": {
              "type": "uri",
              "label": "預賽",
              "uri": "https://blackpanthercup.tw/game_pre2023_1014/#result_pre"
            }
          },
          {
            "type": "button",
            "flex": 2,
            "style": "primary",
            "color": "#aaaaaa",
            "action": {
              "type": "uri",
              "label": "64強",
              "uri": "https://blackpanthercup.tw/game_64_2023_1101/#result_pre"
            }
          },
          {
            "type": "button",
            "flex": 2,
            "style": "primary",
            "color": "#aaaaaa",
            "action": {
              "type": "uri",
              "label": "16強",
              "uri": "https://blackpanthercup.tw/game_16_2023_1111/#result_pre"
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
        "url": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQqAR35Jf7PRANKpq_AY0N7k_PQnBU2IqeP-A&usqp=CAU"
      },
      "body": {
        "type": "box",
        "layout": "vertical",
        "spacing": "sm",
        "contents": [
          {
            "type": "text",
            "text": "賽事比分",
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
                "text": "請依照圖片上的日期區間來選擇你想查詢的比賽",
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
            "flex": 2,
            "style": "primary",
            "color": "#aaaaaa",
            "action": {
              "type": "uri",
              "label": "8強",
              "uri": "https://blackpanthercup.tw/game_8_2023_1116/#result_pre"
            }
          },
          {
            "type": "button",
            "flex": 2,
            "style": "primary",
            "color": "#aaaaaa",
            "action": {
              "type": "uri",
              "label": "4強",
              "uri": "https://blackpanthercup.tw/game_4_2023_1118/#result_pre"
            }
          },
          {
            "type": "button",
            "flex": 2,
            "style": "primary",
            "color": "#aaaaaa",
            "action": {
              "type": "uri",
              "label": "冠軍賽",
              "uri": "https://blackpanthercup.tw/game_champion2023/#result_pre"
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
        "url": "https://blackpanthercup.tw/wp-content/uploads/2023/10/fb_share.jpg"
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
          },
          {
            "type": "box",
            "layout": "baseline",
            "contents": [
              {
                "type": "text",
                "text": "更多資訊請點擊官方網站",
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
            "action": {
              "type": "uri",
              "label": "完整賽程表",
              "uri": "https://blackpanthercup.tw/wp-content/uploads/2023/10/2023%E9%BB%91%E8%B1%B9%E6%97%97%E7%B7%9A%E5%9E%8B%E5%9C%96%E7%B8%BD%E8%A1%A8.pdf"
            }
          },
          {
            "type": "button",
            "style": "primary",
            "action": {
              "type": "uri",
              "label": "最新消息",
              "uri": "https://blackpanthercup.tw/news_list/"
            }
          },
          {
            "type": "button",
            "action": {
              "type": "uri",
              "label": "前往官網了解更多",
              "uri": "https://blackpanthercup.tw/"
            }
          }
        ]
      }
    }
    ]
    } 
    )
    return message

def Flex_Message1():
    message= FlexSendMessage(
        alt_text="知名棒球場",
        contents={
  "type": "carousel",
  "contents": [
    {
      "type": "bubble",
      "size": "micro",
      "hero": {
        "type": "image",
        "url": "https://www.travel.taipei/content/images/attractions/192019/1024x768_attractions-image-g8-9ftqj_es7eipy6zy53g.jpg",
        "size": "full",
        "aspectMode": "cover",
        "aspectRatio": "320:213"
      },
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "text",
            "text": "天母棒球場",
            "weight": "bold",
            "size": "xl",
            "wrap": True
          },
          {
            "type": "box",
            "layout": "baseline",
            "contents": [
              {
                "type": "icon",
                "size": "xs",
                "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png"
              },
              {
                "type": "icon",
                "size": "xs",
                "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png"
              },
              {
                "type": "icon",
                "size": "xs",
                "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png"
              },
              {
                "type": "icon",
                "size": "xs",
                "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png"
              },
              {
                "type": "icon",
                "size": "xs",
                "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png"
              },
              {
                "type": "text",
                "text": "5.0",
                "size": "xs",
                "color": "#8c8c8c",
                "margin": "md",
                "flex": 0
              }
            ]
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "box",
                "layout": "vertical",
                "spacing": "sm",
                "contents": [
                  {
                    "type": "text",
                    "text": "味全龍主場",
                    "wrap": True,
                    "color": "#8c8c8c",
                    "size": "md",
                    "flex": 5
                  },
                  {
                    "type": "text",
                    "text": "台北市",
                    "wrap": True,
                    "color": "#8c8c8c",
                    "size": "md",
                    "flex": 5
                  }
                ]
              }
            ]
          }
        ],
        "spacing": "sm",
        "paddingAll": "13px"
      },
      "footer": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "button",
            "action": {
              "type": "uri",
              "label": "地點",
              "uri": "https://maps.app.goo.gl/iLffv82eqx5ssWaNA"
            }
          }
        ],
        "spacing": "sm",
        "paddingAll": "13px"
      }
    },
    {
      "type": "bubble",
      "size": "micro",
      "hero": {
        "type": "image",
        "url": "https://imgs.gvm.com.tw/upload/gallery/20201102/75520_02.jpg",
        "size": "full",
        "aspectMode": "cover",
        "aspectRatio": "320:213"
      },
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "text",
            "text": "新莊棒球場",
            "weight": "bold",
            "size": "xl",
            "wrap": True
          },
          {
            "type": "box",
            "layout": "baseline",
            "contents": [
              {
                "type": "icon",
                "size": "xs",
                "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png"
              },
              {
                "type": "icon",
                "size": "xs",
                "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png"
              },
              {
                "type": "icon",
                "size": "xs",
                "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png"
              },
              {
                "type": "icon",
                "size": "xs",
                "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png"
              },
              {
                "type": "icon",
                "size": "xs",
                "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png"
              },
              {
                "type": "text",
                "text": "5.0",
                "size": "xs",
                "color": "#8c8c8c",
                "margin": "md",
                "flex": 0
              }
            ]
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "box",
                "layout": "vertical",
                "spacing": "sm",
                "contents": [
                  {
                    "type": "text",
                    "text": "富邦悍將主場",
                    "wrap": True,
                    "color": "#8c8c8c",
                    "size": "md",
                    "flex": 5
                  },
                  {
                    "type": "text",
                    "text": "新北市",
                    "wrap": True,
                    "color": "#8c8c8c",
                    "size": "md",
                    "flex": 5
                  }
                ]
              }
            ]
          }
        ],
        "spacing": "sm",
        "paddingAll": "13px"
      },
      "footer": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "button",
            "action": {
              "type": "uri",
              "label": "地點",
              "uri": "https://maps.app.goo.gl/7AyXZi2vZwoN2T5Z8"
            }
          }
        ],
        "spacing": "sm",
        "paddingAll": "13px"
      }
    },
    {
      "type": "bubble",
      "size": "micro",
      "hero": {
        "type": "image",
        "url": "https://img.ltn.com.tw/Upload/sports/page/800/2020/04/13/225.jpg",
        "size": "full",
        "aspectMode": "cover",
        "aspectRatio": "320:213"
      },
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "text",
            "text": "桃園大水壩棒球場",
            "weight": "bold",
            "size": "xl",
            "wrap": True
          },
          {
            "type": "box",
            "layout": "baseline",
            "contents": [
              {
                "type": "icon",
                "size": "xs",
                "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png"
              },
              {
                "type": "icon",
                "size": "xs",
                "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png"
              },
              {
                "type": "icon",
                "size": "xs",
                "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png"
              },
              {
                "type": "icon",
                "size": "xs",
                "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png"
              },
              {
                "type": "icon",
                "size": "xs",
                "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png"
              },
              {
                "type": "text",
                "text": "5.0",
                "size": "xs",
                "color": "#8c8c8c",
                "margin": "md",
                "flex": 0
              }
            ]
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "box",
                "layout": "vertical",
                "spacing": "sm",
                "contents": [
                  {
                    "type": "text",
                    "text": "樂天桃猿主場",
                    "wrap": True,
                    "color": "#8c8c8c",
                    "size": "md",
                    "flex": 5
                  },
                  {
                    "type": "text",
                    "text": "桃園市",
                    "wrap": True,
                    "color": "#8c8c8c",
                    "size": "md",
                    "flex": 5
                  }
                ]
              }
            ]
          }
        ],
        "spacing": "sm",
        "paddingAll": "13px"
      },
      "footer": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "button",
            "action": {
              "type": "uri",
              "label": "地點",
              "uri": "https://maps.app.goo.gl/4LLZ2hGAFJnEuMZ47"
            }
          }
        ],
        "spacing": "sm",
        "paddingAll": "13px"
      }
    },
    {
      "type": "bubble",
      "size": "micro",
      "hero": {
        "type": "image",
        "url": "https://hiromishi.com/wp-content/uploads/20200913191641_71.jpg",
        "size": "full",
        "aspectMode": "cover",
        "aspectRatio": "320:213"
      },
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "text",
            "text": "洲際棒球場",
            "weight": "bold",
            "size": "xl",
            "wrap": True
          },
          {
            "type": "box",
            "layout": "baseline",
            "contents": [
              {
                "type": "icon",
                "size": "xs",
                "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png"
              },
              {
                "type": "icon",
                "size": "xs",
                "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png"
              },
              {
                "type": "icon",
                "size": "xs",
                "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png"
              },
              {
                "type": "icon",
                "size": "xs",
                "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png"
              },
              {
                "type": "icon",
                "size": "xs",
                "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png"
              },
              {
                "type": "text",
                "text": "5.0",
                "size": "xs",
                "color": "#8c8c8c",
                "margin": "md",
                "flex": 0
              }
            ]
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "box",
                "layout": "vertical",
                "spacing": "sm",
                "contents": [
                  {
                    "type": "text",
                    "text": "中信兄弟主場",
                    "wrap": True,
                    "color": "#8c8c8c",
                    "size": "md",
                    "flex": 5
                  },
                  {
                    "type": "text",
                    "text": "台中市",
                    "wrap": True,
                    "color": "#8c8c8c",
                    "size": "md",
                    "flex": 5
                  }
                ]
              }
            ]
          }
        ],
        "spacing": "sm",
        "paddingAll": "13px"
      },
      "footer": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "button",
            "action": {
              "type": "uri",
              "label": "地點",
              "uri": "https://maps.app.goo.gl/ga4nUR3QdsaPpVhh7"
            }
          }
        ],
        "spacing": "sm",
        "paddingAll": "13px"
      }
    },
    {
      "type": "bubble",
      "size": "micro",
      "hero": {
        "type": "image",
        "url": "https://img.ltn.com.tw/Upload/sports/page/800/2019/08/04/phppCl86a.jpg",
        "size": "full",
        "aspectMode": "cover",
        "aspectRatio": "320:213"
      },
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "text",
            "text": "台南棒球場",
            "weight": "bold",
            "size": "xl",
            "wrap": True
          },
          {
            "type": "box",
            "layout": "baseline",
            "contents": [
              {
                "type": "icon",
                "size": "xs",
                "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png"
              },
              {
                "type": "icon",
                "size": "xs",
                "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png"
              },
              {
                "type": "icon",
                "size": "xs",
                "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png"
              },
              {
                "type": "icon",
                "size": "xs",
                "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png"
              },
              {
                "type": "icon",
                "size": "xs",
                "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png"
              },
              {
                "type": "text",
                "text": "5.0",
                "size": "xs",
                "color": "#8c8c8c",
                "margin": "md",
                "flex": 0
              }
            ]
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "box",
                "layout": "vertical",
                "spacing": "sm",
                "contents": [
                  {
                    "type": "text",
                    "text": "統一獅主場",
                    "wrap": True,
                    "color": "#8c8c8c",
                    "size": "md",
                    "flex": 5
                  },
                  {
                    "type": "text",
                    "text": "台南市",
                    "wrap": True,
                    "color": "#8c8c8c",
                    "size": "md",
                    "flex": 5
                  }
                ]
              }
            ]
          }
        ],
        "spacing": "sm",
        "paddingAll": "13px"
      },
      "footer": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "button",
            "action": {
              "type": "uri",
              "label": "地點",
              "uri": "https://maps.app.goo.gl/EQkppLBRZiPhpuoK8"
            }
          }
        ],
        "spacing": "sm",
        "paddingAll": "13px"
      }
    },
    {
      "type": "bubble",
      "size": "micro",
      "hero": {
        "type": "image",
        "url": "https://imgs.tsna.com/article/1657873536_Iii8O.jpg",
        "size": "full",
        "aspectMode": "cover",
        "aspectRatio": "320:213"
      },
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "text",
            "text": "澄清湖棒球場",
            "weight": "bold",
            "size": "xl",
            "wrap": True
          },
          {
            "type": "box",
            "layout": "baseline",
            "contents": [
              {
                "type": "icon",
                "size": "xs",
                "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png"
              },
              {
                "type": "icon",
                "size": "xs",
                "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png"
              },
              {
                "type": "icon",
                "size": "xs",
                "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png"
              },
              {
                "type": "icon",
                "size": "xs",
                "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png"
              },
              {
                "type": "icon",
                "size": "xs",
                "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png"
              },
              {
                "type": "text",
                "text": "5.0",
                "size": "xs",
                "color": "#8c8c8c",
                "margin": "md",
                "flex": 0
              }
            ]
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "box",
                "layout": "vertical",
                "spacing": "sm",
                "contents": [
                  {
                    "type": "text",
                    "text": "臺鋼雄鷹主場",
                    "wrap": True,
                    "color": "#8c8c8c",
                    "size": "md",
                    "flex": 5
                  },
                  {
                    "type": "text",
                    "text": "高雄市",
                    "wrap": True,
                    "color": "#8c8c8c",
                    "size": "md",
                    "flex": 5
                  }
                ]
              }
            ]
          }
        ],
        "spacing": "sm",
        "paddingAll": "13px"
      },
      "footer": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "button",
            "action": {
              "type": "uri",
              "label": "地點",
              "uri": "https://maps.app.goo.gl/SKTGnzbecE3jqR2SA"
            }
          }
        ],
        "spacing": "sm",
        "paddingAll": "13px"
      }
    }
  ]
}
    )
    return message

def twelve_Message():
    message= FlexSendMessage(
        alt_text="世界12強棒球賽地點",
        contents={
      "type": "bubble",
      "size": "micro",
      "hero": {
        "type": "image",
        "url": "https://d1b8dyiuti31bx.cloudfront.net/NewsPhotos/20231120/50_021704114692.jpg",
        "size": "full",
        "aspectMode": "cover",
        "aspectRatio": "320:213"
      },
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "text",
            "text": "台北大巨蛋",
            "weight": "bold",
            "size": "xl",
            "wrap": True
          },
          {
            "type": "box",
            "layout": "baseline",
            "contents": [
              {
                "type": "icon",
                "size": "xs",
                "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png"
              },
              {
                "type": "icon",
                "size": "xs",
                "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png"
              },
              {
                "type": "icon",
                "size": "xs",
                "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png"
              },
              {
                "type": "icon",
                "size": "xs",
                "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png"
              },
              {
                "type": "icon",
                "size": "xs",
                "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png"
              },
              {
                "type": "text",
                "text": "5.0",
                "size": "xs",
                "color": "#8c8c8c",
                "margin": "md",
                "flex": 0
              }
            ]
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "box",
                "layout": "vertical",
                "spacing": "sm",
                "contents": [
                  {
                    "type": "text",
                    "text": "世界12強棒球賽地點",
                    "wrap": True,
                    "color": "#8c8c8c",
                    "size": "md",
                    "flex": 5
                  },
                  {
                    "type": "text",
                    "text": "台北市",
                    "wrap": True,
                    "color": "#8c8c8c",
                    "size": "md",
                    "flex": 5
                  }
                ]
              }
            ]
          }
        ],
        "spacing": "sm",
        "paddingAll": "13px"
      },
      "footer": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "button",
            "action": {
              "type": "uri",
              "label": "地點",
              "uri": "https://maps.app.goo.gl/wppNVKLA2i6HnwZh8"
            }
          }
        ],
        "spacing": "sm",
        "paddingAll": "13px"
      }
    }
    )
    return message

def wbc_Message():
    message= FlexSendMessage(
        alt_text="wbc世界棒球經典賽地點",
        contents={
      "type": "bubble",
      "size": "micro",
      "hero": {
        "type": "image",
        "url": "https://hiromishi.com/wp-content/uploads/20200913191641_71.jpg",
        "size": "full",
        "aspectMode": "cover",
        "aspectRatio": "320:213"
      },
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "text",
            "text": "洲際棒球場",
            "weight": "bold",
            "size": "xl",
            "wrap": True
          },
          {
            "type": "box",
            "layout": "baseline",
            "contents": [
              {
                "type": "icon",
                "size": "xs",
                "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png"
              },
              {
                "type": "icon",
                "size": "xs",
                "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png"
              },
              {
                "type": "icon",
                "size": "xs",
                "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png"
              },
              {
                "type": "icon",
                "size": "xs",
                "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png"
              },
              {
                "type": "icon",
                "size": "xs",
                "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png"
              },
              {
                "type": "text",
                "text": "5.0",
                "size": "xs",
                "color": "#8c8c8c",
                "margin": "md",
                "flex": 0
              }
            ]
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "box",
                "layout": "vertical",
                "spacing": "sm",
                "contents": [
                  {
                    "type": "text",
                    "text": "wbc世界棒球經典賽地點",
                    "wrap": True,
                    "color": "#8c8c8c",
                    "size": "md",
                    "flex": 5
                  },
                  {
                    "type": "text",
                    "text": "台中市",
                    "wrap": True,
                    "color": "#8c8c8c",
                    "size": "md",
                    "flex": 5
                  }
                ]
              }
            ]
          }
        ],
        "spacing": "sm",
        "paddingAll": "13px"
      },
      "footer": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "button",
            "action": {
              "type": "uri",
              "label": "地點",
              "uri": "https://maps.app.goo.gl/ga4nUR3QdsaPpVhh7"
            }
          }
        ],
        "spacing": "sm",
        "paddingAll": "13px"
      }
    }
    )
    return message
# def postback_message(event):
#     data = event.postback.data
#     userID = event.source.user_id
#     if data == '國內職業比賽':
        


