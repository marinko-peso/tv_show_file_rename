# tv_show_file_rename
Script to automatically remove noise from tv series season/episodes by renaming them to only contain season and episode numbers in format SnumberEnumber. Can also be used for subtitle files.

### Usage
`python tv_show_file_rename.py directory_path`

When you provide the script with a directory it will automatically scan throught it and attempt to find all supported files inside that contain two numbers required for season and episode. After that it will rename them.

### Customization
- ALLOWED_FILE_TYPES - support to specific file types. This is to make sure you don't rename some other files you didn't have intention to.
- FILE_RENAME_FORMAT - generated name format, make sure to keep both placeholders if you change it.
