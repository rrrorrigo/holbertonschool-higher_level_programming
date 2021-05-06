#!/usr/bin/python3
def best_score(a_dictionary):
    # key= is a way to sort some result in this case it sort if the value exist
    return (max(a_dictionary, key=a_dictionary.get) if a_dictionary else None)
