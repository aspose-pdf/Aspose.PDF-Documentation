---
title: PDF Highlights Annotation 
linktitle: Highlights Annotation
type: docs
weight: 20
url: id/java/highlights-annotation/
description: Anotasi Markup ditampilkan dalam teks sebagai sorotan, garis bawah, coretan, atau garis bawah bergelombang dalam teks dokumen.
lastmod: "2021-11-24"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

Anotasi Teks Markup akan muncul sebagai sorotan, garis bawah, coretan, atau garis bawah bergelombang dalam teks dokumen. Ketika dibuka, mereka akan menampilkan jendela pop-up yang berisi teks dari catatan terkait.

Properti dari anotasi teks markup dalam dokumen PDF dapat diedit menggunakan jendela properti yang disediakan dalam kontrol penampil PDF. Warna, opasitas, penulis, dan subjek dari anotasi teks markup dapat dimodifikasi.

Dimungkinkan untuk mendapatkan atau mengatur pengaturan anotasi sorotan menggunakan properti highlightSettings.
 The `highlightSettings` properti digunakan untuk mengatur warna, opasitas, penulis, subjek, tanggal dimodifikasi, dan properti `isLocked` dari anotasi sorotan.

Juga dimungkinkan untuk mendapatkan atau mengatur pengaturan dari anotasi coret menggunakan properti `strikethroughSettings`. Properti `strikethroughSettings` digunakan untuk mengatur warna, opasitas, penulis, subjek, tanggal dimodifikasi, dan properti `isLocked` dari anotasi coret.

Fitur berikutnya adalah kemampuan untuk mendapatkan atau mengatur pengaturan dari anotasi garis bawah menggunakan properti `underlineSettings`. Properti `underlineSettings` digunakan untuk mengatur warna, opasitas, penulis, subjek, tanggal dimodifikasi, dan properti `isLocked` dari anotasi garis bawah.

## Tambahkan Anotasi Penandaan Teks

Untuk menambahkan Anotasi Penandaan Teks ke dokumen PDF, kita perlu melakukan tindakan berikut:

1. Muat file PDF - objek [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) baru.
1. Buat anotasi:

    - [HighlightAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/class-use/HighlightAnnotation) dan atur parameter (judul, warna).- [StrikeOutAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf.class-use/StrikeOutAnnotation) dan atur parameter (judul, warna).
- [SquigglyAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf.class-use/SquigglyAnnotation) dan atur parameter (judul, warna).
- [UnderlineAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/UnderlineAnnotation) dan atur parameter (judul, warna).

1. Setelah itu kita harus menambahkan semua anotasi ke halaman.

```java
package com.aspose.pdf.examples;

import java.util.*;
import com.aspose.pdf.*;

public class ExampleTextMarkupAnnotation {
    // Jalur ke direktori dokumen.
    private static String _dataDir = "/home/admin1/pdf-examples/Samples/";

    public static void AddTextMarkupAnnotation() {
        try {
            // Memuat file PDF
            Document document = new Document(_dataDir + "sample.pdf");
            Page page = document.getPages().get_Item(1);
            TextFragmentAbsorber tfa = new TextFragmentAbsorber("PDF");
            tfa.visit(page);

            // Membuat anotasi
            HighlightAnnotation highlightAnnotation = new HighlightAnnotation(page,
                    tfa.getTextFragments().get_Item(1).getRectangle());
            highlightAnnotation.setTitle("Pengguna Aspose");
            highlightAnnotation.setColor(Color.getLightGreen());

            StrikeOutAnnotation strikeOutAnnotation = new StrikeOutAnnotation(page,
                    tfa.getTextFragments().get_Item(2).getRectangle());
            strikeOutAnnotation.setTitle("Pengguna Aspose");
            strikeOutAnnotation.setColor(Color.getBlue());

            SquigglyAnnotation squigglyAnnotation = new SquigglyAnnotation(page,
                    tfa.getTextFragments().get_Item(3).getRectangle());
            squigglyAnnotation.setTitle("Pengguna Aspose");
            squigglyAnnotation.setColor(Color.getRed());

            UnderlineAnnotation underlineAnnotation = new UnderlineAnnotation(page,
                    tfa.getTextFragments().get_Item(4).getRectangle());
            underlineAnnotation.setTitle("Pengguna Aspose");
            underlineAnnotation.setColor(Color.getViolet());

            // Menambahkan anotasi ke halaman
            page.getAnnotations().add(highlightAnnotation);
            page.getAnnotations().add(squigglyAnnotation);
            page.getAnnotations().add(strikeOutAnnotation);
            page.getAnnotations().add(underlineAnnotation);
            document.save(_dataDir + "sample_mod.pdf");
        } catch (Exception ex) {
            System.out.println(ex.getMessage());
        }
    }
}
```


Jika Anda ingin menyoroti fragmen multi-baris, Anda harus menggunakan contoh lanjutan:

