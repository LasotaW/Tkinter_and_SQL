import tkinter as tk
import mysql.connector
import tkinter.ttk as ttk

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    database="sales"
)

def populate_results(searchContent):
    selectedDropBoxOption = drop.get()

    if selectedDropBoxOption == "Wyszukaj po...":
        msg = tk.Label(text="Wybierz kategorię!")
        msg.grid(row=5, column=8)
    if selectedDropBoxOption == "Row_ID":
        sql = f"SELECT * FROM sales_data WHERE Row_ID = '{searchContent}'"
    if selectedDropBoxOption == "Order_ID":
        sql = f"SELECT * FROM sales_data WHERE Order_ID = '{searchContent}'"
    if selectedDropBoxOption == "Order_Date":
        sql = f"SELECT * FROM sales_data WHERE Order_Date = '{searchContent}'"
    if selectedDropBoxOption == "Ship_Date":
        sql = f"SELECT * FROM sales_data WHERE Ship_Date = '{searchContent}'"
    if selectedDropBoxOption == "Ship_Mode":
        sql = f"SELECT * FROM sales_data WHERE Ship_Mode = '{searchContent}'"
    if selectedDropBoxOption == "Customer_ID":
        sql = f"SELECT * FROM sales_data WHERE Customer_ID = '{searchContent}'"
    if selectedDropBoxOption == "Customer_Name":
        sql = f"SELECT * FROM sales_data WHERE Customer_Name = '{searchContent}'"
    if selectedDropBoxOption == "Segment":
        sql = f"SELECT * FROM sales_data WHERE Segment ='{searchContent}'"
    if selectedDropBoxOption == "Country":
        sql = f"SELECT * FROM sales_data WHERE Country ='{searchContent}''"
    if selectedDropBoxOption == "City":
        sql = f"SELECT * FROM sales_data WHERE City = '{searchContent}'"     
    if selectedDropBoxOption == "State":
        sql = f"SELECT * FROM sales_data WHERE State = '{searchContent}'"
    if selectedDropBoxOption == "Region":
        sql = f"SELECT * FROM sales_data WHERE Region = '{searchContent}'"
    if selectedDropBoxOption == "Postal_Code":
        sql = f"SELECT * FROM sales_data WHERE Postal_Code = '{searchContent}'"
    if selectedDropBoxOption == "Product_ID":
        sql = f"SELECT * FROM sales_data WHERE Product_ID = '{searchContent}'"
    if selectedDropBoxOption == "Category":
        sql = f"SELECT * FROM sales_data WHERE Category = '{searchContent}'"
    if selectedDropBoxOption == "Sub_Category":
        sql = f"SELECT * FROM sales_data WHERE Sub_Category = '{searchContent}'"
    if selectedDropBoxOption == "Product_Name":
        sql = f"SELECT * FROM sales_data WHERE Product_Name = '{searchContent}'"
    if selectedDropBoxOption == "Sales":
        sql = f"SELECT * FROM sales_data WHERE Sales = '{searchContent}'"
    if selectedDropBoxOption == "Quantity":
        sql = f"SELECT * FROM sales_data WHERE Quantity = '{searchContent}'"
    if selectedDropBoxOption == "Discount":
        sql = f"SELECT * FROM sales_data WHERE Discount = '{searchContent}'"
    if selectedDropBoxOption == "Profit":
        sql = f"SELECT * FROM sales_data WHERE Profit = '{searchContent}'"

    mycursor = mydb.cursor()
    mycursor.execute(sql)
    myresult = mycursor.fetchall()

    if not myresult:
        msg = tk.Label(text="Nie znaleziono wyników!")
        msg.grid(row=5, column=8)
    else:
        i = 6
        for x in myresult:
            result_label = tk.Label(master=root, text=x)
            result_label.grid(row=i, column=0, columnspan=10)
            i += 1

def get_results():
    searchContent = usrSearch.get()
    populate_results(searchContent)

root = tk.Tk()
root.title("Wyszukiwarka danych")
root.geometry("800x400")

usrSearch = tk.StringVar()
usrSearchLabel = tk.Label(root, text="Wprowadź dane", font=("bold", 15), padx=10)
usrSearchLabel.grid(row=2, column=0)

usrEntry = tk.Entry(root, textvariable=usrSearch)
usrEntry.grid(row=2, column=2)

searchButton = tk.Button(root, text="Szukaj", width=10, command=get_results)
searchButton.grid(row=3, column=0)

dropboxContent = ["Wyszukaj po...", "Row_ID", "Order_ID", "Order_Date", "Ship_Date", 
                    "Ship_Mode", "Customer_ID", "Customer_Name", "Segment", "Country", 
                    "City", "State", "Region", "Postal_Code", "Product_ID", 
                    "Category", "Sub_Category", "Product_Name", "Sales", 
                    "Quantity", "Discount", "Profit"]
drop = ttk.Combobox(value=dropboxContent)
drop.current(0)
drop.grid(row=2, column=7)

root.mainloop()