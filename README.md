Usage
-----

Create a file <plk_file_name> containing all of the md5 hashes of files in \<path>.

`python gen_md5_dictionary.py <path> <pkl_file_name>`

Test to see which files in path <new_path> were contained in <path> using <pkl_file_name>. Creates two files that contain the list of duplicate and non-duplicate files from <new_path>. 

`python compare_against_dict.py <new_path> <pkl_file_name> <dup_file> <non_dup_file>`