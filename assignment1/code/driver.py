from trainer import Trainer
from member import Member
from group_exercise import GroupExercise


def main():
    # 1 create 5 member objects, 2 trainer objects and 2 group exercise class objects
    print('==========Question 1 start==========')
    # 1.1 create 5 member objects
    member1 = Member('John', 'Tan', 'M001')
    member2 = Member('Mary', 'Lim', 'M002')
    member3 = Member('Peter', 'Lim', 'M003')
    member4 = Member('Jane', 'Tan', 'M004')
    member5 = Member('Tommy', 'Tan', 'M005')
    members = [member1, member2, member3, member4, member5]

    # 1.2 create 2 trainer objects
    trainer1 = Trainer('John', 'Lim', 'Yoga')
    trainer2 = Trainer('Mary', 'Tan', 'Zumba')
    trainers = [trainer1, trainer2]

    # 1.3 create 2 group exercise class objects
    group_exercise_class1 = GroupExercise(name='Yoga', capacity=3)
    group_exercise_class2 = GroupExercise(name='Zumba', capacity=6)
    classes = [group_exercise_class1, group_exercise_class2]
    print('==========Question 1 end==========\n')

    # 2 assign the trainer to the group exercise class
    print('==========Question 2 start==========')
    group_exercise_class1.assign_trainer(trainer1)
    group_exercise_class2.assign_trainer(trainer2)
    print('==========Question 2 end==========\n')

    print('==========Question 3 start==========')
    print('3 set the class fee for each group exercise class')
    group_exercise_class1.set_fee(25)
    group_exercise_class2.set_fee(30)
    print('==========Question 3 end==========\n')

    print('==========Question 4 start==========')
    print('4 Set up specific member booking for a group exercise class')
    member1.book_class(group_exercise_class1)
    member2.book_class(group_exercise_class2)
    member3.book_class(group_exercise_class1)
    member3.book_class(group_exercise_class2)
    member4.book_class(group_exercise_class1)
    member4.book_class(group_exercise_class2)
    member5.book_class(group_exercise_class1)
    member5.book_class(group_exercise_class2)
    print('==========Question 4 end==========\n')

    print('==========Question 5 start==========')
    print('5 Cancelling a specific member\'s group exercise class')
    group_exercise_class1.cancel_enrolment(member3)
    print('==========Question 5 end==========\n')

    print('==========Question 6 start==========')
    print('6 Record a specific member checking in to a group exercise class')
    group_exercise_class1.mark_attendance(member1)
    print('==========Question 6 end==========\n')

    print('==========Question 7 start==========')
    print('7 Display the list of enrolled participants for a group exercise class')
    for group_class in classes:
        group_class.display_enrolled_members()
    print('==========Question 7 end==========\n')

    print('==========Question 8 start==========')
    # 8 Display the waiting list for a group exercise class
    for group_class in classes:
        group_class.display_waitlist_members()
    print('==========Question 8 end==========\n')

    print('==========Question 9 start==========')
    # 9 Display the available slots for a group exercise class
    for group_class in classes:
        print(f'Number of {group_class.name} available slots is: {group_class.get_available_slot()}')
    print('==========Question 9 end==========\n')

    # 10 Display the number of participants enrolled in a group exercise class
    print('==========Question 10 start==========')
    for group_class in classes:
        print(f'Number of {group_class.name} enrolled members is: {group_class.get_enrolled_number()}')
    print('==========Question 10 end==========\n')

    # 11 Display the number of wait list participants for a group exercise class
    print('==========Question 11 start==========')
    for group_class in classes:
        print(f'Number of {group_class.name} waitlist is: {len(group_class.waitlist)}')
    print('==========Question 11 end==========\n')

    # 12 Display the number of attendees for a group exercise class
    print('==========Question 12 start==========')
    for group_class in classes:
        print(f'Number of {group_class.name} attendees is {len(group_class.checked_in_members)}')
    print('==========Question 12 end==========\n')

    # 13 Display the attendance percentage for a group exercise class
    print('==========Question 13 start==========')
    for group_class in classes:
        print(f'Attendance percentage of {group_class.name} is {group_class.get_attendance_percentage():.2f}%')
    print('==========Question 13 end==========\n')

    # 14 Display the total payment collected for a group exercise class
    print('==========Question 14 start==========')
    for group_class in classes:
        print(f'Total payment collected for {group_class.name} is {group_class.get_income()}')
    print('==========Question 14 end==========\n')

    # 15 Display the list of group exercise classes for which a specific member is enrolled
    print('==========Question 15 start==========')
    for member in members:
        member.display_booked_classes()
    print('==========Question 15 end==========\n')

    # 16 Display the list of classes offered by a particular trainer
    print('==========Question 16 start==========')
    for trainer in trainers:
        trainer.display_classes()
    print('==========Question 16 end==========\n')


if __name__ == '__main__':
    main()
