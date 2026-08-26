---
title: Add Attachment
linktitle: Add Attachment
type: docs
weight: 10
url: /java/add-attachment/
description: Learn how to attach an external file to a PDF document in Java using the PdfContentEditor facade in Aspose.PDF.
lastmod: "2026-06-09"
TechArticle: true
AlternativeHeadline: Add a file attachment to a PDF in Java
Abstract: This article shows how to bind a PDF, open an attachment as a stream, add the document attachment with a description, and save the updated file using the PdfContentEditor facade in Aspose.PDF for Java.
---
## Add a document attachment

1. Bind the source PDF to the `PdfContentEditor` facade.
2. Open the attachment file as an input stream.
3. Call `addDocumentAttachment(...)` with the stream, file name, and description.
4. Save the updated PDF document.

```java
public static void addAttachment(Path inputFile, Path attachmentFile, Path outputFile) throws Exception {
    PdfContentEditor editor = new PdfContentEditor();
    try (InputStream attachmentStream = Files.newInputStream(attachmentFile)) {
        editor.bindPdf(inputFile.toString());
        editor.addDocumentAttachment(attachmentStream, attachmentFile.getFileName().toString(), "Sample attachment.");
        editor.save(outputFile.toString());
    } finally {
        editor.close();
    }
}
```
