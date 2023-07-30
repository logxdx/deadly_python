def harmonic_mean(numbers):
    if len(numbers)==1:
        return numbers[0]
    else:
        return len(numbers)/((1/numbers[len(numbers)-1])+((len(numbers)-1)/harmonic_mean(numbers[:-1])))
