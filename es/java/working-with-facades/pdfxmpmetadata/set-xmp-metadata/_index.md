---
title: Set XMP Metadata of an existing PDF - facades
type: docs
weight: 20
url: /es/java/set-xmp-metadata/
description: Esta sección explica cómo establecer metadatos XMP con Aspose.PDF Facades utilizando la clase PdfXmpMetadata.
lastmod: "2021-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

Para establecer metadatos XMP en un archivo PDF, necesita crear un objeto [PdfXmpMetadata](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfXmpMetadata) y enlazar el archivo PDF utilizando el método [bindPdf(..)](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Facade#bindPdf-com.aspose.pdf.IDocument-).
 Puedes usar el método setByDefaultMetadataProperties(..) de la clase [PdfXmpMetadata](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfXmpMetadata) para agregar diferentes propiedades. Finalmente, llama al método [save(...)](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/SaveableFacade#save-java.io.OutputStream-) de la clase [PdfXmpMetadata](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfXmpMetadata).

El siguiente fragmento de código te muestra cómo agregar metadatos XMP en un archivo PDF.

{{< gist "aspose-pdf" "474c352a71ac9477aa0d604fd32e1c6a" "Examples-src-main-java-com-aspose-pdf-examples-facades-Document-SetXMPMetadataOfAnExistingPDF-.java" >}}