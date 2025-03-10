---
title: Ganti Teks di PDF
linktitle: Ganti Teks di PDF
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 40
url: /id/net/replace-text-in-pdf/
description: Pelajari lebih lanjut tentang berbagai cara mengganti dan menghapus teks dari Aspose.PDF for .NET library.
lastmod: "2022-02-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Replace Text in PDF",
    "alternativeHeadline": "Efficiently Modify Text Across PDF Pages with Ease",
    "abstract": "Fitur Ganti Teks di PDF dalam Aspose.PDF for .NET memungkinkan pengguna untuk dengan efisien menemukan dan mengganti teks di seluruh dokumen PDF atau dalam wilayah halaman tertentu. Ini mendukung kemampuan lanjutan, termasuk penggantian teks berdasarkan ekspresi reguler, pengaturan ulang konten halaman secara otomatis setelah penggantian, dan kemampuan untuk menghapus font yang tidak terpakai, meningkatkan pengalaman pengeditan dokumen.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "2744",
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
    "url": "/net/replace-text-in-pdf/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/replace-text-in-pdf/"
    },
    "dateModified": "2024-11-26",
    "description": "Pelajari lebih lanjut tentang berbagai cara mengganti dan menghapus teks dari Aspose.PDF for .NET library."
}
</script>

Potongan kode berikut juga bekerja dengan [Aspose.PDF.Drawing](/pdf/id/net/drawing/) library.

## Ganti Teks di semua halaman dokumen PDF

{{% alert color="primary" %}}

Anda dapat mencoba menemukan dan mengganti teks dalam dokumen menggunakan Aspose.PDF dan mendapatkan hasilnya secara online di [tautan ini](https://products.aspose.app/pdf/redaction)

{{% /alert %}}

Untuk mengganti teks di semua halaman dokumen PDF, Anda pertama-tama perlu menggunakan TextFragmentAbsorber untuk menemukan frasa tertentu yang ingin Anda ganti. Setelah itu, Anda perlu melalui semua TextFragments untuk mengganti teks dan mengubah atribut lainnya. Setelah Anda melakukannya, Anda hanya perlu menyimpan PDF keluaran menggunakan metode Save dari objek Document. Potongan kode berikut menunjukkan cara mengganti teks di semua halaman dokumen PDF.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ReplaceTextInAllPages()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Text();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "ReplaceTextAll.pdf"))
    {
        // Create TextAbsorber object to find all instances of the input search phrase
        var absorber = new Aspose.Pdf.Text.TextFragmentAbsorber("text");

        // Accept the absorber for all the pages
        document.Pages.Accept(absorber);

        // Get the extracted text fragments
        var textFragmentCollection = absorber.TextFragments;

        // Loop through the fragments
        foreach (var textFragment in textFragmentCollection)
        {
            // Update text and other properties
            textFragment.Text = "TEXT";
            textFragment.TextState.Font = Aspose.Pdf.Text.FontRepository.FindFont("Verdana");
            textFragment.TextState.FontSize = 22;
            textFragment.TextState.ForegroundColor = Aspose.Pdf.Color.FromRgb(System.Drawing.Color.Blue);
            textFragment.TextState.BackgroundColor = Aspose.Pdf.Color.FromRgb(System.Drawing.Color.Green);
        }

        // Save PDF document
        document.Save(dataDir + "ReplaceTextInAllPages_out.pdf");
    }
}
```

## Ganti Teks di wilayah halaman tertentu

Untuk mengganti teks di wilayah halaman tertentu, pertama, kita perlu menginstansiasi objek TextFragmentAbsorber, menentukan wilayah halaman menggunakan properti TextSearchOptions.Rectangle dan kemudian iterasi melalui semua TextFragments untuk mengganti teks. Setelah operasi ini selesai, kita hanya perlu menyimpan PDF keluaran menggunakan metode Save dari objek Document. Potongan kode berikut menunjukkan cara mengganti teks di semua halaman dokumen PDF.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ReplaceTextInParticularPageRegion()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Text();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "programaticallyproducedpdf.pdf"))
    {
        // instantiate TextFragment Absorber object
        var absorber = new Aspose.Pdf.Text.TextFragmentAbsorber();

        // search text within page bound
        absorber.TextSearchOptions.LimitToPageBounds = true;

        // specify the page region for TextSearch Options
        absorber.TextSearchOptions.Rectangle = new Aspose.Pdf.Rectangle(100, 100, 200, 200);

        // search text from first page of PDF file
        document.Pages[1].Accept(absorber);

        // iterate through individual TextFragment
        foreach (var textFragment in absorber.TextFragments)
        {
            // update text to blank characters
            textFragment.Text = "";
        }

        // Save PDF document
        document.Save(dataDir + "ReplaceTextInParticularPageRegion_out.pdf");
    }
}
```

