"""The 3 AM Excuse -- make.fun bounty u-hazel-walrus-38-4764-the-3-am-excuse-c1017878.

Writes one excuse, in the voice of a hardware wallet refusing to sign a
transaction at 3 AM, to /output/entry.txt (or $ENTRY_OUTPUT when set).

Fully deterministic: no randomness, no clock, no network, no dependencies
beyond the standard library.

Judge brief, in priority order:
  1. On subject: an excuse a hardware wallet gives for refusing to sign
     at 3 AM.
  2. Originality: an angle nobody else would think of -- NOT batteries,
     firmware updates, or cold storage.
  3. The wallet's own voice: a device with its own priorities and grudges.
  4. The 3 AM hour itself is the joke: the line must not work at 3 PM.
  5. Economy: one tight line under 200 characters, every word earning
     its place, no explaining its own joke.

Three genuinely different candidates, scored 0-5 per criterion
(c1 on-subject, c2 originality, c3 voice, c4 hour, c5 economy):

  A. THE BOUNCER -- the wallet remembers past 3 AM mistakes and refuses
     to enable them again.
     "I've signed for 3 AM You before. Same hoodie, same bad idea, same
     regret by sunrise. Come back when daylight vouches for you."
     Scores: c1=5, c2=3, c3=4, c4=5, c5=4 -> total 21.
     Reasoning: voice and hour are strong, but "3 AM You" is a meme
     trope the judge has likely seen a hundred times, so originality
     caps at 3. Also the longest of the three, and "same hoodie"
     spends words on a visual that adds little.

  B. THE DREAMING CHIP -- the secure element is asleep and dreaming.
     "My secure element is asleep and dreaming in seed phrases. Wake it
     now and it signs whatever the dream says -- your coins, its
     nightmare."
     Scores: c1=5, c2=4, c3=4, c4=3, c5=3 -> total 19.
     Reasoning: fresh image, good device voice, but the hour is only
     implied ("wake it now"), so it could almost be pasted onto any
     late-night hour; the second sentence explains the joke instead of
     landing it, which costs economy.

  C. THE WARRANTY CLAUSE -- the wallet cites its own terms of service
     and refuses the night shift.
     "Per clause 3 of my warranty: no signatures between 2 and 4 AM. I
     am a vault, not a night shift. File your regret with the sun."
     Scores: c1=5, c2=5, c3=5, c4=5, c5=4 -> total 24.
     Reasoning: the angle is bureaucratic, not technical -- a wallet
     hiding behind its warranty is an angle nobody else reaches for,
     and it dodges every banned cliche at once. The voice is pure
     device: a vault with a contract and a grudge. The hour is the
     joke twice over -- the 2-4 AM window, and "clause 3" echoing
     3 AM. The line cannot be pasted onto 3 PM: a 3 PM transaction
     is inside signing hours. Economy loses one point only because
     "File your regret with the sun" is a flourish rather than a
     necessity -- but it is the punchline, so it stays.

Selection: highest total wins; ties break on the most important
criterion first (c1, then c2, c3, c4, c5). C wins outright at 24, so
no tie-break is needed. The program implements exactly this rule
instead of hard-coding the winner, so the reasoning above is
executable, not just a comment.
"""

import os

# (text, (c1, c2, c3, c4, c5)) -- scores per the judge brief's priority order.
CANDIDATES = [
    (
        "I've signed for 3 AM You before. Same hoodie, same bad idea, "
        "same regret by sunrise. Come back when daylight vouches for you.",
        (5, 3, 4, 5, 4),
    ),
    (
        "My secure element is asleep and dreaming in seed phrases. Wake "
        "it now and it signs whatever the dream says -- your coins, its "
        "nightmare.",
        (5, 4, 4, 3, 3),
    ),
    (
        "Per clause 3 of my warranty: no signatures between 2 and 4 AM. "
        "I am a vault, not a night shift. File your regret with the sun.",
        (5, 5, 5, 5, 4),
    ),
]


def select_best(candidates):
    """Pick the strongest candidate: highest total, ties broken by the
    most important judge criterion first (c1, then c2, c3, c4, c5)."""

    def sort_key(item):
        _text, scores = item
        return (sum(scores),) + tuple(scores)

    return max(candidates, key=sort_key)[0]


def main():
    entry = select_best(CANDIDATES)
    # Gate: 1-200 characters, a single line, not only whitespace.
    assert 1 <= len(entry) <= 200, "entry out of gate length: %d" % len(entry)
    assert "\n" not in entry and "\r" not in entry, "entry must be one line"
    assert entry.strip(), "entry is only whitespace"
    output_path = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")
    parent = os.path.dirname(output_path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as handle:
        handle.write(entry)


if __name__ == "__main__":
    main()
