def convert_object_to_dict(obj):
    """
      A function takes in a custom object and returns a dictionary representation of the object.
      This dict representation includes meta data such as the object's module and class names.

      Source: https://gist.github.com/ardenn/76aa5653245388519a2edb690d8ed7ba#file-json_convert_to_dict-py
    """

    object_dict = {
        "__class__": obj.__class__.__name__,
        "__module__": obj.__module__
    }

    object_dict.update(obj.__dict__)

    return object_dict


def convert_dict_to_object(my_dict):
    """
        Function that takes in a dict and returns a custom object associated with the dict.
        This function makes use of the "__module__" and "__class__" metadata in the dictionary
        to know which object type to create.

        Source: https://gist.github.com/ardenn/30f94f57876a70832a5c960fd4742d89#file-json_dict_to_obj-py
    """
    if "__class__" in my_dict:

        class_name = my_dict.pop("__class__")

        module_name = my_dict.pop("__module__")

        module = __import__(module_name)

        class_ = getattr(module, class_name)

        obj = class_(**my_dict)
    else:
        obj = my_dict

    return obj
