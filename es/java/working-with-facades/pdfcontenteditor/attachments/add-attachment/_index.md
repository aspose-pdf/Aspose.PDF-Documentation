---
title: Agregar adjunto
linktitle: Agregar adjunto
type: docs
weight: 10
url: /es/java/add-attachment/
description: Aprenda cómo adjuntar un archivo externo a un documento PDF en Java usando la fachada PdfContentEditor en Aspose.PDF.
lastmod: "2026-09-29"
TechArticle: true
AlternativeHeadline: Agregar un archivo adjunto a un PDF en Java
Abstract: Este artículo muestra cómo vincular un PDF, abrir un adjunto como flujo, agregar el adjunto del documento con una descripción y guardar el archivo actualizado usando la fachada PdfContentEditor en Aspose.PDF for Java.
---
## Agregar un adjunto de documento

1. Vincule el PDF de origen a la fachada `PdfContentEditor`.
2. Abra el archivo adjunto como un flujo de entrada.
3. Llame `addDocumentAttachment(...)` con el flujo, el nombre del archivo y la descripción.
4. Guarde el documento PDF actualizado.

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
