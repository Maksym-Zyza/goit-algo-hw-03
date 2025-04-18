import os
import shutil
import argparse


def copy_files(source_path, dest_path):
    try:
        # Create destination directory if it doesn't exist
        os.makedirs(dest_path, exist_ok=True)
        
        # Iterate through all items in the source directory
        for item in os.listdir(source_path):
            item_path = os.path.join(source_path, item)
            
            # If item is a directory, recursively process it
            if os.path.isdir(item_path):
                copy_files(item_path, dest_path)
            # If item is a file, copy it to appropriate subdirectory
            elif os.path.isfile(item_path):
                # Get file extension (without dot) or use 'no_extension' if none
                extension = os.path.splitext(item)[1][1:] or 'no_extension'
                
                # Create subdirectory for the extension
                extension_dir = os.path.join(dest_path, extension)
                os.makedirs(extension_dir, exist_ok=True)
                
                # Copy file to the appropriate subdirectory
                shutil.copy2(item_path, os.path.join(extension_dir, item))
                
    except PermissionError as e:
        print(f"Permission error: {e}")
    except Exception as e:
        print(f"Error processing {source_path}: {e}")

def main():
    parser = argparse.ArgumentParser(description='Copy and sort files by extension')
    parser.add_argument('source_dir', help='Source directory path')
    parser.add_argument('dest_dir', nargs='?', default='dist', help='Destination directory path (default: dist)')
    
    args = parser.parse_args()
    
    source_dir = args.source_dir
    dest_dir = args.dest_dir
    
    # Check if source directory exists
    if not os.path.exists(source_dir):
        print(f"Error: Source directory '{source_dir}' does not exist")
        return
    
    # Check if source is a directory
    if not os.path.isdir(source_dir):
        print(f"Error: '{source_dir}' is not a directory")
        return
    
    print(f"Copying files from {source_dir} to {dest_dir}")
    copy_files(source_dir, dest_dir)
    print("File copying and sorting completed")

if __name__ == "__main__":
    main() 