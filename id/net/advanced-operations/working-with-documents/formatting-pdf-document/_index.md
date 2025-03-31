---
title: Memformat Dokumen PDF menggunakan C#
linktitle: Memformat Dokumen PDF
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 20
url: /id/net/formatting-pdf-document/
description: Buat dan format Dokumen PDF dengan Aspose.PDF for .NET. Gunakan cuplikan kode berikut untuk menyelesaikan tugas Anda.
lastmod: "2022-02-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Formatting Document using C#",
    "alternativeHeadline": "Enhance PDF Formatting with Aspose.PDF for .NET",
    "abstract": "Temukan fitur baru yang kuat dari Aspose.PDF for .NET yang memungkinkan pengguna untuk membuat dan memformat dokumen PDF dengan mudah. Dengan kontrol komprehensif atas properti dokumen seperti pengaturan tampilan jendela, opsi penyematan font, dan faktor zoom yang dapat disesuaikan, pengembang dapat meningkatkan pengalaman pengguna dan menjaga integritas dokumen di berbagai platform. Optimalkan tugas manipulasi PDF Anda dengan fungsionalitas yang kuat ini yang secara signifikan meningkatkan efisiensi aplikasi .NET Anda.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "keywords": "Formatting PDF Document, Aspose.PDF for .NET, PDF document properties, embed fonts, font substitution, set zoom factor, document window properties, PDF manipulation library, PDF document generation, C# PDF formatting",
    "wordcount": "2526",
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
    "url": "/net/formatting-pdf-document/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/formatting-pdf-document/"
    },
    "dateModified": "2024-11-25",
    "description": "Buat dan format Dokumen PDF dengan Aspose.PDF for .NET. Gunakan cuplikan kode berikut untuk menyelesaikan tugas Anda."
}
</script>

## Memformat Dokumen PDF

### Mendapatkan Properti Jendela Dokumen dan Tampilan Halaman

Topik ini membantu Anda memahami cara mendapatkan properti jendela dokumen, aplikasi penampil, dan cara halaman ditampilkan. Untuk mengatur properti ini:

