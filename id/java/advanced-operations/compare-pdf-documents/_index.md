---
title: Bandingkan Dokumen PDF dalam Java
linktitle: Bandingkan PDF
type: docs
weight: 130
url: /id/java/compare-pdf-documents/
description: Pelajari cara membandingkan dokumen PDF dalam Java menggunakan output perbedaan side-by-side dan grafis dengan Aspose.PDF.
lastmod: "2026-09-29"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Bandingkan halaman PDF dan dokumen lengkap dengan output perbedaan visual dalam Java
Abstract: Artikel ini menjelaskan cara membandingkan dokumen PDF menggunakan Aspose.PDF for Java. Pelajari cara membandingkan halaman tertentu atau seluruh file PDF dengan output berdampingan, menghasilkan laporan perbedaan PDF secara grafis, dan mengekspor perbedaan gambar tingkat halaman.
---
Aspose.PDF for Java menyediakan API perbandingan berdampingan dan grafis untuk mendeteksi perbedaan antara file PDF.

## Bandingkan halaman dan ekspor gambar perbedaan

Gunakan contoh ini ketika Anda memerlukan output perbedaan berbasis gambar untuk pasangan halaman PDF tertentu.

1. Buka kedua PDF sumber [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) objek.
1. Gunakan [GraphicalPdfComparer](https://reference.aspose.com/pdf/java/com.aspose.pdf/comparison/graphicalpdfcomparer/) untuk mendapatkan tingkat halaman [ImagesDifference](https://reference.aspose.com/pdf/java/com.aspose.pdf/comparison/imagesdifference/).
1. Gunakan 'GraphicalPdfComparer' untuk mendapatkan tingkat halaman 'ImagesDifference'.
1. Ekspor gambar perbedaan yang dihasilkan dan buang hasil perbandingan.

```java
public static void comparePdfWithGetDifferenceMethod(
        Path inputFile1, Path inputFile2, Path diffOutputFile, Path destinationOutputFile) throws Exception {
    try (Document document1 = new Document(inputFile1.toString());
         Document document2 = new Document(inputFile2.toString())) {
        GraphicalPdfComparer comparer = new GraphicalPdfComparer();
        ImagesDifference imagesDifference = comparer.getDifference(document1.getPages().get_Item(1),
                document2.getPages().get_Item(1));

        ImageIO.write(imagesDifference.differenceToImage(Color.getRed(), Color.getWhite()),
                "png", diffOutputFile.toFile());
        ImageIO.write(imagesDifference.getDestinationImage(), "png", destinationOutputFile.toFile());
        imagesDifference.dispose();
    }
    System.out.println("Difference images saved to " + diffOutputFile + " and " + destinationOutputFile);
}
```

## Bandingkan halaman tertentu berdampingan

Gunakan contoh ini ketika hanya halaman yang dipilih yang harus dibandingkan dan disimpan sebagai hasil PDF berdampingan.

1. Buka kedua PDF sumber [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) objek.
1. Konfigurasikan [SideBySideComparisonOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/comparison/sidebysidecomparisonoptions/) untuk mode perbandingan yang diperlukan.
1. Bandingkan halaman yang dipilih dan simpan PDF output.

```java
public static void comparingSpecificPages(Path inputFile1, Path inputFile2, Path outputFile) {
    try (Document document1 = new Document(inputFile1.toString());
         Document document2 = new Document(inputFile2.toString())) {
        SideBySideComparisonOptions options = new SideBySideComparisonOptions();
        options.setAdditionalChangeMarks(true);
        options.setComparisonMode(ComparisonMode.IgnoreSpaces);

        SideBySidePdfComparer.compare(document1.getPages().get_Item(1), document2.getPages().get_Item(1),
                outputFile.toString(), options);
    }
    System.out.println("Specific pages comparison saved to " + outputFile);
}
```

## Bandingkan dokumen PDF lengkap secara grafis

Contoh ini menghasilkan laporan PDF grafis yang menyoroti perbedaan visual di seluruh dokumen.

1. Buka kedua PDF sumber [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) objek.
1. Konfigurasikan [GraphicalPdfComparer](https://reference.aspose.com/pdf/java/com.aspose.pdf/comparison/graphicalpdfcomparer/) ambang batas, warna, dan resolusi.
1. Bandingkan seluruh dokumen dan simpan PDF output grafis.

```java
public static void comparePdfWithCompareDocumentsToPdfMethod(Path inputFile1, Path inputFile2, Path outputFile) {
    try (Document document1 = new Document(inputFile1.toString());
         Document document2 = new Document(inputFile2.toString())) {
        GraphicalPdfComparer pdfComparer = new GraphicalPdfComparer();
        pdfComparer.setThreshold(3.0);
        pdfComparer.setColor(Color.getBlue());
        pdfComparer.setResolution(new Resolution(300));
        pdfComparer.compareDocumentsToPdf(document1, document2, outputFile.toString());
    }
    System.out.println("Graphical comparison saved to " + outputFile);
}
```

## Bandingkan seluruh dokumen berdampingan

Gunakan contoh ini ketika seluruh dokumen harus dibandingkan halaman per halaman dalam output PDF berdampingan.

1. Buka kedua PDF sumber [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) objek.
1. Konfigurasikan [SideBySideComparisonOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/comparison/sidebysidecomparisonoptions/) untuk perilaku perbandingan yang diinginkan.
1. Bandingkan seluruh dokumen dan simpan hasilnya sebagai PDF.

```java
public static void comparingEntireDocuments(Path inputFile1, Path inputFile2, Path outputFile) {
    try (Document document1 = new Document(inputFile1.toString());
         Document document2 = new Document(inputFile2.toString())) {
        SideBySideComparisonOptions options = new SideBySideComparisonOptions();
        options.setAdditionalChangeMarks(true);
        options.setComparisonMode(ComparisonMode.IgnoreSpaces);

        SideBySidePdfComparer.compare(document1, document2, outputFile.toString(), options);
    }
    System.out.println("Entire document comparison saved to " + outputFile);
}
```
