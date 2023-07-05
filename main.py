from tkinter import *
from tkinter import ttk
import mysql.connector
from tkinter import messagebox
import datetime
import tkinter
from tkinter import StringVar






class LibraryManagementSysyem:
    def __init__(self, root):
        self.root = root
        self.root.title("Library Management System")
        self.root.geometry("1550x800+0+0")



        # ==============================================variable=========================================

        self.member_Var = StringVar()
        self.prn_Var = StringVar()
        self.id_Var = StringVar()
        self.firstname_Var = StringVar()
        self.lastname_Var = StringVar()
        self.address1_Var = StringVar()
        self.address2_Var = StringVar()
        self.postcode_Var = StringVar()
        self.mobile_Var = StringVar()
        self.bookid_Var = StringVar()
        self.booktitle_Var = StringVar()
        self.author_Var = StringVar()
        self.dateborrowed_Var = StringVar()
        self.datedue_Var = StringVar()
        self.days_Var = StringVar()
        self.daysonbook_Var = StringVar()
        self.latereturnfine_Var = StringVar()
        self.dateoverdue_Var = StringVar()
        self.dateoverdue_Var = StringVar()
        self.finalprice_Var = StringVar()

        lbltitle = Label(self.root, text="LIBRARY MANAGEMENT SYSTEM", bg="powder blue", fg="darkred", bd=20,
                         relief="ridge", font=("times new roman", 50, "bold"), padx=2, pady=6)
        lbltitle.pack(side="top", fill="x")

        frame = Frame(self.root, bd=12, relief=RIDGE, padx=20, bg="powder blue")
        frame.place(x=0, y=130, width=1530, height=400)
        # ==================================================DataFreameLeft===============================================================

        DataframeLeft = LabelFrame(frame, text="Library membrship information", bg="powder blue", fg="black", bd=12,
                                   relief="ridge", font=("times new roman", 12, "bold"))
        DataframeLeft.place(x=0, y=5, width=900, height=350)
        lblMember = Label(DataframeLeft, bg="powder blue", text="Member Type:", font=("times new roman", 15, "bold"),padx=2, pady=6)
        lblMember.grid(row=0, column=0, sticky=W)

        comMember = ttk.Combobox(DataframeLeft, values=self.member_Var, state="readonly",font=('arial', 12, 'bold'))
        comMember = ttk.Combobox(DataframeLeft, state="readonly", font=("arial", 12, "bold"), width=27)
        comMember["value"] = ("Admin Staf", "Student", "Lecturer")
        comMember.grid(row=0, column=1)

        lblPRN_Number = Label(DataframeLeft, bg="powder blue", text="PRN Number:", font=("arial", 12, "bold"),padx=2, pady=4)
        lblPRN_Number.grid(row=1, column=0, sticky=W)
        txtPRN_number = Entry(DataframeLeft, font=("arial", 13, "bold"), textvariable=self.prn_Var, width=29)
        txtPRN_number.grid(row=2, column=1)

        lbltitle = Label(DataframeLeft, font=("arial", 12, "bold"), text="ID Number:", padx=2, pady=4, bg="powder blue")
        lbltitle.grid(row=2, column=0, sticky=W)
        txtPRN_number = Entry(DataframeLeft, font=("arial", 13, "bold"), textvariable=self.id_Var, width=29)
        txtPRN_number.grid(row=2, column=1)

        lblFirstName = Label(DataframeLeft, font=("arial", 12, "bold"), text="FirstName:", padx=2, pady=4,bg="powder blue")
        lblFirstName.grid(row=3, column=0, sticky=W)
        txtlblFirstName = Entry(DataframeLeft, font=("arial", 13, "bold"), textvariable=self.firstname_Var, width=29)
        txtlblFirstName.grid(row=3, column=1)

        lblLastName = Label(DataframeLeft, font=("arial", 12, "bold"), text="Last Name:", padx=2, pady=6,bg="powder blue")
        lblLastName.grid(row=4, column=0, sticky=W)
        txtlblLastName = Entry(DataframeLeft, font=("arial", 13, "bold"), textvariable=self.lastname_Var, width=29)
        txtlblLastName.grid(row=4, column=1)

        lblAddress1 = Label(DataframeLeft, font=("arial", 12, "bold"), text="Address1:", padx=2, pady=4,bg="powder blue")
        lblAddress1.grid(row=5, column=0, sticky=W)
        txtlblAddress1 = Entry(DataframeLeft, font=("arial", 13, "bold"), textvariable=self.address1_Var, width=29)
        txtlblAddress1.grid(row=5, column=1)

        lblAddress2 = Label(DataframeLeft, font=("arial", 12, "bold"), text="Address2:", padx=2, pady=4,bg="powder blue")
        lblAddress2.grid(row=6, column=0, sticky=W)
        txtlblAddress2 = Entry(DataframeLeft, font=("arial", 13, "bold"), textvariable=self.address2_Var, width=29)
        txtlblAddress2.grid(row=6, column=1)

        lblPostCode = Label(DataframeLeft, font=("arial", 12, "bold"), text="Post Code:", padx=2, pady=4,bg="powder blue")
        lblPostCode.grid(row=7, column=0, sticky=W)
        txtPostCode = Entry(DataframeLeft, font=("arial", 13, "bold"), textvariable=self.postcode_Var, width=29)
        txtPostCode.grid(row=7, column=1)

        lblMobile = Label(DataframeLeft, font=("arial", 12, "bold"), text="Mobile:", padx=2, pady=4, bg="powder blue")
        lblMobile.grid(row=8, column=0, sticky=W)
        txtMobile = Entry(DataframeLeft, font=("arial", 13, "bold"), textvariable=self.mobile_Var, width=29)
        txtMobile.grid(row=8, column=1)

        lblBookID = Label(DataframeLeft, font=("arial", 12, "bold"), text="BookID:", padx=2, bg="powder blue")
        lblBookID.grid(row=0, column=2, sticky=W)
        txtBookID = Entry(DataframeLeft, font=("arial", 12, "bold"), textvariable=self.bookid_Var, width=29)
        txtBookID.grid(row=0, column=3)

        lblBookTitle = Label(DataframeLeft, font=("arial", 12, "bold"), text="BookTitle:", padx=2, pady=6,bg="powder blue")
        lblBookTitle.grid(row=1, column=2, sticky=W)
        txtBookTitle = Entry(DataframeLeft, font=("arial", 12, "bold"), textvariable=self.booktitle_Var, width=29)
        txtBookTitle.grid(row=1, column=3)

        lblAuther = Label(DataframeLeft, font=("arial", 12, "bold"), text="Auther Name:", padx=2, pady=6,bg="powder blue")
        lblAuther.grid(row=2, column=2, sticky=W)
        txtAuther = Entry(DataframeLeft, font=("arial", 12, "bold"), textvariable=self.author_Var, width=29)
        txtAuther.grid(row=2, column=3)

        lblDateBorrowed = Label(DataframeLeft, font=("arial", 12, "bold"), text="DateBorrowed:", padx=2, pady=6,bg="powder blue")
        lblDateBorrowed.grid(row=3, column=2, sticky=W)
        txtDateBorrowed = Entry(DataframeLeft, font=("arial", 12, "bold"), textvariable=self.dateborrowed_Var, width=29)
        txtDateBorrowed.grid(row=3, column=3)

        lblDateDue = Label(DataframeLeft, font=("arial", 12, "bold"), text="Date Due:", padx=2, pady=6,bg="powder blue")
        lblDateDue.grid(row=4, column=2, sticky=W)
        txtDateDue = Entry(DataframeLeft, font=("arial", 12, "bold"), textvariable=self.datedue_Var, width=29)
        txtDateDue.grid(row=4, column=3)

        lblDaysOnBook = Label(DataframeLeft, font=("arial", 12, "bold"), text="Days On Book:", padx=2, pady=6,bg="powder blue")
        lblDaysOnBook.grid(row=5, column=2, sticky=W)
        txtDaysOnBook = Entry(DataframeLeft, font=("arial", 12, "bold"), textvariable=self.daysonbook_Var, width=29)
        txtDaysOnBook.grid(row=5, column=3)

        lblLateReturnFine = Label(DataframeLeft, font=("arial", 12, "bold"), text="Late Return Fine:", padx=2, pady=6,bg="powder blue")
        lblLateReturnFine.grid(row=6, column=2, sticky=W)
        txtLateReturnFine = Entry(DataframeLeft, font=("arial", 12, "bold"), textvariable=self.latereturnfine_Var,width=29)
        txtLateReturnFine.grid(row=6, column=3)

        lblDateOverdata = Label(DataframeLeft, font=("arial", 12, "bold"), text="Date Over Data:", padx=2, pady=6,bg="powder blue")
        lblDateOverdata.grid(row=7, column=2, sticky=W)
        txtDateOverdata = Entry(DataframeLeft, font=("arial", 12, "bold"), textvariable=self.dateoverdue_Var, width=29)
        txtDateOverdata.grid(row=7, column=3)

        lblActualPrice = Label(DataframeLeft, font=("arial", 12, "bold"), text="Actual Price:", padx=2, pady=6,bg="powder blue")
        lblActualPrice.grid(row=8, column=2, sticky=W)
        txtActualPrice = Entry(DataframeLeft, font=("arial", 12, "bold"), textvariable=self.finalprice_Var, width=29)
        txtActualPrice.grid(row=8, column=3)

        txtPRN_Number = Entry(DataframeLeft, font=("times new roman", 15, "bold"))
        txtPRN_Number.grid(row=1, column=1)
        DataframeRight = LabelFrame(frame, text="Book Detailse", bg="powder blue", fg="green", bd=12, relief="ridge",font=("times new roman", 12, "bold"))
        DataframeRight.place(x=910, width=540, height=350)

        # ==================================================DataFreameRight===============================================================

        DataframeRight = LabelFrame(frame, bd=12, padx=20, relief=RIDGE, bg="powder blue", font=("arial", 12, "bold"),text="Book Details")
        DataframeRight.place(x=870, y=5, width=500, height=350)

        self.txtBox = Text(DataframeRight, font=("arial", 12, "bold"), width=32, height=16, padx=2, pady=6)
        self.txtBox.grid(row=0, column=2)

        listScrollbar = Scrollbar(DataframeRight)
        listScrollbar.grid(row=0, column=1, sticky="ns")

        listBooks = [
            'Rich Dad Poor Dad',
            'The 48 Laws of Power',
            'Atomic Habits',
            'The Subtle Art of Not Giving a F*ck',
            'Meditations',
            'Marcus Aurelius - Meditations',
            'The Art of War',
            'The Daily Stoic Journal',
            'The Way, the Enemy, and the Key',
            'The Daily Dad'
        ]

        def SelectBook(even=""):
            value = str(listBox.get(listBox.curselection()))
            x = value
            if x == "Rich Dad Poor Dad":
                self.bookid_Var.set("RDPD1562")
                self.booktitle_Var.set("Rich Dad Poor Dad")
                self.author_Var.set("Robert Kiyosaki and Sharon Lechter")

                d1 = datetime.datetime.today()
                d2 = datetime.timedelta(days=15)
                d3 = d1 + d2
                self.dateborrowed_Var.set(d1)
                self.datedue_Var.set(d3)
                self.days_Var.set(15)
                self.latereturnfine_Var.set("5$")
                self.dateoverdue_Var.set("No")
                self.finalprice_Var.set("20$")

            elif x == "The 48 Laws of Power":
                self.bookid_Var.set("T4LOP8495")
                self.booktitle_Var.set("The 48 Laws of Power")
                self.author_Var.set("Robert Greene")

                d1 = datetime.datetime.today()
                d2 = datetime.timedelta(days=15)
                d3 = d1 + d2
                self.dateborrowed_Var.set(d1)
                self.datedue_Var.set(d3)
                self.days_Var.set(15)
                self.latereturnfine_Var.set("7$")
                self.dateoverdue_Var.set("No")
                self.finalprice_Var.set("25$")

            elif x == "Atomic Habits":
                self.bookid_Var.set("AHJC8794")
                self.booktitle_Var.set("Atomic Habits")
                self.author_Var.set("James Clear")

                d1 = datetime.datetime.today()
                d2 = datetime.timedelta(days=15)
                d3 = d1 + d2
                self.dateborrowed_Var.set(d1)
                self.datedue_Var.set(d3)
                self.days_Var.set(15)
                self.latereturnfine_Var.set("4$")
                self.dateoverdue_Var.set("No")
                self.finalprice_Var.set("18$")

            elif x == "The Subtle Art of Not Giving a F*ck":
                self.bookid_Var.set("TSAON1654")
                self.booktitle_Var.set("The Subtle Art of Not Giving a F*ck")
                self.author_Var.set("Mark Manson")

                d1 = datetime.datetime.today()
                d2 = datetime.timedelta(days=15)
                d3 = d1 + d2
                self.dateborrowed_Var.set(d1)
                self.datedue_Var.set(d3)
                self.days_Var.set(15)
                self.latereturnfine_Var.set("2$")
                self.dateoverdue_Var.set("No")
                self.finalprice_Var.set("14$")

            elif x == "Meditations":
                self.bookid_Var.set("M1325")
                self.booktitle_Var.set("Meditations")
                self.author_Var.set("Marcus Aurelius")

                d1 = datetime.datetime.today()
                d2 = datetime.timedelta(days=15)
                d3 = d1 + d2
                self.dateborrowed_Var.set(d1)
                self.datedue_Var.set(d3)
                self.days_Var.set(15)
                self.latereturnfine_Var.set("4$")
                self.dateoverdue_Var.set("No")
                self.finalprice_Var.set("14$")

            elif x == "Marcus Aurelius - Meditations":
                self.bookid_Var.set("MAM785")
                self.booktitle_Var.set("Marcus Aurelius - Meditations")
                self.author_Var.set("Marcus Aurelius")

                d1 = datetime.datetime.today()
                d2 = datetime.timedelta(days=15)
                d3 = d1 + d2
                self.dateborrowed_Var.set(d1)
                self.datedue_Var.set(d3)
                self.days_Var.set(15)
                self.latereturnfine_Var.set("7$")
                self.dateoverdue_Var.set("No")
                self.finalprice_Var.set("16$")

            elif x == "The Art of War":
                self.bookid_Var.set("TAOW2163")
                self.booktitle_Var.set("The Art of War")
                self.author_Var.set("Sun Tzu")

                d1 = datetime.datetime.today()
                d2 = datetime.timedelta(days=15)
                d3 = d1 + d2
                self.dateborrowed_Var.set(d1)
                self.datedue_Var.set(d3)
                self.days_Var.set(15)
                self.latereturnfine_Var.set("7$")
                self.dateoverdue_Var.set("No")
                self.finalprice_Var.set("26$")

            elif x == "The Daily Stoic Journal":
                self.bookid_Var.set("KJUY4787")
                self.booktitle_Var.set("The Daily Stoic Journal")
                self.author_Var.set("Ryan Holiday and Stephen Hanselman")

                d1 = datetime.datetime.today()
                d2 = datetime.timedelta(days=15)
                d3 = d1 + d2
                self.dateborrowed_Var.set(d1)
                self.datedue_Var.set(d3)
                self.days_Var.set(15)
                self.latereturnfine_Var.set("4$")
                self.dateoverdue_Var.set("No")
                self.finalprice_Var.set("13$")

            elif x == "The Enemy":
                self.bookid_Var.set("TE2564")
                self.booktitle_Var.set("The Enemy")
                self.author_Var.set("Charlie Higsonr")

                d1 = datetime.datetime.today()
                d2 = datetime.timedelta(days=15)
                d3 = d1 + d2
                self.dateborrowed_Var.set(d1)
                self.datedue_Var.set(d3)
                self.days_Var.set(15)
                self.latereturnfine_Var.set("2$")
                self.dateoverdue_Var.set("No")
                self.finalprice_Var.set("7$")

            elif x == "The Daily Dad":
                self.bookid_Var.set("TDD3497")
                self.booktitle_Var.set("The Daily Dad")
                self.author_Var.set("Ryan Holiday")

                d1 = datetime.datetime.today()
                d2 = datetime.timedelta(days=15)
                d3 = d1 + d2
                self.dateborrowed_Var.set(d1)
                self.datedue_Var.set(d3)
                self.days_Var.set(15)
                self.latereturnfine_Var.set("7$")
                self.dateoverdue_Var.set("No")
                self.finalprice_Var.set("25$")

        listBox = Listbox(DataframeRight, font=("arial", 12, "bold"), width=20, height=16)
        listBox.bind("<<ListboxSelect>>", SelectBook)
        listBox.grid(row=0, column=0, padx=4)
        listScrollbar.config(command=listBox.yview)


        for item in listBooks:
            listBox.insert(END, item)


        # ==============================================================Buttons Frame===========================================================
        Framebutton = Frame(self.root, bd=12, relief=RIDGE, padx=20, bg="powder blue")
        Framebutton.place(x=0, y=530, width=1530, height=70)

        btnAddData = Button(Framebutton, command=self.add_data, text="Add Data", font=("arial", 12, "bold"), width=23,
                            bg="dimgrey", fg="white")
        btnAddData.grid(row=0, column=0)

        btnShowData = Button(Framebutton, command=self.show_data, text="Show Data", font=("arial", 12, "bold"),
                             width=23, bg="dimgrey", fg="white")
        btnShowData.grid(row=0, column=1)

        btnAddData = Button(Framebutton,command=self.update ,text="Update", font=("arial", 12, "bold"), width=23, bg="dimgrey", fg="white")
        btnAddData.grid(row=0, column=2)

        btnAddData = Button(Framebutton, command=self.delete,text="Delete", font=("arial", 12, "bold"), width=23, bg="dimgrey", fg="white")
        btnAddData.grid(row=0, column=3)

        btnAddData = Button(Framebutton, command=self,text="Reset", font=("arial", 12, "bold"), width=23, bg="dimgrey", fg="white")
        btnAddData.grid(row=0, column=4)

        btnAddData = Button(Framebutton, command=self.iExit ,text="Exit", font=("arial", 12, "bold"), width=23, bg="dimgrey", fg="white")
        btnAddData.grid(row=0, column=5)

        # ==============================================================Information Frame===========================================================
        FrameDetails = Frame(self.root, bd=12, relief=RIDGE, padx=20, bg="powder blue")
        FrameDetails.place(x=0, y=590, width=1530, height=210)

        Table_frame = Frame(FrameDetails, bd=6, relief=RIDGE, padx=20, bg="powder blue")
        Table_frame.place(x=0, y=2, width=1460, height=190)

        xscroll = ttk.Scrollbar(Table_frame, orient=HORIZONTAL)
        yscroll = ttk.Scrollbar(Table_frame, orient=VERTICAL)

        self.library_Table = ttk.Treeview(Table_frame,
                                          column=("memebertype", "prnno", "id", "firstname", "lastname", "address1",
                                                  "address2", "postid", "mobile", "bookid", "booktitle", "author",
                                                  "datedue", "days", "larereturnfine", "dateoverdue", "finalprice",
                                                  "dateborrowed"), xscrollcommand=xscroll.set,
                                          yscrollcommand=yscroll.set)
        xscroll.pack(side=BOTTOM, fill=X)
        yscroll.pack(side=RIGHT, fill=Y)

        xscroll.config(command=self.library_Table.xview)
        yscroll.config(command=self.library_Table.yview)

        self.library_Table.heading("memebertype", text="MemberType")
        self.library_Table.heading("prnno", text="PRNnumber.")
        self.library_Table.heading("id", text="ID")
        self.library_Table.heading("firstname", text="FirstName")
        self.library_Table.heading("lastname", text="LastName")
        self.library_Table.heading("address1", text="Address1")
        self.library_Table.heading("address2", text="Address2")
        self.library_Table.heading("postid", text="PostID")
        self.library_Table.heading("mobile", text="MobileNumber")
        self.library_Table.heading("bookid", text="BookID")
        self.library_Table.heading("booktitle", text="BookTitle")
        self.library_Table.heading("author", text="Author")
        self.library_Table.heading("dateborrowed", text="DateofBorrowed")
        self.library_Table.heading("datedue", text="DateDue")
        self.library_Table.heading("days", text="DaysONBook")
        self.library_Table.heading("larereturnfine", text="LateReturnFine")
        self.library_Table.heading("dateoverdue", text="DateOverDue")
        self.library_Table.heading("finalprice", text="FinalPrice")

        self.library_Table["show"] = "headings"
        self.library_Table.pack(fill=BOTH, expand=1)

        self.library_Table.column("memebertype", width=100)
        self.library_Table.column("prnno", width=100)
        self.library_Table.column("id", width=100)
        self.library_Table.column("firstname", width=100)
        self.library_Table.column("lastname", width=100)
        self.library_Table.column("address1", width=100)
        self.library_Table.column("address2", width=100)
        self.library_Table.column("postid", width=100)
        self.library_Table.column("mobile", width=100)
        self.library_Table.column("bookid", width=100)
        self.library_Table.column("booktitle", width=100)
        self.library_Table.column("author", width=100)
        self.library_Table.column("dateborrowed", width=100)
        self.library_Table.column("datedue", width=100)
        self.library_Table.column("days", width=100)
        self.library_Table.column("larereturnfine", width=100)
        self.library_Table.column("dateoverdue", width=100)
        self.library_Table.column("finalprice", width=100)

        self.fetch_data()
        self.library_Table.bind("<<ButtonRelease-1>>", self.get_cursor)

        btnAddData = Button(Framebutton, command=self.add_data, text="Add Data", font=("arial", 12, "bold"), width=23,
                            bg="dimgrey", fg="white")
        btnAddData.grid(row=0, column=0)

    def add_data(self):
        try:
            conn = mysql.connector.connect(host="localhost", user="root", password="Omar2002Hazem@#",
                                           database="lms")
            cursor = conn.cursor()

            insert_query = "INSERT INTO library (MemberType, PRN_Number, ID, FirstName, LastName, Address1, Address2, PostID, MobileNumber, BookID, BookTitle, Author, DateofBorrowed, DateDue, DaysONBook, LateReturnFine, DateOverDue, FinalPrice) VALUES (%s, %s, %s, %s, %s, %s, %s, %d, %d, %d, %s, %s, %s, %s, %s, %s, %s, %s)"
            record = (self.member_Var.get(), self.prn_Var.get(), self.id_Var.get(), self.firstname_Var.get(),
                      self.lastname_Var.get(), self.address1_Var.get(), self.address2_Var.get(), self.postcode_Var.get(),
                      self.mobile_Var.get(), self.bookid_Var.get(), self.booktitle_Var.get(), self.author_Var.get(),
                      self.dateborrowed_Var.get(), self.datedue_Var.get(), self.days_Var.get(), self.latereturnfine_Var.get(),
                      self.dateoverdue_Var.get(), self.finalprice_Var.get())

            cursor.execute(insert_query, record)
            conn.commit()

            self.reset()
            self.fetch_data()

            conn.close()
        except Exception as e:
            messagebox.showinfo("Success", "Member has been inserted successfully")



    def update(self):
        try:
            conn = mysql.connector.connect(host="localhost", user="root", password="Omar2002Hazem@#",
                                           database="lms")
            cursor = conn.cursor()

            update_query = "UPDATE library SET MemberType = %s, ID = %s, FirstName = %s, LastName = %s, Address1 = %s, Address2 = %s, PostID = %s, MobileNumber = %s, BookID = %s, BookTitle = %s, Author = %s, DateofBorrowed = %s, DateDue = %s, DaysONBook = %s, LateReturnFine = %s, DateOverDue = %s, FinalPrice = %s WHERE PRN_Number = %s"
            record = (self.member_Var.get(), self.id_Var.get(), self.firstname_Var.get(), self.lastname_Var.get(),
                      self.address1_Var.get(), self.address2_Var.get(), self.postcode_Var.get(), self.mobile_Var.get(),
                      self.bookid_Var.get(), self.booktitle_Var.get(), self.author_Var.get(), self.dateborrowed_Var.get(),
                      self.datedue_Var.get(), self.days_Var.get(), self.latereturnfine_Var.get(), self.dateoverdue_Var.get(),
                      self.finalprice_Var.get(), self.prn_Var.get())

            cursor.execute(update_query, record)
            conn.commit()

            self.reset()
            self.fetch_data()

            conn.close()
        except Exception as e:
            messagebox.showinfo("Success", "Member has been updated")

    def fetch_data(self):
        try:
            conn = mysql.connector.connect(host="localhost", user="root", password="Omar2002Hazem@#",
                                           database="lms")
            cursor = conn.cursor()

            select_query = "SELECT * FROM library"
            cursor.execute(select_query)
            rows = cursor.fetchall()

            if len(rows) != 0:
                self.library_Table.delete(*self.library_Table.get_children())
                for row in rows:
                    self.library_Table.insert("", END, values=row)

            conn.close()
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def get_cursor(self, event=""):
        cursor_row = self.library_Table.focus()
        content = self.library_Table.item(cursor_row)
        row = content['values']

        self.member_Var.set(row[0])
        self.prn_Var.set(row[1])
        self.id_Var.set(row[2])
        self.firstname_Var.set(row[3])
        self.lastname_Var.set(row[4])
        self.address1_Var.set(row[5])
        self.address2_Var.set(row[6])
        self.postcode_Var.set(row[7])
        self.mobile_Var.set(row[8])
        self.bookid_Var.set(row[9])
        self.booktitle_Var.set(row[10])
        self.author_Var.set(row[11])
        self.dateborrowed_Var.set(row[12])
        self.datedue_Var.set(row[13])
        self.days_Var.set(row[14])
        self.latereturnfine_Var.set(row[15])
        self.dateoverdue_Var.set(row[16])
        self.finalprice_Var.set(row[17])

    def show_data(self):
        self.txtBox.delete("1.0", END)
        self.txtBox.insert(END, "Member Type\t\t" + self.member_Var.get() + "\n")
        self.txtBox.insert(END, "PRN Number\t\t" + self.prn_Var.get() + "\n")
        self.txtBox.insert(END, "ID Number\t\t" + self.id_Var.get() + "\n")
        self.txtBox.insert(END, "First Name\t\t" + self.firstname_Var.get() + "\n")
        self.txtBox.insert(END, "Last Name\t\t" + self.lastname_Var.get() + "\n")
        self.txtBox.insert(END, "Address1\t\t" + self.address1_Var.get() + "\n")
        self.txtBox.insert(END, "Address2\t\t" + self.address2_Var.get() + "\n")
        self.txtBox.insert(END, "Post Code\t\t" + self.postcode_Var.get() + "\n")
        self.txtBox.insert(END, "Mobile\t\t" + self.mobile_Var.get() + "\n")
        self.txtBox.insert(END, "Book ID\t\t" + self.bookid_Var.get() + "\n")
        self.txtBox.insert(END, "Book Title\t\t" + self.booktitle_Var.get() + "\n")
        self.txtBox.insert(END, "Author:\t\t" + self.author_Var.get() + "\n")
        self.txtBox.insert(END, "Date Borrowed\t\t" + self.dateborrowed_Var.get() + "\n")
        self.txtBox.insert(END, "Date Due\t\t" + self.datedue_Var.get() + "\n")
        self.txtBox.insert(END, "Days On Book:\t\t" + self.days_Var.get() + "\n")
        self.txtBox.insert(END, "Late Return Fine\t\t" + self.latereturnfine_Var.get() + "\n")
        self.txtBox.insert(END, "Date Overdue:\t\t" + self.dateoverdue_Var.get() + "\n")
        self.txtBox.insert(END, "Final Price:\t\t" + self.finalprice_Var.get() + "\n")

    def reset(self):
        self.member_Var.set("")
        self.prn_Var.set("")
        self.id_Var.set("")
        self.firstname_Var.set("")
        self.lastname_Var.set("")
        self.address1_Var.set("")
        self.address2_Var.set("")
        self.postcode_Var.set("")
        self.mobile_Var.set("")
        self.bookid_Var.set("")
        self.booktitle_Var.set("")
        self.author_Var.set("")
        self.dateborrowed_Var.set("")
        self.datedue_Var.set("")
        self.days_Var.set("")
        self.postcode_Var.set("")
        self.dateoverdue_Var.set("")
        self.finalprice_Var.set("")

    def iExit(self):
        iExit = tkinter.messagebox.askyesno("Library management system", "Do you want to exit?")
        if iExit > 0:
            self.root.destroy()

    def delete(self):
        if self.prn_Var.get() == "" or self.id_Var.get() == "":
            messagebox.showerror("Error", "First select the Member")
        else:
            conn = mysql.connector.connect(host="localhost", username="root", password="Omar2002Hazem@#",
                                           database="lms")
            my_cursor = conn.cursor()
            query = "DELETE FROM library WHERE PRN_Number=%s"
            value = (self.prn_Var.get(),)
            my_cursor.execute(query, value)

            conn.commit()
            self.fetch_data()
            self.reset()
            conn.close()

            messagebox.showinfo("Success", "Member has been deleted")


if __name__ == "__main__":
    root = Tk()
    obj = LibraryManagementSysyem(root)
    root.mainloop()
