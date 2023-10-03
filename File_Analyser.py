import os
import pandas as pd
import re
import subprocess
import glob


def extract_file_names(content, pattern):
    """
    Extract filenames from content based on a given pattern.

    Args:
    - content (str): The content to search within.
    - pattern (str): The regex pattern to search for.

    Returns:
    - list: A list of filenames that match the pattern.
    """
    return re.findall(pattern, content, re.MULTILINE | re.IGNORECASE)


def generate_tree(directory, output_file):
    """
    Generate a directory tree and save it to an output file.

    Args:
    - directory (str): The directory to generate the tree for.
    - output_file (str): The file to save the tree to.
    """
    with open(output_file, 'w') as f:
        for root, dirs, files in os.walk(directory):
            level = root.replace(directory, '').count(os.sep)
            indent = ' ' * 4 * (level)
            f.write('{}{}/\n'.format(indent, os.path.basename(root)))
            sub_indent = ' ' * 4 * (level + 1)
            for file in files:
                f.write('{}{}\n'.format(sub_indent, file))


def pad_lists_to_same_length(*lists):
    """
    Pad lists with None until they all have the same length.

    Args:
    - *lists: Lists to be padded.

    Returns:
    - list: A list of lists, all padded to the same length.
    """
    max_length = max(len(lst) for lst in lists)
    return [lst + [None] * (max_length - len(lst)) for lst in lists]


def main():
    # Generate directory tree
    subprocess.run(["Tree", "/F", "/A", "> Review_Data.txt"], shell=True, check=True)

    # Get the current directory and list of directories
    current_dir = os.getcwd()
    directories = [name for name in os.listdir(current_dir) if os.path.isdir(os.path.join(current_dir, name))]

    # Read the content of Review_Data.txt
    review_data_path = os.path.join(current_dir, "Review_Data.txt")
    generate_tree(current_dir, review_data_path)
    try:
        with open(review_data_path, 'r') as f:
            content = f.read()
    except FileNotFoundError:
        print(f"Error: {review_data_path} not found.")
        return

    # Extract filenames based on patterns
    full_report_files = extract_file_names(content, r"[\w+-]+.Full_Report.html")
    metrics_report_files = extract_file_names(content, r"[\w-]+.Metrics_Report.html")
    testcase_management_report_files = extract_file_names(content, r"[\w-]+.[\w-]+.Testcase_Management_Report.html")

    # Pad the lists to the same length
    directories, full_report_files, metrics_report_files, testcase_management_report_files = pad_lists_to_same_length(
        directories, full_report_files, metrics_report_files, testcase_management_report_files
    )

    # Create DataFrame
    review_data_set = {
        'File Name': directories,
        'Full Report': full_report_files,
        'Metrics_Report': metrics_report_files,
        'Testcase_Management_Report': testcase_management_report_files
    }
    df = pd.DataFrame(review_data_set)

    # Save DataFrame to Excel
    df.to_excel("output.xlsx", index=False)
    print(df)


if __name__ == "__main__":
    main()
