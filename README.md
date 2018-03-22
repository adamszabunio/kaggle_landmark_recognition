# kaggle_landmark_recognition

### To pass some time in between interviews, thought I would compete in my first Kaggle competition:
### [The Google Landmark Recognition Challenge](https://www.kaggle.com/c/landmark-recognition-challenge) 

- The main purpose of this repo is to be used as a refresher of deep learning topics.

- This Kaggle competiton uses over one million (1,225,029) training images of popular landmarks, such as the Colosseum in Rome, Italy: 

<img height="120px" src="http://lh3.ggpht.com/-KXyELwqwp_Q/Ry-qmQAqwUI/AAAAAAAAAoU/SUt6osy86xk/s1600/" />
<img style='height: 20px; margin: 1px; float: left; border: 1px solid black;' src='http://lh3.ggpht.com/-GtgCG7ZNNDw/TWWRUVMMpUI/AAAAAAAAC00/AUNX8bd957w/s1600/' /><img style='height: 20px; margin: 1px; float: left; border: 1px solid black;' src='http://lh6.ggpht.com/-Xc0B_C_xpfc/RsIor9h8-SI/AAAAAAAABK0/d6gJYx06eKI/s1600/' /><img style='height: 20px; margin: 1px; float: left; border: 1px solid black;' src='https://lh3.googleusercontent.com/-r7w0c7chrC8/TKvJKIyP-yI/AAAAAAAAAbE/G1GYmt5t-bg/s1600/' />

- From just these 4 images above, you can see how this will be a challenge to classify all of these images as "Colosseum"

- However, an even larger challenge is the uneven distrbution of the Landmarks:
    + From [initial EDA](eda_training_data.ipynb) we found there are ≈15K unique Landmarks in our training set of 1.2 million images.
    + Nearly 44% of the Landmarks have at most 10 images.
    + Furthermore, 20 of the most frequent Landmarks contain one-third of the training images!

![Landmark Distribution](/images/landmark_dist.png)

