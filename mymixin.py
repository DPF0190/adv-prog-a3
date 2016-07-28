from json import loads, dumps

class MySerializer(object):

    @classmethod
    def deserialize(cls, jsonstr):
        #load from json to dict
        d = loads(jsonstr)
        # initialize object, return
        return cls(**d)

    def serialize(self):
        #iterate over self.my_attrs
        #get attrs, set into dictionary
        #return dumps
        return json.dumps(jsonstr)
