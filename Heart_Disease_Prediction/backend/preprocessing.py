def preprocess_input(data):

    return {
        "age": data["age"],
        "sex": data["sex"],
        "cp": data["cp"],
        "trestbps": data["trestbps"],
        "chol": data["chol"],
        "fbs": data["fbs"],
        "restecg": data["restecg"],
        "thalach": data["thalach"],
        "exang": data["exang"],
        "oldpeak": data["oldpeak"],
        "slope": data["slope"],
        "ca": data["ca"],
        "thal": data["thal"]
    }