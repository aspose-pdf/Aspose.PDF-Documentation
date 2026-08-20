---
title: Comparar documentos PDF en Java
linktitle: Comparar PDF
type: docs
weight: 130
url: /java/compare-pdf-documents/
description: Aprenda a comparar documentos PDF en Java utilizando salidas gráficas y en paralelo con Aspose.PDF.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Compare páginas PDF y documentos completos con resultados de diferencia visual en Java
Abstract: Este artículo explica cómo comparar documentos PDF usando Aspose.PDF para Java. Aprenda a comparar páginas específicas o archivos PDF completos con salida en paralelo, generar informes gráficos de diferencias en PDF y exportar diferencias de imágenes a nivel de página.
---
Aspose.PDF para Java proporciona API de comparación gráfica y en paralelo para detectar diferencias entre archivos PDF.


## 
Compara páginas y exporta imágenes diferentes



Utilice este ejemplo cuando necesite una salida diferenciada basada en imágenes para un par específico de páginas PDF.


1. 
Abra ambos objetos PDF de origen [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

1. 
Utilice [GraphicalPdfComparer](https://reference.aspose.com/pdf/java/com.aspose.pdf/comparison/graphicalpdfcomparer/) para obtener la [ImagesDifference](https://reference.aspose.com/pdf/java/com.aspose.pdf/comparison/imagesdifference/) a nivel de página.
1. Utilice 'GraphicalPdfComparer' para obtener la 'ImagesDifference' a nivel de página.

1. 
Exporte las imágenes de diferencias generadas y elimine el resultado de la comparación.


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

## 
Compara páginas específicas una al lado de la otra



Utilice este ejemplo cuando solo las páginas seleccionadas deban compararse y guardarse como un resultado PDF uno al lado del otro.


1. 
Abra ambos objetos PDF de origen [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Configure [SideBySideComparisonOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/comparison/sidebysidecomparisonoptions/) para el modo de comparación requerido.

1. 
Compare las páginas seleccionadas y guarde el PDF de salida.


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

## 
Compara documentos PDF completos gráficamente



Este ejemplo genera un informe gráfico en PDF que resalta las diferencias visuales en todos los documentos.


1. 
Abra ambos objetos PDF de origen [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Configure el umbral, el color y la resolución de [GraphicalPdfComparer](https://reference.aspose.com/pdf/java/com.aspose.pdf/comparison/graphicalpdfcomparer/).

1. 
Compare los documentos completos y guarde el PDF de salida gráfica.


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

## 
Compare documentos completos uno al lado del otro



Utilice este ejemplo cuando los documentos completos deban compararse página por página en una salida PDF lado a lado.


1. 
Abra ambos objetos PDF de origen [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Configure [SideBySideComparisonOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/comparison/sidebysidecomparisonoptions/) para el comportamiento de comparación deseado.

1. 
Compare los documentos completos y guarde el resultado como PDF.

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
