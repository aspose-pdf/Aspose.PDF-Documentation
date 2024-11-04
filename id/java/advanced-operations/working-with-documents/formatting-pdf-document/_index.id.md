---
title: Memformat Dokumen PDF 
linktitle: Memformat Dokumen PDF
type: docs
weight: 20
url: /java/formatting-pdf-document/
description: Format Dokumen PDF dengan Aspose.PDF untuk Java. Gunakan cuplikan kode berikut untuk menyelesaikan tugas Anda.
lastmod: "2021-06-05"
---

## Mendapatkan Properti Jendela Dokumen dan Tampilan Halaman

Topik ini membantu Anda memahami cara mendapatkan properti dari jendela dokumen, aplikasi penampil, dan bagaimana halaman ditampilkan.

Untuk mengatur properti yang berbeda ini, buka file PDF menggunakan kelas [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document). Anda sekarang bisa mendapatkan metode objek [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document), seperti

- [IsCenterWindow](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#isCenterWindow--) – Memusatkan jendela dokumen di layar. Default: false.
- [SetDirection](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#setDirection-int-) – Urutan membaca.
 Ini menentukan bagaimana halaman diatur ketika ditampilkan berdampingan. Default: kiri ke kanan.
- [isDisplayDocTitle](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#isDisplayDocTitle--) – Tampilkan judul dokumen di bilah judul jendela dokumen. Default: false (judul ditampilkan).
- [setHideMenuBar](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#setHideMenubar-boolean-) – Sembunyikan atau tampilkan bilah menu jendela dokumen. Default: false (bilah menu ditampilkan).
- [setHideToolBar](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#setHideToolBar-boolean-) – Sembunyikan atau tampilkan bilah alat jendela dokumen. Default: false (bilah alat ditampilkan).
- [setHideWindowUI](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#setHideWindowUI-boolean-) – Sembunyikan atau tampilkan elemen jendela dokumen seperti bilah gulir. Default: false (elemen UI ditampilkan).

- [setNonFullScreenPageMode](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#setNonFullScreenPageMode-int-) – Bagaimana dokumen ditampilkan ketika tidak ditampilkan dalam mode halaman penuh.- [setPageLayout](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#setPageLayout-int-) – Tata letak halaman.
- [setPageMode](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#setPageMode-int-) – Bagaimana dokumen ditampilkan saat pertama kali dibuka. Opsinya adalah menampilkan thumbnail, layar penuh, menampilkan panel lampiran.

Cuplikan kode berikut menunjukkan kepada Anda cara mendapatkan properti menggunakan kelas [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document).

```java
package com.aspose.pdf.examples;

import com.aspose.pdf.*;

public class ExampleFormatting {

  private static String _dataDir = "/home/admin1/pdf-examples/Samples/";

  public static void GetDocumentWindowAndPageDisplayProperties() {

    // Buka dokumen
    Document pdfDocument = new Document(_dataDir + "sample.pdf");

    // Dapatkan berbagai properti dokumen
    // Posisi jendela dokumen - Default: false
    System.out.printf("CenterWindow : " + pdfDocument.isCenterWindow());

    // Urutan membaca yang dominan; tentukan posisi halaman
    // saat ditampilkan berdampingan - Default: L2R
    System.out.printf("Direction :- " + pdfDocument.getDirection());

    // Apakah bilah judul jendela harus menampilkan judul dokumen.
    // Jika false, bilah judul menampilkan nama file PDF - Default: false
    System.out.printf("DisplayDocTitle :- " + pdfDocument.isDisplayDocTitle());

    // Apakah akan mengubah ukuran jendela dokumen agar sesuai dengan ukuran
    // halaman pertama yang ditampilkan - Default: false
    System.out.printf("FitWindow :- " + pdfDocument.isFitWindow());

    // Apakah akan menyembunyikan bilah menu aplikasi penampil - Default: false
    System.out.printf("HideMenuBar :-" + pdfDocument.isHideMenubar());

    // Apakah akan menyembunyikan bilah alat aplikasi penampil - Default: false
    System.out.printf("HideToolBar :-" + pdfDocument.isHideToolBar());

    // Apakah akan menyembunyikan elemen UI seperti bilah gulir
    // dan hanya menampilkan konten halaman - Default: false
    System.out.printf("HideWindowUI :-" + pdfDocument.isHideWindowUI());

    // Mode halaman dokumen. Bagaimana menampilkan dokumen saat keluar
    // dari mode layar penuh.
    System.out.printf("NonFullScreenPageMode :-" + pdfDocument.getNonFullScreenPageMode());

    // Tata letak halaman yaitu satu halaman, satu kolom
    System.out.printf("PageLayout :-" + pdfDocument.getPageLayout());

    // Bagaimana dokumen seharusnya ditampilkan saat dibuka.
    System.out.printf("pageMode :-" + pdfDocument.getPageMode());

  }

```

## Mengatur Jendela Dokumen dan Properti Tampilan Halaman

Topik ini menjelaskan cara mengatur properti jendela dokumen, aplikasi penampil, dan tampilan halaman.

Untuk mengatur properti yang berbeda ini:

1. Buka file PDF menggunakan kelas [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document).
1. Atur properti objek Dokumen.
1. Simpan file PDF yang diperbarui menggunakan metode Save.

Properti yang tersedia adalah:

- [setCenterWindow](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#setCenterWindow-boolean-)
- [setDirection](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#setDirection-int-)
- [setDisplayDocTitle](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#setDisplayDocTitle-boolean-)
- [setFitWindow](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#setFitWindow-boolean-)
- [setHideMenuBar](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#setHideMenubar-boolean-)

- [setHideToolBar](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#setHideToolBar-boolean-)
- [setHideWindowUI](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#setHideWindowUI-boolean-)
- [setNonFullScreenPageMode](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#setNonFullScreenPageMode-int-)
- [setPageLayout](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#setPageLayout-int-)
- [setPageMode](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#setPageMode-int-)

Cuplikan kode berikut menunjukkan kepada Anda bagaimana mengatur properti menggunakan kelas [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document).

```java
  public static void SetDocumentWindowAndPageDisplayProperties() {

    // Buka dokumen
    Document pdfDocument = new Document(_dataDir + "sample.pdf");
    
    // Mengatur berbagai properti dokumen
    // tentukan untuk memposisikan jendela dokumen - Default: false
    pdfDocument.setCenterWindow(true);
    
    // Urutan membaca yang dominan; tentukan posisi halaman
    // ketika ditampilkan berdampingan - Default: L2R
    pdfDocument.setDirection(com.aspose.pdf.Direction.R2L);
    
    // Tentukan apakah bilah judul jendela harus menampilkan judul dokumen
    // jika false, bilah judul menampilkan nama file PDF - Default: false
    pdfDocument.setDisplayDocTitle(true);
    
    // Tentukan apakah jendela dokumen harus diubah ukurannya agar sesuai
    // ukuran halaman pertama yang ditampilkan - Default: false
    pdfDocument.setFitWindow(true);
    
    // Tentukan apakah menu bar dari aplikasi penampil harus disembunyikan - Default:
    // false
    pdfDocument.setHideMenubar(true);
    
    // Tentukan apakah toolbar dari aplikasi penampil harus disembunyikan - Default:
    // false
    pdfDocument.setHideToolBar(true);
    
    // Tentukan apakah elemen UI seperti bilah gulir harus disembunyikan
    // dan hanya menampilkan konten halaman - Default: false
    pdfDocument.setHideWindowUI(true);
    
    // Mode halaman dokumen. tentukan bagaimana menampilkan dokumen saat keluar
    // dari mode layar penuh.
    pdfDocument.setNonFullScreenPageMode(com.aspose.pdf.PageMode.UseOC);
    
    // Tentukan tata letak halaman yaitu satu halaman, satu kolom
    pdfDocument.setPageLayout(com.aspose.pdf.PageLayout.TwoColumnLeft);
    
    // Tentukan bagaimana dokumen harus ditampilkan saat dibuka
    // yaitu menampilkan thumbnail, layar penuh, menampilkan panel lampiran
    pdfDocument.setPageMode(com.aspose.pdf.PageMode.UseThumbs);
    
    // Simpan file PDF yang diperbarui
    pdfDocument.save(_dataDir + "UpdatedFile_output.pdf");

  }
```

## Menyematkan Font dalam File PDF yang Ada

Pembaca PDF mendukung [inti dari 14 font](http://en.wikipedia.org/wiki/Portable_Document_Format#Fonts) sehingga dokumen dapat ditampilkan dengan cara yang sama terlepas dari platform tempat dokumen ditampilkan. Ketika PDF mengandung font yang berada di luar font inti, sematkan font tersebut untuk menghindari substitusi font.

Aspose.PDF untuk Java mendukung penyematan font dalam dokumen PDF yang ada. Anda dapat menyematkan font lengkap atau subset. Untuk menyematkan font:

1. Buka file PDF yang ada menggunakan kelas [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document).
1. Gunakan kelas [com.aspose.pdf.Font](https://reference.aspose.com/pdf/java/com.aspose.pdf/Font) untuk menyematkan font.
   1. Metode setEmbedded(true) menyematkan font penuh.
   1. Metode pageFont.isSubset(true) menyematkan subset dari font.

Subset font hanya menyematkan karakter yang digunakan dan berguna di mana font digunakan untuk kalimat pendek atau slogan, misalnya di mana font perusahaan digunakan untuk logo, tetapi tidak untuk teks tubuh.
 Menggunakan subset mengurangi ukuran file dari output PDF.

Namun, jika font kustom digunakan untuk teks utama, sematkan seluruhnya.

Cuplikan kode berikut menunjukkan cara menyematkan font dalam file PDF.
```java
public static void EmbeddingFontsInAnExistingPDFFile() {
    // Buka dokumen
    Document pdfDocument = new Document(_dataDir + "sample.pdf");
    // Iterasi melalui semua halaman
    for (com.aspose.pdf.Page page : (Iterable<com.aspose.pdf.Page>) pdfDocument.getPages()) {
      if (page.getResources().getFonts() != null) {
        for (com.aspose.pdf.Font pageFont : (Iterable<com.aspose.pdf.Font>) page.getResources().getFonts()) {
          // Periksa apakah font sudah disematkan
          if (!pageFont.isEmbedded())
            pageFont.setEmbedded(true);
        }
      }

      // Periksa objek Formulir
      for (com.aspose.pdf.XForm form : (Iterable<com.aspose.pdf.XForm>) page.getResources().getForms()) {
        if (form.getResources().getFonts() != null) {
          for (com.aspose.pdf.Font formFont : (Iterable<com.aspose.pdf.Font>) form.getResources().getFonts()) {
            // Periksa apakah font disematkan
            if (!formFont.isEmbedded())
              formFont.setEmbedded(true);
          }
        }
      }
    }
    // Simpan file PDF yang diperbarui
    pdfDocument.save(_dataDir + "UpdatedFile_output.pdf");
  }
```

## Menyematkan Font saat membuat PDF

Jika Anda perlu menggunakan font selain dari 14 font inti yang didukung oleh Adobe Reader, maka Anda harus menyematkan deskripsi font saat menghasilkan file PDF. Jika informasi font tidak disematkan, Adobe Reader akan mengambilnya dari Sistem Operasi jika terinstal di sistem, atau akan membangun font pengganti sesuai dengan deskriptor font dalam PDF. Harap dicatat bahwa font yang disematkan harus terinstal di mesin host yaitu dalam kasus kode berikut font 'Univers Condensed' terinstal di sistem.

Kami menggunakan properti setEmbedded dari kelas [Font](https://reference.aspose.com/pdf/java/com.aspose.pdf/Font) untuk menyematkan informasi font ke dalam file PDF. Mengatur nilai properti ini ke 'true' akan menyematkan seluruh file font ke dalam PDF, dengan mengetahui fakta bahwa hal itu akan meningkatkan ukuran file PDF. Berikut adalah potongan kode yang dapat digunakan untuk menyematkan informasi font ke dalam PDF.

```java
public static void EmbeddingFontsWhileCreatingPDF() {

    // Memanggil objek PDF dengan konstruktor kosongnya
    com.aspose.pdf.Document document = new com.aspose.pdf.Document();

    // Membuat bagian dalam objek PDF
    com.aspose.pdf.Page page = document.getPages().add();

    com.aspose.pdf.TextFragment fragment = new com.aspose.pdf.TextFragment("");

    com.aspose.pdf.TextSegment segment = new com.aspose.pdf.TextSegment(" Ini adalah teks sampel menggunakan font Kustom.");
    com.aspose.pdf.TextState ts = new com.aspose.pdf.TextState();
    ts.setFont(FontRepository.findFont("Univers Condensed"));
    ts.getFont().setEmbedded(true);
    segment.setTextState(ts);
    fragment.getSegments().add(segment);
    page.getParagraphs().add(fragment);

    // Simpan file PDF yang diperbarui
    document.save(_dataDir + "UpdatedFile_output.pdf");
  }
```

## Atur Nama Font Default saat Menyimpan PDF

Ketika dokumen PDF berisi font, yang tidak tersedia di dalam dokumen itu sendiri dan pada perangkat, API menggantikan font ini dengan font default. Ketika font tersedia (terinstal di perangkat atau tertanam ke dalam dokumen), output PDF harus memiliki font yang sama (tidak boleh diganti dengan font default). Nilai dari font default harus berisi nama font (bukan jalur ke file font). Kami telah mengimplementasikan fitur untuk mengatur nama font default saat menyimpan dokumen sebagai PDF. Cuplikan kode berikut dapat digunakan untuk mengatur font default:

```java
public static void SetDefaultFontNameWhileSavingPDF() {

    // Memuat dokumen PDF yang ada
    Document document = new Document("input.pdf");

    String newName = "Arial";

    // Inisialisasi opsi simpan untuk format PDF
    PdfSaveOptions ops = new PdfSaveOptions();

    // Atur nama font default
    ops.setDefaultFontName(newName);

    // Simpan file PDF
    document.save(_dataDir + "output_out.pdf", ops);
  }
```


## Dapatkan Semua Font dari Dokumen PDF

Jika Anda ingin mendapatkan semua font dari dokumen PDF, Anda dapat menggunakan metode **Document.getFontUtilities().getAllFonts()** yang disediakan dalam kelas [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document). Silakan periksa cuplikan kode berikut untuk mendapatkan semua font dari dokumen PDF yang ada:

```java
public static void GetAllFontsFromPDFDocument() {

    // Memuat dokumen PDF yang ada
    Document document = new Document(_dataDir + "sample.pdf");

    // Dapatkan semua font dari dokumen
    com.aspose.pdf.Font[] fonts = document.getFontUtilities().getAllFonts();
    for (com.aspose.pdf.Font f : fonts) {
      System.out.println(f.getFontName());
    }
  }
```

## Dapatkan-Setel Faktor Zoom dari File PDF

Terkadang, Anda ingin mengatur atau mendapatkan faktor zoom dari dokumen PDF. Anda dapat dengan mudah memenuhi kebutuhan ini dengan Aspose.PDF.

Objek [GoToAction](https://reference.aspose.com/pdf/java/com.aspose.pdf/GoToAction) memungkinkan Anda mendapatkan nilai zoom yang terkait dengan file PDF.
 Begitu pula, ini dapat digunakan untuk mengatur faktor Zoom sebuah file.

```java
  public static void GetSetZoomFactorOfPDFFile() {
    // Memuat dokumen PDF yang sudah ada
    Document document = new Document(_dataDir + "sample.pdf");
    double zoom = .5;
    // mengatur faktor zoom dokumen
    GoToAction actionzoom = new GoToAction(new XYZExplicitDestination(document.getPages().get_Item(1),
        document.getPages().get_Item(1).getMediaBox().getWidth(),
        document.getPages().get_Item(1).getMediaBox().getHeight(), zoom));

    // mengatur aksi untuk menyesuaikan zoom lebar halaman
    GoToAction actionFittoWidth = new GoToAction(new FitHExplicitDestination(document.getPages().get_Item(1),
        document.getPages().get_Item(1).getMediaBox().getWidth()));

    // mengatur aksi untuk menyesuaikan zoom tinggi halaman
    GoToAction actionFittoHeight = new GoToAction(new FitVExplicitDestination(document.getPages().get_Item(1),
        document.getPages().get_Item(1).getMediaBox().getHeight()));

    document.setOpenAction(actionzoom);
    document.setOpenAction(actionFittoWidth);
    document.setOpenAction(actionFittoHeight);
```

The following code snippet shows how to get the Zoom factor of a PDF file.

```java
    // Membuat objek Dokumen baru
    Document doc1 = new Document(_dataDir + "Zoomed_actionzoom.pdf");
    // Membuat objek GoToAction
    GoToAction action = (GoToAction) doc1.getOpenAction();
    // Mendapatkan faktor Zoom dari file PDF
    System.out.println(((XYZExplicitDestination) action.getDestination()).getZoom());

    // Menyimpan file PDF yang telah diperbarui
    document.save(_dataDir + "UpdatedFile_output.pdf");
  }
}
```