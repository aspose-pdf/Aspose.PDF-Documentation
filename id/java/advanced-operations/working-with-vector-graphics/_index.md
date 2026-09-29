---
title: Bekerja dengan Vektor Grafik di Java
linktitle: Bekerja dengan Vektor Grafik
type: docs
weight: 100
url: /id/java/working-with-vector-graphics/
description: Pelajari cara mengekstrak, memindahkan, menghapus, menyalin, dan mengekspor grafis vektor dalam dokumen PDF menggunakan Java.
lastmod: "2026-09-29"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Gunakan GraphicsAbsorber untuk memeriksa dan memanipulasi grafis vektor PDF dalam Java.
Abstract: Artikel ini menjelaskan cara bekerja dengan grafik vektor di Aspose.PDF for Java menggunakan kelas GraphicsAbsorber. Pelajari cara memeriksa elemen vektor pada halaman, memindahkan atau menghapusnya, menyalin grafik antar halaman, dan mengekspor konten vektor ke SVG.
---
Aspose.PDF for Java mengekspos konten vektor melalui `GraphicsAbsorber` dan `GraphicElement` objek. Ini memungkinkan Anda memeriksa elemen vektor tingkat rendah pada sebuah halaman dan kemudian memperbarui, menghapus, menyalin, atau mengekspornya.

## Periksa grafik vektor pada halaman

Gunakan contoh ini ketika Anda perlu mengenumerasi elemen vektor dan memeriksa halaman, posisi, serta jumlah operatornya.

