---
title: Modifing AcroForm
linktitle: Modifing AcroForm
type: docs
weight: 40
url: id/net/modifing-form/
description: Memodifikasi formulir dalam file PDF Anda dengan perpustakaan Aspose.PDF untuk .NET. Anda dapat menambahkan atau menghapus bidang dalam formulir yang ada, mendapatkan dan mengatur batas bidang, dan lainnya.
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Modifing AcroForm",
    "alternativeHeadline": "How to Modifing AcroForm",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "keywords": "pdf, c#, modifing acroform",
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
    "url": "/net/modifing-form/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/modifing-form/"
    },
    "dateModified": "2022-02-04",
    "description": "Memodifikasi formulir dalam file PDF Anda dengan perpustakaan Aspose.PDF untuk .NET. Anda dapat menambahkan atau menghapus bidang dalam formulir yang ada, mendapatkan dan mengatur batas bidang, dan lainnya."
}
</script>
Kode berikut juga berfungsi dengan pustaka [Aspose.PDF.Drawing](/pdf/net/drawing/).

## Dapatkan atau Atur Batas Bidang

Metode SetFieldLimit(field, limit) dari kelas FormEditor memungkinkan Anda untuk menetapkan batas bidang, jumlah maksimum karakter yang dapat dimasukkan ke dalam suatu bidang.

```csharp
// Untuk contoh lengkap dan berkas data, silakan kunjungi https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Jalur ke direktori dokumen.
string dataDir = RunExamples.GetDataDir_AsposePdf_Forms();

// Menambahkan Bidang dengan batas
FormEditor form = new FormEditor();

form.BindPdf(dataDir + "input.pdf");
form.SetFieldLimit("textbox1", 15);
dataDir = dataDir + "SetFieldLimit_out.pdf";
form.Save(dataDir);
```

Demikian pula, Aspose.PDF memiliki metode yang mendapatkan batas bidang menggunakan pendekatan DOM. Cuplikan kode berikut menunjukkan langkah-langkahnya.

```csharp
// Untuk contoh lengkap dan berkas data, silakan kunjungi https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Jalur ke direktori dokumen.
string dataDir = RunExamples.GetDataDir_AsposePdf_Forms();
// Mendapatkan batas maksimum bidang menggunakan DOM
Document doc = new Document(dataDir + "FieldLimit.pdf");
Console.WriteLine("Limit: " + (doc.Form["textbox1"] as TextBoxField).MaxLen);
```
Anda juga bisa mendapatkan nilai yang sama menggunakan namespace *Aspose.PDF.Facades* dengan menggunakan potongan kode berikut.

```csharp
// Untuk contoh lengkap dan file data, silakan kunjungi https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Jalur ke direktori dokumen.
string dataDir = RunExamples.GetDataDir_AsposePdf_Forms();
// Mendapatkan batas maksimum field menggunakan Facades
Aspose.Pdf.Facades.Form form = new Aspose.Pdf.Facades.Form();
form.BindPdf(dataDir + "FieldLimit.pdf");
Console.WriteLine("Limit: " + form.GetFieldLimit("textbox1"));
```

## Mengatur Font Kustom untuk Field Formulir

Field formulir dalam file Adobe PDF dapat dikonfigurasi untuk menggunakan font default tertentu.
Bidang formulir dalam file Adobe PDF dapat dikonfigurasi untuk menggunakan font default tertentu.

Berikut ini adalah potongan kode yang menunjukkan cara mengatur font default untuk bidang formulir PDF.

```csharp
// Untuk contoh lengkap dan file data, silakan kunjungi https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Jalur ke direktori dokumen.
string dataDir = RunExamples.GetDataDir_AsposePdf_Forms();

// Buka dokumen
Document pdfDocument = new Document(dataDir + "FormFieldFont14.pdf");

// Dapatkan bidang formulir tertentu dari dokumen
Aspose.Pdf.Forms.Field field = pdfDocument.Form["textbox1"] as Aspose.Pdf.Forms.Field;

// Buat objek font
Aspose.Pdf.Text.Font font = FontRepository.FindFont("ComicSansMS");

// Atur informasi font untuk bidang formulir
// Field.DefaultAppearance = new Aspose.Pdf.Forms.in.DefaultAppearance(font, 10, System.Drawing.Color.Black);

dataDir = dataDir + "FormFieldFont14_out.pdf";
// Simpan dokumen yang telah diperbarui
pdfDocument.Save(dataDir);
```

## Menambah/menghapus bidang dalam formulir yang ada

Semua bidang formulir terdapat dalam koleksi Form dari objek Dokumen.
Semua bidang formulir terkandung dalam koleksi Form dari objek Dokumen.

```csharp
// Untuk contoh lengkap dan berkas data, silakan kunjungi https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Jalur ke direktori dokumen.
string dataDir = RunExamples.GetDataDir_AsposePdf_Forms();

// Buka dokumen
Document pdfDocument = new Document(dataDir + "DeleteFormField.pdf");

// Hapus bidang tertentu dengan nama
pdfDocument.Form.Delete("textbox1");
dataDir = dataDir + "DeleteFormField_out.pdf";
// Simpan dokumen yang dimodifikasi
pdfDocument.Save(dataDir);
```

