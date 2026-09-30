---
title: "Anotasi markup menggunakan Java"
linktitle: "Anotasi markup"
type: docs
weight: 30
url: /id/java/markup-annotations/
description: Pelajari cara menambahkan, memeriksa, dan menghapus anotasi sorotan, garis bawah, bergelombang, dan coret dalam dokumen PDF menggunakan Aspose.PDF for Java.
lastmod: "2026-09-30"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: "Bekerja dengan anotasi markup dalam file PDF menggunakan Java"
Abstract: Artikel ini menjelaskan cara membuat, memeriksa, dan menghapus anotasi markup teks dalam dokumen PDF menggunakan Aspose.PDF for Java. Ini mencakup anotasi sorot, garis bawah, bergelombang, dan coret berdasarkan contoh Java di repositori.
---
Alur kerja anotasi markup dalam bagian ini berfokus pada komentar bergaya catatan, penanda caret, dan skenario penggantian‑ulasan yang dikelompokkan.

## Menambahkan anotasi teks

Gunakan contoh ini ketika Anda perlu menempatkan anotasi teks gaya catatan tempel dengan metadata popup pada sebuah halaman.

1. Buka PDF sumber [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Buat sebuah [`TextAnnotation`](https://reference.aspose.com/pdf/java/com.aspose.pdf/textannotation/) dan mengatur judul, konten, ikon, dan popup-nya.
1. Tambahkan anotasi ke halaman dan simpan dokumen.

```java
public static void textAnnotationAdd(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        TextAnnotation textAnnotation = new TextAnnotation(
                document.getPages().get_Item(1),
                new Rectangle(299.988, 613.664, 428.708, 680.769, true));
        textAnnotation.setTitle("Aspose User");
        textAnnotation.setSubject("Sticky Note");
        textAnnotation.setContents("This is a text annotation added by Aspose.PDF for Java");
        textAnnotation.setFlags(AnnotationFlags.Print);
        textAnnotation.setColor(Color.getBlue());
        textAnnotation.setIcon(TextIcon.Help);

        PopupAnnotation popup = new PopupAnnotation(
                document.getPages().get_Item(1),
                new Rectangle(428.708, 613.664, 528.708, 713.664, true));
        popup.setOpen(true);
        textAnnotation.setPopup(popup);

        document.getPages().get_Item(1).getAnnotations().add(textAnnotation, false);
        document.save(outputFile.toString());
    }
}
```

## Mendapatkan anotasi teks

Contoh ini memindai halaman dan mencetak persegi panjang setiap anotasi teks.

1. Buka PDF sumber [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Iterasikan melalui anotasi pada halaman.
1. Filter anotasi berdasarkan [`AnnotationType`](https://reference.aspose.com/pdf/java/com.aspose.pdf/annotationtype/).`Text` dan cetak persegi panjang mereka.

```java
public static void textAnnotationGet(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        for (Annotation annotation : document.getPages().get_Item(1).getAnnotations()) {
            if (annotation.getAnnotationType() == AnnotationType.Text) {
                System.out.println(annotation.getRect());
            }
        }
    }
}
```

## Menghapus anotasi teks

Gunakan pendekatan ini ketika anotasi teks yang ada harus dihapus dari dokumen.

1. Buka PDF sumber [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Kumpulkan anotasi tipe [`AnnotationType`](https://reference.aspose.com/pdf/java/com.aspose.pdf/annotationtype/).`Text`.
1. Hapus anotasi yang dikumpulkan dan simpan file output.

```java
public static void textAnnotationDelete(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        List<Annotation> toDelete = new ArrayList<>();
        for (Annotation annotation : document.getPages().get_Item(1).getAnnotations()) {
            if (annotation.getAnnotationType() == AnnotationType.Text) {
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

## Menambahkan anotasi caret

Gunakan contoh ini saat Anda perlu menandai teks yang disisipkan dengan anotasi tinjauan bergaya caret.

1. Buka PDF sumber [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Buat sebuah [`CaretAnnotation`](https://reference.aspose.com/pdf/java/com.aspose.pdf/caretannotation/) dan atur popup serta tampilannya.
1. Tambahkan anotasi ke halaman dan simpan dokumen.

```java
public static void caretAnnotationsAdd(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        Page page = document.getPages().get_Item(1);

        CaretAnnotation caretAnnotation = new CaretAnnotation(
                page,
                new Rectangle(299.988, 713.664, 308.708, 720.769, true));
        caretAnnotation.setTitle("Aspose User");
        caretAnnotation.setSubject("Inserted text 1");
        caretAnnotation.setFlags(AnnotationFlags.Print);
        caretAnnotation.setColor(Color.getBlue());
        caretAnnotation.setPopup(new PopupAnnotation(
                page,
                new Rectangle(310, 713, 410, 730, true)));
        page.getAnnotations().add(caretAnnotation);

        document.save(outputFile.toString());
    }
}
```

## Mendapatkan anotasi caret

Contoh ini membaca anotasi caret yang ada dan mencetak lokasinya.

1. Buka PDF sumber [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Iterasikan anotasi halaman.
1. Filter anotasi berdasarkan [`AnnotationType`](https://reference.aspose.com/pdf/java/com.aspose.pdf/annotationtype/).`Caret` dan cetak persegi panjang mereka.

```java
public static void caretAnnotationsGet(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        Page page = document.getPages().get_Item(1);
        for (Annotation annot : page.getAnnotations()) {
            if (annot.getAnnotationType() == AnnotationType.Caret) {
                System.out.println(annot.getRect());
            }
        }
    }
}
```

## Menghapus anotasi caret

Gunakan pendekatan ini ketika anotasi caret harus dihapus dari halaman.

1. Buka PDF sumber [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Kumpulkan anotasi yang tipenya adalah [`AnnotationType`](https://reference.aspose.com/pdf/java/com.aspose.pdf/annotationtype/).`Caret`.
1. Hapus anotasi yang dikumpulkan dan simpan dokumen keluaran.

```java
public static void caretAnnotationsDelete(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        Page page = document.getPages().get_Item(1);

        List<Annotation> caretAnnotations = new ArrayList<>();
        for (Annotation annot : page.getAnnotations()) {
            if (annot.getAnnotationType() == AnnotationType.Caret) {
                caretAnnotations.add(annot);
            }
        }
        for (Annotation annot : caretAnnotations) {
            page.getAnnotations().delete(annot);
        }
        document.save(outputFile.toString());
    }
}
```

## Menambahkan anotasi pengganti berkelompok

Contoh ini menggabungkan anotasi caret dengan anotasi coret untuk mewakili komentar tinjauan bergaya penggantian.

1. Buka PDF sumber [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Buat anotasi caret dan yang terkait [`StrikeOutAnnotation`](https://reference.aspose.com/pdf/java/com.aspose.pdf/strikeoutannotation/).
1. Hubungkan anotasi melalui `setInReplyTo` dan `setReplyType`, lalu simpan dokumen.

```java
public static void replaceAnnotationsAdd(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        Page page = document.getPages().get_Item(1);

        CaretAnnotation caretAnnotation = new CaretAnnotation(
                page,
                new Rectangle(361.246, 727.908, 370.081, 735.107, true));
        caretAnnotation.setFlags(AnnotationFlags.Print);
        caretAnnotation.setSubject("Inserted text 2");
        caretAnnotation.setTitle("Aspose User");
        caretAnnotation.setColor(Color.getBlue());
        caretAnnotation.setPopup(new PopupAnnotation(
                page,
                new Rectangle(310, 713, 410, 730, true)));

        StrikeOutAnnotation strikeoutAnnotation = new StrikeOutAnnotation(
                page,
                new Rectangle(318.407, 727.826, 368.916, 740.098, true));
        strikeoutAnnotation.setColor(Color.getBlue());
        strikeoutAnnotation.setQuadPoints(new Point[]{
                new Point(321.66, 739.416),
                new Point(365.664, 739.416),
                new Point(321.66, 728.508),
                new Point(365.664, 728.508)
        });
        strikeoutAnnotation.setSubject("Cross-out");
        strikeoutAnnotation.setInReplyTo(caretAnnotation);
        strikeoutAnnotation.setReplyType(ReplyType.Group);

        page.getAnnotations().add(caretAnnotation);
        page.getAnnotations().add(strikeoutAnnotation);

        document.save(outputFile.toString());
    }
}
```

## Mendapatkan anotasi pengganti yang dikelompokkan

Contoh ini mendeteksi anotasi coret yang berpartisipasi dalam alur kerja penggantian berkelompok.

1. Buka PDF sumber [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Iterasikan anotasi halaman dan pilih anotasi coret.
1. Periksa hubungan balasan dan cetak persegi panjang anotasi yang cocok.

```java
public static void replaceAnnotationsGet(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        Page page = document.getPages().get_Item(1);
        for (Annotation annot : page.getAnnotations()) {
            if (annot.getAnnotationType() == AnnotationType.StrikeOut) {
                StrikeOutAnnotation sa = (StrikeOutAnnotation) annot;
                if (sa.getInReplyTo() != null && sa.getReplyType() == ReplyType.Group) {
                    System.out.println("Replace annotation rect: " + sa.getRect());
                }
            }
        }
    }
}
```

## Menghapus anotasi pengganti yang dikelompokkan

Gunakan pendekatan ini ketika anotasi coret replace-review harus dihapus dari halaman.

1. Buka PDF sumber [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Kumpulkan anotasi coret yang mewakili markup pengganti.
1. Hapus anotasi yang dikumpulkan dan simpan dokumen yang diperbarui.

```java
public static void replaceAnnotationsDelete(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        Page page = document.getPages().get_Item(1);

        List<StrikeOutAnnotation> replaceAnnotations = new ArrayList<>();
        for (Annotation annot : page.getAnnotations()) {
            if (annot.getAnnotationType() == AnnotationType.StrikeOut) {
                replaceAnnotations.add((StrikeOutAnnotation) annot);
            }
        }
        for (StrikeOutAnnotation annot : replaceAnnotations) {
            page.getAnnotations().delete(annot);
        }
        document.save(outputFile.toString());
    }
}
```

## Topik anotasi terkait

- [Anotasi teks](/pdf/id/java/text-based-annotations/)
- [Anotasi interaktif](/pdf/id/java/interactive-annotations/)
- [Anotasi bentuk](/pdf/id/java/shape-annotations/)
- [Anotasi media](/pdf/id/java/media-annotations/)
- [Anotasi keamanan](/pdf/id/java/security-annotations/)
- [Anotasi watermark](/pdf/id/java/watermark-annotations/)
