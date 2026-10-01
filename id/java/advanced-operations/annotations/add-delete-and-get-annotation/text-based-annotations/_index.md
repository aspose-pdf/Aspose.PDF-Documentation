---
title: "Anotasi berbasis teks menggunakan Java"
linktitle: "Anotasi teks"
type: docs
weight: 10
url: /id/java/text-based-annotations/
description: Pelajari cara membuat, memeriksa, dan menghapus anotasi PDF berbasis teks menggunakan Aspose.PDF for Java, termasuk markup teks bebas, penyorotan, coret, garis bergelombang, dan garis bawah.
lastmod: "2026-09-30"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: "Bekerja dengan anotasi PDF teks di Java"
Abstract: Artikel ini menunjukkan cara bekerja dengan lima jenis anotasi berbasis teks di Aspose.PDF for Java, termasuk anotasi teks bebas, sorot, coret, bergelombang, dan garis bawah. Pelajari cara menambahkan, mengambil, dan menghapus anotasi, serta teknik lanjutan seperti menandai teks dan meratakan markup interaktif.
---
Anotasi berbasis teks memungkinkan peninjau dan pengembang menambahkan catatan interaktif, penyorotan, dan markup ke dokumen PDF tanpa mengubah konten inti. Bagian ini mencakup lima tipe anotasi praktis yang digunakan dalam alur kerja tinjauan dokumen, skenario kepatuhan, dan siklus umpan balik kolaboratif.

## Referensi cepat: jenis anotasi

Artikel ini mencakup jenis anotasi berbasis teks berikut:

- **Free Text**: Kotak teks yang dapat diedit untuk menambahkan catatan dan komentar
- **Sorotan**: Penekanan visual pada bagian teks penting
- **Strikeout**: Tandai teks untuk penghapusan atau revisi selama tinjauan
- **Squiggly**: Garis bawah bergelombang untuk menunjukkan kesalahan atau kekhawatiran
- **Underline**: Penekanan underline tradisional dengan presisi empat titik opsional

## Menambahkan, mendapatkan, dan menghapus anotasi teks bebas

Anotasi teks bebas berfungsi sebagai kotak teks mengambang yang dapat diedit tanpa memengaruhi struktur dokumen. Gunakan contoh-contoh ini untuk menambahkan kotak komentar, memeriksa propertinya, atau menghapusnya.

### Menambahkan anotasi teks bebas

