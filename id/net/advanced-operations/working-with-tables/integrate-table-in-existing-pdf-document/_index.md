---
title: Integrasi Tabel dengan Sumber Data PDF
linktitle: Integrasi Tabel
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 30
url: /id/net/integrate-table/
description: Artikel ini menunjukkan cara mengintegrasikan tabel PDF. Integrasi Tabel dengan Database dan menentukan apakah tabel akan terputus di halaman saat ini.
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Integrate Table with Data Sources PDF",
    "alternativeHeadline": "Integrate PDF Tables with Data Sources Seamlessly",
    "abstract": "Fitur integrasi Tabel dengan Sumber Data PDF memungkinkan pengembang untuk mengimpor data dari berbagai sumber, termasuk database dan Entity Framework, langsung ke dalam tabel PDF menggunakan Aspose.PDF for .NET. Dengan fungsionalitas untuk menentukan pagination dan dukungan untuk kolom yang diulang, fitur ini meningkatkan presentasi data sambil menjaga integritas dokumen dengan mencegah pemutusan tabel di seluruh halaman.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "2201",
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
    "url": "/net/integrate-table/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/integrate-table/"
    },
    "dateModified": "2024-11-26",
    "description": "Artikel ini menunjukkan cara mengintegrasikan tabel PDF. Integrasi Tabel dengan Database dan menentukan apakah tabel akan terputus di halaman saat ini."
}
</script>

Potongan kode berikut juga bekerja dengan [Aspose.PDF.Drawing](/pdf/id/net/drawing/) library.

## Integrasi Tabel dengan Database

