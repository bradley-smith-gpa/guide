################
Python Refresher
################

************
General Tips
************

Naming Conventions
==================

* Best to name a Python module as one lowercase word e.g. basics.py

* Use spaces instead of underscores if need be

* Use snake case for variables

  * All lower case
  * Underscores are used instead of spaces e.g. ``my_list``

* Keep functions short

* Better to have multiple smaller functions that tie into together rather than one large one

* Aim to keep your code **DRY** - Don't Repeat Yourself

  * It's okay to repeat yourself when initially figuring out a problem

  * But eventually it should be refactored to avoid duplicate code

**************
Basic Examples
**************


First line
==========
.. code-block:: python
  :caption: Display to screen
  
  print('Hello World')



Setting Variables
=================

.. code-block:: python
  :caption: Variables have different types, such as strings (i.e. text) or integers

  fruit = 'apple'
  print(fruit)
  print(type(fruit))
  print(len(fruit))
  print(type(len(fruit)))



*if* statement
==============
.. code-block:: python

  fruit = 'apple'
  if fruit == 'apple':
      print('This will keep the doctor away')
  elif fruit == 'banana':
      print('This is yellow')
  else:
      print('no clue')

*for* loop
==========

.. code-block:: python

  # define empty list
  my_list = []
  # loop through numbers 0 to 5 and add each to our list
  for i in range(6):
    my_list.append(i)
  print(my_list)

  # exact same code above but using a list comprehension to be concise
  my_list = [i for i in range(6)]
  print(my_list)

We can have a loop within a loop - i.e. a nested loop

.. code-block:: python

  words = ['Goose', 'Duck']

  # outer loop goes through each word
  for word in words:
    # inner loop goes through each letter of given word
    for letter in word:
      print('Gimme a',letter.upper() + '!')
    print('What does that spell?', word.upper() + '!')

* using a list
* note the conversion of the integer into a string for the character count
* retrieve element by passing index as integer in square brackets on list

.. tip::

  Use **f-strings** instead of using the ``+`` operator to concatenate strings with 
  variables as it more readable and you are less likely to make an error writing them.

  They are a string with an ``f`` at the start and with any variables surrounded by
  curly brackets: ``{ }``. See the example below to see them in action.

