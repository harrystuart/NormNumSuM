# NormNumSuM
NormNumSuM (Normalised Number of Substring Movements) is a string comparison algorithm designed to be token-order invariant. The algorithm works by iteratively finding the longest substring between the two strings, removing the previously found substring at each timestep and finally comparing this value to the length of the shortest string.

Most existing string comparison algorithms, such as Levenshtein Distance, assert that the two strings should be "similar from left to right". These common algorithms are unsuitable for situations where one is looking to compare string similarity at the token level, where the order of tokens is less important. Rather than naively comparing tokens (where misspellings can be detrimental if token comparison is binary), the proposed substring approach allows for a more continous measure of similarity between strings at the token level. This is also a very lightweight approach relative to mechanisms employing semantic analysis.

Below are some example results (lower score is better.)


```
normnumsum("richmond tigers vs sydney swans", "sydney swans vs richmond tigers")
>>> 0.097

normnumsum("i ate an apple from the tree this morning", "this morning i ate an apple from the tree")
>>> 0.073

normnumsum("elon tusk", "elon musk")
>>> 0.333

normnumsum("jupiter orbits our sun", "john does not seem to get it")
>>> 0.818

normnumsum("photosynthesis is necessary for life", "connor tried jumping down the stairs")
>>> 0.889

normnumsum("roger federer won the latest grand slam", "federer won the recent grand slam")
>>> 0.182
```
