---
title: Extraer imagen y cambiar posición del sello
type: docs
weight: 30
url: /net/extract-image-and-change-position-of-a-stamp/
description: Esta sección explica cómo extraer imagen y cambiar la posición de un sello con Aspose.PDF Facades.
lastmod: "2021-06-05"
draft: false
---

## Extraer imagen de un sello de imagen

La clase [PdfContentEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor) permite extraer imágenes de un sello en un archivo PDF. Primero, necesitas crear un objeto de la clase [PdfContentEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor) y enlazar el archivo PDF de entrada usando el método [BindPdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades.facade/bindpdf/methods/3). Después de eso, llama al método [GetStamps](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor/methods/getstamps) para obtener un array de objetos StampInfo de una página particular del archivo PDF. Luego puedes obtener la imagen de un StampInfo usando la propiedad StampInfo.Image. Una vez que obtienes la imagen, puedes guardar la imagen o trabajar con diferentes propiedades de la imagen. El siguiente fragmento de código te muestra cómo extraer una imagen de un sello de imagen.

{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-Stamps-Watermarks-ExtractImageImageStamp-ExtractImageImageStamp.cs" >}}

## Cambiar la posición de un sello en un archivo PDF

La clase [PdfContentEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor) te permite cambiar la posición de un sello en un archivo PDF. Primero, necesitas crear un objeto de la clase [PdfContentEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor) y vincular el archivo PDF de entrada usando el método [BindPdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades.facade/bindpdf/methods/3). Después de eso, llama al método [MoveStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor/methods/movestamp) con el índice del sello y la nueva posición en una página particular del archivo PDF. Luego, puedes guardar el archivo actualizado usando el método [Save](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/save). El siguiente fragmento de código te muestra cómo mover un sello en una página particular.



{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-Stamps-Watermarks-ChangeStampPosition-ChangeStampPosition.cs" >}}



Además, puedes usar el método [MoveStampById](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor/methods/movestampbyid) para mover un sello específico usando StampId.




{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-Stamps-Watermarks-ChangeStampPosition-ChangeStampPositionByID.cs" >}}