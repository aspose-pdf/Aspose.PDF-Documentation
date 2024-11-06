---
title: Extrair imagem e mudar posição do carimbo
type: docs
weight: 30
url: pt/net/extract-image-and-change-position-of-a-stamp/
description: Esta seção explica como extrair imagem e mudar posição de um carimbo com Aspose.PDF Facades.
lastmod: "2021-06-05"
draft: false
---

## Extrair Imagem de um Carimbo de Imagem

A classe [PdfContentEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor) permite que você extraia imagens de um carimbo em um arquivo PDF. Primeiro, você precisa criar um objeto da classe [PdfContentEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor) e vincular o arquivo PDF de entrada usando o método [BindPdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades.facade/bindpdf/methods/3). Depois disso, chame o método [GetStamps](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor/methods/getstamps) para obter um array de objetos StampInfo de uma página específica do arquivo PDF. Em seguida, você pode obter a imagem de um StampInfo usando a propriedade StampInfo.Image. Uma vez que você obtém a imagem, você pode salvá-la ou trabalhar com diferentes propriedades da imagem. O trecho de código a seguir mostra como extrair a imagem de um selo de imagem.

{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-Stamps-Watermarks-ExtractImageImageStamp-ExtractImageImageStamp.cs" >}}

## Alterar a Posição de um Selo em um arquivo PDF

A classe [PdfContentEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor) permite que você altere a posição de um selo em um arquivo PDF. Primeiro, você precisa criar um objeto da classe [PdfContentEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor) e vincular o arquivo PDF de entrada usando o método [BindPdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades.facade/bindpdf/methods/3). Depois disso, chame o método [MoveStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor/methods/movestamp) com o índice do carimbo e a nova posição em uma página específica do arquivo PDF. Em seguida, você pode salvar o arquivo atualizado usando o método [Save](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/save). O trecho de código a seguir mostra como mover um carimbo em uma página específica.

{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-Stamps-Watermarks-ChangeStampPosition-ChangeStampPosition.cs" >}}

Além disso, você pode usar o método [MoveStampById](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor/methods/movestampbyid) para mover um carimbo específico usando StampId.

{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-Stamps-Watermarks-ChangeStampPosition-ChangeStampPositionByID.cs" >}}