# merge_pdf_app.py （画面パーツの配置のみ）
import tkinter as tk
from tkinter import ttk
import teamDivisionMain


def set_team(team_list):
    team_box.delete('1.0', 'end')
    for team in team_list.keys():
        team_box.insert(tk.END, "チーム" + str(team))
        team_box.insert(tk.END, "\n")
        for member_data in team_list[team]:
            team_box.insert(tk.END, member_data)
            team_box.insert(tk.END, "\n")
        team_box.insert(tk.END, "\n")


# メインウィンドウ
main_win = tk.Tk()
main_win.title("Team Divisional")
main_win.geometry("500x300")

# メインフレーム
main_frm = ttk.Frame(main_win)
main_frm.grid(column=0, row=0, sticky=tk.NSEW, padx=5, pady=10)

# ウィジェット作成（メンバーとチーム）
member_label = ttk.Label(main_frm, text="メンバー")
member_box = tk.Text(main_frm, height=10, width=20)
team_label = ttk.Label(main_frm, text="チーム")
team_box = tk.Text(main_frm, height=10, width=20)

# 初期読み込み時、別ファイルのメンバーリストを読み込む
member_list = teamDivisionMain.get_member_list()
for member in member_list:
    member_box.insert(tk.END, member["name"])
    member_box.insert(tk.END, "\n")

member_box.configure(state="disabled")

# ウィジェット作成（チーム人数）
team_people_label = ttk.Label(main_frm, text="チーム人数")
team_people_comb = ttk.Combobox(main_frm, values=[2, 3, 4], width=3)
team_people_comb.current(0)

# ウィジェット作成（実行ボタン）
app_btn = ttk.Button(main_frm, text="チーム分け",
                     command=lambda: set_team(teamDivisionMain.member_randomize(member_list, team_people_comb.get())))

# ウィジェットの配置
member_label.grid(column=0, row=0, pady=10)
member_box.grid(column=0, row=1, sticky=tk.EW, padx=5)

team_label.grid(column=2, row=0, pady=10)
team_box.grid(column=2, row=1, sticky=tk.EW, padx=5)

team_people_label.grid(column=1, row=2)
team_people_comb.grid(column=1, row=3, padx=5)

app_btn.grid(column=1, row=1)

# 配置設定
main_win.columnconfigure(0, weight=1)
main_win.rowconfigure(0, weight=1)
main_frm.columnconfigure(1, weight=1)

main_win.mainloop()
