"""
main.py
==============
A one line summary of the module or program, terminated by a period.

Leave one blank line.  The rest of this docstring should contain an
overall description of the module or program.  Optionally, it may also
contain a brief description of exported classes and functions and/or usage
examples.

  Typical usage example:

  foo = ClassFoo()
  bar = foo.FunctionBar()
"""

def about_me(your_name:str):
    """Return the most important thing about a person.

    Blah Blah Blah Blah Blah Blah Blah 

    Args:
        your_name: A string indicating the name of the person.

    """
    return "The wise {} loves Python.".format(your_name)


class ExampleClass:
    """Summary of class here.

    Longer class information....
    Longer class information....

    Attributes:
        name: A boolean indicating if we like SPAM or not.
    """

    def __init__(self, name:str):
        self.name = name

    def about_self(self, string_format:str):
        """Return information about an instance created from ExampleClass.

        Args:
        string_format: A string indicating the name of the person.

        Returns:
            None

        Raises:
            IOError: An error occurred accessing the smalltable.
        """
        return "I am a very smart {} object.".format(self.name)
