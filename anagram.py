#!/usr/bin/python

import sys, copy

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def add(self, word):
        word = word.lower()
        curr = self.root
        for i in range(0, len(word)):
            ch = word[i]
            if not curr.children.has_key(ch):
                curr.children[ch] = TrieNode()
            curr = curr.children[ch]
            if i == len(word) - 1:
                curr.is_word = True

def build_trie(file_name):
    trie = Trie()
    for line in file(file_name):
        curr_word = line.strip()
        trie.add(curr_word)
    return trie

def print_anagrams_recur(remaining_chars, node, word):
    visited = set()
    for i in range(0, len(remaining_chars)):
        ch = remaining_chars[i]
        if ch in visited:
            continue
        if node.children.has_key(ch):
            new_remaining_chars = copy.copy(remaining_chars)
            del new_remaining_chars[i]
            new_word = word + ch
            new_node = node.children[ch]
            if len(new_remaining_chars) == 0:
                if new_node.is_word:
                    print(new_word)
            else:
                print_anagrams_recur(new_remaining_chars, new_node, new_word)
        visited.add(ch)

def print_anagrams(trie, start_word):
    start_word = start_word.lower()
    chars = []
    for ch in start_word:
        chars.append(ch)
    word = ""
    node = trie.root
    print_anagrams_recur(chars, node, word)

def main():
    if len(sys.argv) != 3:
        print("USAGE anagrams.py START_WORD DICTIONARY_FILE")
        sys.exit(1)
    start_word = sys.argv[1]
    trie = build_trie(sys.argv[2])
    print_anagrams(trie, start_word)

if __name__ == "__main__":
    main()