1. Buka PDF sumber [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Buat [GraphicsAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/vector/graphicsabsorber/) dan kunjungi halaman target.
1. Iterasi melalui yang diserap [GraphicElement](https://reference.aspose.com/pdf/java/com.aspose.pdf/vector/graphicelement/) objek dan keluarkan properti mereka.

```java
public static void usingGraphicsAbsorber(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        GraphicsAbsorber graphicsAbsorber = new GraphicsAbsorber();
        try {
            Page page = document.getPages().get_Item(1);
            graphicsAbsorber.visit(page);
            for (GraphicElement element : graphicsAbsorber.getElements()) {
                System.out.println("Page Number: " + element.getSourcePage().getNumber());
                System.out.println("Position: (" + element.getPosition().getX() + ", "
                        + element.getPosition().getY() + ")");
                System.out.println("Number of Operators: " + element.getOperators().size());
            }
        } finally {
            graphicsAbsorber.dispose();
        }
    }
}
```

## Pindahkan grafik vektor pada halaman

Gunakan contoh ini ketika semua elemen vektor yang terdeteksi harus dipindahkan ke posisi baru.

1. Buka PDF sumber [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Kunjungi halaman target dengan [GraphicsAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/vector/graphicsabsorber/) dan sementara menonaktifkan pembaruan.
1. Ubah posisi setiap elemen yang diserap, lanjutkan pembaruan, dan simpan dokumen.

```java
public static void moveGraphics(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        GraphicsAbsorber graphicsAbsorber = new GraphicsAbsorber();
        try {
            Page page = document.getPages().get_Item(1);
            graphicsAbsorber.visit(page);
            graphicsAbsorber.suppressUpdate();
            for (GraphicElement element : graphicsAbsorber.getElements()) {
                Point position = element.getPosition();
                element.setPosition(new Point(position.getX() + 150, position.getY() - 10));
            }
            graphicsAbsorber.resumeUpdate();
        } finally {
            graphicsAbsorber.dispose();
        }
        document.save(outputFile.toString());
    }
    System.out.println("Vector graphics moved in " + outputFile);
}
```

## Hapus grafik vektor berdasarkan posisi dengan penghapusan elemen

Gunakan contoh ini ketika elemen vektor di dalam persegi panjang tertentu harus dihapus satu per satu.

1. Buka PDF sumber [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Kunjungi halaman dengan [GraphicsAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/vector/graphicsabsorber/) dan definisikan target [Rectangle](https://reference.aspose.com/pdf/java/com.aspose.pdf/rectangle/).
1. Hapus elemen yang cocok, lanjutkan pembaruan, dan simpan dokumen.

```java
public static void removeGraphicsMethod1(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        GraphicsAbsorber graphicsAbsorber = new GraphicsAbsorber();
        try {
            Page page = document.getPages().get_Item(1);
            Rectangle rectangle = new Rectangle(70, 248, 170, 252, true);
            graphicsAbsorber.visit(page);
            graphicsAbsorber.suppressUpdate();
            for (GraphicElement element : graphicsAbsorber.getElements()) {
                if (rectangle.contains(element.getPosition(), false)) {
                    element.remove();
                }
            }
            graphicsAbsorber.resumeUpdate();
        } finally {
            graphicsAbsorber.dispose();
        }
        document.save(outputFile.toString());
    }
    System.out.println("Vector graphics removed with method 1 in " + outputFile);
}
```

## Hapus grafik vektor dengan menghapus koleksi

Gunakan contoh ini ketika elemen vektor yang cocok harus dikumpulkan terlebih dahulu dan kemudian dihapus dalam satu operasi halaman.

1. Buka PDF sumber [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Kunjungi halaman dengan [GraphicsAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/vector/graphicsabsorber/) dan kumpulkan elemen yang cocok.
1. Hapus grafik yang terkumpul dari konten halaman dan simpan dokumen yang telah diperbarui.

```java
public static void removeGraphicsMethod2(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        GraphicsAbsorber graphicsAbsorber = new GraphicsAbsorber();
        try {
            Page page = document.getPages().get_Item(1);
            Rectangle rectangle = new Rectangle(70, 248, 170, 252, true);
            graphicsAbsorber.visit(page);
            GraphicElementCollection removedElements = new GraphicElementCollection();
            for (GraphicElement element : graphicsAbsorber.getElements()) {
                if (rectangle.contains(element.getPosition(), false)) {
                    removedElements.add(element);
                }
            }
            page.getContents().suppressUpdate();
            page.deleteGraphics(removedElements);
            page.getContents().resumeUpdate();
        } finally {
            graphicsAbsorber.dispose();
        }
        document.save(outputFile.toString());
    }
    System.out.println("Vector graphics removed with method 2 in " + outputFile);
}
```

## Salin grafik vektor ke elemen halaman lain elemen demi elemen

Gunakan contoh ini ketika setiap elemen vektor yang diserap harus ditambahkan secara individu ke halaman baru.

1. Buka PDF sumber [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) dan tambahkan halaman tujuan.
1. Kunjungi halaman sumber dengan [GraphicsAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/vector/graphicsabsorber/).
1. Tambahkan masing-masing [GraphicElement](https://reference.aspose.com/pdf/java/com.aspose.pdf/vector/graphicelement/) ke halaman tujuan dan simpan dokumen.

```java
public static void addToAnotherPageMethod1(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        GraphicsAbsorber graphicsAbsorber = new GraphicsAbsorber();
        try {
            Page page1 = document.getPages().get_Item(1);
            Page page2 = document.getPages().add();
            graphicsAbsorber.visit(page1);
            page2.getContents().suppressUpdate();
            for (GraphicElement element : graphicsAbsorber.getElements()) {
                element.addOnPage(page2);
            }
            page2.getContents().resumeUpdate();
        } finally {
            graphicsAbsorber.dispose();
        }
        document.save(outputFile.toString());
    }
    System.out.println("Vector graphics copied with method 1 in " + outputFile);
}
```

## Salin grafik vektor ke halaman lain sebagai koleksi

Gunakan contoh ini ketika seluruh koleksi grafis vektor yang diserap harus disalin ke halaman baru dalam satu panggilan.

1. Buka PDF sumber [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) dan tambahkan halaman tujuan.
1. Kunjungi halaman sumber dengan [GraphicsAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/vector/graphicsabsorber/).
1. Tambahkan koleksi grafik yang diserap ke halaman tujuan dan simpan dokumen.

```java
public static void addToAnotherPageMethod2(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        GraphicsAbsorber graphicsAbsorber = new GraphicsAbsorber();
        try {
            Page page1 = document.getPages().get_Item(1);
            Page page2 = document.getPages().add();
            graphicsAbsorber.visit(page1);
            page2.getContents().suppressUpdate();
            page2.addGraphics(graphicsAbsorber.getElements());
            page2.getContents().resumeUpdate();
        } finally {
            graphicsAbsorber.dispose();
        }
        document.save(outputFile.toString());
    }
    System.out.println("Vector graphics copied with method 2 in " + outputFile);
}
```
