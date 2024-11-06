---
title: Dapatkan dan Setel Properti Halaman menggunakan Python
linktitle: Dapatkan dan Setel Properti Halaman
type: docs
weight: 90
url: id/python-net/get-and-set-page-properties/
description: Bagian ini menunjukkan cara mendapatkan jumlah halaman dalam file PDF, mendapatkan informasi tentang properti halaman PDF seperti warna dan menyetel properti halaman.
lastmod: "2023-04-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Dapatkan dan Setel Properti Halaman menggunakan Python",
    "alternativeHeadline": "Mendapatkan dan Menyetel Properti Halaman PDF",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pembuatan dokumen pdf",
    "keywords": "pdf, python, mendapatkan properti halaman, menyetel properti halaman",
    "wordcount": "302",
    "proficiencyLevel":"Pemula",
    "publisher": {
        "@type": "Organization",
        "name": "Tim Dokumen Aspose.PDF",
        "url": "https://products.aspose.com/pdf",
        "logo": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-python-net.svg",
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
    "url": "/python-net/get-and-set-page-properties/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/python-net/get-and-set-page-properties/"
    },
    "dateModified": "2023-04-04",
    "description": ""
}
</script>


Aspose.PDF untuk Python via .NET memungkinkan Anda membaca dan mengatur properti halaman dalam file PDF di aplikasi Python Anda. Bagian ini menunjukkan cara mendapatkan jumlah halaman dalam file PDF, mendapatkan informasi tentang properti halaman PDF seperti warna dan mengatur properti halaman. Contoh yang diberikan menggunakan Python.

## Mendapatkan Jumlah Halaman dalam File PDF

Saat bekerja dengan dokumen, Anda sering ingin mengetahui berapa banyak halaman yang mereka miliki. Dengan Aspose.PDF, ini tidak membutuhkan lebih dari dua baris kode.

Untuk mendapatkan jumlah halaman dalam file PDF:

1. Buka file PDF menggunakan kelas [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).
1. Kemudian gunakan properti Count dari koleksi [PageCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/) (dari objek Document) untuk mendapatkan total jumlah halaman dalam dokumen.

Cuplikan kode berikut menunjukkan cara mendapatkan jumlah halaman dari file PDF.

```python

    import aspose.pdf as ap

    # Buka dokumen
    document = ap.Document(input_pdf)

    # Dapatkan jumlah halaman
    print("Jumlah Halaman:", str(len(document.pages)))
```


### Dapatkan jumlah halaman tanpa menyimpan dokumen

Terkadang kita membuat file PDF secara langsung dan selama pembuatan file PDF, kita mungkin menghadapi kebutuhan (seperti membuat Daftar Isi dll.) untuk mendapatkan jumlah halaman file PDF tanpa menyimpan file di sistem atau stream. Jadi untuk memenuhi kebutuhan ini, sebuah metode [process_paragraphs()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) telah diperkenalkan dalam kelas Document. Silakan lihat potongan kode berikut yang menunjukkan langkah-langkah untuk mendapatkan jumlah halaman tanpa menyimpan dokumen.

```python

    import aspose.pdf as ap

    # Membuat instance Document
    document = ap.Document()
    # Menambahkan halaman ke koleksi halaman file PDF
    page = document.pages.add()
    # Membuat instance loop
    for i in range(0, 300):
        # Menambahkan TextFragment ke koleksi paragraf dari objek halaman
        page.paragraphs.add(ap.text.TextFragment("Uji jumlah halaman"))
    # Memproses paragraf dalam file PDF untuk mendapatkan jumlah halaman yang akurat
    document.process_paragraphs()
    # Mencetak jumlah halaman dalam dokumen
    print("Jumlah halaman dalam dokumen =", str(len(document.pages)))
```


## Dapatkan Properti Halaman

Setiap halaman dalam file PDF memiliki sejumlah properti, seperti lebar, tinggi, bleed-, crop- dan trimbox. Aspose.PDF memungkinkan Anda untuk mengakses properti ini.

### **Memahami Properti Halaman: Perbedaan antara Artbox, BleedBox, CropBox, MediaBox, TrimBox, dan properti Rect**

