---
title: Menambahkan Anotasi ke File PDF yang Ada
type: docs
weight: 80
url: /java/adding-annotations-to-existing-pdf-file/
description: Bagian ini menjelaskan cara menambahkan Anotasi ke file PDF yang ada dengan Aspose.PDF Facades.
lastmod: "2021-06-30"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Menambahkan Anotasi Teks Bebas di File PDF yang Ada (facades)

Sebuah anotasi teks bebas menampilkan teks langsung di halaman. [PdfContentEditor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfContentEditor) memungkinkan Anda menambahkan anotasi dari berbagai jenis pada file PDF yang ada. Anda dapat menggunakan metode yang sesuai untuk menambahkan anotasi tertentu. Misalnya, dalam cuplikan kode berikut, kami telah menggunakan metode [createFreeText](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfContentEditor#createFreeText-java.awt.Rectangle-java.lang.String-int-) untuk menambahkan anotasi tipe FreeText.

Jenis anotasi apa pun dapat ditambahkan ke file PDF dengan cara yang sama.
 Pertama-tama, Anda perlu membuat objek dari jenis [PdfContentEditor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfContentEditor) dan mengikat file PDF input menggunakan metode bindPdf. Kedua, Anda harus membuat objek Rectangle untuk menentukan area anotasi. Setelah itu, Anda dapat memanggil metode [createFreeText](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfContentEditor#createFreeText-java.awt.Rectangle-java.lang.String-int-) untuk menambahkan anotasi FreeText, nomor halaman di mana anotasi berada, dan kemudian menggunakan metode save untuk menyimpan file PDF yang diperbarui.

Cuplikan kode berikut menunjukkan kepada Anda cara menambahkan anotasi teks bebas dalam file PDF.

```java
  public static void AddFreeTextAnnotation()
    {
        var document = new Document(_dataDir + "sample.pdf");
        PdfContentEditor editor = new PdfContentEditor(document);
        TextFragmentAbsorber tfa = new TextFragmentAbsorber("PDF");
        tfa.visit(document.getPages().get_Item(1));

        java.awt.Rectangle rect = new  java.awt.Rectangle();
        rect.x = (int)tfa.getTextFragments().get_Item(1).getRectangle().getLLX();
        rect.y = (int)tfa.getTextFragments().get_Item(1).getRectangle().getURY() + 5;
        rect.height = 18;
        rect.width = 100;        

        editor.createFreeText(rect, "Free Text Demo", 1); // parameter terakhir adalah nomor halaman
        editor.save(_dataDir + "PdfContentEditorDemo_FreeTextAnnotation.pdf");
    }
```

## Tambahkan Anotasi Teks dalam File PDF yang Ada (facades)

Dalam contoh ini juga, Anda perlu membuat objek dari tipe [PdfContentEditor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfContentEditor) dan mengaitkan file PDF input menggunakan metode [bindPdf](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfContentEditor#bindPdf-java.lang.String-). Kedua, Anda harus membuat objek Rectangle untuk menentukan area anotasi. Setelah itu, Anda dapat memanggil metode [createFreeText](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfContentEditor#createFreeText-java.awt.Rectangle-java.lang.String-int-) untuk menambahkan anotasi FreeText, membuat judul anotasi Anda, dan nomor halaman tempat anotasi berada.

```java
 public static void AddTextAnnotation()
    {
        var document = new Document(_dataDir + "sample.pdf");
        PdfContentEditor editor = new PdfContentEditor(document);
        TextFragmentAbsorber tfa = new TextFragmentAbsorber("PDF");
        tfa.visit(document.getPages().get_Item(1));

        java.awt.Rectangle rect = new  java.awt.Rectangle();
        rect.x = (int)tfa.getTextFragments().get_Item(1).getRectangle().getLLX();
        rect.y = (int)tfa.getTextFragments().get_Item(1).getRectangle().getURY() + 5;
        rect.height = 18;
        rect.width = 100;        

        editor.createText(rect, "Pengguna Aspose", "PDF adalah format yang lebih baik untuk dokumen modern", false, "Key", 1);
        editor.save(_dataDir + "PdfContentEditorDemo_TextAnnotation.pdf");
    }
```


## Menambahkan Anotasi Garis dalam File PDF yang Ada (facades)

Kami juga menentukan Rectangle, koordinat awal dan akhir garis, nomor halaman, ketebalan, gaya dan warna bingkai anotasi, jenis garis putus-putus, jenis awal dan akhir garis.

```java

    public static void AddLineAnnotation()
    {
        var document = new Document(_dataDir + "Appartments.pdf");
        PdfContentEditor editor = new PdfContentEditor(document);
        // Buat Anotasi Garis
        editor.createLine(
            new java.awt.Rectangle(550, 93, 562, 439),
            "Test",
            556, 99, 556, 443, 1, 1,
            java.awt.Color.RED,
            "dash",
            new int[] { 1, 0, 3 },
            new String[] { "Open", "Open" });
        editor.save(_dataDir + "PdfContentEditorDemo_LineAnnotation.pdf");
    }
```