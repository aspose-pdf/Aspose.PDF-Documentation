---
title: Setel Metadata XMP dari PDF yang ada - fasad
type: docs
weight: 20
url: /id/java/set-xmp-metadata/
description: Bagian ini menjelaskan cara menyetel metadata XMP dengan Aspose.PDF Facades menggunakan Kelas PdfXmpMetadata.
lastmod: "2021-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

Untuk menyetel metadata XMP dalam file PDF, Anda perlu membuat objek [PdfXmpMetadata](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfXmpMetadata) dan mengikat file PDF menggunakan metode [bindPdf(..)](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Facade#bindPdf-com.aspose.pdf.IDocument-).
 Anda dapat menggunakan metode setByDefaultMetadataProperties(..) dari kelas [PdfXmpMetadata](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfXmpMetadata) untuk menambahkan berbagai properti. Akhirnya, panggil metode [save(...)](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/SaveableFacade#save-java.io.OutputStream-) dari kelas [PdfXmpMetadata](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfXmpMetadata).

Cuplikan kode berikut menunjukkan kepada Anda bagaimana menambahkan metadata XMP dalam file PDF.

{{< gist "aspose-pdf" "474c352a71ac9477aa0d604fd32e1c6a" "Examples-src-main-java-com-aspose-pdf-examples-facades-Document-SetXMPMetadataOfAnExistingPDF-.java" >}}