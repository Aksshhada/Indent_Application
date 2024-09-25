def runAction(self, event):
    PR_Title = self.getSibling('PR_Title').props.text
	Part_No = self.getSibling('Part_No').props.text
	Part_Description = self.getSibling('Part_Description').props.text
	QYT = self.getSibling('QYT').props.text
	Expense_Booking = self.getSibling('Expense_Booking').props.value
	Section = self.getSibling('Section').props.value
	Category = self.getSibling('Category').props.value
	ID = self.getSibling('ID').props.text
	Category_ID = self.getSibling('Category_ID').props.text
	Category_ID = Category + ID
	query = "INSERT INTO indendinfo (PR_Title, Part_No, Part_Description, QYT, Expense_Booking, Section, Category, Category_ID) VALUES (?,?,?,?,?,?,?,?)"
	args = [PR_Title, Part_No, Part_Description, QYT, Expense_Booking, Section, Category, Category_ID]
	system.db.runPrepUpdate(query, args)
	#**********************************************************************************************************
	query = "SELECT * FROM indendinfo"
	returnedData = system.db.runQuery(query, "SQLserver")
	self.getSibling("Table").props.data = returnedData