Buka file PDF menggunakan kelas [Document](https://reference.aspose.com/pdf/id/net/aspose.pdf/document). Sekarang, Anda dapat mengatur properti objek Document, seperti

- CenterWindow – Pusatkan jendela dokumen di layar. Default: false.
- Direction – Urutan bacaan. Ini menentukan bagaimana halaman disusun saat ditampilkan berdampingan. Default: kiri ke kanan.
- DisplayDocTitle – Tampilkan judul dokumen di bilah judul jendela dokumen. Default: false (judul ditampilkan).
- HideMenuBar – Sembunyikan atau tampilkan bilah menu jendela dokumen. Default: false (bilah menu ditampilkan).
- HideToolBar – Sembunyikan atau tampilkan bilah alat jendela dokumen. Default: false (bilah alat ditampilkan).
- HideWindowUI – Sembunyikan atau tampilkan elemen jendela dokumen seperti bilah gulir. Default: false (elemen UI ditampilkan).
- NonFullScreenPageMode – Cara dokumen ditampilkan saat tidak ditampilkan dalam mode layar penuh.
- PageLayout – Tata letak halaman.
- PageMode – Cara dokumen ditampilkan saat pertama kali dibuka. Opsi yang tersedia adalah menampilkan thumbnail, layar penuh, menampilkan panel lampiran.

Cuplikan kode berikut juga bekerja dengan pustaka [Aspose.PDF.Drawing](/pdf/id/net/drawing/).

Cuplikan kode berikut menunjukkan cara mendapatkan properti menggunakan kelas [Document](https://reference.aspose.com/pdf/id/net/aspose.pdf/document).

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void GetDocumentWindowProperties()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "GetDocumentWindow.pdf"))
    {
        // Get different document properties
        // Position of document's window - Default: false
        Console.WriteLine("CenterWindow : {0}", document.CenterWindow);

        // Predominant reading order; determines the position of page
        // When displayed side by side - Default: L2R
        Console.WriteLine("Direction : {0}", document.Direction);

        // Whether window's title bar should display document title
        // If false, title bar displays PDF file name - Default: false
        Console.WriteLine("DisplayDocTitle : {0}", document.DisplayDocTitle);

        // Whether to resize the document's window to fit the size of
        // First displayed page - Default: false
        Console.WriteLine("FitWindow : {0}", document.FitWindow);

        // Whether to hide menu bar of the viewer application - Default: false
        Console.WriteLine("HideMenuBar : {0}", document.HideMenubar);

        // Whether to hide tool bar of the viewer application - Default: false
        Console.WriteLine("HideToolBar : {0}", document.HideToolBar);

        // Whether to hide UI elements like scroll bars
        // And leaving only the page contents displayed - Default: false
        Console.WriteLine("HideWindowUI : {0}", document.HideWindowUI);

        // Document's page mode. How to display document on exiting full-screen mode.
        Console.WriteLine("NonFullScreenPageMode : {0}", document.NonFullScreenPageMode);

        // The page layout i.e. single page, one column
        Console.WriteLine("PageLayout : {0}", document.PageLayout);

        // How the document should display when opened
        // I.e. show thumbnails, full-screen, show attachment panel
        Console.WriteLine("PageMode : {0}", document.PageMode);
    }
}
```

### Mengatur Properti Jendela Dokumen dan Tampilan Halaman

Topik ini menjelaskan cara mengatur properti jendela dokumen, aplikasi penampil, dan tampilan halaman. Untuk mengatur berbagai properti ini:

1. Buka file PDF menggunakan kelas [Document](https://reference.aspose.com/pdf/id/net/aspose.pdf/document).
1. Atur properti objek Document.
1. Simpan file PDF yang diperbarui menggunakan metode Save.

Properti yang tersedia adalah:

- CenterWindow.
- Direction.
- DisplayDocTitle.
- FitWindow.
- HideMenuBar.
- HideToolBar.
- HideWindowUI.
- NonFullScreenPageMode.
- PageLayout.
- PageMode.

Masing-masing digunakan dan dijelaskan dalam kode di bawah ini. Cuplikan kode berikut menunjukkan cara mengatur properti menggunakan kelas [Document](https://reference.aspose.com/pdf/id/net/aspose.pdf/document).

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void SetDocumentWindowProperties()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "SetDocumentWindow.pdf"))
    {
        // Set different document properties
        // Specify to position document's window - Default: false
        document.CenterWindow = true;

        // Predominant reading order; determines the position of page
        // When displayed side by side - Default: L2R
        document.Direction = Aspose.Pdf.Direction.R2L;

        // Specify whether window's title bar should display document title
        // If false, title bar displays PDF file name - Default: false
        document.DisplayDocTitle = true;

        // Specify whether to resize the document's window to fit the size of
        // First displayed page - Default: false
        document.FitWindow = true;

        // Specify whether to hide menu bar of the viewer application - Default: false
        document.HideMenubar = true;

        // Specify whether to hide tool bar of the viewer application - Default: false
        document.HideToolBar = true;

        // Specify whether to hide UI elements like scroll bars
        // And leaving only the page contents displayed - Default: false
        document.HideWindowUI = true;

        // Document's page mode. Specify how to display document on exiting full-screen mode.
        document.NonFullScreenPageMode = Aspose.Pdf.PageMode.UseOC;

        // Specify the page layout i.e. single page, one column
        document.PageLayout = Aspose.Pdf.PageLayout.TwoColumnLeft;

        // Specify how the document should display when opened
        // I.e. show thumbnails, full-screen, show attachment panel
        document.PageMode = Aspose.Pdf.PageMode.UseThumbs;

        // Save PDF document
        document.Save(dataDir + "SetDocumentWindow_out.pdf");
    }
}
```

### Menyematkan Font dalam file PDF yang ada

