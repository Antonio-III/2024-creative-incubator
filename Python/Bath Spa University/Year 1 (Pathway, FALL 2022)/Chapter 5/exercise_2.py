python_words = {
"print": "A function that displays the output of whatever is stored in its parenthesis.",
"sort": "A function that sorts the list into an alphabetical or ascending order. This function is written as: ex_variable.sort(). This function will make the variable's contents be replaced with the sorted ones.",
"while": "A keyword that will accept a condition, and if it is True, will execute its contents until the condition is False.",
"break": "A keyword that will make the code exit out of the loop.",
"continue":"A keyword that will skip the condition and return to the top of the loop."
}

# Print each word and its meaning as neatly formatted output. You might print the word followed by a colon and then its meaning, or print the word on one line and then print its meaning indented on a second line. Use the newline character (\n) to insert a blank line between each word-meaning pair in your output.
print(f"print: {python_words['print']}")
print(f"sort: {python_words['sort']}")
print(f"while: {python_words['while']}")
print(f"break: {python_words['break']}")
print(f"continue: {python_words['continue']}")