- **Media box**: Media box adalah kotak halaman terbesar. Ini sesuai dengan ukuran halaman (misalnya A4, A5, US Letter, dll.) yang dipilih ketika dokumen dicetak ke PostScript atau PDF. Dengan kata lain, media box menentukan ukuran fisik media di mana dokumen PDF ditampilkan atau dicetak.
- **Bleed box**: Jika dokumen memiliki bleed, PDF juga akan memiliki bleed box.
 Bleed adalah jumlah warna (atau karya seni) yang meluas melampaui tepi halaman. Ini digunakan untuk memastikan bahwa ketika dokumen dicetak dan dipotong sesuai ukuran ("dipotong"), tinta akan mencapai seluruh tepi halaman. Bahkan jika halaman terpotong sedikit tidak sesuai tanda potong, tidak akan ada tepi putih yang muncul pada halaman.
- **Trim box**: Trim box menunjukkan ukuran akhir dari dokumen setelah dicetak dan dipotong.
- **Art box**: Art box adalah kotak yang digambar di sekitar konten sebenarnya dari halaman dalam dokumen Anda. Kotak halaman ini digunakan saat mengimpor dokumen PDF dalam aplikasi lain.
- **Crop box**: Crop box adalah ukuran "halaman" di mana dokumen PDF Anda ditampilkan di Adobe Acrobat. Dalam tampilan normal, hanya isi dari crop box yang ditampilkan di Adobe Acrobat.  
  Untuk deskripsi detail tentang properti ini, baca spesifikasi Adobe.Pdf, terutama 10.10.1 Batas Halaman.
- **Page.Rect**: perpotongan (umumnya persegi panjang yang terlihat) dari MediaBox dan DropBox. Gambar di bawah ini mengilustrasikan properti ini.

