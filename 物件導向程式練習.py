
#(a) 定義一個學生類。一個學生具有以下屬性：名字、姓氏、性別（可以是男性或女性）、狀態（可以是大一、大二、大三和大四）和GPA。
#然後為學生類定義以下方法：
#show_myself方法將在調用對象時簡單打印所有屬性變量。此方法沒有輸入參數。
#study_time方法將根據以下公式增加學生的GPA： gpa = gpa + log(study_time)。此方法的唯一輸入參數是study_time變量。此外，確保即使學生學習了很長時間，GPA變量也永遠不會超過4.0。
#(b) 現在定義5個學生對象，並將對象存儲在名為student_list的列表中。這五個學生是：Mike Barnes、Jim Nickerson、Jack Indabox、Jane Miller和Mary Scott。Mike是大一，Jim是大二，Jack是大三，Jane和Mary是大四。他們各自的GPA分別為：4、3、2.5、3.6和2.7。請確保在實例化對象時分配性別。
#然後在所有對象上調用show_myself方法。我建議您使用一個循環來生成對象，使用另一個循環來顯示對象。
#(c) 使用上面的對象，讓這5位學生分別學習60、100、40、300、1000分鐘。因此，第一個學生學習60分鐘，第二個學習100分鐘，依此類推。然後再次在所有5個學生上調用show_myself方法，檢查他們的新GPA是否反映了他們的學習時間。
from asyncio import log
import math

students_info = [
    ("Mike", "Barnes", "male", "freshman", 4.0),
    ("Jim", "Nickerson", "male", "sophomore", 3.0),
    ("Jack", "Indabox", "male", "junior", 2.5),
    ("Jane", "Miller", "female", "senior", 3.6),
    ("Mary", "Scott", "female", "senior", 2.7)
]

GPA=   [4.0,3.0,2.5,3.6,2.7]

studytime= [60,100,40,300,1000]

student_list=[]


class Classmates:
    def __init__(self,firstname,lastname,gender,status,gpa):
        self.firstname = firstname
        self.lastname = lastname
        self.gender = gender
        self.status = status
        self.gpa = gpa
    
    def show_Myself(self):
        print ("Name:{self.firstname},{self.lastname},Gender:{self.gender},Status:{self.status},GPA:{self.gpa}")
# gpa = gpa + log(study_time)
    def gpa(self,GPA,studytime):
        