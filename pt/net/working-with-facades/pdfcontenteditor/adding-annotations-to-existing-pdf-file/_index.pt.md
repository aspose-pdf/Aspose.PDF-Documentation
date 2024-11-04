---
title: Adicionando Anotações a um arquivo PDF existente
type: docs
weight: 80
url: /net/adding-annotations-to-existing-pdf-file/
description: Esta seção explica como adicionar Anotações a um arquivo PDF existente com Aspose.PDF Facades.
lastmod: "2021-06-30"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Adicionar Anotação de Texto Livre em um Arquivo PDF Existente (facades)

[PdfContentEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor) permite que você adicione anotações de diferentes tipos em um arquivo PDF existente. Você pode usar o método respectivo para adicionar uma anotação específica. Por exemplo, no trecho de código a seguir, usamos o método [CreateFreeText](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor/methods/createfreetext) para adicionar uma anotação do tipo [FreeText](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/freetextannotation).

Qualquer tipo de anotações pode ser adicionado ao arquivo PDF da mesma forma. Primeiro, você precisa criar um objeto do tipo [PdfContentEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor) e vincular o arquivo PDF de entrada usando o método [BindPdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades.facade/bindpdf/methods/3). Em segundo lugar, você deve criar um objeto Rectangle para especificar a área da anotação.

Depois disso, você pode chamar o método [CreateFreeText](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor/methods/createfreetext) para adicionar a anotação [FreeText](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/freetextannotation), e então usar o método [Save](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/save) para salvar o arquivo PDF atualizado.

O trecho de código a seguir mostra como adicionar uma anotação de texto livre em um arquivo PDF.

```csharp
  public static void AddFreeTextAnnotation()
        {
            var document = new Document(_dataDir + "sample.pdf");
            PdfContentEditor editor = new PdfContentEditor(document);
            TextFragmentAbsorber tfa = new TextFragmentAbsorber("PDF");
            tfa.Visit(document.Pages[1]);

            var rect = new System.Drawing.Rectangle
            {
                X = (int)tfa.TextFragments[1].Rectangle.LLX,
                Y = (int)tfa.TextFragments[1].Rectangle.URY + 5,
                Height = 18,
                Width = 100
            };

            editor.CreateFreeText(rect, "Free Text Demo", 1); // último parâmetro é o número da página
            editor.Save(_dataDir + "PdfContentEditorDemo_FreeTextAnnotation.pdf");
        }
```
## Adicionar Anotação de Texto em um Arquivo PDF Existente (facades)

Neste exemplo também, você precisa criar um objeto do tipo [PdfContentEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor) e vincular o arquivo PDF de entrada usando o método [BindPdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades.facade/bindpdf/methods/3). Em segundo lugar, você deve criar um objeto Rectangle para especificar a área da anotação. Depois disso, você pode chamar o método [CreateFreeText](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor/methods/createfreetext) para adicionar anotação FreeText, criar o título de suas anotações e o número da página onde a anotação está localizada.

```csharp
 public static void AddTextAnnotation()
        {
            var document = new Document(_dataDir + "sample.pdf");
            PdfContentEditor editor = new PdfContentEditor(document);
            TextFragmentAbsorber tfa = new TextFragmentAbsorber("PDF");
            tfa.Visit(document.Pages[1]);

            var rect = new System.Drawing.Rectangle
            {
                X = (int)tfa.TextFragments[1].Rectangle.LLX,
                Y = (int)tfa.TextFragments[1].Rectangle.URY + 5,
                Height = 18,
                Width = 100
            };

            editor.CreateText(rect, "Aspose User", "PDF é um formato melhor para documentos modernos", false, "Key", 1);
            editor.Save(_dataDir + "PdfContentEditorDemo_TextAnnotation.pdf");
        }
```

## Adicionar Anotação de Linha em um Arquivo PDF Existente (fachadas)

Também especificamos o Retângulo, as coordenadas do início e fim da linha, o número da página, a espessura, o estilo e a cor da moldura da anotação, o tipo de traço da linha, o tipo de início e fim da linha.

```csharp
  public static void AddLineAnnotation()
        {
            var document = new Document(_dataDir + "Appartments.pdf");
            PdfContentEditor editor = new PdfContentEditor(document);
            // Create Line Annotation
            editor.CreateLine(
                new System.Drawing.Rectangle(550, 93, 562, 439),
                "Test",
                556, 99, 556, 443, 1, 2,
                System.Drawing.Color.Red,
                "dash",
                new int[] { 1, 0, 3 },
                new[] { "Open", "Open" });
            editor.Save(_dataDir + "PdfContentEditorDemo_LineAnnotation.pdf");
        }
```