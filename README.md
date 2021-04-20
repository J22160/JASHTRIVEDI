# COMPARISON OF PRE TRAINED MODEL(VGG19) TO CNN

### Input data:
The data consists of cell images. The task is to identify whether the indiviual is infected to malaria or not.
![DATA IMAGE](https://user-images.githubusercontent.com/71454551/115407899-0d38cc00-a20e-11eb-8fbc-10dc84323b09.png)

**Training size: 416 images** 

**Validation size: 134 images**

### Model used 
**1. VGG19**

VGG-19 is a convolutional neural network that is 19 layers deep. The pretrained network can classify images into 1000 object categories

![VGG19](https://user-images.githubusercontent.com/71454551/115407778-f6927500-a20d-11eb-890f-ddc4b7727185.png)

**2.CNN model**

It is a sequential model having 2 Convolutional Blocks and a Fully Connected Layer.

### Accuracy and loss graph 
**1. VGG19**

![vgg19 accuracy](https://user-images.githubusercontent.com/71454551/115408005-22adf600-a20e-11eb-95e7-d98b4d6866d8.png) ![vgg19 loss](https://user-images.githubusercontent.com/71454551/115408084-35c0c600-a20e-11eb-96df-db012ae393b1.png)

**2. CNN model**

![CNN model accuracy](https://user-images.githubusercontent.com/71454551/115408166-47a26900-a20e-11eb-98c8-e0a7948dcf4d.png) ![CNN model loss](https://user-images.githubusercontent.com/71454551/115408270-59840c00-a20e-11eb-96fd-37126c556cda.png)

### Score:

![score](https://user-images.githubusercontent.com/71454551/115410516-538f2a80-a210-11eb-90dd-2ca52974ec85.png)

### Conclusion 

The pre-trained model outperforms the CNN Model and also has a higher mean accuracy. Fine tuning the pre trained model by using a 2 step process also contributes in a higher validation accuracy.
