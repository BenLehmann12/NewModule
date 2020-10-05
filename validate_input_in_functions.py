'''
:param: test_name, test_score, invalid_message
:returns: Returns the Test Name and Grade or it can return an error message if the grade value is below 0
'''
def test_score(test_name,test_score=0,invalid_message="Invalid Test Score, Try Again"):
    try:
        if(test_score < 0 or test_score > 100):
            return invalid_message
        else:
            name_and_score = test_name ,int(test_score)    #returns a key, return {test_name:test_score}
    except ValueError as error:
        raise error
    else:
        return name_and_score

if __name__=="__main__":
    try:
        print(test_score("Math"))
    except ValueError as error:
        print("Error")