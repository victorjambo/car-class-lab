class Car(object):
  def __init__(self, name='General', model='GM', type=None):
    self.name = name
    self.model = model
    self.type = type
    self.num_of_doors = 4
    self.num_of_wheels = 4
    self.speed = 0
    if self.model == '911 Turbo' or self.model == 'Agera R':
      self.num_of_doors = 2
    if self.type == 'trailer':
      self.num_of_wheels = 8

  def is_saloon(self):
    if self.type == 'trailer':
      return False
    return True

  def drive(self, speed):
    self.speed = speed
    if self.is_saloon():
      self.speed = 1000
      return self
    else:
      self.speed = 77
      return self
    return self