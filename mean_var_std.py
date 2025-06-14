import numpy as np

def calculate(list: list) -> dict:
    if len(list) != 9:
        raise ValueError("List must contain nine numbers.")
    eda_array = np.array(list).reshape(3, 3)
    # print(eda_array)
    calculations = dict()
    calculations["mean"] = [np.mean(eda_array, axis=0).tolist(),np.mean(eda_array, axis=1).tolist(), np.mean(eda_array)]
    calculations["variance"] = [np.var(eda_array, axis=0).tolist(),np.var(eda_array, axis=1).tolist(),np.var(eda_array)]
    calculations["standard deviation"] = [np.std(eda_array, axis=0).tolist(),np.std(eda_array, axis=1).tolist(),np.std(eda_array)]
    calculations["max"] = [np.max(eda_array, axis=0).tolist(),np.max(eda_array, axis=1).tolist(),np.max(eda_array)]
    calculations["min"] = [np.min(eda_array, axis=0).tolist(),np.min(eda_array, axis=1).tolist(),np.min(eda_array)]
    calculations["sum"] = [np.sum(eda_array, axis=0).tolist(),np.sum(eda_array, axis=1).tolist(),np.sum(eda_array)]
    # print(calculations)
    return calculations
