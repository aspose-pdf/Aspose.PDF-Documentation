---
title: Working with Operators
linktitle: Working with Operators
type: docs
weight: 170
url: /id/net/operators/
description: Topik ini menjelaskan cara menggunakan operator dengan Aspose.PDF. Kelas operator menyediakan fitur hebat untuk manipulasi PDF.
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
aliases:
    - /net/working-with-operators/
    - /net/operator/
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Working with Operators",
    "alternativeHeadline": "How to use PDF operators",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "keywords": "pdf, c#, operators in pdf, use pdf operators",
    "wordcount": "302",
    "proficiencyLevel":"Beginner",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDF Doc Team",
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
    "url": "/net/operators/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/operators/"
    },
    "dateModified": "2022-02-04",
    "description": "Topik ini menjelaskan cara menggunakan operator dengan Aspose.PDF. Kelas operator menyediakan fitur hebat untuk manipulasi PDF."
}
</script>

## Pengenalan terhadap Operator PDF dan Penggunaannya

Operator adalah kata kunci PDF yang menentukan tindakan tertentu yang harus dilakukan, seperti melukis bentuk grafis di halaman. Kata kunci operator dibedakan dari objek bernama dengan tidak adanya karakter solidus awal (2Fh). Operator hanya bermakna di dalam aliran konten.

