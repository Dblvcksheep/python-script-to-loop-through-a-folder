import os

# Define paths
folder_path = 'C:/Users/leona/PycharmProjects/Vortex/src'  # Adjust if needed (e.g., use absolute path)
output_file = 'combined.txt'

# Ensure the folder exists
if not os.path.exists(folder_path):
    print(f"Error: The folder '{folder_path}' does not exist.")
    exit(1)

# Open the output file
with open(output_file, 'w', encoding='utf-8') as output:
    for root, dirs, files in os.walk(folder_path):
        # Filter for .sol files (optional: remove this if you want all files)
        # sol_files = [f for f in files if f.endswith('.sol')]  #this is if i want to get specific files
        # for filename in sol_files:
        for filename in files:
            file_path = os.path.join(root, filename)
            print(f'Processing {file_path}')
            try:
                with open(file_path, 'r', encoding='utf-8') as file:
                    content = file.read()
                    output.write(f'\n\n-- {file_path} --\n')
                    output.write(content)
            except UnicodeDecodeError as e:
                print(f'Encoding error in {file_path}: {e}')
            except PermissionError as e:
                print(f'Permission error in {file_path}: {e}')
            except Exception as e:
                print(f'General error reading {file_path}: {e}')

print(f"Combined output written to {output_file}")