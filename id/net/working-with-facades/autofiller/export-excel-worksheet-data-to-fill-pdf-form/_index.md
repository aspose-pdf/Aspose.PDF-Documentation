---
title: Ekspor data Excel untuk mengisi formulir PDF
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 10
url: /id/net/export-excel-worksheet-data-to-fill-pdf-form/
description: Bagian ini menjelaskan bagaimana Anda dapat mengekspor data lembar kerja Excel untuk mengisi formulir PDF menggunakan Kelas AutoFiller.
lastmod: "2021-06-05"
draft: false
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Export Excel data to fill PDF form",
    "alternativeHeadline": "Export Excel Data to Auto-Fill PDF Forms",
    "abstract": "Fitur dalam Aspose.PDF for .NET memungkinkan pengguna untuk mengekspor data dari lembar kerja Excel ke dalam formulir PDF menggunakan Kelas AutoFiller. Dengan memanfaatkan metode ExportDataTable, pengguna dapat mengubah data Excel menjadi DataTable dan mengisi formulir PDF dengan efisien, menyederhanakan proses entri data dan meningkatkan produktivitas. Fungsionalitas ini memastikan bahwa formulir PDF diisi dengan akurat dan otomatis berdasarkan struktur data di Excel",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "908",
    "proficiencyLevel": "Beginner",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDF for .NET",
        "url": "https://products.aspose.com/pdf",
        "logo": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-net.svg",
        "alternateName": "Aspose",
        "sameAs": [
            "https://facebook.com/aspose.pdf/",
            "https://twitter.com/asposepdf",
            "https://www.youtube.com/channel/UCmV9sEg_QWYPi6BJJs7ELOg/featured",
            "https://www.linkedin.com/company/aspose",
            "https://stackoverflow.com/questions/tagged/aspose",
            "https://aspose.quora.com/",
            "https://aspose.github.io/"
        ],
        "contactPoint": [
            {
                "@type": "ContactPoint",
                "telephone": "+1 903 306 1676",
                "contactType": "sales",
                "areaServed": "US",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+44 141 628 8900",
                "contactType": "sales",
                "areaServed": "GB",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+61 2 8006 6987",
                "contactType": "sales",
                "areaServed": "AU",
                "availableLanguage": "en"
            }
        ]
    },
    "url": "/net/export-excel-worksheet-data-to-fill-pdf-form/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/export-excel-worksheet-data-to-fill-pdf-form/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF dapat melakukan tidak hanya tugas yang sederhana dan mudah tetapi juga dapat menangani tujuan yang lebih kompleks. Periksa bagian berikut untuk pengguna dan pengembang tingkat lanjut."
}
</script>

{{% alert color="primary" %}}

