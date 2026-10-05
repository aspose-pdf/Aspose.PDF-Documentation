---
title: "Memperbarui tautan PDF di Java"
linktitle: "Memperbarui tautan"
type: docs
weight: 20
url: /id/java/update-links/
description: Pelajari cara memperbarui tampilan tautan PDF dan tujuan di Java.
lastmod: "2026-09-30"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: "Memperbarui tampilan anotasi tautan dan tujuan web dalam file PDF dengan Java"
Abstract: Artikel ini menunjukkan cara memperbarui anotasi tautan yang ada menggunakan Aspose.PDF for Java. Contoh-contoh menunjukkan perubahan warna teks yang dicakup oleh tautan, memperbarui warna anotasi tautan, dan mengganti URI target untuk tautan web.
---
Tautan yang ada dapat diedit dengan menemukan anotasi tautan pada halaman dan memperbarui baik penampilannya maupun aksinya.

## Memperbarui warna teks yang ditautkan

Gunakan contoh ini ketika area teks yang dicakup oleh anotasi tautan harus diwarnai ulang.

1. Buka PDF sumber [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Temukan anotasi tautan dan buat persegi pencarian teks dari setiap area anotasi.
1. Ubah warna fragmen teks yang cocok dan simpan dokumen.

```java
public static void linkAnnotationUpdateTextColor(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        for (Annotation annotation : document.getPages().get_Item(1).getAnnotations()) {
            if (annotation.getAnnotationType() == AnnotationType.Link) {
                TextFragmentAbsorber absorber = new TextFragmentAbsorber();
                Rectangle rect = annotation.getRect();
                rect.setLLX(rect.getLLX() - 2);
                rect.setLLY(rect.getLLY() - 2);
                rect.setURX(rect.getURX() + 2);
                rect.setURY(rect.getURY() + 2);
                absorber.setTextSearchOptions(new TextSearchOptions(rect));
                absorber.visit(document.getPages().get_Item(1));
                for (TextFragment textFragment : absorber.getTextFragments()) {
                    textFragment.getTextState().setForegroundColor(Color.getRed());
                }
            }
        }

        document.save(outputFile.toString());
    }
}
```

## Memperbarui warna batas tautan

Gunakan contoh ini ketika warna yang terlihat dari anotasi tautan yang ada harus diubah.

1. Buka PDF sumber [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Iterasikan melalui anotasi halaman dan filter untuk objek [`LinkAnnotation`](https://reference.aspose.com/pdf/java/com.aspose.pdf/linkannotation/).
1. Perbarui warna anotasi tautan dan simpan dokumen.

```java
public static void linkAnnotationUpdateBorder(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        for (Annotation annotation : document.getPages().get_Item(1).getAnnotations()) {
            if (annotation.getAnnotationType() == AnnotationType.Link && annotation instanceof LinkAnnotation) {
                LinkAnnotation linkAnnotation = (LinkAnnotation) annotation;
                linkAnnotation.setColor(Color.getRed());
            }
        }

        document.save(outputFile.toString());
    }
}
```

## Memperbarui tujuan tautan web

Gunakan contoh ini ketika tautan web yang ada harus mengarah ke URI baru.

1. Buka PDF sumber [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Temukan anotasi tautan yang tindakannya adalah [`GoToURIAction`](https://reference.aspose.com/pdf/java/com.aspose.pdf/gotouriaction/).
1. Ganti URI dan simpan dokumen yang diperbarui.

```java
public static void linkAnnotationUpdateWebDestination(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        for (Annotation annotation : document.getPages().get_Item(1).getAnnotations()) {
            if (annotation.getAnnotationType() == AnnotationType.Link && annotation instanceof LinkAnnotation) {
                LinkAnnotation linkAnnotation = (LinkAnnotation) annotation;
                if (linkAnnotation.getAction() instanceof GoToURIAction) {
                    GoToURIAction action = (GoToURIAction) linkAnnotation.getAction();
                    action.setURI("https://www.aspose.com");
                }
            }
        }
        document.save(outputFile.toString());
    }
}
```
