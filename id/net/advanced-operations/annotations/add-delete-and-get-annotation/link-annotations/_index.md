---
title: Menggunakan Anotasi Tautan dalam PDF
linktitle: Anotasi Tautan
type: docs
weight: 70
url: id/net/link-annotations/
description: Aspose.PDF untuk .NET memungkinkan Anda untuk Menambahkan, Mendapatkan, dan Menghapus Anotasi Tautan dari dokumen PDF Anda.
lastmod: "2024-07-28"
sitemap:
    changefreq: "monthly"
    priority: 0.5
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Menggunakan Anotasi Tautan untuk PDF",
    "alternativeHeadline": "Cara menambahkan Anotasi Tautan dalam PDF",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pembuatan dokumen pdf",
    "keywords": "pdf, c#, anotasi teks",
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
    "url": "/net/link-annotation/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/link-annotation/"
    },
    "dateModified": "2022-02-04",
    "description": "Aspose.PDF untuk .NET memungkinkan Anda untuk Menambahkan, Mendapatkan, dan Menghapus Anotasi Teks dari dokumen PDF Anda."
}
</script>

## Menambahkan Anotasi Tautan ke dalam file PDF yang ada

> Cuplikan kode berikut juga bisa digunakan dengan pustaka [Aspose.PDF.Drawing](/pdf/net/drawing/).

Anotasi [Tautan](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/linkannotation) mewakili hyperlink, tujuan lain, dan dokumen. Menurut Standar PDF, anotasi tautan dapat digunakan dalam tiga kasus: membuka tampilan halaman, membuka file, dan membuka halaman web.

### Menggunakan Anotasi Tautan untuk membuka tampilan halaman

Beberapa langkah tambahan dilakukan untuk membuat anotasi. Kami menggunakan 2 TextFragmentAbsorbers untuk menemukan fragmen untuk demo. Yang pertama adalah untuk teks anotasi tautan, dan yang kedua menunjukkan beberapa tempat dalam dokumen.

```cs
Document document = new Document(System.IO.Path.Combine(_dataDir, "Link Annotation Demo.pdf"));

var page = document.Pages[1];

var regEx = new Regex(@"Link Annotation Demo \d");
TextFragmentAbsorber textFragmentAbsorber1 = new TextFragmentAbsorber(regEx);
textFragmentAbsorber1.Visit(document);

regEx = new Regex(@"Sample text \d");
TextFragmentAbsorber textFragmentAbsorber2 = new TextFragmentAbsorber(regEx);
textFragmentAbsorber2.Visit(document);

var linkFragments = textFragmentAbsorber1.TextFragments;
var sampleTextFragments = textFragmentAbsorber2.TextFragments;

var linkAnnotation1 = new LinkAnnotation(page, linkFragments[1].Rectangle)
{
    Action = new GoToAction(
        new XYZExplicitDestination(
            sampleTextFragments[1].Page,
            sampleTextFragments[1].Rectangle.LLX,
            sampleTextFragments[1].Rectangle.URX, 1.5))
};

page.Annotations.Add(linkAnnotation1);

document.Save("test.pdf");
```
Untuk membuat anotasi kami telah mengikuti beberapa langkah:

1. Buat `LinkAnnotation` dan berikan objek halaman serta persegi panjang fragmen teks yang sesuai dengan anotasi.
1. Atur `Action` sebagai `GoToAction` dan berikan `XYZExplicitDestination` sebagai tujuan yang diinginkan. Kami membuat `XYZExplicitDestination` berdasarkan halaman, koordinat kiri dan atas serta zoom.
1. Tambahkan anotasi ke koleksi anotasi halaman.
1. Simpan dokumen

### Menggunakan Link Annotation dengan tujuan yang dinamai

Ketika memproses berbagai dokumen, situasi muncul ketika Anda mengetik dan tidak tahu kemana anotasi akan menunjuk.
Dalam kasus ini Anda dapat menggunakan tujuan khusus (yang dinamai) dan kode akan terlihat seperti di sini:

```cs
var destinationName = "Link2";
var linkAnnotation2 = new LinkAnnotation(page, linkFragments[2].Rectangle)
{
    Action = new GoToAction(document, destinationName)
};
```

Di tempat lain Anda dapat membuat Tujuan yang Dinamai.

```cs
document.NamedDestinations.Add(destinationName,
    new XYZExplicitDestination(
        sampleTextFragments[2].Page,
        sampleTextFragments[2].Rectangle.LLX,
        sampleTextFragments[2].Rectangle.URX, 1));
```
### Menggunakan Anotasi Tautan untuk Membuka File

Pendekatan yang sama digunakan saat membuat anotasi untuk membuka file, seperti pada contoh di atas.

