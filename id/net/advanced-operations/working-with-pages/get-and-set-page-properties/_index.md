---
title: Dapatkan dan Atur Properti Halaman
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
url: /id/net/get-and-set-page-properties/
description: Pelajari cara mendapatkan dan mengatur properti halaman untuk dokumen PDF menggunakan Aspose.PDF for .NET, memungkinkan format dokumen yang disesuaikan.
lastmod: "2022-02-17"
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Get and Set Page Properties",
    "alternativeHeadline": "Manage PDF Page Properties with Ease",
    "abstract": "Fitur Dapatkan dan Atur Properti Halaman di Aspose.PDF for .NET memberdayakan pengembang untuk dengan mudah mengakses dan memanipulasi atribut halaman PDF. Fungsionalitas ini memungkinkan pengguna untuk mengambil informasi penting, seperti jumlah halaman dan properti spesifik seperti jenis warna, media box, dan trim box, semuanya hanya dengan beberapa baris kode. Tingkatkan kemampuan manajemen dokumen PDF Anda hari ini dengan memanfaatkan fitur kuat ini untuk manipulasi PDF yang efisien dalam aplikasi .NET",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "1117",
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
    "url": "/net/get-and-set-page-properties/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/get-and-set-page-properties/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF dapat melakukan tidak hanya tugas sederhana dan mudah tetapi juga mengatasi tujuan yang lebih kompleks. Periksa bagian berikut untuk pengguna dan pengembang tingkat lanjut."
}
</script>

Aspose.PDF for .NET memungkinkan Anda membaca dan mengatur properti halaman dalam file PDF di aplikasi .NET Anda. Bagian ini menunjukkan cara mendapatkan jumlah halaman dalam file PDF, mendapatkan informasi tentang properti halaman PDF seperti warna dan mengatur properti halaman. Contoh yang diberikan dalam C# tetapi Anda dapat menggunakan bahasa .NET lainnya seperti VB.NET untuk mencapai hal yang sama.

Potongan kode berikut juga bekerja dengan pustaka [Aspose.PDF.Drawing](/pdf/net/drawing/).

## Dapatkan Jumlah Halaman dalam File PDF

Saat bekerja dengan dokumen, Anda sering ingin tahu berapa banyak halaman yang mereka miliki. Dengan Aspose.PDF ini tidak memerlukan lebih dari dua baris kode.

Untuk mendapatkan jumlah halaman dalam file PDF:

1. Buka file PDF menggunakan kelas [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document).
1. Kemudian gunakan properti Count dari koleksi [PageCollection](https://reference.aspose.com/pdf/net/aspose.pdf/pagecollection) (dari objek Document) untuk mendapatkan total jumlah halaman dalam dokumen.

Potongan kode berikut menunjukkan cara mendapatkan jumlah halaman dari file PDF.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void GetNumberOfPagesInAPdfFile()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Pages();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "GetNumberofPages.pdf"))
    {
        // Get page count
        System.Console.WriteLine("Page Count : {0}", document.Pages.Count);
    }
}
```

### Dapatkan jumlah halaman tanpa menyimpan dokumen

Terkadang kita menghasilkan file PDF secara langsung dan selama pembuatan file PDF, kita mungkin menghadapi kebutuhan (membuat Daftar Isi, dll.) untuk mendapatkan jumlah halaman file PDF tanpa menyimpan file di sistem atau stream. Jadi untuk memenuhi kebutuhan ini, sebuah metode [ProcessParagraphs](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/processparagraphs) telah diperkenalkan dalam kelas Document. Silakan lihat potongan kode berikut yang menunjukkan langkah-langkah untuk mendapatkan jumlah halaman tanpa menyimpan dokumen.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void GetPageCountWithoutSavingTheDocument()
{
    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        // Add page
        var page = document.Pages.Add();
        // Create loop instance
        for (var i = 0; i < 300; i++)
        {
            // Add TextFragment to paragraphs collection of page object
            page.Paragraphs.Add(new Aspose.Pdf.Text.TextFragment("Pages count test"));
        }
        // Process the paragraphs in PDF file to get accurate page count
        document.ProcessParagraphs();
        // Print number of pages in document
        Console.WriteLine("Number of pages in document = " + document.Pages.Count);
    }
}
```

## Dapatkan Properti Halaman

Setiap halaman dalam file PDF memiliki sejumlah properti, seperti lebar, tinggi, bleed-, crop- dan trimbox. Aspose.PDF memungkinkan Anda mengakses properti ini.

