---
title: Adicionando ações Javascript PDF
type: docs
weight: 10
url: /pt/net/adding-javascript-actions/
description: Esta seção explica como adicionar ações Javascript a um arquivo PDF existente com Aspose.PDF Facades.
lastmod: "2021-06-30"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

A classe [PdfContentEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/PdfContentEditor) presente no pacote Aspose.Pdf.Facades fornece a flexibilidade para adicionar ações Javascript a um arquivo PDF. Você pode criar um link com as ações em série correspondentes para executar um item de menu no visualizador de PDF. Esta classe também fornece a funcionalidade para criar ações adicionais para eventos de documento.

Primeiramente, um objeto é desenhado no [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document), em nosso exemplo um [Rectangle](https://reference.aspose.com/pdf/net/aspose.pdf.drawing/rectangle). E defina a ação [createJavaScriptLink](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor/methods/createjavascriptlink) para o Retângulo. Depois você pode salvar seu documento.

```csharp
  public static void AddingJavascriptActions()
        {
            PdfContentEditor editor = new PdfContentEditor();
            editor.BindPdf(_dataDir + "sample.pdf");
            // criar link de Javascript
            System.Drawing.Rectangle rect = new System.Drawing.Rectangle(50, 750, 50, 50);
            String code = "app.alert('Bem-vindo ao Aspose!');";
            editor.CreateJavaScriptLink(code, rect, 1, System.Drawing.Color.Green);
            // salvar o arquivo de saída
            editor.Save(_dataDir + "JavaScriptAdded_output.pdf");
        }
```