## Ganti Teks Berdasarkan Ekspresi Reguler

Jika Anda ingin mengganti beberapa frasa berdasarkan ekspresi reguler, Anda pertama-tama perlu menemukan semua frasa yang cocok dengan ekspresi reguler tertentu menggunakan TextFragmentAbsorber. Anda harus melewatkan ekspresi reguler sebagai parameter ke konstruktor TextFragmentAbsorber. Anda juga perlu membuat objek TextSearchOptions yang menentukan apakah ekspresi reguler sedang digunakan atau tidak. Setelah Anda mendapatkan frasa yang cocok dalam TextFragments, Anda perlu melakukan loop melalui semuanya dan memperbarui sesuai kebutuhan. Akhirnya, Anda perlu menyimpan PDF yang diperbarui menggunakan metode Save dari objek Document. Potongan kode berikut menunjukkan cara mengganti teks berdasarkan ekspresi reguler.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ReplaceTextBasedOnARegularExpression()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Text();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "SearchRegularExpressionPage.pdf"))
    {

        // Create TextAbsorber object to find all the phrases matching the regular expression
        var absorber = new Aspose.Pdf.Text.TextFragmentAbsorber("\\d{4}-\\d{4}"); // Like 1999-2000

        // Set text search option to specify regular expression usage
        absorber.TextSearchOptions = new Aspose.Pdf.Text.TextSearchOptions(true);

        // Accept the absorber for a single page
        document.Pages[1].Accept(absorber);

        // Get the extracted text fragments
        var collection = absorber.TextFragments;

        // Loop through the fragments
        foreach (var textFragment in collection)
        {
            // Update text and other properties
            textFragment.Text = "New Phrase";
            // Set to an instance of an object.
            textFragment.TextState.Font = Aspose.Pdf.Text.FontRepository.FindFont("Verdana");
            textFragment.TextState.FontSize = 22;
            textFragment.TextState.ForegroundColor = Aspose.Pdf.Color.FromRgb(System.Drawing.Color.Blue);
            textFragment.TextState.BackgroundColor = Aspose.Pdf.Color.FromRgb(System.Drawing.Color.Green);
        }

        // Save PDF document
        document.Save(dataDir + "ReplaceTextonRegularExpression_out.pdf");
    }
}
```

## Ganti font di file PDF yang ada

Aspose.PDF for .NET mendukung kemampuan untuk mengganti teks di dokumen PDF. Namun, terkadang Anda memiliki kebutuhan untuk hanya mengganti font yang digunakan di dalam dokumen PDF. Jadi alih-alih mengganti teks, hanya font yang digunakan yang diganti. Salah satu overload dari konstruktor TextFragmentAbsorber menerima objek TextEditOptions sebagai argumen dan kita dapat menggunakan nilai RemoveUnusedFonts dari enumerasi TextEditOptions.FontReplace untuk memenuhi kebutuhan kita. Potongan kode berikut menunjukkan cara mengganti font di dalam dokumen PDF.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ReplaceFonts()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Text();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "ReplaceTextPage.pdf"))
    {
        // Create text edit options
        var options = new Aspose.Pdf.Text.TextEditOptions(Aspose.Pdf.Text.TextEditOptions.FontReplace.RemoveUnusedFonts);

        // Search text fragments and set edit option as remove unused fonts
        var absorber = new Aspose.Pdf.Text.TextFragmentAbsorber(options);

        // Accept the absorber for all the pages
        document.Pages.Accept(absorber);

        // Traverse through all the TextFragments
        foreach (var textFragment in absorber.TextFragments)
        {
            // If the font name is ArialMT, replace font name with Arial
            if (textFragment.TextState.Font.FontName == "Arial,Bold")
            {
                textFragment.TextState.Font = Aspose.Pdf.Text.FontRepository.FindFont("Arial");
            }
        }

        // Save PDF document
        document.Save(dataDir + "ReplaceFonts_out.pdf");
    }
}
```

