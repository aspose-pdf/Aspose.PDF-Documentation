---
title: Update Links in PDF
linktitle: Update Links
type: docs
weight: 20
url: /net/update-links/
description: Memperbarui tautan dalam PDF secara pemrograman. Panduan ini adalah tentang cara memperbarui tautan dalam PDF dalam bahasa C#.
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Update Links in PDF",
    "alternativeHeadline": "How to update Links in PDF",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "keywords": "pdf, c#, update link in pdf",
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
    "url": "/net/update-links/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/update-links/"
    },
    "dateModified": "2022-02-04",
    "description": "Memperbarui tautan dalam PDF secara pemrograman. Panduan ini adalah tentang cara memperbarui tautan dalam PDF dalam bahasa C#."
}
</script>
Potongan kode berikut ini juga berfungsi dengan perpustakaan [Aspose.PDF.Drawing](/pdf/net/drawing/).

## Perbarui Tautan dalam File PDF

Seperti yang dibahas dalam Menambahkan Hyperlink dalam File PDF, kelas [LinkAnnotation](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/linkannotation) memungkinkan penambahan tautan dalam file PDF. Ada juga kelas serupa yang digunakan untuk mendapatkan tautan yang ada dari dalam file PDF. Gunakan ini jika Anda perlu memperbarui tautan yang sudah ada. Untuk memperbarui tautan yang ada:

1. Muat file PDF.
1. Pergi ke halaman tertentu dalam file PDF.
1. Tentukan tujuan tautan menggunakan properti Destination dari objek [GoToAction](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/gotoaction).
1. Halaman tujuan ditentukan menggunakan konstruktor [XYZExplicitDestination](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/xyzexplicitdestination).

### Atur Target Tautan ke Halaman di Dokumen yang Sama

Potongan kode berikut menunjukkan cara memperbarui tautan dalam file PDF dan menetapkan targetnya ke halaman kedua dari dokumen.
Potongan kode berikut ini menunjukkan cara memperbarui tautan dalam file PDF dan mengatur targetnya ke halaman kedua dokumen.

```csharp
// Untuk contoh lengkap dan file data, silakan kunjungi https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Jalur ke direktori dokumen.
string dataDir = RunExamples.GetDataDir_AsposePdf_LinksActions();
// Memuat file PDF
Document doc = new Document(dataDir + "UpdateLinks.pdf");
// Dapatkan anotasi tautan pertama dari halaman pertama dokumen
LinkAnnotation linkAnnot = (LinkAnnotation)doc.Pages[1].Annotations[1];
// Modifikasi tautan: mengubah tujuan tautan
GoToAction goToAction = (GoToAction)linkAnnot.Action;
// Tentukan tujuan untuk objek tautan
// Parameter pertama adalah objek dokumen, kedua adalah nomor halaman tujuan.
// Argumen kelima adalah faktor zoom saat menampilkan halaman yang bersangkutan. Saat menggunakan 2, halaman akan ditampilkan dalam zoom 200%
goToAction.Destination = new Aspose.Pdf.Annotations.XYZExplicitDestination(1, 1, 2, 2);
dataDir = dataDir + "PDFLINK_Modified_UpdateLinks_out.pdf";
// Simpan dokumen dengan tautan yang diperbarui
doc.Save(dataDir);
```
### Tetapkan Tujuan Tautan ke Alamat Web

Untuk memperbarui hyperlink agar mengarah ke alamat web, instansiasi objek [GoToURIAction](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/gotouriaction) dan berikan ke properti Action dari LinkAnnotation. Cuplikan kode berikut menunjukkan cara memperbarui tautan dalam file PDF dan mengatur targetnya ke alamat web.

```csharp
// Untuk contoh lengkap dan file data, silakan kunjungi https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Jalur ke direktori dokumen.
string dataDir = RunExamples.GetDataDir_AsposePdf_LinksActions();
// Muat file PDF
Document doc = new Document(dataDir + "UpdateLinks.pdf");

// Dapatkan anotasi tautan pertama dari halaman pertama dokumen
LinkAnnotation linkAnnot = (LinkAnnotation)doc.Pages[1].Annotations[1];
// Modifikasi tautan: ubah aksi tautan dan tetapkan target sebagai alamat web
linkAnnot.Action = new GoToURIAction("www.aspose.com");

dataDir = dataDir + "SetDestinationLink_out.pdf";
// Simpan dokumen dengan tautan yang diperbarui
doc.Save(dataDir);
```
### Mengatur Target Tautan ke File PDF Lain

Berikut ini adalah potongan kode yang menunjukkan bagaimana memperbarui tautan dalam file PDF dan mengatur targetnya ke file PDF lain.

```csharp
// Untuk contoh lengkap dan file data, silakan kunjungi https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Jalur ke direktori dokumen.
string dataDir = RunExamples.GetDataDir_AsposePdf_LinksActions();
// Muat file PDF
Document document = new Document(dataDir + "UpdateLinks.pdf");

LinkAnnotation linkAnnot = (LinkAnnotation)document.Pages[1].Annotations[1];

GoToRemoteAction goToR = (GoToRemoteAction)linkAnnot.Action;
// Baris berikut memperbarui destinasi, tidak memperbarui file
goToR.Destination = new XYZExplicitDestination(2, 0, 0, 1.5);
// Baris berikut memperbarui file
goToR.File = new FileSpecification(dataDir +  "input.pdf");

dataDir = dataDir + "SetTargetLink_out.pdf";
// Simpan dokumen dengan tautan yang diperbarui
document.Save(dataDir);
```

### Memperbarui Warna Teks LinkAnnotation

Anotasi tautan tidak mengandung teks.
Anotasi tautan tidak mengandung teks.

```csharp
// Untuk contoh lengkap dan file data, silakan kunjungi https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Jalur ke direktori dokumen.
string dataDir = RunExamples.GetDataDir_AsposePdf_LinksActions();
// Muat file PDF
Document doc = new Document(dataDir + "UpdateLinks.pdf");
foreach (Annotation annotation in doc.Pages[1].Annotations)
{
    if (annotation is LinkAnnotation)
    {
        // Mencari teks di bawah anotasi
        TextFragmentAbsorber ta = new TextFragmentAbsorber();
        Rectangle rect = annotation.Rect;
        rect.LLX -= 10;
        rect.LLY -= 10;
        rect.URX += 10;
        rect.URY += 10;
        ta.TextSearchOptions = new TextSearchOptions(rect);
        ta.Visit(doc.Pages[1]);
        // Mengubah warna teks.
        foreach (TextFragment tf in ta.TextFragments)
        {
            tf.TextState.ForegroundColor = Color.Red;
        }
    }

}
dataDir = dataDir + "UpdateLinkTextColor_out.pdf";
// Simpan dokumen dengan tautan yang diperbarui
doc.Save(dataDir);
```

<script type="application/ld+json">
{
    "@context": "http://schema.org",
    "@type": "SoftwareApplication",
    "name": "Aspose.PDF untuk Pustaka .NET",
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
    "applicationCategory": "Pustaka Manipulasi PDF untuk .NET",
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

