---
title: Ekstrak AcroForm - Ekstrak Data Formulir dari PDF di C#
linktitle: Ekstrak AcroForm
type: docs
weight: 30
url: /net/extract-form/
keywords: extract form data from pdf c#
description: Ekstrak formulir dari dokumen PDF Anda dengan perpustakaan Aspose.PDF untuk .NET. Dapatkan nilai dari bidang individu file PDF.
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Extract AcroForm",
    "alternativeHeadline": "Cara mengekstrak AcroForm dari PDF",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pembuatan dokumen pdf",
    "keywords": "pdf, c#, ekstrak acroform",
    "wordcount": "302",
    "proficiencyLevel":"Pemula",
    "publisher": {
        "@type": "Organization",
        "name": "Tim Dok Aspose.PDF",
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
                "areaServed": "US",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+44 141 628 8900",
                "contactType": "penjualan",
                "areaServed": "GB",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+61 2 8006 6987",
                "contactType": "penjualan",
                "areaServed": "AU",
                "availableLanguage": "en"
            }
        ]
    },
    "url": "/net/extract-form/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/extract-form/"
    },
    "dateModified": "2022-02-04",
    "description": "Ekstrak formulir dari dokumen PDF Anda dengan perpustakaan Aspose.PDF untuk .NET. Dapatkan nilai dari bidang individu file PDF."
}
</script>
Kode snippet berikut juga berfungsi dengan perpustakaan [Aspose.PDF.Drawing](/pdf/net/drawing/).

## Ekstrak data dari formulir

### Dapatkan Nilai dari Semua Bidang Dokumen PDF

Untuk mendapatkan nilai dari semua bidang dalam dokumen PDF, Anda perlu menavigasi melalui semua bidang formulir dan kemudian mendapatkan nilai menggunakan properti Value. Dapatkan setiap bidang dari koleksi Form, dalam tipe bidang dasar yang disebut Field dan akses properti Valuenya.

Snippet kode C# berikut menunjukkan cara mendapatkan nilai dari semua bidang dalam dokumen PDF.

```csharp
// Untuk contoh lengkap dan file data, silakan kunjungi https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Jalur ke direktori dokumen.
string dataDir = RunExamples.GetDataDir_AsposePdf_Forms();

// Buka dokumen
Document pdfDocument = new Document(dataDir + "GetValuesFromAllFields.pdf");

// Dapatkan nilai dari semua bidang
foreach (Field formField in pdfDocument.Form)
{
    Console.WriteLine("Nama Bidang : {0} ", formField.PartialName);
    Console.WriteLine("Nilai : {0} ", formField.Value);
}
```
### Mendapatkan Nilai dari Satu Bidang Dokumen PDF

Properti Value dari bidang formulir memungkinkan Anda untuk mendapatkan nilai dari bidang tertentu. Untuk mendapatkan nilai, dapatkan bidang formulir dari koleksi Form objek Document. Contoh C# ini memilih [TextBoxField](https://reference.aspose.com/pdf/net/aspose.pdf.forms/textboxfield) dan mengambil nilainya menggunakan properti Value.

```csharp
// Untuk contoh lengkap dan file data, silakan kunjungi https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Jalur ke direktori dokumen.
string dataDir = RunExamples.GetDataDir_AsposePdf_Forms();

// Buka dokumen
Document pdfDocument = new Document(dataDir + "GetValueFromField.pdf");

// Dapatkan bidang
TextBoxField textBoxField = pdfDocument.Form["textbox1"] sebagai TextBoxField;

// Dapatkan nilai bidang
Console.WriteLine("PartialName : {0} ", textBoxField.PartialName);
Console.WriteLine("Value : {0} ", textBoxField.Value);
```

Untuk mendapatkan URL tombol submit, gunakan baris kode berikut.

```csharp
// Untuk contoh lengkap dan file data, silakan kunjungi https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Jalur ke direktori dokumen.
string dataDir = RunExamples.GetDataDir_AsposePdf_Forms();

// Buka dokumen
Document pdfDocument = new Document(dataDir + "GetValueFromField.pdf");
SubmitFormAction act = pdfDocument.Form[1].OnActivated sebagai SubmitFormAction;
if(act != null)
Console.WriteLine(act.Url.Name);
```
### Dapatkan Bidang Formulir dari Wilayah Tertentu di File PDF

Terkadang, Anda mungkin tahu di mana dalam dokumen terdapat bidang formulir, tetapi tidak tahu namanya. Misalnya, jika yang Anda miliki hanyalah skema formulir cetak. Dengan Aspose.PDF untuk .NET, ini bukan masalah. Anda dapat mengetahui bidang apa saja yang ada di wilayah tertentu dari file PDF. Untuk mendapatkan bidang formulir dari wilayah tertentu di file PDF:

1. Buka file PDF menggunakan objek [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document).
1. Dapatkan formulir dari koleksi Forms dokumen.
1. Tentukan wilayah persegi panjang dan lewatkan ke metode GetFieldsInRect objek Form. Koleksi Fields dikembalikan.
1. Gunakan ini untuk memanipulasi bidang.

Potongan kode C# berikut menunjukkan cara mendapatkan bidang formulir di wilayah persegi panjang tertentu dari file PDF.

```csharp
// Untuk contoh lengkap dan file data, silakan kunjungi https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Jalur ke direktori dokumen.
string dataDir = RunExamples.GetDataDir_AsposePdf_Forms();

// Buka file pdf
Aspose.Pdf.Document doc = new Aspose.Pdf.Document(dataDir + "GetFieldsFromRegion.pdf");

// Buat objek persegi panjang untuk mendapatkan bidang di area tersebut
Aspose.Pdf.Rectangle rectangle = new Aspose.Pdf.Rectangle(35, 30, 500, 500);

// Dapatkan formulir PDF
Aspose.Pdf.Forms.Form form = doc.Form;

// Dapatkan bidang di area persegi panjang
Aspose.Pdf.Forms.Field[] fields = form.GetFieldsInRect(rectangle);

// Tampilkan nama dan nilai Field
foreach (Field field in fields)
{
    // Tampilkan properti penempatan gambar untuk semua penempatan
    Console.Out.WriteLine("Nama Bidang: " + field.FullName + "-" + "Nilai Bidang: " + field.Value);
}
```

<script type="application/ld+json">
{
    "@context": "http://schema.org",
    "@type": "SoftwareApplication",
    "name": "Perpustakaan Aspose.PDF untuk .NET",
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
                "areaServed": "US",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+44 141 628 8900",
                "contactType": "penjualan",
                "areaServed": "GB",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+61 2 8006 6987",
                "contactType": "penjualan",
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