Untuk detail lebih lanjut, silakan kunjungi [halaman ini](http://www.enfocus.com/manuals/ReferenceGuide/PP/10/enUS/en-us/concept/c_aa1095731.html).

### **Mengakses Properti Halaman**

Kelas [Page](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) menyediakan semua properti yang terkait dengan halaman PDF tertentu. Semua halaman dari file PDF terkandung dalam koleksi [PageCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/) dari objek [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).

Dari situ, dimungkinkan untuk mengakses objek Page individual menggunakan indeksnya, atau melakukan iterasi melalui koleksi dengan menggunakan loop foreach untuk mendapatkan semua halaman. Setelah halaman individu diakses, kita dapat memperoleh propertinya. Cuplikan kode berikut menunjukkan cara mendapatkan properti halaman.

```python

    import aspose.pdf as ap

    # Buka dokumen
    document = ap.Document(input_pdf)
    # Dapatkan halaman tertentu
    page = document.pages[1]
    # Dapatkan properti halaman
    print(
        "ArtBox : Height={},Width={},LLX={},LLY={},URX={},URY={}".format(
            page.art_box.height,
            page.art_box.width,
            page.art_box.llx,
            page.art_box.lly,
            page.art_box.urx,
            page.art_box.ury,
        )
    )
    print(
        "BleedBox : Height={},Width={},LLX={},LLY={},URX={},URY={}".format(
            page.bleed_box.height,
            page.bleed_box.width,
            page.bleed_box.llx,
            page.bleed_box.lly,
            page.bleed_box.urx,
            page.bleed_box.ury,
        )
    )
    print(
        "CropBox : Height={},Width={},LLX={},LLY={},URX={},URY={}".format(
            page.crop_box.height,
            page.crop_box.width,
            page.crop_box.llx,
            page.crop_box.lly,
            page.crop_box.urx,
            page.crop_box.ury,
        )
    )
    print(
        "MediaBox : Height={},Width={},LLX={},LLY={},URX={},URY={}".format(
            page.media_box.height,
            page.media_box.width,
            page.media_box.llx,
            page.media_box.lly,
            page.media_box.urx,
            page.media_box.ury,
        )
    )
    print(
        "TrimBox : Height={},Width={},LLX={},LLY={},URX={},URY={}".format(
            page.trim_box.height,
            page.trim_box.width,
            page.trim_box.llx,
            page.trim_box.lly,
            page.trim_box.urx,
            page.trim_box.ury,
        )
    )
    print(
        "Rect : Height={},Width={},LLX={},LLY={},URX={},URY={}".format(
            page.rect.height,
            page.rect.width,
            page.rect.llx,
            page.rect.lly,
            page.rect.urx,
            page.rect.ury,
        )
    )
    print("Nomor Halaman :", page.number)
    print("Rotasi :", page.rotate)
```

## Dapatkan Halaman Tertentu dari File PDF

Aspose.PDF untuk Python memungkinkan Anda untuk [memisahkan PDF menjadi halaman individu](/pdf/python-net/split-pdf-document/) dan menyimpannya sebagai file PDF. Mendapatkan halaman tertentu dalam file PDF dan menyimpannya sebagai PDF baru adalah operasi yang sangat mirip: buka dokumen sumber, akses halaman, buat dokumen baru dan tambahkan halaman ke dalamnya.

Objek [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document) memiliki [PageCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection) yang menyimpan halaman dalam file PDF. Untuk mendapatkan halaman tertentu dari koleksi ini:

1. Tentukan indeks halaman menggunakan properti Pages.
1. Buat objek [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) baru.
1. Tambahkan objek [Page](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) ke objek Document baru.
1. Simpan output menggunakan metode [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods).

Kode berikut menunjukkan cara mendapatkan halaman tertentu dari file PDF dan menyimpannya sebagai file baru.

```python

    import aspose.pdf as ap

    # Buka dokumen
    document = ap.Document(input_pdf)

    # Dapatkan halaman tertentu
    page = document.pages[2]

    # Simpan halaman sebagai file PDF
    new_document = ap.Document()
    new_document.pages.add(page)
    new_document.save(output_pdf)
```

## Menentukan Warna Halaman

Kelas [Page](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) menyediakan properti terkait dengan halaman tertentu dalam dokumen PDF, termasuk jenis warna apa - RGB, hitam dan putih, skala abu-abu atau tidak terdefinisi - yang digunakan halaman tersebut.

Semua halaman dari file PDF terkandung dalam koleksi [PageCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/).
 The [color_type](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/#properties) property menentukan warna elemen pada halaman. Untuk mendapatkan atau menentukan informasi warna untuk halaman PDF tertentu, gunakan properti [color_type](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/#properties) dari objek [Page](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/).

Cuplikan kode berikut menunjukkan cara untuk mengiterasi melalui halaman individu dari file PDF untuk mendapatkan informasi warna.

```python

    import aspose.pdf as ap

    # Buka file PDF sumber
    document = ap.Document(input_pdf)
    # Iterasi melalui semua halaman dari file PDF
    for page_n in range(0, len(document.pages)):
        page_number = page_n + 1
        # Dapatkan informasi tipe warna untuk halaman PDF tertentu
        page_color_type = document.pages[page_number].color_type
        if page_color_type == ap.ColorType.BLACK_AND_WHITE:
            print("Halaman # " + str(page_number) + " adalah Hitam dan putih.")

        if page_color_type == ap.ColorType.GRAYSCALE:
            print("Halaman # " + str(page_number) + " adalah Skala Abu-abu.")

        if page_color_type == ap.ColorType.RGB:
            print("Halaman # " + str(page_number) + " adalah RGB.")

        if page_color_type == ap.ColorType.UNDEFINED:
            print("Halaman # " + str(page_number) + " Warna tidak terdefinisi.")
```

<script type="application/ld+json">
{
    "@context": "http://schema.org",
    "@type": "SoftwareApplication",
    "name": "Aspose.PDF untuk Python melalui .NET Library",
    "image": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-python-net.svg",
    "url": "https://www.aspose.com/",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDF",
        "url": "https://products.aspose.com/pdf",
        "logo": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-python-net.svg",
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
    "applicationCategory": "Perpustakaan Manipulasi PDF untuk Python",
    "downloadUrl": "https://www.nuget.org/packages/Aspose.PDF/",
    "operatingSystem": "Windows, MacOS, Linux",
    "screenshot": "https://docs.aspose.com/pdf/python-net/create-pdf-document/example.png",
    "softwareVersion": "2022.1",
    "aggregateRating": {
        "@type": "AggregateRating",
        "ratingValue": "5",
        "ratingCount": "16"
    }
}
</script>