1. Buka PDF sumber [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Buat sebuah [`FreeTextAnnotation`](https://reference.aspose.com/pdf/java/com.aspose.pdf/freetextannotation/) dengan persegi panjang dan pengaturan tampilan.
1. Tambahkan anotasi ke halaman dan simpan dokumen.

```java
public static void freeTextAnnotationAdd(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        FreeTextAnnotation freeTextAnnotation = new FreeTextAnnotation(
                document.getPages().get_Item(1),
                new Rectangle(299, 713, 308, 720, true),
                new DefaultAppearance());
        freeTextAnnotation.setTitle("Aspose User");
        freeTextAnnotation.setColor(Color.getLightGreen());

        document.getPages().get_Item(1).getAnnotations().add(freeTextAnnotation);
        document.save(outputFile.toString());
    }
}
```

### Mendapatkan anotasi teks bebas

1. Buka PDF sumber [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Iterasikan melalui anotasi pada halaman dan saring berdasarkan [`AnnotationType.FreeText`](https://reference.aspose.com/pdf/java/com.aspose.pdf/annotationtype/).
1. Ambil properti anotasi atau batas.

```java
public static void freeTextAnnotationGet(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        for (Annotation annotation : document.getPages().get_Item(1).getAnnotations()) {
            if (annotation.getAnnotationType() == AnnotationType.FreeText) {
                System.out.println(annotation.getRect());
            }
        }
    }
}
```

### Menghapus anotasi teks bebas

1. Buka PDF sumber [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Temukan anotasi teks bebas dengan mengiterasi anotasi halaman dan menyaring berdasarkan tipe.
1. Tambahkan anotasi yang cocok ke daftar hapus dan hapus anotasi tersebut dari halaman.
1. Simpan dokumen yang diperbarui.

```java
public static void freeTextAnnotationDelete(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        List<Annotation> toDelete = new ArrayList<>();
        for (Annotation annotation : document.getPages().get_Item(1).getAnnotations()) {
            if (annotation.getAnnotationType() == AnnotationType.FreeText) {
                toDelete.add(annotation);
            }
        }
        for (Annotation annotation : toDelete) {
            document.getPages().get_Item(1).getAnnotations().delete(annotation);
        }
        document.save(outputFile.toString());
    }
}
```

## Menambahkan, mendapatkan, dan menghapus anotasi sorotan

Anotasi highlight menandai bagian penting dengan lapisan semi-transparan. Gunakan contoh-contoh ini untuk membuat highlight untuk peninjauan dokumen, menemukan highlight yang ada, dan membersihkan markup.

### Menambahkan anotasi sorotan

1. Buka PDF sumber [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Buat sebuah [`HighlightAnnotation`](https://reference.aspose.com/pdf/java/com.aspose.pdf/highlightannotation/) dengan sebuah persegi panjang yang menentukan area sorotan.
1. Tambahkan anotasi ke halaman dan simpan dokumen.

```java
public static void textHighlightAnnotationAdd(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        HighlightAnnotation highlightAnnotation = new HighlightAnnotation(
                document.getPages().get_Item(1),
                new Rectangle(300, 750, 320, 770, true));

        document.getPages().get_Item(1).getAnnotations().add(highlightAnnotation);
        document.save(outputFile.toString());
    }
}
```

### Mendapatkan anotasi sorotan

1. Buka PDF sumber [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Iterasikan melalui anotasi dan saring berdasarkan [`AnnotationType.Highlight`](https://reference.aspose.com/pdf/java/com.aspose.pdf/annotationtype/).
1. Baca properti anotasi seperti batas atau warna.

```java
public static void textHighlightAnnotationGet(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        for (Annotation annotation : document.getPages().get_Item(1).getAnnotations()) {
            if (annotation.getAnnotationType() == AnnotationType.Highlight) {
                System.out.println(annotation.getRect());
            }
        }
    }
}
```

### Menghapus anotasi sorotan

1. Buka PDF sumber [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Kumpulkan anotasi sorotan dengan memfilter anotasi berdasarkan tipe.
1. Hapus setiap anotasi dari halaman.
1. Simpan dokumen yang diperbarui.

```java
public static void textHighlightAnnotationDelete(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        List<Annotation> toDelete = new ArrayList<>();
        for (Annotation annotation : document.getPages().get_Item(1).getAnnotations()) {
            if (annotation.getAnnotationType() == AnnotationType.Highlight) {
                toDelete.add(annotation);
            }
        }
        for (Annotation annotation : toDelete) {
            document.getPages().get_Item(1).getAnnotations().delete(annotation);
        }
        document.save(outputFile.toString());
    }
}
```

## Menambahkan, mendapatkan, dan menghapus anotasi coret

Anotasi coret menghapus teks untuk menunjukkan penghapusan, penolakan, atau revisi. Gunakan contoh-contoh ini untuk menerapkan markup coret selama peninjauan dokumen, menemukan teks yang ditandai, dan menghapus anotasi coret.

### Menambahkan anotasi coret

1. Buka PDF sumber [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Buat sebuah [`StrikeOutAnnotation`](https://reference.aspose.com/pdf/java/com.aspose.pdf/strikeoutannotation/) dengan persegi panjang, judul, dan warna.
1. Tambahkan anotasi ke halaman dan simpan dokumen.

```java
public static void textStrikeoutAnnotationAdd(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        StrikeOutAnnotation strikeoutAnnotation = new StrikeOutAnnotation(
                document.getPages().get_Item(1),
                new Rectangle(299.988, 713.664, 308.708, 720.769, true));
        strikeoutAnnotation.setTitle("Aspose User");
        strikeoutAnnotation.setSubject("Inserted text 1");
        strikeoutAnnotation.setFlags(AnnotationFlags.Print);
        strikeoutAnnotation.setColor(Color.getBlue());

        document.getPages().get_Item(1).getAnnotations().add(strikeoutAnnotation);
        document.save(outputFile.toString());
    }
}
```

### Mendapatkan anotasi coret

1. Buka PDF sumber [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Iterasikan melalui anotasi dan saring berdasarkan [`AnnotationType.StrikeOut`](https://reference.aspose.com/pdf/java/com.aspose.pdf/annotationtype/).
1. Baca metadata anotasi atau batas.

```java
public static void textStrikeoutAnnotationGet(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        for (Annotation annotation : document.getPages().get_Item(1).getAnnotations()) {
            if (annotation.getAnnotationType() == AnnotationType.StrikeOut) {
                System.out.println(annotation.getRect());
            }
        }
    }
}
```

### Menghapus anotasi coret

1. Buka PDF sumber [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Kumpulkan anotasi coret dengan memfilter berdasarkan tipe.
1. Hapus setiap anotasi dari halaman.
1. Simpan dokumen yang diperbarui.

```java
public static void textStrikeoutAnnotationDelete(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        List<Annotation> toDelete = new ArrayList<>();
        for (Annotation annotation : document.getPages().get_Item(1).getAnnotations()) {
            if (annotation.getAnnotationType() == AnnotationType.StrikeOut) {
                toDelete.add(annotation);
            }
        }
        for (Annotation annotation : toDelete) {
            document.getPages().get_Item(1).getAnnotations().delete(annotation);
        }
        document.save(outputFile.toString());
    }
}
```

## Menambahkan, mendapatkan, dan menghapus anotasi bergelombang

Anotasi bergelombang (garis bawah bergelombang) menyoroti potensi kesalahan, kekhawatiran, atau item yang memerlukan perhatian. Gunakan contoh-contoh ini untuk menandai teks yang bermasalah, memeriksa anotasi bergelombang, dan menghapusnya dari dokumen.

### Menambahkan anotasi bergelombang

1. Buka PDF sumber [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Buat sebuah [`SquigglyAnnotation`](https://reference.aspose.com/pdf/java/com.aspose.pdf/squigglyannotation/) dengan persegi panjang dan judul.
1. Tambahkan anotasi ke halaman dan simpan dokumen.

```java
public static void textSquigglyAnnotationAdd(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        Page page = document.getPages().get_Item(1);
        SquigglyAnnotation squigglyAnnotation = new SquigglyAnnotation(
                page,
                new Rectangle(67, 317, 261, 459, true));
        squigglyAnnotation.setTitle("John Smith");
        squigglyAnnotation.setColor(Color.getBlue());

        page.getAnnotations().add(squigglyAnnotation);
        document.save(outputFile.toString());
    }
}
```

### Mendapatkan anotasi bergelombang

1. Buka PDF sumber [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Iterasikan melalui anotasi dan saring berdasarkan [`AnnotationType.Squiggly`](https://reference.aspose.com/pdf/java/com.aspose.pdf/annotationtype/).
1. Baca batas anotasi atau metadata.

```java
public static void textSquigglyAnnotationGet(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        for (Annotation annotation : document.getPages().get_Item(1).getAnnotations()) {
            if (annotation.getAnnotationType() == AnnotationType.Squiggly) {
                System.out.println(annotation.getRect());
            }
        }
    }
}
```

### Menghapus anotasi bergelombang

1. Buka PDF sumber [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Kumpulkan anotasi bergelombang dengan memfilter berdasarkan tipe.
1. Hapus setiap anotasi dari halaman.
1. Simpan dokumen yang diperbarui.

```java
public static void textSquigglyAnnotationDelete(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        List<Annotation> toDelete = new ArrayList<>();
        for (Annotation annotation : document.getPages().get_Item(1).getAnnotations()) {
            if (annotation.getAnnotationType() == AnnotationType.Squiggly) {
                toDelete.add(annotation);
            }
        }
        for (Annotation annotation : toDelete) {
            document.getPages().get_Item(1).getAnnotations().delete(annotation);
        }
        document.save(outputFile.toString());
    }
}
```

## Menambahkan, mendapatkan, dan menghapus anotasi garis bawah

Anotasi garis bawah menekankan bagian penting dengan garis bawah tradisional. Gunakan contoh-contoh ini untuk membuat garis bawah, membaca konten teks yang ditandai, dan menghapus anotasi garis bawah dari halaman.

### Menambahkan anotasi garis bawah

1. Buka PDF sumber [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Buat sebuah [`UnderlineAnnotation`](https://reference.aspose.com/pdf/java/com.aspose.pdf/underlineannotation/) dengan persegi panjang dan warna.
1. Tambahkan anotasi ke halaman dan simpan dokumen.

```java
public static void textUnderlineAnnotationAdd(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        UnderlineAnnotation underlineAnnotation = new UnderlineAnnotation(
                document.getPages().get_Item(1),
                new Rectangle(299.988, 713.664, 308.708, 720.769, true));
        underlineAnnotation.setTitle("Aspose User");
        underlineAnnotation.setSubject("Inserted Underline 1");
        underlineAnnotation.setFlags(AnnotationFlags.Print);
        underlineAnnotation.setColor(Color.getBlue());

        document.getPages().get_Item(1).getAnnotations().add(underlineAnnotation);
        document.save(outputFile.toString());
    }
}
```

### Mendapatkan anotasi garis bawah

1. Buka PDF sumber [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Iterasikan melalui anotasi dan saring berdasarkan [`AnnotationType.Underline`](https://reference.aspose.com/pdf/java/com.aspose.pdf/annotationtype/).
1. Baca properti anotasi atau batas.

```java
public static void textUnderlineAnnotationGet(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        for (Annotation annotation : document.getPages().get_Item(1).getAnnotations()) {
            if (annotation.getAnnotationType() == AnnotationType.Underline) {
                System.out.println(annotation.getRect());
            }
        }
    }
}
```

### Menghapus anotasi garis bawah

1. Buka PDF sumber [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Kumpulkan anotasi garis bawah dengan memfilter berdasarkan tipe.
1. Hapus setiap anotasi dari halaman.
1. Simpan dokumen yang diperbarui.

```java
public static void textUnderlineAnnotationDelete(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        List<Annotation> toDelete = new ArrayList<>();
        for (Annotation annotation : document.getPages().get_Item(1).getAnnotations()) {
            if (annotation.getAnnotationType() == AnnotationType.Underline) {
                toDelete.add(annotation);
            }
        }
        for (Annotation annotation : toDelete) {
            document.getPages().get_Item(1).getAnnotations().delete(annotation);
        }
        document.save(outputFile.toString());
    }
}
```

## Menambahkan anotasi underline dengan quad points

Contoh ini mendefinisikan area garis bawah secara eksplisit melalui titik kuad yang diambil dari sebuah persegi panjang.

1. Buka PDF sumber [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Buat sebuah [`UnderlineAnnotation`](https://reference.aspose.com/pdf/java/com.aspose.pdf/underlineannotation/) dan hitung titik kuadnya.
1. Tambahkan anotasi ke halaman dan simpan dokumen.

```java
public static void textUnderlineWithQuadPointsAdd(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        Rectangle rect = new Rectangle(299.988, 713.664, 308.708, 720.769, true);
        UnderlineAnnotation underlineAnnotation = new UnderlineAnnotation(
                document.getPages().get_Item(1), rect);
        underlineAnnotation.setTitle("Aspose User");
        underlineAnnotation.setSubject("Inserted Underline with Quad Points");
        underlineAnnotation.setFlags(AnnotationFlags.Print);
        underlineAnnotation.setColor(Color.getBlue());
        underlineAnnotation.setQuadPoints(new com.aspose.pdf.Point[]{
                new com.aspose.pdf.Point(rect.getLLX(), rect.getLLY()),
                new com.aspose.pdf.Point(rect.getURX(), rect.getLLY()),
                new com.aspose.pdf.Point(rect.getURX(), rect.getURY()),
                new com.aspose.pdf.Point(rect.getLLX(), rect.getURY())
        });

        document.getPages().get_Item(1).getAnnotations().add(underlineAnnotation);
        document.save(outputFile.toString());
    }
}
```

## Mendapatkan teks yang ditandai dari anotasi garis bawah

Ambil konten teks sebenarnya yang dicakup oleh anotasi bergaris bawah. Contoh-contoh ini menunjukkan dua pendekatan: membaca seluruh teks yang ditandai sebagai satu string, atau memproses fragmen teks secara individual untuk analisis terperinci.

1. Buka PDF sumber [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Iterasikan melalui anotasi underline pada halaman.
1. Baca salah satu `getMarkedText()` atau `getMarkedTextFragments()` dan cetak hasilnya.

```java
public static void textUnderlineMarkedTextGet(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        for (Annotation annotation : document.getPages().get_Item(1).getAnnotations()) {
            if (annotation.getAnnotationType() == AnnotationType.Underline) {
                UnderlineAnnotation ua = (UnderlineAnnotation) annotation;
                System.out.println("Marked text: " + ua.getMarkedText());
            }
        }
    }
}
```

```java
public static void textUnderlineMarkedFragmentsGet(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        for (Annotation annotation : document.getPages().get_Item(1).getAnnotations()) {
            if (annotation.getAnnotationType() == AnnotationType.Underline) {
                UnderlineAnnotation ua = (UnderlineAnnotation) annotation;
                for (TextFragment fragment : ua.getMarkedTextFragments()) {
                    System.out.println("Fragment text: " + fragment.getText());
                }
            }
        }
    }
}
```

## Menghapus anotasi garis bawah berdasarkan judul

Hapus anotasi secara selektif dengan memfilter properti metadata seperti judul. Pendekatan ini memungkinkan pembersihan anotasi yang ditargetkan berdasarkan penulis atau tujuan.

1. Buka PDF sumber [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Filter anotasi garis bawah berdasarkan judul.
1. Hapus anotasi yang cocok dan simpan dokumen yang diperbarui.

```java
public static void textUnderlineByTitleDelete(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        List<UnderlineAnnotation> toDelete = new ArrayList<>();
        for (Annotation annotation : document.getPages().get_Item(1).getAnnotations()) {
            if (annotation.getAnnotationType() == AnnotationType.Underline) {
                UnderlineAnnotation ua = (UnderlineAnnotation) annotation;
                if ("Aspose User".equals(ua.getTitle())) {
                    toDelete.add(ua);
                }
            }
        }
        for (UnderlineAnnotation ua : toDelete) {
            document.getPages().get_Item(1).getAnnotations().delete(ua);
        }
        document.save(outputFile.toString());
    }
}
```

## Menambahkan dan meratakan anotasi garis bawah

Ubah anotasi garis bawah interaktif menjadi konten halaman permanen dengan meratakannya. Ini mencegah pengeditan lebih lanjut sambil mempertahankan tampilan garis bawah di semua penampil PDF.

1. Buka PDF sumber [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Tambahkan sebuah [`UnderlineAnnotation`](https://reference.aspose.com/pdf/java/com.aspose.pdf/underlineannotation/) ke halaman.
1. Panggil `flatten()` pada anotasi dan simpan file output.

```java
public static void textUnderlineFlattenAdd(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        UnderlineAnnotation underlineAnnotation = new UnderlineAnnotation(
                document.getPages().get_Item(1),
                new Rectangle(299.988, 713.664, 308.708, 720.769, true));
        underlineAnnotation.setTitle("Aspose User");
        underlineAnnotation.setSubject("Inserted Underline to Flatten");
        underlineAnnotation.setFlags(AnnotationFlags.Print);
        underlineAnnotation.setColor(Color.getBlue());

        document.getPages().get_Item(1).getAnnotations().add(underlineAnnotation);
        underlineAnnotation.flatten();

        document.save(outputFile.toString());
    }
}
```

## Topik anotasi terkait

- [Anotasi interaktif](/pdf/id/java/interactive-annotations/)
- [Anotasi markup](/pdf/id/java/markup-annotations/)
- [Anotasi keamanan](/pdf/id/java/security-annotations/)
- [Anotasi bentuk](/pdf/id/java/shape-annotations/)
- [Anotasi watermark](/pdf/id/java/watermark-annotations/)
- [Mengimpor dan mengekspor anotasi](/pdf/id/java/import-export-annotations/)
