
from collections import deque
import string

class Solution:
    def findLadders(self, beginWord, endWord, wordList):

        wordSet = set(wordList)

        if endWord not in wordSet:
            return []

        queue = deque()
        queue.append([beginWord])

        result = []

        while queue:

            level_size = len(queue)
            chosen_words = set()

            for _ in range(level_size):

                sequence = queue.popleft()
                last_word = sequence[-1]

                if last_word == endWord:
                    result.append(sequence)
                    continue

                for i in range(len(last_word)):

                    for ch in string.ascii_lowercase:

                        if ch == last_word[i]:
                            continue

                        new_word = (
                            last_word[:i] +
                            ch +
                            last_word[i+1:]
                        )

                        if new_word in wordSet:

                            new_seq = sequence + [new_word]

                            queue.append(new_seq)
                            chosen_words.add(new_word)

            for word in chosen_words:
                wordSet.remove(word)

            if result:
                break

        return result
