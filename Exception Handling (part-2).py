def voter(age):
    if age<18:
        raise ValueError("Invalid Voter")
    return "You are allow to vote"

try:
    print(voter(17))
except ValueError as e:
    print(e)
