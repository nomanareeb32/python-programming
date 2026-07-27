import curses
from curses import wrapper
import time
import random


def start_screen(Standard_Screen):
	Standard_Screen.clear()
	Standard_Screen.addstr("Welcome to the Speed Typing Test!")
	Standard_Screen.addstr("\nPress any key to begin!")
	Standard_Screen.refresh()
	Standard_Screen.getkey()

def display_text(Standard_Screen, Target, Current, wpm=0):
	Standard_Screen.addstr(Target)
	Standard_Screen.addstr(1, 0, f"WPM: {wpm}")

	for i, char in enumerate(Current):
		correct_char = Target[i]
		color = curses.color_pair(1)
		if char != correct_char:
			color = curses.color_pair(2)

		Standard_Screen.addstr(0, i, char, color)

def load_text():
	with open("WPM Text.txt", "r") as f:
		lines = f.readlines()
		return random.choice(lines).strip()

def wpm_test(Standard_Screen):
	Target_text = load_text()
	Current_text = []
	wpm = 0
	start_time = time.time()
	Standard_Screen.nodelay(True)

	while True:
		time_elapsed = max(time.time() - start_time, 1)
		wpm = round((len(Current_text) / (time_elapsed / 60)) / 5)

		Standard_Screen.clear()
		display_text(Standard_Screen, Target_text, Current_text, wpm)
		Standard_Screen.refresh()

		if "".join(Current_text) == Target_text:
			Standard_Screen.nodelay(False)
			break

		try:
			key = Standard_Screen.getkey()
		except:
			continue

		if ord(key) == 27:
			break

		if key in ("KEY_BACKSPACE", '\b', "\x7f"):
			if len(Current_text) > 0:
				Current_text.pop()
		elif len(Current_text) < len(Target_text):
			Current_text.append(key)


def main(Standard_Screen):
	curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
	curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
	curses.init_pair(3, curses.COLOR_WHITE, curses.COLOR_BLACK)

	start_screen(Standard_Screen)
	while True:
		wpm_test(Standard_Screen)
		Standard_Screen.addstr(2, 0, "You completed the text! Press any key to continue...")
		key = Standard_Screen.getkey()
		
		if ord(key) == 27:
			break

wrapper(main)