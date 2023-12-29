class Chained_list :
  def __init__(self) :
    self.first_node = None
    self.last_node = None
    # If starts at 0, current_index will skip first element
    # Since move_up() ---> current_index = 0 + 1 = index 1
    # (2nd element => skipping 1st element)
    self.current_index = -1
    self.size = 0

# // ------------------------------------------------------------ \\ #
  # Add value to list

  def append(self, data) :
    if self.first_node == None :
      self.first_node = Node_list(data, self.size)
      self.last_node = self.first_node
      self.size += 1
      return

    new_node = Node_list(data, self.size)
    self.last_node.next_node = new_node
    self.last_node = new_node
    self.size += 1

# // ------------------------------------------------------------ \\ #
  # Delete all values

  def empty(self) :
    self.first_node = None
    self.size = 0

# // ------------------------------------------------------------ \\ #
  # Get last value of list

  def get_last_value(self) :
    if self.last_node != None :
      return "```!" + self.last_node.data + "(" + str(self.last_node.index) + ")```"
    else :
      return "```You have not used any commands```"

# // ------------------------------------------------------------ \\ #
  # Get next value (current_index + 1)

  def move_up(self) :
    next_index = self.current_index + 1

    if 0 <= next_index < self.size :
      self.current_index = next_index
      return "```!" + self[next_index] + "(" + str(next_index) + ")```"
    else :
      raise IndexError(f"Index {next_index} is out of range")

# // ------------------------------------------------------------ \\ #
  # Get previous command (current_index - 1)

  def move_down(self) :
    previous_index = self.current_index -1

    if 0 <= previous_index < self.size :
      self.current_index = previous_index
      return "```!" + self[previous_index] + "(" + str(previous_index) + ")```"
    else :
      raise IndexError(f"Index {previous_index} is out of range")

# // ------------------------------------------------------------ \\ #
  # Allow the use of [] (brackets) for indexing

  def __getitem__(self, index) :
    current_node = self.first_node

    while current_node :
      if current_node.index == index :
        return current_node.data

      current_node = current_node.next_node

    raise IndexError(f"Index {index} is out of range")

# // ------------------------------------------------------------ \\ #
  # Make the chained_list iterable
  # Allowing it to be used in a for loop

  def __iter__(self) :
    current_node = self.first_node

    # Create an iterator object of Node
    # Now we can access the attributes of a Node like 'data', 'index' ...
    # We can also yield the data directly from the current_node (yield current_node.data)
    while current_node :
      yield current_node
      current_node = current_node.next_node

# // ------------------------------------------------------------ \\ #
  # Display all data

  def __str__(self) :
    if self.first_node == None :
      return "```NO COMMANDS USED```"

    result = "```History of Commands Used :\n"

    # Iterate over each value (using the iterator object from __iter__)
    for command in self :
      result += f"→ {command.data} ({command.index})\n"

    result += "```\n"

    return result