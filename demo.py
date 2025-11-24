from UserInputValidator import UserInputValidator
validator1 = UserInputValidator()
validator2 = UserInputValidator()

data1 = ["10", "-5", "3", "abs", "7"]
data2 = ["1", "0", "22", "-3", "hello", "99"]

result1 = validator1.validate_positive_integers(data1)
result2 = validator2.validate_positive_integers(data2)

print("Validator 1 result:", result1)
print("Validator 2 result:", result2)

validator1.info()
validator2.info()