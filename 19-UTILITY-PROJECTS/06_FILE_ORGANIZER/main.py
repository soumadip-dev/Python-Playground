import os


def rename_files_by_extension(file_list, target_extension):
    # Filter files that match the given extension
    matching_files = [
        file_name for file_name in file_list if file_name.endswith(target_extension)
    ]

    file_counter = 1

    # Create the "photos" directory if it does not exist
    if not os.path.exists("photos"):
        os.mkdir("photos")

    # Rename and move each matching file
    for original_file_name in matching_files:
        new_file_name = f"photo-{file_counter}{target_extension}"
        new_file_path = os.path.join("photos", new_file_name)

        os.rename(original_file_name, new_file_path)
        file_counter += 1


# Execute the script only when it is run directly
if __name__ == "__main__":
    current_directory_files = os.listdir()
    rename_files_by_extension(current_directory_files, ".jpg")
