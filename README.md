# Introduction

The purpose of this bot is to integrate the newly learned things : <br>
→ Chained list <br>
→ Hashmap <br>
→ Binary tree 

The data structures have been manually made which entails the creation of multiple elements like the node itself which has the information of the next node with his own value, the chained list having its first node, etc. <br>

### A few things to note
→ This project has been made inside Google Colaboraty and the installation process will be tailored to be compatible for colab <br>
→ In the **bot/run.py**, you must replace the ```bot.run("YOUR-BOT-TOKEN")``` with your own bot token. <br>
→ The conversation tree is not tied to a specific user. This means that any user can advance the same conversation.

## Project Structure Overview

### • *require*
This folder contains the code needed for the bot to run inside Google Colaboratory.

### • *bot*
This folder contains all commands / events or any other function that is related to the functionnality of the bot.

### • *class*
This folder contains all classes used inside **bot/run.py**

# Bot

## Commands

In this section, you'll find detailed descriptions of all the commands available to use. <br>

The command will be highlighted and should be written in discord as it is written here. All commands have the prefix "**!**". 

### ```!help```
Used for getting a description of all commands available. Same purpose as this section but less detailed.

### ```!test_command```
Used for testing if a command works as well as adding it to the history of commands that every user has.

### ```!start_conversation```
Used for starting a quick chat where the bot will ask you some questions that you may or may not need help with.

### ```!reset_conversation```
Used for restarting a conversation that has ended. A conversation has reached its end when the bot responds by giving you an answer to the wanted question, and if you want to continue, a message indicating that the conversation has ended will appear. Note, you don't have to reach the end of the conversation to use this command.

### ```!speak_about```
Used for asking the bot if the conversation mentions a specific topic. Remember, after typing the command, you must pass it a parameter or an error will appear. The parameter will be simply written after the command (and a space).

### ```!show_hashmap```
Used for displaying the hashmap. The hashmap contains the user ID which is used as the key and a chained list as the value. The chained list is the history of commands. Note, every user has their own history of commands and this history will deleted as soon as the bot is turned off.

### ```!last_command```
Used for showing the last command used. Note, each command will have a number in parantheses (like this (2)). This number represents the index in the chained list. Having 2 means that this is the 3rd element in the commands history.

### ```!move_up_history```
Used for showing the next command used in the history of commands.

### ```!move_down_history```
Used for showing the previous command used in the history of commands.

### ```!show_history```
Used for showing the history of commands of the user that has typed this command.

### ```!delete_history```
Used for deleting the history of commands.

### ```!find_words```
Used for finding words from the English alphabet from random letters. This function will need a parameter in which you can type any letter or combination of letters and the bot will give you 50 words that you can make with those combinations of letters. Note, words that are shorter than 3 letters will not be shown. In addition, the words shown will not necessarily contain all the letters that you have used. It searches words that can you made with your combination of letters but will not try to use every letter.