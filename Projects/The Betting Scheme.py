import tkinter as tk


def parse_named_bets(raw_text):
    named_bets = []
    entries = raw_text.split(",")
    for entry in entries:
        name, amount = entry.split(":")
        name = name.strip()
        amount = int(amount.strip())
        named_bets.append((name, amount))
    return named_bets


def calculate_payouts(winning_named_bets, total_pool):
    total_winning_bets = 0
    for name, bet in winning_named_bets:
        total_winning_bets += bet

    payouts = []
    for name, bet in winning_named_bets:
        share = (bet / total_winning_bets) * total_pool
        payouts.append((name, share))

    return payouts


def on_calculate():
    team1_number = int(team1_number_entry.get())
    team2_number = int(team2_number_entry.get())

    team1_named_bets = parse_named_bets(team1_bets_entry.get())
    team2_named_bets = parse_named_bets(team2_bets_entry.get())

    winning_team_number = int(winning_team_entry.get())

    team1_total = 0
    for name, bet in team1_named_bets:
        team1_total += bet

    team2_total = 0
    for name, bet in team2_named_bets:
        team2_total += bet

    total_pool = team1_total + team2_total

    if winning_team_number == team1_number:
        winning_named_bets = team1_named_bets
    elif winning_team_number == team2_number:
        winning_named_bets = team2_named_bets
    else:
        result_label.config(text="Winning team number doesn't match either team.")
        return

    payouts = calculate_payouts(winning_named_bets, total_pool)

    result_text = f"Team {winning_team_number} has won!\n"
    for name, payout in payouts:
        result_text += f"{name} has won {payout:.2f} BDT\n"
    result_label.config(text=result_text)


window = tk.Tk()
window.title("The Betting Scheme")
window.geometry("450x420")

tk.Label(window, text="Team 1 number:").pack()
team1_number_entry = tk.Entry(window)
team1_number_entry.pack()

tk.Label(window, text="Team 2 number:").pack()
team2_number_entry = tk.Entry(window)
team2_number_entry.pack()

tk.Label(window, text="Team 1 bets (e.g. lelin:20, sowmik:30):").pack()
team1_bets_entry = tk.Entry(window, width=40)
team1_bets_entry.pack()

tk.Label(window, text="Team 2 bets (e.g. rifat:60, tanvir:80):").pack()
team2_bets_entry = tk.Entry(window, width=40)
team2_bets_entry.pack()

tk.Label(window, text="Winning team number:").pack()
winning_team_entry = tk.Entry(window)
winning_team_entry.pack()

calculate_button = tk.Button(window, text="Calculate", command=on_calculate)
calculate_button.pack(pady=10)

result_label = tk.Label(window, text="", justify="left")
result_label.pack(pady=10)

window.mainloop()