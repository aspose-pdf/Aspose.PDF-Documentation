---
title: Adicionando ações de Favoritos a um arquivo PDF existente
type: docs
weight: 20
url: /java/adding-bookmark-actions/
description: Esta seção explica como adicionar ações de Favoritos a um arquivo PDF existente com Aspose.PDF Facades.
lastmod: "2021-06-30"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

A classe [PdfContentEditor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfContentEditor) presente no pacote com.aspose.pdf.facades oferece flexibilidade para adicionar ações de Favoritos a um arquivo PDF. Você pode criar um link com as ações em série correspondentes para executar um item de menu no visualizador de PDF. Esta classe também fornece a funcionalidade de criar ações adicionais para eventos de documentos.

O exemplo de código a seguir demonstra como adicionar uma ação de Favorito a um documento PDF.

```java
// Carregar o documento PDF existente
PdfContentEditor pdfContentEditor = new PdfContentEditor();
pdfContentEditor.bindPdf("input.pdf");

// Adicionar ação de Favorito
pdfContentEditor.addBookmarkAction("Favorito 1", 1, "javascript:app.alert('Ação de Favorito!');");

// Salvar o documento PDF atualizado
pdfContentEditor.save("output.pdf");

 Se você clicar nesta aba, a ação desejada será executada. Com a ajuda de um Favorito, clicando nele, executamos a ação desejada. Em seguida, crie um [CreateBookmarkAction](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfContentEditor#createBookmarksAction-java.lang.String-java.awt.Color-boolean-boolean-java.lang.String-java.lang.String-java.lang.String-), defina os parâmetros do texto, cores, indique o nome do favorito e também indique o número da página. A última ação é feita com "GoTo", ela permite que você vá de qualquer lugar para a página que precisamos.

```java
public static void AddBookmarksAction()
        {
            var document = new Document(_dataDir + "Sample.pdf");
            PdfContentEditor editor = new PdfContentEditor(document);
            editor.createBookmarksAction("Bookmark 1", java.awt.Color.GREEN, true, false, "", "GoTo", "2");

            // Salva o PDF resultante no arquivo
            editor.save(_dataDir + "PdfContentEditorDemo_Bookmark.pdf");
        }
```