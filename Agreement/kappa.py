from nltk.metrics import agreement, ConfusionMatrix
import itertools

data = [['1', 5723, 'ORG'],['2', 5723, 'ORG'],['3', 5723, 'ORG'],['1', 55829, 'LOC'],['2', 55829, 'LOC'],['3', 55829, 'ORG'],['1', 259742, 'PER'],['2', 259742, 'LOC'],['3',259742,'PER'],['1', 269340, 'PER'],['2', 269340, 'LOC'],['3',269340,'PER']]
#data = [['1', 5723, 1],['2', 5723, 4],['1', 55829, 1],['2', 55829, 1],['1', 259742, 2],['2', 259742, 4],['1', 269340, 3],['2', 269340, 3]]

def get_coder_answers(coder_name):
    return [d[2] for d in data if d[0] == coder_name]

def get_datapoints():
    datapoints = {}
    for i in data:
        if i[1] not in datapoints:
            datapoints[i[1]] = {}
        datapoints[i[1]][i[0]] = i[2]
    return datapoints

def get_coders():
    return list(set([d[0] for d in data]))

def get_disagreements(datapoints):
    disagreements = {}
    for i,answers in datapoints.items():
        answered_categories = answers.values()
        if len(set(answers.values())) > 1:
            disagreements[i] = answers
    return disagreements


coders = get_coders()
num_coders = len(coders)

task = agreement.AnnotationTask(data=data)
for pair in itertools.combinations(coders, 2):
    print("Coders",pair[0],pair[1])
    print("Observed agreement:",task.Ao(pair[0],pair[1]))
    print("Expected agreement:",task.Ae_kappa(pair[0],pair[1]))
    print(task.kappa_pairwise(pair[0],pair[1]))
    a1 = get_coder_answers(pair[0])
    a2 = get_coder_answers(pair[1])
    cm = ConfusionMatrix(a1,a2)
    print(cm)

print(task.kappa())


datapoints = get_datapoints()
for i,answers in datapoints.items():
    print(i,answers)

disagreements = get_disagreements(datapoints)

#for d,answers in disagreements.items():
#    print(d,answers)