Pembaca PDF mendukung [inti 14 font](https://en.wikipedia.org/wiki/PDF#Text) sehingga dokumen dapat ditampilkan dengan cara yang sama terlepas dari platform tempat dokumen ditampilkan. Ketika sebuah PDF berisi font yang bukan salah satu dari 14 font inti, sematkan font ke file PDF untuk menghindari penggantian font.

Aspose.PDF for .NET mendukung penyematan font dalam file PDF yang ada. Anda dapat menyematkan font lengkap atau subset dari font. Untuk menyematkan font, buka file PDF menggunakan kelas [Document](https://reference.aspose.com/pdf/id/net/aspose.pdf/document). Kemudian gunakan kelas [Aspose.Pdf.Text.Font](https://reference.aspose.com/pdf/id/net/aspose.pdf.text) untuk menyematkan font ke dalam file PDF. Untuk menyematkan font lengkap, gunakan properti IsEmbeded dari kelas Font; untuk menggunakan subset dari font, gunakan properti IsSubset.

{{% alert color="primary" %}}

Sebuah subset font hanya menyematkan karakter yang digunakan dan berguna di mana font digunakan untuk kalimat pendek atau slogan, misalnya di mana font perusahaan digunakan untuk logo, tetapi tidak untuk teks tubuh. Menggunakan subset mengurangi ukuran file PDF keluaran. Namun, jika font kustom digunakan untuk teks tubuh, sematkan sepenuhnya.

{{% /alert %}}

Cuplikan kode berikut menunjukkan cara menyematkan font dalam file PDF.

### Menyematkan Font Tipe 1 Standar

Beberapa dokumen PDF memiliki font dari set font khusus Adobe. Font dari set ini disebut "Font Tipe 1 Standar". Set ini mencakup 14 font dan penyematan jenis font ini memerlukan penggunaan bendera khusus yaitu [Aspose.Pdf.Document.EmbedStandardFonts](https://reference.aspose.com/pdf/id/net/aspose.pdf/document/properties/embedstandardfonts). Berikut adalah cuplikan kode yang dapat digunakan untuk mendapatkan dokumen dengan semua font disematkan termasuk Font Tipe 1 Standar:

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void EmbedFontsType1ToPdf()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Text();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "input.pdf"))
    {
        // Set EmbedStandardFonts property of document
        document.EmbedStandardFonts = true;

        // Iterate through each page
        foreach (var page in document.Pages)
        {
            if (page.Resources.Fonts != null)
            {
                foreach (var pageFont in page.Resources.Fonts)
                {
                    // Check if font is already embedded
                    if (!pageFont.IsEmbedded)
                    {
                        pageFont.IsEmbedded = true;
                    }
                }
            }
        }

        // Save PDF document
        document.Save(dataDir + "EmbeddedFontsUpdated_out.pdf");
    }
}
```

### Menyematkan Font saat membuat PDF

Jika Anda perlu menggunakan font lain selain 14 font inti yang didukung oleh Adobe Reader, Anda harus menyematkan deskripsi font saat menghasilkan file PDF. Jika informasi font tidak disematkan, Adobe Reader akan mengambilnya dari Sistem Operasi jika terinstal di sistem, atau akan membangun font pengganti sesuai dengan deskriptor font dalam PDF.

> Harap dicatat bahwa font yang disematkan harus diinstal di mesin host yaitu, dalam kasus kode berikut font 'Univers Condensed' diinstal di sistem.

Kami menggunakan properti IsEmbedded dari kelas Font untuk menyematkan informasi font ke dalam file PDF. Mengatur nilai properti ini ke 'True' akan menyematkan file font lengkap ke dalam PDF, dengan mengetahui bahwa ini akan meningkatkan ukuran file PDF. Berikut adalah cuplikan kode yang dapat digunakan untuk menyematkan informasi font ke dalam PDF.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void EmbedFontWhileCreatingPdf()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        // Create a section in the Pdf object
        var page = document.Pages.Add();

        // Create a TextFragment
        var fragment = new Aspose.Pdf.Text.TextFragment("");

        // Create a TextSegment with sample text
        var segment = new Aspose.Pdf.Text.TextSegment(" This is a sample text using Custom font.");

        // Create and configure TextState
        var ts = new Aspose.Pdf.Text.TextState();
        ts.Font = Aspose.Pdf.Text.FontRepository.FindFont("Arial");
        ts.Font.IsEmbedded = true;
        segment.TextState = ts;

        // Add the segment to the fragment
        fragment.Segments.Add(segment);

        // Add the fragment to the page
        page.Paragraphs.Add(fragment);

        // Save PDF Document
        document.Save(dataDir + "EmbedFontWhileDocCreation_out.pdf");
    }
}
```

