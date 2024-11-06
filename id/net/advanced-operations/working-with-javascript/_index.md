---
title: Bekerja dengan JavaScript
type: docs
url: id/net/working-with-javascript/
lastmod: "2022-02-17"
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Bekerja dengan JavaScript",
    "alternativeHeadline": "Cara Bekerja dengan JavaScript dalam PDF",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pembuatan dokumen pdf",
    "keywords": "pdf, c#, javascript dalam pdf",
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
    "url": "/net/working-with-javascript/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/working-with-javascript/"
    },
    "dateModified": "2022-02-04",
    "description": ""
}
</script>

## Menambahkan JavaScript (DOM)

### Apa itu Acrobat JavaScript?

Acrobat JavaScript adalah bahasa yang berbasis pada inti JavaScript versi 1.5 dari ISO-16262, yang sebelumnya dikenal sebagai ECMAScript, bahasa scripting berorientasi objek yang dikembangkan oleh Netscape Communications. JavaScript dibuat untuk mengalihkan pemrosesan halaman Web dari server ke klien dalam aplikasi berbasis Web. Acrobat JavaScript mengimplementasikan ekstensi, dalam bentuk objek baru dan metode serta properti yang menyertainya, ke bahasa JavaScript. Objek spesifik Acrobat ini memungkinkan pengembang untuk mengelola keamanan dokumen, berkomunikasi dengan database, menangani lampiran file, memanipulasi file PDF sehingga berperilaku seperti formulir interaktif yang diaktifkan web, dan sebagainya. Karena objek spesifik Acrobat ditambahkan di atas JavaScript inti, Anda masih memiliki akses ke kelas standarnya, termasuk Math, String, Date, Array, dan RegExp.

### Acrobat JavaScript vs HTML (Web) JavaScript

Dokumen PDF memiliki keberagaman yang besar karena dapat ditampilkan baik dalam perangkat lunak Acrobat maupun browser Web.
Dokumen PDF memiliki banyak kegunaan karena dapat ditampilkan baik melalui perangkat lunak Acrobat maupun browser web.

- JavaScript Acrobat tidak memiliki akses ke objek dalam halaman HTML. Demikian pula, JavaScript HTML tidak dapat mengakses objek dalam file PDF.
- JavaScript HTML dapat memanipulasi objek seperti Window. JavaScript Acrobat tidak dapat mengakses objek tersebut tetapi dapat memanipulasi objek khusus PDF.

Anda dapat menambahkan JavaScript baik pada tingkat dokumen maupun halaman menggunakan [Aspose.PDF for .NET](/pdf/net/). Untuk menambahkan JavaScript:

### Menambahkan JavaScript ke Aksi Dokumen atau Halaman

1. Deklarasikan dan instansiasi objek JavascriptAction dengan pernyataan JavaScript yang diinginkan sebagai argumen konstruktor.
1. Tetapkan objek JavascriptAction ke aksi yang diinginkan dari dokumen PDF atau halaman.

Contoh di bawah ini menerapkan OpenAction ke dokumen tertentu.

{{< gist "aspose-pdf" "7e1330795d76012fcb04248bb81d45b3" "Examples-CSharp-AsposePDF-Working-Document-AddJavaScriptToPage-AddJavaScriptToPage.cs" >}}

### **Menambah/Menghapus JavaScript pada Tingkat Dokumen**
### **Menambah/Menghapus JavaScript pada Tingkat Dokumen**

Sebuah properti baru bernama JavaScript ditambahkan di kelas Dokumen yang memiliki tipe kumpulan JavaScript dan memberikan akses ke skenario JavaScript melalui kuncinya. Properti ini digunakan untuk menambahkan JavaScript tingkat Dokumen. Kumpulan JavaScript memiliki properti dan metode berikut:

- string this(string key)– Mendapatkan atau mengatur JavaScript berdasarkan namanya
- IList Keys – menyediakan daftar kunci yang ada dalam kumpulan JavaScript
- bool Remove(string key) – menghapus JavaScript berdasarkan kuncinya.

{{< gist "aspose-pdf" "7e1330795d76012fcb04248bb81d45b3" "Examples-CSharp-AsposePDF-Working-Document-AddRemoveJavascriptToDoc-AddRemoveJavascriptToDoc.cs" >}}

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


