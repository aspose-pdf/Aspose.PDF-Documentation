---
title: Adding Javascript actions to existing PDF file
type: docs
weight: 10
url: /java/adding-javascript-actions/
description: Esta seção explica como adicionar ações Javascript a um arquivo PDF existente com Aspose.PDF Facades.
lastmod: "2021-06-30"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

A classe [PdfContentEditor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfContentEditor) presente no pacote com.aspose.pdf.facades fornece a flexibilidade para adicionar ações Javascript a um arquivo PDF. Você pode criar um link com as ações em série correspondentes para executar um item de menu no visualizador de PDF. Esta classe também oferece o recurso de criar ações adicionais para eventos de documentos.

Primeiramente, um objeto é desenhado no [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document), em nosso exemplo um [Rectangle](https://reference.aspose.com/pdf/java/com.aspose.pdf/Rectangle).
 E defina a ação [createJavaScriptLink](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfContentEditor#createJavaScriptLink-java.lang.String-java.awt.Rectangle-int-java.awt.Color-) para o Retângulo. Depois, você pode salvar seu documento.

```java
 public static void AddingJavascriptActions() {
        PdfContentEditor editor = new PdfContentEditor();
        editor.bindPdf(_dataDir+"sample.pdf");
        // criar link de Javascript
        java.awt.Rectangle rect = new java.awt.Rectangle(50, 750, 50, 50);
        String code = "app.alert('Bem-vindo ao Aspose!');";
        editor.createJavaScriptLink(code, rect, 1, java.awt.Color.GREEN);
        // salvar o arquivo de saída
        editor.save(_dataDir+"JavaScriptAdded_output.pdf");
    }
```