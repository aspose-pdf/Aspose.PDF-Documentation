---
title: Page Break dalam PDF yang Ada
type: docs
weight: 30
url: /java/page-break-in-existing-pdf/
description: Bagian ini menjelaskan cara memecah halaman dalam PDF yang ada menggunakan kelas PdfFileEditor.
lastmod: "2021-06-05"
draft: false
---

Sebagai tata letak default, konten di dalam file PDF ditambahkan dalam tata letak Kiri-Atas ke Kanan-Bawah. Setelah konten melebihi batas bawah halaman, pemisahan halaman terjadi. Namun, Anda mungkin menemui persyaratan untuk menyisipkan pemisahan halaman tergantung pada kebutuhan. Sebuah metode bernama AddPageBreak(...) ditambahkan dalam kelas [PdfFileEditor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileEditor) untuk memenuhi kebutuhan ini.

1. [public void AddPageBreak(Document src, Document dest, PageBreak[] pageBreaks)](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileEditor#addPageBreak-com.aspose.pdf.IDocument-com.aspose.pdf.IDocument-com.aspose.pdf.facades.PdfFileEditor.PageBreak:A-)

1. [public void AddPageBreak(string src, string dest, PageBreak[] pageBreaks)](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileEditor#addPageBreak-java.lang.String-java.lang.String-com.aspose.pdf.facades.PdfFileEditor.PageBreak:A-)
1. [public void AddPageBreak(Stream src, Stream dest, PageBreak[] pageBreaks)](https://docs.oracle.com/javase/7/docs/api/java/io/InputStream.html?is-external=true)

- src adalah dokumen sumber/jalur ke dokumen/aliran dengan dokumen sumber
- dest adalah dokumen tujuan/jalur tempat dokumen akan disimpan/aliran tempat dokumen akan disimpan
- PageBreak adalah array dari objek pemisah halaman. Ini memiliki dua properti: indeks halaman tempat pemisah halaman harus ditempatkan dan posisi vertikal dari pemisah halaman pada halaman.

## Contoh 1 (Menambahkan pemisah halaman)

```java
   public static void PageBrakeExample01() {
        // Membuat instance Dokumen
        Document doc = new Document(_dataDir + "Sample-Document-01.pdf");
        // Membuat instance Dokumen kosong
        Document dest = new Document();
        // Membuat objek PdfFileEditor
        PdfFileEditor fileEditor = new PdfFileEditor();
        fileEditor.AddPageBreak(doc, dest, new PdfFileEditor.PageBreak[] { new PdfFileEditor.PageBreak(1, 450) });
        // Simpan file hasil
        dest.Save(_dataDir + "PageBreak_out.pdf");
    }
```


## Contoh 2

```java
  public static void PageBrakeExample02() {
        // Buat objek PdfFileEditor
        PdfFileEditor fileEditor = new PdfFileEditor();

        fileEditor.AddPageBreak(_dataDir + "Sample-Document-02.pdf", _dataDir + "PageBreakWithDestPath_out.pdf",
                new PdfFileEditor.PageBreak[] { new PdfFileEditor.PageBreak(1, 450) });
    }
```

## Contoh 3

```java
 public static void PageBrakeExample03() {
        Stream src = new FileStream(_dataDir + "Sample-Document-03.pdf", FileMode.Open, FileAccess.Read);
        Stream dest = new FileStream(_dataDir + "PageBreakWithStream_out.pdf", FileMode.Create, FileAccess.ReadWrite);
        PdfFileEditor fileEditor = new PdfFileEditor();
        fileEditor.AddPageBreak(src, dest, new PdfFileEditor.PageBreak[] { new PdfFileEditor.PageBreak(1, 450) });
        dest.Close();
        src.Close();
    }
```