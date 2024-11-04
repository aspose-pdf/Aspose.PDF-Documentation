---
title: Edición de páginas individuales de un PDF
type: docs
weight: 20
url: /net/editing-a-pdf-s-individual-pages-using-pdfpageeditor-class/
description: Esta sección explica cómo editar páginas individuales de un PDF utilizando la clase PdfPageEditor.
lastmod: "2021-06-05"
draft: false
---

{{% alert color="primary" %}}

El espacio de nombres Aspose.Pdf.Facades en [Aspose.PDF para .NET](/pdf/net/) te permite manipular páginas individuales en un archivo PDF. Esta función te ayuda a trabajar con la visualización de la página, alineación, y transición, etc. La clase PdfPageEditor ayuda a lograr esta funcionalidad. En este artículo, examinaremos las propiedades y métodos proporcionados por esta clase y el funcionamiento de estos métodos también.

{{% /alert %}}

## Explicación

La clase [PdfPageEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfpageeditor) es diferente de la clase [PdfFileEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor) y de la clase [PdfContentEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor). Primero, necesitamos entender la diferencia, y luego podremos comprender mejor la clase PdfPageEditor. La clase PdfFileEditor te permite manipular todas las páginas en un archivo como agregar, eliminar o concatenar páginas, etc., mientras que la clase PdfContentEditor te ayuda a manipular el contenido de una página, es decir, texto y otros objetos, etc. Mientras que, la clase PdfPageEditor solo trabaja con la página individual en sí, como rotar, hacer zoom y alinear una página, etc.

Podemos dividir las características proporcionadas por esta clase en tres categorías principales, es decir, Transición, Alineación y Visualización. Vamos a discutir estas categorías a continuación:

### Transition

Esta clase contiene dos propiedades relacionadas con la transición, es decir, [TransitionType](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfpageeditor/properties/transitiontype) y [TransitionDuration](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfpageeditor/properties/transitionduration). TransitionType especifica el estilo de transición que se utilizará al pasar a esta página desde otra página durante una presentación. TransitionDuration especifica la duración de visualización para las páginas.

### Alignment

La clase PdfPageEditor admite alineaciones tanto horizontales como verticales. Proporciona dos propiedades para servir al propósito, es decir, [Alignment](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfpageeditor/properties/alignment) y [VerticalAlignment](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfpageeditor/properties/VerticalAlignment). La propiedad Alignment se utiliza para alinear los contenidos horizontalmente. La propiedad Alignment toma un valor de AlignmentType, que contiene tres opciones, es decir, Center, Left y Right. La propiedad VerticalAlignment toma un valor de VerticalAlignmentType, que contiene tres opciones, es decir, Bottom, Center y Top.

### Display

Bajo la categoría de visualización, podemos incluir propiedades como PageSize, Rotation, Zoom y DisplayDuration. PageSize propiedad especifica el tamaño de la página individual en el archivo. Esta propiedad toma un objeto PageSize como entrada, que encapsula tamaños de página predefinidos como A0, A1, A2, A3, A4, A5, A6, B5, Letter, Ledger, y P11x17. La propiedad Rotation se utiliza para establecer la rotación de una página individual. Puede tomar valores 0, 90, 180, o 270. La propiedad Zoom establece el coeficiente de zoom para la página, y toma un valor flotante como entrada. Esta clase también proporciona un método para obtener el tamaño de página y la rotación de página de la página individual en el archivo.

Puedes encontrar ejemplos de los métodos mencionados anteriormente en el fragmento de código dado a continuación:



{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-TechnicalArticles-EditPdfPages-EditPdfPages.cs" >}}

## Conclusión

{{% alert color="primary" %}}
En este artículo, hemos examinado más de cerca la clase [PdfPageEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfpageeditor). We have elaborated the properties and methods provided by this class. It makes the manipulation of individual pages in a class a very easy and simple task.  
Hemos elaborado las propiedades y métodos proporcionados por esta clase. Hace que la manipulación de páginas individuales en una clase sea una tarea muy fácil y sencilla.  
{{% /alert %}}