.. code-block:: python

  # list of strings
  fruit_list = ['apple', 'banana', 'cherry']

  # loop through all fruits and display information
  for fruit in fruit_list:
      print(fruit)
      print(f'Character count: {len(fruit)}')
  # retrieve specific element from list
  # index start at 0
  first_fruit = fruit_list[0]
  print(f'The first fruit is {first_fruit})

while loop
==========

.. code-block:: python

  age = 10
  while age < 18:
    print('You still cannot buy alcohol: you are only',str(age))
    age += 1
  else:
    print('Feel free to buy booze now that you are',str(age)+'!')

.. code-block:: python

  import time


  print('The wheels on the bus go round and round...')
  while True:
    print('round and round')
    time.sleep(3)

Dictionary
==========
* code above can be written more efficiently with simple dictionary

.. code-block:: python

  fruit_dictionary = {
    'apple': 'This will keep the doctor away',
    'banana': 'This is yellow'
  }
  print(fruit_dictionary.keys())
  print(fruit_dictionary['apple'])
  fruit = 'banana'
  if fruit in fruit_dictionary.keys():
      print(fruit_dictionary[fruit])
  else:
      print('unidentified fruit')


Function
========
.. code-block:: python

  def traffic_light(colour):
    if colour == 'red':
      return 'Stop!'
    elif colour == 'amber':
      return 'Get ready!'
    elif colour == 'green':
      return 'Go!'
    else:
      return colour + ' is not a valid colour'

  message = traffic_light('Amber')
  print(message)

  message = traffic_light('Blue')
  print(message)


The above function can be written concisely using a dictionary instead.

.. code-block:: python

  # dry version of traffic light function
  action_dict = {
    'red': 'Stop!', 'amber': 'Get ready!', 'green': 'Go!'
  }

  def traffic_light(colour):
    if colour in action_dict:
      return action_dict[colour]
    else:
      return f'{colour} is not a valid colour'

  message = traffic_light('green')
  print(message)


Packing/Unpacking Arguments and Keyword Arguments
=================================================


If a function has parameters that packs arguments together (i.e. uses \*args and \*\*kwargs)
, you can pass in arguments by unpacking a list or dictionary when calling it

.. code-block:: python

  # prices of basic ingredients in £s (e.g. dough, cheese, tomato sauce)
  basic_ingredients = [0.50 , 1.25, 0.40]

  # prices of optional toppings in £s
  optional_toppings = {'Olives': 0.65,'Pepperoni': 1.10, 'Onions': 0.5}

  def get_pizza_price(*args, **kwargs):
    basic_price = sum(args)
    print('Basic Price:', str(basic_price))

    toppings_price = sum(kwargs.values())
    print('Your toppings were:')

    for name, price in kwargs.items():
      print('\t'+name+':', str(price))

    print('\tToppings Subtotal:', toppings_price)

    total_price = basic_price + toppings_price
    print('Total Price:', str(total_price))

  get_pizza_price(*basic_ingredients, **optional_toppings)

*******
Classes
*******

Defining a class
================
.. code-block:: python
  
  # defining a class
  class MyClass:
    pass

Setting Attributes
==================

.. code-block:: python

  class MyClass:
    pass

  # creating instances of that class
  my_instance = MyClass()
  another_instance = MyClass()

  # setting attributes
  MyClass.my_class_attribute = 1
  my_instance.my_instance_attribute = 'Hello'

  # class attributes will be passed down to each instance...
  print(my_instance.my_class_attribute)

  # ...but instance attributes will override any class attributes
  another_instance.my_class_attribute = 500

  print(another_instance.my_class_attribute)

Methods
=======

.. code-block:: python

  class Aircraft:
    military_vehicle = True
    origin_country = 'USA'
    can_hover = False

    def __init__(self, name, length, max_speed, manufacturer, nickname=None):
      # run code just after a given instance has been created
      self.name = name
      self.length = length
      self.max_speed = max_speed
      self.manufacturer = manufacturer
      self.nickname = nickname


    def get_max_speed(self, metric=True):
      '''
      Return max speed of aircraft.
      
      Set `metric` to `False` for imperial units.
      '''
      if metric:
        max_speed = self.max_speed
        units = 'km/h'
      else:
        # convert to imperial units
        conversion_ratio = 0.621371
        max_speed = conversion_ratio * self.max_speed
        units = 'mph'
      print("{:.2f}".format(max_speed) + units)
      return max_speed
    
    def __len__(self):
      return self.length
    
    # def __str__(self):
    #   return self.name +' ('+self.nickname+')'

  class Plane(Aircraft):

    def __init__(self, wingspan, *args, **kwargs):
      # wingspan is an attribute specific to a plane instance
      # show what arguments are passed in and then forwarded
      print('Args:',args)
      print('Kwargs:',kwargs)
      super().__init__(*args, **kwargs)
      self.wingspan = wingspan
      # the number of rolls a plane has done will always start at zero
      self.rolls = 0

    def do_a_barrel_roll(self):
      '''Do a barrel roll which will increment the number of rolls performed'''
      # google 'do a barrel roll' for a demonstration
      self.rolls += 1
      print(f'The {self.name} just did a barrel roll!')


  class Helicopter(Aircraft):
    can_hover = True

    def __init__(self, *args, num_of_blades = 4, **kwargs ):
      super().__init__(*args, **kwargs)
      self.num_of_blades = num_of_blades
      self.troops = 0
    
    def add_troops(self, num = 1):
      ''' Add troops to heli to be transported. Default number is 1'''
      self.troops += num
      print(f'Just added a quantity of {num} troop(s)')
    
    def deploy_with_fries(self):
      ''' Deploy the troops from heli using a fast rope technique '''
      if self.troops:
        print(f'The {self.nickname} just deployed {self.troops} troops')
      else:
        print(f'The {self.nickname} does not have any troops to deploy!')
      
  # instantiate a fighter jet from the Aircraft class
  f16 = Aircraft('F16',14.8, 2414, 'General Dynamics', nickname='Fighting Falcon')

  print(f16)
  print(f16.name)
  print(f16.origin_country)

  # call our method
  f16.get_max_speed(metric = False)
  # alternatively it can be called from the class with instance as first arg
  Aircraft.get_max_speed(f16, metric = False)

  # instantiate a fighter jet from the Plane class with wingspan argument
  f16 = Plane(9.96,'F16',14.8, 2414, 'General Dynamics', nickname='Fighting Falcon')

  # verify that attributes and methods have been inherited from Aircraft
  print(f16.nickname)
  f16.get_max_speed()

  # instantiate a bomber from the Plane class
  b2 = Plane(52.4,'B-2',21.0, 1010, 'Northrop Grumman', nickname='Spirit')

  # call our method defined in the Plane class
  print(b2.rolls)
  b2.do_a_barrel_roll()
  b2.do_a_barrel_roll()
  b2.do_a_barrel_roll()
  print(b2.rolls)

  # instantiate an attack heli from the Helicopter class
  ah64 = Helicopter('AH-64', 17.7, 365, 'Boeing', nickname='Apache')
  print(ah64.num_of_blades)

  # instantiate a utility heli from the Helicopter class
  uh1n = Helicopter('UH-1N', 17.6, 220,'Bell',nickname='Twin Huey', num_of_blades=2)
  uh1n.deploy_with_fries()
  uh1n.add_troops()
  uh1n.add_troops(num=4)
  uh1n.deploy_with_fries()

  print(uh1n)

Instantiation Explained
=======================

.. code-block:: python

  # these above steps represent the instantiation when the class is 'called'
  class MyClass:
    def __init__(self,x):
      self.x = x

  # constructor method __new__ has class as first argument
  # can be called from object or MyClass
  instance = object.__new__(MyClass)
  # verify we have indeed constructed and returned an instance
  print(instance)
  # verify that attributes have not been set
  try:
    print(instance.x)
  except AttributeError as e:
    print(e)
  # now call initialized method to set values
  # __init__ does not return anything! (it shouldn't because it just sets values)
  # alternative to line below: object.__init__(instance,2)
  # or instance.__init__(2)
  MyClass.__init__(instance,2)
  print(instance.x)

Inheritance Explained
=====================

.. code-block:: python

  class MyClass:
    def __init__(self,x):
      self.x = x
    
  class MySubClass(MyClass):
    def __init__(self, x):
      print(self)
      print(super().__self__)
      super().__init__(x)

  instance = object.__new__(MySubClass)
  instance.__init__(3)
  print(instance.x)
  MySubClass.__mro__

  class Plane(Aircraft):
    pass
