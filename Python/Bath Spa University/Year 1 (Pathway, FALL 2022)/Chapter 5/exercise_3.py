python_words = {
"print": "A function that displays the output of whatever is stored in its parenthesis.",
"sort": "A function that sorts the list into an alphabetical or ascending order. This function is written as: ex_variable.sort(). This function will make the variable's contents be replaced with the sorted ones.",
"while": "A keyword that will accept a condition, and if it is True, will execute its contents until the condition is False.",
"break": "A keyword that will make the code exit out of the loop.",
"continue":"A keyword that will skip the condition and return to the top of the loop."
}

# This is adding elements to the dictionary
python_words['sorted'] = "A keyword that will sort the contents of a variable into an alphabetical or ascending order. Unlike the 'sort' keyword, it will only be done temporarily, so it is better to store this function in a variable like: new_var=sorted(ex_var). It could also be done like: print(sorted(ex_variable)) but the variable will still be same next time it's called."
python_words['reverse'] = "A keyword that will reverse the order of the variable, which is the opposite of sort/sorted functions. It is done permanently and is written as: ex_var.reverse()"
python_words['del'] = "A keyword that will delete the entire variable that the next time it's called, it will no longer be defined."
python_words['clear'] = "A keyword that will clear the content of a list-type variable, but only making it empty. It is written as: ex_var.clear()"
python_words['keys'] = "A keyword that will get the Key values of a dictionary variable. It is written as: ex_var.keys(). Putting it in a variable like: new_var=ex_var.keys() will cause the newvar variable have all the Key values in the dictionary."

# Loop through the data structure
for key_word, meaning in python_words.items():
	print(f"{key_word}: {meaning}\n")