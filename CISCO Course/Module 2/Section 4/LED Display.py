# segments = {
#     '0': ["###", "# #", "# #", "# #", "###"],
#     '1': ["  #", "  #", "  #", "  #", "  #"],
#     '2': ["###", "  #", "###", "#  ", "###"],
#     '3': ["###", "  #", "###", "  #", "###"],
#     '4': ["# #", "# #", "###", "  #", "  #"],
#     '5': ["###", "#  ", "###", "  #", "###"],
#     '6': ["###", "#  ", "###", "# #", "###"],
#     '7': ["###", "  #", "  #", "  #", "  #"],
#     '8': ["###", "# #", "###", "# #", "###"],
#     '9': ["###", "# #", "###", "  #", "###"],
# }
#
# number = input("Enter a non-negative integer: ")
#
# valid = True
# for ch in number:
#     if not ch.isdigit():
#         valid = False
#
# if not valid:
#     print("Please enter a valid non-negative integer.")
# else:
#     for row in range(5):
#         line = ""
#         for digit in number:
#             line += segments[digit][row] + " "
#         print(line)



# digits = [ '1111110',   # 0
#            '0110000',   # 1
#            '1101101',   # 2
#            '1111001',   # 3
#            '0110011',   # 4
#            '1011011',   # 5
#            '1011111',   # 6
#            '1110000',   # 7
#            '1111111',   # 8
#            '1111011',   # 9
#            ]
#
# def build_digit(pattern):
#     a, b, c, d, e, f, g = pattern
#
#     top      = "###" if a == '1' else "   "
#     up_left  = "#"   if f == '1' else " "
#     up_right = "#"   if b == '1' else " "
#     middle   = "###" if g == '1' else "   "
#     dn_left  = "#"   if e == '1' else " "
#     dn_right = "#"   if c == '1' else " "
#     bottom   = "###" if d == '1' else "   "
#
#     return [top,
#             up_left + " " + up_right,
#             middle,
#             dn_left + " " + dn_right,
#             bottom]
#
# def print_number(num):
#     text = str(num)
#     shapes = [build_digit(digits[int(ch)]) for ch in text]
#
#     for row in range(5):
#         line = ""
#         for shape in shapes:
#             line += shape[row] + " "
#         print(line)
#
# print_number(int(input("Enter the number you wish to display: ")))