
## WhoAreYou?

A Flask project using open-cv and deepface analyze to predict the given image(face).

Predictions include: Age, Race, Gender, Emotion and dominant features. 

## Requirements

- Flask
```bash
import Flask
```
- DeepFace
```bash
from deepface import DeepFace
```
- cv2
```bash
import cv2
```

## Install and Run

Clone the repo
```bash
  git clone https://github.com/matheusclmb/WhoAreYou.git
```
Install the requirements
```bash  
  pip install -r requirements.txt
```
Run with Python
```bash
  python app.py
```