```cs
var linkAnnotation3 = new LinkAnnotation(page, linkFragments[3].Rectangle)
{
    Action = new GoToRemoteAction("another.pdf", 2)
};
```

Perbedaannya adalah kita akan menggunakan `GoToRemoteAction` daripada `GoToAction`. Konstruktor dari GoToRemoteAction mendapatkan dua parameter: nama file dan nomor halaman.
Anda juga dapat menggunakan bentuk lain dan memberikan nama file dan beberapa tujuan. Jelas, Anda perlu membuat tujuan seperti itu sebelum menggunakannya.

### Menggunakan Anotasi Tautan untuk Membuka Halaman Web

Untuk membuka halaman web cukup atur `Action` dengan objek `GoToURIAction`.
Anda dapat memberikan hyperlink sebagai parameter konstruktor atau jenis URI lainnya. Misalnya, Anda dapat menggunakan `callto` untuk melaksanakan aksi dengan memanggil nomor telepon.

```cs
var linkAnnotation4 = new LinkAnnotation(page, linkFragments[4].Rectangle)
{
    Action = new GoToURIAction("https://products.aspose.com/pdf/net"),
    // Membuat Anotasi Tautan dan mengatur aksi untuk memanggil nomor telepon
    //Action = new GoToURIAction("callto:678-555-0103")
    Color = Color.Blue
};
```
## Menambahkan Anotasi Tautan yang Didekorasi

Anda dapat mengkustomisasi Anotasi Tautan menggunakan bingkai. Pada contoh di bawah ini kita akan membuat bingkai bergaris biru dengan lebar 3pt.

```cs
var linkAnnotation4 = new LinkAnnotation(page, linkFragments[4].Rectangle)
{
    Action = new GoToURIAction("https://products.aspose.com/pdf/net"),    
    Color = Color.Blue
};

linkAnnotation4.Border = new Border(linkAnnotation4)
{
    Style = BorderStyle.Dashed,
    Dash = new Dash(5, 5),
    Width = 3
};
```

Contoh lain menunjukkan cara mensimulasikan gaya browser dan menggunakan Garis bawah untuk tautan.

```cs
var linkAnnotation5 = new LinkAnnotation(page, linkFragments[5].Rectangle)
{
    Color = Color.Blue
};
linkAnnotation5.Border = new Border(linkAnnotation5)
{
    Style = BorderStyle.Underline,
    Width = 3
};
```

### Mendapatkan Anotasi Tautan

Silakan coba gunakan potongan kode berikut untuk Mendapatkan Anotasi Tautan dari dokumen PDF.

```csharp
class ExampleLinkAnnotations
{
    // Jalur ke direktori dokumen.
    private const string _dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();
    public static void GetLinkAnnotations()
    {
        // Muat file PDF
        Document document = new Document(System.IO.Path.Combine(_dataDir, "SimpleResume_mod.pdf"));
        var linkAnnotations = document.Pages[1].Annotations.Where(a => a.AnnotationType == AnnotationType.Link);
        foreach (Aspose.Pdf.Annotations.Annotation annot in linkAnnotations)
        {
            // Cetak URL dari setiap Anotasi Tautan
            Console.WriteLine("URI: " + ((annot as LinkAnnotation).Action as GoToURIAction).URI);
            TextAbsorber absorber = new TextAbsorber();
            absorber.TextSearchOptions.LimitToPageBounds = true;
            absorber.TextSearchOptions.Rectangle = annot.Rect;
            document.Pages[1].Accept(absorber);
            string extractedText = absorber.Text;
            // Cetak teks yang terkait dengan hyperlink
            Console.WriteLine(extractedText);
        }
    }
}
```
### Hapus Anotasi Tautan

Potongan kode berikut menunjukkan cara Menghapus Anotasi Tautan dari file PDF. Untuk ini kita perlu menemukan dan menghapus semua anotasi tautan pada halaman pertama. Setelah ini kita akan menyimpan dokumen dengan anotasi yang dihapus.

```csharp
class ExampleLinkAnnotations
{
    // Jalur ke direktori dokumen.
    private const string _dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();
    public static void DeleteLinkAnnotations()
    {
        // Muat file PDF
        Document document = new Document(System.IO.Path.Combine(_dataDir, "SimpleResume_mod.pdf"));
        // Temukan dan hapus semua anotasi tautan di halaman pertama
        var linkAnnotations = document.Pages[1].Annotations.Where(a => a.AnnotationType == AnnotationType.Link);

        foreach (var la in linkAnnotations)
            document.Pages[1].Annotations.Delete(la);
        // Simpan dokumen dengan anotasi yang dihapus
        document.Save(System.IO.Path.Combine(_dataDir, "SimpleResume_del.pdf"));
    }
}
```
