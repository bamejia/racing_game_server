import json


def get_json(obj):
    return json.loads(
        json.dumps(obj, default=lambda o: getattr(o, '__dict__', str(o)))
  )
#
# class fromJson:
#     def from_json(json_string):
#         json_dict = json.loads(json_string)
