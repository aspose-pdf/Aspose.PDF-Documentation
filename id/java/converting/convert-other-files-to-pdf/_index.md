---
title: "Mengonversi Format file lain ke PDF dengan Java"
linktitle: "Mengonversi format file lain ke PDF"
type: docs
weight: 80
url: /id/java/convert-other-files-to-pdf/
lastmod: "2026-09-30"
description: Pelajari cara mengonversi file EPUB, Markdown, PCL, XPS, PostScript, XML, XSL-FO, OFD, dan TeX ke PDF dalam Java dengan Aspose.PDF.
sitemap:
    changefreq: "monthly"
    priority: 0.5
TechArticle: true
AlternativeHeadline: "Mengonversi format file lain ke PDF dalam Java"
Abstract: Artikel ini menjelaskan cara mengonversi banyak format file sumber ke PDF menggunakan Aspose.PDF for Java. Artikel ini mencakup alur kerja konversi EPUB, Markdown, OFD, PCL, PostScript, EPS, TeX, teks, XML, XPS, dan XSL-FO menggunakan opsi pemuatan khusus format serta langkah pra‑pemrosesan bila diperlukan.
---
Aspose.PDF for Java mendukung konversi dari format dokumen, markup, dan deskripsi halaman ke PDF.

## Mengonversi OFD ke PDF

Gunakan contoh ini ketika dokumen OFD harus dikonversi menjadi PDF.

1. Buka sumber OFD dengan memberikan jalur file dan [`OfdLoadOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/ofdloadoptions/) ke dalam konstruktor [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Biarkan Aspose.PDF mengurai paket OFD menjadi model dokumen PDF.
1. Simpan PDF yang dihasilkan ke jalur output target.

```java
public static void convertOfdToPdf(Path inputFile, Path outputFile) {
       try (Document document = new Document(inputFile.toString(), new OfdLoadOptions())) {
           document.save(outputFile.toString());
       }
       System.out.println(inputFile + " converted into " + outputFile);
   }
```

## Mengonversi TeX ke PDF

Gunakan contoh ini ketika konten TeX harus dirender langsung sebagai PDF.

1. Buka sumber TeX dengan melewatkan path file dan [`TeXLoadOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/texloadoptions/) ke dalam konstruktor [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Biarkan Aspose.PDF menafsirkan markup TeX dan membangun tata letak PDF saat pemuatan.
1. Simpan PDF yang dihasilkan.

```java
public static void convertTexToPdf(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString(), new com.aspose.pdf.TeXLoadOptions())) {
        document.save(outputFile.toString());
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## Mengonversi PostScript ke PDF

Gunakan contoh ini ketika file PostScript harus dikonversi menjadi dokumen PDF.

1. Buka sumber PostScript dengan [`PsLoadOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/psloadoptions/) di konstruktor [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Biarkan Aspose.PDF menerjemahkan aliran deskripsi halaman PostScript menjadi model dokumen PDF.
1. Simpan file PDF yang telah dikonversi.

```java
public static void convertPostScripToPdf(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString(), new PsLoadOptions())) {
        document.save(outputFile.toString());
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## Mengonversi EPS ke PDF

Gunakan contoh ini ketika file Encapsulated PostScript harus dikonversi ke PDF.

1. Buka sumber EPS dengan [`PsLoadOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/psloadoptions/) karena EPS mengikuti jalur pemuatan berbasis PostScript yang sama.
1. Muat file ke dalam a [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) jadi konten deskripsi halaman dikonversi selama impor.
1. Simpan PDF output.

