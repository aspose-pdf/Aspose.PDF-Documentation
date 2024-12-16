---
title: Rotacionar Texto Dentro de PDF 
linktitle: Rotacionar Texto Dentro de PDF
type: docs
weight: 50
url: /pt/java/rotate-text-inside-pdf/
description: Aprenda diferentes maneiras de rotacionar texto em PDF. O Aspose.PDF permite que você rotacione texto em qualquer ângulo, roteie fragmentos de texto ou um parágrafo inteiro.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Rotacionar Texto Dentro de PDF usando a Propriedade Rotation

Usando o método [setRotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextFragmentState#setRotation-double-) da Classe [TextFragment](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextFragment), você pode rotacionar texto em vários ângulos. A rotação de texto pode ser usada em diferentes cenários de geração de documentos. Você pode especificar o ângulo de rotação em graus para rotacionar o texto conforme sua necessidade. Por favor, verifique os diferentes cenários a seguir, nos quais você pode implementar a rotação de texto.

## Implementar Rotação usando TextFragment e TextBuilder

```java
public class ExampleRotateText {
    private static String _dataDir = "/home/admin1/pdf-examples/Samples/";

    public static void ImplementRotationUsingTextFragmentAndTextBuilder() {

        // Inicializar objeto de documento
        Document pdfDocument = new Document();
        // Obter página específica
        Page pdfPage = pdfDocument.getPages().add();
        // Criar fragmento de texto
        TextFragment textFragment1 = new TextFragment("texto principal");
        textFragment1.setPosition(new Position(100, 600));

        // Definir propriedades do texto
        textFragment1.getTextState().setFontSize(12);
        textFragment1.getTextState().setFont(FontRepository.findFont("TimesNewRoman"));

        // Criar fragmento de texto rotacionado
        TextFragment textFragment2 = new TextFragment("texto rotacionado");
        textFragment2.setPosition(new Position(200, 600));
        // Definir propriedades do texto
        textFragment2.getTextState().setFontSize(12);
        textFragment2.getTextState().setFont(FontRepository.findFont("TimesNewRoman"));
        textFragment2.getTextState().setRotation(45);

        // Criar fragmento de texto rotacionado
        TextFragment textFragment3 = new TextFragment("texto rotacionado");
        textFragment3.setPosition(new Position(300, 600));

        // Definir propriedades do texto
        textFragment3.getTextState().setFontSize(12);
        textFragment3.getTextState().setFont(FontRepository.findFont("TimesNewRoman"));
        textFragment3.getTextState().setRotation(90);

        // criar objeto TextBuilder
        TextBuilder textBuilder = new TextBuilder(pdfPage);
        // Anexar o fragmento de texto à página PDF
        textBuilder.appendText(textFragment1);
        textBuilder.appendText(textFragment2);
        textBuilder.appendText(textFragment3);

        // Salvar documento
        pdfDocument.save(_dataDir + "TextFragmentTests_Rotated1_out.pdf");
    }
}
```


## Implementar Rotação usando TextParagraph e TextBuilder (Fragmentos Rotacionados)

```java
public static void ImplementRotationUsingTextParagraphAndTextBuilder_RotatedFragments() {

    // Inicializar objeto de documento
    Document pdfDocument = new Document();
    // Obter página específica
    Page pdfPage = (Page) pdfDocument.getPages().add();
    TextParagraph paragraph = new TextParagraph();
    paragraph.setPosition(new Position(200, 600));
    // Criar fragmento de texto
    TextFragment textFragment1 = new TextFragment("texto rotacionado");
    // Definir propriedades do texto
    textFragment1.getTextState().setFontSize(12);
    textFragment1.getTextState().setFont(FontRepository.findFont("TimesNewRoman"));
    // Definir rotação
    textFragment1.getTextState().setRotation(45);

    // Criar fragmento de texto
    TextFragment textFragment2 = new TextFragment("texto principal");
    // Definir propriedades do texto
    textFragment2.getTextState().setFontSize(12);
    textFragment2.getTextState().setFont(FontRepository.findFont("TimesNewRoman"));

    // Criar fragmento de texto
    TextFragment textFragment3 = new TextFragment("outro texto rotacionado");
    // Definir propriedades do texto
    textFragment3.getTextState().setFontSize(12);
    textFragment3.getTextState().setFont(FontRepository.findFont("TimesNewRoman"));
    // Definir rotação
    textFragment3.getTextState().setRotation(-45);

    // Adicionar os fragmentos de texto ao parágrafo
    paragraph.appendLine(textFragment1);
    paragraph.appendLine(textFragment2);
    paragraph.appendLine(textFragment3);
    // Criar objeto TextBuilder
    TextBuilder textBuilder = new TextBuilder(pdfPage);
    // Adicionar o parágrafo de texto à página PDF
    textBuilder.appendParagraph(paragraph);
    // Salvar documento
    pdfDocument.save(_dataDir + "TextFragmentTests_Rotated2_out.pdf");
}
```


## Implementar Rotação usando TextFragment e Page.Paragraphs

```csharp
public static void ImplementRotationUsingTextFragmentAndPageParagraphs() {
    // Inicializar objeto do documento
    Document pdfDocument = new Document();
    // Obter página específica
    Page pdfPage = (Page) pdfDocument.getPages().add();
    // Criar fragmento de texto
    TextFragment textFragment1 = new TextFragment("texto principal");
    // Definir propriedades do texto
    textFragment1.getTextState().setFontSize(12);
    textFragment1.getTextState().setFont(FontRepository.findFont("TimesNewRoman"));

    // Criar fragmento de texto
    TextFragment textFragment2 = new TextFragment("texto rotacionado");

    // Definir propriedades do texto
    textFragment2.getTextState().setFontSize(12);
    textFragment2.getTextState().setFont(FontRepository.findFont("TimesNewRoman"));

    // Definir rotação
    textFragment2.getTextState().setRotation(315);

    // Criar fragmento de texto
    TextFragment textFragment3 = new TextFragment("texto rotacionado");
    // Definir propriedades do texto
    textFragment3.getTextState().setFontSize(12);
    textFragment3.getTextState().setFont(FontRepository.findFont("TimesNewRoman"));

    // Definir rotação
    textFragment3.getTextState().setRotation(270);
    pdfPage.getParagraphs().add(textFragment1);
    pdfPage.getParagraphs().add(textFragment2);
    pdfPage.getParagraphs().add(textFragment3);

    // Salvar documento
    pdfDocument.save(_dataDir + "TextFragmentTests_Rotated3_out.pdf");
    }
```


## Implementar Rotação usando TextParagraph e TextBuilder (Parágrafo Inteiro Rotacionado)

```java
public static void ImplementRotationUsingTextParagraphAndTextBuilder() {

    // Inicializar objeto de documento
    Document pdfDocument = new Document();
    // Obter página específica
    Page pdfPage = pdfDocument.getPages().add();
    for (int i = 0; i < 4; i++) {
        TextParagraph paragraph = new TextParagraph();
        paragraph.setPosition(new Position(200, 600));
        // Especificar rotação
        paragraph.setRotation(i * 90 + 45);
        // Criar fragmento de texto
        TextFragment textFragment1 = new TextFragment("Texto do Parágrafo");
        // Criar fragmento de texto
        textFragment1.getTextState().setFontSize(12);
        textFragment1.getTextState().setFont(FontRepository.findFont("TimesNewRoman"));
        textFragment1.getTextState().setBackgroundColor(Color.getLightGray());
        textFragment1.getTextState().setForegroundColor(Color.getBlue());

        // Criar fragmento de texto
        TextFragment textFragment2 = new TextFragment("Segunda linha de texto");
        // Definir propriedades de texto
        textFragment2.getTextState().setFontSize(12);
        textFragment2.getTextState().setFont(FontRepository.findFont("TimesNewRoman"));
        textFragment2.getTextState().setBackgroundColor(Color.getLightGray());
        textFragment2.getTextState().setForegroundColor(Color.getBlue());

        // Criar fragmento de texto
        TextFragment textFragment3 = new TextFragment("E mais um pouco de texto...");
        // Definir propriedades de texto
        textFragment3.getTextState().setFontSize(12);
        textFragment3.getTextState().setFont(FontRepository.findFont("TimesNewRoman"));
        textFragment3.getTextState().setBackgroundColor(Color.getLightGray());
        textFragment3.getTextState().setForegroundColor(Color.getBlue());
        textFragment3.getTextState().setUnderline(true);

        paragraph.appendLine(textFragment1);
        paragraph.appendLine(textFragment2);
        paragraph.appendLine(textFragment3);
        // Criar objeto TextBuilder
        TextBuilder textBuilder = new TextBuilder(pdfPage);
        // Adicionar o fragmento de texto à página PDF
        textBuilder.appendParagraph(paragraph);
    }
    // Salvar documento
    pdfDocument.save(_dataDir + "TextFragmentTests_Rotated4_out.pdf");
}
```