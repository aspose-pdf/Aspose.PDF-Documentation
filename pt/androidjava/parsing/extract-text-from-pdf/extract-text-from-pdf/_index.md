---
title: Extraindo texto bruto de arquivo PDF 
linktitle: Extrair texto de PDF
type: docs
weight: 10
url: /pt/androidjava/extract-text-from-all-pdf/
description: Este artigo descreve várias maneiras de extrair texto de documentos PDF usando Aspose.PDF para Android via Java. De páginas inteiras, de uma parte específica, com base em colunas, etc.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Extrair Texto de Todas as Páginas de um Documento PDF

Extrair texto de um documento PDF é uma exigência comum. Neste exemplo, você verá como o Aspose.PDF para Java permite extrair texto de todas as páginas de um documento PDF.
Para extrair texto de todas as páginas do PDF:

1. Crie um objeto da classe [TextAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextAbsorber).

1. Abra o PDF usando a classe [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) e chame o método [Accept](https://reference.aspose.com/pdf/java/com.aspose.pdf/PageCollection#accept-com.aspose.pdf.TextAbsorber-) da coleção [Pages](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page).
1. A classe [TextAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextAbsorber) absorve o texto do documento e retorna na propriedade **Text**.

O seguinte trecho de código mostra como extrair texto de todas as páginas de um documento PDF.

```java
public static void ExtractFromAllPages() {
        // O caminho para o diretório dos documentos.

        String filePath = _dataDir + "ExtractTextAll.pdf";

        // Abrir documento
        Document pdfDocument = new com.aspose.pdf.Document(filePath);

        // Criar objeto TextAbsorber para extrair texto
        TextAbsorber textAbsorber = new com.aspose.pdf.TextAbsorber();

        // Aceitar o absorvedor para todas as páginas
        pdfDocument.getPages().accept(textAbsorber);

        // Obter o texto extraído
        String extractedText = textAbsorber.getText();
        try {
            java.io.FileWriter writer = new java.io.FileWriter(_dataDir + "extracted-text.txt", true);
            // Escrever uma linha de texto no arquivo
            writer.write(extractedText);
            // Fechar o fluxo
            writer.close();
        } catch (java.io.IOException e) {
            e.printStackTrace();
        }

    }
```


## Extrair Texto Destacado de Documento PDF

Em vários cenários de extração de texto de um documento PDF, pode haver um requisito de extrair apenas o texto destacado do documento PDF. Para implementar essa funcionalidade, adicionamos os métodos TextMarkupAnnotation.GetMarkedText() e TextMarkupAnnotation.GetMarkedTextFragments() na API. Você pode extrair texto destacado de um documento PDF filtrando TextMarkupAnnotation e usando os métodos mencionados. O snippet de código a seguir mostra como você pode extrair texto destacado de um documento PDF.

```java
public static void ExtractHighlightedText() {
        Document doc = new Document(_dataDir + "ExtractHighlightedText.pdf");
        // Percorrer todas as anotações
        for (Annotation annotation : doc.getPages().get_Item(1).getAnnotations()) {
            // Filtrar TextMarkupAnnotation
            if (annotation.getAnnotationType() == AnnotationType.Highlight) {
                HighlightAnnotation highlightedAnnotation = (HighlightAnnotation) annotation;
                // Recuperar fragmentos de texto destacados
                TextFragmentCollection collection = highlightedAnnotation.getMarkedTextFragments();
                for (TextFragment tf : collection) {
                    // Exibir texto destacado
                    System.out.println(tf.getText());
                }
            }
        }
    }
```


## Acessar Elementos de Fragmento de Texto e Segmento de XML

Às vezes, precisamos acessar itens TextFragement ou TextSegment ao processar documentos PDF gerados a partir de XML. O Aspose.PDF para Android via Java fornece acesso a esses itens pelo nome. O trecho de código abaixo mostra como usar essa funcionalidade.

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