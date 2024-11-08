---
title: Dapatkan dan Atur Properti Halaman
type: docs
url: /id/net/get-and-set-page-properties/
lastmod: "2022-02-17"
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Dapatkan dan Atur Properti Halaman",
    "alternativeHeadline": "Mendapatkan dan Mengatur Properti Halaman PDF",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pembuatan dokumen pdf",
    "keywords": "pdf, c#, dapatkan properti halaman, atur properti halaman",
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
    "url": "/net/get-and-set-page-properties/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/get-and-set-page-properties/"
    },
    "dateModified": "2022-02-04",
    "description": ""
}
</script>

Aspose.PDF untuk .NET memungkinkan Anda membaca dan mengatur properti halaman dalam file PDF di aplikasi .NET Anda. Bagian ini menunjukkan cara mendapatkan jumlah halaman dalam file PDF, mendapatkan informasi tentang properti halaman PDF seperti warna dan mengatur properti halaman. Contoh yang diberikan adalah dalam C# tetapi Anda dapat menggunakan bahasa .NET lain seperti VB.NET untuk mencapai hal yang sama.

Potongan kode berikut juga bekerja dengan perpustakaan [Aspose.PDF.Drawing](/pdf/id/net/drawing/).

## Dapatkan Jumlah Halaman dalam File PDF

Saat bekerja dengan dokumen, Anda sering ingin tahu berapa banyak halaman yang mereka berisi. Dengan Aspose.PDF ini tidak memerlukan lebih dari dua baris kode.

Untuk mendapatkan jumlah halaman dalam file PDF:

