---
title: Bekerja dengan Formulir XFA
linktitle: Formulir XFA
type: docs
weight: 20
url: /id/net/xfa-forms/
description: Aspose.PDF untuk .NET API memungkinkan Anda bekerja dengan bidang XFA dan XFA Acroform dalam dokumen PDF. Aspose.PDF.Facades.
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Bekerja dengan Formulir XFA",
    "alternativeHeadline": "Mengisi, Mengonversi dan Mendapatkan Formulir XFA dalam PDF",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pembuatan dokumen pdf",
    "keywords": "pdf, c#, mengisi formulir xfa, mendapatkan formulir xfa, mengonversi formulir xfa",
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
    "url": "/net/xfa-forms/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/xfa-forms/"
    },
    "dateModified": "2022-02-04",
    "description": "Aspose.PDF untuk .NET API memungkinkan Anda bekerja dengan bidang XFA dan XFA Acroform dalam dokumen PDF. Aspose.PDF.Facades."
}
</script>
{{% alert color="primary" %}}

Formulir dinamis berdasarkan spesifikasi XML yang dikenal sebagai XFA, "XML Forms Architecture". Ini juga dapat mengonversi formulir XFA dinamis menjadi Acroform standar. Informasi tentang formulir (sejauh yang berkaitan dengan PDF) sangat samar – menyatakan bahwa bidang ada, dengan properti, dan peristiwa JavaScript, tetapi tidak menentukan rendering apa pun. Objek formulir XFA digambar pada saat memuat dokumen.

{{% /alert %}}

Kelas Form menyediakan kemampuan untuk menangani AcroForm statis dan Anda dapat memperoleh instance bidang tertentu menggunakan metode GetFieldFacade(..) dari kelas Form. Namun, bidang XFA tidak dapat diakses melalui metode Form.GetFieldFacade(..). Sebagai gantinya, gunakan [Document.Form.XFA](https://reference.aspose.com/pdf/net/aspose.pdf.forms/form/properties/xfa) untuk mendapatkan/mengatur nilai bidang dan memanipulasi template bidang XFA (mengatur properti bidang).

Potongan kode berikut juga bekerja dengan perpustakaan [Aspose.PDF.Drawing](/pdf/id/net/drawing/).

## Mengisi bidang XFA

Potongan kode berikut menunjukkan cara mengisi bidang dalam formulir XFA.
Potongan kode berikut menunjukkan cara mengisi bidang dalam formulir XFA.

```csharp
// Untuk contoh lengkap dan file data, silakan kunjungi https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Jalur ke direktori dokumen.
string dataDir = RunExamples.GetDataDir_AsposePdf_Forms();

// Muat formulir XFA
Document doc = new Document(dataDir + "FillXFAFields.pdf");

// Dapatkan nama-nama bidang formulir XFA
string[] names = doc.Form.XFA.FieldNames;

// Atur nilai bidang
doc.Form.XFA[names[0]] = "Field 0";
doc.Form.XFA[names[1]] = "Field 1";
dataDir = dataDir + "Filled_XFA_out.pdf";
// Simpan dokumen yang telah diperbarui
doc.Save(dataDir);
```

## Konversi XFA-ke-Acroform

{{% alert color="primary" %}}

Coba secara online
Anda dapat memeriksa kualitas konversi Aspose.PDF dan melihat hasilnya secara online di tautan ini: [products.aspose.app/pdf/xfa/](https://products.aspose.app/pdf/xfa/)

{{% /alert %}}

Formulir dinamis didasarkan pada spesifikasi XML yang dikenal sebagai XFA, "XML Forms Architecture".
Formulir dinamis didasarkan pada spesifikasi XML yang dikenal sebagai XFA, "Arsitektur Formulir XML".

Saat ini, PDF mendukung dua metode berbeda untuk mengintegrasikan data dan formulir PDF:

- AcroForms (juga dikenal sebagai formulir Acrobat), diperkenalkan dan termasuk dalam spesifikasi format PDF 1.2.
- Formulir Arsitektur Formulir XML Adobe (XFA), diperkenalkan dalam spesifikasi format PDF 1.5 sebagai fitur opsional (Spesifikasi XFA tidak termasuk dalam spesifikasi PDF, hanya dirujuk.)

Kita tidak dapat mengekstrak atau memanipulasi halaman Formulir XFA, karena konten formulir dihasilkan pada waktu runtime (selama penayangan formulir XFA) dalam aplikasi yang mencoba menampilkan atau merender formulir XFA. Aspose.PDF memiliki fitur yang memungkinkan pengembang untuk mengonversi formulir XFA menjadi AcroForms standar.

```csharp
// Untuk contoh lengkap dan file data, silakan kunjungi https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Jalur ke direktori dokumen.
string dataDir = RunExamples.GetDataDir_AsposePdf_Forms();

// Muat formulir XFA dinamis
Document document = new Document(dataDir + "DynamicXFAToAcroForm.pdf");

// Tetapkan tipe bidang formulir sebagai AcroForm standar
document.Form.Type = FormType.Standard;

dataDir = dataDir + "Standard_AcroForm_out.pdf";
// Simpan PDF hasilnya
document.Save(dataDir);
```
## Dapatkan Properti Bidang XFA

Untuk mengakses properti bidang, pertama gunakan Document.Form.XFA.Teamplate untuk mengakses template bidang. Potongan kode berikut menunjukkan langkah-langkah mendapatkan koordinat X dan Y dari bidang formulir XFA.

```csharp
// Untuk contoh lengkap dan file data, silakan kunjungi https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Jalur ke direktori dokumen.
string dataDir = RunExamples.GetDataDir_AsposePdf_Forms();

// Muat formulir XFA
Document doc = new Document(dataDir + "GetXFAProperties.pdf");

string[] names = doc.Form.XFA.FieldNames;

// Atur nilai bidang
doc.Form.XFA[names[0]] = "Field 0";
doc.Form.XFA[names[1]] = "Field 1";

// Dapatkan posisi bidang
Console.WriteLine(doc.Form.XFA.GetFieldTemplate(names[0]).Attributes["x"].Value);

// Dapatkan posisi bidang
Console.WriteLine(doc.Form.XFA.GetFieldTemplate(names[0]).Attributes["y"].Value);

dataDir = dataDir + "Filled_XFA_out.pdf";
// Simpan dokumen yang telah diperbarui
doc.Save(dataDir);
```

