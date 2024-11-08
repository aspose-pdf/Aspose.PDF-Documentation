---
title: Exportar datos de Excel para llenar formulario PDF
type: docs
weight: 10
url: /es/net/export-excel-worksheet-data-to-fill-pdf-form/
description: Esta sección explica cómo puedes exportar datos de la hoja de cálculo de Excel para llenar un formulario PDF usando la clase AutoFiller.
lastmod: "2021-06-05"
draft: false
---

{{% alert color="primary" %}}

[Espacio de nombres Aspose.Pdf.Facades](https://reference.aspose.com/pdf/net/aspose.pdf.facades) en [Aspose.PDF para .NET](/pdf/es/net/) ofrece varias formas de llenar los formularios PDF. Puedes importar datos desde un archivo XML, DFD, XFDF, usar API e incluso puedes usar los datos de la hoja de cálculo de Excel.
Utilizaremos el método [ExportDataTable](https://reference.aspose.com/cells/net/aspose.cells/range/methods/exportdatatable/index) de la clase [Cells](https://reference.aspose.com/pdf/net/aspose.pdf/cells) de [Aspose.Cells](https://docs.aspose.com//cells/net) para exportar los datos de la hoja de Excel a un objeto DataTable. Luego necesitamos importar estos datos en formato Pdf usando el método [ImportDataTable](https://reference.aspose.com/pdf/net/aspose.pdf.facades/autofiller/methods/importdatatable) de la clase [AutoFiller](https://reference.aspose.com/pdf/net/aspose.pdf.facades/autofiller). Asegúrate de que el nombre de la columna de DataTable sea el mismo que el nombre del campo en el formulario PDF.
{{% /alert %}}

## Detalles de Implementación

En el siguiente escenario vamos a utilizar un formulario PDF, que contiene tres campos de formulario llamados ID, Nombre y Género.

![todo:image_alt_text](export-excel-worksheet-data-to-fill-pdf-form_1.png)

En el formulario especificado arriba tiene una página, con tres campos llamados "ID", "Name" y "Gender" consecuentemente. Estaríamos extrayendo los datos de la siguiente hoja de Excel en el objeto DataTable.

![todo:image_alt_text](export-excel-worksheet-data-to-fill-pdf-form_2.png)

Necesitamos crear un objeto de la clase [AutoFiller](https://reference.aspose.com/pdf/net/aspose.pdf.facades/autofiller) y vincular el formulario Pdf presente en las imágenes de arriba y usar el método [ImportDataTable](https://reference.aspose.com/pdf/net/aspose.pdf.facades/autofiller/methods/importdatatable) para llenar los campos del formulario usando los datos presentes en el objeto DataTable.Una vez que se llama al método, se genera un nuevo archivo de formulario Pdf, que contiene cinco páginas con el formulario completado basado en los datos de la hoja de Excel. El formulario Pdf de entrada era de una sola página y el resultado es de cinco páginas, porque el número de filas de datos en la hoja de Excel es 5. La clase DataTable ofrece la capacidad de usar la primera fila de la hoja como ColumnName.

|**![todo:image_alt_text](export-excel-worksheet-data-to-fill-pdf-form_3.png)**|**![todo:image_alt_text](export-excel-worksheet-data-to-fill-pdf-form_4.png)**|
| :- | :- |
|![todo:image_alt_text](export-excel-worksheet-data-to-fill-pdf-form_5.png)|![todo:image_alt_text](export-excel-worksheet-data-to-fill-pdf-form_6.png)|

```csharp
Workbook workbook = new Workbook();
// Creando un flujo de archivo que contiene el archivo de Excel que se va a abrir
FileStream fstream = new FileStream("d:\\pdftest\\newBook1.xls", FileMode.Open);
// Abriendo el archivo de Excel a través del flujo de archivo
workbook.Open(fstream);
// Accediendo a la primera hoja de trabajo en el archivo de Excel
Worksheet worksheet = workbook.Worksheets[0];
// Exportando el contenido de 7 filas y 2 columnas comenzando desde la primera celda a DataTable
DataTable dataTable = worksheet.Cells.ExportDataTable(0, 0, worksheet.Cells.MaxRow + 1, worksheet.Cells.MaxColumn + 1, true);
// Cerrando el flujo de archivo para liberar todos los recursos
fstream.Close();
// Crear un objeto de la clase AutoFiller
AutoFiller autoFiller = new AutoFiller();
// El archivo pdf de entrada que contiene campos de formulario
autoFiller.InputFileName = "d:\\pdftest\\DataTableExample.pdf";
// El pdf resultante, que contendrá los campos del formulario llenos con información de DataTable
autoFiller.OutputFileName = "D:\\pdftest\\DataTableExample_Filled.pdf";
// Llamar al método para importar los datos del objeto DataTable en los campos del formulario Pdf.
autoFiller.ImportDataTable(dataTable);
// Llamar al método de guardar para generar el archivo pdf
autoFiller.Save();
```

Para completar desde XLSX, utilice el siguiente fragmento de código:

```csharp
internal static void FillFromXLSX()
        {
            // Crea un objeto de la clase AutoFiller
            AutoFiller autoFiller = new AutoFiller();
            // El archivo pdf de entrada que contiene campos de formulario
            autoFiller.BindPdf(@"C:\Samples\Facades\Autofiller\Sample-Form-01.pdf");

            DataTable dataTable = GenerateDataTable();

            // Llama al método para importar los datos del objeto DataTable en los campos de formulario del Pdf.
            autoFiller.ImportDataTable(dataTable);

            // El pdf resultante, que contendrá los campos de formulario llenos con información de DataTable
            autoFiller.Save(@"C:\Samples\Facades\Autofiller\Sample-Form-01_mod.pdf");

        }
```

Aspose.PDF para .NET te permite generar una Tabla de Datos en un documento PDF:

```csharp
private static DataTable GenerateDataTable()
        {
            string[] names = new[] { "Olivia", "Oliver", "Amelia", "George", "Isla", "Harry", "Ava", "Noah" };
            // Crea un nuevo DataTable.
            System.Data.DataTable table = new DataTable("Students");
            // Declara variables para los objetos DataColumn y DataRow.
            DataColumn column;
            DataRow row;

            // Crea un nuevo DataColumn, establece DataType,
            // ColumnName y añade al DataTable.
            column = new DataColumn
            {
                DataType = System.Type.GetType("System.Int32"),
                ColumnName = "id",
                ReadOnly = true,
                Unique = true
            };
            // Añade la columna al DataColumnCollection.
            table.Columns.Add(column);

            // Crea la segunda columna.
            column = new DataColumn
            {
                DataType = System.Type.GetType("System.String"),
                ColumnName = "First Name",
                AutoIncrement = false,
                Caption = "First Name",
                ReadOnly = false,
                Unique = false
            };
            // Añade la columna a la tabla.
            table.Columns.Add(column);

            // Haz de la columna ID la columna clave principal.
            DataColumn[] PrimaryKeyColumns = new DataColumn[1];
            PrimaryKeyColumns[0] = table.Columns["id"];
            table.PrimaryKey = PrimaryKeyColumns;

            // Crea tres nuevos objetos DataRow y añádelos
            // al DataTable
            var rand = new Random();
            for (int i = 1; i <= 4; i++)
            {
                row = table.NewRow();
                row["id"] = i;
                row["First Name"] = names[rand.Next(names.Length)];
                table.Rows.Add(row);
            }
            return table;
        }
```

## Conclusión

{{% alert color="primary" %}}
[Aspose.PDF.Facades](https://reference.aspose.com/pdf/net/aspose.pdf.facades) también ofrece la capacidad de llenar formularios PDF usando datos de una base de datos, pero esta característica actualmente está soportada en la versión .Net.
{{% /alert %}}