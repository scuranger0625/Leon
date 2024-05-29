#[Set]
#使⽤set型別完成下列問題: 本班期末考試
#數學及格的有: Tom, John, Mary, Jimmy, Sunny, Amy
#英⽂及格的有: John, Mary , Tony , Bob , Pony, Tom , Alice
#分別印出數學及格但英⽂不及格的名單，數學不及格但英⽂及格的名單，兩科都及格名單
#最後印出全班總共有幾個同學

math_pass = {"Tom", "John", "Mary", "Jimmy", "Sunny", "Amy"}

eng_pass = {"John", "Mary" , "Tony" , "Bob" , "Pony", "Tom" , "Alice"}

#數學及格且英文及格的人
allpass = (math_pass & eng_pass)


#數學及格英文被當的人
#print(math_pass & eng_fail) #比較直觀
#或是  print(allpass-eng_pass)
print('數學及格但英文被當的人',math_pass-eng_pass) #較省行數

#數學被當但英⽂及格的名單

print('英文及格但數學被當的人',eng_pass-math_pass)

#兩科皆及格的人

print ('兩科都及格的人',allpass)

#全班共有幾人

classmates = len(math_pass | eng_pass)

print('全班共有',classmates,'人')






















