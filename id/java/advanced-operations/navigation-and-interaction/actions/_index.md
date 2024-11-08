---
title: Bekerja dengan Tindakan
linktitle: Tindakan
type: docs
weight: 20
url: /id/java/actions/
description: Bagian ini menjelaskan cara menambahkan tindakan ke dokumen dan bidang formulir secara programatis dengan Java. Pelajari cara Menambahkan, Membuat, dan Mendapatkan Hyperlink dalam File PDF.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

File PDF dapat berisi lampiran file yang tertanam dan seringkali perlu untuk membuat Hyperlink ke dokumen-dokumen tersebut. Anda dapat mengarahkan pembaca dari dokumen PDF utama ke lampiran PDF dengan membuat tautan dalam dokumen induk yang menunjuk ke lampiran.

## Menambahkan Hyperlink dalam File PDF

Dimungkinkan untuk menambahkan hyperlink ke file PDF, baik untuk memungkinkan pembaca menavigasi ke bagian lain dari PDF, atau ke konten eksternal.

Untuk menambahkan hyperlink web ke dokumen PDF:

1. Buat objek Kelas [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document).

1. Dapatkan Kelas [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page) yang ingin Anda tambahkan tautan ke dalamnya.
1. Buat objek [LinkAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/LinkAnnotation) menggunakan objek Page dan [Rectangle](https://reference.aspose.com/pdf/java/com.aspose.pdf/Rectangle). Objek rectangle digunakan untuk menentukan lokasi pada halaman di mana tautan harus ditambahkan.
1. Atur metode getAction ke objek [GoToURIAction](https://reference.aspose.com/pdf/java/com.aspose.pdf/GoToURIAction) yang menentukan lokasi URI jarak jauh.
1. Untuk menampilkan teks hyperlink, tambahkan string teks pada lokasi yang mirip dengan di mana objek [LinkAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/LinkAnnotation) ditempatkan.
1. Untuk menambahkan teks bebas:

- Buat sebuah objek [FreeTextAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/FreeTextAnnotation).
 Itu juga menerima objek Page dan Rectangle sebagai argumen, sehingga memungkinkan untuk memberikan nilai yang sama seperti yang ditentukan terhadap konstruktor LinkAnnotation.
- Menggunakan properti Contents dari objek [FreeTextAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/FreeTextAnnotation), tentukan string yang harus ditampilkan dalam PDF keluaran.
- Secara opsional, atur lebar batas dari objek [LinkAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/LinkAnnotation) dan FreeTextAnnotation menjadi 0 agar tidak muncul dalam dokumen PDF.
- Setelah objek [LinkAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/LinkAnnotation) dan [FreeTextAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/FreeTextAnnotation) telah didefinisikan, tambahkan tautan ini ke koleksi Annotations dari objek [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page).

- Akhirnya, simpan PDF yang telah diperbarui menggunakan metode Save dari objek [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document).
Potongan kode berikut menunjukkan cara menambahkan hyperlink ke file PDF.

```java
package com.aspose.pdf.examples;

import java.util.List;

import com.aspose.pdf.*;

public class ExampleActions {

    private static String _dataDir = "/home/aspose/pdf-examples/Samples/Actions/";

    private static String GetDataDir() {
        String os = System.getProperty("os.name");
        if (os.startsWith("Windows"))
            _dataDir = "C:\\Samples\\Actions";
        return _dataDir;
    }

    public static void AddHyperlinkInPDFFile() {
        // Buka dokumen
        Document document = new Document(GetDataDir() + "AddHyperlink.pdf");
        // Buat tautan
        Page page = document.getPages().get_Item(1);
        // Buat objek anotasi tautan
        LinkAnnotation link = new LinkAnnotation(page, new Rectangle(100, 100, 300, 300));
        // Buat objek border untuk LinkAnnotation
        Border border = new Border(link);
        // Setel nilai lebar border sebagai 0
        border.setWidth(0);
        // Setel border untuk LinkAnnotation
        link.setBorder(border);
        // Tentukan jenis tautan sebagai URI jarak jauh
        link.setAction(new GoToURIAction("www.aspose.com"));
        // Tambahkan anotasi tautan ke koleksi anotasi halaman pertama file PDF
        page.getAnnotations().add(link);

        // Buat anotasi Teks Bebas
        FreeTextAnnotation textAnnotation = new FreeTextAnnotation(page, new Rectangle(100, 100, 300, 300),
                new DefaultAppearance(FontRepository.findFont("TimesNewRoman"), 10, java.awt.Color.BLUE));

        // String yang akan ditambahkan sebagai teks bebas
        textAnnotation.setContents("Link to Aspose website");
        // Setel border untuk Anotasi Teks Bebas
        textAnnotation.setBorder(border);
        // Tambahkan anotasi Teks Bebas ke koleksi anotasi halaman pertama Dokumen
        page.getAnnotations().add(textAnnotation);

        // Simpan dokumen yang diperbarui
        document.save(_dataDir + "AddHyperlink_out.pdf");

    }
```


## Buat Tautan ke halaman dalam PDF yang sama

Aspose.PDF untuk Java menyediakan fitur hebat untuk pembuatan PDF serta manipulasi PDF. Ini juga menawarkan fitur untuk menambahkan tautan ke halaman PDF dan tautan dapat mengarah ke halaman dalam file PDF lain, URL web, tautan untuk meluncurkan Aplikasi, atau bahkan tautan ke halaman dalam file PDF yang sama.

Untuk menambahkan hyperlink lokal, kita perlu membuat TextFragment sehingga tautan dapat dikaitkan dengan TextFragment. Kelas [TextFragment](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextFragment) memiliki metode bernama [getHyperlink](https://reference.aspose.com/pdf/java/com.aspose.pdf/BaseParagraph#getHyperlink--) yang digunakan untuk mengaitkan instance LocalHyperlink. Potongan kode berikut menunjukkan langkah-langkah untuk memenuhi persyaratan ini.

```java
public static void CreateHyperlinkToPagesInSamePDF() {
        // Buat instance Dokumen
        Document document = new Document();

        // Tambahkan halaman ke koleksi halaman file PDF
        Page page = document.getPages().add();

        // Buat instance Text Fragment
        TextFragment text = new TextFragment("tautan nomor halaman uji ke halaman 2");

        // Buat instance hyperlink lokal
        LocalHyperlink link = new LocalHyperlink();

        // Tetapkan halaman target untuk instance tautan
        link.setTargetPageNumber(2);

        // Atur hyperlink TextFragment
        text.setHyperlink(link);

        // Tambahkan teks ke koleksi paragraf Halaman
        page.getParagraphs().add(text);

        // Buat instance TextFragment baru
        text = new TextFragment("tautan nomor halaman uji ke halaman 1");

        // TextFragment harus ditambahkan ke halaman baru
        text.setInNewPage(true);

        // Buat instance hyperlink lokal lainnya
        link = new LocalHyperlink();

        // Tetapkan halaman Target untuk hyperlink kedua
        link.setTargetPageNumber(1);

        // Atur tautan untuk TextFragment kedua
        text.setHyperlink(link);

        // Tambahkan teks ke koleksi paragraf objek halaman
        page.getParagraphs().add(text);

        // Simpan dokumen yang diperbarui
        document.save(GetDataDir() + "CreateLocalHyperlink_out.pdf");
    }
```


## Mendapatkan Tujuan Hyperlink PDF (URL)

Tautan diwakili sebagai anotasi dalam file PDF dan dapat ditambahkan, diperbarui, atau dihapus. Aspose.PDF untuk Java juga mendukung mendapatkan tujuan (URL) dari hyperlink dalam file PDF.

Untuk mendapatkan URL tautan:

1. Buat objek [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document).
1. Dapatkan [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page) yang ingin Anda ekstrak tautannya.
1. Gunakan kelas [AnnotationSelector](https://reference.aspose.com/pdf/java/com.aspose.pdf/AnnotationSelector) untuk mengekstrak semua objek [LinkAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/LinkAnnotation) dari halaman yang ditentukan.
1. Berikan objek [AnnotationSelector](https://reference.aspose.com/pdf/java/com.aspose.pdf/AnnotationSelector) ke metode Accept objek [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page).

1. Dapatkan semua anotasi tautan yang dipilih ke dalam objek IList menggunakan properti Selected dari objek [AnnotationSelector](https://reference.aspose.com/pdf/java/com.aspose.pdf/AnnotationSelector).
1. Akhirnya, ekstrak Tindakan LinkAnnotation sebagai GoToURIAction.

Cuplikan kode berikut menunjukkan cara mendapatkan tujuan hyperlink (URL) dari file PDF.

```java
    public static void GetPDFHyperlinkDestination() {
        Document document = new Document(GetDataDir() + "Aspose-app-list.pdf");
        // Ekstrak tindakan
        Page page = document.getPages().get_Item(1);
        AnnotationSelector selector = new AnnotationSelector(new LinkAnnotation(page, Rectangle.getTrivial()));
        page.accept(selector);
        List<Annotation> list = selector.getSelected();
        // Iterasi melalui item individu di dalam daftar
        if (list.size() == 0)
            System.out.println("Tidak ada Hyperlink yang ditemukan..");
        else {
            // Loop melalui semua penanda buku
            for (Annotation annot : list) {
                LinkAnnotation la = (annot instanceof LinkAnnotation ? (LinkAnnotation) annot : null);
                if (la != null) {
                    // Cetak URL tujuan
                    System.out.println("Tujuan: " + ((GoToURIAction) la.getAction()).getURI());
                }
            }
        } // end else
    }
```


## Dapatkan Teks Hyperlink

Sebuah hyperlink memiliki dua bagian: teks yang muncul di dokumen, dan URL tujuan. Dalam beberapa kasus, teks tersebut yang kita butuhkan daripada URL.

Teks dan anotasi/tindakan dalam file PDF diwakili oleh entitas yang berbeda. Teks pada halaman hanyalah sekumpulan kata dan karakter, sementara anotasi membawa beberapa interaktivitas seperti yang ada dalam hyperlink.

Untuk menemukan konten URL, Anda perlu bekerja dengan anotasi dan teks. Objek [Annotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/Annotation) tidak memiliki teks itu sendiri tetapi berada di bawah teks pada halaman. Jadi untuk mendapatkan teks, Annotation memberikan batasan URL, sementara objek Text memberikan konten URL. Silakan lihat potongan kode berikut.

```java
    public static void GetHyperlinkText() {
        Document document = new Document(GetDataDir() + "Aspose-app-list.pdf");
        // Ekstrak tindakan
        Page page = document.getPages().get_Item(1);

        for (Annotation annot : page.getAnnotations()) {
            LinkAnnotation la = (annot instanceof LinkAnnotation ? (LinkAnnotation) annot : null);
            if (la != null) {
                // Cetak URL dari setiap Link Annotation
                System.out.println("URI: " + ((GoToURIAction) la.getAction()).getURI());
                TextAbsorber absorber = new TextAbsorber();
                absorber.getTextSearchOptions().setLimitToPageBounds(true);
                absorber.getTextSearchOptions().setRectangle(annot.getRect());
                page.accept(absorber);
                String extractedText = absorber.getText();
                // Cetak teks terkait dengan hyperlink
                System.out.println(extractedText);
            }
        }
    }
```


## Menghapus Aksi Buka Dokumen dari File PDF

[Bagaimana Menentukan Halaman PDF saat Melihat Dokumen](#how-to-specify-pdf-page-when-viewing-document) menjelaskan bagaimana memberitahu sebuah dokumen untuk dibuka pada halaman yang berbeda dari halaman pertama. Ketika menggabungkan beberapa dokumen, dan satu atau lebih memiliki aksi GoTo yang ditetapkan, Anda mungkin ingin menghapusnya. Misalnya, jika menggabungkan dua dokumen dan dokumen kedua memiliki aksi GoTo yang membawa Anda ke halaman kedua, dokumen keluaran akan terbuka pada halaman kedua dari dokumen kedua alih-alih halaman pertama dari dokumen gabungan. Untuk menghindari perilaku ini, hapus perintah aksi buka.

Untuk menghapus aksi buka:

1. Atur metode [getOpenAction](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#getOpenAction--) dari objek [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) ke null.
2. Simpan PDF yang diperbarui menggunakan metode Save dari objek Document.

Potongan kode berikut menunjukkan cara menghapus aksi buka dokumen dari file PDF.

```java
    public static void RemoveDocumentOpenActionFromPDFFile()
    {
        // Buka dokumen
        Document document = new Document(_dataDir + "RemoveOpenAction.pdf");
        // Hapus aksi buka dokumen
        document.setOpenAction(null);
        
        // Simpan dokumen yang diperbarui
        document.save(GetDataDir()+"RemoveOpenAction_out.pdf");
    }
```


## Cara Menentukan Halaman PDF saat Melihat Dokumen {#how-to-specify-pdf-page-when-viewing-document}

Saat melihat file PDF di penampil PDF seperti Adobe Reader, file biasanya terbuka pada halaman pertama. Namun, dimungkinkan untuk mengatur file agar terbuka pada halaman yang berbeda.

Kelas [XYZExplicitDestination](https://reference.aspose.com/pdf/java/com.aspose.pdf/XYZExplicitDestination) memungkinkan Anda menentukan halaman dalam file PDF yang ingin Anda buka. Ketika melewatkan nilai objek GoToAction ke metode getOpenAction kelas [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document), dokumen terbuka pada halaman yang ditentukan terhadap objek XYZExplicitDestination. Cuplikan kode berikut menunjukkan cara menentukan halaman sebagai tindakan buka dokumen.

```java
    public static void HowToSpecifyPDFPageWhenViewingDocument()
    {
        // Memuat file PDF
        Document document = new Document(GetDataDir()+ "SpecifyPageWhenViewing.pdf");
        // Mendapatkan instance dari halaman kedua dokumen
        Page page2 = document.getPages().get_Item(2);
        // Membuat variabel untuk mengatur faktor zoom dari halaman target
        double zoom = 1;
        // Membuat instance GoToAction
        GoToAction action = new GoToAction(page2);
        // Menuju halaman ke-2
        action.setDestination (new XYZExplicitDestination(page2, 0, page2.getRect().getHeight(), zoom));
        // Mengatur tindakan pembukaan dokumen
        document.setOpenAction (action);
        // Menyimpan dokumen yang diperbarui
        document.save(_dataDir + "goto2page_out.pdf");
    }
}
```