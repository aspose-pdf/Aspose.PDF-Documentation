---
title: Atualizar, Excluir e Obter Favoritos
type: docs
weight: 30
url: /net/update-delete-and-get-bookmarks/
description: Esta seção explica como atualizar, excluir e obter Favoritos com Aspose.PDF Facades.
lastmod: "2021-06-05"
draft: false
---

## Atualizar um Favorito Existente no Arquivo PDF

Para atualizar um favorito existente em um arquivo PDF, você precisa usar o método [ModifyBookmarks](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfbookmarkeditor/methods/modifybookmarks). Este método aceita dois argumentos: título de origem (o título do marcador a ser modificado), título de destino (o título a ser substituído). Você precisa criar um objeto da classe [PdfBookmarkEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfbookmarkeditor) e vincular o arquivo PDF de entrada usando o método [BindPdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades.facade/bindpdf/methods/3). Depois disso, você precisa chamar o método [ModifyBookmarks](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfbookmarkeditor/methods/modifybookmarks), e então salvar o PDF atualizado usando o método [Save](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/save). O trecho de código a seguir mostra como modificar um marcador existente em um arquivo PDF.

{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-Bookmarks-UpdateBookmark-UpdateBookmark.cs" >}}

## Excluir Todos os Marcadores do Arquivo PDF

Você pode excluir todos os marcadores do arquivo PDF usando o método [DeleteBookmarks](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfbookmarkeditor/methods/deletebookmarks) sem nenhum parâmetro. Primeiro, você precisa criar um objeto da classe [PdfBookmarkEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfbookmarkeditor) e vincular o arquivo PDF de entrada usando o método [BindPdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades.facade/bindpdf/methods/3). Depois disso, você precisa chamar o método [DeleteBookmarks](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfbookmarkeditor/methods/deletebookmarks) e, em seguida, salvar o arquivo PDF atualizado usando o método [Save](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/save). O trecho de código a seguir mostra como deletar todos os marcadores do arquivo PDF.

{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-Bookmarks-DeleteAllBookmarks-DeleteAllBookmarks.cs" >}}

## Deletar um Marcador Específico de um Arquivo PDF

Para deletar um marcador específico, você precisa chamar o método [DeleteBookmarks](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfbookmarkeditor/methods/deletebookmarks) com um parâmetro string (título). O *título* aqui representa o marcador a ser excluído do PDF. Crie um objeto da classe [PdfBookmarkEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfbookmarkeditor) e vincule o arquivo PDF de entrada usando o método [BindPdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades.facade/bindpdf/methods/3). Depois disso, chame o método [DeleteBookmarks](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfbookmarkeditor/methods/deletebookmarks) e, em seguida, salve o arquivo PDF atualizado usando o método [Save](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/save). O trecho de código a seguir mostra como excluir um marcador específico de um arquivo PDF.

{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-Bookmarks-DeleteABookmark-DeleteABookmark.cs" >}}

## Obter Marcadores do Documento PDF Facades

A classe [PdfBookmarkEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfbookmarkeditor) fornece o recurso para manipular marcadores em um arquivo PDF existente. Ele fornece várias propriedades para obter/definir informações sobre os marcadores. O trecho de código a seguir mostra como obter informações relacionadas a cada marcador em um arquivo PDF.

## Extrair Marcadores de um Arquivo PDF Existente

O método [ExtractBookmarks](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdfbookmarkeditor/extractbookmarks/methods/3) permite extrair marcadores de um arquivo PDF. In order to extract the bookmarks, you need to create [PdfBookmarkEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfbookmarkeditor) object and bind the PDF file using [BindPdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades.facade/bindpdf/methods/3) method.

Para extrair os favoritos, você precisa criar o objeto [PdfBookmarkEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfbookmarkeditor) e vincular o arquivo PDF usando o método [BindPdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades.facade/bindpdf/methods/3). Depois disso, você precisa chamar o método [ExtractBookmarks](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdfbookmarkeditor/extractbookmarks/methods/3). O método [ExtractBookmarks](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdfbookmarkeditor/extractbookmarks/methods/3) retorna o objeto [Bookmarks](https://reference.aspose.com/pdf/net/aspose.pdf.facades/bookmarks/methods/index). Você pode então percorrer esses marcadores e obter objetos individuais [Bookmark](https://reference.aspose.com/pdf/net/aspose.pdf.facades/bookmark). Finalmente, salve o arquivo PDF atualizado usando o método [Save](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/save). O trecho de código a seguir mostra como exportar marcadores para um arquivo XML.

{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-Bookmarks-ExtractBookmarks-ExtractBookmarks.cs" >}}