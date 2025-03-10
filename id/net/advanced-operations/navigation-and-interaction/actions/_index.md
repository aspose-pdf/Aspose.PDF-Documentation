---
title: Bekerja dengan Aksi di PDF
linktitle: Aksi
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 20
url: /id/net/actions/
description: Bagian ini menjelaskan cara menambahkan aksi ke dokumen dan bidang formulir secara programatis dengan C#.
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Working with Actions in PDF",
    "alternativeHeadline": "Programmatic Actions in PDF with C#",
    "abstract": "Fitur baru di Aspose.PDF for .NET memungkinkan pengembang untuk menambahkan aksi ke PDF secara programatis, meningkatkan interaktivitas dalam dokumen. Pengguna dapat menerapkan hyperlink untuk menavigasi dalam dokumen atau ke URL eksternal, serta memanipulasi aksi buka dokumen untuk mengontrol bagaimana PDF ditampilkan saat dibuka. Fungsionalitas yang kuat ini memperlancar pembuatan dan interaksi dokumen untuk aplikasi C#",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "keywords": "C#, PDF actions, hyperlink creation, LinkAnnotation, LocalHyperlink, FreeTextAnnotation, document open action, XYZExplicitDestination, Aspose.PDF, PDF manipulation",
    "wordcount": "2007",
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
    "url": "/net/actions/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/actions/"
    },
    "dateModified": "2024-11-25",
    "description": "Bagian ini menjelaskan cara menambahkan aksi ke dokumen dan bidang formulir secara programatis dengan C#."
}
</script>

Potongan kode berikut juga bekerja dengan [Aspose.PDF.Drawing](/pdf/net/drawing/) library.

## Tambahkan Hyperlink di File PDF

Adalah mungkin untuk menambahkan hyperlink ke file PDF, baik untuk memungkinkan pembaca menavigasi ke bagian lain dari PDF, atau ke konten eksternal.

Untuk menambahkan hyperlink web ke dokumen PDF:

