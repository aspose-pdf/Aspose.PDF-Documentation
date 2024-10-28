---
title: Eliminar páginas de PDF
type: docs
weight: 70
url: /net/delete-pdf-pages/
description: Esta sección explica cómo eliminar páginas de PDF con Aspose.PDF Facades utilizando la clase PdfFileEditor.
lastmod: "2021-06-05"
draft: false
---

Si deseas eliminar una serie de páginas del archivo PDF que se encuentra en el disco, puedes usar la sobrecarga del método [Delete](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/methods/delete/index) que toma los siguientes tres parámetros: ruta del archivo de entrada, arreglo de números de páginas a eliminar y ruta del archivo PDF de salida. El segundo parámetro es un arreglo de enteros que representa todas las páginas que deben ser eliminadas. Las páginas especificadas se eliminan del archivo de entrada y el resultado se guarda como archivo de salida. El siguiente fragmento de código te muestra cómo eliminar páginas de PDF usando rutas de archivo.



{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-Pages-DeletePages-DeletePagesUsingFilePath-DeletePagesUsingFilePath.cs" >}}


## Eliminar páginas de PDF usando flujos

El método [Delete](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/methods/delete/index) de la clase [PdfFileEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor) también proporciona una sobrecarga que te permite eliminar las páginas del archivo PDF de entrada, mientras que tanto los archivos de entrada como de salida están en los flujos. Esta sobrecarga toma los siguientes tres parámetros: flujo de entrada, matriz de enteros de páginas PDF a eliminar, y flujo de salida. El siguiente fragmento de código te muestra cómo eliminar páginas de PDF usando flujos.

{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-Pages-DeletePages-DeletePagesUsingStream-DeletePagesUsingStream.cs" >}}