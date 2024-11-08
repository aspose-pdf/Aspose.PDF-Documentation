---
title: PDF Text Annotation
Texttitle: Text Annotation
type: docs
weight: 10
url: /id/java/text-annotation/
description: Aspose.PDF untuk Java memungkinkan Anda untuk Menambahkan, Mendapatkan, dan Menghapus Anotasi Teks dari dokumen PDF Anda.
lastmod: "2021-11-24"
sitemap:
    changefreq: "monthly"
    priority: 0.5
---

Tambahkan, Hapus, dan Dapatkan Anotasi serupa untuk berbagai jenis anotasi. Mari ambil contoh Anotasi Teks.

## Cara menambahkan Anotasi Teks ke dalam file PDF yang ada

Dalam tutorial ini, Anda akan belajar bagaimana menambahkan teks ke dokumen PDF yang ada. Alat teks memungkinkan Anda menambahkan teks di mana saja dalam dokumen. Anotasi Teks adalah anotasi yang ditempelkan pada lokasi tertentu dalam dokumen PDF. Ketika ditutup, anotasi ditampilkan sebagai ikon; ketika dibuka, itu akan menampilkan jendela pop-up yang berisi teks catatan dalam font dan ukuran yang dipilih oleh pembaca.

Anotasi terkandung oleh koleksi [Annotations](https://reference.aspose.com/pdf/java/com.aspose.pdf/class-use/AnnotationCollection) dari Halaman tertentu.
 Koleksi ini hanya berisi anotasi untuk halaman individu tersebut; setiap halaman memiliki koleksi Anotasi sendiri.

Untuk menambahkan anotasi ke halaman tertentu, tambahkan ke koleksi Anotasi halaman tersebut dengan metode Add.

1. Pertama, buat anotasi yang ingin Anda tambahkan ke PDF.
1. Kemudian buka PDF masukan.
1. Tambahkan anotasi ke koleksi Anotasi objek [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page).

Cuplikan kode berikut menunjukkan cara menambahkan anotasi pada halaman PDF.

```java
package com.aspose.pdf.examples;

import com.aspose.pdf.*;
import java.util.*;

public class ExampleTextAnnotation {

    private static String _dataDir = "/home/aspose/pdf-examples/Samples/";

    public static void AddTextAnnotation()
    {
        // Memuat file PDF
        Document document = new Document(_dataDir + "sample.pdf");
        Page page = document.getPages().get_Item(1);
        Rectangle rect = new Rectangle(200, 750, 400, 790);
        TextAnnotation textAnnotation = new TextAnnotation(page, rect);

        textAnnotation.setTitle("Pengguna Aspose");
        textAnnotation.setSubject("Subjek Contoh");
        textAnnotation.setState (AnnotationState.Accepted);
        textAnnotation.setContents("Isi contoh untuk anotasi");
        textAnnotation.setOpen(true);
        textAnnotation.setIcon(TextIcon.Circle);

        Border border = new Border(textAnnotation);
        border.setWidth(5);
        border.setDash(new Dash(1, 1));
        textAnnotation.setBorder(border);
        textAnnotation.setRect(rect);

        page.getAnnotations().add(textAnnotation);
        document.save(_dataDir + "sample_textannot.pdf");
    }
}
```

## Tambahkan (atau Buat) Anotasi Teks Bebas Baru

Anotasi teks bebas menampilkan teks langsung pada halaman. Metode PdfContentEditor.CreateFreeText memungkinkan pembuatan jenis anotasi ini. Dalam potongan berikut, kami menambahkan anotasi teks bebas di atas kemunculan pertama dari string.

```java
package com.aspose.pdf.examples;

import com.aspose.pdf.*;
import java.util.*;

public class ExampleFreeTextAnnotation {

    private static String _dataDir = "/home/aspose/pdf-examples/Samples/";

    public static void AddFreeTextAnnotation()
    {
        // Memuat file PDF
        Document document = new Document(_dataDir + "sample.pdf");
        Page page = document.getPages().get_Item(1);

        DefaultAppearance defaultAppearance = new DefaultAppearance();
        defaultAppearance.setFontName("Helvetica");
        defaultAppearance.setFontSize(12);
        defaultAppearance.setTextColor(java.awt.Color.BLUE);

        FreeTextAnnotation freeTextAnnotation = new FreeTextAnnotation(page, new Rectangle(300.0, 770.0, 400.0, 790.0), defaultAppearance);

        freeTextAnnotation.setRichText("Demo Teks Bebas");
        page.getAnnotations().add(freeTextAnnotation);
        document.save(_dataDir + "sample_freetext.pdf");
    }
}
```


## Dapatkan Anotasi Teks Bebas

Aspose.PDF untuk Java memungkinkan Anda mendapatkan Anotasi Teks Bebas dari dokumen PDF Anda.

Silakan, periksa cuplikan kode berikut untuk menyelesaikan tugas ini:

```java
public static void GetFreeTextAnnotation() {
        // Memuat file PDF
        Document document = new Document(_dataDir + "sample_freetext.pdf");

        // Memfilter anotasi menggunakan AnnotationSelector
        Page page = document.getPages().get_Item(1);
        AnnotationSelector annotationSelector = new AnnotationSelector(
                new FreeTextAnnotation(page, Rectangle.getTrivial(), new DefaultAppearance()));
        page.accept(annotationSelector);
        List<Annotation> freeTextAnnotations = annotationSelector.getSelected();

        // mencetak hasil
        for (Annotation fa : freeTextAnnotations) {
            System.out.println(fa.getRect());
        }
    }
```

## Hapus Anotasi Teks Bebas

Aspose.PDF untuk Java memungkinkan Anda menghapus Anotasi Teks Bebas dari dokumen PDF Anda.

Silakan, periksa cuplikan kode berikut untuk menyelesaikan tugas ini:

```java
  public static void DeleteFreeTextAnnotation() {
         // Muat file PDF
         Document document = new Document(_dataDir + "sample_freetext.pdf");

         // Saring anotasi menggunakan AnnotationSelector
         Page page = document.getPages().get_Item(1);
         AnnotationSelector annotationSelector = new AnnotationSelector(
                 new FreeTextAnnotation(page, Rectangle.getTrivial(), new DefaultAppearance()));
         page.accept(annotationSelector);
         List<Annotation> freeTextAnnotations = annotationSelector.getSelected();

         // hapus anotasi
         for (Annotation fa : freeTextAnnotations) {
            page.getAnnotations().delete(fa);
        }
        document.save(_dataDir + "sample_freetext_del.pdf");
    }
```

## Hapus Semua Anotasi dari Halaman File PDF

Koleksi [AnnotationCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf/class-use/AnnotationCollection) dari objek [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page) berisi semua anotasi untuk halaman tersebut.
 Untuk menghapus semua anotasi dari sebuah halaman, panggil metode *Delete* dari koleksi AnnotationCollection.

Cuplikan kode berikut menunjukkan cara menghapus semua anotasi dari halaman tertentu.

```java
    public static void DeleteTextAnnotation() {
         // Muat file PDF
         Document document = new Document(_dataDir + "sample_textannot.pdf");

         // Saring anotasi menggunakan AnnotationSelector
         Page page = document.getPages().get_Item(1);
         AnnotationSelector annotationSelector = new AnnotationSelector(
                 new TextAnnotation(page, Rectangle.getTrivial()));
         page.accept(annotationSelector);
         List<Annotation> TextAnnotations = annotationSelector.getSelected();

         // hapus anotasi
         for (Annotation fa : TextAnnotations) {
            page.getAnnotations().delete(fa);
        }
        document.save(_dataDir + "sample_textannot_del.pdf");
    }
```

## Dapatkan Semua Anotasi dari Halaman Dokumen PDF

Aspose.PDF memungkinkan Anda mendapatkan anotasi dari seluruh dokumen, atau dari halaman tertentu. Untuk mendapatkan semua anotasi dari halaman dalam dokumen PDF, lakukan iterasi melalui koleksi [AnnotationCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf/class-use/AnnotationCollection) dari sumber daya halaman yang diinginkan. Potongan kode berikut menunjukkan cara mendapatkan semua anotasi dari sebuah halaman.

```java
  public static void GetTextAnnotation() {
        // Muat file PDF
        Document document = new Document(_dataDir + "sample_textannot.pdf");

        // Saring anotasi menggunakan AnnotationSelector
        Page page = document.getPages().get_Item(1);
        AnnotationSelector annotationSelector = new AnnotationSelector(
                new TextAnnotation(page, Rectangle.getTrivial()));
        page.accept(annotationSelector);
        List<Annotation> TextAnnotations = annotationSelector.getSelected();

        // cetak hasil
        for (Annotation fa : TextAnnotations) {
            System.out.println(fa.getRect());
        }
    }
```