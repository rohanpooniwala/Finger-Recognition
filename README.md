# Finger-Recognition
Finger Recognition Using CNN in TFLearn

TFlearn is a modular and transparent deep learning library built on top of Tensorflow. It was designed to provide a higher-level API to TensorFlow in order to facilitate and speed-up experimentations, while remaining fully transparent and compatible with it.

link: http://tflearn.org/

I have used TFLearn to create CNN and openCV to collect and store data, and to process data.

<ul>
  <li>record.py uses openCV to record and store data in folders. 
    <ul>
      <li> Press 1,2,3,4 or 5 to change the finger image that is being stored.
      <li> press 'space' to store the image.
      <li> press 'esc' to quit.
    </ul>
  <li>Use train.py to train the CNN. It automatically saves the weights when it finishes training.
  <li>Use run_cnn.py to run the finger detection. It automatically loads the saved weights.
</ul>