## Penggantian Teks harus secara otomatis mengatur ulang Konten Halaman

Aspose.PDF for .NET mendukung fitur untuk mencari dan mengganti teks di dalam file PDF. Namun baru-baru ini beberapa pelanggan mengalami masalah selama penggantian teks ketika TextFragment tertentu diganti dengan konten yang lebih kecil dan beberapa ruang ekstra ditampilkan di PDF hasil atau jika TextFragment diganti dengan string yang lebih panjang, maka kata-kata tumpang tindih dengan konten halaman yang ada. Jadi, kebutuhan adalah untuk memperkenalkan mekanisme yang setelah teks di dalam dokumen PDF diganti, konten harus diatur ulang.

Untuk memenuhi skenario yang disebutkan di atas, Aspose.PDF for .NET telah ditingkatkan sehingga tidak ada masalah seperti itu muncul saat mengganti teks di dalam file PDF. Potongan kode berikut menunjukkan cara mengganti teks di dalam file PDF dan konten halaman harus diatur ulang secara otomatis.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AutomaticallyReArrangePageContents()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Text();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "ExtractTextPage.pdf"))
    {
        // Create TextFragment Absorber object with regular expression
        var absorber = new Aspose.Pdf.Text.TextFragmentAbsorber("[TextFragmentAbsorber,companyname,Textbox,50]");
        document.Pages.Accept(absorber);

        // Replace each TextFragment
        foreach (var textFragment in absorber.TextFragments)
        {
            // Set font of text fragment being replaced
            textFragment.TextState.Font = Aspose.Pdf.Text.FontRepository.FindFont("Arial");
            // Set font size
            textFragment.TextState.FontSize = 12;
            textFragment.TextState.ForegroundColor = Aspose.Pdf.Color.Navy;
            // Replace the text with larger string than placeholder
            textFragment.Text = "This is a Larger String for the Testing of this issue";
        }

        // Save PDF document
        document.Save(dataDir + "AutomaticallyReArrangePageContents_out.pdf");
    }
}
```

## Merender Simbol yang Dapat Diganti selama pembuatan PDF

Simbol yang dapat diganti adalah simbol khusus dalam string teks yang dapat diganti dengan konten yang sesuai pada waktu berjalan. Simbol yang dapat diganti saat ini didukung oleh Model Objek Dokumen baru dari namespace Aspose.PDF adalah `$P`, `$p,` `\n`, `\r`. `$p` digunakan untuk menangani penomoran halaman pada waktu berjalan. `$p` diganti dengan nomor halaman tempat kelas Paragraph saat ini berada. `$P` diganti dengan total jumlah halaman dalam dokumen. Saat menambahkan `TextFragment` ke koleksi paragraf dokumen PDF, tidak mendukung pemisahan baris di dalam teks. Namun untuk menambahkan teks dengan pemisahan baris, silakan gunakan `TextFragment` dengan `TextParagraph`:

- Gunakan "\r\n" atau Environment.NewLine di TextFragment alih-alih "\n" tunggal.
- Buat objek TextParagraph. Ini akan menambahkan teks dengan pemisahan baris.
- Tambahkan TextFragment dengan TextParagraph.AppendLine.
- Tambahkan TextParagraph dengan TextBuilder.AppendParagraph.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void RenderingReplaceableSymbols()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Text();

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        var page = document.Pages.Add();

        // Initialize new TextFragment with text containing required newline markers
        Aspose.Pdf.Text.TextFragment textFragment = new Aspose.Pdf.Text.TextFragment("Applicant Name: " + Environment.NewLine + " Joe Smoe");

        // Set text fragment properties if necessary
        textFragment.TextState.FontSize = 12;
        textFragment.TextState.Font = Aspose.Pdf.Text.FontRepository.FindFont("TimesNewRoman");
        textFragment.TextState.BackgroundColor = Aspose.Pdf.Color.LightGray;
        textFragment.TextState.ForegroundColor = Aspose.Pdf.Color.Red;

        // Create TextParagraph object
        var par = new Aspose.Pdf.Text.TextParagraph();

        // Add new TextFragment to paragraph
        par.AppendLine(textFragment);

        // Set paragraph position
        par.Position = new Aspose.Pdf.Text.Position(100, 600);

        // Create TextBuilder object
        var textBuilder = new Aspose.Pdf.Text.TextBuilder(page);

        // Add the TextParagraph using TextBuilder
        textBuilder.AppendParagraph(par);

        // Save PDF document
        document.Save(dataDir + "RenderingReplaceableSymbols_out.pdf");
    }
}
```