Aliran konten adalah objek aliran PDF yang datanya terdiri dari instruksi yang menggambarkan elemen grafis yang akan dilukis di halaman. Informasi lebih lanjut tentang operator PDF dapat ditemukan di [spesifikasi PDF](https://opensource.adobe.com/dc-acrobat-sdk-docs/).

### Detail Implementasi

Topik ini menjelaskan cara menggunakan operator dengan Aspose.PDF.
Topik ini menjelaskan cara menggunakan operator dengan Aspose.PDF.

- Operator **GSave** menyimpan keadaan grafis saat ini dari PDF.
- Operator **ConcatenateMatrix** (matriks konkatenasi) digunakan untuk menentukan bagaimana gambar harus diletakkan di halaman PDF.
- Operator **Do** menggambar gambar di halaman.
- Operator **GRestore** mengembalikan keadaan grafis.

Untuk menambahkan gambar ke dalam file PDF:

1. Buat objek [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) dan buka dokumen PDF yang diinginkan.
1. Dapatkan halaman tertentu yang akan ditambahkan gambar.
1. Tambahkan gambar ke dalam koleksi Sumber daya halaman.
1. Gunakan operator untuk meletakkan gambar di halaman:
   - Pertama, gunakan operator GSave untuk menyimpan keadaan grafis saat ini.
   - Kemudian gunakan operator ConcatenateMatrix untuk menentukan di mana gambar akan diletakkan.
   - Gunakan operator Do untuk menggambar gambar di halaman.
1. Akhirnya, gunakan operator GRestore untuk menyimpan keadaan grafis yang telah diperbarui.

Potongan kode berikut juga berfungsi dengan perpustakaan [Aspose.PDF.Drawing](/pdf/id/net/drawing/).
Kode berikut juga dapat bekerja dengan [Aspose.PDF.Drawing](/pdf/id/net/drawing/) library.

Kode berikut menunjukkan cara menggunakan operator PDF.

```csharp
// Untuk contoh lengkap dan file data, silakan kunjungi https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Jalur ke direktori dokumen.
string dataDir = RunExamples.GetDataDir_AsposePdf_Operators();

// Buka dokumen
Document pdfDocument = new Document(dataDir+ "PDFOperators.pdf");

// Atur koordinat
int lowerLeftX = 100;
int lowerLeftY = 100;
int upperRightX = 200;
int upperRightY = 200;

// Dapatkan halaman dimana gambar perlu ditambahkan
Page page = pdfDocument.Pages[1];
// Muat gambar ke dalam stream
FileStream imageStream = new FileStream(dataDir + "PDFOperators.jpg", FileMode.Open);
// Tambahkan gambar ke koleksi Gambar dari Sumber Daya Halaman
page.Resources.Images.Add(imageStream);
// Menggunakan operator GSave: operator ini menyimpan status grafis saat ini
page.Contents.Add(new Aspose.Pdf.Operators.GSave());
// Buat objek Rectangle dan Matrix
Aspose.Pdf.Rectangle rectangle = new Aspose.Pdf.Rectangle(lowerLeftX, lowerLeftY, upperRightX, upperRightY);
Matrix matrix = new Matrix(new double[] { rectangle.URX - rectangle.LLX, 0, 0, rectangle.URY - rectangle.LLY, rectangle.LLX, rectangle.LLY });
// Menggunakan ConcatenateMatrix (menggabungkan matriks) operator: mendefinisikan bagaimana gambar harus ditempatkan
page.Contents.Add(new Aspose.Pdf.Operators.ConcatenateMatrix(matrix));
XImage ximage = page.Resources.Images[page.Resources.Images.Count];
// Menggunakan operator Do: operator ini menggambar gambar
page.Contents.Add(new Aspose.Pdf.Operators.Do(ximage.Name));
// Menggunakan operator GRestore: operator ini mengembalikan status grafis
page.Contents.Add(new Aspose.Pdf.Operators.GRestore());
dataDir = dataDir + "PDFOperators_out.pdf";
// Simpan dokumen yang telah diperbarui
pdfDocument.Save(dataDir);
```
## Menggambar XForm pada Halaman menggunakan Operator

Topik ini menunjukkan cara menggunakan operator GSave/GRestore, operator ContatenateMatrix untuk memposisikan xForm dan operator Do untuk menggambar xForm di halaman.

Kode di bawah ini membungkus konten yang sudah ada di file PDF dengan pasangan operator GSave/GRestore. Pendekatan ini membantu mendapatkan keadaan grafis awal di akhir konten yang sudah ada. Tanpa pendekatan ini, transformasi yang tidak diinginkan mungkin tetap ada di akhir rantai operator yang ada.

```csharp
// Untuk contoh lengkap dan file data, silakan kunjungi https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Jalur ke direktori dokumen.
string dataDir = RunExamples.GetDataDir_AsposePdf_Operators();


string imageFile = dataDir+ "aspose-logo.jpg";
string inFile = dataDir + "DrawXFormOnPage.pdf";
string outFile = dataDir + "blank-sample2_out.pdf";

using (Document doc = new Document(inFile))
{
    OperatorCollection pageContents = doc.Pages[1].Contents;

    // Contoh ini menunjukkan
    // penggunaan operator GSave/GRestore
    // penggunaan operator ContatenateMatrix untuk memposisikan xForm
    // penggunaan operator Do untuk menggambar xForm di halaman

    // Membungkus konten yang ada dengan pasangan operator GSave/GRestore
    //        ini untuk mendapatkan keadaan grafis awal di akhir konten yang ada
    //        jika tidak, mungkin masih ada beberapa transformasi yang tidak diinginkan di akhir rantai operator yang ada
    pageContents.Insert(1, new Aspose.Pdf.Operators.GSave());
    pageContents.Add(new Aspose.Pdf.Operators.GRestore());

    // Tambahkan operator menyimpan keadaan grafis untuk benar-benar membersihkan keadaan grafis setelah perintah baru
    pageContents.Add(new Aspose.Pdf.Operators.GSave());

    #region create xForm

    // Buat xForm
    XForm form = XForm.CreateNewForm(doc.Pages[1], doc);
    doc.Pages[1].Resources.Forms.Add(form);
    form.Contents.Add(new Aspose.Pdf.Operators.GSave());
    // Tentukan lebar dan tinggi gambar
    form.Contents.Add(new Aspose.Pdf.Operators.ConcatenateMatrix(200, 0, 0, 200, 0, 0));
    // Muat gambar ke dalam stream
    Stream imageStream = new FileStream(imageFile, FileMode.Open);
    // Tambahkan gambar ke koleksi Gambar dari Sumber Daya XForm
    form.Resources.Images.Add(imageStream);
    XImage ximage = form.Resources.Images[form.Resources.Images.Count];
    // Menggunakan operator Do: operator ini menggambar gambar
    form.Contents.Add(new Aspose.Pdf.Operators.Do(ximage.Name));
    form.Contents.Add(new Aspose.Pdf.Operators.GRestore());

    #endregion

    pageContents.Add(new Aspose.Pdf.Operators.GSave());
    // Tempatkan formulir ke koordinat x=100 y=500
    pageContents.Add(new Aspose.Pdf.Operators.ConcatenateMatrix(1, 0, 0, 1, 100, 500));
    // Gambar formulir dengan operator Do
    pageContents.Add(new Aspose.Pdf.Operators.Do(form.Name));
    pageContents.Add(new Aspose.Pdf.Operators.GRestore());

    pageContents.Add(new Aspose.Pdf.Operators.GSave());
    // Tempatkan formulir ke koordinat x=100 y=300
    pageContents.Add(new Aspose.Pdf.Operators.ConcatenateMatrix(1, 0, 0, 1, 100, 300));
    // Gambar formulir dengan operator Do
    pageContents.Add(new Aspose.Pdf.Operators.Do(form.Name));
    pageContents.Add(new Aspose.Pdf.Operators.GRestore());

    // Kembalikan keadaan grafis dengan GRestore setelah GSave
    pageContents.Add(new Aspose.Pdf.Operators.GRestore());
    doc.Save(outFile);
}
```
## Menghapus Objek Grafis menggunakan Kelas Operator

Kelas operator menyediakan fitur hebat untuk manipulasi PDF. Ketika file PDF mengandung grafik yang tidak dapat dihapus menggunakan metode [DeleteImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor/methods/deleteimage) dari kelas [PdfContentEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor), kelas operator dapat digunakan sebagai alternatif untuk menghapusnya.

Potongan kode berikut menunjukkan cara menghapus grafik. Perlu dicatat bahwa jika file PDF mengandung label teks untuk grafis, label tersebut mungkin masih bertahan dalam file PDF, dengan menggunakan pendekatan ini. Oleh karena itu, cari operator grafik untuk metode alternatif dalam menghapus gambar tersebut.

```csharp
// Untuk contoh lengkap dan file data, silakan kunjungi https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Jalur ke direktori dokumen.
string dataDir = RunExamples.GetDataDir_AsposePdf_Operators();

Document doc = new Document(dataDir+ "RemoveGraphicsObjects.pdf");
Page page = doc.Pages[2];
OperatorCollection oc = page.Contents;

// Menggunakan operator pewarnaan jalur
Operator[] operators = new Operator[] {
        new Aspose.Pdf.Operators.Stroke(),
        new Aspose.Pdf.Operators.ClosePathStroke(),
        new Aspose.Pdf.Operators.Fill()
};

oc.Delete(operators);
doc.Save(dataDir+ "No_Graphics_out.pdf");
```

<script type="application/ld+json">
{
    "@context": "http://schema.org",
    "@type": "SoftwareApplication",
    "name": "Aspose.PDF untuk Perpustakaan .NET",
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
                "contactType": "penjualan",
                "areaServed": "AS",
                "availableLanguage": "Inggris"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+44 141 628 8900",
                "contactType": "penjualan",
                "areaServed": "Inggris Raya",
                "availableLanguage": "Inggris"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+61 2 8006 6987",
                "contactType": "penjualan",
                "areaServed": "Australia",
                "availableLanguage": "Inggris"
            }
        ]
    },
    "offers": {
        "@type": "Offer",
        "price": "1199",
        "priceCurrency": "USD"
    },
    "applicationCategory": "Perpustakaan Manipulasi PDF untuk .NET",
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
```

