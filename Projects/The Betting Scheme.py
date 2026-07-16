import tkinter as tk


def calculate_payouts(winning_bets, total_pool):
    total_winning_bets = sum(winning_bets)

    payouts = []
    for bet in winning_bets:
        share = (bet / total_winning_bets) * total_pool
        payouts.append(share)

    return payouts


def on_calculate():
    team1_number = int(team1_number_entry.get())
    team2_number = int(team2_number_entry.get())

    team1_bet_strings = team1_bets_entry.get().split()
    team2_bet_strings = team2_bets_entry.get().split()

    team1_bets = []
    for bet_string in team1_bet_strings:
        team1_bets.append(int(bet_string))

    team2_bets = []
    for bet_string in team2_bet_strings:
        team2_bets.append(int(bet_string))

    winning_team_number = int(winning_team_entry.get())

    total_pool = sum(team1_bets) + sum(team2_bets)

    if winning_team_number == team1_number:
        winning_bets = team1_bets
    elif winning_team_number == team2_number:
        winning_bets = team2_bets
    else:
        result_label.config(text="Winning team number doesn't match either team.")
        return

    payouts = calculate_payouts(winning_bets, total_pool)

    result_text = f"Team {winning_team_number} has won!\n"
    for bet, payout in zip(winning_bets, payouts):
        result_text += f"Bettor who bet {bet} BDT has won {payout:.2f} BDT\n"
    result_label.config(text=result_text)


window = tk.Tk()
window.title("The Betting Scheme")
window.geometry("450x400")

tk.Label(window, text="Team 1 number:").pack()
team1_number_entry = tk.Entry(window)
team1_number_entry.pack()

tk.Label(window, text="Team 2 number:").pack()
team2_number_entry = tk.Entry(window)
team2_number_entry.pack()

tk.Label(window, text="Team 1 bets (separated by spaces):").pack()
team1_bets_entry = tk.Entry(window)
team1_bets_entry.pack()

tk.Label(window, text="Team 2 bets (separated by spaces):").pack()
team2_bets_entry = tk.Entry(window)
team2_bets_entry.pack()

tk.Label(window, text="Winning team number:").pack()
winning_team_entry = tk.Entry(window)
winning_team_entry.pack()

calculate_button = tk.Button(window, text="Calculate", command=on_calculate)
calculate_button.pack(pady=10)

result_label = tk.Label(window, text="", justify="left")
result_label.pack(pady=10)

window.mainloop()