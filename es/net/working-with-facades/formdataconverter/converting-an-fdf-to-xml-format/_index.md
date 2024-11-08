---
title: Converting an FDF to XML format
type: docs
weight: 10
url: /es/net/converting-an-fdf-to-xml-format/
description: Esta sección explica cómo puedes convertir un FDF al formato XML con la Clase FormDataConverter.
lastmod: "2021-06-05"
draft: false
---

{{% alert color="primary" %}}

El espacio de nombres [Aspose.Pdf.Facades](https://reference.aspose.com/pdf/net/aspose.pdf.facades) en [Aspose.PDF para .NET](/pdf/es/net/) soporta muy bien los AcroForms. También admite la importación y exportación de datos de formularios a diferentes formatos de archivo como FDF, XFDF y XML. Sin embargo, a veces los desarrolladores podrían necesitar convertir un formato en otro. Este artículo analiza la función que convierte FDF en XML.

{{% /alert %}}

## Detalles

FDF significa Form Data Format, y un archivo FDF contiene los valores del formulario en un par clave/valor. Sabemos también que el archivo XML contiene los valores como etiquetas. Donde, principalmente la clave se representa como el nombre de la etiqueta y el valor se representa como el valor dentro de esa etiqueta. Ahora, [Aspose.Pdf.Facades](https://reference.aspose.com/pdf/net/aspose.pdf.facades) nos proporciona la flexibilidad de convertir un formato de archivo FDF en un formato XML.

Podemos utilizar la clase [FormDataConverter](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formdataconverter) para este propósito. Esta clase nos proporciona diferentes métodos para convertir un formato de datos en otro formato. En este artículo, solo utilizaremos un método llamado [ConvertFdfToXml](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formdataconverter/methods/convertfdftoxml). Este método toma un archivo FDF como entrada o flujo de origen y lo guarda en formato XML.

El siguiente fragmento de código te muestra cómo convertir un archivo FDF en un archivo XML:




{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-TechnicalArticles-ConvertPdfToXML-ConvertPdfToXML.cs" >}}