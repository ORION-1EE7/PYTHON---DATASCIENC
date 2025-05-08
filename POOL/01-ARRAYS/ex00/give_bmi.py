def give_bmi(height: list[int | float], weight: list[int | float]) -> list[int | float]:
    try:
        ret_list = [0] * len(weight)
        assert len(weight) == len(height), "invalid list size "
        for i in range(len(height)):
            assert isinstance(weight[i], (int, float)), f"Error: weight[{i}] is not int or float"
            assert isinstance(height[i], (int, float)), f"Error: height[{i}] is not int or float"
            ret_list[i] =  weight[i] / (height[i] * height[i])
        return ret_list
    except AssertionError as error:
        print(error)
        return 1

def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    limit_lst = [0] * len(bmi)
    for i in range(len(bmi)):
        if bmi[i] > limit:
            limit_lst[i] = True
        else:
            limit_lst[i] = False
    return limit_lst

# height = [2.71, 1.15]
# weight = [165.3, 38.4]
# bmi = give_bmi(height, weight)
# print(bmi, type(bmi))
# print(apply_limit(bmi, 26))