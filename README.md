# Mindflex Server

<!-- HEADER -->
<p align="center">
<!-- Logo -->
    <img src="./assets/Logo1024x1024.png" alt="Mindflex Logo" width="300px" >
<!-- Tagline -->
    <p align="center">
        <em>Flex your mind</em>
    <br/>
    </p>
</p>

<!-- BODY -->
# Table of Contents
1. [About](#about)
    * [Tech Stack](#tech-stack)
    * [Endpoints and Objects](#endpoints-and-objects)
2. [Coming Soon](#coming-soon)
    * [User Accounts](#user-accounts)
    * [Game Modes](#game-modes)
    * [Sound Effects](#sound-effects)
4. [Contact](#contact)

# About
A Python-Flask server that contains API endpoints and routes that support [Mindflex](https://github.com/yoshiohasegawa/mindflex), an iOS game application. The database is a noSQL MongoDB database.

## Tech Stack
- [Python](https://www.python.org/)
- [Flask](https://flask.palletsprojects.com/en/2.0.x/)
- [MongoDB](https://www.mongodb.com/)

## Endpoints and Objects
### *Root* 
- `[GET] /`
    * response: *Welcome to the Mindflex API*

### *Questions*
- `[GET] /api/questions`
    * response: ```{_id: "1991fakeid1991", question: "47 > 7", answer: true}```

# Coming Soon
### User Accounts
- We hope to enable users to create User Accounts in order to keep track of high scores.
### Game Modes
- Different game modes will keep things exciting and, allow users to not only challenge themselves in arithmetic but, also in other topics found in basic trivia.
### Sound Effects
- Sound effects and audio makes games like this much more fun! Keep an eye out for this in the near future.

# Contact
For support, feedback or, to report a bug, you may contact the maintainer:
- Yoshio Hasegawa: [GitHub](https://github.com/yoshiohasegawa), [LinkedIn](https://www.linkedin.com/in/yoshiohasegawa/)

## License
Distributed under the MIT License.