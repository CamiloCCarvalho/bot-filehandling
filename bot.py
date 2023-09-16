from botcity.plugins.files import BotFilesPlugin

# Instantiate the plugin
files = BotFilesPlugin()

# List of all files that will be zipped
files_path = ['docs/example.txt', 'docs/img/test.png']

# Creates a zip file called "my_zip" containing the given files
files.zip_files(files_path, "my_zip.zip")


# For Directory
files.zip_directory("docs", "result.zip")


# with away file download 
with files.wait_for_file(directory_path="/Users/ash/Downloads", file_extension=".mp3", timeout=30000):
    print("\nDownloading will start ...")
print("\nDownload completed, continuing the process...")

# Getting the path of the newest ".bin" file in the "downloads" folder
files_path_2 = files.get_last_created_file(directory_path="/Users/ash/Downloads", file_extension=".mp3")
print(files_path_2)