## Face Detection 

### Requirements
python3

### Setup
- [optional] create a python virtual environment<br>
`python -m venv env`

- Install opencv for python<br>
`pip install opencv_python`

### Commands
`python face_detect.py --image path_to_image --neighbors integer`

### Example
`face_detect.py --image images/img_3.jfif`<br>
<img src="images/sample_outputs/img_3_output.png" width="40%">

### Adjustments
Somestimes there will be false positives<br>
`face_detect.py --image images/img_6.jfif`<br>
<img src="images/sample_outputs/img_6_output.png" width="40%">

Adjusting the minimum neighbors value to 8<br>
`face_detect.py --image images/img_6.jfif --neighbors 8`<br>
<img src="images/sample_outputs/img_6_nb8_output.png" width="40%">
