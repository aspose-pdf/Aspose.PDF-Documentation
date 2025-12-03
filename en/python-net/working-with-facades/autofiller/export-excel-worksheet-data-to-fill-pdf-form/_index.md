---
title: Export Excel data to fill PDF form
type: docs
weight: 10
url: /python-net/export-excel-worksheet-data-to-fill-pdf-form/
description: This section explains how you can export Excel worksheet data to fill PDF form using AutoFiller Class.
lastmod: "2025-11-05"
---

{{% alert color="primary" %}}

[Aspose.Pdf.Facades namespace](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/) in [Aspose.PDF for Python via .NET](/pdf/python-net/) offers various ways to fill the Pdf forms. You can import data from XML file, DFD, XFDF, use API and even can use the data from Excel worksheet.

{{% /alert %}}

## Implementation details

Fill interactive PDF form fields using data extracted from an Excel worksheet. You can export cell ranges directly into a DataTable, and then pass that table into Aspose.PDF for Python via .NET using the AutoFiller facade.

It makes it possible to automatically generate filled PDF forms for every row of Excel data—perfect for generating certificates, reports, ID cards, invoices, registration documents, or any scenario where structured form filling is required.

This approach automates large-scale form filling with minimal code and ensures accurate field mapping as long as the column names match the PDF form’s field names.

In the following scenario we are going to using a PDF form, which contains three form fields named ID, Name and Gender.

![todo:image_alt_text](export-excel-worksheet-data-to-fill-pdf-form_1.png)

In the Form specified above has one page, with three fields named as "ID", "Name" and "Gender" consequently. We would be extracting the data from the following excel sheet into DataTable object.

![todo:image_alt_text](export-excel-worksheet-data-to-fill-pdf-form_2.png)

Our code snippet shows how to export data from an Excel worksheet into a PDF form using Aspose.PDF for Python via .NET. The workflow extracts tabular data from an Excel file, converts it into a DataTable, and then uses the [AutoFiller](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/autofiller/) class to populate fields in a PDF form. This approach automates data transfer between spreadsheets and interactive PDF forms, ensuring consistency and reducing manual input.

|![todo:image_alt_text](export-excel-worksheet-data-to-fill-pdf-form_3.png)|![todo:image_alt_text](export-excel-worksheet-data-to-fill-pdf-form_4.png)|
| :- | :- |
|![todo:image_alt_text](export-excel-worksheet-data-to-fill-pdf-form_5.png)|![todo:image_alt_text](export-excel-worksheet-data-to-fill-pdf-form_6.png)|

1. Load the Excel workbook.
1. Access the worksheet.
1. Export worksheet data to a DataTable.
1. Initialize [AutoFiller](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/autofiller/).
1. Set input and output PDF files.
1. Import DataTable into PDF form fields.
1. Save the updated PDF.

```python

import os
import clr

# Add references (adjust paths if needed)
clr.AddReference("Aspose.Cells")
clr.AddReference("Aspose.PDF")

def export_excel_to_pdf_form():
    # Path to documents
    data_dir = "/path/to/documents/"   # <- update this

    # Load Excel workbook
    workbook = cells.Workbook(os.path.join(data_dir, "newBook1.xls"))

    # Access first worksheet
    worksheet = workbook.get_Worksheets().get_Item(0)

    # Export full sheet range to a DataTable
    dt = worksheet.get_Cells().ExportDataTable(
        0, 0,
        worksheet.get_Cells().get_MaxRow() + 1,
        worksheet.get_Cells().get_MaxColumn() + 1,
        True
    )
    # Create AutoFiller object
    auto_filler = pdf_facades.AutoFiller()

    # Input PDF form
    auto_filler.set_InputFileName(os.path.join(data_dir, "DataTableExample.pdf"))

    # Output PDF
    auto_filler.set_OutputFileName(os.path.join(data_dir, "DataTableExample_out.pdf"))

    # Import DataTable into PDF form fields
    auto_filler.ImportDataTable(dt)

    # Save PDF
    auto_filler.Save()

    print("PDF form successfully filled from Excel data.")
```

For filling from XLSX please use next code snippet:

```python

import os
import clr

# Add references (adjust paths if needed)
clr.AddReference("Aspose.PDF")

import Aspose.Pdf.Facades as pdf_facades

def fill_from_xlsx():
    # Path to documents directory
    data_dir = "/path/to/documents/"   # <- update this to your actual path

    # Create AutoFiller object
    auto_filler = pdf_facades.AutoFiller()

    # Bind PDF document
    auto_filler.BindPdf(os.path.join(data_dir, "Sample-Form-01.pdf"))

    # Generate a DataTable (replace with your own implementation)
    data_table = generate_data_table()

    # Import DataTable into PDF form fields
    auto_filler.ImportDataTable(data_table)

    # Save updated PDF
    auto_filler.Save(os.path.join(data_dir, "Sample-Form-01_out.pdf"))

    print("PDF form successfully filled from Excel data.")
```

Aspose.PDF for Python via .NET allows you to generate Data Table in PDF document:

```python

import clr
import System
from System import Random
from System.Data import DataTable, DataColumn

def generate_data_table():
    # Sample names
    names = ["Olivia", "Oliver", "Amelia", "George", "Isla", "Harry", "Ava", "Noah"]

    # Create a new DataTable
    table = DataTable("Students")

    # Create ID column
    id_column = DataColumn()
    id_column.DataType = System.Type.GetType("System.Int32")
    id_column.ColumnName = "id"
    id_column.ReadOnly = True
    id_column.Unique = True
    table.Columns.Add(id_column)

    # Create First Name column
    name_column = DataColumn()
    name_column.DataType = System.Type.GetType("System.String")
    name_column.ColumnName = "First Name"
    name_column.AutoIncrement = False
    name_column.Caption = "First Name"
    name_column.ReadOnly = False
    name_column
```

## Conclusion

{{% alert color="primary" %}}
[Aspose.Pdf.Facades](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades) also offers the capability to fill PDF form using data from database but this feature is currently supported in Python version.
{{% /alert %}}
