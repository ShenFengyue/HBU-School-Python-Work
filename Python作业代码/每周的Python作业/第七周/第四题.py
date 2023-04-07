#这是第四题
 
#获取四大件 （感谢百度翻译）
principal = float(input("请输入贷款本金："))
months = int(input("请输入分期月数："))
method = input("请输入还款方式（ACPI或AC）：")
rate = float(input("请输入月利率："))
 
#不同方式不同输出
if method == "ACPI": 
  payment = principal * rate * (1 + rate) ** months / ((1 + rate) ** months - 1)
  payment = round(payment, 2)
  print("每月还款额为:",payment)
  
elif method == "AC":
  principal_per_month = principal / months 
  payments = [] 
  for i in range(months):  
    paid_principal = principal_per_month * i  
    payment = principal_per_month + (principal - paid_principal) * rate
    payments.append(round(payment, 2))
  print(",".join(str(x) for x in payments))
 
 
  #提示错误
else:
  print("还款方式输入错误")
