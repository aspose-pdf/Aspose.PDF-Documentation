---
title: Adicionando Anotações a um arquivo PDF existente
type: docs
weight: 80
url: pt/java/adding-annotations-to-existing-pdf-file/
description: Esta seção explica como adicionar Anotações a um arquivo PDF existente com Aspose.PDF Facades.
lastmod: "2021-06-30"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Adicionar Anotação de Texto Livre em um Arquivo PDF Existente (facades)

Uma anotação de texto livre exibe texto diretamente na página. [PdfContentEditor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfContentEditor) permite que você adicione anotações de diferentes tipos em um arquivo PDF existente. Você pode usar o método respectivo para adicionar uma anotação específica. Por exemplo, no trecho de código a seguir, usamos o método [createFreeText](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfContentEditor#createFreeText-java.awt.Rectangle-java.lang.String-int-) para adicionar uma anotação do tipo FreeText.

Qualquer tipo de anotações pode ser adicionado ao arquivo PDF da mesma forma.
 Primeiro, você precisa criar um objeto do tipo [PdfContentEditor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfContentEditor) e vincular o arquivo PDF de entrada usando o método bindPdf. Em segundo lugar, você deve criar um objeto Rectangle para especificar a área da anotação. Depois disso, você pode chamar o método [createFreeText](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfContentEditor#createFreeText-java.awt.Rectangle-java.lang.String-int-) para adicionar a anotação FreeText, o número da página na qual a anotação está localizada, e então usar o método save para salvar o arquivo PDF atualizado.

O snippet de código a seguir mostra como adicionar uma anotação de texto livre em um arquivo PDF.

```java
  public static void AddFreeTextAnnotation()
    {
        var document = new Document(_dataDir + "sample.pdf");
        PdfContentEditor editor = new PdfContentEditor(document);
        TextFragmentAbsorber tfa = new TextFragmentAbsorber("PDF");
        tfa.visit(document.getPages().get_Item(1));

        java.awt.Rectangle rect = new  java.awt.Rectangle();
        rect.x = (int)tfa.getTextFragments().get_Item(1).getRectangle().getLLX();
        rect.y = (int)tfa.getTextFragments().get_Item(1).getRectangle().getURY() + 5;
        rect.height = 18;
        rect.width = 100;        

        editor.createFreeText(rect, "Demonstração de Texto Livre", 1); // o último parâmetro é o número da página
        editor.save(_dataDir + "PdfContentEditorDemo_FreeTextAnnotation.pdf");
    }
```

## Adicionar Anotação de Texto em um Arquivo PDF Existente (facades)

Neste exemplo também, você precisa criar um objeto do tipo [PdfContentEditor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfContentEditor) e vincular o arquivo PDF de entrada usando o método [bindPdf](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfContentEditor#bindPdf-java.lang.String-). Em segundo lugar, você deve criar um objeto Rectangle para especificar a área da anotação. Depois disso, você pode chamar o método [createFreeText](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfContentEditor#createFreeText-java.awt.Rectangle-java.lang.String-int-) para adicionar a anotação de texto livre, criar o título das suas anotações e o número da página na qual a anotação está localizada.

```java
 public static void AddTextAnnotation()
    {
        var document = new Document(_dataDir + "sample.pdf");
        PdfContentEditor editor = new PdfContentEditor(document);
        TextFragmentAbsorber tfa = new TextFragmentAbsorber("PDF");
        tfa.visit(document.getPages().get_Item(1));

        java.awt.Rectangle rect = new  java.awt.Rectangle();
        rect.x = (int)tfa.getTextFragments().get_Item(1).getRectangle().getLLX();
        rect.y = (int)tfa.getTextFragments().get_Item(1).getRectangle().getURY() + 5;
        rect.height = 18;
        rect.width = 100;        

        editor.createText(rect, "Aspose User", "PDF é um formato melhor para documentos modernos", false, "Key", 1);
        editor.save(_dataDir + "PdfContentEditorDemo_TextAnnotation.pdf");
    }
```


## Adicionar Anotação de Linha em um Arquivo PDF Existente (facades)

Também especificamos o Retângulo, coordenadas do início e fim da linha, número da página, espessura, estilo e cor da moldura da anotação, tipo de traço da linha, tipo de início e fim da linha.

```java

    public static void AddLineAnnotation()
    {
        var document = new Document(_dataDir + "Appartments.pdf");
        PdfContentEditor editor = new PdfContentEditor(document);
        // Criar Anotação de Linha
        editor.createLine(
            new java.awt.Rectangle(550, 93, 562, 439),
            "Test",
            556, 99, 556, 443, 1, 1,
            java.awt.Color.RED,
            "dash",
            new int[] { 1, 0, 3 },
            new String[] { "Open", "Open" });
        editor.save(_dataDir + "PdfContentEditorDemo_LineAnnotation.pdf");
    }
```