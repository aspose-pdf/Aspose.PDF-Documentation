---
title: Manipular Propriedades da Página
type: docs
weight: 80
url: /net/manipulate-page-properties/
description: Esta seção explica como manipular Propriedades da Página com Aspose.PDF Facades usando a Classe PdfPageEditor.
lastmod: "2021-06-05"
draft: false
---

## Obter Propriedades da Página PDF de um Arquivo PDF Existente

[PdfPageEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfpageeditor) permite que você trabalhe com páginas individuais do arquivo PDF. Ele ajuda você a obter as propriedades da página individual, como diferentes tamanhos de caixa de página, rotação de página, zoom de página, etc. Para obter essas propriedades, você precisa criar um objeto [PdfPageEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfpageeditor) e vincular o arquivo PDF de entrada usando o método [BindPdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades.facade/bindpdf/methods/3). Depois disso, você pode usar diferentes métodos para obter as propriedades da página, como [GetPageRotation](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfpageeditor/methods/getpagerotation), [GetPages](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfpageeditor/methods/getpages), [GetPageBoxSize](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfpageeditor/methods/getpageboxsize), etc.

O snippet de código a seguir mostra como obter propriedades de página PDF de um arquivo PDF existente.




{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-Pages-ManipulatePageProperties-GetPageProperties-GetPageProperties.cs" >}}
## Definir Propriedades de Página em um Arquivo PDF Existente

Para definir propriedades de página como rotação de página, zoom ou ponto de origem, você precisa usar a classe [PdfPageEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfpageeditor). Esta classe fornece diferentes métodos e propriedades para definir essas propriedades de página. Primeiro, você precisa criar um objeto da classe [PdfPageEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfpageeditor) e vincular o arquivo PDF de entrada usando o método [BindPdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades.facade/bindpdf/methods/3). Depois disso, você pode usar esses métodos e propriedades para definir as propriedades da página. Finalmente, salve o arquivo PDF atualizado usando o método [Save](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/save).

O trecho de código a seguir mostra como definir propriedades de página em um arquivo PDF existente.




{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-Pages-ManipulatePageProperties-SetPageProperties-SetPageProperties.cs" >}}

## Redimensionar Conteúdos da Página de Páginas Específicas em um Arquivo PDF

O método ResizeContents da classe [PdfPageEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfpageeditor) permite redimensionar os conteúdos da página em um arquivo PDF. A classe [ContentsResizeParameters](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdffileeditor/contentsresizeparameters) é usada para especificar os parâmetros a serem usados para redimensionar a(s) página(s), por exemplo, margens em porcentagem ou unidades, etc. Você pode redimensionar todas as páginas ou especificar uma matriz de páginas a serem redimensionadas usando o método ResizeContents.

O trecho de código a seguir mostra como redimensionar o conteúdo de algumas páginas específicas de um arquivo PDF.



{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-Pages-ManipulatePageProperties-ResizePageContents-ResizePageContents.cs" >}}