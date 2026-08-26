---
title: Add Attachments to PDF in Java
linktitle: Adding Attachment to a PDF document
type: docs
weight: 10
url: /java/add-attachment-to-pdf-document/
description: Learn how to add file attachments to PDF documents in Java using Aspose.PDF.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Add embedded files to PDF documents with Java
Abstract: Este artículo muestra cómo adjuntar un archivo externo a un documento PDF usando Aspose.PDF para Java. El ejemplo abre un PDF existente, crea una especificación de archivo para el archivo adjunto, lo agrega a la colección EmbeddedFiles del documento y guarda el archivo actualizado.
---
To attach a file to a PDF, load the source document, create a `FileSpecification`, add it to the embedded file collection, and save the result.

## Agregar un archivo adjunto a un documento PDF

Use this example when an external file should be embedded into an existing PDF.

1. Open the source PDF [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Cree una [Especificación de archivo](https://reference.aspose.com/pdf/java/com.aspose.pdf/filespecification/) para el archivo que desea incrustar.
1. Agregue la especificación del archivo a la colección `EmbeddedFiles` y guarde el documento actualizado.

```java
public static void addAttachments(Path inputFile, Path attachmentPath, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        FileSpecification fileSpecification = new FileSpecification(attachmentPath.toString(), "Sample text file");
        document.getEmbeddedFiles().add(attachmentPath.getFileName().toString(), fileSpecification);
        document.save(outputFile.toString());
    }
}
```
