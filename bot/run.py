# RUN DISCORD BOT

import discord
from discord.ext import commands

# Download resource 'words' to be able to use it
import nltk
nltk.download('words')

# Import from Natural Language Toolkit (NLTK) library
# This contains a list of English words
from nltk.corpus import words
nltk.download('words')

# Give bot all rights
intents = discord.Intents.all()

# Create bot
bot = commands.Bot(command_prefix="!", intents = intents)

# Remove default command 'help' to create a custom 'help' function
bot.remove_command('help')

# If needed, increase hashmap size
user_hashmap = Hashmap(10)

conversation_tree = Conversation_tree()
conversation_tree.setup()

# // --------------------------------------------------------------------- \\ #
  ### Functions ###
# // --------------------------------------------------------------------- \\ #
  # Check if command has been types by the bot itself

def not_bot(context) :
  return context.message.author != bot.user

# // --------------------------------------------------------------------- \\ #
  # Add an user to the hashmap with his own history of commands

def user_in_hashmap(context) :
  if not user_hashmap.contains(context.author.id) :
    user_hashmap.set(context.author.id, Chained_list())

  # The purpose of this function is to ONLY add the user to the hashmap
  # ==> so always return True to pass commands.check()
  return True

# // --------------------------------------------------------------------- \\ #
  # Add command to history

def add_command_to_history(context) :
  user_id = context.author.id
  command_used = context.invoked_with

  # Get commands history (chained_list) from hashmap using user ID
  history_commands_user = user_hashmap.get(user_id)

  # Add command used to user commands history
  history_commands_user.append(command_used)

# // --------------------------------------------------------------------- \\ #
  ### BOT Commands ###
# // --------------------------------------------------------------------- \\ #
  # Help commands

@commands.check(not_bot)
@commands.check(user_in_hashmap)
@bot.command(name='help', help="Shows this message")
async def help_commands(context) :
  add_command_to_history(context)

  result=""

  # Iterate through every command created in ### BOT Commands ###
  for command in bot.commands :
    result += f"**{command.help}**" + f"```!{command}```\n"

  # Send message to discord channel
  await context.message.channel.send(result)

 # // --------------------------------------------------------------------- \\ #
  # Test command

@commands.check(not_bot)
@commands.check(user_in_hashmap)
@bot.command(name='test_command', help="Test command")
async def add_command_to_list(context) :
  add_command_to_history(context)

  # Send message to discord channel
  await context.message.channel.send("```'test_command' has been added to history```")

# // --------------------------------------------------------------------- \\ #
  # Start conversation tree

@commands.check(not_bot)
@commands.check(user_in_hashmap)
@bot.command(name='start_conversation', help="Start a conversation with the bot")
async def start_conversation_tree(context) :
  add_command_to_history(context)

  # Set True to indicate that the conversation has started
  # And messages like "no" or "yes" will be taken as answers and advance the conversation
  conversation_tree.ongoing_conversation = True

  conversation_message = conversation_tree.get_current_message()
  await context.message.channel.send(conversation_message)

# // --------------------------------------------------------------------- \\ #
  # Reset conversation

@commands.check(not_bot)
@commands.check(user_in_hashmap)
@bot.command(name='reset_conversation', help="Reset conversation")
async def reset_conversation_tree(context) :
  add_command_to_history(context)

  conversation_tree.reset_conversation()
  await context.message.channel.send("Restarting conversation... You can now use the command **!start_conversation**")

# // --------------------------------------------------------------------- \\ #
  # Conversation search topics

@commands.check(not_bot)
@commands.check(user_in_hashmap)
@bot.command(name='speak_about', help="Ask if the bot has information on a particular topic")
async def conversation_speak_about(context, topic_search) :
  add_command_to_history(context)

  # Send message to user based on result
  result = conversation_tree.search_topic(topic_search)
  if result == True :
    await context.message.channel.send(f"The bot has information on your topic : **{topic_search}**")
  else :
    await context.message.channel.send(f"The bot has no idea what **{topic_search}** means")

# // --------------------------------------------------------------------- \\ #
  # Display user hashmap

@commands.check(not_bot)
@commands.check(user_in_hashmap)
@bot.command(name='show_hashmap', help="Show all users ID and their commands history")
async def display_hashmap(context) :
  add_command_to_history(context)

  # Send message to discord channel
  await context.message.channel.send(user_hashmap)

# // --------------------------------------------------------------------- \\ #
  # Show last command used

@commands.check(not_bot)
@commands.check(user_in_hashmap)
@bot.command(name='last_command', help="Show last command used")
async def get_last_command(context) :
  user_id = context.author.id

  # Get last command used
  history_commands_user = user_hashmap.get(user_id)
  last_command = history_commands_user.get_last_value()

  # Add command to history
  add_command_to_history(context)

  # Send message to discord channel
  await context.message.channel.send("**Latest command used**\n" + last_command)

