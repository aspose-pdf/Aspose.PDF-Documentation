---
title: Extrayendo texto sin formato de archivo PDF
linktitle: Extraer texto de PDF
type: docs
weight: 10
url: /es/androidjava/extract-text-from-all-pdf/
description: Este artículo describe varias formas de extraer texto de documentos PDF usando Aspose.PDF for Android via Java. Desde páginas completas, desde una parte específica, basado en columnas, etc.
lastmod: "2026-06-30"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Extraer texto de todas las páginas de un documento PDF

Extraer texto de un documento PDF es una necesidad común. En este ejemplo, verás cómo Aspose.PDF for Java permite extraer texto de todas las páginas de un documento PDF.
Para extraer texto de todas las páginas del PDF:

1. Crear un objeto de la [TextAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextAbsorber) clase.
1. Abrir el PDF usando [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) clase y llamar al [Aceptar](https://reference.aspose.com/pdf/java/com.aspose.pdf/PageCollection#accept-com.aspose.pdf.TextAbsorber-) método del [Páginas](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page) colección.
1. El [TextAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextAbsorber) La clase absorbe el texto del documento y lo devuelve en la propiedad **Text**.

El siguiente fragmento de código le muestra cómo extraer texto de todas las páginas del documento PDF.

```java
public static void ExtractFromAllPages() {
        // The path to the documents directory.

        String filePath = _dataDir + "ExtractTextAll.pdf";

        // Open document
        Document pdfDocument = new com.aspose.pdf.Document(filePath);

        // Create TextAbsorber object to extract text
        TextAbsorber textAbsorber = new com.aspose.pdf.TextAbsorber();

        // Accept the absorber for all the pages
        pdfDocument.getPages().accept(textAbsorber);

        // Get the extracted text
        String extractedText = textAbsorber.getText();
        try {
            java.io.FileWriter writer = new java.io.FileWriter(_dataDir + "extracted-text.txt", true);
            // Write a line of text to the file
            writer.write(extractedText);
            // Close the stream
            writer.close();
        } catch (java.io.IOException e) {
            e.printStackTrace();
        }

    }
```

## Extraer texto resaltado de documento PDF

En varios escenarios de extracción de texto de un documento PDF, puede surgir la necesidad de extraer solo el texto resaltado del documento PDF. Para implementar la funcionalidad, hemos añadido los métodos TextMarkupAnnotation.GetMarkedText() y TextMarkupAnnotation.GetMarkedTextFragments() en la API. Puede extraer el texto resaltado del documento PDF filtrando TextMarkupAnnotation y utilizando los métodos mencionados. El siguiente fragmento de código muestra cómo puede extraer el texto resaltado del documento PDF.

```java
public static void ExtractHighlightedText() {
        Document doc = new Document(_dataDir + "ExtractHighlightedText.pdf");
        // Loop through all the annotations
        for (Annotation annotation : doc.getPages().get_Item(1).getAnnotations()) {
            // Filter TextMarkupAnnotation
            if (annotation.getAnnotationType() == AnnotationType.Highlight) {
                HighlightAnnotation highlightedAnnotation = (HighlightAnnotation) annotation;
                // Retrieve highlighted text fragments
                TextFragmentCollection collection = highlightedAnnotation.getMarkedTextFragments();
                for (TextFragment tf : collection) {
                    // Display highlighted text
                    System.out.println(tf.getText());
                }
            }
        }
    }
```

## Acceder a fragmentos de texto y elementos de segmento desde XML

A veces necesitamos acceder a elementos TextFragement o TextSegment al procesar documentos PDF generados a partir de XML. Aspose.PDF for Android via Java proporciona acceso a dichos elementos por nombre. El fragmento de código a continuación muestra cómo usar esta funcionalidad.

  public static void AccessTextFragmentAndSegmentElements() {
        String inXml = "40014.xml";
        Document doc = new Document();
        doc.bindXml(_dataDir + inXml);

        TextSegment segment = (TextSegment) doc.getObjectById("boldHtml");
        segment = (TextSegment) doc.getObjectById("strongHtml");

        System.out.println(segment.getText());
        
    }
```

