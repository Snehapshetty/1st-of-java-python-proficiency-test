# 1st-of-java-python-proficiency-test

To find the length of the longest substring without repeating characters, you can use a sliding window approach. Here's how you can do it for the input string "abcabcbb":

Initialize two pointers, start and end, both initially at the beginning of the string.

Create a set to keep track of unique characters within the current substring.

Initialize a variable max_length to 0 to store the maximum length of the substring.

Iterate through the string with the end pointer, and for each character encountered:

Check if it's already in the set. If not, add it to the set.
Calculate the current substring length as end - start + 1.
Update max_length with the maximum between its current value and the current substring length.
If a repeating character is found, move the start pointer to the right until the repeating character is no longer in the set. This ensures that the substring remains without repeating characters.

Repeat steps 4 and 5 until the end pointer reaches the end of the string.

Return the max_length as the length of the longest substring without repeating characters.

For "abcabcbb," the process would look like this:

Initially, start and end are both at index 0, and the set contains "a."
Move end to index 1 (now the set contains "ab").
Move end to index 2 (now the set contains "abc," and max_length is 3).
At index 3, "a" repeats, so move start to index 1 (the set now contains "bc").
Continue this process until end reaches the end of the string.
The final max_length is 3, which corresponds to the substring "abc." So, the output is 3.




