---
title: Dividir páginas PDF
type: docs
weight: 60
url: es/net/split-pdf-pages/
description: Esta sección explica cómo dividir páginas PDF con Aspose.PDF Facades utilizando la clase PdfFileEditor.
lastmod: "2021-06-05"
draft: false
---

## Dividir páginas PDF desde la primera usando rutas de archivos

El método [SplitFromFirst](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdffileeditor/splitfromfirst/methods/1) de la clase [PdfFileEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdffileeditor) te permite dividir el archivo PDF comenzando desde la primera página y terminando en el número de página especificado. Si deseas manipular los archivos PDF desde el disco, puedes pasar las rutas de los archivos PDF de entrada y salida a este método. El siguiente fragmento de código te muestra cómo dividir páginas PDF desde la primera usando rutas de archivos.

{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-Pages-SplitPages-SplitPagesUsingPaths-SplitPagesUsingPaths.cs" >}}

## Dividir páginas PDF desde la primera usando flujos de archivos

[SplitFromFirst](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdffileeditor/splitfromfirst/methods/1) método de la clase [PdfFileEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdffileeditor) te permite dividir el archivo PDF comenzando desde la primera página y terminando en el número de página especificado. Si deseas manipular los archivos PDF desde los flujos, puedes pasar los flujos de entrada y salida del PDF a este método. El siguiente fragmento de código te muestra cómo dividir las páginas PDF desde la primera utilizando flujos de archivos.

{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-Pages-SplitPages-SplitPagesUsingStreams-SplitPagesUsingStreams.cs" >}}

## Dividir Páginas PDF en Lotes Usando Rutas de Archivos

[SplitToBulks](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdffileeditor/methods/splittobulks/index) método de la clase [PdfFileEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdffileeditor) te permite dividir el archivo PDF en múltiples conjuntos de páginas. En este ejemplo, requerimos dos conjuntos de páginas (1, 2) y (5, 6). Si deseas acceder al archivo PDF desde el disco, necesitas pasar el PDF de entrada como ruta de archivo. Este método devuelve un array de MemoryStream. Puedes recorrer este array y guardar los conjuntos individuales de páginas como archivos separados. El siguiente fragmento de código te muestra cómo dividir las páginas PDF en bloques usando rutas de archivo.

{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-Pages-SplitPages-SplitPagesToBulkUsingPaths-SplitPagesToBulkUsingPaths.cs" >}}

## Dividir Páginas de PDF en Bloques Usando Streams

El método [SplitToBulks](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/methods/splittobulks/index) de la clase [PdfFileEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor) te permite dividir el archivo PDF en múltiples conjuntos de páginas. En este ejemplo, necesitamos dos conjuntos de páginas (1, 2) y (5, 6). Puede pasar un flujo a este método en lugar de acceder al archivo desde el disco. Este método devuelve un array de MemoryStream. Puede recorrer este array y guardar los conjuntos individuales de páginas como archivos separados. El siguiente fragmento de código le muestra cómo dividir páginas de PDF en bloque usando flujos.

{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-Pages-SplitPages-SplitPagesToBulkUsingStreams-SplitPagesToBulkUsingStreams.cs" >}}

## Dividir Páginas de PDF Hasta el Final Usando Rutas de Archivos

El método [SplitToEnd](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/methods/splittoend/index) de la clase [PdfFileEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor) le permite dividir el PDF desde el número de página especificado hasta el final del archivo PDF y guardarlo como un nuevo PDF. Para hacer esto, utilizando rutas de archivos, necesitas pasar las rutas de archivo de entrada y salida y el número de página desde donde se debe comenzar la división. El PDF de salida se guardará en el disco. El siguiente fragmento de código te muestra cómo dividir las páginas del PDF hasta el final usando rutas de archivo.

{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-Pages-SplitPages-SplitPagesToEndUsingPaths-SplitPagesToEndUsingPaths.cs" >}}

## Dividir Páginas de PDF hasta el Final Usando Streams

El método [SplitToEnd](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/methods/splittoend/index) de la clase [PdfFileEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor) te permite dividir el PDF desde el número de página especificado hasta el final del archivo PDF y guardarlo como un nuevo PDF. Para hacer esto, usando flujos, necesitas pasar flujos de entrada y salida y el número de página desde donde se necesita comenzar la división. El PDF de salida se guardará en el flujo de salida. El siguiente fragmento de código te muestra cómo dividir las páginas del PDF hasta el final usando flujos.

{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-Pages-SplitPages-SplitPagesToEndUsingStreams-SplitPagesToEndUsingStreams.cs" >}}

## Dividir PDF en Páginas Individuales Usando Rutas de Archivos

{{% alert color="primary" %}}

Puedes intentar dividir el documento PDF y ver los resultados en línea en este enlace:

[products.aspose.app/pdf/splitter](https://products.aspose.app/pdf/splitter) {{% /alert %}}

Para dividir el archivo PDF en páginas individuales, necesitas pasar el PDF como ruta de archivo al método [SplitToPages](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/methods/splittopages/index). Este método devolverá un array de MemoryStream que contiene páginas individuales del archivo PDF. Puedes recorrer este array de MemoryStream y guardar páginas individuales como archivos PDF individuales en el disco. El siguiente fragmento de código te muestra cómo dividir un PDF en páginas individuales usando rutas de archivo.

{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-Pages-SplitPages-SplitToIndividualPagesUsingPaths-SplitToIndividualPagesUsingPaths.cs" >}}

## Dividir PDF en Páginas Individuales Usando Streams

Para dividir un archivo PDF en páginas individuales, necesitas pasar el PDF como flujo al método [SplitToPages](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/methods/splittopages/index). Este método devolverá un array de MemoryStream que contiene páginas individuales del archivo PDF. Puedes recorrer este array de MemoryStream y guardar páginas individuales como archivos PDF individuales en el disco, o puedes mantener estas páginas individuales en el flujo de memoria para usarlas más tarde en tu aplicación. El siguiente fragmento de código te muestra cómo dividir un PDF en páginas individuales usando flujos.

{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-Pages-SplitPages-SplitToIndividualPagesUsingStreams-SplitToIndividualPagesUsingStreams.cs" >}}