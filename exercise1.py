def exercise1(tp, fp, fn):
    if type(tp) != int or type(fp) != int or type(fn) != int:
        if type(tp) != int:
            print("tp must be int")
        if type(fp) != int:
            print("fp must be int")
        if type(fn) != int:
            print("fn must be int")
        return
    if tp <= 0 or fp <= 0 or fn <= 0:
        print("tp and fp and fn must be greater than zero")
        return
    precision = tp / (tp + fp)
    recall = tp / (tp + fn)
    f1_score = 2 * (precision * recall) / (precision + recall)

    print("precision is " + str(precision))
    print("recall is " + str(recall))
    print("f1_score is " + str(f1_score))


exercise1(3, 1, 2)
exercise1 ( 2 , 'a', 4)
exercise1(2,3,5)

# assert round(exercise1(2, 3 ,5),2) == 0.33