Database dibangun untuk menyimpan dan mengelola data. Merupakan praktik umum bagi programmer untuk mengisi berbagai objek dengan data dari database. Artikel ini membahas penambahan data dari database ke dalam tabel. Dimungkinkan untuk mengisi objek [Table](https://reference.aspose.com/pdf/id/net/aspose.pdf/table) dengan data dari sumber data mana pun menggunakan Aspose.PDF for .NET. Dan tidak hanya mungkin tetapi juga sangat mudah.

[Aspose.PDF for .NET](https://docs.aspose.com/pdf/net/) memungkinkan pengembang untuk mengimpor data dari:

- Object Array
- DataTable
- DataView

Topik ini memberikan informasi tentang mengambil data dari DataTable atau DataView.

Semua pengembang yang bekerja di bawah platform .NET harus akrab dengan konsep dasar ADO.NET yang diperkenalkan oleh .NET Framework. Dimungkinkan untuk terhubung ke hampir semua jenis sumber data menggunakan ADO.NET. Kita dapat mengambil data dari database dan menyimpannya ke dalam DataSet, DataTable, atau DataView. Aspose.PDF for .NET juga mendukung impor data dari ini. Ini memberikan lebih banyak kebebasan kepada pengembang untuk mengisi tabel dalam dokumen PDF dari sumber data mana pun.

Metode ImportDataTable(..) dan ImportDataView(..) dari kelas Table digunakan untuk mengimpor data dari database.

Contoh di bawah ini menunjukkan penggunaan metode ImportDataTable. Dalam contoh ini, objek DataTable dibuat dari awal dan catatan ditambahkan secara programatis alih-alih mengisi DataTable dengan data dari database. Pengembang juga dapat mengisi DataTable dari database sesuai keinginan mereka.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ImportFromDataTable()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Tables();

    DataTable dt = new DataTable("Employee");
    dt.Columns.Add("Employee_ID", typeof(Int32));
    dt.Columns.Add("Employee_Name", typeof(string));
    dt.Columns.Add("Gender", typeof(string));
    // Add 2 rows into the DataTable object programmatically
    DataRow dr = dt.NewRow();
    dr[0] = 1;
    dr[1] = "John Smith";
    dr[2] = "Male";
    dt.Rows.Add(dr);
    dr = dt.NewRow();
    dr[0] = 2;
    dr[1] = "Mary Miller";
    dr[2] = "Female";
    dt.Rows.Add(dr);
    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        // Add page
        var page = document.Pages.Add();
        // Initializes a new instance of the Table
        Aspose.Pdf.Table table = new Aspose.Pdf.Table();
        // Set column widths of the table
        table.ColumnWidths = "40 100 100 100";
        // Set the table border color as LightGray
        table.Border = new Aspose.Pdf.BorderInfo(Aspose.Pdf.BorderSide.All, .5f, Aspose.Pdf.Color.FromRgb(System.Drawing.Color.LightGray));
        // Set the border for table cells
        table.DefaultCellBorder = new Aspose.Pdf.BorderInfo(Aspose.Pdf.BorderSide.All, .5f, Aspose.Pdf.Color.FromRgb(System.Drawing.Color.LightGray));
        table.ImportDataTable(dt, true, 0, 1, 3, 3);

        // Add table object to first page of input document
        page.Paragraphs.Add(table);

        // Save PDF document
        document.Save(dataDir + "ImportFromDataTable_out.pdf");
    }
}
```

## Cara menentukan apakah tabel akan terputus di halaman saat ini

Tabel secara default ditambahkan dari posisi kiri atas dan jika tabel mencapai akhir halaman, ia secara otomatis terputus. Anda dapat secara programatis mendapatkan informasi apakah Tabel akan muat di halaman saat ini atau akan terputus di bagian bawah halaman. Untuk alasan itu, pertama-tama Anda perlu mendapatkan informasi ukuran dokumen, kemudian Anda perlu mendapatkan informasi margin Atas halaman dan margin Bawah halaman, informasi margin Atas tabel dan tinggi tabel. Jika Anda menambahkan Margin Atas halaman + Margin Bawah halaman + Margin Atas tabel + Tinggi tabel dan menguranginya dari tinggi dokumen, Anda dapat mendapatkan jumlah ruang yang tersisa di atas dokumen. Bergantung pada tinggi baris tertentu (yang telah Anda tentukan), Anda dapat menghitung apakah semua baris tabel dapat dimuat dalam ruang yang tersisa di atas halaman atau tidak. Silakan lihat potongan kode berikut. Dalam kode berikut, tinggi rata-rata baris adalah 23.002 Poin.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void DetermineTableBreak()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Tables();

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        // Add page
        var page = pdf.Pages.Add();
        // Instantiate a table object
        Aspose.Pdf.Table table1 = new Aspose.Pdf.Table();
        table1.Margin.Top = 300;
        // Add the table in paragraphs collection of the desired section
        page.Paragraphs.Add(table1);
        // Set with column widths of the table
        table1.ColumnWidths = "100 100 100";
        // Set default cell border using BorderInfo object
        table1.DefaultCellBorder = new Aspose.Pdf.BorderInfo(Aspose.Pdf.BorderSide.All, 0.1F);
        // Set table border using another customized BorderInfo object
        table1.Border = new Aspose.Pdf.BorderInfo(Aspose.Pdf.BorderSide.All, 1F);
        // Create MarginInfo object and set its left, bottom, right and top margins
        Aspose.Pdf.MarginInfo margin = new Aspose.Pdf.MarginInfo();
        margin.Top = 5f;
        margin.Left = 5f;
        margin.Right = 5f;
        margin.Bottom = 5f;
        // Set the default cell padding to the MarginInfo object
        table1.DefaultCellPadding = margin;
        // If you increase the counter to 17, table will break
        // Because it cannot be accommodated any more over this page
        for (int RowCounter = 0; RowCounter <= 16; RowCounter++)
        {
            // Create rows in the table and then cells in the rows
            Aspose.Pdf.Row row1 = table1.Rows.Add();
            row1.Cells.Add("col " + RowCounter.ToString() + ", 1");
            row1.Cells.Add("col " + RowCounter.ToString() + ", 2");
            row1.Cells.Add("col " + RowCounter.ToString() + ", 3");
        }
        // Get the Page Height information
        float PageHeight = (float)pdf.PageInfo.Height;
        // Get the total height information of Page Top & Bottom margin,
        // Table Top margin and table height.
        float TotalObjectsHeight = (float)page.PageInfo.Margin.Top + (float)page.PageInfo.Margin.Bottom + (float)table1.Margin.Top + (float)table1.GetHeight();

        // Display Page Height, Table Height, table Top margin and Page Top
        // And Bottom margin information
        Console.WriteLine("PDF document Height = " + pdf.PageInfo.Height.ToString() + "\nTop Margin Info = " + page.PageInfo.Margin.Top.ToString() + "\nBottom Margin Info = " + page.PageInfo.Margin.Bottom.ToString() + "\n\nTable-Top Margin Info = " + table1.Margin.Top.ToString() + "\nAverage Row Height = " + table1.Rows[0].MinRowHeight.ToString() + " \nTable height " + table1.GetHeight().ToString() + "\n ----------------------------------------" + "\nTotal Page Height =" + PageHeight.ToString() + "\nCummulative height including Table =" + TotalObjectsHeight.ToString());

        // Check if we deduct the sume of Page top margin + Page Bottom margin
        // + Table Top margin and table height from Page height and its less
        // Than 10 (an average row can be greater than 10)
        if ((PageHeight - TotalObjectsHeight) <= 10)
        {
            // If the value is less than 10, then display the message.
            // Which shows that another row can not be placed and if we add new
            // Row, table will break. It depends upon the row height value.
            Console.WriteLine("Page Height - Objects Height < 10, so table will break");
        }

        // Save PDF document
        document.Save(dataDir + "DetermineTableBreak_out.pdf");
    }
}
```

