---
title: Comparar documentos PDF en Java
linktitle: Comparar PDF
type: docs
weight: 130
url: /es/java/compare-pdf-documents/
description: Aprenda cómo comparar documentos PDF en Java usando una salida de diferencias lado a lado y gráfica con Aspose.PDF.
lastmod: "2026-09-03"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Compare páginas PDF y documentos completos con salida visual de diferencias en Java
Abstract: Este artículo explica cómo comparar documentos PDF usando Aspose.PDF for Java. Aprenda cómo comparar páginas específicas o archivos PDF completos con salida lado a lado, generar informes gráficos de diferencias PDF y exportar diferencias de imagen a nivel de página.
---
Aspose.PDF for Java proporciona API de comparación tanto lado a lado como gráficas para detectar diferencias entre archivos PDF.

## Compare páginas y exporta imágenes de diferencias

Utilice este ejemplo cuando necesite una salida de diferencias basada en imágenes para un par específico de páginas PDF.

1. Abrir ambos PDF de origen [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) objetos.
1. Usar [GraphicalPdfComparer](https://reference.aspose.com/pdf/java/com.aspose.pdf/comparison/graphicalpdfcomparer/) para obtener el nivel de página [ImagesDifference](https://reference.aspose.com/pdf/java/com.aspose.pdf/comparison/imagesdifference/).
1. Utilice 'GraphicalPdfComparer' para obtener el 'ImagesDifference' a nivel de página.
1. Exporta las imágenes de diferencia generadas y libera el resultado de la comparación.

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

## Comparar páginas específicas lado a lado

Utilice este ejemplo cuando solo se deban comparar páginas seleccionadas y guardarse como un PDF resultante lado a lado.

1. Abrir ambos PDF de origen [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) objetos.
1. Configurar [SideBySideComparisonOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/comparison/sidebysidecomparisonoptions/) para el modo de comparación requerido.
1. Compare las páginas seleccionadas y guarde el PDF de salida.

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

## Comparar documentos PDF completos gráficamente

Este ejemplo genera un informe PDF gráfico que resalta las diferencias visuales en todos los documentos.

1. Abrir ambos PDF de origen [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) objetos.
1. Configure el [GraphicalPdfComparer](https://reference.aspose.com/pdf/java/com.aspose.pdf/comparison/graphicalpdfcomparer/) umbral, color y resolución.
1. Compare los documentos completos y guarde el PDF de salida gráfico.

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

## Comparar documentos completos lado a lado

Utilice este ejemplo cuando los documentos completos deban compararse página por página en una salida PDF lado a lado.

1. Abrir ambos PDF de origen [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) objetos.
1. Configurar [SideBySideComparisonOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/comparison/sidebysidecomparisonoptions/) para el comportamiento de comparación deseado.
1. Compare los documentos completos y guarde el resultado como un PDF.

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