### **Memahami Properti Halaman: Perbedaan antara Artbox, BleedBox, CropBox, MediaBox, TrimBox dan properti Rect**

- **Media box**: Media box adalah kotak halaman terbesar. Ini sesuai dengan ukuran halaman (misalnya A4, A5, US Letter, dll.) yang dipilih saat dokumen dicetak ke PostScript atau PDF. Dengan kata lain, media box menentukan ukuran fisik media di mana dokumen PDF ditampilkan atau dicetak.
- **Bleed box**: Jika dokumen memiliki bleed, PDF juga akan memiliki bleed box. Bleed adalah jumlah warna (atau karya seni) yang meluas di luar tepi halaman. Ini digunakan untuk memastikan bahwa ketika dokumen dicetak dan dipotong sesuai ukuran (“trimmed”), tinta akan sampai ke tepi halaman. Bahkan jika halaman dipotong tidak tepat - sedikit di luar tanda potong - tidak akan ada tepi putih yang muncul di halaman.
- **Trim box**: Trim box menunjukkan ukuran akhir dokumen setelah dicetak dan dipotong.
- **Art box**: Art box adalah kotak yang digambar di sekitar konten aktual halaman dalam dokumen Anda. Kotak halaman ini digunakan saat mengimpor dokumen PDF ke aplikasi lain.
- **Crop box**: Crop box adalah ukuran “halaman” di mana dokumen PDF Anda ditampilkan di Adobe Acrobat. Dalam tampilan normal, hanya konten dari crop box yang ditampilkan di Adobe Acrobat.
  Untuk deskripsi rinci tentang properti ini, baca spesifikasi Adobe.Pdf, khususnya 10.10.1 Batas Halaman.
- **Page.Rect**: irisan (umumnya persegi panjang yang terlihat) dari MediaBox dan DropBox. Gambar di bawah ini menggambarkan properti ini.

Untuk detail lebih lanjut, silakan kunjungi [halaman ini](http://www.enfocus.com/manuals/ReferenceGuide/PP/10/enUS/en-us/concept/c_aa1095731.html).

### **Mengakses Properti Halaman**

Kelas [Page](https://reference.aspose.com/pdf/net/aspose.pdf/page) menyediakan semua properti yang terkait dengan halaman PDF tertentu. Semua halaman dari file PDF terkandung dalam koleksi [PageCollection](https://reference.aspose.com/pdf/net/aspose.pdf/pagecollection) dari objek [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document).

Dari sana, dimungkinkan untuk mengakses objek Page individu menggunakan indeksnya, atau melakukan loop melalui koleksi, menggunakan loop foreach, untuk mendapatkan semua halaman. Setelah halaman individu diakses, kita dapat mendapatkan propertinya. Potongan kode berikut menunjukkan cara mendapatkan properti halaman.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AccessingPageProperties()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Pages();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "GetProperties.pdf"))
    {
        // Get page collection
        var pageCollection = document.Pages;
        // Get particular page
        var pdfPage = pageCollection[1];
        // Get page properties
        System.Console.WriteLine("ArtBox : Height={0},Width={1},LLX={2},LLY={3},URX={4},URY={5}", pdfPage.ArtBox.Height, pdfPage.ArtBox.Width, pdfPage.ArtBox.LLX,
            pdfPage.ArtBox.LLY, pdfPage.ArtBox.URX, pdfPage.ArtBox.URY);
        System.Console.WriteLine("BleedBox : Height={0},Width={1},LLX={2},LLY={3},URX={4},URY={5}", pdfPage.BleedBox.Height, pdfPage.BleedBox.Width, pdfPage.BleedBox.LLX,
            pdfPage.BleedBox.LLY, pdfPage.BleedBox.URX, pdfPage.BleedBox.URY);
        System.Console.WriteLine("CropBox : Height={0},Width={1},LLX={2},LLY={3},URX={4},URY={5}", pdfPage.CropBox.Height, pdfPage.CropBox.Width, pdfPage.CropBox.LLX,
            pdfPage.CropBox.LLY, pdfPage.CropBox.URX, pdfPage.CropBox.URY);
        System.Console.WriteLine("MediaBox : Height={0},Width={1},LLX={2},LLY={3},URX={4},URY={5}", pdfPage.MediaBox.Height, pdfPage.MediaBox.Width, pdfPage.MediaBox.LLX,
            pdfPage.MediaBox.LLY, pdfPage.MediaBox.URX, pdfPage.MediaBox.URY);
        System.Console.WriteLine("TrimBox : Height={0},Width={1},LLX={2},LLY={3},URX={4},URY={5}", pdfPage.TrimBox.Height, pdfPage.TrimBox.Width, pdfPage.TrimBox.LLX,
            pdfPage.TrimBox.LLY, pdfPage.TrimBox.URX, pdfPage.TrimBox.URY);
        System.Console.WriteLine("Rect : Height={0},Width={1},LLX={2},LLY={3},URX={4},URY={5}", pdfPage.Rect.Height, pdfPage.Rect.Width, pdfPage.Rect.LLX, pdfPage.Rect.LLY,
            pdfPage.Rect.URX, pdfPage.Rect.URY);
        System.Console.WriteLine("Page Number : {0}", pdfPage.Number);
        System.Console.WriteLine("Rotate : {0}", pdfPage.Rotate);
    }
}
```

## Dapatkan Halaman Tertentu dari File PDF

Aspose.PDF memungkinkan Anda [memisahkan PDF menjadi halaman individual](/pdf/net/split-pdf-document/) dan menyimpannya sebagai file PDF. Mendapatkan halaman tertentu dalam file PDF dan menyimpannya sebagai PDF baru adalah operasi yang sangat mirip: buka dokumen sumber, akses halaman, buat dokumen baru dan tambahkan halaman ke dokumen ini.

Koleksi [PageCollection](https://reference.aspose.com/pdf/net/aspose.pdf/pagecollection) dari objek [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) menyimpan halaman-halaman dalam file PDF. Untuk mendapatkan halaman tertentu dari koleksi ini:

1. Tentukan indeks halaman menggunakan properti Pages.
1. Buat objek [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) baru.
1. Tambahkan objek [Page](https://reference.aspose.com/pdf/net/aspose.pdf/page) ke objek [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) baru.
1. Simpan output menggunakan metode [Save](https://reference.aspose.com/pdf/net/aspose.pdf.document/save/methods/4).

Potongan kode berikut menunjukkan cara mendapatkan halaman tertentu dari file PDF dan menyimpannya sebagai file baru.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void GetAParticularPageOfThePdfFile()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Pages();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "input.pdf"))
    {
        // Get particular page
        var pdfPage = document.Pages[2];
        // Save the page as PDF file
        using (var newDocument = new Aspose.Pdf.Document())
        {
            newDocument.Pages.Add(pdfPage);
            // Save PDF document
            newDocument.Save(dataDir + "GetParticularPage_out.pdf");
        }
    }
}
```

