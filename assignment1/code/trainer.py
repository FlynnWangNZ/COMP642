class Trainer:
    """Class of Trainer

    Attributes:
        firstname (str): First name of the trainer
        lastname (str): Last name of the trainer
        specialisation (str): Specialisation of the trainer
        group_exercise_classes (list): List of group exercise classes
    """

    def __init__(self, firstname, lastname, specialisation):
        self.__firstname = firstname
        self.__lastname = lastname
        self.__specialisation = specialisation
        self.__group_exercise_classes = []
        print(f'Create trainer: {self}')

    @property
    def firstname(self):
        """get the first name of the trainer"""
        return self.__firstname
    
    @firstname.setter
    def firstname(self, firstname):
        """set the first name of the trainer"""
        self.__firstname = firstname
    
    @property
    def lastname(self):
        """get the last name of the trainer"""
        return self.__lastname
    
    @lastname.setter
    def lastname(self, lastname):
        """set the last name of the trainer"""
        self.__lastname = lastname

    @property
    def specialisation(self):
        """get the specialisation of the trainer"""
        return self.__specialisation

    @specialisation.setter
    def specialisation(self, specialisation):
        """set the specialisation of the trainer"""
        self.__specialisation = specialisation

    @property
    def group_exercise_classes(self):
        """get the list of group exercise classes that the trainer is teaching"""
        return self.__group_exercise_classes

    @group_exercise_classes.setter
    def group_exercise_classes(self, group_exercise_classes):
        """set the list of group exercise classes that the trainer is teaching"""
        self.__group_exercise_classes = group_exercise_classes

    def __str__(self):
        """default string representation of the trainer"""
        return f'Trainer name: {self.firstname} {self.lastname}'

    def display_classes(self):
        """display the list of group exercise classes assigned to the trainer"""
        print(f'Group exercise classes assigned to {self}:')
        for group_exercise_class in self.group_exercise_classes:
            print(group_exercise_class)

    def add_class(self, group_exercise_class):
        """for trainer to add a group exercise class"""
        group_exercise_class.assign_trainer(self)
