def runAction(self, event):
    IDS = self.getSibling('ID').props.text
	ID = IDS
	
	args = [ID]
	query = "SELECT PR_Title, Part_No, Part_Description, QYT, Expense_Booking, Section, Category, Category_ID, ID FROM indendinfo WHERE ID = ?"
	
	data = system.db.runPrepQuery(query, args)
	
	if data:
		self.getSibling('PR_Title').props.text = data[0]['PR_Title']
		self.getSibling('Part_No').props.text = data[0]['Part_No']
		self.getSibling('Part_Description').props.text = data[0]['Part_Description']
		self.getSibling('QYT').props.text = data[0]['QYT']
		self.getSibling('Expense_Booking').props.value = data[0]['Expense_Booking']
		self.getSibling('Section').props.value = data[0]['Section']
		self.getSibling('Category').props.value = data[0]['Category']
		self.getSibling('ID').props.value = data[0]['ID']
		self.getSibling('Category_ID').props.text = data[0]['Category_ID']
	
#		system.gui.messageBox('Data Successfully Retrieved')
	