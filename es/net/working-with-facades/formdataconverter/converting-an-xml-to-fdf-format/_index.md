---
title: Converting an XML to FDF format
type: docs
weight: 20
url: /es/net/converting-an-xml-to-fdf-format/
description: Esta sección explica cómo puedes convertir un XML a formato FDF con FormDataConverter.
lastmod: "2021-06-05"
draft: false
---

{{% alert color="primary" %}}

El espacio de nombres [Aspose.Pdf.Facades](https://reference.aspose.com/pdf/net/aspose.pdf.facades) en [Aspose.PDF for .NET](/pdf/es/net/) soporta muy bien AcroForms. También soporta la importación y exportación de datos de formularios a diferentes formatos de archivo como FDF, XFDF y XML. Sin embargo, a veces un desarrollador necesita convertir un formato a otro. En este artículo, analizaremos la función que nos permite convertir un formato FDF a XML.

{{% /alert %}}

## Detalles

FDF significa Formato de Datos de Formularios, y un archivo FDF contiene los valores del formulario en un par clave/valor. Sabemos también que el archivo XML contiene los valores como etiquetas. Donde, principalmente la clave se representa como el nombre de la etiqueta y el valor se representa como el valor dentro de esa etiqueta. Ahora, [Aspose.Pdf.Facades](https://reference.aspose.com/pdf/net/aspose.pdf.facades) proporciona la flexibilidad para convertir un formato de archivo XML en formato FDF.

Utilice la clase [FormDataConverter](https://reference.aspose.com/pdf/net/aspose.pdf.facades/FormDataConverter) para este propósito. Esta clase proporciona diferentes métodos para convertir un formato de datos en otro. Este artículo muestra cómo usar un método, ConvertXmlToFdf(..), que toma un archivo FDF como entrada o flujo de origen y lo guarda en formato XML. El siguiente fragmento de código muestra cómo convertir un archivo FDF en un archivo XML.

{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-TechnicalArticles-XMLToPdf-XMLToPdf.cs" >}}