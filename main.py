import tkinter as tk
import mysql.connector
import tkinter.ttk as ttk
from tkinter import messagebox

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    database="sales"
)

def addWindow():
    def submit():
        inputs = {
            'rowID': rowID.get(),
            'orderID': orderID.get(),
            'orderDate': orderDate.get(),
            'shipDate': shipDate.get(),
            'shipMode': shipMode.get(),
            'customerID': customerID.get(),
            'cusName': cusName.get(),
            'segment': segment.get(),
            'country': country.get(),
            'city': city.get(),
            'state': state.get(),
            'region': region.get(),
            'postal': postal.get(),
            'productID': productID.get(),
            'category': category.get(),
            'subCat': subCat.get(),
            'product': product.get(),
            'sales': sales.get(),
            'quantity': quantity.get(),
            'discount': discount.get(),
            'profit': profit.get()
        }

        x = f"INSERT INTO sales_data VALUES({inputs['rowID']}, {inputs['orderID']}, {inputs['orderDate']}, {inputs['shipDate']}, {inputs['shipMode']}, {inputs['customerID']}, {inputs['cusName']}, {inputs['segment']}, {inputs['country']}, {inputs['city']}, {inputs['state']}, {inputs['region']}, {inputs['postal']}, {inputs['productID']}, {inputs['category']}, {inputs['subCat']}, {inputs['product']}, {inputs['sales']}, {inputs['quantity']}, {inputs['discount']}, {inputs['profit']})"
        try:
            mycursor = mydb.cursor()
            mycursor.execute(x)
            mydb.commit()
        except:
            messagebox.showwarning("Błąd!", "Nie wypełniono wszystkich pól lub podany rekord nie istnieje!")

        rowID.delete(0, tk.END)
        orderID.delete(0, tk.END)
        orderDate.delete(0, tk.END)
        shipDate.delete(0, tk.END)
        shipMode.delete(0, tk.END)
        customerID.delete(0, tk.END)
        cusName.delete(0, tk.END)
        segment.delete(0, tk.END)
        country.delete(0, tk.END)
        city.delete(0, tk.END)
        state.delete(0, tk.END)
        region.delete(0, tk.END)
        postal.delete(0, tk.END)
        productID.delete(0, tk.END)
        category.delete(0, tk.END)
        subCat.delete(0, tk.END)
        product.delete(0, tk.END)
        sales.delete(0, tk.END)
        quantity.delete(0, tk.END)
        discount.delete(0, tk.END)
        profit.delete(0, tk.END)

    win = tk.Tk()
    win.title("Dodaj nowy rekord")
    win.geometry("300x500")

    rowIDlabel = tk.Label(win, text="Row_ID")
    rowIDlabel.grid(row=5, column=0)
    rowID = tk.Entry(win)
    rowID.grid(row=5, column=2)

    orderIDlabel = tk.Label(win, text="Order_ID")
    orderIDlabel.grid(row=6, column=0)
    orderID = tk.Entry(win)
    orderID.grid(row=6, column=2)

    orderDatelabel = tk.Label(win, text="Order_Date")
    orderDatelabel.grid(row=7, column=0)
    orderDate = tk.Entry(win)
    orderDate.grid(row=7, column=2)

    shipDatelabel = tk.Label(win, text="Ship_Date")
    shipDatelabel.grid(row=8, column=0)
    shipDate = tk.Entry(win)
    shipDate.grid(row=8, column=2)

    shipModelabel = tk.Label(win, text="Ship_Mode")
    shipModelabel.grid(row=9, column=0)
    shipMode = tk.Entry(win)
    shipMode.grid(row=9, column=2)

    customerIDlabel = tk.Label(win, text="Customer_ID")
    customerIDlabel.grid(row=10, column=0)
    customerID = tk.Entry(win)
    customerID.grid(row=10, column=2)

    cusNamelabel = tk.Label(win, text="Customer_Name")
    cusNamelabel.grid(row=11, column=0)
    cusName = tk.Entry(win)
    cusName.grid(row=11, column=2)

    segmentLabel = tk.Label(win, text="Segment")
    segmentLabel.grid(row=12, column=0)
    segment = tk.Entry(win)
    segment.grid(row=12, column=2)

    countryLabel = tk.Label(win, text="Country")
    countryLabel.grid(row=13, column=0)
    country = tk.Entry(win)
    country.grid(row=13, column=2)

    cityLabel = tk.Label(win, text="City")
    cityLabel.grid(row=14, column=0)
    city = tk.Entry(win)
    city.grid(row=14, column=2)

    stateLabel = tk.Label(win, text="State")
    stateLabel.grid(row=15, column=0)
    state = tk.Entry(win)
    state.grid(row=15, column=2)

    regionLabel = tk.Label(win, text="Region")
    regionLabel.grid(row=16, column=0)
    region = tk.Entry(win)
    region.grid(row=16, column=2)

    postalLabel = tk.Label(win, text="Postal_Code")
    postalLabel.grid(row=17, column=0)
    postal = tk.Entry(win)
    postal.grid(row=17, column=2)

    productIDlabel = tk.Label(win, text="Product_ID")
    productIDlabel.grid(row=18, column=0)
    productID = tk.Entry(win)
    productID.grid(row=18, column=2)

    categoryLabel = tk.Label(win, text="Category")
    categoryLabel.grid(row=19, column=0)
    category = tk.Entry(win)
    category.grid(row=19, column=2)

    subCatLabel = tk.Label(win, text="Sub_Category")
    subCatLabel.grid(row=20, column=0)
    subCat = tk.Entry(win)
    subCat.grid(row=20, column=2)

    productLabel = tk.Label(win, text="Product_Name")
    productLabel.grid(row=21, column=0)
    product = tk.Entry(win)
    product.grid(row=21, column=2)

    salesLabel = tk.Label(win, text="Sales")
    salesLabel.grid(row=22, column=0)
    sales = tk.Entry(win)
    sales.grid(row=22, column=2)

    quantityLabel = tk.Label(win, text="Quantity")
    quantityLabel.grid(row=23, column=0)
    quantity = tk.Entry(win)
    quantity.grid(row=23, column=2)

    discountLabel = tk.Label(win, text="Discount")
    discountLabel.grid(row=24, column=0)
    discount = tk.Entry(win)
    discount.grid(row=24, column=2)

    profitLabel = tk.Label(win, text="Profit")
    profitLabel.grid(row=25, column=0)
    profit = tk.Entry(win)
    profit.grid(row=25, column=2)

    addButton = tk.Button(win, text="Dodaj nowy", width=10, command=submit)
    addButton.grid(row=26, column=2)