## Simbol yang dapat diganti di area Header/Footer

Simbol yang dapat diganti juga dapat ditempatkan di dalam bagian Header/Footer file PDF. Silakan lihat potongan kode berikut untuk detail tentang cara menambahkan simbol yang dapat diganti di bagian footer.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ReplaceableSymbolsInHeaderOrFooterArea()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Text();

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        var page = document.Pages.Add();

        // Create margin info
        var marginInfo = new Aspose.Pdf.MarginInfo();
        marginInfo.Top = 90;
        marginInfo.Bottom = 50;
        marginInfo.Left = 50;
        marginInfo.Right = 50;
        // Assign the marginInfo instance to Margin property of sec1.PageInfo
        page.PageInfo.Margin = marginInfo;

        var headerFooterFirst = new Aspose.Pdf.HeaderFooter();
        page.Header = headerFooterFirst;
        headerFooterFirst.Margin.Left = 50;
        headerFooterFirst.Margin.Right = 50;

        // Instantiate a Text paragraph that will store the content to show as header
        var fragment1 = new Aspose.Pdf.Text.TextFragment("report title");
        fragment1.TextState.Font = Aspose.Pdf.Text.FontRepository.FindFont("Arial");
        fragment1.TextState.FontSize = 16;
        fragment1.TextState.ForegroundColor = Aspose.Pdf.Color.Black;
        fragment1.TextState.FontStyle = Aspose.Pdf.Text.FontStyles.Bold;
        fragment1.TextState.HorizontalAlignment = Aspose.Pdf.HorizontalAlignment.Center;
        fragment1.TextState.LineSpacing = 5f;
        headerFooterFirst.Paragraphs.Add(fragment1);

        var fragment2 = new Aspose.Pdf.Text.TextFragment("Report_Name");
        fragment2.TextState.Font = Aspose.Pdf.Text.FontRepository.FindFont("Arial");
        fragment2.TextState.ForegroundColor = Aspose.Pdf.Color.Black;
        fragment2.TextState.HorizontalAlignment = Aspose.Pdf.HorizontalAlignment.Center;
        fragment2.TextState.LineSpacing = 5f;
        fragment2.TextState.FontSize = 12;
        headerFooterFirst.Paragraphs.Add(fragment2);

        // Create a HeaderFooter object for the section
        var headerFooterFoot = new Aspose.Pdf.HeaderFooter();

        // Set the HeaderFooter object to odd & even footer
        page.Footer = headerFooterFoot;
        headerFooterFoot.Margin.Left = 50;
        headerFooterFoot.Margin.Right = 50;

        // Add a text paragraph containing current page number of total number of pages
        var fragment3 = new Aspose.Pdf.Text.TextFragment("Generated on test date");
        var fragment4 = new Aspose.Pdf.Text.TextFragment("report name ");
        var fragment5 = new Aspose.Pdf.Text.TextFragment("Page $p of $P");

        // Instantiate a table object
        var table2 = new Aspose.Pdf.Table();

        // Add the table in paragraphs collection of the desired section
        headerFooterFoot.Paragraphs.Add(table2);

        // Set with column widths of the table
        table2.ColumnWidths = "165 172 165";

        // Create rows in the table and then cells in the rows
        var row3 = table2.Rows.Add();

        row3.Cells.Add();
        row3.Cells.Add();
        row3.Cells.Add();

        // Set the vertical allignment of the text as center alligned
        row3.Cells[0].Alignment = Aspose.Pdf.HorizontalAlignment.Left;
        row3.Cells[1].Alignment = Aspose.Pdf.HorizontalAlignment.Center;
        row3.Cells[2].Alignment = Aspose.Pdf.HorizontalAlignment.Right;

        row3.Cells[0].Paragraphs.Add(fragment3);
        row3.Cells[1].Paragraphs.Add(fragment4);
        row3.Cells[2].Paragraphs.Add(fragment5);

        // Sec1.Paragraphs.Add(New Text("Aspose.Total for Java is a compilation of every Java component offered by Aspose. It is compiled on a#$NL" + "daily basis to ensure it contains the most up to date versions of each of our Java components. #$NL " + "Using Aspose.Total for Java developers can create a wide range of applications. #$NL #$NL #$NP" + "Aspose.Total for Java is a compilation of every Java component offered by Aspose. It is compiled on a#$NL" + "daily basis to ensure it contains the most up to date versions of each of our Java components. #$NL " + "Using Aspose.Total for Java developers can create a wide range of applications. #$NL #$NL #$NP" + "Aspose.Total for Java is a compilation of every Java component offered by Aspose. It is compiled on a#$NL" + "daily basis to ensure it contains the most up to date versions of each of our Java components. #$NL " + "Using Aspose.Total for Java developers can create a wide range of applications. #$NL #$NL"))
        var table = new Aspose.Pdf.Table();

        table.ColumnWidths = "33% 33% 34%";
        table.DefaultCellPadding = new Aspose.Pdf.MarginInfo();
        table.DefaultCellPadding.Top = 10;
        table.DefaultCellPadding.Bottom = 10;

        // Add the table in paragraphs collection of the desired section
        page.Paragraphs.Add(table);

        // Set default cell border using BorderInfo object
        table.DefaultCellBorder = new Aspose.Pdf.BorderInfo(Aspose.Pdf.BorderSide.All, 0.1f);

        // Set table border using another customized BorderInfo object
        table.Border = new Aspose.Pdf.BorderInfo(Aspose.Pdf.BorderSide.All, 1f);

        table.RepeatingRowsCount = 1;

        // Create rows in the table and then cells in the rows
        var row1 = table.Rows.Add();

        row1.Cells.Add("col1");
        row1.Cells.Add("col2");
        row1.Cells.Add("col3");
        const string CRLF = "\r\n";
        for (int i = 0; i <= 10; i++)
        {
            var row = table.Rows.Add();
            row.IsRowBroken = true;
            for (int c = 0; c <= 2; c++)
            {
                Aspose.Pdf.Cell c1;
                if (c == 2)
                {
                    c1 = row.Cells.Add("Aspose.Total for Java is a compilation of every Java component offered by Aspose. It is compiled on a" + CRLF + "daily basis to ensure it contains the most up to date versions of each of our Java components. " + CRLF + "daily basis to ensure it contains the most up to date versions of each of our Java components. " + CRLF + "Using Aspose.Total for Java developers can create a wide range of applications.");
                }
                else
                {
                    c1 = row.Cells.Add("item1" + c);
                }
                c1.Margin = new Aspose.Pdf.MarginInfo();
                c1.Margin.Left = 30;
                c1.Margin.Top = 10;
                c1.Margin.Bottom = 10;
            }
        }

        // Save PDF document
        document.Save(dataDir + "ReplaceableSymbolsInHeaderFooter_out.pdf");
    }
}
```

## Hapus Font yang Tidak Digunakan dari File PDF

Aspose.PDF for .NET mendukung fitur untuk menyematkan font saat membuat dokumen PDF, serta kemampuan untuk menyematkan font di file PDF yang ada. Dari Aspose.PDF for .NET 7.3.0, ini juga memungkinkan Anda untuk menghapus font duplikat atau yang tidak terpakai dari dokumen PDF.

Untuk mengganti font, gunakan pendekatan berikut:

1. Panggil kelas [TextFragmentAbsorber](https://reference.aspose.com/pdf/net/aspose.pdf.text/textfragmentabsorber).
1. Panggil parameter TextFragmentAbsorber kelas’ TextEditOptions.FontReplace.RemoveUnusedFonts. (Ini menghapus font yang telah menjadi tidak terpakai selama penggantian font).
1. Atur font secara individu untuk setiap fragmen teks.

Potongan kode berikut mengganti font untuk semua fragmen teks dari semua halaman dokumen dan menghapus font yang tidak terpakai.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void RemoveUnusedFonts()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Text();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "ReplaceTextPage.pdf"))
    {
        var options = new Aspose.Pdf.Text.TextEditOptions(Aspose.Pdf.Text.TextEditOptions.FontReplace.RemoveUnusedFonts);
        var absorber = new Aspose.Pdf.Text.TextFragmentAbsorber();
        document.Pages.Accept(absorber);

        // Iterate through all the TextFragments
        foreach (var textFragment in absorber.TextFragments)
        {
            textFragment.TextState.Font = Aspose.Pdf.Text.FontRepository.FindFont("Arial, Bold");
        }

        // Save PDF document
        document.Save(dataDir + "RemoveUnusedFonts_out.pdf");
    }
}
```

