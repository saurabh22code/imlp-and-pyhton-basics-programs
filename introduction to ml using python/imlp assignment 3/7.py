'''Q.7. Create a python programme to create a copy of the existing image file 

Here is a Python program to create a copy of an existing image file using the pickle module:
'''
import pickle

def copy_image_with_pickle(source_file, destination_file):
    try:
        # Step 1: Read the image file in binary mode
        with open(source_file, "rb") as source:
            image_data = source.read()

        # Step 2: Serialize the image data using pickle
        with open("temp_pickle.pkl", "wb") as pickle_file:
            pickle.dump(image_data, pickle_file)

        # Step 3: Deserialize the image data from the pickle file
        with open("temp_pickle.pkl", "rb") as pickle_file:
            copied_image_data = pickle.load(pickle_file)

        # Step 4: Write the copied data to the destination file
        with open(destination_file, "wb") as destination:
            destination.write(copied_image_data)

        print(f"Image has been successfully copied to {destination_file}")
    except FileNotFoundError:
        print(f"The file '{source_file}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
source_file = "source_image.jpg"  # Replace with the path to your source image
destination_file = "copied_image.jpg"  # Replace with the desired name for the copied image

copy_image_with_pickle(source_file, destination_file)