[Nama ruang Aspose.Pdf.Facades](https://reference.aspose.com/pdf/net/aspose.pdf.facades) di [Aspose.PDF for .NET](/pdf/id/net/) menawarkan berbagai cara untuk mengisi formulir PDF. Anda dapat mengimpor data dari file XML, DFD, XFDF, menggunakan API dan bahkan dapat menggunakan data dari lembar kerja Excel.
Kami akan menggunakan metode [ExportDataTable](https://reference.aspose.com/cells/net/aspose.cells/range/methods/exportdatatable/index) dari kelas [Cells](https://reference.aspose.com/pdf/net/aspose.pdf/cells) dari [Aspose.Cells](https://docs.aspose.com//cells/net) untuk mengekspor data dari lembar Excel ke objek DataTable. Kemudian kami perlu mengimpor data ini ke dalam formulir PDF menggunakan metode [ImportDataTable](https://reference.aspose.com/pdf/net/aspose.pdf.facades/autofiller/methods/importdatatable) dari kelas [AutoFiller](https://reference.aspose.com/pdf/net/aspose.pdf.facades/autofiller). Pastikan bahwa nama Kolom dari DataTable sama dengan nama field di formulir PDF.

{{% /alert %}}

## Detail implementasi

Dalam skenario berikut, kami akan menggunakan formulir PDF, yang berisi tiga field formulir bernama ID, Nama, dan Jenis Kelamin.

![todo:image_alt_text](export-excel-worksheet-data-to-fill-pdf-form_1.png)

Dalam formulir yang disebutkan di atas memiliki satu halaman, dengan tiga field bernama "ID", "Nama", dan "Jenis Kelamin" secara berturut-turut. Kami akan mengekstrak data dari lembar Excel berikut ke dalam objek DataTable.

![todo:image_alt_text](export-excel-worksheet-data-to-fill-pdf-form_2.png)

Kami perlu membuat objek dari kelas [AutoFiller](https://reference.aspose.com/pdf/net/aspose.pdf.facades/autofiller) dan mengikat formulir PDF yang ada di gambar di atas dan menggunakan metode [ImportDataTable](https://reference.aspose.com/pdf/net/aspose.pdf.facades/autofiller/methods/importdatatable) untuk mengisi field formulir menggunakan data yang ada di objek DataTable.
Setelah metode dipanggil, file formulir PDF baru dihasilkan, yang berisi lima halaman dengan formulir yang diisi berdasarkan data dari lembar Excel. Formulir PDF input adalah satu halaman dan hasilnya adalah lima halaman, karena jumlah baris data di lembar Excel adalah 5. Kelas DataTable menawarkan kemampuan untuk menggunakan baris pertama dari lembar sebagai ColumnName.

|**![todo:image_alt_text](export-excel-worksheet-data-to-fill-pdf-form_3.png)**|**![todo:image_alt_text](export-excel-worksheet-data-to-fill-pdf-form_4.png)**|
| :- | :- |
|![todo:image_alt_text](export-excel-worksheet-data-to-fill-pdf-form_5.png)|![todo:image_alt_text](export-excel-worksheet-data-to-fill-pdf-form_6.png)|

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ExportExcelToPdfForm()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Excel();

    var workbook = new Workbook();
    // Creating a file stream containing the Excel file to be opened
    using (FileStream fstream = new FileStream(dataDir + "newBook1.xls", FileMode.Open))
    {
        // Opening the Excel file through the file stream
        workbook.Open(fstream);
        // Accessing the first worksheet in the Excel file
        var worksheet = workbook.Worksheets[0];
        // Exporting the contents of 7 rows and 2 columns starting from 1st cell to DataTable
        System.Data.DataTable dataTable = worksheet.Cells.ExportDataTable(0, 0, worksheet.Cells.MaxRow + 1, worksheet.Cells.MaxColumn + 1, true);
        // Create an object of AutoFiller class
        using (var autoFiller = new Aspose.Pdf.Facades.AutoFiller())
        {
            // The input pdf file that contains form fields
            autoFiller.InputFileName = dataDir + "DataTableExample.pdf";
            // The resultant pdf, that will contain the form fields filled with information from DataTable
            autoFiller.OutputFileName = dataDir + "DataTableExample_out.pdf";
            // Call the method to import the data from DataTable object into Pdf form fields
            autoFiller.ImportDataTable(dataTable);
            // Save PDF document
            autoFiller.Save();
        }
    }
}
```

Untuk mengisi dari XLSX silakan gunakan potongan kode berikut:

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void FillFromXLSX()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Excel();

    // Create an object of AutoFiller class
    using (var autoFiller = new Aspose.Pdf.Facades.AutoFiller())
    {
        // Bind PDF document
        autoFiller.BindPdf(dataDir + "Sample-Form-01.pdf");

        System.Data.DataTable dataTable = GenerateDataTable();

        // Call the method to import the data from DataTable object into Pdf form fields
        autoFiller.ImportDataTable(dataTable);

        // Save PDF document
        autoFiller.Save(dataDir + "Sample-Form-01_out.pdf");
    }
}
```

Aspose.PDF for .NET memungkinkan Anda untuk menghasilkan Tabel Data dalam dokumen PDF:

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static System.Data.DataTable GenerateDataTable()
{
    string[] names = new[] { "Olivia", "Oliver", "Amelia", "George", "Isla", "Harry", "Ava", "Noah" };
    // Create a new DataTable
    var table = new System.Data.DataTable("Students");

    // Create new DataColumn, set DataType,
    // ColumnName and add to DataTable
    var column = new System.Data.DataColumn
    {
        DataType = System.Type.GetType("System.Int32"),
        ColumnName = "id",
        ReadOnly = true,
        Unique = true
    };
    // Add the Column to the DataColumnCollection
    table.Columns.Add(column);

    // Create second column
    column = new System.Data.DataColumn
    {
        DataType = System.Type.GetType("System.String"),
        ColumnName = "First Name",
        AutoIncrement = false,
        Caption = "First Name",
        ReadOnly = false,
        Unique = false
    };
    // Add the column to the table
    table.Columns.Add(column);

    // Make the ID column the primary key column
    var primaryKeyColumns = new System.Data.DataColumn[1];
    primaryKeyColumns[0] = table.Columns["id"];
    table.PrimaryKey = primaryKeyColumns;

    // Create three new DataRow objects and add
    // them to the DataTable
    var rand = new Random();
    System.Data.DataRow row;
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

## Kesimpulan

{{% alert color="primary" %}}
[Aspose.Pdf.Facades](https://reference.aspose.com/pdf/net/aspose.pdf.facades) juga menawarkan kemampuan untuk mengisi formulir PDF menggunakan data dari database tetapi fitur ini saat ini didukung dalam versi .NET.
{{% /alert %}}