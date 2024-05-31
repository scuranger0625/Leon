import subprocess

def extract_with_password(archive_path, destination_dir, password):
    command = ['C:\\Program Files\\WinRAR\\rar.EXE', 'x', '-p' + password, '--', archive_path, destination_dir]
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()
    return process.returncode, stdout, stderr


#指定解壓鎖檔案和解壓縮位置
def main():
    archive_path = "C:\\Users\\Leon\\Desktop\\SGZ14\\San14PK V1.0.10+1.0.25.part1"
    destination_dir = "C:\\Users\\Leon\\Desktop\\SGZ14\\三國志14PK"
    # 生成所有可能的密碼
    passwords = [str(i).zfill(6) for i in range(1000000)]  

    for password in passwords:
        print("Trying password:", password)
        returncode, stdout, stderr = extract_with_password(archive_path, destination_dir, password)
        if returncode == 0:
            print("Extraction successful with password:", password)
            break
        else:
            print("Extraction failed with password:", password)
            print("Error message:", stderr.strip())

if __name__ == "__main__":
    main()








