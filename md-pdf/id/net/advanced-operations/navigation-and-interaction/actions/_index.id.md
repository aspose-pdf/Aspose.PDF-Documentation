---
title: Bekerja dengan Aksi dalam PDF
linktitle: Aksi
type: docs
weight: 20
url: /net/actions/
description: Bagian ini menjelaskan cara menambahkan aksi ke dokumen dan bidang formulir secara pemrograman dengan C#.
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Bekerja dengan Aksi dalam PDF",
    "alternativeHeadline": "Cara Menambahkan Aksi dalam PDF",
    "author": {
        "@type": "Person",
        "name":"Andriy Andrukhovskiy",
        "givenName": "Andriy",
        "familyName": "Andrukhovskiy",
        "url":"https://www.linkedin.com/in/andruhovski/"
    },
    "genre": "pembuatan dokumen pdf",
    "keywords": "pdf, c#, aksi dalam pdf",
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
    "url": "/net/actions/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/actions/"
    },
    "dateModified": "2022-02-04",
    "description": "Bagian ini menjelaskan cara menambahkan aksi ke dokumen dan bidang formulir secara pemrograman dengan C#."
}
</script>
Potongan kode berikut juga berfungsi dengan perpustakaan [Aspose.PDF.Drawing](/pdf/net/drawing/).

## Menambahkan Hyperlink dalam File PDF

Memungkinkan untuk menambahkan hyperlink ke file PDF, baik untuk memungkinkan pembaca navigasi ke bagian lain dari PDF, atau ke konten eksternal.

Untuk menambahkan hyperlink web ke dokumen PDF:

