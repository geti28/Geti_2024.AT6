class UserInputValidator:
    def validate_positive_integers(self, items):
        valid = []
        for x in items:
            if x.isdigit() and int(x) > 0:
                valid.append(int(x))
        return valid

    def info(self):
        print("Validation complete")