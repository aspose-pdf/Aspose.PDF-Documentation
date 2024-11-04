---
title: Definir Metadados XMP de um PDF existente - fachadas
type: docs
weight: 20
url: /java/set-xmp-metadata/
description: Esta seção explica como definir metadados XMP com Aspose.PDF Facades usando a Classe PdfXmpMetadata.
lastmod: "2021-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

Para definir metadados XMP em um arquivo PDF, você precisa criar um objeto [PdfXmpMetadata](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfXmpMetadata) e vincular o arquivo PDF usando o método [bindPdf(..)](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Facade#bindPdf-com.aspose.pdf.IDocument-).
 Você pode usar o método setByDefaultMetadataProperties(..) da classe [PdfXmpMetadata](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfXmpMetadata) para adicionar diferentes propriedades. Finalmente, chame o método [save(...)](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/SaveableFacade#save-java.io.OutputStream-) da classe [PdfXmpMetadata](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfXmpMetadata).

O trecho de código a seguir mostra como adicionar metadados XMP em um arquivo PDF.

{{< gist "aspose-pdf" "474c352a71ac9477aa0d604fd32e1c6a" "Examples-src-main-java-com-aspose-pdf-examples-facades-Document-SetXMPMetadataOfAnExistingPDF-.java" >}}