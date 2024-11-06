---
title: Memotong Halaman PDF secara pemrograman C#
linktitle: Memotong Halaman
type: docs
weight: 80
url: id/net/crop-pages/
description: Anda dapat mendapatkan properti halaman, seperti lebar, tinggi, bleed-, crop- dan trimbox menggunakan Aspose.PDF untuk .NET.
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Memotong Halaman PDF secara pemrograman C#",
    "alternativeHeadline": "Cara memotong Halaman PDF di .NET",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pembuatan dokumen pdf",
    "keywords": "pdf, c#, memotong halaman pdf",
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
    "url": "/net/crop-pages/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/crop-pages/"
    },
    "dateModified": "2022-02-04",
    "description": "Anda dapat mendapatkan properti halaman, seperti lebar, tinggi, bleed-, crop- dan trimbox menggunakan Aspose.PDF untuk .NET."
}
</script>
## Dapatkan Properti Halaman

Setiap halaman dalam file PDF memiliki sejumlah properti, seperti lebar, tinggi, kotak pemotong, kotak pemangkasan, dan kotak pemotongan. Aspose.PDF memungkinkan Anda untuk mengakses properti-properti ini.

- **Kotak media**: Kotak media adalah kotak halaman terbesar. Ini sesuai dengan ukuran halaman (misalnya A4, A5, Surat AS, dll.) yang dipilih ketika dokumen dicetak ke PostScript atau PDF. Dengan kata lain, kotak media menentukan ukuran fisik media tempat dokumen PDF ditampilkan atau dicetak.
- **Kotak pemotongan**: Jika dokumen memiliki pemotongan, PDF juga akan memiliki kotak pemotongan. Pemotongan adalah jumlah warna (atau karya seni) yang melampaui tepi halaman. Ini digunakan untuk memastikan bahwa ketika dokumen dicetak dan dipotong menjadi ukuran ("dipangkas"), tinta akan sampai ke tepi halaman. Bahkan jika halaman dipotong sedikit dari tanda pemotongan - tidak ada tepi putih yang akan muncul di halaman.
- **Kotak pemangkasan**: Kotak pemangkasan menunjukkan ukuran akhir dokumen setelah dicetak dan dipangkas.
- **Kotak seni**: Kotak seni adalah kotak yang digambar di sekitar konten sebenarnya dari halaman dalam dokumen Anda.
- **Kotak Seni**: Kotak Seni adalah kotak yang digambar mengelilingi konten sebenarnya dari halaman dalam dokumen Anda.
- **Kotak Pemotong**: Kotak Pemotong adalah "ukuran halaman" di mana dokumen PDF Anda ditampilkan di Adobe Acrobat. Dalam tampilan normal, hanya konten dari kotak pemotong yang ditampilkan di Adobe Acrobat. Untuk deskripsi rinci tentang properti ini, baca spesifikasi Adobe.Pdf, terutama 10.10.1 Batas Halaman.
- **Page.Rect**: perpotongan (persegi panjang yang umumnya terlihat) dari MediaBox dan DropBox. Gambar di bawah ini mengilustrasikan properti ini.
Untuk detail lebih lanjut, silakan kunjungi [halaman ini](http://www.enfocus.com/manuals/ReferenceGuide/PP/10/enUS/en-us/concept/c_aa1095731.html).

Potongan kode berikut juga bekerja dengan pustaka [Aspose.PDF.Drawing](/pdf/net/drawing/).

Potongan di bawah ini menunjukkan cara memotong halaman:

```csharp
public static void CropPagesPDF()
{
    var pdfDocument1 = new Aspose.Pdf.Document("crop_page.pdf");
    Console.WriteLine(pdfDocument1.Pages[1].CropBox);
    Console.WriteLine(pdfDocument1.Pages[1].TrimBox);
    Console.WriteLine(pdfDocument1.Pages[1].ArtBox);
    Console.WriteLine(pdfDocument1.Pages[1].BleedBox);
    Console.WriteLine(pdfDocument1.Pages[1].MediaBox);

    // Membuat Kotak Persegi Baru
    var newBox = new Rectangle(200, 220, 2170, 1520);
    pdfDocument1.Pages[1].CropBox = newBox;
    pdfDocument1.Pages[1].TrimBox = newBox;
    pdfDocument1.Pages[1].ArtBox = newBox;
    pdfDocument1.Pages[1].BleedBox = newBox;
   
    pdfDocument1.Save("crop_page_modified.pdf");           
}
```
Dalam contoh ini kami menggunakan file contoh [di sini](crop_page.pdf). Awalnya halaman kami terlihat seperti yang ditampilkan pada Gambar 1.
![Gambar 1. Halaman yang Dipotong](crop_page.png)

Setelah perubahan, halaman akan terlihat seperti Gambar 2.
![Gambar 2. Halaman yang Dipotong](crop_page2.png)
Of course, I can help translate the document into Bahasa Indonesia. However, you need to provide the content of the document you want to translate. Please paste the text here so I can assist you further.
