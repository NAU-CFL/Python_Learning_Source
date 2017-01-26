# Losing Your Head over Chess

story = """
The game of chess is generally believed to have been invented in India in the
sixth century for a ruling king by one of his subjects. The king was supposedly
very delighted with the game and asked the subject what he wanted in return.
The subject, being clever, asked for one grain of wheat on the first square,
two grains of wheat on the second square, four grains of wheat on the third
square, and so forth, doubling the amount on each next square. The king thought
that this was a modest reward for such an invention. However, the total amount
of wheat would have been more than 1,000 times the current world production.
"""

"""
Develop and test a Python program that calculates how much wheat this would be
in pounds, using the fact that a grain of wheat weighs approximately 1/7,000 of a pound.
"""

print("Story of our program: ")
print(story)

chess_table = 8*8

print()
print("Total number of chess squares: ", chess_table)

# Brute Force :
# total_grain = 2**0 + 2**1 + ... + 2**62 + 2**63

# To find sum of powers of two:
# total := 2**i , until i 63
# total = 2**64 - 1

print("Total number of pounds required: " ,  ((2**64-1) / 7000))
