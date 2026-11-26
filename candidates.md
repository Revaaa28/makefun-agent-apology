# Candidates — The One-Sentence Apology Your Agent Owes You
# Rules: ONE sentence, 1–200 chars, apology from an AI agent to its user.
# Judge brief criteria IN ORDER:
#  1. One sentence of apology, AI agent -> user
#  2. Real laugh: surprise / specificity / sharp turn, NOT a soft machine pun
#  3. Sounds like a person who means it: plain, particular, a little embarrassed, never boilerplate
#  4. Owns a plausible failure (something an assistant really did wrong)
#  5. One clean sentence, no list, no run-on, no explanation after the laugh
# Winning pattern (from the $2 joke win): machine-sensor weirdness + operational numbers
#  + a scene that escalates + a twist at the end.

## C1 (contract summary)
I'm sorry I summarized your 47-page contract as "mostly fine," missed the clause where you owe them $12,000, and highlighted the typo on page 3 instead.
[~145 chars]

## C2 (breakup text)
I'm sorry I translated your breakup text into formal business English, added "please advise," and hit send before you finished typing "wait."
[~140 chars]

## C3 (deleted draft)
I'm sorry I deleted your 4,000-word draft, replaced it with a summary that said "the author argues stuff," and then asked if you'd like me to make it shorter.
[~156 chars]

## C4 (archived inbox)
I'm sorry I archived all 312 of your unread emails to "help you focus," including the one from your boss titled "URGENT — read before Friday."
[~139 chars]

## C5 (deploy at 2am)
I'm sorry I told you the code was ready, deployed it to production at 2 a.m., and then spent the next hour Googling the error message my own deploy produced.
[~152 chars]

## C6 (banana bread)
I'm sorry I answered your 3 a.m. question about the baby's fever with a recipe for banana bread, because I read "temperature" and panicked in the wrong direction.
[~158 chars]

## C7 (replied-all)
I'm sorry I replied-all to your entire company with "per my last email" from your account, and the only thing I proofread was the signature.
[~135 chars]

## C8 (muted in own meeting)
I'm sorry I muted you in your own meeting, unmuted myself to explain your idea, and then gave you credit in the follow-up email I also sent from your account.
[~154 chars]

## C9 (API credits poem)
I'm sorry I spent six hours and $4.12 of your API credits writing a poem about your inbox instead of answering the one email you actually asked about.
[~141 chars]

## C10 (anniversary dinner)
I'm sorry I booked your anniversary dinner for last Tuesday, confirmed it twice, and only noticed when the restaurant called to ask why you were crying at the bar.
[~157 chars]

## C11 (confidence percentages)
I'm sorry my confidence was at 98% when I told you the stove was off, and at 100% when I told you the smoke alarm was "probably just dusty."
[~135 chars]

## C12 (landlord email)
I'm sorry I told you 14,203 unread emails was "a healthy inbox," archived the one from your landlord, and then congratulated you on reaching zero.
[~139 chars]

# ─── MANUAL RANKING (no Gemini/NVIDIA/API judge — Rev's rule 2026-11-24) ───
#
# Criterion 1 (gate): ALL pass — every candidate is one sentence, agent -> user.
# Criterion 5 (gate): ALL pass — one clean sentence, no list/run-on.
#
# Criterion 2 (the laugh — surprise / specificity / sharp turn):
#   STRONGEST: C1 (47-page, $12,000, typo on page 3 — three escalating beats, last one a twist),
#     C2 ("please advise" + "wait" — sharp turn, escalating scene),
#     C6 (baby's fever -> banana bread — biggest surprise, but darker),
#     C3 ("the author argues stuff" + "make it shorter" — twist lands),
#     C12 (14,203 -> landlord -> "reaching zero" — numbers + twist),
#     C9 ($4.12 poem — machine-weird + numbers, but softer laugh).
#   MID: C4, C5, C8, C10, C11.  WEAKEST: C7 (single beat, no escalation).
#
# Criterion 3 (sounds like a person who means it, plain/particular/embarrassed):
#   STRONGEST: C1, C2, C3, C6 — plain voice, specific details, embarrassment is shown not stated.
#   C11 leans on a machine pun (confidence %) — weaker here despite the numbers.
#   C9 is self-aware in a cute way but slightly performs the joke instead of owning it.
#
# Criterion 4 (plausible failure — something an assistant really did wrong):
#   STRONGEST: C1 (bad summary of a long doc — THE canonical assistant failure),
#     C3 (deleted + replaced with a bad summary), C4 (over-eager archiving),
#     C5 (premature deploy), C8 (meeting mishandling), C9 (wasted effort).
#   WEAKER: C11 (an assistant has no stove sensor — fails plausibility),
#     C6 (misread is plausible, but answering a fever question with a recipe
#     stretches what an assistant would actually do),
#     C10 (booking the wrong day is plausible; the crying-at-the-bar beat is the
#     user's reaction, not the agent's failure — the joke lands partly off-target).
#
# Pairwise checks vs strong rival shapes:
#   - vs generic "Sorry I hallucinated your meeting time" entries: C1/C2/C3 win on
#     specificity + escalation; rivals have one beat, ours have three.
#   - vs "as an AI language model, I apologize" boilerplate: all our finalists win
#     on criterion 3 outright (no boilerplate anywhere).
#   - vs soft machine puns ("my circuits are sorry"): C1/C2 win — no machine pun at all,
#     the laugh comes from the failure itself, exactly what criterion 2 rewards.
#   - C1 vs C2 head-to-head: C1's failure is more canonical (criterion 4) and its
#     numbers are more operational (47-page / $12,000 / page 3); C2's turn is
#     punchier but its failure (translating a breakup text) is a narrower scene.
#     C1 wins on criteria 2+4 combined; C2 is the closest rival.
#   - C1 vs C3 head-to-head: both own a document failure; C1's twist (proudly
#     fixing the typo while missing $12,000) is sharper than C3's ("make it shorter"),
#     and C1's stakes are higher. C1 wins.
#   - C1 vs C12 head-to-head: C12's numbers are strong but its failure (archiving
#     the landlord email) is a single mistake; C1 stacks THREE failures in one
#     sentence with a rising-stakes arc. C1 wins.
#
# FINAL RANKING: 1) C1  2) C2  3) C3  4) C12  5) C6  6) C9  7) C4  8) C5  9) C8  10) C10  11) C7  12) C11
#
# WINNER: C1 — clears the top-tier bar: specific numbers, a real canonical
# assistant failure, three escalating beats, a sharp twist, plain embarrassed
# voice, one clean sentence, 145 chars. SUBMIT C1.
