---
title: Obter, Atualizar e Expandir um Marcador 
linktitle: Obter, Atualizar e Expandir um Marcador
type: docs
weight: 20
url: /pt/java/get-update-and-expand-bookmark/
description: Este artigo descreve como usar marcadores em um arquivo PDF. Com nossa biblioteca Java, você pode obter marcadores do arquivo PDF, obter o número da página de um marcador, atualizar marcadores em um Documento PDF e expandir marcadores ao visualizar um documento.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Obter Marcadores

A coleção [OutlineCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf/OutlineCollection) do objeto [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) contém todos os marcadores de um arquivo PDF. Este artigo explica como obter marcadores de um arquivo PDF e como obter em qual página um marcador específico está.

Para obter os marcadores, percorra a coleção [OutlineCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf/OutlineCollection) e obtenha cada marcador na OutlineItemCollection.
 The OutlineItemCollection fornece acesso a todos os atributos do marcador. O trecho de código a seguir mostra como obter marcadores do arquivo PDF.

```java
    public static void GettingBookmarks() {
        // Abrir documento
        Document pdfDocument = new Document(GetDataDir() + "UpdateBookmarks.pdf");
        // Percorrer todos os marcadores
        for (OutlineItemCollection outlineItem : (Iterable<OutlineItemCollection>) pdfDocument.getOutlines()) {
            System.out.println("Título :- " + outlineItem.getTitle());
            System.out.println("É Itálico :- " + outlineItem.getItalic());
            System.out.println("É Negrito :- " + outlineItem.getBold());
            System.out.println("Cor :- " + outlineItem.getColor());
        }
    }
```

## Obtendo o Número da Página de um Marcador

Uma vez que você tenha adicionado um marcador, você pode descobrir em qual página ele está obtendo o PageNumber de destino associado ao objeto Bookmark.

```java
    public static void GettingBookmarksPageNumber() {
        // Criar PdfBookmarkEditor
        PdfBookmarkEditor bookmarkEditor = new PdfBookmarkEditor();
        // Abrir arquivo PDF
        bookmarkEditor.bindPdf(GetDataDir() + "UpdateBookmarks.pdf");
        // Extrair marcadores
        Bookmarks bookmarks = bookmarkEditor.extractBookmarks();
        for (Bookmark bookmark : (Iterable<Bookmark>) bookmarks) {
            String strLevelSeprator = "";
            for (int i = 1; i < bookmark.getLevel(); i++) {
                strLevelSeprator += "---- ";
            }
            System.out.println("Título :- " + strLevelSeprator + bookmark.getTitle());
            System.out.println("Número da Página :- " + strLevelSeprator + bookmark.getPageNumber());
            System.out.println("Ação da Página :- " + strLevelSeprator + bookmark.getAction());
        }
    }
```

## Atualizar Favoritos em um Documento PDF

Para atualizar um favorito em um arquivo PDF, primeiro obtenha o favorito específico da coleção OutlineColletion do objeto Document especificando o índice do favorito. Uma vez que você tenha recuperado o favorito no objeto [OutlineItemCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf/OutlineCollection), você pode atualizar suas propriedades e então salvar o arquivo PDF atualizado usando o método Save. Os seguintes trechos de código mostram como atualizar favoritos em um documento PDF.

```java
    public static void UpdateBookmarksInPDFDocument() {
        // Abrir documento
        Document pdfDocument = new Document(GetDataDir() + "UpdateBookmarks.pdf");
        // Obter um objeto de favorito
        OutlineItemCollection pdfOutline = pdfDocument.getOutlines().get_Item(1);

        // Atualizar o objeto de favorito
        pdfOutline.setTitle("Outline Atualizado");
        pdfOutline.setItalic(true);
        pdfOutline.setBold(true);
        // Definir a página de destino como 2
        pdfOutline.setDestination(new GoToAction(pdfDocument.getPages().get_Item(2)));

        // Salvar saída
        pdfDocument.save(GetDataDir() + "Bookmarkupdated_output.pdf");
    }
```


## Atualizar Favoritos Filhos em um Documento PDF

Para atualizar um favorito filho:

1. Recupere o favorito filho que você deseja atualizar do arquivo PDF, primeiro obtendo o favorito pai e, em seguida, o favorito filho usando os valores de índice apropriados.
1. Salve o arquivo PDF atualizado usando o método Save.

{{% alert color="primary" %}}

Obtenha um favorito da coleção OutlineCollection do objeto Document especificando o índice do favorito e, em seguida, obtenha o favorito filho especificando o índice desse favorito pai.

{{% /alert %}}

O seguinte trecho de código mostra como atualizar favoritos filhos em um documento PDF.

```java
    public static void UpdateChildBookmarksInPDFDocument() {
        // Abrir documento
        Document pdfDocument = new Document(GetDataDir() + "UpdateBookmarks.pdf");
        // Obter um objeto de favorito
        OutlineItemCollection pdfOutline = pdfDocument.getOutlines().get_Item(1);
        // Obter objeto de favorito filho
        OutlineItemCollection childOutline = pdfOutline.get_Item(1);

        // Atualizar o objeto de favorito
        childOutline.setTitle("Updated Outline");
        childOutline.setItalic(true);
        childOutline.setBold(true);
        // Definir a página de destino como 2
        childOutline.setDestination(new GoToAction(pdfDocument.getPages().get_Item(2)));

        // Salvar saída
        pdfDocument.save(GetDataDir() + "Bookmarkupdated_output.pdf");
    }
```


## Favoritos Expandidos ao visualizar o documento

Os favoritos estão contidos na coleção [OutlineItemCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf/OutlineItemCollection) do objeto Documento, que por sua vez está na coleção [OutlineCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf/OutlineCollection). No entanto, podemos ter a necessidade de ter todos os favoritos expandidos ao visualizar o arquivo PDF.

Para cumprir esse requisito, podemos definir o status de abertura para cada item de contorno/favorito como Aberto. O seguinte trecho de código mostra como definir o status de abertura para cada favorito como expandido em um documento PDF.

```java
    public static void ExpandedBookmarks() {    
        Document doc = new Document(GetDataDir()+"UpdateBookmarks.pdf");
        // definir modo de visualização da página, ou seja, mostrar miniaturas, tela cheia, mostrar painel de anexos
        doc.setPageMode(PageMode.UseOutlines);
        // imprimir contagem total de Favoritos no arquivo PDF
        System.out.println(doc.getOutlines().size());
        // percorrer cada item de contorno na coleção de contornos do arquivo PDF
        for (int counter = 1; counter <= doc.getOutlines().size(); counter++) {
            // definir status de abertura para item de contorno
            doc.getOutlines().get_Item(counter).setOpen(true);
        }
        // salvar o arquivo PDF
        doc.save(_dataDir+"Bookmarks_Expanded.pdf");
    }
```