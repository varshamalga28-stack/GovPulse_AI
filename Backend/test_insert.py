from database import save_complaint

data = {
    "complaint": "Water supply issue in Hyderabad",
    "customer_name": "Varsha",
    "email": "varsha@gmail.com",
    "phone": "9876543210"
}

result = save_complaint(data)
print(result)