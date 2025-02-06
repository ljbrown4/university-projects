#
# ps8pr1.py  (Problem Set 8, Problem 1)
#
# A class to represent calendar dates       
#

class Date:
    """ A class that stores and manipulates dates that are
        represented by a day, month, and year.
    """

    # The constructor for the Date class.
    def __init__(self, init_month, init_day, init_year):
        """ constructor that initializes the three attributes  
            in every Date object (month, day, and year)
        """
        # add the necessary assignment statements below
        self.month = init_month
        self.day = init_day
        self.year = init_year

    # The function for the Date class that returns a string
    # representation of a Date object.
    def __repr__(self):
        """ This method returns a string representation for the
            object of type Date that it is called on (named self).

            ** Note that this *can* be called explicitly, but
              it more often is used implicitly via printing or evaluating.
        """
        s = '%02d/%02d/%04d' % (self.month, self.day, self.year)
        return s

    def is_leap_year(self):
        """ Returns True if the called object is
            in a leap year, and False otherwise.
        """
        if self.year % 400 == 0:
            return True
        elif self.year % 100 == 0:
            return False
        elif self.year % 4 == 0:
            return True
        return False

    def days_in_month(self):
        """ Returns the number of days in the called object's month
        """
        numdays = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        if self.is_leap_year():
            numdays[2] = 29
            
        return numdays[self.month]    

    def copy(self):
        """ Returns a new object with the same month, day, and year
            as the called object (self).
        """
        new_date = Date(self.month, self.day, self.year)
        return new_date
    
    def day_name(self):
        """ Return the day of the week that the called Date object falls on. 
            IMPORTANT: This method won't work until you implement the 
            other methods of the class, as specified in Problem 1.
        """
        day_names = ['Monday', 'Tuesday', 'Wednesday',
                     'Thursday', 'Friday', 'Saturday', 'Sunday']
        monday = Date(11, 20, 2023)
        num_days = self.days_between(monday)
        return day_names[num_days % 7]
    
    #### Put your code for the methods from Problem 1 below. ####
    #### Make sure that it is indented by an appropriate amount. ####
    def advance_one(self):
        '''chnages the date so that it is one day after'''
        maxdays = self.days_in_month()
        day = self.day
        month = self.month
        if month == 12 and day == maxdays:
            self.day = 1 
            self.month = 1
            self.year += 1
        elif month != 12 and day == maxdays:
            self.day = 1
            self.month += 1
        else:
            self.day += 1
            
    def __eq__(self, other):
        '''returns true if the date of self is the same date as other, returns false otherwise'''
        return self.day == other.day and self.month == other.month and self.year == other.year
    
    def is_before(self, other):
        '''returns true if the date of self is before the date of other, returns false otherwise'''
        if self.year < other.year:
            return True
        elif self.year == other.year and self.month < other.month:
            return True
        elif self.year == other.year and self.month == other.month and self.day < other.day:
            return True
        return False
    
    def is_after(self, other):
        '''returns true if the date of self is after the date of other, returns false otherwise'''
        if self == other:
            return False
        elif self.is_before(other) ==  True:
            return False
        return True
    
    def days_between(self, other):
        '''returns an integer for the amount of days between self and other'''
        if self == other:
            return 0
        count = 0
        check = self.is_before(other)
        if check == True:
            d1 = self.copy()
            d2 = other.copy()
        else:
            d1 = other.copy()
            d2 = self.copy()
        while d1 != d2:
            count += 1
            d1.advance_one()
        if check == True:
            return count * -1
        else:
            return count
            
        
        
            
        