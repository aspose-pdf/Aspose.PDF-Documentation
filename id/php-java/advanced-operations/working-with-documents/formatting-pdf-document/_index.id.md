---
title: Memformat Dokumen PDF 
linktitle: Memformat Dokumen PDF
type: docs
weight: 20
url: /php-java/formatting-pdf-document/
description: Format Dokumen PDF dengan Aspose.PDF untuk PHP via Java. Gunakan cuplikan kode berikut untuk menyelesaikan tugas Anda.
lastmod: "2024-06-05"
---

## Mendapatkan Properti Jendela Dokumen dan Tampilan Halaman

Topik ini membantu Anda memahami cara mendapatkan properti jendela dokumen, aplikasi penampil, dan cara halaman ditampilkan.

Untuk mengatur berbagai properti ini, buka file PDF menggunakan kelas [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document). Anda sekarang dapat memperoleh metode objek [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document), seperti

- [isCenterWindow](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#isCenterWindow--) – Memusatkan jendela dokumen di layar. Default: false.
- [setDirection](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#setDirection-int-) – Urutan membaca.
 Ini menentukan bagaimana halaman ditata saat ditampilkan berdampingan. Default: kiri ke kanan.
- [isDisplayDocTitle](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#isDisplayDocTitle--) – Menampilkan judul dokumen di bilah judul jendela dokumen. Default: false (judul ditampilkan).
- [isHideMenubar](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/#isHideMenubar--) – Mendapatkan flag yang menentukan apakah bilah menu harus disembunyikan saat dokumen aktif.
- [isHideToolBar](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/#isHideToolBar--) – Mendapatkan flag yang menentukan apakah bilah alat harus disembunyikan saat dokumen aktif.
- [isHideWindowUI](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/#isHideWindowUI--) – Mendapatkan flag yang menentukan apakah elemen antarmuka pengguna harus disembunyikan saat dokumen aktif.

- [getNonFullScreenPageMode](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/#getNonFullScreenPageMode--) – Mendapatkan mode halaman, menentukan cara menampilkan dokumen saat keluar dari mode layar penuh.- [getPageLayout](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/#getPageLayout--) – Tata letak halaman.
- [getPageMode](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/#getPageMode--) – Mendapatkan mode halaman, menentukan bagaimana dokumen harus ditampilkan saat dibuka.

Cuplikan kode berikut menunjukkan cara mendapatkan properti menggunakan kelas [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document).

```php  

    // Buka dokumen
    $document = new Document($inputFile);

    // Mendapatkan berbagai properti dokumen
    // Posisi jendela dokumen - Default: false
    $responseData = "CenterWindow : " . $document->isCenterWindow();

    // Urutan bacaan utama; menentukan posisi halaman
    // ketika ditampilkan berdampingan - Default: L2R
    $responseData = $responseData . "Direction : " . $document->getDirection();

    // Apakah bilah judul jendela harus menampilkan judul dokumen.
    // Jika false, bilah judul menampilkan nama file PDF - Default: false
    $responseData = $responseData . "DisplayDocTitle : " . $document->isDisplayDocTitle();

    // Apakah untuk mengubah ukuran jendela dokumen agar sesuai dengan ukuran
    // halaman pertama yang ditampilkan - Default: false
    $responseData = $responseData . "FitWindow : " . $document->isFitWindow();

    // Apakah untuk menyembunyikan bilah menu aplikasi penampil - Default: false
    $responseData = $responseData . "HideMenuBar :" . $document->isHideMenubar();

    // Apakah untuk menyembunyikan bilah alat aplikasi penampil - Default: false
    $responseData = $responseData . "HideToolBar :" . $document->isHideToolBar();

    // Apakah untuk menyembunyikan elemen UI seperti bilah gulir
    // dan hanya menampilkan konten halaman - Default: false
    $responseData = $responseData . "HideWindowUI :" . $document->isHideWindowUI();

    // Mode halaman dokumen. Cara menampilkan dokumen saat keluar
    // dari mode layar penuh.
    $responseData = $responseData . "NonFullScreenPageMode :" . $document->getNonFullScreenPageMode();

    // Tata letak halaman yaitu satu halaman, satu kolom
    $responseData = $responseData . "PageLayout :" . $document->getPageLayout();

    // Bagaimana dokumen harus ditampilkan saat dibuka.
    $responseData = $responseData . "Page Mode :" . $document->getPageMode();
    $document->close();  
```


## Atur Properti Jendela Dokumen dan Tampilan Halaman

Topik ini menjelaskan cara mengatur properti jendela dokumen, aplikasi penampil, dan tampilan halaman.

Untuk mengatur properti yang berbeda ini:

1. Buka file PDF menggunakan kelas [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document).
1. Atur properti objek Dokumen.
1. Simpan file PDF yang telah diperbarui menggunakan metode Save.

Metode yang tersedia adalah:

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

Cuplikan kode berikut menunjukkan kepada Anda cara mengatur properti menggunakan kelas [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document).

```php

    // Buka dokumen
    $document = new Document($inputFile);
    // Atur properti dokumen yang berbeda
    // tentukan untuk memposisikan jendela dokumen - Default: false
    $document->setCenterWindow(true);
    // Urutan membaca yang dominan; tentukan posisi halaman
    // ketika ditampilkan berdampingan - Default: L2R
    $document->setDirection(Direction::$R2L);
    // Tentukan apakah bilah judul jendela harus menampilkan judul dokumen
    // jika false, bilah judul menampilkan nama file PDF - Default: false
    $document->setDisplayDocTitle(true);
    // Tentukan apakah akan mengubah ukuran jendela dokumen agar sesuai dengan ukuran
    // halaman pertama yang ditampilkan - Default: false
    $document->setFitWindow(true);
    // Tentukan apakah akan menyembunyikan bilah menu dari aplikasi penampil - Default:
    // false
    $document->setHideMenubar(true);
    // Tentukan apakah akan menyembunyikan bilah alat dari aplikasi penampil - Default:
    // false
    $document->setHideToolBar(true);
    // Tentukan apakah akan menyembunyikan elemen UI seperti bilah gulir
    // dan hanya menampilkan konten halaman - Default: false
    $document->setHideWindowUI(true);
    // Mode halaman dokumen. tentukan bagaimana menampilkan dokumen saat keluar
    // dari mode layar penuh.
    $document->setNonFullScreenPageMode(PageMode::$UseOC);
    // Tentukan tata letak halaman yaitu satu halaman, satu kolom
    $document->setPageLayout(PageLayout::$TwoColumnLeft);
    // Tentukan bagaimana dokumen harus ditampilkan saat dibuka
    // yaitu menampilkan thumbnail, layar penuh, menampilkan panel lampiran
    $document->setPageMode(PageMode::$UseThumbs);
    // Simpan file PDF yang diperbarui
    $document->save($outputFile);
    $document->close();

```


## Menanamkan Font dalam File PDF yang Ada

Pembaca PDF mendukung [inti dari 14 font](http://en.wikipedia.org/wiki/Portable_Document_Format#Fonts) sehingga dokumen dapat ditampilkan dengan cara yang sama terlepas dari platform tempat dokumen ditampilkan. Ketika PDF mengandung font yang berada di luar inti font, tanamkan font untuk menghindari penggantian font.

Aspose.PDF untuk PHP melalui Java mendukung penanaman font dalam dokumen PDF yang ada. Anda dapat menanamkan font lengkap atau subset. Untuk menanamkan font:

1. Buka file PDF yang ada menggunakan kelas [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document).
1. Gunakan kelas [com.aspose.pdf.Font](https://reference.aspose.com/pdf/java/com.aspose.pdf/Font) untuk menanamkan font.
   1. Metode setEmbedded(true) menanamkan font penuh.
   1. [Metode isSubset(true)](https://reference.aspose.com/pdf/java/com.aspose.pdf/font/#isSubset--) menanamkan subset dari font.

Subset font hanya menanamkan karakter yang digunakan dan berguna ketika font digunakan untuk kalimat pendek atau slogan, misalnya ketika font perusahaan digunakan untuk logo, tetapi tidak untuk teks tubuh.
 Menggunakan subset mengurangi ukuran file dari output PDF.

Namun, jika font kustom digunakan untuk teks tubuh, sematkan seluruhnya.

Cuplikan kode berikut menunjukkan cara menyematkan font dalam file PDF.

```php

    // Buka dokumen
    $document = new Document($inputFile);
    $pages = $document->getPages();
    for ($i = 1; $i <= $pages->size(); $i++) {
      $page = $pages->get_Item($i);
      $fonts = $page->getResources()->getFonts();
      if (!is_null($fonts)) {
        for ($fontIndex = 1; $fontIndex <= $fonts->size(); $fontIndex++) {
          $pageFont = $fonts->get_Item($fontIndex);
          // Periksa apakah font sudah disematkan
          if (!$pageFont->isEmbedded())
            $pageFont->setEmbedded(true);
        }
      }
      $forms = $page->getResources()->getForms();
      // Periksa objek Form
      for ($formIndex = 0; $formIndex < -$forms->size(); $formIndex++) {
        $formFonts = $forms->get_Item($formIndex)->getResources()->getFonts();
        if (!is_null($formFonts)) {
          for ($fontIndex = 1; $fontIndex <= $formFonts->size(); $fontIndex++) {
            $pageFont = $formFonts->get_Item($fontIndex);
            // Periksa apakah font sudah disematkan
            if (!$pageFont->isEmbedded())
              $pageFont->setEmbedded(true);
          }
        }
      }
      $responseData = "Ok";
    }

    // Simpan file PDF yang diperbarui
    $document->save($outputFile);
    $document->close();
```

## Menyematkan Font saat membuat PDF

Jika Anda perlu menggunakan font lain selain 14 font inti yang didukung oleh Adobe Reader, maka Anda harus menyematkan deskripsi font saat menghasilkan file PDF. Jika informasi font tidak disematkan, Adobe Reader akan mengambilnya dari Sistem Operasi jika terpasang di sistem, atau akan membangun font pengganti sesuai dengan deskriptor font dalam PDF. Harap dicatat bahwa font yang disematkan harus terpasang di mesin host yaitu dalam kasus kode berikut font 'Univers Condensed' terpasang di sistem.

Kami menggunakan properti setEmbedded dari kelas [Font](https://reference.aspose.com/pdf/java/com.aspose.pdf/Font) untuk menyematkan informasi font ke dalam file PDF. Mengatur nilai properti ini menjadi 'true' akan menyematkan file font lengkap ke dalam PDF, dengan mengetahui fakta bahwa hal itu akan meningkatkan ukuran file PDF. Berikut adalah potongan kode yang dapat digunakan untuk menyematkan informasi font ke dalam PDF.

```php

    // Memanggil konstruktor kosong untuk menginstansiasi objek PDF
    $document = new Document();

    // Membuat sebuah bagian dalam objek Pdf
    $page = $document->getPages()->add();
    $fragment = new TextFragment("");
    $segment = new TextSegment("Ini adalah teks contoh menggunakan font Kustom.");

    $fontRepository = new FontRepository();

    $ts = new TextState();
    $ts->setFont($fontRepository->findFont("Univers Condensed"));
    $ts->getFont()->setEmbedded(true);
    $segment->setTextState($ts);
    $fragment->getSegments()->add($segment);
    $page->getParagraphs()->add($fragment);

    // Menyimpan file PDF yang diperbarui
    $document->save($outputFile);
    $document->close();
```


## Atur Nama Font Default saat Menyimpan PDF

Ketika dokumen PDF berisi font yang tidak tersedia dalam dokumen itu sendiri dan pada perangkat, API mengganti font tersebut dengan font default. Ketika font tersedia (terinstal di perangkat atau disematkan ke dalam dokumen), output PDF harus memiliki font yang sama (tidak boleh diganti dengan font default). Nilai font default harus mengandung nama font (bukan path ke file font). Kami telah mengimplementasikan fitur untuk mengatur nama font default saat menyimpan dokumen sebagai PDF. Cuplikan kode berikut dapat digunakan untuk mengatur font default:

```php

    // Memuat dokumen PDF yang sudah ada
    $document = new Document($inputFile);
    $newName = "Arial";

    // Inisialisasi opsi simpan untuk format PDF
    $ops = new PdfSaveOptions();

    // Atur nama font default
    $ops->setDefaultFontName($newName);

    // Simpan file PDF
    $document->save($outputFile, $ops);
    // Simpan file PDF yang diperbarui
    $document->close();
```

## Dapatkan Semua Font dari Dokumen PDF

Jika Anda ingin mendapatkan semua font dari dokumen PDF, Anda dapat menggunakan metode **Document.getFontUtilities().getAllFonts()** yang disediakan dalam kelas [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document).
 Silakan periksa cuplikan kode berikut untuk mendapatkan semua font dari dokumen PDF yang ada:

```php

    // Muat dokumen PDF yang ada
    $document = new Document($inputFile);

    // Dapatkan semua font dari dokumen
    $fonts = $document->getFontUtilities()->getAllFonts();
    foreach ($fonts as $font) {
      $responseData = $responseData . $f->getFontName() . PHP_EOL;
    }

    // Simpan file PDF yang diperbarui
    $document->close();
```

## Dapatkan-Setel Faktor Zoom dari File PDF

Terkadang, Anda ingin mengatur atau mendapatkan faktor zoom dari dokumen PDF. Anda dapat dengan mudah memenuhi kebutuhan ini dengan Aspose.PDF.

Objek [GoToAction](https://reference.aspose.com/pdf/java/com.aspose.pdf/GoToAction) memungkinkan Anda mendapatkan nilai zoom yang terkait dengan file PDF. Demikian pula, objek ini dapat digunakan untuk mengatur faktor Zoom file.

```php

    // Muat dokumen PDF yang ada
    $document = new Document($inputFile);

    // Buat objek GoToAction
    $action = $document->getOpenAction();

    // Dapatkan faktor Zoom dari file PDF
    $responseData = $action->getDestination()->getZoom();

    // Simpan file PDF yang diperbarui
    $document->close();  
```

Cuplikan kode berikut menunjukkan cara mendapatkan faktor Zoom dari sebuah file PDF.

```php

    // Memuat dokumen PDF yang ada
    $document = new Document($inputFile);
    $zoom = 0.5;
    // menetapkan faktor zoom dokumen
    $page = $document->getPages()->get_Item(1);
    $actionzoom = new GoToAction(
      new XYZExplicitDestination($page, $page->getMediaBox()->getWidth(), $page->getMediaBox()->getHeight(), $zoom)
    );

    // menetapkan tindakan untuk menyesuaikan lebar halaman dengan zoom
    $actionFitToWidth = new GoToAction(
      new FitHExplicitDestination($page, $page->getMediaBox()->getWidth())
    );

    // menetapkan tindakan untuk menyesuaikan tinggi halaman dengan zoom
    $actionFittoHeight = new GoToAction(
      new FitVExplicitDestination( $page, $page->getMediaBox()->getHeight())
    );

    $document->setOpenAction($actionzoom);
    $document->setOpenAction($actionFittoWidth);
    $document->setOpenAction($actionFittoHeight);

    // Menyimpan file PDF yang diperbarui
    $document->save($outputFile);
    $document->close();  
```