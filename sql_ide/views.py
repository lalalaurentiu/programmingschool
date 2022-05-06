from django.shortcuts import render, redirect
from django.views.generic import TemplateView
import sqlite3
from sql_ide.forms import SqlIdeForm

class SqlIde(TemplateView):
    template_name = "sql_ide/sql_ide.html"
    connect = sqlite3.connect("test.db",check_same_thread=False)
    cursor = connect.cursor()
    columns = []
    rows = []
    errors = []
    message = []
    
    def get(self, request):
        form = SqlIdeForm()
        context = {
            "form" : form,
            "columns": self.columns,
            "rows": self.rows,
            "errors":self.errors,
            "messages":self.message
            }
        return render(request, self.template_name, context)

    def post(self, request):
        form = SqlIdeForm(request.POST, )
        self.columns.clear()
        self.rows.clear()
        self.errors.clear()
        self.message.clear()

        if form.is_valid():
            inquiry = request.POST.get('interogare')

            if "create" in inquiry.lower():
                try:
                    self.cursor.execute(str(inquiry))
                    self.connect.commit()
                    column = self.cursor.description
                    table = inquiry.replace("(", "").split()
                    self.message.append(f"<b>Table {table[2]} created successfully</b>")
                except Exception as err:
                    self.errors.append(f"<div class='text-center' style='color:red'> <b>Type of error: {type(err).__name__}</b> <br> <b>Error: {str(err)}</b> <br> <b>Query failed: {str(inquiry)}</b></div>")

            elif "select" in inquiry.lower():
                try:
                    for rows in self.cursor.execute(str(inquiry)):
                        self.rows.append(rows)
                    self.connect.commit()
                    column = self.cursor.description
                    for c in column:
                        self.columns.append(c[0])
                except Exception as err:
                    self.errors.append(f"<div class='text-center' style='color:red'> <b>Type of error: {type(err).__name__}</b> <br> <b>Error: {str(err)}</b> <br> <b>Query failed: {str(inquiry)}</b> </div>")

            elif "insert" or "update" or "delete" in inquiry.lower():
                try:
                    self.cursor.execute(str(inquiry))
                    self.connect.commit()
                    column = self.cursor.description
                    method = inquiry.split()
                    self.message.append(f"<b>{method[0]} successfully</b>")
                except Exception as err:
                    self.errors.append(f"<div class='text-center' style='color:red'> <b>Type of error: {type(err).__name__}</b> <br> <b>Error: {str(err)}</b> <br> <b>Query failed: {str(inquiry)}</b></div>")
            else:
                try:
                    self.cursor.execute(str(inquiry))
                    self.connect.commit()
                    method = inquiry.split()
                    self.message.append(f"<b>{method[0]} successfully</b>")
                except Exception as err:
                    self.errors.append(f"<div class='text-center' style='color:red'> <b>Type of error: {type(err).__name__}</b> <br> <b>Error: {str(err)}</b> <br> <b>Query failed: {str(inquiry)}</b></div>")

            
        return redirect('sql_ide:sql_ide')
        