# // --------------------------------------------------------------------- \\ #
  # Move up in history commands

@commands.check(not_bot)
@commands.check(user_in_hashmap)
@bot.command(name='move_up_history', help="Show next command in history")
async def move_up_history(context) :
  user_id = context.author.id

  # Get next command used
  history_commands_user = user_hashmap.get(user_id)
  next_command = history_commands_user.move_up()

  # Add command to history
  add_command_to_history(context)

  # Send message to discord channel
  await context.message.channel.send("**Next command**\n" + next_command)

# // --------------------------------------------------------------------- \\ #
  # Move down in history commands

@commands.check(not_bot)
@commands.check(user_in_hashmap)
@bot.command(name='move_down_history', help="Show previous command in history")
async def move_down_history(context) :
  user_id = context.author.id

  # Get next command used
  history_commands_user = user_hashmap.get(user_id)
  previous_command = history_commands_user.move_down()

  # Add command to history
  add_command_to_history(context)

  # Send message to discord channel
  await context.message.channel.send("**Previous command**\n" + previous_command)

# // --------------------------------------------------------------------- \\ #
  # Display history of commands

@commands.check(not_bot)
@commands.check(user_in_hashmap)
@bot.command(name='show_history', help="Show commands history")
async def display_command_history(context) :
  add_command_to_history(context)

  # Send message to discord channel
  await context.message.channel.send(user_hashmap.get(context.author.id))

# // --------------------------------------------------------------------- \\ #
  # Remove all commands from history

@commands.check(not_bot)
@commands.check(user_in_hashmap)
@bot.command(name='delete_history', help="Delete commands history")
async def empty_list(context) :
  add_command_to_history(context)

  # Delete commands history of an user
  user_hashmap.get(context.author.id).empty()

  # Send message to discord channel
  await context.message.channel.send("```Commands history has been deleted```")

# // --------------------------------------------------------------------- \\ #
  # Find x words using random letters given by user
  # The point is to transform the 'letters' string and 'word' string
  # Into a 'set' so that we can compare the two
  # If 'letters' is a superset of 'word' then it means that 'letters' contains all
  # Necessary letters to form the respective 'word'
  #
  # letters_set = {a, b, c, f, e}
  # word_set    = {f, a, c, e}
  #
  # letters_set is a superset of word_set since the letters 'f', 'a', 'c', and 'e'
  # Are all present in the letters_set

@commands.check(not_bot)
@commands.check(user_in_hashmap)
@bot.command(name='find_words', help="Give the bot a string of random letters to form words from")
async def find_words_using_letters(context, letters) :
  valid_words = []

  # words.words() ---> returns a list of English words
  for word in words.words() :

    # Filter very short words
    if len(word) > 3 :

      # 'set' is an unordered collection of unique elements
      word_set = set(word)
      letters_set = set(letters)

      # issuperset() checks if the provided letters can form the current word
      if letters_set.issuperset(word_set) :
        valid_words.append(word)

  # Checks if 'valid_words' is not empty
  if valid_words :

    # Display the first 50 words
    # Words are separeted by a comma + space ==> ', '
    # We then use the mod join() on this string
    # Use slice to get first 50 words and join them in one string
    display_words = ', '.join(valid_words[:50])

    # Send message to discord channel
    await context.message.channel.send(display_words)
  else:
    await context.message.channel.send("No valid words found")

# // --------------------------------------------------------------------- \\ #
  ### BOT Events ###
# // --------------------------------------------------------------------- \\ #
  # Handle user responses (yes / no) for the conversation tree

@bot.event
async def on_message(message) :
  # Check if message has been sent by bot
  if message.author == bot.user :
    return

  # Check if message is a command
  if message.content.startswith('!') :
    await bot.process_commands(message)
    return

  # Check if user has answered 'yes' or 'no'
  if message.content.lower() in ["yes", "no"] and conversation_tree.ongoing_conversation == True :
    response = message.content.lower()
    conversation_tree.next_message(response)

  # Display current message
    current_message = conversation_tree.get_current_message()
    if current_message != None :
      await message.channel.send(current_message)

# // --------------------------------------------------------------------- \\ #
  # Send an error regarding the commands

@bot.event
async def on_command_error(context, error) :
    await context.message.channel.send(f"```{str(error)}, type !help for all available commands !```")

# // --------------------------------------------------------------------- \\ #
  # Send message when the bot has successfully connected to Discord

@bot.event
async def on_ready() :
    print("Bot has connected to discord !")

# // --------------------------------------------------------------------- \\ #

bot.run("YOUR-BOT-TOKEN")