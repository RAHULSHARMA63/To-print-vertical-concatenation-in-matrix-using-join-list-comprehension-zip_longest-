from itertools import zip_longest

test_list = [["Akbar", "not"], ["is", "good"], ["boy"]]

print("The original list : " + str(test_list))

res = ["".join(ele) for ele in zip_longest(*test_list, fillvalue ="")]

print("List after column Concatenation : " + str(res))