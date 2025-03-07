'''
AI50 2023
Week 5: traffic.py

Complete the implementation of load_data and get_model in traffic.py.

To Run:
    python traffic.py gtsrb
'''
import cv2
import numpy as np
import os
import sys
import tensorflow as tf

from sklearn.model_selection import train_test_split

EPOCHS = 10
IMG_WIDTH = 30
IMG_HEIGHT = 30
NUM_CATEGORIES = 43
TEST_SIZE = 0.4


def main():

    # Check command-line arguments
    if len(sys.argv) not in [2, 3]:
        sys.exit("Usage: python traffic.py data_directory [model.h5]")

    # Get image arrays and labels for all image files
    images, labels = load_data(sys.argv[1])

    # Split data into training and testing sets
    labels = tf.keras.utils.to_categorical(labels)
    x_train, x_test, y_train, y_test = train_test_split(
        np.array(images), np.array(labels), test_size=TEST_SIZE
    )

    # Get a compiled neural network
    model = get_model()

    # Fit model on training data
    model.fit(x_train, y_train, epochs=EPOCHS)

    # Evaluate neural network performance
    model.evaluate(x_test,  y_test, verbose=2)

    # Save model to file
    if len(sys.argv) == 3:
        filename = sys.argv[2]
        model.save(filename)
        print(f"Model saved to {filename}.")


def load_data(data_dir):
    """
    Load image data from directory `data_dir`.
    Assume `data_dir` has one directory named after each category, numbered
    0 through NUM_CATEGORIES - 1. Inside each category directory will be some
    number of image files.
    Return tuple `(images, labels)`. `images` should be a list of all
    of the images in the data directory, where each image is formatted as a
    numpy ndarray with dimensions IMG_WIDTH x IMG_HEIGHT x 3. `labels` should
    be a list of integer labels, representing the categories for each of the
    corresponding `images`.
    """
    # Initialize empty lists for images and labels
    images = []
    labels = []

    # Iterate through data set directories
    for directory in os.listdir(data_dir):
        
        # Iterate through single image files in the current directory
        print(f"Started loading files from {directory} directory")
        for file in os.listdir(os.path.join(data_dir, directory)):
            
            # Read image file and resize it to IMG_WIDTH x IMG_HEIGHT
            image = cv2.imread(os.path.join(data_dir, directory, file))
            resized = cv2.resize(image, (IMG_WIDTH, IMG_HEIGHT))
            
            # Append resized image and corresponding label to the lists
            images.append(resized)
            labels.append(int(directory))
            
        print(f"Ended loading files from {directory} directory")
        
    # Return the images and labels as numpy arrays wrapped in a tuple
    return np.array(images), np.array(labels)


def get_model():
    """
    Returns a compiled convolutional neural network model. Assumes that the
    `input_shape` of the first layer is `(IMG_WIDTH, IMG_HEIGHT, 3)`.
    The output layer should have `NUM_CATEGORIES` units, one for each category.
    """
    model = tf.keras.models.Sequential([
        # Convolutional layer
        tf.keras.layers.Conv2D(
            filters=32,
            kernel_size=(3, 3),
            activation='relu',
            input_shape=(IMG_WIDTH, IMG_HEIGHT, 3)
        ),
        
        # Max-pooling layer
        tf.keras.layers.MaxPooling2D(
            pool_size=(2, 2)
        ),

        # Second convolutional layer
        tf.keras.layers.Conv2D(
            filters=32,
            kernel_size=(3, 3),
            activation='relu'
        ),

        # Flatten layer
        tf.keras.layers.Flatten(),

        # Dense layer with ReLU activation and dropout
        tf.keras.layers.Dense(
            units=128,
            activation='relu'
        ),
        tf.keras.layers.Dropout(
            rate=0.5
        ),

        # Output layer with softmax activation
        tf.keras.layers.Dense(
            units=NUM_CATEGORIES,
            activation='softmax'
        )
    ])

    # Compile the model with Adam optimizer, categorical crossentropy loss,
    # and accuracy metric
    model.compile(
        optimizer=tf.keras.optimizers.Adam(),
        loss='categorical_crossentropy',
        metrics=['accuracy']
    )

    return model

if __name__ == "__main__":
    main()
