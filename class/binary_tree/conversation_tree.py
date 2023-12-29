class Conversation_tree :
  def __init__(self) :
    self.first_node = None
    self.current_conversation_node = None
    self.ongoing_conversation = False
    self.topics = []

# // ------------------------------------------------------------ \\ #

  def add_message(self, new_message, yes_or_no, old_message) :
    self.first_node.add_message(new_message, yes_or_no, old_message)

# // ------------------------------------------------------------ \\ #
  # Advance conversation

  def next_message(self, yes_or_no) :
    if yes_or_no == "yes" :
      # Check if yes_node exists
      if self.current_conversation_node.yes_node != None :
        self.current_conversation_node = self.current_conversation_node.yes_node
      else :
        self.end_conversation()
    else :
      # Check if no_node exists
      if self.current_conversation_node.no_node != None :
        self.current_conversation_node = self.current_conversation_node.no_node
      else :
        self.end_conversation()

# // ------------------------------------------------------------ \\ #
  # End conversation

  def end_conversation(self) :
    # Indicate end of conversation using the node
    # If user tries to advance conversation, this message will show
    self.current_conversation_node = Node_tree("This is the end of the conversation. Type this to start again ```!reset_conversation```")

    # Set False as to not take messages like "no" and "yes" as answers for the conversation anymore
    self.ongoing_conversation = False

# // ------------------------------------------------------------ \\ #
  # Get current conversation node message

  def get_current_message(self) :
    return self.current_conversation_node.message

# // ------------------------------------------------------------ \\ #
  # Reset conversation

  def reset_conversation(self) :
    self.current_conversation_node = self.first_node

# // ------------------------------------------------------------ \\ #
  # Search if the conversation contains a particular topic

  def search_topic(self, topic_search) :
    for topic in self.topics :
      if topic == topic_search :
        return True
    return False

# // ------------------------------------------------------------ \\ #
  # Prepare conversation

  def setup(self) :
    self.first_node = Node_tree("Do you need any help ?")
    self.current_conversation_node = self.first_node

    # // ------------------------------------------------------------ \\ #
      # Start conversation

    self.add_message("Do you need help with Python ?", "yes", "Do you need any help ?")
    self.add_message("Have a nice day", "no", "Do you need any help ?")

    # // ------------------------------------------------------------ \\ #
      # Topic ---> Python

    # Add topic
    self.topics.append("python")

    # Answer 'NO' ---> Next topic
    self.add_message("Do you need help with math ?", "no", "Do you need help with Python ?")

    # Answer 'YES' ---> Question 1
    self.add_message("Need help creating a class ?", "yes", "Do you need help with Python ?")

    self.add_message("```class example :\n def __ini__(self, attribute1) :\n  self.attribute1 = attribute1\n  self.attribute2 = None```", "yes", "Need help creating a class ?")
    self.add_message("Do you want to know what the keyword 'async' means ?", "no", "Need help creating a class ?")

    # Answer 'YES' ---> Question 2
    self.add_message("'async' is used to define asynchronous functions or coroutines. These functions can be paused with 'await', enabling other tasks to run without blocking the main program's execution",
                     "yes", "Do you want to know what the keyword 'async' means ?")
    self.add_message("That's all I can help you with about python", "no", "Do you want to know what the keyword 'async' means ?")

    # // ------------------------------------------------------------ \\ #
      # Topic ---> Math

    # Add topic
    self.topics.append("math")

    # Answer 'NO' ---> End of conversation
    self.add_message("I do not have any more topics that I can help you with", "no", "Do you need help with math ?")

    # Answer 'YES' ---> Question 1
    self.add_message("Do you want to know what is 2 + 2 ?", "yes", "Do you need help with math ?")

    self.add_message("The answer is obviously ```4```", "yes", "Do you want to know what is 2 + 2 ?")
    self.add_message("That's all I can help you with about math", "no", "Do you want to know what is 2 + 2 ?")