
#(a) 定義一個學生類。一個學生具有以下屬性：名字、姓氏、性別（可以是男性或女性）、狀態（可以是大一、大二、大三和大四）和GPA。
#然後為學生類定義以下方法：
#show_myself方法將在調用對象時簡單打印所有屬性變量。此方法沒有輸入參數。
#study_time方法將根據以下公式增加學生的GPA： gpa = gpa + log(study_time)。此方法的唯一輸入參數是study_time變量。此外，
#確保即使學生學習了很長時間
#，GPA變量也永遠不會超過4.0。
#(b) 現在定義5個學生對象，並將對象存儲在名為student_list的列表中。這五個學生是：Mike Barnes、Jim Nickerson、Jack Indabox、Jane Miller
#和Mary Scott。Mike是大一，Jim是大二，Jack是大三，Jane和Mary是大四。他們各自的GPA分別為：4、3、2.5、3.6和2.7。請確保在實例化對象時分配性別。
#然後在所有對象上調用show_myself方法。我建議您使用一個循環來生成對象，使用另一個循環來顯示對象。
#(c) 使用上面的對象，讓這5位學生分別學習60、100、40、300、1000分鐘。因此，第一個學生學習60分鐘，第二個學習100分鐘，依此類推。
#然後再次在所有5個學生上調用show_myself方法，檢查他們的新GPA是否反映了他們的學習時間。


from asyncio import log
import math

# 定義學生信息、GPA 和 studytime
students_info = [
    ("Mike", "Barnes", "男性", "大一"),
    ("Jim", "Nickerson", "男性", "大二"),
    ("Jack", "Indabox", "男性", "大三"),
    ("Jane", "Miller", "女性", "大四"),
    ("Mary", "Scott", "女性", "大四")
]

GPA = [4.0, 3.0, 2.5, 3.6, 2.7]

studytime = [60, 100, 40, 300, 1000]

student_list = []


class Student:
    def __init__(self, firstname, lastname, gender, status, gpa):
        self.firstname = firstname
        self.lastname = lastname
        self.gender = gender
        self.status = status
        self.gpa = gpa
    
    def show_myself(self):
        print(f"姓名: {self.firstname} {self.lastname}, 性別: {self.gender}, 狀態: {self.status}, GPA: {self.gpa}")
    
    def study_time(self, study_time):
        # 根據傳入的 study_time 參數更新 GPA 屬性，但不超過最大成績
        max_gpa = self.gpa  # 獲取學生的最大GPA
        self.gpa = min(max_gpa, self.gpa + math.log(study_time))
        #新增GPA不大於4.0的上限
        if self.gpa>4.0:
            self.gpa=4.0
                


# 創建學生對象並添加到 student_list 中
for info, gpa, study_time in zip(students_info, GPA, studytime):  # 使用 zip 迭代三個列表
    student = Student(*info, gpa)
    student.study_time(study_time)
    student_list.append(student)

# 調用 show_myself 方法顯示所有學生的信息
for student in student_list:
    student.show_myself()


