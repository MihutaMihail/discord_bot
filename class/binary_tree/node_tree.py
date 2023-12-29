class Node_tree :
  def __init__(self, message) :
    self.message = message
    self.yes_node = None
    self.no_node = None

# // ------------------------------------------------------------ \\ #
  # Add new message to tree to the corresponding yes / no node

  def add_message(self, new_message, yes_or_no, old_message) :
    if self.message == old_message :
      if yes_or_no == "yes" :
        self.yes_node = Node_tree(new_message)
      else :
        self.no_node = Node_tree(new_message)
    else :
      if self.yes_node != None :
        self.yes_node.add_message(new_message, yes_or_no, old_message)
      if self.no_node != None :
        self.no_node.add_message(new_message, yes_or_no, old_message)