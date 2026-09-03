---
title: Mejorando la extracción de texto de PDFs de varias columnas
linktitle: Extracción de texto de PDFs de varias columnas
type: docs
weight: 30
url: /es/java/text-extraction-from-multi-column-pdf/
description: Aprenda técnicas para mejorar la extracción de texto de diseños PDF de varias columnas con Aspose.PDF for Java.
lastmod: "2026-09-03"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
Los diseños de varias columnas a menudo requieren procesamiento adicional para mejorar el orden de lectura y la calidad de la extracción.

## Extraer texto después de reducir el tamaño de fuente

Esta técnica actualiza los tamaños de fuente de los fragmentos de texto, guarda el documento ajustado en memoria y luego extrae texto del resultado transformado.

1. Abrir el PDF de origen en un [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) instancia.
1. Crear un [TextFragmentAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/textfragmentabsorber/) y visitar todas las páginas del documento para recopilar [TextFragment](https://reference.aspose.com/pdf/java/com.aspose.pdf/textfragment/) objetos.
1. Itera a través de los fragmentos y reduce el tamaño de fuente de cada uno según la proporción solicitada para que el diseño denso de columnas pueda normalizarse antes de la extracción.
1. Guarda lo ajustado [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) a un flujo de bytes en memoria.
1. Reabrir un segundo [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) desde ese búfer de memoria.
1. Crear un [TextAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/textabsorber/), visite todas las páginas del documento transformado y escriba el texto extraído en el archivo de salida.

```java
public static void extractTextReduceFont(Path inputFile, Path outputFile, double reduceRatio) throws Exception {
    try (Document document = new Document(inputFile.toString())) {
        TextFragmentAbsorber fragmentAbsorber = new TextFragmentAbsorber();
        document.getPages().accept(fragmentAbsorber);
        for (TextFragment fragment : fragmentAbsorber.getTextFragments()) {
            fragment.getTextState().setFontSize((float) (fragment.getTextState().getFontSize() * reduceRatio));
        }

        ByteArrayOutputStream stream = new ByteArrayOutputStream();
        document.save(stream);
        try (Document document2 = new Document(new ByteArrayInputStream(stream.toByteArray()))) {
            TextAbsorber textAbsorber = new TextAbsorber();
            document2.getPages().accept(textAbsorber);
            Files.writeString(outputFile, textAbsorber.getText());
        }
    }
}
```

## Extraer texto con un factor de escala

Usar `TextExtractionOptions` en modo de formato puro y ajustar el factor de escala para diseños con muchas columnas.

1. Abrir el PDF de origen en un [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) instancia.
1. Crear un [TextAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/textabsorber/) para extracción de documento completo.
1. Crear [TextExtractionOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/textextractionoptions/) en modo de formato puro para que se use el comportamiento de extracción sensible al diseño.
1. Establezca el factor de escala y aplique las opciones de extracción al absorber antes de visitar las páginas.
1. Visite todas las páginas del documento y escriba el texto extraído en el archivo de salida.

```java
public static void extractTextScaleFactor(Path inputFile, Path outputFile, double scaleFactor) throws Exception {
    try (Document document = new Document(inputFile.toString())) {
        TextAbsorber textAbsorber = new TextAbsorber();
        TextExtractionOptions extractionOptions =
                new TextExtractionOptions(TextExtractionOptions.TextFormattingMode.Pure);
        extractionOptions.setScaleFactor(scaleFactor);
        textAbsorber.setExtractionOptions(extractionOptions);
        document.getPages().accept(textAbsorber);
        Files.writeString(outputFile, textAbsorber.getText());
    }
}
```
