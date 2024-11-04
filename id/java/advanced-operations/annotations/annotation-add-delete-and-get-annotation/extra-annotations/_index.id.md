---
title: Menggunakan jenis anotasi PDF tambahan
linktitle: Anotasi Tambahan
type: docs
weight: 60
url: /java/extra-annotations/
description: Bagian ini menjelaskan cara menambahkan, mendapatkan, dan menghapus jenis anotasi tambahan dari dokumen PDF Anda.
lastmod: "2021-11-24"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Cara menambahkan Anotasi Caret ke file PDF yang sudah ada

Anotasi Caret adalah simbol yang menunjukkan pengeditan teks. Anotasi Caret juga merupakan anotasi markup, jadi kelas Caret berasal dari kelas Markup dan juga menyediakan fungsi untuk mendapatkan atau mengatur properti Anotasi Caret dan mengatur ulang alur tampilan Anotasi Caret.

Langkah-langkah untuk membuat anotasi Caret:

1. Memuat file PDF - baru [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document).

1. Buat [Caret Annotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/CaretAnnotation) baru dan atur parameter Caret (new Rectangle, title, Subject, Flags, color, width, StartingStyle dan EndingStyle). Anotasi ini digunakan untuk menunjukkan penyisipan teks.
1. Buat [StrikeOutAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf.class-use/StrikeOutAnnotation) baru dan atur parameter (new Rectangle, title, color, new QuadPoints dan new points, Subject, InReplyTo, ReplyType).
1. Setelah itu kita bisa menambahkan anotasi ke halaman.

Cuplikan kode berikut menunjukkan cara menambahkan Anotasi Caret ke file PDF:

```java
package com.aspose.pdf.examples;

import java.util.*;
import com.aspose.pdf.*;

public class ExampleCaretAnnotation {
    private static String _dataDir = "/home/admin1/pdf-examples/Samples/";

    public static void AddCaretAnnotation() {
        // Memuat file PDF
        Document document = new Document(_dataDir + "sample.pdf");
        // Anotasi ini digunakan untuk menunjukkan penyisipan teks
        CaretAnnotation caretAnnotation1 = new CaretAnnotation(
                document.getPages().get_Item(1), new Rectangle(299.988, 713.664, 308.708, 720.769));
        caretAnnotation1.setTitle("Aspose User");
        caretAnnotation1.setSubject("Inserted text 1");
        caretAnnotation1.setFlags(AnnotationFlags.Print);
        caretAnnotation1.setColor(Color.getBlue());

        // Anotasi ini digunakan untuk menunjukkan penggantian teks
        CaretAnnotation caretAnnotation2 = new CaretAnnotation(
                document.getPages().get_Item(1), new Rectangle(361.246, 727.908, 370.081, 735.107));

        caretAnnotation2.setTitle("Aspose User");
        caretAnnotation2.setFlags(AnnotationFlags.Print);
        caretAnnotation2.setSubject("Inserted text 2");
        caretAnnotation2.setColor(Color.getBlue());

        StrikeOutAnnotation strikeOutAnnotation = new StrikeOutAnnotation(
                document.getPages().get_Item(1), new Rectangle(318.407, 727.826, 368.916, 740.098));

        strikeOutAnnotation.setColor(Color.getBlue());
        strikeOutAnnotation.setQuadPoints(new Point[] { new Point(321.66, 739.416),
                new Point(365.664, 739.416), new Point(321.66, 728.508),
                new Point(365.664, 728.508) });

        strikeOutAnnotation.setSubject("Cross-out");
        strikeOutAnnotation.setInReplyTo(caretAnnotation2);
        strikeOutAnnotation.setReplyType(ReplyType.Group);

        document.getPages().get_Item(1).getAnnotations().add(caretAnnotation1);
        document.getPages().get_Item(1).getAnnotations().add(caretAnnotation2);
        document.getPages().get_Item(1).getAnnotations().add(strikeOutAnnotation);

        document.save(_dataDir + "sample_caret.pdf");

    }
```


## Dapatkan Anotasi Caret

Silakan coba gunakan potongan kode berikut untuk Mendapatkan Anotasi Caret dalam dokumen PDF

