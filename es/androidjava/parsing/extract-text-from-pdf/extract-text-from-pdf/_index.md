---
title: Extracción de texto sin formato de un archivo PDF
linktitle: Extraer texto de PDF
type: docs
weight: 10
url: /es/androidjava/extract-text-from-all-pdf/
description: Este artículo describe varias formas de extraer texto de documentos PDF utilizando Aspose.PDF para Android a través de Java. De páginas enteras, de una parte específica, basado en columnas, etc.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Extraer texto de todas las páginas de un documento PDF

La extracción de texto de un documento PDF es un requisito común. En este ejemplo, verás cómo Aspose.PDF para Java permite extraer texto de todas las páginas de un documento PDF.
Para extraer texto de todas las páginas del PDF:

1. Crea un objeto de la clase [TextAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextAbsorber).

1. Abra el PDF usando la clase [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) y llame al método [Accept](https://reference.aspose.com/pdf/java/com.aspose.pdf/PageCollection#accept-com.aspose.pdf.TextAbsorber-) de la colección [Pages](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page).
1. La clase [TextAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextAbsorber) absorbe el texto del documento y lo devuelve en la propiedad **Text**.

El siguiente fragmento de código muestra cómo extraer texto de todas las páginas de un documento PDF.

```java
public static void ExtractFromAllPages() {
        // La ruta al directorio de documentos.

        String filePath = _dataDir + "ExtractTextAll.pdf";

        // Abrir documento
        Document pdfDocument = new com.aspose.pdf.Document(filePath);

        // Crear objeto TextAbsorber para extraer texto
        TextAbsorber textAbsorber = new com.aspose.pdf.TextAbsorber();

        // Aceptar el absorbedor para todas las páginas
        pdfDocument.getPages().accept(textAbsorber);

        // Obtener el texto extraído
        String extractedText = textAbsorber.getText();
        try {
            java.io.FileWriter writer = new java.io.FileWriter(_dataDir + "extracted-text.txt", true);
            // Escribir una línea de texto en el archivo
            writer.write(extractedText);
            // Cerrar el flujo
            writer.close();
        } catch (java.io.IOException e) {
            e.printStackTrace();
        }

    }
```


## Extraer Texto Resaltado de un Documento PDF

En varios escenarios de extracción de texto de un documento PDF, puedes encontrarte con el requisito de extraer solo el texto resaltado del documento PDF. Para implementar la funcionalidad, hemos añadido los métodos TextMarkupAnnotation.GetMarkedText() y TextMarkupAnnotation.GetMarkedTextFragments() en la API. Puedes extraer texto resaltado de un documento PDF filtrando TextMarkupAnnotation y usando los métodos mencionados. El siguiente fragmento de código muestra cómo puedes extraer texto resaltado de un documento PDF.

```java
public static void ExtractHighlightedText() {
        Document doc = new Document(_dataDir + "ExtractHighlightedText.pdf");
        // Recorre todas las anotaciones
        for (Annotation annotation : doc.getPages().get_Item(1).getAnnotations()) {
            // Filtrar TextMarkupAnnotation
            if (annotation.getAnnotationType() == AnnotationType.Highlight) {
                HighlightAnnotation highlightedAnnotation = (HighlightAnnotation) annotation;
                // Recuperar fragmentos de texto resaltado
                TextFragmentCollection collection = highlightedAnnotation.getMarkedTextFragments();
                for (TextFragment tf : collection) {
                    // Mostrar texto resaltado
                    System.out.println(tf.getText());
                }
            }
        }
    }
```


## Acceder a Fragmentos de Texto y Elementos de Segmento desde XML

A veces necesitamos acceder a elementos TextFragment o TextSegment al procesar documentos PDF generados a partir de XML. Aspose.PDF para Android vía Java proporciona acceso a tales elementos por nombre. El fragmento de código a continuación muestra cómo usar esta funcionalidad.

```java
  public static void AccessTextFragmentAndSegmentElements() {
        String inXml = "40014.xml";
        Document doc = new Document();
        doc.bindXml(_dataDir + inXml);

        TextSegment segment = (TextSegment) doc.getObjectById("boldHtml");
        segment = (TextSegment) doc.getObjectById("strongHtml");

        System.out.println(segment.getText());
        
    }
```