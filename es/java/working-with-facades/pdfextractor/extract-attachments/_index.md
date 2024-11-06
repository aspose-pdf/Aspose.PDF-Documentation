---
title: Extraer Adjuntos de un Archivo PDF
type: docs
weight: 10
url: es/java/extract-attachments/
description: Esta sección explica sobre cómo extraer adjuntos de un pdf con la clase PdfExtractor.
lastmod: "2021-06-05"
draft: false
---

Una de las principales categorías bajo las capacidades de extracción de [com.aspose.pdf.facades](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/package-frame) es la extracción de adjuntos.
 Esta categoría proporciona un conjunto de métodos, que no solo ayudan a extraer los archivos adjuntos, sino que también proporcionan los métodos que pueden ofrecer información relacionada con los archivos adjuntos, es decir, los métodos [GetAttachmentInfo](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfExtractor#getAttachmentInfo--) y [GetAttachName](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfExtractor#getAttachNames--) proporcionan información del archivo adjunto y el nombre del archivo adjunto respectivamente. Para extraer y luego obtener los archivos adjuntos usamos los métodos [ExtractAttachment](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfExtractor#extractAttachment--) y [GetAttachment](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfExtractor#getAttachment--).

El siguiente fragmento de código muestra cómo usar los métodos de PdfExtractor:

```java
  public static void ExtractAttachments() {
        PdfExtractor pdfExtractor = new PdfExtractor();
        pdfExtractor.bindPdf(_dataDir + "sample-attach.pdf");

        // Extraer archivos adjuntos
        pdfExtractor.extractAttachment();

        // Obtener nombres de archivos adjuntos
        if (pdfExtractor.getAttachNames().size() > 0) {
            System.out.println("Extrayendo y almacenando...");
            // Obtener archivos adjuntos extraídos
            pdfExtractor.getAttachment(_dataDir);
        }
    }
```