```java
    /// <summary>
    /// Contoh lanjutan untuk Anda yang ingin menyoroti fragmen multi-baris
    /// </summary>
    public static void AddHighlightAnnotationAdvanced() {
        Document document = new Document(_dataDir + "sample_mod.pdf");
        Page page = document.getPages().get_Item(1);
        TextFragmentAbsorber tfa = new TextFragmentAbsorber("Adobe\\W+Acrobat\\W+Reader", new TextSearchOptions(true));
        tfa.visit(page);
        for (TextFragment textFragment : tfa.getTextFragments()) {
            HighlightAnnotation highlightAnnotation = HighLightTextFragment(page, textFragment, Color.getYellow());
            page.getAnnotations().add(highlightAnnotation);
        }
        document.save(_dataDir + "sample_mod.pdf");
    }

    private static HighlightAnnotation HighLightTextFragment(Page page, TextFragment textFragment, Color color) {
        HighlightAnnotation ha;
        if (textFragment.getSegments().size() == 1) {
            ha = new HighlightAnnotation(page, textFragment.getSegments().get_Item(1).getRectangle());
            ha.setTitle("Pengguna Aspose");
            ha.setColor(color);
            ha.setModified(new Date());
            Rectangle rect = textFragment.getSegments().get_Item(1).getRectangle();
            ha.setQuadPoints(
                    new Point[] { new Point(rect.getLLX(), rect.getURY()), new Point(rect.getURX(), rect.getURY()),
                            new Point(rect.getLLX(), rect.getLLY()), new Point(rect.getURX(), rect.getLLY()) });
            return ha;
        }

        int offset = 0;
        Point[] quadPoints = new Point[textFragment.getSegments().size() * 4];
        for (TextSegment segment : textFragment.getSegments()) {
            Rectangle r = segment.getRectangle();
            quadPoints[offset + 0] = new Point(r.getLLX(), r.getURY());
            quadPoints[offset + 1] = new Point(r.getURX(), r.getURY());
            quadPoints[offset + 2] = new Point(r.getLLX(), r.getLLY());
            quadPoints[offset + 3] = new Point(r.getURX(), r.getLLY());
            offset += 4;
        }

        double llx = quadPoints[0].getX();
        double lly = quadPoints[0].getY();
        double urx = quadPoints[0].getX();
        double ury = quadPoints[0].getY();
        for (Point pt : quadPoints) {
            if (llx > pt.getX())
                llx = pt.getX();
            if (lly > pt.getY())
                lly = pt.getY();
            if (urx < pt.getX())
                urx = pt.getX();
            if (ury < pt.getY())
                ury = pt.getY();
        }
        ha = new HighlightAnnotation(page, new Rectangle(llx, lly, urx, ury));
        ha.setTitle("Pengguna Aspose");
        ha.setColor(color);
        ha.setModified(new Date());
        ha.setQuadPoints(quadPoints);
        return ha;
    }

    /// <summary>
    /// Cara mendapatkan Teks yang Disorot
    /// </summary>
    public static void GetHighlightedText() {
        // Memuat file PDF
        Document document = new Document(_dataDir + "sample_mod.pdf");
        Page page = document.getPages().get_Item(1);

        AnnotationSelector annotationSelector1 = new AnnotationSelector(
                new HighlightAnnotation(page, Rectangle.getTrivial()));
        page.accept(annotationSelector1);
        List<Annotation> highlightAnnotations = annotationSelector1.getSelected();
        for (Annotation ta : highlightAnnotations) {
            System.out.println("[" + ((HighlightAnnotation) ta).getMarkedText() + "]");
        }
    }
```


## Dapatkan Anotasi Markup Teks

Silakan coba gunakan cuplikan kode berikut untuk mendapatkan Anotasi Markup Teks dari dokumen PDF.

```java
     public static void GetTextMarkupAnnotation() {
        // Muat file PDF
        Document document = new Document(_dataDir + "sample_mod.pdf");
        Page page = document.getPages().get_Item(1);

        AnnotationSelector annotationSelector1 = new AnnotationSelector(
                new HighlightAnnotation(page, Rectangle.getTrivial()));
        page.accept(annotationSelector1);
        AnnotationSelector annotationSelector2 = new AnnotationSelector(
                new SquigglyAnnotation(page, Rectangle.getTrivial()));
        page.accept(annotationSelector2);

        List<Annotation> textMarkupAnnotations = annotationSelector1.getSelected();
        textMarkupAnnotations.addAll(annotationSelector2.getSelected());

        // cetak hasil
        for (Annotation ta : textMarkupAnnotations) {
            System.out.printf("[" + ta.getAnnotationType() + ta.getRect() + "]");
        }
    }
```


## Hapus Anotasi Markup Teks

Cuplikan kode berikut menunjukkan cara Menghapus Anotasi Markup Teks dari file PDF.

```java
   public static void DeleteTextMarkupAnnotation() {
        // Muat file PDF
        Document document = new Document(_dataDir + "sample_mod.pdf");
        Page page = document.getPages().get_Item(1);

        AnnotationSelector annotationSelector1 = new AnnotationSelector(
                new HighlightAnnotation(page, Rectangle.getTrivial()));
        page.accept(annotationSelector1);
        AnnotationSelector annotationSelector2 = new AnnotationSelector(
                new SquigglyAnnotation(page, Rectangle.getTrivial()));
        page.accept(annotationSelector2);

        List<Annotation> textMarkupAnnotations = annotationSelector1.getSelected();
        textMarkupAnnotations.addAll(annotationSelector2.getSelected());

        // cetak hasil
        for (Annotation ta : textMarkupAnnotations) {
            page.getAnnotations().delete(ta);
        }
        document.save(_dataDir + "sample_del.pdf");
    }
```