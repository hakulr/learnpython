class Student(object):
    def __init__(self,name,score):
        self.__name = name
        self.__score = score
    def print_score(self):
        print('%s: %s'%(self.__name,self.__score))

    def get_grade(self):
        if self.__score >= 90:
            return 'A'
        elif self.__score >= 60:
            return 'B'
        else:
            return 'C'
    def get_name(self):
        return self.__name
lisa = Student('Lisa rong',100)
kobi = Student('Kobi Brant',59)
print(kobi.get_grade())
lisa.print_score()
print(lisa.get_name())