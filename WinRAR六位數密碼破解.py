import itertools
import patoolib
import os

def extract_rar_with_password(rar_path, output_path):
    # 將文件名更改為.rar
    renamed_rar_path = os.path.splitext(rar_path)[0] + ".rar"
    os.rename(rar_path, renamed_rar_path)

    # 生成所有六位數密碼的組合
    for password in itertools.product('0123456789', repeat=6):
        password = ''.join(password)
        try:
            print(f"嘗試密碼: {password}")
            patoolib.extract_archive(renamed_rar_path, outdir=output_path, password=password)
            print(f"成功解壓縮，密碼是: {password}")
            os.rename(renamed_rar_path, rar_path)  # 將文件名改回原始文件名
            return True
        except patoolib.util.PatoolError as e:
            if 'non-zero exit status 11' in str(e):
                print(f"密碼錯誤: {password}")
                continue
            else:
                print(f"解壓縮時發生錯誤: {e}")
                break
        except Exception as e:
            print(f"發生未知錯誤: {e}")
            break

    print("所有密碼都已嘗試，未找到正確的密碼。")
    os.rename(renamed_rar_path, rar_path)  # 將文件名改回原始文件名
    return False

# 使用示例
rar_path = r"C:\Users\Leon\Desktop\SGZ14\San14PK V1.0.10+1.0.25\San14PK V1.0.10+1.0.25\San14PK V1.0.10+1.0.25.part1.rar"
output_path = r"C:\Users\Leon\Desktop\SGZ14\三國志14PK"
extract_rar_with_password(rar_path, output_path)





