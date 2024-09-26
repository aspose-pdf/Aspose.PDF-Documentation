---
title: PDF Tooltip menggunakan C#
linktitle: PDF Tooltip
type: docs
weight: 20
url: /net/pdf-tooltip/
description: Pelajari cara menambahkan tooltip pada fragmen teks dalam PDF menggunakan C# dan Aspose.PDF
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "PDF Tooltip menggunakan C#",
    "alternativeHeadline": "Tambahkan PDF Tooltip pada Teks",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pembuatan dokumen pdf",
    "keywords": "pdf, c#, tambahkan pdf tooltip",
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
    "url": "/net/pdf-tooltip/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/pdf-tooltip/"
    },
    "dateModified": "2022-02-04",
    "description": "Pelajari cara menambahkan tooltip pada fragmen teks dalam PDF menggunakan C# dan Aspose.PDF"
}
</script>
Kode berikut juga dapat digunakan dengan pustaka [Aspose.PDF.Drawing](/pdf/net/drawing/).

## Tambahkan Tooltip pada Teks yang Dicari dengan Menambahkan Tombol Tak Terlihat

Sering kali diperlukan untuk menambahkan beberapa detail untuk frasa atau kata tertentu sebagai tooltip dalam dokumen PDF sehingga dapat muncul ketika pengguna mengarahkan kursor mouse ke atas teks. Aspose.PDF untuk .NET menyediakan fitur ini untuk membuat tooltip dengan menambahkan tombol tak terlihat di atas teks yang dicari. Potongan kode berikut akan menunjukkan cara untuk mencapai fungsionalitas ini:

```csharp
// Untuk contoh lengkap dan file data, silakan kunjungi https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Jalur ke direktori dokumen.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();
string outputFile = dataDir + "Tooltip_out.pdf";

// Buat dokumen contoh dengan teks
Document doc = new Document();
doc.Pages.Add().Paragraphs.Add(new TextFragment("Arahkan kursor mouse ke sini untuk menampilkan tooltip"));
doc.Pages[1].Paragraphs.Add(new TextFragment("Arahkan kursor mouse ke sini untuk menampilkan tooltip yang sangat panjang"));
doc.Save(outputFile);

// Buka dokumen dengan teks
Document document = new Document(outputFile);
// Buat objek TextAbsorber untuk menemukan semua frasa yang cocok dengan ekspresi reguler
TextFragmentAbsorber absorber = new TextFragmentAbsorber("Arahkan kursor mouse ke sini untuk menampilkan tooltip");
// Terima absorber untuk halaman dokumen
document.Pages.Accept(absorber);
// Dapatkan fragmen teks yang diekstraksi
TextFragmentCollection textFragments = absorber.TextFragments;

// Loop melalui fragmen
foreach (TextFragment fragment in textFragments)
{
    // Buat tombol tak terlihat pada posisi fragmen teks
    ButtonField field = new ButtonField(fragment.Page, fragment.Rectangle);
    // Nilai AlternateName akan ditampilkan sebagai tooltip oleh aplikasi penampil
    field.AlternateName = "Tooltip untuk teks.";
    // Tambahkan bidang tombol ke dokumen
    document.Form.Add(field);
}

// Berikutnya akan menjadi contoh tooltip yang sangat panjang
absorber = new TextFragmentAbsorber("Arahkan kursor mouse ke sini untuk menampilkan tooltip yang sangat panjang");
document.Pages.Accept(absorber);
textFragments = absorber.TextFragments;

foreach (TextFragment fragment in textFragments)
{
    ButtonField field = new ButtonField(fragment.Page, fragment.Rectangle);
    // Atur teks yang sangat panjang
    field.AlternateName = "Lorem ipsum dolor sit amet, consectetur adipiscing elit," +
                            " sed do eiusmod tempor incididunt ut labore et dolore magna" +
                            " aliqua. Ut enim ad minim veniam, quis nostrud exercitation" +
                            " ullamco laboris nisi ut aliquip ex ea commodo consequat." +
                            " Duis aute irure dolor in reprehenderit in voluptate velit" +
                            " esse cillum dolore eu fugiat nulla pariatur. Excepteur sint" +
                            " occaecat cupidatat non proident, sunt in culpa qui officia" +
                            " deserunt mollit anim id est laborum.";
    document.Form.Add(field);
}

// Simpan dokumen
document.Save(outputFile);
```
{{% alert color="primary" %}}

Mengenai panjang tooltip, teks tooltip terdapat dalam dokumen PDF sebagai tipe string PDF, di luar aliran konten. Tidak ada pembatasan efektif pada string semacam ini dalam file PDF (Lihat Referensi PDF Lampiran C.). Namun, pembaca yang mematuhi (mis. Adobe Acrobat) yang berjalan pada prosesor tertentu dan dalam lingkungan operasional tertentu memang memiliki batasan tersebut. Silakan merujuk pada dokumentasi aplikasi pembaca PDF Anda.

{{% /alert %}}

