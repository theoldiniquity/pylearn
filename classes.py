class MyClass():
    def cl(self):
        print("!!!")
        pass
def class_name_changer(cls, new_name):
    last = ''
    for i in new_name:
        if not i.isalnum():
            last += i
    if  not new_name[0].isupper() or last:
        raise TypeError

    print(cls.__name__)
    print(new_name)
    cls.__name__ = new_name
    print(cls.__name__)


class_name_changer(MyClass, 'Qwe')
a = MyClass()
a.cl()
class_name_changer(MyClass, 'Asdf')
class_name_changer(MyClass, 'Asd_f')