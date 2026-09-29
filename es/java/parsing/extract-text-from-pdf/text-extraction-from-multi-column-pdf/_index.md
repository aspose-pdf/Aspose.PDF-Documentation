---
title: Mejorando la extracción de texto de PDFs de varias columnas
linktitle: Extracción de texto de PDFs de varias columnas
type: docs
weight: 30
url: /es/java/text-extraction-from-multi-column-pdf/
description: Aprenda técnicas para mejorar la extracción de texto de diseños PDF de varias columnas con Aspose.PDF for Java.
lastmod: "2026-09-29"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
Los diseños de varias columnas a menudo requieren procesamiento adicional para mejorar el orden de lectura y la calidad de la extracción.

## Extraer texto después de reducir el tamaño de fuente

Esta técnica actualiza los tamaños de fuente del fragmento de texto, guarda el documento ajustado en la memoria y luego extrae texto del resultado transformado.

1. Abra el PDF de origen en una instancia de [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Cree un [`TextFragmentAbsorber`](https://reference.aspose.com/pdf/java/com.aspose.pdf/textfragmentabsorber/) y visite todas las páginas del documento para recopilar [`TextFragment`](https://reference.aspose.com/pdf/java/com.aspose.pdf/textfragment/) objetos.
1. Itere a través de los fragmentos y reduzca el tamaño de cada fuente por la proporción solicitada para que el diseño de columnas densas pueda normalizarse antes de la extracción.
1. Guarde lo ajustado [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) en un flujo de bytes en memoria.
1. Reabra un segundo [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) desde ese búfer de memoria.
1. Cree un [`TextAbsorber`](https://reference.aspose.com/pdf/java/com.aspose.pdf/textabsorber/), visita todas las páginas del documento transformado, y escriba el texto extraído en el archivo de salida.

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

Utilice `TextExtractionOptions` en modo de formato puro y ajuste el factor de escala para diseños con muchas columnas.

1. Abra el PDF de origen en una instancia de [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Cree un [`TextAbsorber`](https://reference.aspose.com/pdf/java/com.aspose.pdf/textabsorber/) para la extracción de documento completo.
1. Cree [`TextExtractionOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/textextractionoptions/) en modo de formato puro para que se utilice el comportamiento de extracción sensible al diseño.
1. Establezca el factor de escala y aplique las opciones de extracción al absorbente antes de visitar las páginas.
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
