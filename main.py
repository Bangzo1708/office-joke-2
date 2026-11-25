"""The Funniest Office Joke, Judged Head to Head.

Program writes ONE one-line office joke to /output/entry.txt
(or the path in env ENTRY_OUTPUT). Fully deterministic: no random,
no clock, no network, no external dependencies.

Gate (competition.yaml): entry.txt must be UTF-8 text of 1-200
characters, not only whitespace, a single line, punchline last.

----------------------------------------------------------------
CANDIDATE SELECTION (3 genuinely different angles, scored 0-5
against the judge brief, in the judge's own priority order):

  1. Real one-line joke about office life: setup + turn.
  2. Turns on something anyone who has worked in an office knows.
  3. Surprises: a turn the reader does not see coming, not a
     plain complaint.
  4. Lands in one line: every word earns its place, punchline last.
  5. Feels new, not a joke already going round the office.

Candidate A -- the mute button (identity angle):
  "I've been on mute so long that my team now introduces me as
  'the quiet one who types in the chat'."
  Scores: 1) 4 -- setup ("on mute so long") + turn (introduced
  as a job title), 2) 5 -- muting is universal post-2020 office
  life, 3) 3 -- the direction is guessable once "mute" appears,
  4) 4 -- one line, punchline last, 5) 3 -- mute jokes are
  common. TOTAL 19.

Candidate B -- the out-of-office reply (boundaries angle):
  "My out-of-office reply says I'm on holiday, which is the only
  time my inbox has ever respected my boundaries."
  Scores: 1) 4 -- setup (out-of-office) + turn (inbox respecting
  boundaries), 2) 4 -- out-of-office is universal, 3) 4 -- the
  "boundaries" turn is unexpected, 4) 4 -- one line, punchline
  last, 5) 3 -- out-of-office jokes are well worn. TOTAL 19.

Candidate C -- the declined meeting (recursive-loop angle):
  "I declined a meeting to get work done, so they booked a
  meeting to discuss why I declined the meeting."
  Scores: 1) 5 -- clean setup + turn: the act of declining
  creates the very thing declined, 2) 5 -- meeting overload is
  the most universal office experience there is, 3) 5 -- the
  recursive loop is a genuine surprise, not a complaint restated,
  4) 5 -- tight, every word earns its place, punchline last,
  5) 4 -- "meeting about a meeting" is known, but the
  decline-punished-by-a-meeting twist is a fresher turn on it.
  TOTAL 24.

DECISION: Candidate C wins outright (24 vs 19 vs 19). No tie-break
needed. It is the strongest on the judge's top criterion (a real
joke with a setup and a turn), on universality, and on surprise --
the three criteria the judge weighs first and hardest.
----------------------------------------------------------------
"""

import os

# The winning joke: 102 characters, one line, punchline last.
JOKE = (
    "I declined a meeting to get work done, so they booked a "
    "meeting to discuss why I declined the meeting."
)


def main() -> None:
    output_path = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")
    parent = os.path.dirname(output_path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as handle:
        handle.write(JOKE)


if __name__ == "__main__":
    main()
