Code for paper titled Transfer Learning for Human Activity Recognition using Representational Analysis of Neural Networks

The code is divided into folders. matlab_code and python_code

The matlab_code folder generates the figures presented in the paper. Description of each file is below:

plot_cnn_accuracy.m -> This file plots the baseline accuracy when trained on one UC and test on others. The 
input file can be changed to get the accuracy for the other datasets. This is done on line 14.

plot_cnn_acc_after_FT.m -> This file plots the accuracy after fine-tuning. The 
input file can be changed to get the accuracy for the other datasets. This is done on line 4.

plot_cca_distances.m -> This file generates the CCA distances between the networks trained on same UC. 
To change the dataset line 50 and 53 need to be changed. Number of features of wHAR is 120 while it is 561
for the other two datasets.

plot_CCA_cross_UC.m -> This file generates the CCA distances between the networks trained on different UC. 
To change the dataset line 27, 31, 32 to be changed. Number of features of wHAR is 120 while it is 561
for the other two datasets.

the train_test_files/ folder provides the user clusters obtained from k-means clustering for the three datasets.


The python_code folder contains the training code and pre-trained models.

The pre-trained models are present the ./CNN/ folder for the three datasets. 

wHAR_UC_k_means_HAR_with_syn -> wHAR
UCI_UC_k_means_HAR_33_17 -> HCI HAR
HAPT_UC_k_means_HAR_33_17 -> UCI HAPT
unimib_UC_k_means -> unimib
WISDM_UC_k_means -> WISDM

Explanation of files

har_streaming_CNN.py -> This file performs the training, accuracy evaluation and fine-tuning for the CNNs.
The file is currently set up for the wHAR dataset. To change to a different dataset, we need to change all the file
paths to point to the new datasets.

har_calculate_cca_within_uc_CNN.py -> Calculates the CCA distance for networks trained with the same UC. To change to a different dataset, we need to change all the file
paths to point to the new datasets.

har_calculate_cca_cross_uc_CNN -> Calculates the CCA distance for networks trained with different UCs. To change to a different dataset, we need to change all the file
paths to point to the new datasets.

har_convergence_analysis.py -> Plots the convergence figures for baseline training and finetuning.

Finally, CCA distances with the pre-trained models are present in the folder cca_out. The folder names give
the details of the dataset used and the scenario.