1. Buat objek Kelas [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document).
1. Dapatkan Kelas [Page](https://reference.aspose.com/pdf/net/aspose.pdf/page) yang ingin Anda tambahkan tautan.
1. Buat objek [LinkAnnotation](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/linkannotation) menggunakan objek Page dan [Rectangle](https://reference.aspose.com/pdf/net/aspose.pdf/rectangle). Objek rectangle digunakan untuk menentukan lokasi di halaman tempat tautan harus ditambahkan.
1. Atur properti Action ke objek [GoToURIAction](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/gotouriaction) yang menentukan lokasi URI jarak jauh.
1. Untuk menampilkan teks hyperlink, tambahkan string teks di lokasi yang mirip dengan tempat objek [LinkAnnotation](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/linkannotation) ditempatkan.
1. Untuk menambahkan teks bebas:

- Buat objek [FreeTextAnnotation](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/freetextannotation). Ini juga menerima objek Page dan Rectangle sebagai argumen, sehingga mungkin untuk memberikan nilai yang sama seperti yang ditentukan terhadap konstruktor LinkAnnotation.
- Menggunakan properti Contents objek [FreeTextAnnotation](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/freetextannotation), tentukan string yang harus ditampilkan di PDF keluaran.
- Opsional, atur lebar batas dari objek [LinkAnnotation](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/linkannotation) dan FreeTextAnnotation ke 0 sehingga tidak muncul di dokumen PDF.
- Setelah objek [LinkAnnotation](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/linkannotation) dan [FreeTextAnnotation](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/freetextannotation) didefinisikan, tambahkan tautan ini ke koleksi Annotations objek [Page](https://reference.aspose.com/pdf/net/aspose.pdf/page).
- Terakhir, simpan PDF yang diperbarui menggunakan metode [Save](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/save) dari objek [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document).

Potongan kode berikut menunjukkan cara menambahkan hyperlink ke file PDF.

{{< tabs tabID="1" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddHyperlink()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_LinksActions();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "AddHyperlink.pdf"))
    {
        // Get page
        var page = document.Pages[1];
        // Create Link annotation object
        var link = new Aspose.Pdf.Annotations.LinkAnnotation(page, new Aspose.Pdf.Rectangle(100, 100, 300, 300));
        // Create border object for LinkAnnotation
        var border = new Aspose.Pdf.Annotations.Border(link);
        // Set the border width value as 0
        border.Width = 0;
        // Set the border for LinkAnnotation
        link.Border = border;
        // Specify the link type as remote URI
        link.Action = new Aspose.Pdf.Annotations.GoToURIAction("www.aspose.com");
        // Add link annotation to annotations collection of first page of PDF file
        page.Annotations.Add(link);

        // Create Free Text annotation
        var textAnnotation = new Aspose.Pdf.Annotations.FreeTextAnnotation(document.Pages[1], new Aspose.Pdf.Rectangle(100, 100, 300, 300), new Aspose.Pdf.Annotations.DefaultAppearance(Aspose.Pdf.Text.FontRepository.FindFont("TimesNewRoman"), 10, System.Drawing.Color.Blue));
        // String to be added as Free text
        textAnnotation.Contents = "Link to Aspose website";
        // Set the border for Free Text Annotation
        textAnnotation.Border = border;
        // Add FreeText annotation to annotations collection of first page of Document
        document.Pages[1].Annotations.Add(textAnnotation);

        // Save PDF document
        document.Save(dataDir + "AddHyperlink_out.pdf");
    }
}
```
{{< /tab >}}

{{< tab tabNum="2" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddHyperlink()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_LinksActions();

    // Open PDF document
    using var document = new Aspose.Pdf.Document(dataDir + "AddHyperlink.pdf");
    // Get page
    var page = document.Pages[1];
    // Create Link annotation object
    var link = new Aspose.Pdf.Annotations.LinkAnnotation(page, new Aspose.Pdf.Rectangle(100, 100, 300, 300));
    // Create border object for LinkAnnotation
    var border = new Aspose.Pdf.Annotations.Border(link);
    // Set the border width value as 0
    border.Width = 0;
    // Set the border for LinkAnnotation
    link.Border = border;
    // Specify the link type as remote URI
    link.Action = new Aspose.Pdf.Annotations.GoToURIAction("www.aspose.com");
    // Add link annotation to annotations collection of first page of PDF file
    page.Annotations.Add(link);

    // Create Free Text annotation
    var textAnnotation = new Aspose.Pdf.Annotations.FreeTextAnnotation(document.Pages[1], new Aspose.Pdf.Rectangle(100, 100, 300, 300), new Aspose.Pdf.Annotations.DefaultAppearance(Aspose.Pdf.Text.FontRepository.FindFont("TimesNewRoman"), 10, System.Drawing.Color.Blue));
    // String to be added as Free text
    textAnnotation.Contents = "Link to Aspose website";
    // Set the border for Free Text Annotation
    textAnnotation.Border = border;
    // Add FreeText annotation to annotations collection of first page of Document
    document.Pages[1].Annotations.Add(textAnnotation);

    // Save PDF document
    document.Save(dataDir + "AddHyperlink_out.pdf");
}
```
{{< /tab >}}
{{< /tabs >}}

## Buat Hyperlink ke halaman di PDF yang sama

Aspose.PDF for .NET menyediakan fitur hebat untuk pembuatan PDF serta manipulasi. Ini juga menawarkan fitur untuk menambahkan tautan ke halaman PDF dan tautan dapat mengarahkan ke halaman di file PDF lain, URL web, tautan untuk meluncurkan Aplikasi atau bahkan tautan ke halaman di file PDF yang sama. Untuk menambahkan hyperlink lokal (tautan ke halaman di file PDF yang sama), sebuah kelas bernama [LocalHyperlink](https://reference.aspose.com/pdf/net/aspose.pdf/localhyperlink) ditambahkan ke namespace Aspose.PDF dan kelas ini memiliki properti bernama TargetPageNumber, yang digunakan untuk menentukan halaman target/tujuan untuk hyperlink.

Untuk menambahkan hyperlink lokal, kita perlu membuat TextFragment sehingga tautan dapat diasosiasikan dengan TextFragment. Kelas [TextFragment](https://reference.aspose.com/pdf/net/aspose.pdf.text/textfragment) memiliki properti bernama Hyperlink yang digunakan untuk mengasosiasikan instance LocalHyperlink. Potongan kode berikut menunjukkan langkah-langkah untuk memenuhi persyaratan ini.

{{< tabs tabID="2" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddHyperlink()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_LinksActions();

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        // Add page
        var page = document.Pages.Add();
        // Create Text Fragment instance
        var text = new Aspose.Pdf.Text.TextFragment("link page number test to page 7");
        // Create local hyperlink instance
        var link = new Aspose.Pdf.LocalHyperlink();
        // Set target page for link instance
        link.TargetPageNumber = 7;
        // Set TextFragment hyperlink
        text.Hyperlink = link;
        // Add text to paragraphs collection of Page
        page.Paragraphs.Add(text);
        // Create new TextFragment instance
        text = new Aspose.Pdf.Text.TextFragment("link page number test to page 1");
        // TextFragment should be added over new page
        text.IsInNewPage = true;
        // Create another local hyperlink instance
        link = new Aspose.Pdf.LocalHyperlink();
        // Set Target page for second hyperlink
        link.TargetPageNumber = 1;
        // Set link for second TextFragment
        text.Hyperlink = link;
        // Add text to paragraphs collection of page object
        page.Paragraphs.Add(text);

        // Save PDF document
        document.Save(dataDir + "CreateLocalHyperlink_out.pdf");
    }
}
```
{{< /tab >}}

{{< tab tabNum="2" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddHyperlink()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_LinksActions();

    // Create PDF document
    using var document = new Aspose.Pdf.Document();
    // Add page
    var page = document.Pages.Add();
    // Create Text Fragment instance
    var text = new Aspose.Pdf.Text.TextFragment("link page number test to page 7");
    // Create local hyperlink instance
    var link = new Aspose.Pdf.LocalHyperlink();
    // Set target page for link instance
    link.TargetPageNumber = 7;
    // Set TextFragment hyperlink
    text.Hyperlink = link;
    // Add text to paragraphs collection of Page
    page.Paragraphs.Add(text);
    // Create new TextFragment instance
    text = new Aspose.Pdf.Text.TextFragment("link page number test to page 1");
    // TextFragment should be added over new page
    text.IsInNewPage = true;
    // Create another local hyperlink instance
    link = new Aspose.Pdf.LocalHyperlink();
    // Set Target page for second hyperlink
    link.TargetPageNumber = 1;
    // Set link for second TextFragment
    text.Hyperlink = link;
    // Add text to paragraphs collection of page object
    page.Paragraphs.Add(text);

    // Save PDF document
    document.Save(dataDir + "CreateLocalHyperlink_out.pdf");
}
```
{{< /tab >}}
{{< /tabs >}}

## Dapatkan Tujuan Hyperlink PDF (URL)

Tautan direpresentasikan sebagai anotasi dalam file PDF dan mereka dapat ditambahkan, diperbarui, atau dihapus. Aspose.PDF for .NET juga mendukung mendapatkan tujuan (URL) dari hyperlink dalam file PDF.

Untuk mendapatkan URL tautan:

1. Buat objek [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document).
1. Dapatkan [Page](https://reference.aspose.com/pdf/net/aspose.pdf/page) yang ingin Anda ekstrak tautan darinya.
1. Gunakan kelas [AnnotationSelector](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/annotationselector) untuk mengekstrak semua objek [LinkAnnotation](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/linkannotation) dari halaman yang ditentukan.
1. Lewati objek [AnnotationSelector](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/annotationselector) ke metode Accept objek [Page](https://reference.aspose.com/pdf/net/aspose.pdf/page).
1. Dapatkan semua anotasi tautan yang dipilih ke dalam objek IList menggunakan properti Selected dari objek [AnnotationSelector](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/annotationselector).
1. Terakhir, ekstrak Aksi LinkAnnotation sebagai GoToURIAction.

Potongan kode berikut menunjukkan cara mendapatkan tujuan hyperlink (URL) dari file PDF.

{{< tabs tabID="3" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void GetHyperlink()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_LinksActions();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "input.pdf"))
    {
        // Traverse through all the page of PDF
        foreach (var page in document.Pages)
        {
            // Get the link annotations from particular page
            var selector = new Aspose.Pdf.Annotations.AnnotationSelector(new Aspose.Pdf.Annotations.LinkAnnotation(page, Aspose.Pdf.Rectangle.Trivial));

            page.Accept(selector);

            // Create list holding all the links
            var list = selector.Selected;

            // Iterate through individual item inside list
            foreach (var a in list)
            {
                // Print the destination URL
                Console.WriteLine("\nDestination: " + (a.Action as Aspose.Pdf.Annotations.GoToURIAction).URI + "\n");
            }
        }
    }
}
```
{{< /tab >}}

{{< tab tabNum="2" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void GetHyperlink()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_LinksActions();

    // Open PDF document
    using var document = new Aspose.Pdf.Document(dataDir + "input.pdf");

    // Traverse through all the page of PDF
    foreach (var page in document.Pages)
    {
        // Get the link annotations from particular page
        var selector = new Aspose.Pdf.Annotations.AnnotationSelector(new Aspose.Pdf.Annotations.LinkAnnotation(page, Aspose.Pdf.Rectangle.Trivial));

        page.Accept(selector);

        // Create list holding all the links
        var list = selector.Selected;

        // Iterate through individual item inside list
        foreach (var a in list)
        {
            // Print the destination URL
            Console.WriteLine("\nDestination: " + (a.Action as Aspose.Pdf.Annotations.GoToURIAction).URI + "\n");
        }
    }
}
```
{{< /tab >}}
{{< /tabs >}}

## Dapatkan Teks Hyperlink

Sebuah hyperlink memiliki dua bagian: teks yang ditampilkan dalam dokumen, dan URL tujuan. Dalam beberapa kasus, tekslah yang kita butuhkan daripada URL.

Teks dan anotasi/aksi dalam file PDF direpresentasikan oleh entitas yang berbeda. Teks di halaman hanyalah sekumpulan kata dan karakter, sementara anotasi membawa beberapa interaktivitas seperti yang melekat pada hyperlink.

Untuk menemukan konten URL, Anda perlu bekerja dengan anotasi dan teks. Objek [Annotation](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/annotation) tidak memiliki teks itu sendiri tetapi berada di bawah teks di halaman. Jadi untuk mendapatkan teks, Anotasi memberikan batas URL, sementara objek Teks memberikan konten URL. Silakan lihat potongan kode berikut.

{{< tabs tabID="4" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ShowLinkAnnotationText()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_LinksActions();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "input.pdf"))
    {
        // Iterate through each page of PDF
        foreach (var page in document.Pages)
        {
            // Show link annotation
            ShowLinkAnnotations(page);
        }
    }
}

private static void ShowLinkAnnotations(Aspose.Pdf.Page page)
{
    foreach (var annot in page.Annotations)
    {
        if (annot is Aspose.Pdf.Annotations.LinkAnnotation)
        {
            // Print the URL of each Link Annotation
            Console.WriteLine("URI: " + ((annot as Aspose.Pdf.Annotations.LinkAnnotation).Action as Aspose.Pdf.Annotations.GoToURIAction).URI);
            var absorber = new Aspose.Pdf.Text.TextAbsorber();
            absorber.TextSearchOptions.LimitToPageBounds = true;
            absorber.TextSearchOptions.Rectangle = annot.Rect;
            page.Accept(absorber);
            string extractedText = absorber.Text;
            // Print the text associated with hyperlink
            Console.WriteLine(extractedText);
        }
    }
}
```
{{< /tab >}}

{{< tab tabNum="2" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ShowLinkAnnotationText()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_LinksActions();

    // Open PDF document
    using var document = new Aspose.Pdf.Document(dataDir + "input.pdf");

    // Iterate through each page of PDF
    foreach (var page in document.Pages)
    {
        // Show link annotation
        ShowLinkAnnotations(page);
    }
}

private static void ShowLinkAnnotations(Aspose.Pdf.Page page)
{
    foreach (var annot in page.Annotations)
    {
        if (annot is Aspose.Pdf.Annotations.LinkAnnotation)
        {
            // Print the URL of each Link Annotation
            Console.WriteLine("URI: " + ((annot as Aspose.Pdf.Annotations.LinkAnnotation).Action as Aspose.Pdf.Annotations.GoToURIAction).URI);
            var absorber = new Aspose.Pdf.Text.TextAbsorber();
            absorber.TextSearchOptions.LimitToPageBounds = true;
            absorber.TextSearchOptions.Rectangle = annot.Rect;
            page.Accept(absorber);
            string extractedText = absorber.Text;
            // Print the text associated with hyperlink
            Console.WriteLine(extractedText);
        }
    }
}
```
{{< /tab >}}
{{< /tabs >}}

## Hapus Aksi Buka Dokumen dari File PDF

[Bagaimana Menentukan Halaman PDF saat Melihat Dokumen](#how-to-specify-pdf-page-when-viewing-document) menjelaskan bagaimana memberi tahu dokumen untuk dibuka di halaman yang berbeda dari halaman pertama. Ketika menggabungkan beberapa dokumen, dan satu atau lebih memiliki aksi GoTo yang diatur, Anda mungkin ingin menghapusnya. Misalnya, jika menggabungkan dua dokumen dan dokumen kedua memiliki aksi GoTo yang membawa Anda ke halaman kedua, dokumen keluaran akan terbuka di halaman kedua dari dokumen kedua alih-alih halaman pertama dari dokumen gabungan. Untuk menghindari perilaku ini, hapus perintah aksi buka.

Untuk menghapus aksi buka:

1. Atur properti [OpenAction](https://reference.aspose.com/pdf/net/aspose.pdf/document/properties/openaction) objek [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) ke null.
1. Simpan PDF yang diperbarui menggunakan metode [Save](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/save) dari objek Document.

Potongan kode berikut menunjukkan cara menghapus aksi buka dokumen dari file PDF.

{{< tabs tabID="5" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void RemoveOpenAction()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_LinksActions();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "RemoveOpenAction.pdf"))
    {
        // Remove document open action
        document.OpenAction = null;

        // Save PDF document
        document.Save(dataDir + "RemoveOpenAction_out.pdf");
    }
}
```
{{< /tab >}}

{{< tab tabNum="2" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void RemoveOpenAction()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_LinksActions();

    // Open PDF document
    using var document = new Aspose.Pdf.Document(dataDir + "RemoveOpenAction.pdf");

    // Remove document open action
    document.OpenAction = null;

    // Save PDF document
    document.Save(dataDir + "RemoveOpenAction_out.pdf");
}
```
{{< /tab >}}
{{< /tabs >}}

## Bagaimana Menentukan Halaman PDF saat Melihat Dokumen {#how-to-specify-pdf-page-when-viewing-document}

Saat melihat file PDF di penampil PDF seperti Adobe Reader, file biasanya terbuka di halaman pertama. Namun, adalah mungkin untuk mengatur file agar terbuka di halaman yang berbeda.

Kelas [XYZExplicitDestination](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/xyzexplicitdestination) memungkinkan Anda untuk menentukan halaman dalam file PDF yang ingin Anda buka. Saat melewatkan nilai objek GoToAction ke properti OpenAction kelas [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document), dokumen terbuka di halaman yang ditentukan terhadap objek XYZExplicitDestination. Potongan kode berikut menunjukkan cara menentukan halaman sebagai aksi buka dokumen.

{{< tabs tabID="6" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void SpecifyPage()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_LinksActions();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "SpecifyPageWhenViewing.pdf"))
    {
        // Get the instance of second page of document
        var page2 = document.Pages[2];
        // Create the variable to set the zoom factor of target page
        double zoom = 1;
        // Create GoToAction instance
        var action = new Aspose.Pdf.Annotations.GoToAction(document.Pages[2]);
        // Go to 2 page
        action.Destination = new Aspose.Pdf.Annotations.XYZExplicitDestination(page2, 0, page2.Rect.Height, zoom);
        // Set the document open action
        document.OpenAction = action;
        // Save PDF document
        document.Save(dataDir + "Goto2page_out.pdf");
    }
}
```
{{< /tab >}}

{{< tab tabNum="2" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void SpecifyPage()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_LinksActions();

    // Open PDF document
    using var document = new Aspose.Pdf.Document(dataDir + "SpecifyPageWhenViewing.pdf");
    // Get the instance of second page of document
    var page2 = document.Pages[2];
    // Create the variable to set the zoom factor of target page
    double zoom = 1;
    // Create GoToAction instance
    var action = new Aspose.Pdf.Annotations.GoToAction(document.Pages[2]);
    // Go to 2 page
    action.Destination = new Aspose.Pdf.Annotations.XYZExplicitDestination(page2, 0, page2.Rect.Height, zoom);
    // Set the document open action
    document.OpenAction = action;
    // Save PDF document
    document.Save(dataDir + "Goto2page_out.pdf");
}
```
{{< /tab >}}
{{< /tabs >}}

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