```java
public static void convertEpsToPdf(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString(), new PsLoadOptions())) {
        document.save(outputFile.toString());
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## Mengonversi EPUB ke PDF

Gunakan contoh ini ketika sebuah eBook EPUB harus dikonversi menjadi PDF.

1. Buka sumber EPUB dengan melewatkan jalur file dan [`EpubLoadOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/epubloadoptions/) ke dalam konstruktor [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Biarkan Aspose.PDF memuat struktur ebook dan mengubahnya menjadi halaman PDF.
1. Simpan PDF yang dikonversi.

```java
public static void convertEpubToPdf(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString(), new EpubLoadOptions())) {
        document.save(outputFile.toString());
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## Mengubah Markdown menjadi PDF

Gunakan contoh ini ketika konten Markdown harus dirender dan disimpan sebagai PDF.

1. Buka sumber Markdown dengan melewatkan jalur file dan [`MdLoadOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/mdloadoptions/) ke dalam konstruktor [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Biarkan Aspose.PDF menginterpretasikan konten Markdown dan merendernya menjadi konten halaman PDF.
1. Simpan file PDF output.

```java
public static void convertMdToPdf(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString(), new MdLoadOptions())) {
        document.save(outputFile.toString());
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## Mengonversi teks ke PDF dengan alur kerja sederhana

Gunakan contoh ini ketika file teks biasa harus segera dikonversi ke PDF.

1. Baca sumber teks biasa dengan pengodean UTF-8 sehingga konten teks tersedia sebagai string Java.
1. Buat sebuah kosong [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) dan tambahkan [`Page`](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/).
1. Bungkus teks dalam sebuah [`TextFragment`](https://reference.aspose.com/pdf/java/com.aspose.pdf/textfragment/) dan tambahkan ke koleksi paragraf halaman.
1. Simpan PDF yang dihasilkan.

```java
public static void convertTxtToPdfSimple(Path inputFile, Path outputFile) throws Exception {
    String textContent = Files.readString(inputFile, StandardCharsets.UTF_8);
    try (Document document = new Document()) {
        Page page = document.getPages().add();
        page.getParagraphs().add(new TextFragment(textContent));
        page.close();
        document.save(outputFile.toString());
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## Mengonversi teks ke PDF dengan opsi lanjutan

Gunakan contoh ini ketika teks biasa harus dikonversi dengan opsi tata letak atau enkoding tambahan.

1. Baca semua baris teks dari file input sehingga penanda jeda halaman dapat diperiksa selama konversi.
1. Buat sebuah kosong [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) dan konfigurasikan masing-masing [`Page`](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) dengan margin dan keadaan teks default.
1. Selesaikan font monospaced melalui [`FontRepository`](https://reference.aspose.com/pdf/java/com.aspose.pdf/fontrepository/) dan tambahkan setiap baris sebagai [`TextFragment`](https://reference.aspose.com/pdf/java/com.aspose.pdf/textfragment/).
1. Simpan file output setelah loop pembuatan halaman selesai.

```java
public static void convertTxtToPdf(Path inputFile, Path outputFile) throws Exception {
    List<String> lines = Files.readAllLines(inputFile);
    try (Document document = new Document()) {
        com.aspose.pdf.Page page = document.getPages().add();
        page.getPageInfo().getMargin().setLeft(20);
        page.getPageInfo().getMargin().setRight(10);
        page.getPageInfo().getDefaultTextState().setFont(FontRepository.findFont("Courier New"));
        page.getPageInfo().getDefaultTextState().setFontSize(12);

        int pageCount = 1;
        for (String line : lines) {
            if (!line.isEmpty() && line.charAt(0) == '\f') {
                page = document.getPages().add();
                page.getPageInfo().getMargin().setLeft(20);
                page.getPageInfo().getMargin().setRight(10);
                page.getPageInfo().getDefaultTextState().setFont(FontRepository.findFont("Courier New"));
                page.getPageInfo().getDefaultTextState().setFontSize(12);
                pageCount++;
                if (pageCount == 4) {
                    break;
                }
            } else {
                page.getParagraphs().add(new TextFragment(line));
            }
        }
        document.save(outputFile.toString());
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## Mengonversi PCL ke PDF

Gunakan contoh ini ketika aliran cetak PCL harus dikonversi menjadi PDF.

1. Buat [`PclLoadOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/pclloadoptions/) dan aktifkan penekanan kesalahan parsing ketika perilaku impor yang lunak diperlukan.
1. Buka sumber PCL dengan melewatkan jalur file dan opsi pemuatan ke dalam konstruktor [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Simpan hasil sebagai PDF.

```java
public static void convertPclToPdf(Path inputFile, Path outputFile) {
    PclLoadOptions loadOptions = new PclLoadOptions();
    loadOptions.setSupressErrors(true);
    try (Document document = new Document(inputFile.toString(), loadOptions)) {
        document.save(outputFile.toString());
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## Mengonversi XML ke PDF melalui XSLT dan HTML

Gunakan contoh ini ketika data XML harus diubah sebelum pembuatan PDF akhir.

1. Transformasikan sumber XML dengan file XSLT menjadi file HTML sementara dengan memanggil metode transformasi khusus.
1. Masukkan file HTML yang dihasilkan ke dalam fungsi konversi HTML-ke-PDF yang ada sehingga PDF akhir menggunakan standar [`HtmlLoadOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/htmlloadoptions/) alur kerja.
1. Hapus file HTML sementara dalam blok `finally` setelah konversi selesai.
1. Simpan file PDF yang dihasilkan.

```java
public static void convertXmlToPdf(Path xsltFile, Path xmlFile, Path outputFile) throws Exception {
    Path htmlFile = Files.createTempFile("aspose-pdf-xml-", ".html");
    try {
        transformXmlToHtml(xmlFile, xsltFile, htmlFile);
        HtmlToPdfExamples.convertHtmlToPdf(htmlFile, outputFile);
    } finally {
        Files.deleteIfExists(htmlFile);
    }
    System.out.println(xmlFile + " converted into " + outputFile);
}
```

## Mengubah XPS ke PDF

Gunakan contoh ini ketika dokumen XPS harus dikonversi menjadi PDF.

1. Buka sumber XPS dengan melewatkan jalur file dan [`XpsLoadOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/xpsloadoptions/) ke dalam konstruktor [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Biarkan Aspose.PDF menginterpretasikan deskripsi halaman XPS selama pemuatan dokumen.
1. Simpan PDF yang dikonversi.

```java
public static void convertXpsToPdf(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString(), new XpsLoadOptions())) {
        document.save(outputFile.toString());
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## Mengonversi XSL-FO ke PDF

Gunakan contoh ini ketika konten XSL-FO harus dirender sebagai PDF.

1. Buat [`XslFoLoadOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/xslfoloadoptions/) dengan jalur XSLT sehingga sumber XML dapat diubah selama pemuatan.
1. Konfigurasikan mode penanganan kesalahan parsing untuk melempar segera saat XSL-FO yang tidak valid ditemukan.
1. Buka sumber XML dalam sebuah [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) dengan opsi pemuatan tersebut.
1. Simpan dokumen PDF yang dihasilkan.

```java
public static void convertXslFoToPdf(Path xsltFile, Path xmlFile, Path outputFile) {
    XslFoLoadOptions loadOptions = new XslFoLoadOptions(xsltFile.toString());
    loadOptions.setParsingErrorsHandlingType(XslFoLoadOptions.ParsingErrorsHandlingTypes.ThrowExceptionImmediately);
    try (Document document = new Document(xmlFile.toString(), loadOptions)) {
        document.save(outputFile.toString());
    }
    System.out.println(xmlFile + " converted into " + outputFile);
}
```

## Mengubah XML menjadi HTML menengah

Gunakan metode ini ketika data XML harus diubah menjadi HTML sebelum langkah konversi PDF akhir.

1. Buka file input XML dan XSLT sebagai sumber transformasi.
1. Buat sebuah `Transformer` dari stylesheet XSLT dan jalankan terhadap sumber XML.
1. Tuliskan file HTML yang telah diubah ke disk sehingga fungsi konversi PDF hilir dapat memuatnya.

```java
private static void transformXmlToHtml(Path xmlFile, Path xsltFile, Path htmlFile) throws Exception {
    Transformer transformer = TransformerFactory.newInstance()
            .newTransformer(new StreamSource(xsltFile.toFile()));
    transformer.transform(new StreamSource(xmlFile.toFile()), new StreamResult(htmlFile.toFile()));
}
```
