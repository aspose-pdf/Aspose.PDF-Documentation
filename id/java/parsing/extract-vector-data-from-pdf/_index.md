---
title: "Mengekstrak data vektor dari file PDF menggunakan Java"
linktitle: "Mengekstrak data vektor dari PDF"
type: docs
weight: 80
url: /id/java/extract-vector-data-from-pdf/
description: Aspose.PDF memudahkan ekstraksi data vektor dari file PDF. Anda dapat memperoleh data vektor, seperti posisi, batas persegi panjang, dan output SVG.
lastmod: "2026-09-30"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
## Mengakses data vektor dari dokumen PDF

Gunakan `GraphicsAbsorber` untuk memeriksa elemen grafik vektor pada sebuah halaman dan menulis geometri dasar mereka ke file teks.

1. Buka PDF sumber dalam sebuah instans [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Buat sebuah [`GraphicsAbsorber`](https://reference.aspose.com/pdf/java/com.aspose.pdf.vector/graphicsabsorber/) dan kunjungi [`Page`](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) target untuk mengumpulkan operasi grafik vektor.
1. Iterasikan melalui objek [`GraphicElement`](https://reference.aspose.com/pdf/java/com.aspose.pdf.vector/graphicelement/) yang diekstrak dan membaca koleksi persegi panjang, posisi, dan operator mereka.
1. Bangun teks keluaran dengan detail geometri dan hitungan operator untuk setiap elemen.
1. Tuliskan data vektor yang diekstrak ke file keluaran.

```java
public static void extractGraphicsElements(Path inputFile, Path outputFile) throws Exception {
    try (Document document = new Document(inputFile.toString())) {
        GraphicsAbsorber absorber = new GraphicsAbsorber();
        absorber.visit(document.getPages().get_Item(1));

        StringBuilder text = new StringBuilder();
        int index = 1;
        for (GraphicElement element : absorber.getElements()) {
            text.append("Element ").append(index)
                    .append(": Rectangle = ").append(element.getRectangle())
                    .append(", Position = ").append(element.getPosition())
                    .append(", Operators = ").append(element.getOperators().size())
                    .append("\n");
            index++;
        }
        Files.writeString(outputFile, text.toString());
    }
}
```

## Menyimpan grafik vektor halaman ke SVG

1. Buka PDF sumber dalam sebuah instans [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Dapatkan [`Page`](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) target dari dokumen.
1. Panggil `page.trySaveVectorGraphics(outputFile.toString())` untuk mengekspor konten grafik vektor dari halaman itu langsung ke SVG.

```java
public static void saveVectorGraphicsToSvg(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        Page page = document.getPages().get_Item(1);
        page.trySaveVectorGraphics(outputFile.toString());
    }
}
```

## Menyimpan setiap elemen yang diekstrak ke file SVG terpisah

1. Buka PDF sumber dalam sebuah instans [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Buat sebuah [`GraphicsAbsorber`](https://reference.aspose.com/pdf/java/com.aspose.pdf.vector/graphicsabsorber/) dan kunjungi [`Page`](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) target.
1. Buat direktori output untuk subpath yang diekstrak sebelum menulis file apa pun.
1. Iterasikan melalui objek [`GraphicElement`](https://reference.aspose.com/pdf/java/com.aspose.pdf.vector/graphicelement/) yang diekstrak dan panggilan `saveToSvg(...)` untuk setiap elemen.
1. Simpan setiap elemen yang diekstrak ke file SVG terpisah.

```java
public static void extractSubpathsToSvgs(Path inputFile, Path outputDir) throws Exception {
    try (Document document = new Document(inputFile.toString())) {
        GraphicsAbsorber absorber = new GraphicsAbsorber();
        absorber.visit(document.getPages().get_Item(1));
        Path subpathsDir = outputDir.resolve("subpaths");
        Files.createDirectories(subpathsDir);

        int index = 1;
        for (GraphicElement element : absorber.getElements()) {
            element.saveToSvg(subpathsDir.resolve("subpath_" + index + ".svg").toString());
            index++;
        }
    }
}
```

## Menggabungkan elemen yang diekstrak menjadi satu SVG

1. Buka PDF sumber dalam sebuah instans [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Buat sebuah [`GraphicsAbsorber`](https://reference.aspose.com/pdf/java/com.aspose.pdf.vector/graphicsabsorber/) dan kunjungi [`Page`](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) target.
1. Buat markup pembungkus SVG yang akan berisi fragmen vektor yang digabungkan.
1. Iterasikan melalui objek [`GraphicElement`](https://reference.aspose.com/pdf/java/com.aspose.pdf.vector/graphicelement/) yang diekstrak dan tambahkan setiap fragmen SVG yang dihasilkan.
1. Tuliskan output SVG yang digabungkan ke file target.

```java
public static void extractListOfElementsToSingleImage(Path inputFile, Path outputFile) throws Exception {
    try (Document document = new Document(inputFile.toString())) {
        GraphicsAbsorber absorber = new GraphicsAbsorber();
        absorber.visit(document.getPages().get_Item(1));

        StringBuilder svg = new StringBuilder();
        svg.append("<svg xmlns=\"http://www.w3.org/2000/svg\">\n");
        for (GraphicElement element : absorber.getElements()) {
            svg.append(element.saveToSvg()).append("\n");
        }
        svg.append("</svg>\n");
        Files.writeString(outputFile, svg.toString());
    }
}
```

## Mengekstrak satu elemen vektor

1. Buka PDF sumber dalam sebuah instans [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Buat sebuah [`GraphicsAbsorber`](https://reference.aspose.com/pdf/java/com.aspose.pdf.vector/graphicsabsorber/) dan kunjungi [`Page`](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) target.
1. Dapatkan yang diperlukan [`GraphicElement`](https://reference.aspose.com/pdf/java/com.aspose.pdf.vector/graphicelement/) dari koleksi elemen yang diekstrak.
1. Periksa apakah elemen yang dipilih adalah [`XFormPlacement`](https://reference.aspose.com/pdf/java/com.aspose.pdf.vector/xformplacement/) dan turun ke elemen bersarangnya bila diperlukan.
1. Simpan elemen vektor yang dipilih ke file SVG output.

```java
public static void extractSingleVectorElement(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        GraphicsAbsorber graphicsAbsorber = new GraphicsAbsorber();
        Page page = document.getPages().get_Item(1);
        graphicsAbsorber.visit(page);
        if (graphicsAbsorber.getElements().size() > 1) {
            GraphicElement xformPlacement = graphicsAbsorber.getElements().get_Item(1);
            if (xformPlacement instanceof XFormPlacement) {
                XFormPlacement placement = (XFormPlacement) xformPlacement;
                if (placement.getElements().size() > 2) {
                    placement.getElements().get_Item(2).saveToSvg(outputFile.toString());
                }
            } else {
                xformPlacement.saveToSvg(outputFile.toString());
            }
        }
    }
}
```
