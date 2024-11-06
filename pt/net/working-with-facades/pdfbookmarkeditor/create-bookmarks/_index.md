---
title: Criar Marcadores
type: docs
weight: 10
url: pt/net/create-bookmarks/
description: Esta seção explica como criar marcadores em seu arquivo PDF com Aspose.PDF Facades usando a classe PdfBookmarEditor.
lastmod: "2021-06-05"
draft: false
---

## Criar Marcadores de Todas as Páginas

Para criar marcadores de todas as páginas, você precisa usar o método [CreateBookmarks](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdfbookmarkeditor/createbookmarks/methods/2) sem nenhum parâmetro. A classe [PdfBookmarkEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfbookmarkeditor) permite que você crie marcadores de todas as páginas de um arquivo PDF. Primeiro, você precisa criar um objeto da classe [PdfBookmarkEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfbookmarkeditor) e vincular o PDF de entrada usando o método [BindPdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades.facade/bindpdf/methods/3). Em seguida, você deve chamar o método [CreateBookmarks](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdfbookmarkeditor/createbookmarks/methods/2) e salvar o arquivo PDF de saída usando o método [Save](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/save). O trecho de código a seguir mostra como criar marcadores.

{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-Bookmarks-CreateBookmarksAll-CreateBookmarksAll.cs" >}}

## Criar Marcadores de Todas as Páginas com Propriedades

A classe [PdfBookmarkEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfbookmarkeditor) permite que você crie marcadores de todas as páginas de um arquivo PDF e especifique as propriedades (Cor, Negrito, Itálico). Você pode fazer isso com a ajuda do método [CreateBookmarks](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdfbookmarkeditor/createbookmarks/methods/2). Primeiro, você precisa criar um objeto da classe [PdfBookmarkEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfbookmarkeditor) e vincular o PDF de entrada usando o método [BindPdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades.facade/bindpdf/methods/3). Em seguida, você deve chamar o método [CreateBookmarks](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdfbookmarkeditor/createbookmarks/methods/2) e salvar o arquivo PDF de saída usando o método [Save](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/save). O trecho de código a seguir mostra como criar marcadores de todas as páginas com propriedades.

{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-Bookmarks-CreateBookmarksPagesProperties-CreateBookmarksPagesProperties.cs" >}}

## Criar Marcador de uma Página Específica

Você pode criar um marcador de uma página específica em um arquivo PDF existente usando o método [CreateBookmarkOfPage](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdfbookmarkeditor/createbookmarkofpage/methods/1). Este método leva dois argumentos: título do marcador e número da página. Primeiro, você precisa criar um objeto da classe [PdfBookmarkEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfbookmarkeditor) e vincular o arquivo PDF de entrada usando o método [BindPdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades.facade/bindpdf/methods/3). Em seguida, você deve chamar o método [CreateBookmarkOfPage](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdfbookmarkeditor/createbookmarkofpage/methods/1) e salvar o arquivo PDF de saída usando o método [Save](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/save). O trecho de código a seguir mostra como criar um marcador de uma página específica.

{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-Bookmarks-CreateBookmarkPage-CreateBookmarkPage.cs" >}}

## Criar Marcadores de um Intervalo de Páginas

A classe [PdfBookmarkEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfbookmarkeditor) permite criar marcadores de um intervalo de páginas. Você pode usar o método [CreateBookmarkOfPage](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdfbookmarkeditor/createbookmarkofpage/methods/1) com dois parâmetros: lista de marcadores (a lista dos títulos dos marcadores) e lista de páginas (a lista das páginas a serem marcadas). Primeiro, você precisa criar um objeto da classe [PdfBookmarkEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfbookmarkeditor) e vincular o arquivo PDF de entrada usando o método [BindPdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades.facade/bindpdf/methods/3). Em seguida, você deve chamar o método [CreateBookmarkOfPage](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdfbookmarkeditor/createbookmarkofpage/methods/1) e salvar o PDF de saída usando o método [Save](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/save). O trecho de código a seguir mostra como criar marcadores de um intervalo de páginas.




{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-Bookmarks-CreateBookmarkPageRange-CreateBookmarkPageRange.cs" >}}
## Adicionar Marcador em um Arquivo PDF Existente

Você pode adicionar um marcador em um arquivo PDF existente usando a classe [PdfBookmarkEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfbookmarkeditor). Para criar o marcador, você precisa criar um objeto [Bookmark](https://reference.aspose.com/pdf/net/aspose.pdf.facades/bookmark) e definir os atributos necessários do marcador. Depois disso, você precisa passar o objeto [Bookmark](https://reference.aspose.com/pdf/net/aspose.pdf.facades/bookmark) para o método [CreateBookmarks](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdfbookmarkeditor/createbookmarks/methods/2) da classe [PdfBookmarkEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfbookmarkeditor). Finalmente, você precisa salvar o arquivo PDF atualizado usando o método [Save](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/save). O trecho de código a seguir mostra como adicionar o marcador em um arquivo PDF existente.




{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-Bookmarks-AddBookmark-AddBookmark.cs" >}}

## Adicionar Marcador Filho em um Arquivo PDF Existente

Você pode adicionar marcadores filhos em um arquivo PDF existente usando a classe [PdfBookmarkEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfbookmarkeditor). In order to add child bookmarks, you need to create [Bookmark](https://reference.aspose.com/pdf/net/aspose.pdf.facades/bookmark) objects.

Para adicionar subfavoritos, você precisa criar objetos [Bookmark](https://reference.aspose.com/pdf/net/aspose.pdf.facades/bookmark). Você pode adicionar objetos individuais de [Bookmark](https://reference.aspose.com/pdf/net/aspose.pdf.facades/bookmark) no objeto [Bookmarks](https://reference.aspose.com/pdf/net/aspose.pdf.facades/bookmarks). Você também precisa criar um objeto [Bookmark](https://reference.aspose.com/pdf/net/aspose.pdf.facades/bookmark) e definir sua propriedade [ChildItem](https://reference.aspose.com/pdf/net/aspose.pdf.facades/bookmark/properties/childitem) para o objeto [Bookmarks](https://reference.aspose.com/pdf/net/aspose.pdf.facades/bookmarks). Em seguida, você precisa passar este objeto [Bookmark](https://reference.aspose.com/pdf/net/aspose.pdf.facades/bookmark) com [ChildItem](https://reference.aspose.com/pdf/net/aspose.pdf.facades/bookmark/properties/childitem) para o método [CreateBookmarks](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdfbookmarkeditor/createbookmarks/methods/2). Finalmente, você precisa salvar o PDF atualizado usando o método [Save](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/save) da classe [PdfBookmarkEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfbookmarkeditor). O trecho de código a seguir mostra como adicionar marcadores filhos em um arquivo PDF existente.




{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-Bookmarks-AddChildBookmark-AddChildBookmark.cs" >}}
## Veja também

Tente comparar e encontrar uma maneira de trabalhar com favoritos que seja adequada para você. Vamos aprender a seção [Trabalhando com Favoritos em PDF](/pdf/net/bookmarks/).