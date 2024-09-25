def runAction(self, event):
    table = self.getSibling('Table')
	selectedRow = table.props.selection.data[0]
	id =selectedRow['ID']
	self.getSibling('ID').props.value = id
	sql = "DELETE FROM indendinfo WHERE id = ?"
	args = [id]
	system.db.runPrepUpdate(sql, args)
	query = "SELECT * FROM indendinfo"
	returnedData = system.db.runQuery(query, "SQLserver")
	self.getSibling("Table").props.data = returnedData