### Mengatur Nama Font Default saat Menyimpan PDF

Ketika dokumen PDF berisi font, yang tidak tersedia dalam dokumen itu sendiri dan di perangkat, API mengganti font ini dengan font default. Ketika font tersedia (diinstal di perangkat atau disematkan ke dalam dokumen), PDF keluaran harus memiliki font yang sama (tidak boleh diganti dengan font default). Nilai dari font default harus berisi nama font (bukan jalur ke file font). Kami telah menerapkan fitur untuk mengatur nama font default saat menyimpan dokumen sebagai PDF. Cuplikan kode berikut dapat digunakan untuk mengatur font default:

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void SetDefaultFontOnDocumentSave(string documentName, string newName)
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Open PDF document
    using (var fs = new FileStream(dataDir + "GetDocumentWindow.pdf", FileMode.Open))
    {
        using (var document = new Aspose.Pdf.Document(fs))
        {
            // Create PdfSaveOptions and specify Default Font Name
            var pdfSaveOptions = new Aspose.Pdf.PdfSaveOptions
            {
                DefaultFontName = newName
            };

            // Save PDF document
            document.Save(dataDir + "DefaultFont_out.pdf", pdfSaveOptions);
        }
    }
}
```

### Mendapatkan Semua Font dari Dokumen PDF

Jika Anda ingin mendapatkan semua font dari dokumen PDF, Anda dapat menggunakan metode FontUtilities.GetAllFonts() yang disediakan dalam kelas [Document](https://reference.aspose.com/pdf/id/net/aspose.pdf/document). Silakan periksa cuplikan kode berikut untuk mendapatkan semua font dari dokumen PDF yang ada:

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void GetAllFontsFromPdf()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "input.pdf"))
    {
        // Get all fonts used in the document
        var fonts = document.FontUtilities.GetAllFonts();

        // Iterate through each font and print its name
        foreach (var font in fonts)
        {
            Console.WriteLine(font.FontName);
        }
    }
}
```

### Mendapatkan Peringatan untuk Penggantian Font

Aspose.PDF for .NET menyediakan metode untuk mendapatkan notifikasi tentang penggantian font untuk menangani kasus penggantian font. Cuplikan kode di bawah ini menunjukkan cara menggunakan fungsionalitas yang sesuai.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void NotificationFontSubstitution()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "input.pdf"))
    {
        // Attach the FontSubstitution event handler
        document.FontSubstitution += OnFontSubstitution;
        // You can use lambda
        // (oldFont, newFont) => Console.WriteLine(string.Format("Font '{0}' was substituted with another font '{1}'",
        //                                                                        oldFont.FontName, newFont.FontName));

        // Save PDF document
        document.Save(dataDir + "NotificationFontSubstitution_out.pdf");
    }
}
```

Metode **OnFontSubstitution** adalah sebagai berikut.

```csharp
private static void OnFontSubstitution(Aspose.Pdf.Text.Font oldFont, Aspose.Pdf.Text.Font newFont)
{
    // Handle the font substitution event here
    Console.WriteLine(string.Format("Font '{0}' was substituted with another font '{1}'",
        oldFont.FontName, newFont.FontName));
}
```

### Meningkatkan Penyematan Font menggunakan FontSubsetStrategy

Fitur untuk menyematkan font sebagai subset dapat dicapai dengan menggunakan properti IsSubset, tetapi terkadang Anda ingin mengurangi set font yang sepenuhnya disematkan hanya menjadi subset yang digunakan dalam dokumen. Aspose.Pdf.Document memiliki properti FontUtilities yang mencakup metode SubsetFonts(FontSubsetStrategy subsetStrategy). Dalam metode SubsetFonts(), parameter subsetStrategy membantu menyetel strategi subset. FontSubsetStrategy mendukung dua varian berikut dari subsetting font.

- SubsetAllFonts - Ini akan menyubset semua font yang digunakan dalam dokumen.
- SubsetEmbeddedFontsOnly - Ini akan menyubset hanya font yang sepenuhnya disematkan ke dalam dokumen.

Cuplikan kode berikut menunjukkan cara mengatur FontSubsetStrategy:

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void SetFontSubsetStrategy()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "input.pdf"))
    {
        // All fonts will be embedded as subset into document in case of SubsetAllFonts.
        document.FontUtilities.SubsetFonts(Aspose.Pdf.FontSubsetStrategy.SubsetAllFonts);

        // Font subset will be embedded for fully embedded fonts but fonts which are not embedded into document will not be affected.
        document.FontUtilities.SubsetFonts(Aspose.Pdf.FontSubsetStrategy.SubsetEmbeddedFontsOnly);

        // Save PDF document
        document.Save(dataDir + "SetFontSubsetStrategy_out.pdf");
    }
}
```

