class Member:
    """Class of Member

    Attributes:
        firstname (str): First name of the member
        lastname (str): Last name of the member
        membership_number (str): Membership number of the member
        group_exercise_classes (list): List of group exercise classes
        that the member has booked
    """

    def __init__(self, firstname, lastname, membership_number):
        self.__firstname = firstname
        self.__lastname = lastname
        self.__membership_number = membership_number
        self.__group_exercise_classes = []
        print(f'Create member: {self}')

    @property
    def firstname(self):
        """get the first name of the member"""
        return self.__firstname

    @firstname.setter
    def firstname(self, firstname):
        """set the first name of the member"""
        self.__firstname = firstname

    @property
    def lastname(self):
        """get the last name of the member"""
        return self.__lastname

    @lastname.setter
    def lastname(self, lastname):
        """set the last name of the member"""
        self.__lastname = lastname

    def __membership_number_is_unique(self):
        """check if the membership number is unique
        
        In a real system, this will check against a database
        """
        ...
        return True

    @property
    def membership_number(self):
        """get the membership number of the member"""
        return self.__membership_number

    @membership_number.setter
    def membership_number(self, membership_number):
        """set the membership number of the member"""
        if self.__membership_number_is_unique():
            self.__membership_number = membership_number
        else:
            Exception('Membership number exists')

    @property
    def group_exercise_classes(self):
        """get the list of group exercise classes that the member has booked"""
        return self.__group_exercise_classes

    @group_exercise_classes.setter
    def group_exercise_classes(self, group_exercise_classes):
        """set the list of group exercise classes that the member has booked"""
        self.__group_exercise_classes = group_exercise_classes

    def __str__(self):
        """default string representation of the member"""
        return f'Member name: {self.firstname} {self.lastname}'

    def book_class(self, group_exercise_class):
        """for member to book a group exercise class"""
        group_exercise_class.enrol(self)

    def cancel_class(self, group_exercise_class):
        """for member to cancel a group exercise class"""
        group_exercise_class.cancel_enrolment(self)

    def display_booked_classes(self):
        """display the list of group exercise classes that the member has booked"""
        print(f'Group exercise classes booked by {self}:')
        for group_exercise_class in self.group_exercise_classes:
            print(group_exercise_class)
