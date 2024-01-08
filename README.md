## Table of Contents

- [Introduction](#introduction)
- [Project Structure Overview](#project-structure-overview)
- [Installation](#installation)
- [Commands](#commands)
- [Sources](#sources)

## Introduction

The purpose of this bot is to integrate the newly learned things : <br>
• Chained list <br>
• Hashmap <br>
• Binary tree 

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

## Bot

## Installation
In this section, you'll find how to integrate this bot and use it in your own discord server. 

Note, this will not touch on the subject of how to create a bot or how to add it to your own server.

As shown above, in the **Project Structure Overview**, there are multiple elements that are required for the bot to work.

### Steps
**(1)** You must first create a new Google Colaboratory file.

**(2)** You will then take each block of code and add it to a cell. Each block of code, meaning each **file_name.py** will be added to their own cell inside the colab file. I recommend that you have the **require/require.py** at the top, following that, the **bot/run.py** and ending with each individual file inside **class/**.

**(3)** You then need to execute the code of each cell for them to be taken into account and making sure that there's no errors in the cell. For this, there is a little circle with an arrow inside on the top left corner of the cell. You must have a green tick next to that circle after executing. You can execute them in any order except the bot cell itself, which will be ran at the end.

**(4)** Add your own bot token that is located at the end of the bot cell.

**(5)** Execute bot cell and you should have a message saying **Bot has connected to discord !**. The bot should now be online in your discord server and ready for use.

## Commands

In this section, you'll find detailed descriptions of all the commands available to use. <br>

The command will be highlighted and should be written in discord as it is written here. All commands have the prefix "**!**". 

#### ```!help```
Used for getting a description of all commands available. Same purpose as this section but less detailed.

#### ```!test_command```
Used for testing if a command works as well as adding it to the history of commands that every user has.

#### ```!start_conversation```
Used for starting a quick chat where the bot will ask you some questions that you may or may not need help with. You must answer with **no** or **yes**. Any other message will not advance the conversation.

#### ```!reset_conversation```
Used for restarting a conversation that has ended. A conversation has reached its end when the bot responds with an answer to question. If you want to continue, a message indicating that the conversation has ended will appear. Note, you don't have to reach the end of the conversation to use this command.

#### ```!speak_about```
Used for asking the bot if the conversation mentions a specific topic. Remember, after typing the command, you must pass it a parameter or an error will appear. The parameter will be simply written after the command (and a space).

#### ```!show_hashmap```
Used for displaying the hashmap. The hashmap contains the user ID which is used as the key and a chained list as the value. The chained list is the history of commands. Note, every user has their own history of commands and this history will deleted as soon as the bot is turned off.

#### ```!last_command```
Used for showing the last command used. Note, each command will have a number in parantheses (like this (2)). This number represents the index in the chained list. Having 2 means that this is the 3rd element in the commands history.

#### ```!move_up_history```
Used for showing the next command used in the history of commands.

#### ```!move_down_history```
Used for showing the previous command used in the history of commands.

#### ```!show_history```
Used for showing the history of commands of the user that has typed this command.

#### ```!delete_history```
Used for deleting the history of commands.

#### ```!find_words```
Used for finding words from the English alphabet from random letters. This function will need a parameter in which you can type any letter or combination of letters and the bot will give you 50 words that you can make with those combinations of letters. Note, words that are shorter than 3 letters will not be shown. In addition, the words shown will not necessarily contain all the letters that you have used. It searches words that can you make with your combination of letters but will not try to use every letter.

## Sources

In this section, you'll find the multiple sources that I have used for multiple things across this project.

### Chatgpt
→ Get some specific attributes from **context** like **ctx.invoke_with** which returns the command name without the prefix "**!**"

→ Using **@commands.check(function_name())** before a bot command. This will be ran before the bot command and will exit out of the command if the function returns False.

→ Learned of multiple special methods that can be overwritten like : <br>
**__iter__** which signifies iteration. This is needed for the object to be iteratable, meaning using the for loop. <br>
**__getitem__** which allows the use of brackets [] for indexing.

→ Learned that the bot has an attributes called **bot.commands** that can be used to get every command. In addition, if specified when creating the command, you can use **command.help** to get the description of the command. This is how you can do it :
```@bot.command(name="add_command", help=”description here”)```

→ There is a method called **bot.process_commands(message)** which if called will iterate through every command and check if the parameter corresponds to any command.

→ Everything about nltk so things like import or nltk.download() etc

→ Learned about set() which makes a string into an unordered collection of unique elements. In this case, it is used to separate the **word** and the **letters** into a collection of unique elements to compare them

### Stackoverflow
→ https://stackoverflow.com/questions/62771154/discord-py-rewrite-sending-an-error-message-when-there-is-an-unknown-command-or <br>
For the on_command_error

→ https://stackoverflow.com/questions/45951224/how-to-remove-or-change-the-default-help-command <br>
Remove default “help” command





