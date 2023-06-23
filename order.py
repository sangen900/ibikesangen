import random as ran

class Order:

	def __init__(self):
		# initialize attributes for the bike order. Order will have a type (road, mountain, or city) and will have 3 other specications from the customer--2 specific to the type of the bike, and 1 general preference that could apply to any type.
		# the preferences 
		self.type = self.get_type()
		spref1, spref2 = self.get_sprefs()
		self.spref1 = spref1
		self.spref2 = spref2
		self.gpref = self.get_gref()

	def get_type(self):
		type_options = ['Road','Mountain','City']
		type = ran.choice(type_options)
		return type

	def get_sprefs(self):
		# method to return a tuple of strings to represent the two type-specific prefences.
		# create pref_options as an empty list
		pref_options = []

		# if the type of the bike is road . . .
		if self.type == 'Road':
			# add our road preferences to the list
		    pref_options.append('High Speed')
            pref_options.append('Travel long distances')
        	pref_options.append('Aerodynamic')
        	pref_options.append('Allows the rider to bend forward rather than sitting upright')
        	pref_options.append('Clip-in pedals')
            pref_options.append('Has a handlebar that supports the rider with a variety of hand posititons')
           
		elif self.type == 'Mountain':
            pref_options.append('Off road racing')
            pref_options.append('Is able to absorb shocks or vibrations from jumping or riding on uneven terrain')
            pref_options.append('Ability to take punishment on challenging terrains')
            pref_options.append('Large tires with a lot of traction')
            pref_options.append('Powerful brakes to stop while goining down hills')
            pref_options.append('Ability to take punishment on challenging terrains')
            pref_options.append('A flat handle bar that allows the customer to keep a down hand position inline with the stem')
            pref_options.append('A slack head angle and long wheelbase for stability during descents')

      #city bike
		else:
            pref_options.append('Easy to pedal')
            pref_options.append('Used mostly for paved roads but can be riden on gentle trails')
            pref_options.append('Built for comfort and practical')
            pref_options.append('Allows for rider to sit upright rather than forward')
            pref_options.append('Can accommodate higher weights')
		
		spref1 = ran.choice(pref_options)
		pref_options.remove(spref1)
		spref2 = ran.choice(pref_options)

		return spref1, spref2

	def get_gpref(self):
		
		pref_options = ['Easy to control whilst cycling',
						'Easy to maintain',
                        'Comfortable to ride',
                        'High Quality',
                        'Low Cost']
		
		pref = ran.choice(pref_options)
		
		return pref

	def build_order(self):
		# a method to return a string containing the customer expectations for the entire order
		string_out = f"The customer wants a {self.type} bike with the following features:"
		string_out += f"\n\t1) {self.spref1}"
		string_out += f"\n\t2) {self.spref2}"
		string_out += f"\n\t3) {self.gpref}"

		return string_out

	def show_order(self):
		print self.build_order()

	
		