1. Buat objek Kelas [Dokumen](https://reference.aspose.com/pdf/net/aspose.pdf/document).
1. Dapatkan Kelas [Halaman](https://reference.aspose.com/pdf/net/aspose.pdf/page) yang ingin Anda tambahkan tautan kepadanya.
1. Buat objek [LinkAnnotation](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/linkannotation) menggunakan objek Halaman dan [Persegi Panjang](https://reference.aspose.com/pdf/net/aspose.pdf/rectangle). Objek persegi panjang digunakan untuk menentukan lokasi di halaman di mana tautan harus ditambahkan.
1. Setel properti Action ke objek [GoToURIAction](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/gotouriaction) yang menentukan lokasi URI jauh.
1. Untuk menambahkan teks bebas:

- Instansiasi objek [FreeTextAnnotation](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/freetextannotation). Objek ini juga menerima objek Page dan Rectangle sebagai argumen, sehingga memungkinkan untuk memberikan nilai yang sama seperti yang ditentukan pada konstruktor LinkAnnotation.
- Menggunakan properti Contents dari objek [FreeTextAnnotation](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/freetextannotation), tentukan string yang harus ditampilkan di PDF keluaran.
- Opsional, atur lebar batas dari objek [LinkAnnotation](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/linkannotation) dan FreeTextAnnotation menjadi 0 agar keduanya tidak muncul di dokumen PDF.
- Setelah objek [LinkAnnotation](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/linkannotation) dan [FreeTextAnnotation](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/freetextannotation) telah didefinisikan, tambahkan tautan ini ke koleksi Annotations dari objek [Page](https://reference.aspose.com/pdf/net/aspose.pdf/page).
- Setelah objek [LinkAnnotation](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/linkannotation) dan [FreeTextAnnotation](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/freetextannotation) telah didefinisikan, tambahkan tautan ini ke koleksi Anotasi objek [Page](https://reference.aspose.com/pdf/net/aspose.pdf/page).
- Akhirnya, simpan PDF yang telah diperbarui menggunakan metode [Save](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/save) dari objek [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document).

Berikut adalah cuplikan kode yang menunjukkan cara menambahkan hyperlink ke file PDF.

```csharp
// Untuk contoh lengkap dan file data, silakan kunjungi https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Jalur ke direktori dokumen.
string dataDir = RunExamples.GetDataDir_AsposePdf_LinksActions();

// Buka dokumen
Document document = new Document(dataDir + "AddHyperlink.pdf");
// Buat tautan
Page page = document.Pages[1];
// Buat objek anotasi tautan
LinkAnnotation link = new LinkAnnotation(page, new Aspose.Pdf.Rectangle(100, 100, 300, 300));
// Buat objek border untuk LinkAnnotation
Border border = new Border(link);
// Atur nilai lebar border sebagai 0
border.Width = 0;
// Atur border untuk LinkAnnotation
link.Border = border;
// Tentukan tipe tautan sebagai URI jarak jauh
link.Action = new GoToURIAction("www.aspose.com");
// Tambahkan anotasi tautan ke koleksi anotasi halaman pertama file PDF
page.Annotations.Add(link);

// Buat anotasi Teks Bebas
FreeTextAnnotation textAnnotation = new FreeTextAnnotation(document.Pages[1], new Aspose.Pdf.Rectangle(100, 100, 300, 300), new DefaultAppearance(Aspose.Pdf.Text.FontRepository.FindFont("TimesNewRoman"), 10, System.Drawing.Color.Blue));
// String yang akan ditambahkan sebagai teks bebas
textAnnotation.Contents = "Link ke situs web Aspose";
// Atur border untuk Anotasi Teks Bebas
textAnnotation.Border = border;
// Tambahkan anotasi Teks Bebas ke koleksi anotasi halaman pertama Dokumen
document.Pages[1].Annotations.Add(textAnnotation);
dataDir = dataDir + "AddHyperlink_out.pdf";
// Simpan dokumen yang telah diperbarui
document.Save(dataDir);
```
## Membuat Hyperlink ke halaman dalam PDF yang sama

Aspose.PDF untuk .NET menyediakan fitur hebat untuk pembuatan PDF serta manipulasinya. Fitur ini juga menawarkan kemampuan untuk menambahkan tautan ke halaman PDF dan tautan bisa mengarah ke halaman di file PDF lain, URL web, tautan untuk menjalankan aplikasi atau bahkan tautan ke halaman di file PDF yang sama. Untuk menambahkan hyperlink lokal (tautan ke halaman dalam file PDF yang sama), sebuah kelas bernama [LocalHyperlink](https://reference.aspose.com/pdf/net/aspose.pdf/localhyperlink) ditambahkan ke namespace Aspose.PDF dan kelas ini memiliki properti bernama TargetPageNumber, yang digunakan untuk menentukan halaman tujuan untuk hyperlink.

Untuk menambahkan hyperlink lokal, kita perlu membuat TextFragment sehingga tautan dapat dikaitkan dengan TextFragment. Kelas [TextFragment](https://reference.aspose.com/pdf/net/aspose.pdf.text/textfragment) memiliki properti bernama Hyperlink yang digunakan untuk mengaitkan instansi LocalHyperlink. Cuplikan kode berikut menunjukkan langkah-langkah untuk mencapai kebutuhan ini.

```csharp
```csharp
// Untuk contoh lengkap dan file data, silakan kunjungi https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Jalur ke direktori dokumen.
string dataDir = RunExamples.GetDataDir_AsposePdf_LinksActions();

// Buat instansi Dokumen
Document doc = new Document();
// Tambahkan halaman ke koleksi halaman file PDF
Page page = doc.Pages.Add();
// Buat instansi Fragmen Teks
Aspose.Pdf.Text.TextFragment text = new Aspose.Pdf.Text.TextFragment("tes nomor halaman tautan ke halaman 7");
// Buat instansi hyperlink lokal
Aspose.Pdf.LocalHyperlink link = new Aspose.Pdf.LocalHyperlink();
// Tetapkan halaman tujuan untuk instansi tautan
link.TargetPageNumber = 7;
// Tetapkan hyperlink Fragmen Teks
text.Hyperlink = link;
// Tambahkan teks ke koleksi paragraf Halaman
page.Paragraphs.Add(text);
// Buat instansi Fragmen Teks baru
text = new TextFragment("tes nomor halaman tautan ke halaman 1");
// Fragmen Teks harus ditambahkan di halaman baru
text.IsInNewPage = true;
// Buat instansi hyperlink lokal lain
link = new LocalHyperlink();
// Tetapkan Halaman target untuk hyperlink kedua
link.TargetPageNumber = 1;
// Tetapkan tautan untuk Fragmen Teks kedua
text.Hyperlink = link;
// Tambahkan teks ke koleksi paragraf objek halaman
page.Paragraphs.Add(text);

dataDir = dataDir + "CreateLocalHyperlink_out.pdf";
// Simpan dokumen yang telah diperbarui
doc.Save(dataDir);
```
## Dapatkan Tujuan Tautan PDF (URL)

Tautan direpresentasikan sebagai anotasi dalam file PDF dan dapat ditambahkan, diperbarui, atau dihapus. Aspose.PDF untuk .NET juga mendukung pengambilan tujuan (URL) dari tautan dalam file PDF.

Untuk mendapatkan URL tautan:

1. Buat objek [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document).
2. Dapatkan [Page](https://reference.aspose.com/pdf/net/aspose.pdf/page) yang ingin Anda ekstrak tautannya.
3. Gunakan kelas [AnnotationSelector](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/annotationselector) untuk mengekstrak semua objek [LinkAnnotation](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/linkannotation) dari halaman yang ditentukan.
4. Serahkan objek [AnnotationSelector](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/annotationselector) ke metode Accept dari objek [Page](https://reference.aspose.com/pdf/net/aspose.pdf/page).
1. Akhirnya, ekstrak LinkAnnotation Action sebagai GoToURIAction.

Kode berikut menunjukkan cara mendapatkan tujuan tautan (URL) dari file PDF.

```csharp
// Untuk contoh lengkap dan file data, silakan kunjungi https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Jalur ke direktori dokumen.
string dataDir = RunExamples.GetDataDir_AsposePdf_LinksActions();
// Memuat file PDF
Document document = new Document(dataDir + "input.pdf");

// Melintasi semua halaman PDF
foreach (Aspose.Pdf.Page page in document.Pages)
{
    // Dapatkan anotasi tautan dari halaman tertentu
    AnnotationSelector selector = new AnnotationSelector(new Aspose.Pdf.Annotations.LinkAnnotation(page, Aspose.Pdf.Rectangle.Trivial));

    page.Accept(selector);
    // Buat daftar yang memegang semua tautan
    IList<Annotation> list = selector.Selected;
    // Iterasi melalui item individu dalam daftar
    foreach (LinkAnnotation a in list)
    {
        // Cetak URL tujuan
        Console.WriteLine("\nDestination: " + (a.Action as Aspose.Pdf.Annotations.GoToURIAction).URI + "\n");
    }
}
```
## Dapatkan Teks Hyperlink

Hyperlink memiliki dua bagian: teks yang ditampilkan di dokumen, dan URL tujuan. Dalam beberapa kasus, tekslah yang kita perlukan bukan URL-nya.

Teks dan anotasi/aksi dalam file PDF diwakili oleh entitas yang berbeda. Teks di halaman hanyalah sekumpulan kata dan karakter, sementara anotasi memberikan beberapa interaktivitas seperti yang melekat pada hyperlink.

Untuk menemukan konten URL, Anda perlu bekerja dengan anotasi dan teks. Objek [Annotation](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/annotation) sendiri tidak memiliki teks tetapi berada di bawah teks di halaman. Jadi untuk mendapatkan teks, Annotation memberikan batas URL, sementara objek Teks memberikan konten URL. Silakan lihat cuplikan kode berikut.

```csharp
  {
        public static void Run()
        {
            try
            {
                // ExStart:GetHyperlinkText
                // Jalur ke direktori dokumen.
                string dataDir = RunExamples.GetDataDir_AsposePdf_LinksActions();
                // Memuat file PDF
                Document document = new Document(dataDir + "input.pdf");
                // Beriterasi melalui setiap halaman PDF
                foreach (Page page in document.Pages)
                {
                    // Menunjukkan anotasi tautan
                    ShowLinkAnnotations(page);
                }
                // ExEnd:GetHyperlinkText
            }
            catch (Exception ex)
            {
                Console.WriteLine(ex.Message);
            }
        }
        // ExStart:ShowLinkAnnotations
        public static void ShowLinkAnnotations(Page page)
        {
            foreach (Aspose.Pdf.Annotations.Annotation annot in page.Annotations)
            {
                if (annot is LinkAnnotation)
                {
                    // Mencetak URL setiap Anotasi Tautan
                    Console.WriteLine("URI: " + ((annot as LinkAnnotation).Action as GoToURIAction).URI);
                    TextAbsorber absorber = new TextAbsorber();
                    absorber.TextSearchOptions.LimitToPageBounds = true;
                    absorber.TextSearchOptions.Rectangle = annot.Rect;
                    page.Accept(absorber);
                    string extractedText = absorber.Text;
                    // Mencetak teks yang terkait dengan hyperlink
                    Console.WriteLine(extractedText);
                }

            }
        }
        // ExEnd:ShowLinkAnnotations
    }
}
```
## Menghapus Aksi Buka Dokumen dari File PDF

[Bagaimana Menentukan Halaman PDF Saat Melihat Dokumen](#how-to-specify-pdf-page-when-viewing-document) menjelaskan bagaimana memberi tahu dokumen untuk dibuka di halaman yang berbeda dari halaman pertama. Saat menggabungkan beberapa dokumen, dan satu atau lebih memiliki aksi GoTo yang ditetapkan, Anda mungkin ingin menghapusnya. Misalnya, jika menggabungkan dua dokumen dan dokumen kedua memiliki aksi GoTo yang membawa Anda ke halaman kedua, dokumen hasil akan dibuka di halaman kedua dari dokumen kedua bukan di halaman pertama dari dokumen gabungan. Untuk menghindari perilaku ini, hapus perintah aksi buka.

Untuk menghapus aksi buka:

1. Atur properti [OpenAction](https://reference.aspose.com/pdf/net/aspose.pdf/document/properties/openaction) dari objek [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) menjadi null.
1. Simpan PDF yang telah diperbarui menggunakan metode [Save](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/save) dari objek Document.

Potongan kode berikut menunjukkan cara menghapus aksi buka dokumen dari file PDF.
Potongan kode berikut menunjukkan cara menghapus tindakan pembukaan dokumen dari file PDF.

```csharp
// Untuk contoh lengkap dan file data, silakan kunjungi https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Jalur ke direktori dokumen.
string dataDir = RunExamples.GetDataDir_AsposePdf_LinksActions();
// Buka dokumen
Document document = new Document(dataDir + "RemoveOpenAction.pdf");
// Hapus tindakan buka dokumen
document.OpenAction = null;
dataDir = dataDir + "RemoveOpenAction_out.pdf";
// Simpan dokumen yang telah diperbarui
document.Save(dataDir);
```

## Cara Menentukan Halaman PDF Saat Melihat Dokumen {#how-to-specify-pdf-page-when-viewing-document}

Saat melihat file PDF dalam penampil PDF seperti Adobe Reader, file biasanya dibuka di halaman pertama. Namun, Anda dapat mengatur file untuk dibuka di halaman yang berbeda.

Kelas [XYZExplicitDestination](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/xyzexplicitdestination) memungkinkan Anda untuk menentukan halaman dalam file PDF yang ingin Anda buka.
Kelas [XYZExplicitDestination](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/xyzexplicitdestination) memungkinkan Anda untuk menentukan halaman dalam file PDF yang ingin Anda buka.

```csharp
// Untuk contoh lengkap dan file data, silakan kunjungi https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Jalur ke direktori dokumen.
string dataDir = RunExamples.GetDataDir_AsposePdf_LinksActions();

// Muat file PDF
Document doc = new Document(dataDir + "SpecifyPageWhenViewing.pdf");
// Dapatkan instansi halaman kedua dari dokumen
Page page2 = doc.Pages[2];
// Buat variabel untuk mengatur faktor zoom halaman tujuan
double zoom = 1;
// Buat instansi GoToAction
GoToAction action = new GoToAction(doc.Pages[2]);
// Pergi ke halaman 2
action.Destination = new XYZExplicitDestination(page2, 0, page2.Rect.Height, zoom);
// Tetapkan tindakan pembukaan dokumen
doc.OpenAction = action;
// Simpan dokumen yang telah diperbarui
doc.Save(dataDir + "goto2page_out.pdf");
```

