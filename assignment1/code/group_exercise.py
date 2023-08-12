class GroupExercise:
    """Class of Group Exercise Class

    Attributes:
        name (str): Name of the group exercise class
        trainer (Trainer): Trainer assigned to the group exercise class
        capacity (int): Capacity of the group exercise class
        enrolled_members (list): List of members enrolled in the group exercise class
        waitlist (list): List of members on the waitlist for the group exercise class
        checked_in_members (list): List of members who have checked in for the group exercise class
        fee (float): Fee for the group exercise class
    """

    def __init__(self, name, capacity):
        self.__name = name
        self.__trainer = None
        self.__capacity = capacity
        self.__enrolled_members = []
        self.__waitlist = []
        self.__checked_in_members = []
        self.__fee = 0
        print(f'Create group exercise class: {self}')

    @property
    def name(self):
        """get the name of the group exercise class"""
        return self.__name

    @name.setter
    def name(self, name):
        """set the name of the group exercise class"""
        self.__name = name

    @property
    def trainer(self):
        """get the trainer assigned to the group exercise class"""
        return self.__trainer

    @trainer.setter
    def trainer(self, trainer):
        """set the trainer assigned to the group exercise class"""
        self.__trainer = trainer

    @property
    def capacity(self):
        """get the capacity of the group exercise class"""
        return self.__capacity

    @capacity.setter
    def capacity(self, capacity):
        """set the capacity of the group exercise class"""
        self.__capacity = capacity

    @property
    def enrolled_members(self):
        """get the list of enrolled members of the group exercise class"""
        return self.__enrolled_members

    @enrolled_members.setter
    def enrolled_members(self, enrolled_members):
        """set the list of enrolled members of the group exercise class"""
        self.__enrolled_members = enrolled_members

    @property
    def waitlist(self):
        """get the list of members on the waitlist of the group exercise class"""
        return self.__waitlist

    @waitlist.setter
    def waitlist(self, waitlist):
        """set the list of members on the waitlist of the group exercise class"""
        self.__waitlist = waitlist

    @property
    def checked_in_members(self):
        """get the list of members who have checked in for the group exercise class"""
        return self.__checked_in_members

    @checked_in_members.setter
    def checked_in_members(self, checked_in_members):
        """set the list of members who have checked in for the group exercise class"""
        self.__checked_in_members = checked_in_members

    def __str__(self):
        """default string representation of the group exercise class"""
        return f'Group Exercise Class: {self.name}'

    def enrol(self, member):
        """Enrols a gym member into the group exercise class.

        If the class is full, the member will be added to the waitlist.
        """
        if len(self.enrolled_members) < self.capacity:
            self.enrolled_members.append(member)
            member.group_exercise_classes.append(self)
        else:
            self.waitlist.append(member)

    def cancel_enrolment(self, member):
        """Removes a gym member from the enrolled list."""
        self.enrolled_members.remove(member)
        member.group_exercise_classes.remove(self)
        if self.waitlist:
            self.enrol(self.waitlist.pop(0))

    def display_enrolled_members(self):
        """Displays all gym members currently enrolled in the group exercise class."""
        print(f'Enrolled members for {self.name}:')
        for member in self.enrolled_members:
            print(member)

    def display_waitlist_members(self):
        """Displays all gym members currently on the waitlist for the group exercise class."""
        print(f'Waitlist members for {self.name}:')
        for member in self.waitlist:
            print(member)

    def assign_trainer(self, trainer):
        """Assigns a trainer to conduct the group exercise class."""
        print(f'Assign trainer {trainer} to {self}')
        self.trainer = trainer
        trainer.group_exercise_classes.append(self)

    def get_enrolled_number(self):
        """Returns the number of gym members currently enrolled in the class."""
        return len(self.enrolled_members)

    def get_available_slot(self):
        """Returns the number of available slots for enrolment in the class."""
        return self.capacity - len(self.enrolled_members)

    def set_fee(self, fee):
        """Sets the fee amount for the class."""
        self.fee = fee

    def get_income(self):
        """Calculates and returns the total payment received for the group exercise class
        based on the number of enrolled members and the class fee."""
        return self.fee * len(self.enrolled_members)

    def mark_attendance(self, member):
        """Marks a gym member's attendance for the class."""
        self.checked_in_members.append(member)

    def get_attendance_percentage(self):
        """Calculates and returns the attendance percentage for the class,
        representing the ratio of members checked-in to the total number of enrolled members"""
        if len(self.enrolled_members) > 0:
            return len(self.checked_in_members) / len(self.enrolled_members) * 100
        else:
            Exception('No members enrolled in this class.')
