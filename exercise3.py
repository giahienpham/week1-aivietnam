import random
import math
def exercise3():
    num_samples = input("Input number of samples (integer number) which are generated: ")
    if not num_samples.isdigit():
        print("number of samples must be an integer number")
        return
    num_samples = int(num_samples)
    loss_name = input("Input loss name: ").upper()
    if loss_name not in ["MAE", "MSE", "RMSE"]:
        print(f"Loss function {loss_name} is not supported")
        return
    total_loss = 0
    results = []
    for i in range(num_samples):
        predict = random.uniform(0, 10)
        target = random.uniform(0, 10)
        if loss_name == "MAE":
            loss = abs(predict - target)
        elif loss_name == "MSE":
            loss = (predict - target) ** 2
        elif loss_name == "RMSE":
            loss = (predict - target) ** 2
            total_loss += loss
            results.append((i, predict, target, math.sqrt(loss)))
    if loss_name == "RMSE":
        final_rmse = math.sqrt(total_loss / num_samples)
        for result in results:
            print(
                f"loss name: {loss_name}, sample: {result[0]}, pred: {result[1]:.6f}, target: {result[2]:.6f}, loss: {result[3]:.6f}")
        print(f"final {loss_name}: {final_rmse:.6f}")
    else:
        for i, predict, target, loss in results:
            print(f"loss name: {loss_name}, sample: {i}, pred: {predict:.6f}, target: {target:.6f}, loss: {loss:.6f}")
exercise3()