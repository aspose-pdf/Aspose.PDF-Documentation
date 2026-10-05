---
title: "Membuat tautan PDF di Java"
linktitle: "Membuat tautan"
type: docs
weight: 10
url: /id/java/create-links/
description: Pelajari cara membuat tautan PDF internal, eksternal, dan remote di Java.
lastmod: "2026-09-30"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: "Membuat anotasi tautan di file PDF dengan Java"
Abstract: Artikel ini menunjukkan cara membuat anotasi tautan menggunakan Aspose.PDF for Java. Ini mencakup tindakan peluncuran, navigasi dokumen jarak jauh, navigasi halaman dalam dokumen, dan tautan web berbasis URI dengan melampirkan tindakan ke objek LinkAnnotation.
---
Aspose.PDF for Java menggunakan `LinkAnnotation` bersama dengan objek aksi untuk mendefinisikan perilaku tautan.

## Membuat tautan aksi peluncuran

Gunakan contoh ini ketika anotasi tautan harus meluncurkan file eksternal atau target.

1. Buka PDF sumber [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) dan pilih halaman target.
1. Buat sebuah [`LinkAnnotation`](https://reference.aspose.com/pdf/java/com.aspose.pdf/linkannotation/) dan mengonfigurasi batas serta warnanya.
1. Tetapkan sebuah [`LaunchAction`](https://reference.aspose.com/pdf/java/com.aspose.pdf/launchaction/) dan simpan dokumen.

```java
public static void createLinkAnnotationLaunchAction(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        Page page = document.getPages().get_Item(1);

        LinkAnnotation link = new LinkAnnotation(page, new Rectangle(10, 580, 120, 600, true));
        Border border = new Border(link);
        border.setWidth(5);
        border.setDash(new Dash(1, 1));
        link.setBorder(border);
        link.setColor(Color.getGreen());
        link.setAction(new LaunchAction(document, inputFile.toString()));
        page.getAnnotations().add(link);
        document.save(outputFile.toString());
    }
}
```

## Membuat tautan go-to remote

Gunakan contoh ini ketika tautan harus membuka halaman di dokumen PDF lain.

1. Buka PDF sumber [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Buat sebuah [`LinkAnnotation`](https://reference.aspose.com/pdf/java/com.aspose.pdf/linkannotation/) pada halaman target.
1. Tetapkan sebuah [`GoToRemoteAction`](https://reference.aspose.com/pdf/java/com.aspose.pdf/gotoremoteaction/) dan simpan file output.

```java
public static void createLinkAnnotationGoToRemoteAction(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        Page page = document.getPages().get_Item(1);

        LinkAnnotation link = new LinkAnnotation(page, new Rectangle(10, 580, 120, 600, true));
        link.setColor(Color.getGreen());
        link.setAction(new GoToRemoteAction(inputFile.toString(), 1));
        page.getAnnotations().add(link);
        document.save(outputFile.toString());
    }
}
```

## Membuat tautan go-to internal

Gunakan contoh ini ketika tautan harus menavigasi ke halaman lain di dalam dokumen PDF yang sama.

1. Buka PDF sumber [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Buat sebuah [`LinkAnnotation`](https://reference.aspose.com/pdf/java/com.aspose.pdf/linkannotation/) dan konfigurasikan tampilannya.
1. Tetapkan sebuah [`GoToAction`](https://reference.aspose.com/pdf/java/com.aspose.pdf/gotoaction/) ke halaman tujuan dan simpan dokumen.

```java
public static void createLinkAnnotationGoToAction(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        Page page = document.getPages().get_Item(1);

        LinkAnnotation link = new LinkAnnotation(page, new Rectangle(10, 580, 120, 600, true));
        Border border = new Border(link);
        border.setWidth(5);
        border.setDash(new Dash(1, 1));
        link.setBorder(border);
        link.setColor(Color.getGreen());
        if (document.getPages().size() >= 4) {
            link.setAction(new GoToAction(document.getPages().get_Item(4)));
        } else {
            link.setAction(new GoToAction(document.getPages().get_Item(document.getPages().size())));
        }
        page.getAnnotations().add(link);
        document.save(outputFile.toString());
    }
}
```

## Membuat tautan URI

Gunakan contoh ini ketika tautan harus membuka sumber daya web melalui aksi URI.

1. Buka PDF sumber [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Buat sebuah [`LinkAnnotation`](https://reference.aspose.com/pdf/java/com.aspose.pdf/linkannotation/) pada halaman.
1. Tetapkan sebuah [`GoToURIAction`](https://reference.aspose.com/pdf/java/com.aspose.pdf/gotouriaction/) dan simpan file output.

```java
public static void createLinkAnnotationGoToUriAction(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        Page page = document.getPages().get_Item(1);

        LinkAnnotation link = new LinkAnnotation(page, new Rectangle(10, 580, 120, 600, true));
        link.setColor(Color.getGreen());
        link.setAction(new GoToURIAction("https://docs.aspose.com/pdf/python"));
        page.getAnnotations().add(link);
        document.save(outputFile.toString());
    }
}
```
