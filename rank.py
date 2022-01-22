from collections import defaultdict

# load answers
answers = []
with open('answers.txt') as f:
    for line in f:
        word = line.strip()
        answers.append(word)

# load candidate words
candidates = []
with open('allowed.txt') as f:
    for line in f:
        word = line.strip()
        candidates.append(word)


# calculate letter and letter-position frequency counts
l_scores = defaultdict(int)
lp_scores = defaultdict(int)
for word in answers:
    for pos, letter in enumerate(word):
        l_scores[letter] += 1
        lp_scores[(pos, letter)] += 1


# score each 5-letter word based on lp-frequency and lp-l-frequency
lp_scored_candidates = {}
lpl_scored_candidates = {}
for word in candidates:
    lp_score = 0
    for pos, letter in enumerate(word):
        lp_score += lp_scores[(pos, letter)]
    lp_scored_candidates[word] = lp_score

    lpl_score = 0
    for pos, letter in enumerate(word):
        lpl_score += lp_scores[(pos, letter)]
        # count word-positional score only if the letter occurs once
        if word.count(letter) == 1:
            lpl_score += 0.5 * l_scores[letter]
    lpl_scored_candidates[word] = lpl_score


# display top 50
print("LPL-scored")
for idx, word in enumerate(sorted(lpl_scored_candidates, key=lpl_scored_candidates.get, reverse=True)[0:50]):
    print(idx+1, word, lpl_scored_candidates[word])
print("LP-scored")
for idx, word in enumerate(sorted(lp_scored_candidates, key=lp_scored_candidates.get, reverse=True)[0:50]):
    print(idx+1, word, lp_scored_candidates[word])
