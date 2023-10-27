import zipfile

def extract_archive(filepath,dest_dir) :
    with zipfile.ZipFile(filepath,"r") as archive :
        archive.extractall(dest_dir)



if __name__ == "__main__" :
    extract_archive(r"C:\Users\Nags\Videos\Captures\compressed.zip",
                    r"C:\Users\Nags\PycharmProjects\python course\dest_dir")