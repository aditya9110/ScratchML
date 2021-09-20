import csv

# to convert csv file to dictionary format
def csvToDataset(fileName):
    with open(fileName) as f:
        reader = csv.reader(f)
        headers = next(reader, None)
        dataset = {}
        for curr in headers:
            dataset[curr] = []
        n = 0
        for row in reader:
            n += 1
            for h, v in zip(headers, row):
                dataset[h].append(v.upper())
    return dataset, n

# to find the unique labels(yes, no, or anything else) along with their probabilities
def calculateLabelProb(dataset, n):
    labels = list(set(dataset[list(dataset)[-1]]))
    prob = {}
    for l in labels:
        prob[l] = dataset[list(dataset)[-1]].count(l) / n
    return prob, labels

# count the occurence of each user input against each label
def countFeature(dataset, label, feature, value, n):
    count = 0
    for i in range(n):
        if dataset[feature][i] == value and dataset[list(dataset)[-1]][i] == label:
            count += 1
    return count

# to calculate the conditional probability of each label wrt user input
def computeProb(dataset, user_tuples, n):
    probs, labels = calculateLabelProb(dataset, n)
    probabilities = {}
    flag = 1
    for l in labels:
        probTLabel = 1
        for feature in user_tuples:
            probTLabel *= countFeature(dataset, l, feature, user_tuples[feature], n)/(probs[l] * n)
        probabilities[l] = probTLabel * probs[l]
    probOfT = sum(list(probabilities.values()))
    for item in probabilities:
        try:  # error handling for invalid input
            probabilities[item] /= probOfT
        except Exception:
            print('Invalid Input!!')
            flag = 0
            return probabilities, flag
    return probabilities, flag

# to pick the maximum value and return it with respective probability
def predict(probabilities):
    keys = list(probabilities.keys())
    values = list(probabilities.values())
    return keys[values.index(max(values))], max(values)

# main code
try:  # error handling for invalid dataset location
    dataset, n = csvToDataset(input('Enter the dataset file name: '))
except Exception:
    print('Invalid Dataset Location!!')
    exit()

n_test = int(input('Enter number of testcases: '))
for i in range(n_test):
    user_tuples = {}
    for h in list(dataset)[:-1]:
        user_tuples[h] = input(h + ': ').upper()
    probsLabelT, flag = computeProb(dataset, user_tuples, n)
    if flag:
        pred, accuracy = predict(probsLabelT)
        print('Outcome is ' + str(list(dataset)[-1]).upper() + ': ' + str(pred) + ' with an accuracy of ' + str(accuracy))