## Membuat Blok Teks Tersembunyi dan Menampilkannya saat Mouse Diarahkan

Dalam Aspose.PDF, fitur untuk menyembunyikan tindakan diimplementasikan dimana dimungkinkan untuk menampilkan/menyembunyikan kolom teks (atau jenis anotasi lainnya) saat mouse masuk/keluar di atas tombol yang tidak terlihat. Untuk tujuan ini, Kelas Aspose.Pdf.Annotations.HideAction digunakan untuk menetapkan tindakan menampilkan/menyembunyikan pada blok teks. Silakan gunakan cuplikan kode berikut untuk Menampilkan/Menyembunyikan Blok Teks saat Mouse Masuk/Keluar.

Harap juga diperhatikan bahwa tindakan PDF dalam dokumen bekerja dengan baik dalam pembaca yang mematuhi (mis.
Harap diperhatikan bahwa tindakan PDF dalam dokumen berfungsi dengan baik pada pembaca yang sesuai (misalnya.

- Semua implementasi tindakan sembunyi dalam dokumen PDF berfungsi dengan baik di Internet Explorer v.11.0.
- Semua implementasi tindakan sembunyi juga berfungsi di Opera v.12.14, tetapi kami melihat beberapa penundaan respons pada pembukaan dokumen pertama.
- Hanya implementasi yang menggunakan konstruktor HideAction yang menerima nama bidang yang berfungsi jika Google Chrome v.61.0 menjelajahi dokumen; Silakan gunakan konstruktor yang sesuai jika menjelajahi di Google Chrome signifikan:

>buttonField.Actions.OnEnter = new HideAction(floatingField.FullName, false);
>buttonField.Actions.OnExit = new HideAction(floatingField.FullName);

```csharp
// Untuk contoh lengkap dan file data, silakan kunjungi https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Jalur ke direktori dokumen.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

string outputFile = dataDir + "TextBlock_HideShow_MouseOverOut_out.pdf";

// Membuat dokumen sampel dengan teks
Document doc = new Document();
doc.Pages.Add().Paragraphs.Add(new TextFragment("Gerakkan kursor mouse ke sini untuk menampilkan teks mengambang"));
doc.Save(outputFile);

// Membuka dokumen dengan teks
Document document = new Document(outputFile);
// Membuat objek TextAbsorber untuk menemukan semua frasa yang cocok dengan ekspresi reguler
TextFragmentAbsorber absorber = new TextFragmentAbsorber("Gerakkan kursor mouse ke sini untuk menampilkan teks mengambang");
// Menerima absorber untuk halaman dokumen
document.Pages.Accept(absorber);
// Mendapatkan fragmen teks yang diekstrak pertama
TextFragmentCollection textFragments = absorber.TextFragments;
TextFragment fragment = textFragments[1];

// Membuat bidang teks tersembunyi untuk teks mengambang di persegi panjang yang ditentukan dari halaman
TextBoxField floatingField = new TextBoxField(fragment.Page, new Rectangle(100, 700, 220, 740));
// Mengatur teks yang akan ditampilkan sebagai nilai bidang
floatingField.Value = "Ini adalah \"bidang teks mengambang\".";
// Kami merekomendasikan untuk membuat bidang 'readonly' untuk skenario ini
floatingField.ReadOnly = true;
// Mengatur bendera 'tersembunyi' untuk membuat bidang tidak terlihat saat pembukaan dokumen
floatingField.Flags |= AnnotationFlags.Hidden;

// Mengatur nama bidang unik tidak diperlukan tetapi diizinkan
floatingField.PartialName = "FloatingField_1";

// Mengatur karakteristik penampilan bidang tidak diperlukan tetapi membuatnya lebih baik
floatingField.DefaultAppearance = new DefaultAppearance("Helv", 10, System.Drawing.Color.Blue);
floatingField.Characteristics.Background = System.Drawing.Color.LightBlue;
floatingField.Characteristics.Border = System.Drawing.Color.DarkBlue;
floatingField.Border = new Border(floatingField);
floatingField.Border.Width = 1;
floatingField.Multiline = true;

// Menambahkan bidang teks ke dokumen
document.Form.Add(floatingField);

// Membuat tombol tak terlihat pada posisi fragmen teks
ButtonField buttonField = new ButtonField(fragment.Page, fragment.Rectangle);
// Membuat tindakan sembunyi baru untuk bidang yang ditentukan (anotasi) dan bendera ketidakmampuan.
// (Anda juga dapat merujuk bidang mengambang dengan nama jika Anda menentukannya di atas.)
// Menambahkan tindakan pada saat mouse masuk/keluar di bidang tombol tak terlihat
buttonField.Actions.OnEnter = new HideAction(floatingField, false);
buttonField.Actions.OnExit = new HideAction(floatingField);

// Menambahkan bidang tombol ke dokumen
document.Form.Add(buttonField);

// Menyimpan dokumen
document.Save(outputFile);
```
```
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

