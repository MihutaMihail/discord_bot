class Hashmap :
  def __init__(self, size) :
    self.size = size
    self.buckets = []
    for i in range(self.size) :
      self.buckets.append([])

# // ------------------------------------------------------------ \\ #
  # Add key,value to hashmap

  def set(self, key, value) :
    hashed_key = hash(key)
    index = hashed_key % self.size
    bucket = self.buckets[index]

    for i in range(len(bucket)) :
      if bucket[i][0] == key :
        del bucket[i]

    self.buckets[index].append((key,value))

# // ------------------------------------------------------------ \\ #
  # Get value from key

  def get(self, key) :
    hashed_key = hash(key)
    index = hashed_key % self.size
    bucket = self.buckets[index]

    for k,v in bucket :
      if k == key :
        return v

# // ------------------------------------------------------------ \\ #
  # Checks if key already exists in hashmap

  def contains(self, key):
    hashed_key = hash(key)
    index = hashed_key % self.size
    bucket = self.buckets[index]

    for k, _ in bucket:
      if k == key:
        return True
    return False

# // ------------------------------------------------------------ \\ #
  # Display all data

  def __str__(self) :
    result = ""

    for bucket in self.buckets :
      for k,v in bucket :
        result += f"**User ID : {k}** {v}\n"
    return result