1. Buka file PDF menggunakan kelas [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document).
1. Kemudian gunakan properti Count dari koleksi [PageCollection](https://reference.aspose.com/pdf/net/aspose.pdf/pagecollection) (dari objek Document) untuk mendapatkan total jumlah halaman dalam dokumen.

Potongan kode berikut menunjukkan cara mendapatkan jumlah halaman dari file PDF.
### Dapatkan Jumlah Halaman Tanpa Menyimpan Dokumen

Terkadang kita menghasilkan file PDF secara langsung dan selama pembuatan file PDF, kita mungkin menemui kebutuhan (membuat Daftar Isi dll) untuk mendapatkan jumlah halaman file PDF tanpa menyimpan file di sistem atau aliran. Oleh karena itu, untuk memenuhi kebutuhan ini, metode [ProcessParagraphs](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/processparagraphs) telah diperkenalkan di kelas Dokumen. Silakan lihat cuplikan kode berikut yang menunjukkan langkah-langkah untuk mendapatkan jumlah halaman tanpa menyimpan dokumen.

{{< gist "aspose-pdf" "7e1330795d76012fcb04248bb81d45b3" "Examples-CSharp-AsposePDF-Pages-GetPageCount-GetPageCount.cs" >}}

## Dapatkan Properti Halaman

Setiap halaman dalam file PDF memiliki sejumlah properti, seperti lebar, tinggi, bleed-, crop- dan trimbox.
Setiap halaman dalam file PDF memiliki sejumlah properti, seperti lebar, tinggi, bleed-, crop-, dan trimbox.

### **Memahami Properti Halaman: Perbedaan antara Artbox, BleedBox, CropBox, MediaBox, TrimBox, dan Properti Rect**

- **Media box**: Media box adalah kotak halaman terbesar. Box ini sesuai dengan ukuran halaman (seperti A4, A5, Surat AS, dll.) yang dipilih ketika dokumen dicetak ke PostScript atau PDF. Dengan kata lain, media box menentukan ukuran fisik media di mana dokumen PDF ditampilkan atau dicetak.
- **Bleed box**: Jika dokumen memiliki bleed, PDF tersebut juga akan memiliki bleed box. Bleed adalah jumlah warna (atau karya seni) yang melampaui tepi halaman. Ini digunakan untuk memastikan bahwa ketika dokumen dicetak dan dipotong menjadi ukuran ("dipangkas"), tinta akan sampai ke tepi halaman. Bahkan jika halaman dipangkas - dipotong sedikit dari tanda pemangkasan - tidak akan ada tepi putih yang muncul di halaman.
- **Trim box**: Trim box menunjukkan ukuran akhir dokumen setelah dicetak dan dipangkas.
- **Trim box**: Trim box menunjukkan ukuran akhir dari dokumen setelah dicetak dan dipotong.
- **Art box**: Art box adalah kotak yang digambar mengelilingi konten sebenarnya dari halaman dalam dokumen Anda. Kotak halaman ini digunakan saat mengimpor dokumen PDF dalam aplikasi lain.
- **Crop box**: Crop box adalah ukuran "halaman" di mana dokumen PDF Anda ditampilkan di Adobe Acrobat. Dalam tampilan normal, hanya konten dari crop box yang ditampilkan di Adobe Acrobat.
  Untuk deskripsi rinci dari properti ini, baca spesifikasi Adobe.Pdf, terutama 10.10.1 Batas Halaman.
- **Page.Rect**: persimpangan (persegi panjang yang umumnya terlihat) dari MediaBox dan DropBox. Gambar di bawah ini mengilustrasikan properti ini.

Untuk detail lebih lanjut, silakan kunjungi [halaman ini](http://www.enfocus.com/manuals/ReferenceGuide/PP/10/enUS/en-us/concept/c_aa1095731.html).

### **Mengakses Properti Halaman**

Kelas [Page](https://reference.aspose.com/pdf/net/aspose.pdf/page) menyediakan semua properti yang terkait dengan halaman PDF tertentu.
Kelas [Page](https://reference.aspose.com/pdf/net/aspose.pdf/page) menyediakan semua properti yang terkait dengan halaman PDF tertentu.

Dari sana, Anda dapat mengakses objek Page secara individual menggunakan indeksnya, atau melalui koleksi dengan menggunakan loop foreach, untuk mendapatkan semua halaman. Setelah halaman individual diakses, kita dapat mendapatkan propertinya. Cuplikan kode berikut menunjukkan cara mendapatkan properti halaman.

{{< gist "aspose-pdf" "7e1330795d76012fcb04248bb81d45b3" "Examples-CSharp-AsposePDF-Pages-GetProperties-GetProperties.cs" >}}

## Dapatkan Halaman Tertentu dari File PDF

Aspose.PDF memungkinkan Anda untuk [memisahkan PDF menjadi halaman-halaman individual](/pdf/id/net/split-pdf-document/) dan menyimpannya sebagai file PDF. Mendapatkan halaman tertentu dalam file PDF dan menyimpannya sebagai PDF baru adalah operasi yang sangat mirip: buka dokumen sumber, akses halaman, buat dokumen baru dan tambahkan halaman ke dalamnya.

Objek [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) dengan [PageCollection](https://reference.aspose.com/pdf/net/aspose.pdf/pagecollection) nya menampung halaman-halaman dalam file PDF.
Objek [Dokumen](https://reference.aspose.com/pdf/net/aspose.pdf/document) memiliki [Koleksi Halaman](https://reference.aspose.com/pdf/net/aspose.pdf/pagecollection) yang menyimpan halaman dalam file PDF.

1. Tentukan indeks halaman menggunakan properti Halaman.
1. Buat objek [Dokumen](https://reference.aspose.com/pdf/net/aspose.pdf/document) baru.
1. Tambahkan objek [Halaman](https://reference.aspose.com/pdf/net/aspose.pdf/page) ke objek [Dokumen](https://reference.aspose.com/pdf/net/aspose.pdf/document) baru.
1. Simpan output menggunakan metode [Simpan](https://reference.aspose.com/pdf/net/aspose.pdf.document/save/methods/4).

Potongan kode berikut menunjukkan cara mendapatkan halaman tertentu dari file PDF dan menyimpannya sebagai file baru.

{{< gist "aspose-pdf" "7e1330795d76012fcb04248bb81d45b3" "Examples-CSharp-AsposePDF-Pages-GetParticularPage-GetParticularPage.cs" >}}

## Tentukan Warna Halaman

Kelas [Halaman](https://reference.aspose.com/pdf/net/aspose.pdf/page) menyediakan properti terkait dengan halaman tertentu dalam dokumen PDF, termasuk jenis warna - RGB, hitam putih, skala abu-abu, atau tidak terdefinisi - yang digunakan halaman.
Kelas [Page](https://reference.aspose.com/pdf/net/aspose.pdf/page) menyediakan properti yang terkait dengan halaman tertentu dalam dokumen PDF, termasuk jenis warna - RGB, hitam putih, skala abu-abu atau tidak terdefinisi - yang digunakan oleh halaman tersebut.

Semua halaman dari file PDF terkandung dalam koleksi [PageCollection](https://reference.aspose.com/pdf/net/aspose.pdf/pagecollection). Properti ColorType menentukan warna elemen di halaman. Untuk mendapatkan atau menentukan informasi warna untuk halaman PDF tertentu, gunakan properti [ColorType](https://reference.aspose.com/pdf/net/aspose.pdf/page/properties/colortype) dari objek [Page](https://reference.aspose.com/pdf/net/aspose.pdf/page).

Potongan kode berikut menunjukkan cara mengiterasi melalui halaman individu dari file PDF untuk mendapatkan informasi warna.

{{< gist "aspose-pdf" "7e1330795d76012fcb04248bb81d45b3" "Examples-CSharp-AsposePDF-Pages-DeterminePageColor-DeterminePageColor.cs" >}}

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


