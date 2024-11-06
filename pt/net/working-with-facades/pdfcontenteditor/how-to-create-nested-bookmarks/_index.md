---
title: Adicionando Marcadores ao Arquivo PDF
type: docs
weight: 20
url: pt/net/how-to-create-nested-bookmarks/
description: Esta seção explica como criar Marcadores Aninhados com a Classe PdfContentEditor.
lastmod: "2021-06-05"
draft: false
---

Os marcadores oferecem a opção de acompanhar/ligar a uma página específica dentro do documento PDF. A classe [PdfContentEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/PdfContentEditor) no [namespace Aspose.Pdf.Facades](https://docs-qa.aspose.com/display/pdftemp/Aspose.Pdf.Facades+namespace) fornece um recurso que permite criar seu próprio marcador de uma maneira sofisticada e intuitiva dentro de um arquivo PDF existente, em uma página específica ou em todas as páginas.

## Detalhes da implementação

Além da criação de marcadores simples, às vezes você tem o requisito de criar um marcador na forma de capítulos onde você aninha os marcadores individuais dentro dos marcadores de capítulo, de modo que, quando clicar no sinal de + para um capítulo, você veria as páginas dentro quando os marcadores se expandem, como mostrado na imagem abaixo.
```csharp
   public static void AddBookmarksAction()
        {
            var document = new Document(_dataDir + "Sample.pdf");
            PdfContentEditor editor = new PdfContentEditor(document);
            editor.CreateBookmarksAction("Marcador 1", System.Drawing.Color.Green, true, false, string.Empty, "GoTo", "2");

            // Salva o PDF resultante no arquivo
            editor.Save(_dataDir + "PdfContentEditorDemo_Bookmark.pdf");
        }
```