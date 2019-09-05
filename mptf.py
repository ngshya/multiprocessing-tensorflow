# Run Tensorflow/Keras models in parallel with multiprocessing


# Python 3.6.8
# tensorflow==2.0.0rc0
# tensorflow-gpu==2.0.0rc0
# numpy==1.16.1


# Import packages.
import tensorflow as tf
from tensorflow.keras import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.optimizers import Adam
import multiprocessing as mp
from tensorflow.keras.models import load_model
import os


# Settings
os.environ['CUDA_VISIBLE_DEVICES'] = '-1'
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3' 
mp.set_start_method('spawn', force=True) # (*)


# Function that will be executed in each worker.
def myF(i):
    print("Worker " + str(i) + " working...")
    import tensorflow as tf # (*)
    model = load_model("model.h5")
    print("Worker " + str(i) + " done!")
    return "Worker " + str(i) + " OK!"


# Main 
def main():
    model = Sequential([
    Dense(64, activation='relu', input_shape=(32,)),
    Dense(64, activation='relu'),
    Dense(10, activation='softmax')])
    model.compile(optimizer=Adam(0.01),
                  loss='categorical_crossentropy',
                  metrics=['accuracy'])
    model.save("model.h5")
    p = mp.Pool(5)
    output = p.map(myF, [1,2,3,4,5])
    p.close()
    p.join()
    print(output)



if __name__ == "__main__":
    main()