from json import loads, dumps

class MySerializer(object):

    jsonstr = {'alpha': 1, 'beta': 2}

    @classmethod
    def deserialize(cls, jsonstr):
        #load from json to dict
        d = loads(jsonstr)
        # initialize object, return
        return cls(**d)

    def serialize(self):
        t = {}
        #iterate over self.my_attrs

        for d in self.my_attrs:
           getattr(self, d)
        #get attrs, set into dictionary
        t[] = val
        #return dumps
        return json.dumps(jsonstr)
