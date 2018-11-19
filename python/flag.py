import BodyMassIndex
def flags():
    res = BodyMassIndex.BMI()
    print(f"BMI:{res}")
    if res > 18.5 and res < 24.99:
        return True
    else:
        return False  
    