## Tambahkan Kolom yang Diulang dalam Tabel

Dalam kelas Aspose.Pdf.Table, Anda dapat mengatur RepeatingRowsCount yang akan mengulang baris jika tabel terlalu panjang secara vertikal dan meluap ke halaman berikutnya. Namun, dalam beberapa kasus, tabel terlalu lebar untuk muat di satu halaman dan perlu dilanjutkan ke halaman berikutnya. Untuk memenuhi tujuan tersebut, kami telah menerapkan properti RepeatingColumnsCount dalam kelas Aspose.Pdf.Table. Mengatur properti ini akan menyebabkan tabel terputus ke halaman berikutnya secara kolom dan mengulang jumlah kolom yang diberikan di awal halaman berikutnya. Potongan kode berikut menunjukkan penggunaan properti RepeatingColumnsCount:

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddRepeatingColumn()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Tables();

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        // Add page
        var page = document.Pages.Add();

        // Instantiate an outer table that takes up the entire page
        Aspose.Pdf.Table outerTable = new Aspose.Pdf.Table();
        outerTable.ColumnWidths = "100%";
        outerTable.HorizontalAlignment = HorizontalAlignment.Left;

        // Instantiate a table object that will be nested inside outerTable that will break inside the same page
        Aspose.Pdf.Table mytable = new Aspose.Pdf.Table();
        mytable.Broken = TableBroken.VerticalInSamePage;
        mytable.ColumnAdjustment = ColumnAdjustment.AutoFitToContent;

        // Add the outerTable to the page paragraphs
        // Add mytable to outerTable
        page.Paragraphs.Add(outerTable);
        var bodyRow = outerTable.Rows.Add();
        var bodyCell = bodyRow.Cells.Add();
        bodyCell.Paragraphs.Add(mytable);
        mytable.RepeatingColumnsCount = 5;
        page.Paragraphs.Add(mytable);

        // Add header Row
        Aspose.Pdf.Row row = mytable.Rows.Add();
        row.Cells.Add("header 1");
        row.Cells.Add("header 2");
        row.Cells.Add("header 3");
        row.Cells.Add("header 4");
        row.Cells.Add("header 5");
        row.Cells.Add("header 6");
        row.Cells.Add("header 7");
        row.Cells.Add("header 11");
        row.Cells.Add("header 12");
        row.Cells.Add("header 13");
        row.Cells.Add("header 14");
        row.Cells.Add("header 15");
        row.Cells.Add("header 16");
        row.Cells.Add("header 17");

        for (int RowCounter = 0; RowCounter <= 5; RowCounter++)
        {
            // Create rows in the table and then cells in the rows
            Aspose.Pdf.Row row1 = mytable.Rows.Add();
            row1.Cells.Add("col " + RowCounter.ToString() + ", 1");
            row1.Cells.Add("col " + RowCounter.ToString() + ", 2");
            row1.Cells.Add("col " + RowCounter.ToString() + ", 3");
            row1.Cells.Add("col " + RowCounter.ToString() + ", 4");
            row1.Cells.Add("col " + RowCounter.ToString() + ", 5");
            row1.Cells.Add("col " + RowCounter.ToString() + ", 6");
            row1.Cells.Add("col " + RowCounter.ToString() + ", 7");
            row1.Cells.Add("col " + RowCounter.ToString() + ", 11");
            row1.Cells.Add("col " + RowCounter.ToString() + ", 12");
            row1.Cells.Add("col " + RowCounter.ToString() + ", 13");
            row1.Cells.Add("col " + RowCounter.ToString() + ", 14");
            row1.Cells.Add("col " + RowCounter.ToString() + ", 15");
            row1.Cells.Add("col " + RowCounter.ToString() + ", 16");
            row1.Cells.Add("col " + RowCounter.ToString() + ", 17");
        }

        // Save PDF document
        document.Save(dataDir + "AddRepeatingColumn_out.pdf");
    }
}
```

## Integrasi Tabel dengan sumber Entity Framework

Lebih relevan untuk .NET modern adalah impor data dari kerangka ORM. Dalam hal ini, merupakan ide yang baik untuk memperluas kelas Table dengan metode ekstensi untuk mengimpor data dari daftar sederhana atau dari data yang dikelompokkan. Mari kita berikan contoh untuk salah satu ORM yang paling populer - Entity Framework.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
public static class PdfHelper
{
    private static void ImportEntityList<TSource>(this Pdf.Table table, IList<TSource> data)
    {
        var headRow = table.Rows.Add();

        var props = typeof(TSource).GetProperties(BindingFlags.Public | BindingFlags.Instance);
        foreach (var prop in props)
        {
            headRow.Cells.Add(prop.GetCustomAttribute(typeof(DisplayAttribute)) is DisplayAttribute dd ? dd.Name : prop.Name);
        }

        foreach (var item in data)
        {
            // Add row to table
            var row = table.Rows.Add();
            // Add table cells
            foreach (var t in props)
            {
                var dataItem = t.GetValue(item, null);
                if (t.GetCustomAttribute(typeof(DataTypeAttribute)) is DataTypeAttribute dataType)
                    switch (dataType.DataType)
                    {

                        case DataType.Currency:
                            row.Cells.Add(string.Format("{0:C}", dataItem));
                            break;
                        case DataType.Date:
                            var dateTime = (DateTime)dataItem;
                            if (t.GetCustomAttribute(typeof(DisplayFormatAttribute)) is DisplayFormatAttribute df)
                            {
                                row.Cells.Add(string.IsNullOrEmpty(df.DataFormatString)
                                    ? dateTime.ToShortDateString()
                                    : string.Format(df.DataFormatString, dateTime));
                            }
                            break;
                        default:
                            row.Cells.Add(dataItem.ToString());
                            break;
                    }
                else
                {
                    row.Cells.Add(dataItem.ToString());
                }
            }
        }
    }
    
    private static void ImportGroupedData<TKey,TValue>(this Pdf.Table table, IEnumerable<Models.GroupViewModel<TKey, TValue>> groupedData)
    {
        var headRow = table.Rows.Add();           
        var props = typeof(TValue).GetProperties(BindingFlags.Public | BindingFlags.Instance);
        foreach (var prop in props)
        {
            headRow.Cells.Add(prop.GetCustomAttribute(typeof(DisplayAttribute)) is DisplayAttribute dd ? dd.Name : prop.Name);               
        }

        foreach (var group in groupedData)
        {
            // Add group row to table
            var row = table.Rows.Add();
            var cell = row.Cells.Add(group.Key.ToString());
            cell.ColSpan = props.Length;
            cell.BackgroundColor = Pdf.Color.DarkGray;
            cell.DefaultCellTextState.ForegroundColor = Pdf.Color.White;

            foreach (var item in group.Values)
            {
                // Add data row to table
                var dataRow = table.Rows.Add();
                // Add cells
                foreach (var t in props)
                {
                    var dataItem = t.GetValue(item, null);

                    if (t.GetCustomAttribute(typeof(DataTypeAttribute)) is DataTypeAttribute dataType)
                        switch (dataType.DataType)
                        {
                            case DataType.Currency:
                                dataRow.Cells.Add(string.Format("{0:C}", dataItem));
                                break;
                            case DataType.Date:
                                var dateTime = (DateTime)dataItem;
                                if (t.GetCustomAttribute(typeof(DisplayFormatAttribute)) is DisplayFormatAttribute df)
                                {
                                    dataRow.Cells.Add(string.IsNullOrEmpty(df.DataFormatString)
                                        ? dateTime.ToShortDateString()
                                        : string.Format(df.DataFormatString, dateTime));
                                }
                                break;
                            default:
                                dataRow.Cells.Add(dataItem.ToString());
                                break;
                        }
                    else
                    {
                        dataRow.Cells.Add(dataItem.ToString());
                    }
                }
            }
        }
    }
}
```

