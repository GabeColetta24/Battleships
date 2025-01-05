# Battleships

My goal with this project was to create a Battleships game vs the Computer. I wanted my game to be easy to understand for people who aren't familiar with the game. I made my game on a 5x5 grid to increase the chances of a hit on each of the players shot attempts to keep the player more engaged rather than getting miss after miss, which could result in the player leaving before the game is over.

## Planning

I created a flowchart to give me a visual idea of how I wanted my game to work.

![Flowchart of game](assets/documentation/battleship-flowchart.png)

I used this flowchart to help me write my Python code. This flowchart allowed me to understand the structure of my game better which made it easier to write my code. It also gave me an end goal of how I wanted my game to work.

## Instructions

Ships will be randomly placed

Player chooses coordinates from 0-4  e.g. (2,4)

Wait for result if hit or miss

Computer will choose coordinates 

Wait for result if hit or miss

Repeat until or ships are sunk

## Testing

Once I finished writing my python code I tested the game to make sure all of the components were working as intended. I then deployed to Heroku and tested everything again to make sure it was working correctly.

I had no bugs when testing my game

## Deployment

I deployed my project to Heroku. To do this I had to set up an account with Heroku, I then selected create an app and chose a unique name for my app and set my region to Europe. In settings I added python and nodejs buildpacks and a Config Vars. I then manually deployed my project to Heroku. The live link can be found here - https://battleships-gcoletta-f205116c7c9d.herokuapp.com/