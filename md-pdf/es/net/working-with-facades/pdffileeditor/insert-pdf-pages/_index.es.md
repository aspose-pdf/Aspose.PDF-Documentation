---
title: Insertar páginas PDF
type: docs
weight: 50
url: /net/insert-pdf-pages/
description: Esta sección explica cómo insertar páginas PDF con Aspose.PDF Facades usando la clase PdfFileEditor.
lastmod: "2021-06-05"
draft: false
---

## Insertar páginas PDF entre dos números usando rutas de archivos

Un rango particular de páginas puede insertarse de un PDF en otro usando el método [Insert](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/methods/insert/index) de la clase [PdfFileEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor). Para hacer eso, necesitas un archivo PDF de entrada en el cual deseas insertar las páginas, un archivo de puerto del cual las páginas deben ser tomadas para la inserción, una ubicación donde las páginas deben ser insertadas, y un rango de páginas del archivo de puerto que tienen que ser insertadas en el archivo PDF de entrada. Este rango se especifica con los parámetros de página de inicio y página de fin. Finalmente, el archivo PDF de salida se guarda con el rango especificado de páginas insertadas en el archivo de entrada. El siguiente fragmento de código te muestra cómo insertar páginas de PDF entre dos números usando flujos de archivo.

{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-Pages-InsertPages-InsertPagesBetweenNumbers-InsertPagesBetweenNumbers.cs" >}}

## Insertar un Array de Páginas PDF Usando Rutas de Archivos

Si deseas insertar algunas páginas especificadas en otro archivo PDF, entonces puedes usar una sobrecarga del método [Insert](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/methods/insert/index) que requiere un array de enteros de páginas. En este array, puedes especificar qué páginas particulares deseas insertar en el archivo PDF de entrada. Para hacer eso, necesitas un archivo PDF de entrada en el cual deseas insertar las páginas, un archivo de puerto del cual se deben tomar las páginas para la inserción, una ubicación donde se van a insertar las páginas y un array de enteros de las páginas del archivo de puerto que deben ser insertadas en el archivo PDF de entrada. Este array contiene una lista de páginas particulares que te interesa insertar en el archivo PDF de entrada. Finalmente, el archivo PDF de salida se guarda con el array especificado de páginas insertadas en el archivo de entrada.
El siguiente fragmento de código te muestra cómo insertar un array de páginas PDF usando rutas de archivos.

## Insertar Páginas PDF entre Dos Números Usando Streams

Si deseas insertar el rango de páginas usando streams, solo necesitas usar la sobrecarga adecuada del método [Insert](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/methods/insert/index) de la clase [PdfFileEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor). Para hacer eso, necesitas un flujo de entrada de PDF en el que deseas insertar las páginas, un flujo de puerto del cual se deben tomar las páginas para la inserción, una ubicación donde se deben insertar las páginas y un rango de páginas del flujo de puerto que deben ser insertadas en el flujo de entrada de PDF. Este rango se especifica con parámetros de página de inicio y página final. Finalmente, el flujo de salida de PDF se guarda con el rango especificado de páginas insertadas en el flujo de entrada. El siguiente fragmento de código te muestra cómo insertar páginas de PDF entre dos números usando flujos.

{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-Pages-InsertPages-InsertPagesBetweenNumbersUsingStreams-InsertPagesBetweenNumbersUsingStreams.cs" >}}

## Insertar un Array de Páginas PDF Usando Flujos

También puedes insertar un array de páginas en otro archivo PDF usando flujos con la ayuda de una sobrecarga adecuada del método Insert que requiere un array de enteros de páginas. En este array, puedes especificar qué páginas particulares deseas insertar en el flujo de entrada del PDF. Para hacer eso, necesitas un flujo de entrada de PDF en el que quieras insertar las páginas, un flujo del puerto del cual se deben tomar las páginas para la inserción, una ubicación donde las páginas deben ser insertadas, y un array de enteros de las páginas del flujo del puerto que deben ser insertadas en el archivo PDF de entrada. Este array contiene una lista de páginas particulares que estás interesado en insertar en el flujo de entrada del PDF. Finalmente, el flujo de salida del PDF se guarda con el array especificado de páginas insertadas en el archivo de entrada. El siguiente fragmento de código te muestra cómo insertar un array de páginas PDF usando flujos.



{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-Pages-InsertPages-InsertPagesUsingStreams-InsertPagesUsingStreams.cs" >}}