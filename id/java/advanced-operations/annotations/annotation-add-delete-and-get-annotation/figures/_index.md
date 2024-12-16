---
title: Anotasi Gambar PDF
linktitle: Anotasi Gambar
type: docs
weight: 30
url: /id/java/figures-annotation/
description: Artikel ini menjelaskan cara menambahkan, mendapatkan, dan menghapus anotasi gambar dari dokumen PDF Anda dengan Aspose.PDF untuk Java
lastmod: "2021-11-24"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Tambahkan Anotasi Persegi atau Lingkaran

Anotasi Persegi dan Lingkaran masing-masing akan menampilkan persegi panjang atau elips pada halaman. Ketika dibuka, mereka akan menampilkan jendela pop-up yang berisi teks dari catatan yang terkait.
Anotasi Persegi mirip dengan anotasi Lingkaran (instance dari kelas Aspose.Pdf.Annotations.CircleAnnotation) selain dari bentuknya.

Langkah-langkah untuk membuat Anotasi Persegi dan Lingkaran:

1. Muat file PDF - baru [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document).

1. Buat [Circle Annotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/circleannotation) baru dan atur parameter Circle (Rectangle baru, judul, warna, InteriorColor, Opacity).
1. Buat [PopupAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/class-use/PopupAnnotation) baru.
1. Selanjutnya kita perlu membuat [Square Annotation](https://reference.aspose.com/pdf/java/com.aspose.pdf.class-use/SquareAnnotation).
1. Atur parameter Square yang sama (Rectangle baru, judul, warna, InteriorColor, Opacity).
1. Setelah itu kita perlu menambahkan Anotasi Square dan Circle ke halaman.

Cuplikan kode berikut menunjukkan cara menambahkan Circle Annotations pada halaman PDF.

```java
package com.aspose.pdf.examples;

import java.util.*;
import com.aspose.pdf.*;

public class ExampleCircleAnnotation {

    // Jalur ke direktori dokumen.
    private static String _dataDir = "/home/admin1/pdf-examples/Samples/";

    public static void AddCircleAnnotation() {
        try {
            // Memuat file PDF
            Document document = new com.aspose.pdf.Document(_dataDir + "appartments.pdf");
            Page page = document.getPages().get_Item(1);

            // Membuat Polygon Annotation
            CircleAnnotation circleAnnotation = new CircleAnnotation(page, new Rectangle(270, 160, 483, 383));
            circleAnnotation.setTitle("John Smith");
            circleAnnotation.setColor(Color.getRed());
            circleAnnotation.setInteriorColor(Color.getMistyRose());
            circleAnnotation.setOpacity(0.5);
            circleAnnotation.setPopup(new PopupAnnotation(page, new Rectangle(842, 316, 1021, 459)));

            // Membuat Square Annotation
            SquareAnnotation squareAnnotation = new SquareAnnotation(page, new Rectangle(67, 317, 261, 459));
            squareAnnotation.setTitle("John Smith");
            squareAnnotation.setColor(Color.getBlue());
            squareAnnotation.setInteriorColor(Color.getBlueViolet());
            squareAnnotation.setOpacity(0.25);
            squareAnnotation.setPopup(new PopupAnnotation(page, new Rectangle(842, 196, 1021, 338)));

            // Menambahkan anotasi ke halaman
            page.getAnnotations().add(circleAnnotation);
            page.getAnnotations().add(squareAnnotation);
            document.save(_dataDir + "appartments_mod.pdf");
        } catch (Exception ex) {
            System.out.println(ex.getMessage());
        }
    }
```


Sebagai contoh, kita akan melihat hasil penambahan anotasi Persegi dan Lingkaran ke dokumen PDF berikut ini:

![Demo Anotasi Lingkaran dan Persegi](circle_demo.png)

## Dapatkan Anotasi Lingkaran

Silakan coba menggunakan cuplikan kode berikut untuk Mendapatkan Anotasi Lingkaran dari dokumen PDF.

```java
public static void GetCircleAnnotation() {
        // Memuat file PDF
        Document document = new Document(_dataDir + "appartments_mod.pdf");

        // Memfilter anotasi menggunakan AnnotationSelector
        Page page = document.getPages().get_Item(1);
        AnnotationSelector annotationSelector = new AnnotationSelector(
                new CircleAnnotation(page, Rectangle.getTrivial()));
        page.accept(annotationSelector);
        List<Annotation> caretAnnotations = annotationSelector.getSelected();

        // mencetak hasil
        for (Annotation ca : caretAnnotations) {
            System.out.println(ca.getRect());
        }
    }
```

## Hapus Anotasi Lingkaran

Cuplikan kode berikut menunjukkan cara Menghapus Anotasi Lingkaran dari file PDF.

```java
public static void DeleteCircleAnnotation() {
        // Memuat file PDF
        Document document = new Document(_dataDir + "appartments_mod.pdf");

        // Menyaring anotasi menggunakan AnnotationSelector
        Page page = document.getPages().get_Item(1);
        AnnotationSelector annotationSelector = new AnnotationSelector(
                new CircleAnnotation(page, Rectangle.getTrivial()));
        page.accept(annotationSelector);
        List<Annotation> circleAnnotations = annotationSelector.getSelected();

        for (Annotation ca : circleAnnotations) {
            page.getAnnotations().delete(ca);
        }
        document.save(_dataDir + "appartments_del.pdf");
    }
```

## Tambahkan Anotasi Poligon dan Polyline

Alat Polyline memungkinkan Anda membuat bentuk dan garis luar dengan jumlah sisi yang sembarang pada dokumen.

**Anotasi Poligon** merepresentasikan poligon pada halaman. Mereka dapat memiliki sejumlah titik yang dihubungkan oleh garis lurus.

**Anotasi Polyline** juga mirip dengan poligon, perbedaan satu-satunya adalah titik pertama dan terakhir tidak secara implisit terhubung.

Langkah-langkah untuk membuat anotasi Polygon dan Polyline:

1. Memuat file PDF - baru [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document).
1. Membuat [Polygon Annotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/PolygonAnnotation) baru dan mengatur parameter Polygon (Rectangle baru, Points baru, judul, warna, InteriorColor, dan Opacity).
1. Membuat [PopupAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf.class-use/PopupAnnotation) baru.
1. Selanjutnya, Membuat [PolyLine Annotation](https://reference.aspose.com/pdf/java/com.aspose.pdf.class-use/PolylineAnnotation) dan ulangi semua aksi.
1. Setelah itu kita bisa menambahkan anotasi ke halaman.

Cuplikan kode berikut menunjukkan cara menambahkan Anotasi Polygon dan Polyline ke file PDF:

```java
 package com.aspose.pdf.examples;

import java.util.*;
import com.aspose.pdf.*;

public class ExamplePolygonAnnotation {
    private static String _dataDir = "/home/admin1/pdf-examples/Samples/";

    public static void AddPolynnotation() {
        try {
            // Memuat file PDF
            Document document = new Document(_dataDir + "appartments.pdf");
            Page page = document.getPages().get_Item(1);

            // Membuat Anotasi Polygon
            PolygonAnnotation polygonAnnotation = new PolygonAnnotation(page, new Rectangle(270, 193, 571, 383),
                    new Point[] { new Point(274, 381), new Point(555, 381), new Point(555, 304), new Point(570, 304),
                            new Point(570, 195), new Point(274, 195) });

            polygonAnnotation.setTitle("John Smith");
            polygonAnnotation.setColor(Color.getBlue());
            polygonAnnotation.setInteriorColor(Color.getBlueViolet());
            polygonAnnotation.setOpacity(0.25);
            polygonAnnotation.setPopup(new PopupAnnotation(page, new Rectangle(842, 196, 1021, 338)));

            // Membuat Anotasi PoliLine
            PolylineAnnotation polylineAnnotation = new PolylineAnnotation(page, new Rectangle(270, 193, 571, 383),
                    new Point[] { new Point(545, 150), new Point(545, 190), new Point(667, 190), new Point(667, 110),
                            new Point(626, 111) });

            polygonAnnotation.setTitle("John Smith");
            polygonAnnotation.setColor(Color.getRed());
            polygonAnnotation.setPopup(new PopupAnnotation(page, new Rectangle(842, 196, 1021, 338)));

            // Menambahkan anotasi ke halaman
            page.getAnnotations().add(polygonAnnotation);
            page.getAnnotations().add(polylineAnnotation);
            document.save(_dataDir + "appartments_mod.pdf");
        } catch (Exception ex) {
            System.out.println(ex.getMessage());
        }
    }
```


## Dapatkan Anotasi Poligon dan Polilin

Silakan coba gunakan cuplikan kode berikut untuk Mendapatkan Anotasi Poligon dan Polilin dalam dokumen PDF.

```java
    public static void GetPolyAnnotation() {
        // Memuat file PDF
        Document document = new Document(_dataDir + "Appartments_mod.pdf");
        Page page = document.getPages().get_Item(1);

        AnnotationSelector annotationSelector = new AnnotationSelector(
                new PolylineAnnotation(page, Rectangle.getTrivial(), null));
        page.accept(annotationSelector);
        List<Annotation> polyAnnotations = annotationSelector.getSelected();

        for (Annotation pa : polyAnnotations) {
            System.out.printf("[%s]", pa.getRect());
        }
    }
```

## Hapus Anotasi Poligon dan Polilin

Cuplikan kode berikut menunjukkan cara Menghapus Anotasi Poligon dan Polilin dari file PDF.

```java
        public static void DeletePolyAnnotation() {
        // Memuat file PDF
        Document document = new Document(_dataDir + "Appartments_mod.pdf");
        Page page = document.getPages().get_Item(1);

        AnnotationSelector annotationSelector = new AnnotationSelector(
                new PolylineAnnotation(page, Rectangle.getTrivial(), null));
        page.accept(annotationSelector);
        List<Annotation> polyAnnotations = annotationSelector.getSelected();

        for (Annotation pa : polyAnnotations) {
            page.getAnnotations().delete(pa);
        }

        document.save(_dataDir + "Appartments_del.pdf");
    }
```


## Cara menambahkan Anotasi Garis ke dalam file PDF yang sudah ada

Tujuan dari Anotasi Garis adalah untuk menampilkan satu garis lurus pada halaman. Ketika dibuka, akan menampilkan jendela pop-up yang berisi teks dari catatan terkait. Fitur ini memiliki entri tambahan khusus untuk anotasi garis. Entri ini dienkripsi dalam bentuk huruf, misalnya, LL, BS, IC, dan sebagainya.

Selain itu, Anotasi Garis dapat menyertakan keterangan pada anotasi garis, yang ditentukan dengan mengatur Cap ke `true`.

Fitur berikutnya memungkinkan efek penerapan keterangan pada Anotasi Garis yang memiliki offset pemimpin. Selain itu, jenis anotasi ini memungkinkan Anda untuk mendefinisikan gaya akhir Garis.

Langkah-langkah dengan mana kita membuat anotasi Garis:

1. Muat file PDF - [Dokumen](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) baru.
2. Buat [Anotasi Garis](https://reference.aspose.com/pdf/java/com.aspose.pdf/lineannotation) baru dan atur parameter Garis (Rectangle baru, Titik baru, judul, warna, lebar, GayaMulai dan GayaAkhir).

1. Buat [PopupAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/class-use/PopupAnnotation) baru.
1. Setelah itu kita bisa Menambahkan anotasi ke halaman

Cuplikan kode berikut menunjukkan cara menambahkan Anotasi Garis ke file PDF:

```java
package com.aspose.pdf.examples;

import java.util.*;
import com.aspose.pdf.*;

public class ExampleLineAnnotation {

    // Jalur ke direktori dokumen.
    private static String _dataDir = "/home/admin1/pdf-examples/Samples/";

    public static void AddLineAnnotation() {
        try {
            // Memuat file PDF
            Document document = new Document(_dataDir + "appartments.pdf");
            Page page = document.getPages().get_Item(1);

            // Buat Anotasi Garis
            LineAnnotation lineAnnotation = new LineAnnotation(page, new Rectangle(550, 93, 562, 439),
                    new Point(556, 99), new Point(556, 443));

            lineAnnotation.setTitle("John Smith");
            lineAnnotation.setColor(Color.getRed());
            lineAnnotation.setWidth(3);
            lineAnnotation.setStartingStyle(LineEnding.OpenArrow);
            lineAnnotation.setEndingStyle(LineEnding.OpenArrow);
            lineAnnotation.setPopup(new PopupAnnotation(page, new Rectangle(842, 124, 1021, 266)));

            // Tambahkan anotasi ke halaman
            page.getAnnotations().add(lineAnnotation);
            document.save(_dataDir + "appartments_mod.pdf");
        } catch (Exception ex) {
            System.out.println(ex.getMessage());
        }
    }
```


## Dapatkan Anotasi Garis

Silakan coba menggunakan potongan kode berikut untuk Mendapatkan Anotasi Garis dalam dokumen PDF.

```java
    public static void GetLineAnnotation() {
        // Memuat file PDF
        Document document = new Document(_dataDir + "appartments_mod.pdf");

        // Memfilter anotasi menggunakan AnnotationSelector
        Page page = document.getPages().get_Item(1);
        AnnotationSelector annotationSelector = new AnnotationSelector(
                new LineAnnotation(page, Rectangle.getTrivial(), Point.getTrivial(), Point.getTrivial()));
        page.accept(annotationSelector);
        List<Annotation> lineAnnotations = annotationSelector.getSelected();

        // cetak hasil
        for (Annotation la : lineAnnotations) {
            LineAnnotation l = (LineAnnotation) la;
            System.out.println("[" + l.getStarting().getX() + "," + l.getStarting().getY() + "]" + "["
                    + l.getEnding().getX() + "," + l.getEnding().getY() + "]");
        }
    }
```

## Hapus Anotasi Garis

Cuplikan kode berikut menunjukkan cara Menghapus Anotasi Garis dari file PDF.

```java
   public static void DeleteLineAnnotation() {
        // Memuat file PDF
        Document document = new Document(_dataDir + "appartments_mod.pdf");

        // Memfilter anotasi menggunakan AnnotationSelector
        Page page = document.getPages().get_Item(1);
        AnnotationSelector annotationSelector = new AnnotationSelector(
                new LineAnnotation(page, Rectangle.getTrivial(), Point.getTrivial(), Point.getTrivial()));
        page.accept(annotationSelector);
        List<Annotation> lineAnnotations = annotationSelector.getSelected();

        // mencetak hasil
        for (Annotation la : lineAnnotations) {
            page.getAnnotations().delete(la);
        }
        document.save(_dataDir + "appartments_del.pdf");
    }
}
```

## Cara menambahkan Anotasi Tinta ke file PDF

Sebuah Anotasi Tinta mewakili "coretan" bebas yang terdiri dari satu atau lebih jalur yang terputus.
 Ketika dibuka, ia akan menampilkan jendela pop-up yang berisi teks dari catatan yang terkait.

[InkAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/class-use/InkAnnotation) mewakili coretan tangan bebas yang terdiri dari satu atau lebih titik yang terputus. Silakan coba menggunakan cuplikan kode berikut untuk menambahkan InkAnnotation dalam dokumen PDF.

```java
package com.aspose.pdf.examples;

import java.util.*;
import com.aspose.pdf.*;

public class ExampleInkAnnotation {

    // Jalur ke direktori dokumen.
    private static String _dataDir = "/home/admin1/pdf-examples/Samples/";


    public static void AddInkAnnotation() {
        try {
            // Muat file PDF
            Document document = new com.aspose.pdf.Document(_dataDir + "Appartments.pdf");
            Page page = document.getPages().get_Item(1);
            Rectangle arect = new Rectangle(320.086,189.286,384.75,228.927);
            List<Point[]> inkList = new ArrayList<Point[]>();
            //data dalam ppts, diterima dari mouse atau perangkat penunjuk lainnya
            double ppts[] = { 328.002, 222.017, 328.648, 222.017, 329.294, 222.017, 329.617, 222.34, 330.91, 222.663,
                    331.556, 222.663, 332.203, 222.986, 333.495, 223.633, 334.141, 223.956, 334.788, 224.279, 335.434,
                    224.602, 336.08, 224.602, 336.727, 224.925, 337.373, 225.248, 337.696, 225.248, 338.342, 225.572,
                    338.989, 225.895, 341.897, 225.895, 343.513, 226.218, 346.098, 226.218, 348.683, 226.541, 350.622,
                    226.541, 352.238, 226.541, 353.208, 226.541, 353.854, 226.541, 355.146, 226.541, 356.439, 226.541,
                    357.732, 226.541, 358.378, 226.541, 359.024, 226.541, 360.64, 226.541, 361.286, 226.541, 361.933,
                    226.541, 362.256, 226.541, 362.902, 226.541, 363.548, 226.541, 363.872, 226.541, 363.872, 226.218,
                    365.164, 226.218, 365.487, 226.218, 365.811, 226.218, 367.103, 226.218, 367.749, 226.218, 368.719,
                    226.218, 370.012, 226.218, 370.981, 226.218, 371.627, 226.218, 372.597, 225.895, 372.92, 225.895,
                    373.243, 225.895, 373.243, 225.572, 373.566, 225.572, 374.213, 225.248, 374.536, 225.248, 375.182,
                    224.602, 375.182, 224.279, 375.828, 223.956, 376.475, 223.31, 377.121, 222.986, 377.767, 222.986,
                    378.414, 222.017, 379.383, 221.371, 379.706, 220.724, 380.029, 219.432, 380.676, 219.109, 380.676,
                    218.462, 381.645, 217.493, 381.968, 217.17, 381.968, 216.523, 382.291, 215.554, 382.615, 215.231,
                    382.615, 214.261, 382.938, 213.292, 382.938, 212.645, 382.938, 211.999, 382.938, 211.353, 382.938,
                    210.707, 382.938, 209.737, 382.938, 208.768, 382.938, 208.444, 382.615, 207.475, 382.615, 206.829,
                    382.291, 206.505, 382.291, 205.859, 381.968, 204.89, 381.968, 204.243, 381.645, 203.92, 380.999,
                    203.274, 380.999, 202.951, 380.676, 202.305, 380.353, 201.658, 380.029, 201.335, 380.029, 200.689,
                    380.029, 200.366, 379.383, 199.719, 379.06, 199.719, 378.737, 199.073, 377.767, 198.103, 377.121,
                    197.780, 376.475, 197.457, 375.505, 196.488, 374.859, 196.165, 374.536, 195.841, 372.92, 195.195,
                    371.951, 194.549, 370.658, 194.226, 368.719, 193.902, 367.426, 193.256, 366.457, 193.256, 363.872,
                    192.933, 362.902, 192.933, 361.61, 192.61, 359.024, 192.61, 357.409, 192.61, 356.439, 192.61,
                    353.531, 192.61, 352.561, 192.61, 350.945, 192.61, 349.007, 192.933, 348.36, 193.256, 347.391,
                    193.256, 346.098, 193.902, 345.452, 193.902, 344.806, 193.902, 343.513, 193.902, 342.867, 193.902,
                    342.220, 193.902, 341.574, 193.902, 341.251, 194.226, 340.928, 194.226, 340.928, 194.549, 340.605,
                    194.549, 340.605, 194.872, 339.635, 195.195, 339.635, 195.518, 338.989, 195.518, 338.989, 195.841,
                    338.666, 196.165, 338.019, 196.811, 338.019, 197.134, 337.373, 197.457, 336.404, 198.427, 335.757,
                    198.427, 335.434, 198.75, 334.141, 199.719, 333.818, 199.719, 333.818, 200.042, 332.849, 200.366,
                    332.203, 200.366, 331.556, 201.335, 330.91, 201.981, 330.587, 202.305, 330.264, 202.305, 329.294,
                    202.628, 328.971, 202.951, 328.002, 203.274, 328.002, 203.597, 327.355, 204.243, 326.709, 204.567,
                    326.386, 204.89, 326.063, 205.536, 325.416, 205.859, 325.093, 205.859, 324.447, 205.859, 324.124,
                    206.182, 324.124, 206.505, 323.477, 206.829, 323.477, 207.152, 323.477, 207.798, 322.831, 207.798,
                    322.831, 208.121, 322.831, 208.444, 322.508, 208.444, 322.508, 209.091, 322.185, 209.414, 322.185,
                    209.737, 322.185, 210.383, 322.185, 211.03, 322.185, 211.353, 322.185, 211.676, 322.185, 212.322,
                    323.154, 213.292, 323.154, 213.938, 324.447, 214.584, 325.093, 215.877, 325.416, 216.2, 325.416,
                    216.846, 325.739, 217.17, 326.063, 217.493, 326.386, 218.139, 326.709, 218.139, 326.709, 218.462,
                    327.032, 219.109, 327.032, 219.432, 327.032, 219.755, 327.355, 220.078, 327.355, 220.401, 327.678,
                    221.371, 328.002, 221.371, 328.002, 222.017, 328.325, 222.663, 328.648, 222.663, 328.971, 222.986,
                    329.294, 223.31, 329.617, 223.956, 329.617, 224.279 };

            //konversi data ke titik
            Point[] arrpt = new Point[ppts.length/2];
            for (int i = 0, j=0; i < arrpt.length; i++, j+=2) {
                arrpt[i] = new Point(ppts[j],ppts[j+1]);
            }
            inkList.add(arrpt);

            InkAnnotation ia = new InkAnnotation(page, arect, inkList);
            ia.setTitle("Pengguna Aspose");
            ia.setColor(Color.getRed());
            ia.setCapStyle(CapStyle.Rounded);

            Border border = new Border(ia);
            border.setWidth(3);
            ia.setOpacity(0.75);

            page.getAnnotations().add(ia);
            document.save(_dataDir + "appartments_mod.pdf");
        } catch (Exception ex) {
            System.out.println(ex.getMessage());
        }
    }
```

## Dapatkan InkAnnotation dari PDF Anda

Anda dapat mendapatkan [InkAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/class-use/InkAnnotation) dengan potongan kode berikut:

```java
public static void GetInkAnnotation() {
        // Muat file PDF
        Document document = new Document(_dataDir + "appartments_mod.pdf");

        // Saring anotasi menggunakan AnnotationSelector
        Page page = document.getPages().get_Item(1);
        AnnotationSelector annotationSelector = new AnnotationSelector(
                new InkAnnotation(page, Rectangle.getTrivial(), null));
        page.accept(annotationSelector);
        List<Annotation> inkAnnotations = annotationSelector.getSelected();

        // cetak hasil
        for (Annotation ia : inkAnnotations) {
            System.out.println(ia.getRect());
        }
    }
```

## Hapus InkAnnotation

Aspose.PDF untuk Java memungkinkan Anda untuk menghapus [InkAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/class-use/InkAnnotation) dari file PDF Anda.

```java
public static void DeleteInkAnnotation() {
        // Muat file PDF
        Document document = new Document(_dataDir + "appartments_mod.pdf");

        // Saring anotasi menggunakan AnnotationSelector
        Page page = document.getPages().get_Item(1);
        AnnotationSelector annotationSelector = new AnnotationSelector(
                new InkAnnotation(page, Rectangle.getTrivial(), null));
        page.accept(annotationSelector);
        List<Annotation> InkAnnotations = annotationSelector.getSelected();

        for (Annotation ca : InkAnnotations) {
            page.getAnnotations().delete(ca);
        }
        document.save(_dataDir + "appartments_del.pdf");
    }
```