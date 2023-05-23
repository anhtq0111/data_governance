import requests
import json
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# puuid 
puuid = "CUcPTA2mHGm2O_wFyZl0p5pC4s2OV-uXAt7cnyuK_ylHZNWuHji609Zv6dyvBKU4BuKJ1S1tIru4GA"


# Chỉ số trận đấu đầu tiên và cuối cùng trong danh sách
begin_index = 0
end_index = 100

# API key của bạn
api_key = "RGAPI-9a88ec5c-6e85-4ca6-b130-0e24787724d7"

# Tạo đường dẫn truy vấn API lấy danh sách match id
requestUrl_for_matchIds = f"https://sea.api.riotgames.com/lol/match/v5/matches/by-puuid/{puuid}/ids?type=ranked&start={begin_index}&count={end_index}&api_key={api_key}"

# Gửi truy vấn API và phân tích phản hồi JSON
responseMatchId = requests.get(requestUrl_for_matchIds)
matchIds = json.loads(responseMatchId.text)
listInfo = []


keys_to_delete = ["challenges","perks","puuid","summonerId","riotIdName","riotIdTagline",]

# Gửi truy vấn API lấy thông tin của từng match
for matchId in matchIds :
    requestUrl_for_matchInfor_byId = f"https://sea.api.riotgames.com/lol/match/v5/matches/{matchId}?api_key={api_key}"
    respondMatch = requests.get(requestUrl_for_matchInfor_byId)
    data = json.loads(respondMatch.text)
    dataPar = data["info"]["participants"]
    for par in dataPar:
        par_copy = par.copy()  # Tạo một bản sao độc lập của par
        for key in keys_to_delete:
            par_copy.pop(key, None)
        listInfo.append(par_copy)
print(listInfo[:2])



