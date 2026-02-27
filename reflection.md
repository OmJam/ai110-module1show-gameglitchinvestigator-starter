# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the secret number kept changing" or "the hints were backwards").

- When entering my guess, the hint told me to go lower even though the secret was clearly higher than my guess.
- You can input wrong inputs like negative numbers or numbers out of the range
- With 1 attempt left, the game says I am out of attempts and gives me the wrong score.
- When you press new game only the Secret number resets, and nothing else

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

- I used the Claude Code in VS Code to help complete this project.
- When I created comments and referenced specific lines from the app.py, the AI was able to get all context about what the bug was
- and fix it. It correctly fixed the bug regarding the check_guess function in app.py and explained it
- When I referenced a specific bug and lines, Claude tried to also fix other bugs in the code so I had to instruct it
- to only fix the specified bugs. Also it refactored the check_guess function and put it into logic_utils.py, but it
- never imported it in app.py.

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

- I reviewed the code that Claude generated to see if it makes sense. Then I tested the functionality in the
- app. I had Claude generate pytest cases and ran it to make sure they all passed
- AI helped me generate the pytest cases and I looked over them to make sure they made sense

## 4. What did you learn about Streamlit and state?

- In your own words, explain why the secret number kept changing in the original app.
- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
- What change did you make that finally gave the game a stable secret number?

- The secret number kept changing because it kept being randomized with a range from 1 - 100.
- Streamlit reruns and session states are like refreshing a page almost. It clears or changes what the app
- will do/ progress the website. Passing in the low and high variable for the seceret made it so the range is predictable.

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.

- Creating test cases is something that is very important when using AI to work in a project. Giving
- AI as much context like @ ing specific lines of code, helps the AI focus on what needs to be changed.
- I will use AI more sparingly and first get a full understanding about the code before trying to change it with AI
- AI really does help find bugs and fix them, but it is also important to review what the AI is doing and why its doing it.
- Without understanding what is happening, the project can become very messy and confusing.