```java
    public static void GetCaretAnnotation() {
        // Memuat file PDF
        Document document = new Document(_dataDir + "sample_caret.pdf");

        // Memfilter anotasi menggunakan AnnotationSelector
        Page page = document.getPages().get_Item(1);
        AnnotationSelector annotationSelector = new AnnotationSelector(
                new CaretAnnotation(page, Rectangle.getTrivial()));
        page.accept(annotationSelector);
        List<Annotation> caretAnnotations = annotationSelector.getSelected();

        // mencetak hasil
        for (Annotation ca : caretAnnotations) {
            System.out.println(ca.getRect());
        }
    }
```

## Hapus Anotasi Caret

Potongan kode berikut menunjukkan cara Menghapus Anotasi Caret dari file PDF.

```java
public static void DeleteCaretAnnotation() {
        // Memuat file PDF
        Document document = new Document(_dataDir + "sample_caret.pdf");

        // Memfilter anotasi menggunakan AnnotationSelector
        Page page = document.getPages().get_Item(1);
        AnnotationSelector annotationSelector = new AnnotationSelector(
                new CaretAnnotation(page, Rectangle.getTrivial()));
        page.accept(annotationSelector);
        List<Annotation> caretAnnotations = annotationSelector.getSelected();

        // menghapus anotasi
        for (Annotation ca : caretAnnotations) {
            document.getPages().get_Item(1).getAnnotations().delete(ca);
        }
        document.save(_dataDir + "sample_caret_del.pdf");
    }
```


A [Link Annotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/LinkAnnotation) adalah tautan hypertext yang mengarah ke tujuan di tempat lain dalam dokumen atau ke sebuah tindakan yang akan dilakukan.

## Tambahkan Anotasi Tautan

Sebuah Tautan adalah area persegi panjang yang dapat ditempatkan di mana saja di halaman. Setiap tautan memiliki aksi PDF yang sesuai terkait dengannya. Aksi ini dilakukan ketika pengguna mengklik area dari tautan ini.

Cuplikan kode berikut menunjukkan cara menambahkan Anotasi Tautan ke file PDF menggunakan contoh nomor telepon:

```java
package com.aspose.pdf.examples;

import java.util.*;
import com.aspose.pdf.*;

public class ExampleLinkAnnotation {

    // Jalur ke direktori dokumen.

    private static String _dataDir = "/home/admin1/pdf-examples/Samples/";

    public static void AddLinkAnnotation() {
        try {
            // Memuat file PDF
            Document document = new Document(_dataDir + "SimpleResume.pdf");
            Page page = document.getPages().get_Item(1);

            // Buat objek TextFragmentAbsorber untuk menemukan nomor telepon
            TextFragmentAbsorber textFragmentAbsorber = new TextFragmentAbsorber("678-555-0103");

            // Terima absorber hanya untuk halaman pertama
            page.accept(textFragmentAbsorber);

            TextFragment phoneNumberFragment = textFragmentAbsorber.getTextFragments().get_Item(1);

            // Buat Anotasi Tautan dan atur aksi untuk menelepon nomor telepon
            LinkAnnotation linkAnnotation = new LinkAnnotation(page, phoneNumberFragment.getRectangle());
            linkAnnotation.setAction(new GoToURIAction("callto:678-555-0103"));

            // Tambahkan anotasi ke halaman
            page.getAnnotations().add(linkAnnotation);
            document.save(_dataDir + "SimpleResume_mod.pdf");
        } catch (Exception ex) {
            System.out.println(ex.getMessage());
        }
    }
```


## Dapatkan Anotasi Tautan

Silakan coba menggunakan potongan kode berikut untuk Mendapatkan LinkAnnotation dari dokumen PDF.

```java
    public static void GetLinkAnnotations() {

        // Muat file PDF
        Document document = new Document(_dataDir + "SimpleResume_mod.pdf");

        // Saring anotasi menggunakan AnnotationSelector
        Page page = document.getPages().get_Item(1);
        AnnotationSelector annotationSelector = new AnnotationSelector(
                new LinkAnnotation(page, Rectangle.getTrivial()));
        page.accept(annotationSelector);
        List<Annotation> linkAnnotations = annotationSelector.getSelected();

        // cetak hasil
        for (Annotation la : linkAnnotations) {

            LinkAnnotation l = (LinkAnnotation) la;

            // Cetak URL dari setiap Anotasi Tautan
            System.out.println("URI: " + ((GoToURIAction) l.getAction()).getURI());

            TextAbsorber absorber = new TextAbsorber();
            absorber.getTextSearchOptions().setLimitToPageBounds(true);
            absorber.getTextSearchOptions().setRectangle(l.getRect());
            page.accept(absorber);

            String extractedText = absorber.getText();

            // Cetak teks yang terkait dengan hyperlink
            System.out.println(extractedText);
        }
    }
```


