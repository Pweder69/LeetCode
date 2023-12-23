# Dissecting the problem

The main takeaway from the problem was that i wanted to find an
efficient way to incrementally test for a common prefix. The main idea behind the approach
taken is that we can use any string to test other strings because the prefix will be the
same for all strings we can use any string for a foundation

# Solution

The solution is structured into two parts getting the current prefix:

```python
for lOfFirstWord in range(1, len(strs[0]) + 1):  # Gets the slicing index
    currentPrefixSegment = strs[0][:lOfFirstWord]  # Slices the first word
```

This is just done by indexing through the first word and then slicing up to that point.
For example if this was done with the word "Hello"

```python
"H" -> "He" -> "Hel" -> "Hell" -> "Hello"
```

Next this value is compared with all the other words. This is done by looping though
all words and comparing the "slices"

```python
for words in strs:
    if currentPrefixSegment != words[:lOfFirstWord]:
        return currPrefix
```
