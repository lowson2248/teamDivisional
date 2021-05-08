import csv
import random
from pathlib import Path
import json
import sys
from tqdm import tqdm


def get_current_path():
    """
    実行ファイルのパスを返す
    Returns:

    """
    return Path(sys.argv[0]).parent.absolute()


def load_param():
    """
    実行ファイルが存在するフォルダのconf.jsonを読み込む
    Returns:

    """
    with (get_current_path().joinpath("conf.json")).open("r", encoding="utf-8") as f:
        return json.load(f)


def get_member_list():
    """
    CSV内のメンバー情報を読み取る
    Returns:

    """
    # memberList.csvから情報を読み取る
    member_list = []
    with open(Path(load_param()["memberDataPath"]).joinpath("memberList.csv")) as f:
        for item in tqdm(csv.DictReader(f), "メンバーデータロード"):
            member_list.append(item)
    return member_list


def member_randomize(member_list, team_people_num):
    """
    メンバーを人数毎に分割
    Returns:

    """
    random.shuffle(member_list)
    disp_team_dict = dict()
    member_list_num = len(member_list)

    # 総チーム数計算
    team_num = member_list_num / int(team_people_num)
    if member_list_num % int(team_people_num) != 0:
        team_num = team_num + 1
    save_idx = 0
    for t_num in range(int(team_num)):
        team_list = []
        for m_num in range(int(team_people_num)):
            if member_list_num > save_idx:
                team_list.append(member_list[save_idx]["name"])
                save_idx = save_idx + 1
        disp_team_dict[t_num] = team_list
    return disp_team_dict


def main():
    """
    CSV内のメンバー情報を読み取り、分割する
    Returns:

    """
    # memberList.csvから情報を読み取る
    member_list = []
    with open(Path(load_param()["memberDataPath"]).joinpath("memberList.csv")) as f:
        for item in tqdm(csv.DictReader(f), "メンバーデータロード"):
            member_list.append(item)

    random.shuffle(member_list)


    # チーム人数を取得

    # 画面に出力
    # 分割した後に名前をセミコロン区切りで格納。（履歴）


def start():
    main()


if __name__ == '__main__':
    start()
