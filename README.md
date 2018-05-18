## Clone the Repository
 1. On GitHub, navigate to the main page of the repository https://github.com/Dmytruto/NormalSmartDevice.
 2. Click <strong> Clone or download. </strong>
 3. Copy the URL provided.
 4. Open <strong> Git Bash. </strong>
 5. Choose and go to the directory where you want the cloned directory to be made.(It must be the same folder where you want to use this project)
 6. Type there <strong> git clone (URL that you copied) </strong>
 ```git
 $ git clone https://github.com/Dmytruto/NormalSmartDevice.git
 ```
 7. Press <strong> Enter. </strong> Your local clone will be created.
 ## Creating DataSet
 ### Import CreateTrainingDataAndTrainModel.py
 First of all you need to import our module in file where you want to use it.
  ```python
  import NormalSmartDevice.FacialRecognition.CreateTrainingDataAndTrainModel as CTD
  ```
### Next step
This function creates a directory named faces which will be contain a sub folders with photo set. In input this function takes the directory name and creates the subfolder with inputted name. 
```python 
  CTD.create_directory(sub_directory_name)
```
### Exstracting face from the image
 In input this function has the image. if this image contains faces, function will returns grayscaling cropped face from this image.else it will return emty list.
 ```python
 CTD.face_extractor(img)
 ```
 ### Take a photos
 This function reads images from your web cam and if face is on image it saves the image in subfolder that you have already created. In input this function takes number of photo which you want to be in your data set.
 ```python
 CTD.start_creating_data_set(quantity)
 ```
 ### Train model
This function create histograms from all images in subfolder and save this histogram in json file. In input this method has name of trained model. In order to program work successfully <strong>file_name</strong> must be the same as <strong>sub_directory_name</strong>.
 ```python
CTD.trainModel(file_name)
```
<strong style="font-size: 1.1rem;"> !To create data set and trained model on this data you have to execute this functions in the same order that It had been written on this article!</strong>
 
 ## Face Recognition
 ### Import FaceRecognition.py
 Import reconizer which have already trained on the Data Set.
  ```python
  import NormalSmartDevice.FacialRecognition.FaceRecognition as FR
  ```

### Run Recognizer
In input this function takes human face image and compare it with faces which had been used to create DataSet. If face on the input image is similar to one of the faces in data set, function will return true, else false. 
```python 
  FR.face_recognizer(face_image)
```
<strong style="font-size: 1.1rem;">In order to use face recognizer firstly you need create data set and train model</strong>