## Hapus Anotasi Tautan

Cuplikan kode berikut menunjukkan cara Menghapus Anotasi Tautan dari file PDF. Untuk ini kita perlu menemukan dan menghapus semua anotasi tautan pada halaman pertama. Setelah itu kita akan menyimpan dokumen dengan anotasi yang dihapus.

```java
    public static void DeleteLinkAnnotations() {
        // Memuat file PDF
        Document document = new Document(_dataDir + "SimpleResume_mod.pdf");

        // Memfilter anotasi menggunakan AnnotationSelector
        Page page = document.getPages().get_Item(1);
        AnnotationSelector annotationSelector = new AnnotationSelector(
                new LinkAnnotation(page, Rectangle.getTrivial()));
        page.accept(annotationSelector);
        List<Annotation> linkAnnotations = annotationSelector.getSelected();

        for (Annotation la : linkAnnotations)
            page.getAnnotations().delete(la);

        // Menyimpan dokumen dengan anotasi yang dihapus
        document.save(_dataDir + "SimpleResume_del.pdf");
    }
```

## Menyunting wilayah halaman tertentu dengan Anotasi Penyuntingan menggunakan Aspose.PDF untuk Java

Aspose.PDF untuk Java mendukung fitur untuk menambahkan serta memanipulasi Anotasi dalam file PDF yang sudah ada. Baru-baru ini beberapa pelanggan kami mengajukan permintaan untuk menyunting (menghapus teks, gambar, dll elemen dari) area halaman tertentu dari dokumen PDF. Untuk memenuhi kebutuhan ini, sebuah kelas bernama RedactionAnnotation disediakan, yang dapat digunakan untuk menyunting area halaman tertentu atau dapat digunakan untuk memanipulasi RedactionAnnotations yang sudah ada dan menyuntingnya (yaitu, meratakan anotasi dan menghapus teks di bawahnya).

```java
package com.aspose.pdf.examples;

import com.aspose.pdf.*;
import com.aspose.pdf.facades.PdfAnnotationEditor;

public class ExampleRedactAnnotation {
    private static String _dataDir = "/home/admin1/pdf-examples/Samples/";

    public static void RedactionAnnotation() {

        // Buka dokumen
        Document document = new Document(_dataDir + "sample.pdf");
        Page page = document.getPages().get_Item(1);

        // Buat instance RedactionAnnotation untuk area halaman tertentu
        RedactionAnnotation annot = new RedactionAnnotation(page, new Rectangle(200, 500, 300, 600));
        annot.setFillColor(Color.getGreen());
        annot.setBorderColor(Color.getYellow());
        annot.setColor(Color.getBlue());

        // Teks yang akan dicetak pada anotasi sunting
        annot.setOverlayText("REDACTED");
        annot.setTextAlignment(HorizontalAlignment.Center);

        // Ulangi teks Overlay di atas Anotasi sunting
        annot.setRepeat(true);

        // Tambahkan anotasi ke koleksi anotasi halaman pertama
        page.getAnnotations().add(annot);

        // Meratakan anotasi dan menyunting konten halaman (yaitu menghapus teks dan gambar
        // Di bawah anotasi yang disunting)
        annot.redact();
        document.save(_dataDir + "RedactPage_out.pdf");
    }
```


## Pendekatan Facades

Namespace Aspose.PDF.Facades juga memiliki kelas bernama [PdfAnnotationEditor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfAnnotationEditor) yang menyediakan fitur untuk memanipulasi Anotasi yang ada di dalam file PDF. Kelas ini mengandung metode bernama [RedactArea(..)](https://reference.aspose.com/pdf/java/com.aspose.pdf/Redaction#getredactArea-com.aspose.pdf.Page-com.aspose.pdf.Rectangle-java.awt.Color-) yang menyediakan kemampuan untuk menghapus area tertentu di halaman.

```java
    public static void RedactionAnnotationFacades(){
        PdfAnnotationEditor editor = new PdfAnnotationEditor();

        editor.bindPdf(_dataDir + "sample.pdf");

        // Menghapus area tertentu pada halaman
        editor.redactArea(1, new Rectangle(100, 100, 20, 70), java.awt.Color.white);
        editor.bindPdf(_dataDir + "sample.pdf");
        editor.save( _dataDir + "FacadesApproach_out.pdf");
    }
```