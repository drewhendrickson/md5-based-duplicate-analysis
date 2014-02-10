Usage
-----

Create a file <plk_file_name> containing all of the md5 hashes of files in \<path>.

`python gen_md5_dictionary.py <path> <pkl_file_name>`

Test to see which files in path <new_path> were contained in <path> using <pkl_file_name>. Creates two files that contain the list of duplicate and non-duplicate files from <new_path>. 

`python compare_against_dict.py <new_path> <pkl_file_name> <dup_file> <non_dup_file>`



## Sample:

```
// create <new_pkl> file containing all md5 hashes of files in <path1>
// create two files that list the duplicates found in <path1>: orig_dup.txt, orig_comp.txt
python gen_md5_dictionary.py <path1> <new_pkl> orig_dup.txt orig_comp.txt

// compare files in <path2> to <new_pkl>
// create 3 files: non_dup.txt, dup.txt, comp.txt
python compare_against_dict.py <path2> <new_pkl> image_info/non_dup.txt image_info/dup.txt image_info/comp.txt

cd scripts

// copy the non-duplicated files to <new-pics> folder and save output of script
./copy_files.sh ../image_info/non_dup.txt <new-pics> > non_out.txt

// before doing this check that all the files copied without any issue
// delete the non-duplicate files from their original locations
./del_files.sh ../image_info/non_dup.txt


// copy the duplicated files to <dup-pics> folder and save output of script
./copy_files.sh ../image_info/dup.txt <dup-pics> > dup_out.txt

// before doing this check that all the files copied without any issue
// delete the duplicate files from their original locations
./del_files.sh ../image_info/dup.txt

```

## Useful notes:
### OSes drop tons of files into directories.
### There are some iles to delete before running the python scripts:

.DS_Store  
.picasa.ini  
Picasa.ini  
Thumbs.db  
.iPhoto.db  
.ipspot_update  
.DSS
Icon

### To delete these files using *nix command line:
` find . -iname 'Thumbs.db' -type f -delete `