def searchWindow():
    def populate_results(searchContent):
        selectedDropBoxOption = drop.get()

        if selectedDropBoxOption == "Wyszukaj po...":
            msg = tk.Label(win, text="Wybierz kategorię!", foreground="red", font=(15))
            msg.grid(row=5, column=5)
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
            sql = f"SELECT * FROM sales_data WHERE Country ='{searchContent}'"
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
            msg = tk.Label(win, text="Nie znaleziono wyników!")
            msg.grid(row=5, column=8)
        else:
            i = 6
            for x in myresult:
                for y in x:
                    result_label = tk.Label(win, text=y)
                    result_label.grid(row=i, column=2)
                    i += 1
             
        def deleteRecord():
            try:
                selectedDropBoxOption = drop.get()
                sql = f"DELETE FROM sales_data WHERE {selectedDropBoxOption}={searchContent}"
                mycursor = mydb.cursor()
                mycursor.execute(sql)
                mydb.commit()
                msg = tk.Label(win, text="Pomyślnie usunięto rekord!")
                msg.grid(row=i+3, column=0)
            except:
                msg = tk.Label(win, text="Nie udało się usunąć rekordu")
                msg.grid(row=i+3, column=0)

        deleteButton = tk.Button(win, text="Usuń", width=20, command=deleteRecord)
        deleteButton.grid(row=i+2, column=0)

    def get_results():
        searchContent = usrSearch.get()
        populate_results(searchContent)

    win = tk.Tk()
    win.title("Wyszukaj rekord")
    win.geometry("800x600")
    
    usrSearch = tk.StringVar(win)
    usrSearchLabel = tk.Label(win, text="Wprowadź dane", font=("bold", 15))
    usrSearchLabel.grid(row=2, column=0)

    usrEntry = tk.Entry(win, textvariable=usrSearch)
    usrEntry.grid(row=2, column=2)

    searchButton = tk.Button(win, text="Szukaj", width=10, command=get_results)
    searchButton.grid(row=2, column=8)

    dropboxContent = ["Wyszukaj po...", "Row_ID", "Order_ID", "Order_Date", "Ship_Date", 
                        "Ship_Mode", "Customer_ID", "Customer_Name", "Segment", "Country", 
                        "City", "State", "Region", "Postal_Code", "Product_ID", 
                        "Category", "Sub_Category", "Product_Name", "Sales", 
                        "Quantity", "Discount", "Profit"]

    drop = ttk.Combobox(win, value=dropboxContent)
    drop.current(0)
    drop.grid(row=2, column=5)

root = tk.Tk()
root.title("SQL editor by Wiktor Lasota v0.00001")
root.geometry("230x200")

usrSearchLabel = tk.Label(root, text="Menedżer bazy danych", font=("bold", 15), padx=10)
usrSearchLabel.grid(row=0, column=0)

addNew = tk.Button(root, text="Dodaj nowy rekord", command=addWindow)
addNew.grid(row=2, column=0)

searchBtn = tk.Button(root, text="Wyszukaj/Usuń", command=searchWindow)
searchBtn.grid(row=3, column=0)

root.mainloop()