Atribut Data Annotations sering digunakan untuk mendeskripsikan model dan membantu kita membuat tabel. Oleh karena itu, algoritma pembuatan tabel berikut dipilih untuk ImportEntityList:

- baris 12-18: membangun baris header dan menambahkan sel header sesuai dengan aturan "Jika DisplayAttribute ada, maka ambil nilainya jika tidak ambil nama propertinya"
- baris 50-53: membangun baris data dan menambahkan sel baris sesuai dengan aturan "Jika atribut DataTypeAttribute didefinisikan, maka kita memeriksa apakah kita perlu membuat pengaturan desain tambahan untuk itu, dan jika tidak, cukup konversi data ke string dan tambahkan ke sel;"

Dalam contoh ini, penyesuaian tambahan dibuat untuk DataType.Currency (baris 32-34) dan DataType.Date (baris 35-43), tetapi Anda dapat menambahkan yang lain jika perlu.
Algoritma metode ImportGroupedData hampir sama dengan yang sebelumnya. Kelas GroupViewModel tambahan digunakan untuk menyimpan data yang dikelompokkan.

```csharp
using System.Collections.Generic;
public class GroupViewModel<K,T>
{
    public K Key;
    public IEnumerable<T> Values;
}
```

Karena kita memproses grup, pertama kita menghasilkan baris untuk nilai kunci (baris 66-71), dan setelah itu - baris dari grup ini.

<script type="application/ld+json">
{
    "@context": "http://schema.org",
    "@type": "SoftwareApplication",
    "name": "Aspose.PDF for .NET Library",
    "image": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-net.svg",
    "url": "https://www.aspose.com/",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDF",
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
    "offers": {
        "@type": "Offer",
        "price": "1199",
        "priceCurrency": "USD"
    },
    "applicationCategory": "PDF Manipulation Library for .NET",
    "downloadUrl": "https://www.nuget.org/packages/Aspose.PDF/",
    "operatingSystem": "Windows, MacOS, Linux",
    "screenshot": "https://docs.aspose.com/pdf/net/create-pdf-document/screenshot.png",
    "softwareVersion": "2022.1",
    "aggregateRating": {
        "@type": "AggregateRating",
        "ratingValue": "5",
        "ratingCount": "16"
    }
}
</script>