# System Junk – Portfolio Project 3

![A screenshot of the application in action](docs/features/welcome-page.png)

## [Link to live web application](https://system-junk.herokuapp.com/)

---

## Project Documentation
### Welcome to [System Junk](https://system-junk.herokuapp.com/)

Sytem Junk is quiz game application built as a part of Code Institute’s full-stack web development course curriculum. It utilises pure Python3 and a collection of libraries to expand on the functionality of the project.

The present documentation will provide information critical to understanding the core design principles that enabled the development of the project. More specifically, details regarding the UX/UI development, application testing and deployment, code structure and maintainability, bug fixes and the planned future features for the project.

---

## Table of Contents

-   [The Story](#thestory)
-   [User Experience (UX)](#user-experience-ux)
    -   [Objectives](#objectives)
    -   [User Stories](#user-stories)

-   [Design Process](#design-process)
    -   [User Experience Design (UXD)](#user-experience-design-uxd)
    -   [Colour Palette](#colour-palette)

-   [Website Features](#website-features)
    -   [Shared Elements](#shared-elements)

-   [Future Features](#future-features) 

-   [Testing](#testing)
    -   [User Stories Testing](#user-stories-testing) 

-   [Validation](#validation)
    -   [Python](#python)

-   [Bug Fixes](#bug-fixes)

-   [Deployment](#deployment)

-   [Technologies Used](#technologies-used)
    -   [Hardware](#hardware)
    -   [Software](#software)
    -   [Platforms](#platforms)

-   [Credits and References](#credits-and-references)

-   [Closing Remarks](#closing-remarks)

---

## The Story

The concept of this application regards a traditional quiz game. System Junk is based on a fictional dystopian narrative created specifically for this project. In the year 2555, the player is presented with a story world where world societies have abandoned all pursuits outside of science. This was a direct result of the expiry of various natural resources, forcing humankind to seek refuge in the benefits found through progressing scientific knowledge. While this approach allowed humanity to survive, cultures changed their fundamental approach to arts and humanities where they only view it as redundant practices. Earth's nations are far away from their state 500 years ago, and most are only mere communities. Because of this, people still depend on science to find solutions to solve their biggest problems, and they expect all individuals to invest all their time in this area.

More established societies have institutionalized this approach where every citizen is periodically tested on their knowledge of the fundamentals of science. Those who succeed in these assessments are granted further freedoms and living standards. Those who fail these tests, however, are removed from the mainstream margins of society and discarded to the outskirts of civilization with little to no rights to protect their humanity. Mainstream societies view these groups as unworthy of the full care of their governments, and label them as "System Junk." These outcast communities have since developed into organized societies that aim to take back their fundamental rights. The fate of the world is unknown, but with the emerging activity in outcast communities and the existance of an unyielding opression from mainstream socities, it is only plausible to expect nothing but a worldwide uprise brewing in the future to come.

---

## User Experience (UX)

### Objectives

User Objectives

- Experience an enjoyable and brief quiz game application.
- Be provided information regarding the rules of the quiz.
- Have the ability to submit performance information with a unique username.
- Be presented with a report of the user's unique overall performance in the game.

Developer Objectives

- Develop a game software that is straightforward to play.
- Create a gameplay environment where the purpose of the game is clear to the player.
- Ensure that the user receives feedback on the various processes that occur during the game.
- Provide a game aesthetic that is unique to the game.


### User Stories

User

-   As a user, I want to be presented with a clear welcome section.
-   As a user, I want to be able to learn about the story of the game.
-   As a user, I want to quickly learn how to play the game before it starts.
-   As a user, I want to be presented with questions that are clear and concise.
-   As a user, I want to be able to view my answer options.
-   As a user, I want to receive feedback from the game about the correctness of my answer.
-   As a user, I want to receive feedback from the game when I do something that is not allowed.
-   As a user, I want the game application to tell me what it is doing before and after the quiz completion.
-   As a user, I want to be able to view a report of my results.
-   As a user, I want to be able to provide a username to save my performance data.
-   As a user, I want to be able to see a report of my overall game performance when I complete the game.
-   As a user, I want to be asked if I want to play the game again before the application terminates.

Developer

-   As a developer, I want the user to learn about the game narrative before the application begins.
-   As a developer, I want users to be provided feedback from the system whenever a new critical process is running.
-   As a developer, I want usernames, final scores and final score percentages to be uploaded to Google Spreadsheets.
-   As a developer, I want the user to be warned if they input invalid data or provide an incorrect answer.
-   As a developer, I want user data to be subject to a data validation process to ensure the quality of data and the smooth run of the program.

---

## Technical Design

### Flowchart
![Flowchart](docs/flowchart.png)

### Data Model

The data model of this application consists of compartmentalized code that is imported across different .py files to better manage the various functions in a manageable manner. The class structure present in the colours.py allows access to various colours with shortcuts that are specific to each colour. This way the predetermined elements in the Colorama library are shortened and made easy to access regarding the needs of this application.

As regards the quiz questions, a separate questions.py file is created to house all questions and choices of content to be used in the game. The logic of the code loops through both the QUIZ_QUESTIONS library and QUIZ_CHOICES list and prints these as a pair to the terminal. The correct answer is determined by comparing the question and answer key/value pair in the QUIZ_QUESTIONS list with the user input. Removing this section of the code from the run.py helped better manage the development process without making the code contained in the run.py file too crowded.

The database model of this project is arguably simple as the application itself did not require complex manipulation of user data. That being said, targeting specific and relevant data that the collection of which would add meaningful value to the application was a key consideration for the data model design. Thus, 3 data points, namely; 
    
    - username,
    - final score,
    - final score percentage

were identified as relevant to the goals of this project. This process is achieved by utilizing the combined functionality available in Google Drive API and Google Spreadheets API, where the application communicates with these services to upload relevant data to a target spreadsheet. Please find below a screenshot of the relevant Google Spreadsheet.

<details><summary>Screenshot</summary>
<img src="docs/gspread.png">
</details>

---

### Colour Palette


[Coolors](https://coolors.co/) was a highly beneficial resource in this regard which provided significant help in identifying
matching colours that also have appropriate contrast.

![Colour Palette](docs/colour-palette.png)

---

## Website Features

The design considerations that impacted the envisioned features were mainly structured around CLI-based considerations. While there were more features planned in the initial stages of the project, some were not entertained to the benefit of serving the needs referenced in the [User Stories](#user-stories) section. Thus, it was important to focus on a minimum viable project rather than prioritizing the implementation of further features for the sake of it. This would only bloat the application without adding much real value to the user experience overall.

### Application Elements

The below elements are available to be experienced by the user across the quiz game application as a whole.

#### Welcome Logo

![Welcome Logo](docs/features/welcome-page.png)

#### Game Story

![Game Story](docs/features/story.png)

#### Game Instructions

![Instructions](docs/features/instructions.png)

#### Questions & Choices

![Questions](docs/features/questions.png)

#### Answer Feedback

![Correct Answer](docs/features/answer-correct.png)
![Incorrect Answer](docs/features/answer-incorrect.png)
![Invalid Answer](docs/features/answer-invalid.png)

#### Username Input & Instructions

![Username Instructions](docs/features/username-instructions.png)
![Username Input](docs/features/username-input.png)

#### Quiz Results

![Quiz Resuts](docs/features/quiz-results.png)

#### System Feedback

![System Feedback](docs/features/system-feedback.png)

    There are many examples of the system feedback feature available throughout various sections 
    implemented in the application. As every instance of this feature serve the same purpose, 
    only one example is provided in the documentation to prevent repetition.

#### Player Performance

![Player Performance](docs/features/player-performance.png)

#### Game Restart

![Game Restart](docs/features/game-restart.png)

#### Quiz End 

![Quiz End](docs/features/quiz-end.png)

---

## Future Features

#### Leaderboard

- It is currently not possible to display a history of player data and compare the information in the database to structure a ranking system. However, the data already available in the Google Spreadsheets tied to the program is sufficient to implement this functionality. The development process for this project prioritized the completion of a minimum valuable product, thus removing a leaderboard feature from consideration. The future implementation of functionality like this would adequately expand upon its capacity to display information to the player.

---

## Testing 

### Manual Testing

<summary>User Stories Testing</summary>

1. As a user, I want to be presented with a clear welcome section.

| **Feature**   | **Action**                    | **Expected Result**          | **Actual Result** |
| ------------- | ----------------------------- | ---------------------------- | ----------------- |
| Welcome Logo | Run application | Users are presented with a logo. | Functions as intended |

<details><summary>Screenshot</summary>
<img src="docs/features/welcome-page.png">
</details>

2. As a user, I want to be able to learn about the story of the game.

| **Feature**   | **Action**                    | **Expected Result**          | **Actual Result** |
| ------------- | ----------------------------- | ---------------------------- | ----------------- |
| Animated Story Text | Run application | Users are presented with an animated story section. | Functions as intended |

<details><summary>Screenshot</summary>
<img src="docs/features/story.png">
</details>

3. As a user, I want to learn how to play the game before it starts.

| **Feature**   | **Action**                    | **Expected Result**          | **Actual Result** |
| ------------- | ----------------------------- | ---------------------------- | ----------------- |
| Instruction Text | Run application | Users are presented with game instructions. | Functions as intended |

<details><summary>Screenshot</summary>
<img src="docs/features/instructions.png">
</details>

4. As a user, I want to be presented with questions that are clear and concise.

| **Feature**   | **Action**                    | **Expected Result**          | **Actual Result** |
| ------------- | ----------------------------- | ---------------------------- | ----------------- |
| Questions | Run application | Users are presented with questions. | Functions as intended |

<details><summary>Screenshot</summary>
<img src="docs/features/questions.png">
</details>

5. As a user, I want to be able to view my answer options.

| **Feature**   | **Action**                    | **Expected Result**          | **Actual Result** |
| ------------- | ----------------------------- | ---------------------------- | ----------------- |
| Choices | Run application | Users are presented with choices. | Functions as intended |

<details><summary>Screenshot</summary>
<img src="docs/features/questions.png">
</details>

6. As a user, I want to receive feedback from the game about the correctness of my answer.

| **Feature**   | **Action**                    | **Expected Result**          | **Actual Result** |
| ------------- | ----------------------------- | ---------------------------- | ----------------- |
| Answer Feedback | Input Answer | Users are presented with a feedback depending on whether they input the correct or incorrect answer. | Functions as intended |

<details><summary>Screenshot</summary>
<img src="docs/features/answer-correct.png">
<img src="docs/features/answer-incorrect.png">
</details>

7. As a user, I want to receive feedback from the game when I do something that is not allowed.

| **Feature**   | **Action**                    | **Expected Result**          | **Actual Result** |
| ------------- | ----------------------------- | ---------------------------- | ----------------- |
| Invalid Input Feedback | Enter Invalid Input | Users are notified when their input is not allowed by the system. | Functions as intended |

<details><summary>Screenshot</summary>
<img src="docs/features/answer-invalid.png">
</details>

8. As a user, I want the game application to tell me what it is doing before and after the quiz completion.

| **Feature**   | **Action**                    | **Expected Result**          | **Actual Result** |
| ------------- | ----------------------------- | ---------------------------- | ----------------- |
| System Process Feedback | Run application | Users are presented with feedback from the system whenever a new process begins. | Functions as intended |

<details><summary>Screenshot</summary>
<img src="docs/features/system-feedback.png">
<img src="docs/features/quiz-end.png">
</details>

9. As a user, I want to be able to view a report of my answers.

| **Feature**   | **Action**                    | **Expected Result**          | **Actual Result** |
| ------------- | ----------------------------- | ---------------------------- | ----------------- |
| Quiz Answer Summary | Complete Quiz | Users are presented with a summary of their answers. | Functions as intended |

<details><summary>Screenshot</summary>
<img src="docs/features/quiz-results.png">
</details>

10. As a user, I want to be able to provide a username to save my performance data.

| **Feature**   | **Action**                    | **Expected Result**          | **Actual Result** |
| ------------- | ----------------------------- | ---------------------------- | ----------------- |
| Save Username and Score | Complete Quiz | Users are asked to provide a username. | Functions as intended |

<details><summary>Screenshot</summary>
<img src="docs/features/username-instructions.png">
<img src="docs/features/username-input.png">
</details>

11. As a user, I want to be able to see a report of my overall game performance when I complete the game.

| **Feature**   | **Action**                    | **Expected Result**          | **Actual Result** |
| ------------- | ----------------------------- | ---------------------------- | ----------------- |
| Performance Summary | Submit Username | Users are displayed their saved usernames, final scores and overall accuracy percentages. | Functions as intended |

<details><summary>Screenshot</summary>
<img src="docs/features/player-performance.png">
</details>

12. As a user, I want to be asked if I want to play the game again before the application stops.

| **Feature**   | **Action**                    | **Expected Result**          | **Actual Result** |
| ------------- | ----------------------------- | ---------------------------- | ----------------- |
| Game Restart Prompt | Submit Username | Users are presented with a prompt to choose between restarting or terminating the application. | Functions as intended |

<details><summary>Screenshot</summary>
<img src="docs/features/game-restart.png">
</details>
</details>

---

## Validation

### PYTHON

Code Institute's [Python Linter](https://pep8ci.herokuapp.com/) was the main resouce during the code validation process. The relevant code passes with overall success with occassional minor warnings.

<details><summary>PEP8 Validation: run.py</summary>
<img src="docs/testing/run-py.png">
<ul><li>The errors detected for this file come from the ASCII art implemented to display the logo of the game. While these warnings can be avoided by removing the logo art, this would take away from the identity of the game. There is also an instance of indenting code for visual purposes which helped keep the lines 100-101 from being too long.</li></ul>
</details>

<details><summary>PEP Validatation: questions.py</summary>
<img src="docs/testing/questions-py.png">
</details>

<details><summary>PEP Validatation: colours.py</summary>
<img src="docs/testing/colours-py.png">
</details>

<details><summary>PEP Validatation: database.py</summary>
<img src="docs/testing/database-py.png">
</details>

---    

## Bug Fixes

In this section, all bugs that cased fatal errors that prevented the successful execution of the application and their relevant fixes are provided.

| **Bug** | **Fix** |
| ------- | ------- |
| get_username() 'None' Text Display: A bug where a 'None' text appeared during when the system was expecting input from the user for their username. | Fixed by removing the print element nested inside an outer input element. Click [here](https://github.com/beratzorlu/python-quiz/commit/d3fc300dc47d88aecd65f99b7ab7cbb6ca6f13b7) to review the relevant commit. |
| Unexpected Game Restart Bug: A bug causing the game to restart the game automatically without asking for input after the user chooses to restart the game at their first go. | Fixed by removing the while loop in the main() function. Click [here](https://github.com/beratzorlu/python-quiz/commit/8e7f2c66ffeeeeec7f6998f9da32b7d5518b647e) to review the relevant commit. |
| Invalid Question Answer Bug: A bug where the application would accept input other than A, B, C, or D and register it as an incorrect answer. | Fixed by adding two seperate functions that accept and then validate the user input before passing it to answer check process. Click [here](https://github.com/beratzorlu/python-quiz/commit/c201cb2e448cf5d6f93e1de7d2fe05eb9b4351a3) to review the relevant commit. |

---

## Deployment

---

## Technologies Used

### Hardware

- Monster Abra A5 V13.4 15.6" Laptop
- Samsung VA 1920x1080 144Hz Curved Gaming Monitor
- iPhone 7 Plus
- Samsung Galaxy A51

### Software

- Mozilla Firefox: Main browser used for development, testing and device simulation.
- Google Chrome: Secondary browser for testing and device simulation.
- Microsoft Edge: Tertiary browser for testing.
- Firefox Mobile: Mobile testing of the deployed site.
- Chrome Mobile: Mobile testing of the deployed site.
- Safari Mobile: Mobile testing of the deployed site.
- GIMP: Used for converting .jpg and .png files to .webp for site optimization.
- Balsamiq: Used for wireframing.
- Windows Snip & Sketch: Capturing screenshots for readme and archiving identified bugs.
- Microsoft Snipping Tool: Fallback screen capture software when MS Snip & Sketched became unresponsive.

### Platforms

- GitHub: Version control and site deployment.
- GitPod: Integrated Development Environment (IDE) chosen for this project.
- Pexels: Primary source for high-quality royalty-free images.
- Pixabay: Secondary source for high-quality royalty-free images.
- Google Fonts: Finding and exporting third-party fonts for the website.
- CodePen: For quickly testing out ideas before carrying them to 
DevTools.
- Font Awesome: For importing fonts to further decorate text elements.
- Coolors: For creating a matching colour palette that has appropriate contrast.
- Code Beautify: For looking for differences between two pieces of code. This helped me identify my mistakes.

---

## Credits and References


--- 

## Closing Remarks


---
 [Back to Top]()