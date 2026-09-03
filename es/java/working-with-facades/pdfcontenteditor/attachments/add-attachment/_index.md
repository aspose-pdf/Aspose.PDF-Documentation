---
title: Agregar adjunto
linktitle: Agregar adjunto
type: docs
weight: 10
url: /es/java/add-attachment/
description: Aprenda cómo adjuntar un archivo externo a un documento PDF en Java utilizando la fachada PdfContentEditor en Aspose.PDF.
lastmod: "2026-09-03"
TechArticle: true
AlternativeHeadline: Agregar un archivo adjunto a un PDF en Java
Abstract: Este artículo muestra cómo vincular un PDF, abrir un adjunto como flujo, agregar el adjunto del documento con una descripción y guardar el archivo actualizado utilizando la fachada PdfContentEditor en Aspose.PDF para Java.
---
## Agregar un adjunto de documento

1. Vincula el PDF de origen a la `PdfContentEditor` fachada.
2. Abra el archivo adjunto como un flujo de entrada.
3. Llamada `addDocumentAttachment(...)` con el flujo, el nombre de archivo y la descripción.
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
