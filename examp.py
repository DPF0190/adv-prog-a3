from mymixin import MySerializer

class MyRootModel(MySerializer):
    my_attrs = ('an_attr', 'another_attr')

    def __init__(self, **kwargs):
        for i in self.my_attrs:
            setattr(self, i, kwargs.get(i))

def my_kwargs(anattr, **kwargs):
    print "my key arg", anattr
    for key in kwargs:
       print "another keyword arg: %s: %s" % (key, kwargs[key])

my_kwargs(anattr=1, anotherattr="short", myattr3="tall")


