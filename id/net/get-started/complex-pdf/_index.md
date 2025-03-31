---
title: Membuat PDF yang kompleks
linktitle: Membuat PDF yang kompleks
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 60
url: /id/net/complex-pdf-example/
description: Aspose.PDF untuk NET memungkinkan Anda untuk membuat dokumen yang lebih kompleks yang mengandung gambar, fragmen teks, dan tabel dalam satu dokumen.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Creating a complex PDF",
    "alternativeHeadline": "Create Complex PDFs with Images, Text, and Tables in C#",
    "abstract": "Aspose.PDF for .NET memperkenalkan fitur kuat untuk membuat PDF yang kompleks, memungkinkan pengembang untuk mengintegrasikan gambar, fragmen teks, dan tabel ke dalam satu dokumen dengan mulus. Fungsionalitas ini memanfaatkan pendekatan berbasis DOM, memungkinkan kustomisasi dan kontrol tata letak yang mendetail dalam pembuatan PDF, menjadikannya ideal untuk membuat dokumen berkualitas profesional dengan efisien",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "632",
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
    "url": "/net/complex-pdf-example/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/complex-pdf-example/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF dapat melakukan tidak hanya tugas sederhana dan mudah tetapi juga menangani tujuan yang lebih kompleks. Periksa bagian berikut untuk pengguna dan pengembang tingkat lanjut."
}
</script>

Contoh [Hello, World](/pdf/id/net/hello-world-example/) menunjukkan langkah-langkah sederhana untuk membuat dokumen PDF menggunakan C# dan Aspose.PDF. Dalam artikel ini, kita akan melihat cara membuat dokumen yang lebih kompleks dengan C# dan Aspose.PDF for .NET. Sebagai contoh, kita akan mengambil dokumen dari perusahaan fiktif yang mengoperasikan layanan feri penumpang.
Dokumen kita akan berisi sebuah gambar, dua fragmen teks (header dan paragraf), dan sebuah tabel. Untuk membangun dokumen semacam itu, kita akan menggunakan pendekatan berbasis DOM. Anda dapat membaca lebih lanjut di bagian [Dasar-Dasar API DOM](/pdf/id/net/basics-of-dom-api/).

Jika kita membuat dokumen dari awal, kita perlu mengikuti langkah-langkah tertentu:

1. Menginstansiasi objek [Document](https://reference.aspose.com/pdf/id/net/aspose.pdf/document). Dalam langkah ini kita akan membuat dokumen PDF kosong dengan beberapa metadata tetapi tanpa halaman.
1. Menambahkan [Page](https://reference.aspose.com/pdf/id/net/aspose.pdf/page) ke objek dokumen. Jadi, sekarang dokumen kita akan memiliki satu halaman.
1. Menambahkan [Image](https://reference.aspose.com/pdf/id/net/aspose.pdf/image/methods/index) ke Halaman.
1. Membuat [TextFragment](https://reference.aspose.com/pdf/id/net/aspose.pdf.text/textfragment) untuk header. Untuk header kita akan menggunakan font Arial dengan ukuran font 24pt dan perataan tengah.
1. Menambahkan header ke [Paragraphs](https://reference.aspose.com/pdf/id/net/aspose.pdf/page/properties/paragraphs) halaman.
1. Membuat [TextFragment](https://reference.aspose.com/pdf/id/net/aspose.pdf.text/textfragment) untuk deskripsi. Untuk deskripsi kita akan menggunakan font Arial dengan ukuran font 24pt dan perataan tengah.
1. Menambahkan (deskripsi) ke Paragraphs halaman.
1. Membuat tabel, menambahkan properti tabel.
1. Menambahkan (tabel) ke [Paragraphs](https://reference.aspose.com/pdf/id/net/aspose.pdf/page/properties/paragraphs) halaman.
1. Menyimpan dokumen "Complex.pdf".

Potongan kode berikut juga bekerja dengan pustaka [Aspose.PDF.Drawing](/pdf/id/net/drawing/).

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void CreatingComplexPdf()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();
    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        // Add page
        var page = document.Pages.Add();

        // Add image
        page.AddImage(dataDir + "logo.png", new Aspose.Pdf.Rectangle(20, 730, 120, 830));

        // Add Header
        var header = new Aspose.Pdf.Text.TextFragment("New ferry routes in Fall 2020");
        header.TextState.Font = Aspose.Pdf.Text.FontRepository.FindFont("Arial");
        header.TextState.FontSize = 24;
        header.HorizontalAlignment = Aspose.Pdf.HorizontalAlignment.Center;
        header.Position = new Aspose.Pdf.Text.Position(130, 720);
        page.Paragraphs.Add(header);

        // Add description
        var descriptionText = "Visitors must buy tickets online and tickets are limited to 5,000 per day. Ferry service is operating at half capacity and on a reduced schedule. Expect lineups.";
        var description = new Aspose.Pdf.Text.TextFragment(descriptionText);
        description.TextState.Font = Aspose.Pdf.Text.FontRepository.FindFont("Times New Roman");
        description.TextState.FontSize = 14;
        description.HorizontalAlignment = Aspose.Pdf.HorizontalAlignment.Left;
        page.Paragraphs.Add(description);

        // Add table
        var table = new Aspose.Pdf.Table
        {
            ColumnWidths = "200",
            Border = new Aspose.Pdf.BorderInfo(Aspose.Pdf.BorderSide.Box, 1f, Aspose.Pdf.Color.DarkSlateGray),
            DefaultCellBorder = new Aspose.Pdf.BorderInfo(Aspose.Pdf.BorderSide.Box, 0.5f, Aspose.Pdf.Color.Black),
            DefaultCellPadding = new Aspose.Pdf.MarginInfo(4.5, 4.5, 4.5, 4.5),
            Margin =
            {
                Bottom = 10
            },
            DefaultCellTextState =
            {
                Font =  Aspose.Pdf.Text.FontRepository.FindFont("Helvetica")
            }
        };

        var headerRow = table.Rows.Add();
        headerRow.Cells.Add("Departs City");
        headerRow.Cells.Add("Departs Island");
        foreach (Aspose.Pdf.Cell headerRowCell in headerRow.Cells)
        {
            headerRowCell.BackgroundColor = Aspose.Pdf.Color.Gray;
            headerRowCell.DefaultCellTextState.ForegroundColor = Aspose.Pdf.Color.WhiteSmoke;
        }

        var time = new TimeSpan(6, 0, 0);
        var incTime = new TimeSpan(0, 30, 0);
        for (int i = 0; i < 10; i++)
        {
            var dataRow = table.Rows.Add();
            dataRow.Cells.Add(time.ToString(@"hh\:mm"));
            time = time.Add(incTime);
            dataRow.Cells.Add(time.ToString(@"hh\:mm"));
        }

        page.Paragraphs.Add(table);
        // Save PDF document
        document.Save(dataDir + "Complex_out.pdf");
    }
}
```