---
title: Extensible Metadata Platform - XMP
type: docs
weight: 10
url: /es/net/working-with-extensible-metadata-platform-xmp/
description: Esta sección explica cómo trabajar con la Plataforma de Metadatos Extensible - XMP usando la Clase PdfXmpMetadata.
lastmod: "2021-06-05"
draft: false
---

{{% alert color="primary" %}}

La Plataforma de Metadatos Extensible (XMP) es un estándar creado por Adobe Systems Inc. Este estándar fue desarrollado para procesar y almacenar metadatos estandarizados y propietarios. Estos metadatos pueden ser incrustados en diferentes formatos de archivo, pero en este artículo nos centraremos solo en el formato de archivo PDF. Veremos cómo podemos incrustar metadatos en un archivo PDF usando el espacio de nombres Aspose.Pdf.Facades en Aspose.PDF para .NET. Usaremos la clase [PdfXmpMetadata](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfxmpmetadata) para manipular XMP en el documento PDF.

{{% /alert %}}

## Antecedentes

Un archivo PDF pasa por muchas etapas durante su vida útil. Creamos un documento PDF y luego lo pasamos a otras personas o departamentos para su posterior procesamiento. Sin embargo, durante este proceso necesitamos realizar un seguimiento de diferentes aspectos de los cambios realizados. XMP sirve para este propósito de realizar un seguimiento de los cambios u otra información sobre los datos en el archivo.

## Explicación

Para manipular XMP usando Aspose.Pdf.Facades, utilizaremos la clase [PdfXmpMetadata](http://www.aspose.com/docs/display/pdfnet/PdfXmpMetadata+Class). Usaremos esta clase para manipular propiedades de metadatos predefinidas. La clase [PdfXmpMetadata](http://www.aspose.com/docs/display/pdfnet/PdfXmpMetadata+Class) añade estas propiedades a un archivo PDF. También ayuda a abrir y guardar archivos PDF en los que estamos añadiendo metadatos. Entonces, usando la clase [PdfXmpMetadata](http://www.aspose.com/docs/display/pdfnet/PdfXmpMetadata+Class), podemos manipular fácilmente XMP en un archivo PDF.

El siguiente fragmento de código te ayudará a entender cómo usar la clase [PdfXmpMetadata](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfxmpmetadata) para trabajar con XMP:
{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-TechnicalArticles-ExtensibleMetadataPlatform-ExtensibleMetadataPlatform.cs" >}}

## Conclusión

{{% alert color="primary" %}}
En este artículo, hemos visto cómo podemos trabajar con XMP usando Aspose.Pdf.Facades. [PdfXmpMetadata](http://www.aspose.com/docs/display/pdfnet/PdfXmpMetadata+Class), utilizado en este artículo, hace que sea muy fácil para el usuario manipular metadatos en un documento PDF. Si la clase [PdfXmpMetadata](http://www.aspose.com/docs/display/pdfnet/PdfXmpMetadata+Class) se utiliza correctamente, será muy fácil incorporar inteligencia en los archivos PDF, y acercar un poco más la web semántica a su realización.
{{% /alert %}}