## Tentukan Warna Halaman

Kelas [Page](https://reference.aspose.com/pdf/net/aspose.pdf/page) menyediakan properti yang terkait dengan halaman tertentu dalam dokumen PDF, termasuk jenis warna apa - RGB, hitam dan putih, grayscale atau tidak terdefinisi - yang digunakan halaman tersebut.

Semua halaman dari file PDF terkandung dalam koleksi [PageCollection](https://reference.aspose.com/pdf/net/aspose.pdf/pagecollection). Properti ColorType menentukan warna elemen di halaman. Untuk mendapatkan atau menentukan informasi warna untuk halaman PDF tertentu, gunakan properti [ColorType](https://reference.aspose.com/pdf/net/aspose.pdf/page/properties/colortype) dari objek [Page](https://reference.aspose.com/pdf/net/aspose.pdf/page).

Potongan kode berikut menunjukkan cara melakukan iterasi melalui halaman individu dari file PDF untuk mendapatkan informasi warna.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void DeterminePageColor()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Pages();
    
    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "input.pdf"))
    {
        // Iterate through all the page of PDF file
        for (var pageCount = 1; pageCount <= document.Pages.Count; pageCount++)
        {
            // Get the color type information for particular PDF page
            Aspose.Pdf.ColorType pageColorType = document.Pages[pageCount].ColorType;
            switch (pageColorType)
            {
                case Aspose.Pdf.ColorType.BlackAndWhite:
                    Console.WriteLine("Page # -" + pageCount + " is Black and white..");
                    break;
                case Aspose.Pdf.ColorType.Grayscale:
                    Console.WriteLine("Page # -" + pageCount + " is Gray Scale...");
                    break;
                case Aspose.Pdf.ColorType.Rgb:
                    Console.WriteLine("Page # -" + pageCount + " is RGB..", pageCount);
                    break;
                case Aspose.Pdf.ColorType.Undefined:
                    Console.WriteLine("Page # -" + pageCount + " Color is undefined..");
                    break;
            }
        }
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