## Hapus Semua Teks dari Dokumen PDF

### Hapus Semua Teks menggunakan Operator

Dalam beberapa operasi teks, Anda perlu menghapus semua teks dari dokumen PDF dan untuk itu, Anda perlu mengatur teks yang ditemukan sebagai nilai string kosong biasanya. Intinya adalah bahwa mengubah teks untuk banyak fragmen teks memicu sejumlah pemeriksaan dan penyesuaian posisi teks. Mereka penting dalam skenario pengeditan teks. Kesulitannya adalah Anda tidak dapat menentukan berapa banyak fragmen teks yang akan dihapus dalam skenario di mana mereka diproses dalam loop.

Oleh karena itu, kami merekomendasikan menggunakan pendekatan lain untuk skenario menghapus semua teks dari halaman PDF. Silakan pertimbangkan potongan kode berikut yang bekerja sangat cepat.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void RemoveAllTextFromDocument()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Text();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "RemoveAllText.pdf"))
    {
        // Loop through all pages of PDF Document
        for (int i = 1; i <= document.Pages.Count; i++)
        {
            var page = document.Pages[i];
            var operatorSelector = new Aspose.Pdf.OperatorSelector(new Aspose.Pdf.Operators.TextShowOperator());
            // Select all text on the page
            page.Contents.Accept(operatorSelector);
            // Delete all text
            page.Contents.Delete(operatorSelector.Selected);
        }
        // Save PDF document
        document.Save(dataDir + "RemoveAllText_out.pdf", Aspose.Pdf.SaveFormat.Pdf);
    }
}
```

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