### Mengatur-Faktor Zoom dari File PDF

Terkadang, Anda ingin menentukan apa faktor zoom saat ini dari dokumen PDF. Dengan Aspose.Pdf, Anda dapat mengetahui nilai saat ini serta mengatur satu.

Properti Destination dari kelas [GoToAction](https://reference.aspose.com/pdf/id/net/aspose.pdf.annotations/gotoaction) memungkinkan Anda untuk mendapatkan nilai zoom yang terkait dengan file PDF. Demikian pula, dapat digunakan untuk mengatur faktor zoom file.

#### Mengatur Faktor Zoom

Cuplikan kode berikut menunjukkan cara mengatur faktor zoom dari file PDF.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void SetZoomFactor()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "SetZoomFactor.pdf"))
    {
        // Create GoToAction with a specific zoom factor
        var action = new Aspose.Pdf.Annotations.GoToAction(new Aspose.Pdf.Annotations.XYZExplicitDestination(1, 0, 0, 0.5));
        document.OpenAction = action;

        // Save PDF document
        document.Save(dataDir + "ZoomFactor_out.pdf");
    }
}
```

#### Mendapatkan Faktor Zoom

Cuplikan kode berikut menunjukkan cara mendapatkan faktor zoom dari file PDF.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void GetZoomFactor()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "Zoomed_pdf.pdf"))
    {
        // Create GoToAction object
        if (document.OpenAction is Aspose.Pdf.Annotations.GoToAction action)
        {
            // Get the Zoom factor of PDF file
            if (action.Destination is Aspose.Pdf.Annotations.XYZExplicitDestination destination)
            {
                System.Console.WriteLine(destination.Zoom); // Document zoom value;
            }
        }
    }
}
```

### Mengatur Properti Preset Dialog Cetak

Aspose.PDF memungkinkan pengaturan properti Preset Dialog Cetak dari dokumen PDF. Ini memungkinkan Anda untuk mengubah properti DuplexMode untuk dokumen PDF yang diatur ke simplex secara default. Ini dapat dicapai menggunakan dua metodologi berbeda seperti yang ditunjukkan di bawah ini.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void SetPrintDialogPresetProperties()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        // Add page
        document.Pages.Add();

        // Set duplex printing to DuplexFlipLongEdge
        document.Duplex = Aspose.Pdf.PrintDuplex.DuplexFlipLongEdge;

        // Save PDF document
        document.Save(dataDir + "SetPrintDlgPresetProperties_out.pdf", Aspose.Pdf.SaveFormat.Pdf);
    }
}
```

### Mengatur Properti Preset Dialog Cetak menggunakan Editor Konten PDF

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void SetPrintDialogPresetPropertiesUsingPdfContentEditor()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    string inputFile = dataDir + "input.pdf";

    using (var ed = new Aspose.Pdf.Facades.PdfContentEditor())
    {
        // Bind PDF document
        ed.BindPdf(inputFile);

        // Check if the file has duplex flip short edge
        if ((ed.GetViewerPreference() & Aspose.Pdf.Facades.ViewerPreference.DuplexFlipShortEdge) > 0)
        {
            Console.WriteLine("The file has duplex flip short edge");
        }

        // Change the viewer preference to duplex flip short edge
        ed.ChangeViewerPreference(Aspose.Pdf.Facades.ViewerPreference.DuplexFlipShortEdge);

        // Save PDF document
        ed.Save(dataDir + "SetPrintDlgPropertiesUsingPdfContentEditor_out.pdf");
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