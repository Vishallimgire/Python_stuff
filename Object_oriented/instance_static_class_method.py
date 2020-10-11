class ClassTest:
    i = 1
    def instance_method(self):
        return f'intance method {self}'

    @classmethod
    def class_method(cls):
        return f'class method {cls}'
    
    @staticmethod
    def static_method(a):
        return f'this is static method {a}'

class SubClassTest(ClassTest):
      def call(self):
          s = ClassTest.static_method(10)
          c = ClassTest.class_method()
          print(s, c)

v = SubClassTest()
v.call()
#instnce method calling
test = ClassTest()
print(test.instance_method())

#class mehtod calling
print(ClassTest.class_method())
# print(test.class_method())

#static method calling
print(ClassTest.static_method(10))