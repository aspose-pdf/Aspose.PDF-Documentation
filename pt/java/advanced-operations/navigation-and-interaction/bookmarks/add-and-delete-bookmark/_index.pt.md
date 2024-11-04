---
title: Adicionar e Excluir um Marcador 
linktitle: Adicionar e Excluir um Marcador
type: docs
weight: 10
url: /java/add-and-delete-bookmark/
description: Você pode adicionar um marcador a um documento PDF com Java. É possível excluir todos ou determinados marcadores de um documento PDF.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Adicionar um Marcador a um Documento PDF

Os marcadores são mantidos na coleção [OutlineItemCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf/OutlineItemCollection) do objeto Documento, que por sua vez está na coleção [OutlineCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf/OutlineCollection).

Para adicionar um marcador a um PDF:

1. Abra um documento PDF usando o objeto [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document).
1. Crie um marcador e defina suas propriedades.
1. Adicione a coleção [OutlineItemCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf/OutlineItemCollection) à coleção Outlines.

O seguinte trecho de código mostra como adicionar um marcador em um documento PDF.

```java
package com.aspose.pdf.examples;

import java.io.IOException;

import com.aspose.pdf.*;
import com.aspose.pdf.facades.Bookmark;
import com.aspose.pdf.facades.Bookmarks;
import com.aspose.pdf.facades.PdfBookmarkEditor;

public class ExampleBookmarks {

    private static String _dataDir = "/home/aspose/pdf-examples/Samples/Bookmarks/";

    private static String GetDataDir() {
        String os = System.getProperty("os.name");
        if (os.startsWith("Windows"))
            _dataDir = "C:\\Samples\\Bookmarks\\";
        return _dataDir;
    }

    public static void AddBookmarks() throws IOException {

        Document pdfDocument = new Document(GetDataDir() + "AddBookmark.pdf");

        // Criar um objeto de marcador
        OutlineItemCollection pdfOutline = new OutlineItemCollection(pdfDocument.getOutlines());
        pdfOutline.setTitle("Teste de Esboço");
        pdfOutline.setItalic(true);
        pdfOutline.setBold(true);

        // Definir o número da página de destino
        pdfOutline.setAction(new GoToAction(pdfDocument.getPages().get_Item(2)));

        // Adicionar um marcador na coleção de esboços do documento.
        pdfDocument.getOutlines().add(pdfOutline);

        // Salvar o documento atualizado
        pdfDocument.save(_dataDir + "AddBookmark_out.pdf");
    }
```


## Adicionar um Marcador Filho ao Documento PDF

Marcadores podem ser aninhados, indicando uma relação hierárquica com marcadores pai e filho. Este artigo explica como adicionar um marcador filho, ou seja, um marcador de segundo nível, a um PDF.

Para adicionar um marcador filho a um arquivo PDF, primeiro adicione um marcador pai:

1. Abra um documento.
1. Adicione um marcador à [OutlineItemCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf/OutlineItemCollection), definindo suas propriedades.
1. Adicione o OutlineItemCollection à coleção [OutlineCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf/OutlineCollection) do objeto Document.

O marcador filho é criado da mesma forma que o marcador pai, explicado acima, mas é adicionado à coleção de Outlines do marcador pai.

Os seguintes trechos de código mostram como adicionar um marcador filho a um documento PDF.

```java
    public static void AddChildBookmark() {
        // Abrir documento
        Document pdfDocument = new Document(GetDataDir() + "AddChildBookmark.pdf");

        // Criar um objeto de marcador pai
        OutlineItemCollection pdfOutline = new OutlineItemCollection(pdfDocument.getOutlines());
        pdfOutline.setTitle("Parent Outline");
        pdfOutline.setItalic(true);
        pdfOutline.setBold(true);

        // Criar um objeto de marcador filho
        OutlineItemCollection pdfChildOutline = new OutlineItemCollection(pdfDocument.getOutlines());
        pdfChildOutline.setTitle("Child Outline");
        pdfChildOutline.setItalic(true);
        pdfChildOutline.setBold(true);

        // Adicionar marcador filho na coleção do marcador pai
        pdfOutline.add(pdfChildOutline);
        // Adicionar marcador pai na coleção de outlines do documento.
        pdfDocument.getOutlines().add(pdfOutline);

        // Salvar saída
        pdfDocument.save(_dataDir + "AddChildBookmark_out.pdf");
    }
```


## Excluir todos os Marcadores de um Documento PDF

Todos os marcadores em um PDF são mantidos na coleção [OutlineCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf/OutlineCollection). Este artigo explica como excluir todos os marcadores de um arquivo PDF.

Para excluir todos os marcadores de um arquivo PDF:

1. Chame o método Delete da coleção [OutlineCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf/OutlineCollection).
1. Salve o arquivo modificado usando o método Save do objeto [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document).

Os seguintes trechos de código mostram como excluir todos os marcadores de um documento PDF.

```java
    public static void DeleteAllBookmarksFromPDFDocument() {
        // Abrir documento
        Document pdfDocument = new Document(GetDataDir() + "DeleteAllBookmarks.pdf");

        // Excluir todos os marcadores
        pdfDocument.getOutlines().delete();

        // Salvar arquivo atualizado
        pdfDocument.save(_dataDir + "DeleteAllBookmarks_out.pdf");
    }
```

## Excluir um Marcador Específico de um Documento PDF

[Excluir Todos os Anexos de um Documento PDF](https://docs.aspose.com/pdf/java/working-with-attachments/) mostrou como excluir todos os anexos de um arquivo PDF. Também é possível remover apenas anexos específicos.

Para excluir um marcador específico de um arquivo PDF:

1. Passe o título do marcador como parâmetro para o método [Delete](https://reference.aspose.com/pdf/java/com.aspose.pdf/OutlineCollection#delete--) da coleção [OutlineCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf/OutlineCollection).
2. Em seguida, salve o arquivo atualizado com o método Save do objeto Document.

A classe [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) fornece a coleção [OutlineCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf/OutlineCollection). O método [Delete](https://reference.aspose.com/pdf/java/com.aspose.pdf/OutlineCollection#delete--) remove qualquer marcador com o título passado para o método.

Os seguintes trechos de código mostram como excluir um marcador específico do documento PDF.

```java
    public static void DeleteParticularBookmarkPDFDocument() {
        // Abrir documento
        Document pdfDocument = new Document(GetDataDir() + "DeleteParticularBookmark.pdf");

        // Excluir contorno específico por Título
        pdfDocument.getOutlines().delete("Child Outline");

        // Salvar arquivo atualizado
        pdfDocument.save(_dataDir + "DeleteParticularBookmark_out.pdf");
    }
```