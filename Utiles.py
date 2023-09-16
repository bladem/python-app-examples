class Utiles:

    def num_there(self, s):
        return any(i.isdigit() for i in s)

    def is_string_valid(self, string):
        if self.num_there(string):
            print("El texto introducido no debe contener números")
            return False
        else:
            return True