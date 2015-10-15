import pickle

def add_training_data(spoken_command1, spoken_command2, user_id, TrainingDictionary):
    fw = open("training.data", 'wb')
    TrainingDictionary[user_id] = [spoken_command1, spoken_command2]
    pickle.dump(TrainingDictionary, fw)
    fw.close()


def load_training_data():
    fr = open("training.data", 'rb')
    TrainingDictionary = pickle.load(fr)
    fr.close()
    return TrainingDictionary

#TrainingDictionary = load_training_data()
#print(TrainingDictionary)
TrainingDictionary = {}

for i in range(1, 4):
    add_training_data('light', 'on', "image" + str(i)+ ".png", TrainingDictionary)


TrainingDictionary = load_training_data()
print(TrainingDictionary)

    
