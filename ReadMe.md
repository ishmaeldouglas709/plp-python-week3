PLP Python Week 3

This repository contains my Week 3 Python assignment, covering name splitting and greeting, debugging, and a ticket checker.

Files
name_greeter.py — Asks for the user's full name, separates the name into parts, and greets the user by their first name.
bug_hunt.py — Contains the corrected Bug Hunt program with three # BUG: comments explaining the bugs and their fixes.
ticket_checker.py — Checks whether a user is an adult based on their age and displays the appropriate ticket price.
screenshots/ — Contains screenshots showing the programs running successfully with the required test cases.
Part B: Bug Hunt Reflection

The bug that took me the longest to find was the age calculation bug because Python was treating the input age as text instead of a number. The error message helped me identify that I was trying to combine a string with an integer, which showed me that I needed to convert the age to an integer before adding 1.
