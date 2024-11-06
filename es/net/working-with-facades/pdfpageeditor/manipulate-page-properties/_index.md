---
title: Manipulate Page Properties
type: docs
weight: 80
url: es/net/manipulate-page-properties/
description: Esta sección explica cómo manipular las Propiedades de Página con Aspose.PDF Facades usando la Clase PdfPageEditor.
lastmod: "2021-06-05"
draft: false
---

## Obtener Propiedades de Página de un Archivo PDF Existente

[PdfPageEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfpageeditor) le permite trabajar con páginas individuales del archivo PDF. Ayuda a obtener las propiedades de la página individual, como diferentes tamaños de cuadros de página, rotación de página, zoom de página, etc. Para obtener esas propiedades, necesitas crear un objeto [PdfPageEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfpageeditor) y enlazar el archivo PDF de entrada utilizando el método [BindPdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades.facade/bindpdf/methods/3). Después de eso, puedes usar diferentes métodos para obtener las propiedades de la página como [GetPageRotation](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfpageeditor/methods/getpagerotation), [GetPages](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfpageeditor/methods/getpages), [GetPageBoxSize](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfpageeditor/methods/getpageboxsize), etc.

El siguiente fragmento de código te muestra cómo obtener las propiedades de la página PDF de un archivo PDF existente.




{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-Pages-ManipulatePageProperties-GetPageProperties-GetPageProperties.cs" >}}
## Establecer Propiedades de Página en un Archivo PDF Existente

Para establecer propiedades de página como rotación de página, zoom o punto de origen, necesitas usar la clase [PdfPageEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfpageeditor). Esta clase proporciona diferentes métodos y propiedades para establecer estas propiedades de página. En primer lugar, necesitas crear un objeto de la clase [PdfPageEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfpageeditor) y vincular el archivo PDF de entrada utilizando el método [BindPdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades.facade/bindpdf/methods/3). Después de eso, puedes usar estos métodos y propiedades para establecer las propiedades de la página. Finalmente, guarda el archivo PDF actualizado utilizando el método [Save](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/save).

El siguiente fragmento de código te muestra cómo establecer las propiedades de página de un PDF en un archivo PDF existente.




{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-Pages-ManipulatePageProperties-SetPageProperties-SetPageProperties.cs" >}}

## Cambiar el tamaño del contenido de páginas específicas en un archivo PDF

El método ResizeContents de la clase [PdfPageEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfpageeditor) permite cambiar el tamaño del contenido de las páginas en un archivo PDF. La clase [ContentsResizeParameters](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdffileeditor/contentsresizeparameters) se utiliza para especificar los parámetros que se usarán para cambiar el tamaño de la(s) página(s), por ejemplo, márgenes en porcentaje o unidades, etc. Puedes cambiar el tamaño de todas las páginas o especificar un array de páginas para cambiar su tamaño usando el método ResizeContents.

El siguiente fragmento de código muestra cómo cambiar el tamaño del contenido de algunas páginas específicas de un archivo PDF.



{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-Pages-ManipulatePageProperties-ResizePageContents-ResizePageContents.cs" >}}