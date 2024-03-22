class Contact:
  """Attributes Contacts
  First Name
  Last Name
  Phone Number
  Address
  City
  Zip Code
  """

  def __init__(self, fn, ln, ph, addr, city, zip):
    """Initializing values"""
    self.firstname = fn
    self.lastname = ln
    self.phone = ph
    self.address = addr
    self.city = city
    self.zip = zip

  def __lt__(self, other):
    """Sorting contacts"""
    if self.lastname == other.lastname:
      return self.firstname < other.firstname
    else:
      return self.lastname < other.lastname

  def __str__(self):
    """String representation of contact"""
    return f"{self.firstname} {self.lastname} \n{self.phone} \n{self.address} \n{self.city} {self.zip}"

  def __repr__(self):
    """Write contact to the file"""
    return f"{self.firstname},{self.lastname},{self.phone},{self.address},{self.city},{self.zip}"
