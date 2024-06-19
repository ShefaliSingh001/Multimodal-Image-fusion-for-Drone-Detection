import os
import shutil
from sklearn.model_selection import train_test_split

# Create directory to save data
data_folder = '/Users/shefalisingh/Desktop/mini_proj'
os.makedirs(data_folder, exist_ok=True)

# Define paths for images and labels folders
image_folder = '/Users/shefalisingh/Desktop/mini_proj/images'
label_folder = '/Users/shefalisingh/Desktop/mini_proj/labels'

# Create folders for train, test, and validate images and labels
train_images_folder = os.path.join(data_folder, 'train_images')
test_images_folder = os.path.join(data_folder, 'test_images')
val_images_folder = os.path.join(data_folder, 'val_images')

train_labels_folder = os.path.join(data_folder, 'train_labels')
test_labels_folder = os.path.join(data_folder, 'test_labels')
val_labels_folder = os.path.join(data_folder, 'val_labels')

os.makedirs(train_images_folder, exist_ok=True)
os.makedirs(test_images_folder, exist_ok=True)
os.makedirs(val_images_folder, exist_ok=True)

os.makedirs(train_labels_folder, exist_ok=True)
os.makedirs(test_labels_folder, exist_ok=True)
os.makedirs(val_labels_folder, exist_ok=True)

# Load image filenames
image_filenames = os.listdir(image_folder)

# Split data into train, validation, and test sets
X_train_val, X_test =train_test_split(image_filenames, test_size=0.2, random_state=1)
X_train, X_val =train_test_split(X_train_val, test_size=0.25, random_state=1)

# Function to copy images and corresponding labels from source to destination folder
def copy_images_and_labels(source_paths, dest_image_folder, dest_label_folder):
    for path in source_paths:
        # Copy image
        shutil.copy(os.path.join(image_folder, path), os.path.join(dest_image_folder, path))
        # Load corresponding label from txt file
        label_file_path = os.path.join(label_folder, os.path.splitext(path)[0] + '.txt')
        shutil.copy(label_file_path, os.path.join(dest_label_folder, os.path.basename(label_file_path)))

# Copy images and labels to respective train, test, and validation folders
copy_images_and_labels(X_train, train_images_folder, train_labels_folder)
copy_images_and_labels(X_val, val_images_folder, val_labels_folder)
copy_images_and_labels(X_test, test_images_folder, test_labels_folder)
