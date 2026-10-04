# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- The game ran but the hints were directed the wrong way. 
- The score also seemed to be going up after i gave it a wrong guess. 
- The range of number which depends on the difficulty level was also not accurate. 

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input | Expected Behavior | Actual Behavior | Console Output / Error |
|-------|-------------------|-----------------|------------------------|
| Guess 70, secret 40 | "Go LOWER" | "Go HIGHER" (hint messages were swapped) | None |
| Difficulty set to Easy | Info box says "between 1 and 20" | Always said "between 1 and 100" | None |
| Type a number, click Submit once | Hint appears | Needed two clicks | None |

---

## 2. How did you use AI as a teammate?

- I used claude in the chat for the explanation and to plan how to fix ii and then I used Claude Code in VS code to make edits and write tests. 
- Claude pointed out that app.py converted the secret to a string on even attempts and suggested removing if/else and passing st.session_state.secret straight into the check_guess. I took this suggesstion and i verified it by checking that the diff was one new line and playing the game with guesses of different digit lengths. 
- Claude told me to trust only odd-numbered attempts, then admitted it was backwards, because attempts goes up before the check so my first guess was already even. I caught it by testing in the browser instead of trusting the advice.

---

## 3. Debugging and testing your fixes

- I decided a bug was fixed only when I saw the correct behavior both in the live game and in a test, not just because the AI said so. For the hints, I opened Developer Debug Info to see the secret and guessed above and below it.
- One test I ran was test_guess_too_high with pytest. It calls check_guess(60, 50) and asserts that the outcome is "Too High" and that the message contains "LOWER". This test would have failed on the original code, because the hint messages were swapped and it said "Go HIGHER" for a guess that was too high. It showed me that the problem was in the hint messages themselves and that my fix in logic_utils.py worked. I ran python -m pytest -v and all 10 tests passed.
- AI helped me decide what to test and explain the failures. It explained the timeout and the tuple mismatch, and I used git diff to confirm it only changed what I asked.

---

## 4. What did you learn about Streamlit and state?

- Streamlit reruns your whole script from top to bottom every time you click a button or change a widget. Because of that, normal variables reset on every rerun, like a notebook that gets wiped each time.
- st.session_state is a dictionary that survives reruns, so I use it to store things like the secret number, attempts, score, and history.


---

## 5. Looking ahead: your developer habits

- One habit I want to reuse is working on one bug at a time and making a small commit after each fix, with a test that fails on the old code and passes on the new code. 
- Next time I would write more specific prompts from the start, naming the function, the bug, and the exact expected values. 
- This project changed how I think about AI-generated code: it can look confident and still be wrong, so I need to read the diff and test it myself instead of trusting the summary.
