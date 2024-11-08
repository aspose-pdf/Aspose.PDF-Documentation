---
title: Manipulasi Dokumen PDF 
linktitle: Manipulasi Dokumen PDF
type: docs
weight: 30
url: /id/java/manipulate-pdf-document/
description: Artikel ini berisi informasi tentang cara memvalidasi Dokumen PDF untuk Standar PDF A, cara bekerja dengan TOC, cara mengatur tanggal kedaluwarsa PDF, dan cara menentukan Progres pembuatan file PDF.
lastmod: "2021-06-05"
---

## Memvalidasi Dokumen PDF untuk Standar PDF A (A 1A dan A 1B)

Untuk memvalidasi dokumen PDF agar kompatibel dengan PDF/A-1a atau PDF/A-1b, gunakan metode [validate(..)](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#validate-java.io.OutputStream-int-) dari kelas [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document). Metode ini memungkinkan Anda untuk menentukan nama file di mana hasil akan disimpan dan jenis validasi yang diperlukan dari enumerasi [PdfFormat](https://reference.aspose.com/pdf/java/com.aspose.pdf/PdfFormat): PDF_A_1A atau PDF_A_1B.

Format output XML adalah format kustom dari Aspose.
 The XML berisi kumpulan tag dengan nama Problem; setiap tag berisi detail dari masalah tertentu. Atribut ObjectID dari tag Problem mewakili ID dari objek tertentu yang terkait dengan masalah ini. Atribut Clause mewakili aturan yang sesuai dalam spesifikasi PDF.

```java
  public static void ValidatePDFDocumentForPDF_A_Standard() {
    // Buka dokumen
    Document pdfDocument = new Document(_dataDir + "sample.pdf");

    // Validasi PDF untuk PDF/A-1a
    pdfDocument.validate(_dataDir + "validation-result-A1A.xml", PdfFormat.PDF_A_1A);

    // Simpan file PDF yang diperbarui
    // document.save(_dataDir + "UpdatedFile_output.pdf");
  }
```
## Bekerja dengan TOC

### Tambahkan TOC ke PDF yang Ada

Kelas ListSection dalam paket aspose.pdf memungkinkan Anda membuat daftar isi saat membuat dokumen PDF dari awal. Untuk menambahkan judul, yang merupakan elemen dari TOC, gunakan kelas [aspose.pdf.Heading](https://reference.aspose.com/pdf/java/com.aspose.pdf/Heading).

Untuk menambahkan TOC ke file PDF yang ada, gunakan kelas [Heading](https://reference.aspose.com/pdf/java/com.aspose.pdf/Heading) dalam paket com.aspose.pdf. Paket com.aspose.pdf dapat membuat baru dan memanipulasi file PDF yang sudah ada. Untuk menambahkan TOC ke PDF yang sudah ada, gunakan paket com.aspose.pdf.

Cuplikan kode berikut menunjukkan cara membuat daftar isi di dalam file PDF yang sudah ada.

```java
public static void AddTOCtoExistingPDF() {
    // Memuat file PDF yang sudah ada
    Document document = new Document(_dataDir + "sample.pdf");

    // Dapatkan akses ke halaman pertama dari file PDF
    Page tocPage = document.getPages().insert(1);

    // Buat objek untuk merepresentasikan informasi TOC
    com.aspose.pdf.TocInfo tocInfo = new com.aspose.pdf.TocInfo();
    com.aspose.pdf.TextFragment title = new com.aspose.pdf.TextFragment("Daftar Isi");
    title.getTextState().setFontSize(20);
    title.getTextState().setFontStyle(com.aspose.pdf.FontStyles.Bold);

    // Tetapkan judul untuk TOC
    tocInfo.setTitle(title);
    tocPage.setTocInfo(tocInfo);

    // Buat objek string yang akan digunakan sebagai elemen TOC
    String[] titles = new String[4];
    titles[0] = "Halaman pertama";
    titles[1] = "Halaman kedua";
    titles[2] = "Halaman ketiga";
    titles[3] = "Halaman keempat";
    for (int i = 0; i < 4; i++) {
      // Buat objek Heading
      com.aspose.pdf.Heading heading2 = new com.aspose.pdf.Heading(1);

      com.aspose.pdf.TextSegment segment2 = new com.aspose.pdf.TextSegment();
      heading2.setTocPage(tocPage);
      heading2.getSegments().add(segment2);

      // Tentukan halaman tujuan untuk objek heading
      heading2.setDestinationPage(document.getPages().get_Item(i + 2));

      // Halaman tujuan
      heading2.setTop(document.getPages().get_Item(i + 2).getRect().getHeight());

      // Koordinat tujuan
      segment2.setText(titles[i]);

      // Tambahkan heading ke halaman yang berisi TOC
      tocPage.getParagraphs().add(heading2);
    }
    // Simpan dokumen yang telah diperbarui
    document.save("TOC_Output_Java.pdf");
  }
```
### Setel TabLeaderType yang Berbeda untuk Level TOC yang Berbeda

Aspose.PDF juga memungkinkan pengaturan TabLeaderType yang berbeda untuk level TOC yang berbeda. Anda perlu menetapkan properti LineDash dari FormatArray dengan nilai enum TabLeaderType yang sesuai seperti berikut.

```java
  public static void SetDifferentTabLeaderTypeForTOCLevels() {

    String outFile = "TOC.pdf";

    Document document = new Document();
    Page tocPage = document.getPages().add();

    TocInfo tocInfo = new TocInfo();

    // set LeaderType

    tocInfo.setLineDash(TabLeaderType.Solid);

    TextFragment title = new TextFragment("Daftar Isi");
    title.getTextState().setFontSize(30);
    tocInfo.setTitle(title);

    // Tambahkan bagian daftar ke koleksi bagian dari dokumen Pdf

    tocPage.setTocInfo(tocInfo);

    // Definisikan format dari daftar empat level dengan menetapkan margin kiri dan
    // pengaturan format teks dari setiap level

    tocInfo.setFormatArrayLength(4);
    tocInfo.getFormatArray()[0].getMargin().setLeft(0);
    tocInfo.getFormatArray()[0].getMargin().setRight(30);
    tocInfo.getFormatArray()[0].setLineDash(TabLeaderType.Dot);
    tocInfo.getFormatArray()[0].getTextState().setFontStyle(FontStyles.Bold | FontStyles.Italic);
    tocInfo.getFormatArray()[1].getMargin().setLeft(10);
    tocInfo.getFormatArray()[1].getMargin().setRight(30);
    tocInfo.getFormatArray()[1].setLineDash(TabLeaderType.None);
    tocInfo.getFormatArray()[1].getTextState().setFontSize(10);
    tocInfo.getFormatArray()[2].getMargin().setLeft(20);
    tocInfo.getFormatArray()[2].getMargin().setRight(0);
    tocInfo.getFormatArray()[2].getTextState().setFontStyle(FontStyles.Bold);
    tocInfo.getFormatArray()[3].setLineDash(TabLeaderType.Solid);
    tocInfo.getFormatArray()[3].getMargin().setLeft(30);
    tocInfo.getFormatArray()[3].getMargin().setRight(30);
    tocInfo.getFormatArray()[3].getTextState().setFontStyle(FontStyles.Bold);

    // Buat bagian dalam dokumen Pdf
    Page page = document.getPages().add();

    // Tambahkan empat judul dalam bagian
    for (int Level = 1; Level <= 4; Level++) {
      com.aspose.pdf.Heading heading2 = new com.aspose.pdf.Heading(Level);
      TextSegment segment2 = new TextSegment();

      heading2.getSegments().add(segment2);
      heading2.setAutoSequence(true);
      heading2.setTocPage(tocPage);

      segment2.setText("Contoh Judul" + Level);
      heading2.getTextState().setFont(FontRepository.findFont("Arial UnicodeMS"));

      // Tambahkan judul ke dalam Daftar Isi.
      heading2.setInList(true);
      page.getParagraphs().add(heading2);
    }

    // simpan PDF
    document.save(outFile);
  }
```

### Sembunyikan Nomor Halaman di TOC

Jika Anda tidak ingin menampilkan nomor halaman bersama dengan judul di TOC, Anda dapat menggunakan properti [IsShowPageNumbers](https://reference.aspose.com/pdf/java/com.aspose.pdf/TocInfo) dari Kelas [TOCInfo](https://reference.aspose.com/pdf/java/com.aspose.pdf/tocinfo) sebagai false. Silakan periksa cuplikan kode berikut untuk menyembunyikan nomor halaman di daftar isi:

```java
public static void HidePageNumbersInTOC() {
    String outFile = _dataDir + "HiddenPageNumbers_out.pdf";
    Document doc = new Document();
    Page tocPage = doc.getPages().add();
    TocInfo tocInfo = new TocInfo();
    TextFragment title = new TextFragment("Daftar Isi");
    title.getTextState().setFontSize(20);
    title.getTextState().setFontStyle(FontStyles.Bold);
    tocInfo.setTitle(title);

    // Tambahkan bagian daftar ke koleksi bagian dari dokumen Pdf
    tocPage.setTocInfo(tocInfo);

    // Definisikan format dari daftar empat tingkat dengan mengatur margin kiri dan
    // pengaturan format teks dari setiap tingkat

    tocInfo.setShowPageNumbers(false);
    tocInfo.setFormatArrayLength(4);
    tocInfo.getFormatArray()[0].getMargin().setRight(0);
    tocInfo.getFormatArray()[0].getTextState().setFontStyle(FontStyles.Bold | FontStyles.Italic);

    tocInfo.getFormatArray()[1].getMargin().setLeft(30);
    tocInfo.getFormatArray()[1].getTextState().setUnderline(true);
    tocInfo.getFormatArray()[1].getTextState().setFontSize(10);

    tocInfo.getFormatArray()[2].getTextState().setFontStyle(FontStyles.Bold);
    tocInfo.getFormatArray()[3].getTextState().setFontStyle(FontStyles.Bold);

    Page page = doc.getPages().add();

    // Tambahkan empat judul di bagian ini
    for (int Level = 1; Level != 5; Level++) {
      Heading heading2 = new Heading(Level);
      TextSegment segment2 = new TextSegment();
      heading2.setTocPage(tocPage);
      heading2.getSegments().add(segment2);
      heading2.setAutoSequence(true);
      segment2.setText("ini adalah judul dari tingkat " + Level);
      heading2.setInList(true);
      page.getParagraphs().add(heading2);
    }
    doc.save(_dataDir + outFile);
  }
```


### Sesuaikan Nomor Halaman saat menambahkan TOC

Merupakan hal yang umum untuk menyesuaikan penomoran halaman dalam TOC saat menambahkan TOC dalam dokumen PDF. Misalnya, kita mungkin perlu menambahkan beberapa awalan sebelum nomor halaman seperti P1, P2, P3 dan seterusnya. Dalam kasus seperti itu, Aspose.PDF untuk Java menyediakan properti PageNumbersPrefix dari kelas TocInfo yang dapat digunakan untuk menyesuaikan nomor halaman seperti yang ditunjukkan dalam contoh kode berikut.

```java
  public static void CustomizePageNumbersWhileAddingTOC() {

    String inFile = _dataDir + "sample.pdf";
    String outFile = _dataDir + "42824_out.pdf";

    // Muat file PDF yang ada
    Document doc = new Document(inFile);
    // Dapatkan akses ke halaman pertama file PDF
    Page tocPage = doc.getPages().insert(1);
    // Buat objek untuk mewakili informasi TOC
    TocInfo tocInfo = new TocInfo();
    TextFragment title = new TextFragment("Daftar Isi");
    title.getTextState().setFontSize(20);
    title.getTextState().setFontStyle(FontStyles.Bold);

    // Tetapkan judul untuk TOC
    tocInfo.setTitle(title);
    tocInfo.setPageNumbersPrefix("P");
    tocPage.setTocInfo(tocInfo);

    for (int i = 1; i < doc.getPages().size(); i++) {
      // Buat objek Heading
      Heading heading2 = new Heading(1);
      TextSegment segment2 = new TextSegment();
      heading2.setTocPage(tocPage);
      heading2.getSegments().add(segment2);
      // Tentukan halaman tujuan untuk objek heading
      heading2.setDestinationPage(doc.getPages().get_Item(i + 1));
      // Halaman tujuan
      heading2.setTop(doc.getPages().get_Item(i + 1).getRect().getHeight());
      // Koordinat tujuan
      segment2.setText("Halaman " + i);
      // Tambahkan heading ke halaman yang berisi TOC
      tocPage.getParagraphs().add(heading2);
    }

    // Simpan dokumen yang diperbarui
    doc.save(outFile);
  }
```


## Tambahkan Lapisan ke File PDF

Lapisan dapat digunakan dalam dokumen PDF dengan berbagai cara. Anda mungkin memiliki file multi-bahasa yang ingin Anda distribusikan dan menginginkan teks dalam setiap bahasa muncul di lapisan yang berbeda, dengan desain latar belakang muncul di lapisan terpisah. Anda juga mungkin membuat dokumen dengan animasi yang muncul di lapisan terpisah. Salah satu contohnya adalah menambahkan perjanjian lisensi ke file Anda, dan Anda tidak ingin pengguna melihat kontennya sampai mereka menyetujui syarat dari perjanjian tersebut.

Aspose.PDF untuk Java mendukung penambahan lapisan ke file PDF.

Untuk bekerja dengan lapisan dalam file PDF, gunakan anggota API berikut.

Kelas [Layer](https://reference.aspose.com/pdf/java/com.aspose.pdf/Layer) mewakili sebuah lapisan dan berisi properti berikut:

- **Name** – nama lapisan.
- **Id** – ID lapisan.
- **Contents** – daftar operator lapisan.

Setelah objek [Layer](https://reference.aspose.com/pdf/java/com.aspose.pdf/Layer) didefinisikan, tambahkan mereka ke koleksi Lapisan dari objek [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page).
 Kode di bawah ini menunjukkan cara menambahkan layer ke dokumen PDF.

```java
public static void AddLayersToPDFFile() {
    Document doc = new Document();
    Page page = doc.getPages().add();
    Layer layer = new Layer("oc1", "Garis Merah");
    layer.getContents().add(new com.aspose.pdf.operators.SetRGBColorStroke(1, 0, 0));
    layer.getContents().add(new com.aspose.pdf.operators.MoveTo(500, 700));
    layer.getContents().add(new com.aspose.pdf.operators.LineTo(400, 700));
    layer.getContents().add(new com.aspose.pdf.operators.Stroke());
    page.setLayers(new ArrayList<Layer>());
    page.getLayers().add(layer);
    layer = new Layer("oc2", "Garis Hijau");
    layer.getContents().add(new com.aspose.pdf.operators.SetRGBColorStroke(0, 1, 0));
    layer.getContents().add(new com.aspose.pdf.operators.MoveTo(500, 750));
    layer.getContents().add(new com.aspose.pdf.operators.LineTo(400, 750));
    layer.getContents().add(new com.aspose.pdf.operators.Stroke());
    page.getLayers().add(layer);
    layer = new Layer("oc3", "Garis Biru");
    layer.getContents().add(new com.aspose.pdf.operators.SetRGBColorStroke(0, 0, 1));
    layer.getContents().add(new com.aspose.pdf.operators.MoveTo(500, 800));
    layer.getContents().add(new com.aspose.pdf.operators.LineTo(400, 800));
    layer.getContents().add(new com.aspose.pdf.operators.Stroke());
    page.getLayers().add(layer);
    doc.save("output.pdf");
  
```
## Setel Kedaluwarsa PDF

Fitur kedaluwarsa PDF menentukan berapa lama file PDF berlaku. Pada tanggal tertentu, jika seseorang mencoba mengaksesnya, sebuah pop-up akan ditampilkan, menjelaskan bahwa file tersebut telah kedaluwarsa dan bahwa mereka memerlukan yang baru.

Aspose.PDF memungkinkan Anda untuk mengatur kedaluwarsa saat membuat dan mengedit file PDF.

Cuplikan kode di bawah ini menunjukkan cara mengatur tanggal kedaluwarsa untuk sebuah file PDF. Anda perlu menggunakan JavaScript karena file yang disimpan oleh komponen pihak ketiga (misalnya OwnerGuard) tidak dapat dilihat di workstation lain tanpa utilitas tersebut.

File PDF dapat dibuat menggunakan PDF OwnerGuard menggunakan file yang sudah ada dengan tanggal kedaluwarsa. Namun file baru hanya dapat dibuka di workstation yang memiliki PDF OwnerGuard terpasang. Workstation tanpa PDF OwnerGuard akan memberikan ExpirationFeatureError. Sebagai contoh, PDF Reader membuka file jika OwnerGuard terpasang, tetapi Adobe Acrobat mengembalikan kesalahan.

```java
  public static void SetPDFExpiration() {
    Document document = new Document(_dataDir+"sample.pdf");    
    JavascriptAction javaScript = new JavascriptAction(
      "var year=2020;" + 
      "var month=4;" + 
      "today = new Date(); today = new Date(today.getFullYear(), today.getMonth());" + 
      "expiry = new Date(year, month);" + 
      "if (today.getTime() > expiry.getTime())" + 
      "app.alert('The file is expired. You need a new one.');"
      );
    document.setOpenAction(javaScript);
    document.save(_dataDir + "JavaScript-Added.pdf");
  }
```