import pickle


def open_pickle(pickle_file):
    with open(pickle_file, "rb") as in_file:
        return pickle.load(in_file)
