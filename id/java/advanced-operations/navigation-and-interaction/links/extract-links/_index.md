---
title: Ekstrak Tautan PDF di Java
linktitle: Ekstrak Tautan
type: docs
weight: 30
url: /id/java/extract-links/
description: Pelajari cara mengekstrak anotasi tautan dan hyperlink dari dokumen PDF dalam Java.
lastmod: "2026-09-29"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Ekstrak anotasi tautan dan target URI dari file PDF dengan Java
Abstract: Artikel ini menjelaskan cara mengekstrak anotasi tautan dari dokumen PDF menggunakan Aspose.PDF for Java. Artikel ini menunjukkan cara menghitung anotasi tautan pada sebuah halaman, membaca indeks halaman dan persegiannya, serta mengekstrak target URI dari instance GoToURIAction.
---
Anda dapat memeriksa tautan PDF dengan mengiterasi anotasi halaman dan memfilter untuk `AnnotationType.Link`.

## Ekstrak anotasi tautan

Gunakan contoh ini ketika Anda memerlukan lokasi dan informasi halaman untuk anotasi tautan pada sebuah halaman.

1. Buka PDF sumber [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Iterasi melalui anotasi halaman dan saring untuk anotasi tautan.
1. Baca indeks halaman dan persegi panjang untuk setiap tautan yang cocok.

```java
public static void extractLinkAnnotation(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        for (Annotation annotation : document.getPages().get_Item(1).getAnnotations()) {
            if (annotation.getAnnotationType() == AnnotationType.Link && annotation instanceof LinkAnnotation) {
                LinkAnnotation linkAnnotation = (LinkAnnotation) annotation;
                System.out.println("Page: " + linkAnnotation.getPageIndex()
                        + ", location: " + linkAnnotation.getRect());
            }
        }
    }
}
```

## Ekstrak tujuan hyperlink

Gunakan contoh ini ketika Anda perlu membaca URI target dari anotasi tautan web.

1. Buka PDF sumber [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Cari [LinkAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/linkannotation/) objek yang tindakannya adalah [GoToURIAction](https://reference.aspose.com/pdf/java/com.aspose.pdf/gotouriaction/).
1. Cetak indeks halaman dan target URI untuk setiap hyperlink.

```java
public static void extractHyperlinks(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        for (Annotation annotation : document.getPages().get_Item(1).getAnnotations()) {
            if (annotation.getAnnotationType() == AnnotationType.Link && annotation instanceof LinkAnnotation) {
                LinkAnnotation linkAnnotation = (LinkAnnotation) annotation;
                if (linkAnnotation.getAction() instanceof GoToURIAction) {
                    GoToURIAction action = (GoToURIAction) linkAnnotation.getAction();
                    System.out.println("Page " + linkAnnotation.getPageIndex() + ", URI:" + action.getURI());
                }
            }
        }
    }
}
```
