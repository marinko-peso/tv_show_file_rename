# tv_show_file_rename
Script to automatically remove noise from tv series season/episodes by renaming them to only contain season and episode numbers in format SnumberEnumber. Can also be used for subtitle files.

### Usage
`python tv_show_file_rename.py directory_path`

When you provide the script with a directory it will automatically scan throught it and attempt to find all supported files inside that contain two numbers required for season and episode. After that it will rename them.

### Customization
You can customize the script to support whatever file type you want it to by just modifying the settings on top of the script. This is to make sure you don't rename some other files you didn't have intention to.
- ALLOWED_FILE_TYPES - which file types are allowed to be renamed.
