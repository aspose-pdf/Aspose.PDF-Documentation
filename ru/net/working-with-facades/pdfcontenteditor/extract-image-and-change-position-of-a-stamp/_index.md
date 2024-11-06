---
title: Извлечение изображения и изменение положения штампа
type: docs
weight: 30
url: ru/net/extract-image-and-change-position-of-a-stamp/
description: Этот раздел объясняет, как извлечь изображение и изменить положение штампа с помощью Aspose.PDF Facades.
lastmod: "2021-06-05"
draft: false
---

## Извлечение изображения из штампа

Класс [PdfContentEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor) позволяет извлекать изображения из штампа в файле PDF. Сначала вам нужно создать объект класса [PdfContentEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor) и привязать входной PDF-файл с помощью метода [BindPdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades.facade/bindpdf/methods/3). После этого вызовите метод [GetStamps](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor/methods/getstamps), чтобы получить массив объектов StampInfo из определенной страницы PDF-файла. Затем вы можете получить изображение из StampInfo, используя свойство StampInfo.Image. Как только вы получите изображение, вы можете сохранить его или работать с различными свойствами изображения. Следующий фрагмент кода показывает, как извлечь изображение из штампа изображения.

{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-Stamps-Watermarks-ExtractImageImageStamp-ExtractImageImageStamp.cs" >}}

## Изменение положения штампа в PDF-файле

Класс [PdfContentEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor) позволяет изменить положение штампа в PDF-файле. First, you need to create an object of [PdfContentEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor) class and bind input PDF file using [BindPdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades.facade/bindpdf/methods/3) method. After that, call [MoveStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor/methods/movestamp) method with stamp index and new position on a particular page of PDF file. Then, you can save the updated file using [Save](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/save) method. The following code snippet shows you how to move a stamp in a particular page.

Сначала вам нужно создать объект класса [PdfContentEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor) и привязать входной PDF файл, используя метод [BindPdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades.facade/bindpdf/methods/3). После этого вызовите метод [MoveStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor/methods/movestamp) с индексом штампа и новой позицией на определенной странице PDF файла. Затем вы можете сохранить обновленный файл, используя метод [Save](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/save). Следующий фрагмент кода показывает, как переместить штамп на определенной странице.

{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-Stamps-Watermarks-ChangeStampPosition-ChangeStampPosition.cs" >}}

Also, you can use [MoveStampById](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor/methods/movestampbyid) method to move a specific stamp by using StampId.

Также вы можете использовать метод [MoveStampById](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor/methods/movestampbyid), чтобы переместить конкретный штамп, используя StampId.

{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-Stamps-Watermarks-ChangeStampPosition-ChangeStampPositionByID.cs" >}}