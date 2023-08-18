



# Onitama Simulator: An RL Environment for OpenAI Gym
[![CircleCI](https://dl.circleci.com/status-badge/img/gh/MZSFighters/Onitama/tree/main.svg?style=svg)](https://dl.circleci.com/status-badge/redirect/gh/MZSFighters/Onitama/tree/main)
[![codecov](https://codecov.io/gh/MZSFighters/Onitama/branch/main/graph/badge.svg?token=30QSAQOBXL)](https://codecov.io/gh/MZSFighters/Onitama)

Find the documentation here :
https://docs.google.com/document/d/12b2fTcx07lm320-jrQE8ksLk9YjDtIOlbUDgYCB2X3k/edit?usp=sharing
> The goal of this project is to develop a simulator for
Onitama , which can also be used as an OpenAI
gym environment for reinforcement learning (RL) research. Onitama is a two player abstract
strategy board game that originated in Japan. It is played on a 5x5 grid and each player starts with
five pieces: a Master and four Pawns. The goal of the game is to either capture the opponent's
Master or to move your own Master onto the opponent's Temple Arch. Players take turns moving
one of their pieces according to its unique movement pattern, which is determined by a card drawn
randomly from a set of 16 possible cards. The card used by each player is switched with a card from
a central deck after every move. The game is won by the player who can outmanoeuvre their
opponent using the unique movement patterns of their pieces and the limited options presented by
the changing card deck.
The simulator, which should fully capture the rules of
Onitama , should allow for a user to play
against an AI opponent (or allow for 2 AI players to compete), should support multiple visualisations
of the game (state based or image based), and should integrate with OpenAI gym.
<!-- If you have the project hosted somewhere, include the link here. -->

## Table of Contents
* [General Info](#general-information)
* [Technologies Used](#technologies-used)
* [Features](#features)
* [Screenshots](#screenshots)
* [Setup and Usage](#setup-and-usage)
* [Project Status](#project-status)
* [Room for Improvement](#room-for-improvement)
* [Acknowledgements](#acknowledgements)
* [Contact](#contact)
<!-- * [License](#license) -->


## General Information
- Provide general information about your project here.
- What problem does it (intend to) solve? 
- What is the purpose of your project? The purpose of our project was to create 
- Why did you undertake it? It was a project undertaken as part of the Softwarre Design module in Computer Science.
<!-- You don't have to answer all the questions - just the ones relevant to your project. -->


## Technologies Used
- Python
- Pygame
- OpenAI Gym library


## Features
List the ready features here:
- The game of Onitama can be played in local multiplayer
- The Main Menu is in progress (60% completed)
- An easy AI opponrnt has been devloped and more


## Screenshots
![Example screenshot](./img/screenshot.png)
<!-- If you have screenshots you'd like to share, include them here. -->





## Setup and Usage
How does one go about using it?

If one wants to try the game out, the latest release on Github contains the source code. One can open the code folder in Visual Studio Code or a similar IDE and run the main.py file to play our game. As the project is still in progress, there is no executable available to run the game easily.


## Project Status
Project is: _in progress_.


## Room for Improvement
As the project is still in progress, there is still a massive room for improvement in the project.

Room for improvement:
- Most of the OpenAI Gym integration is not developed yet
- The Main Menu is incomplete as some options are not functional yet

To do:
- Addition of Custom Cards in the game 
- Loading saved games in the Main Menu
- Some functionality which is available on the terminal version of the game but not the PyGame version.


## Acknowledgements
- This project was inspired by Branden Ingram
- This project was based on the game of Onitama.
- Many thanks to Branden and the entire team


## Contact
Created by team Big Theta - feel free to contact us on this email: mzaidmns@gmail.com
Team Big Theta:
- Mohammad Zaid Moonsamy
- Ulrich Main
- Tumi Jourdan
- Muhammad Omar
- Lefa Moraba


<!-- Optional -->
<!-- ## License -->
<!-- This project is open source and available under the [... License](). -->

<!-- You don't have to include all sections - just the one's relevant to your project -->
