---
title: Extraindo texto bruto de arquivo PDF
linktitle: Extrair texto de PDF
type: docs
weight: 10
url: /pt/androidjava/extract-text-from-all-pdf/
description: Este artigo descreve várias maneiras de extrair texto de documentos PDF usando Aspose.PDF for Android via Java. De páginas inteiras, de uma parte específica, com base em colunas, etc.
lastmod: "2026-07-01"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Extrair Texto de Todas as Páginas de um Documento PDF

Extrair texto de um documento PDF é uma necessidade comum. Neste exemplo, você verá como o Aspose.PDF for Java permite extrair texto de todas as páginas de um documento PDF.
Para extrair texto de todas as páginas PDF:

1. Crie um objeto do [TextAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextAbsorber) classe.
1. Abra o PDF usando [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) classe e chame o [Aceitar](https://reference.aspose.com/pdf/java/com.aspose.pdf/PageCollection#accept-com.aspose.pdf.TextAbsorber-) método do [Pages](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page) coleção.
1. O [TextAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextAbsorber) a classe absorve o texto do documento e o retorna na **Text** propriedade.

O trecho de código a seguir mostra como extrair texto de todas as páginas do documento PDF.

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

## Extrair Texto Destacado de Documento PDF

Em vários cenários de extração de texto de um documento PDF, pode surgir a necessidade de extrair apenas o texto destacado do documento PDF. Para implementar essa funcionalidade, adicionamos os métodos TextMarkupAnnotation.GetMarkedText() e TextMarkupAnnotation.GetMarkedTextFragments() na API. Você pode extrair o texto destacado do documento PDF filtrando TextMarkupAnnotation e usando os métodos mencionados. O trecho de código a seguir mostra como extrair o texto destacado do documento PDF.

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

## Acessar TextFragment e Elementos de Segmento a partir de XML

Às vezes, precisamos acessar itens TextFragement ou TextSegment ao processar documentos PDF gerados a partir de XML. Aspose.PDF for Android via Java fornece acesso a esses itens por nome. O trecho de código abaixo mostra como usar essa funcionalidade.

  public static void AccessTextFragmentAndSegmentElements() {
        String inXml = "$014.xml";
        Document doc = new Document();
        doc.bindXml(_dataDir + inXml);

        TextSegment segment = (TextSegment) doc.getObjectById("boldHtml");
        segment = (TextSegment) doc.getObjectById("strongHtml");

        System.out.println(segment.getText());
        
    }
```

