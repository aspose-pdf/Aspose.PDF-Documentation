---
title: Agregar archivo adjunto
linktitle: Agregar archivo adjunto
type: docs
weight: 10
url: /java/add-attachment/
description: Aprenda cómo adjuntar un archivo externo a un documento PDF en Java usando la fachada PdfContentEditor en Aspose.PDF.
lastmod: "2026-06-09"
TechArticle: true
AlternativeHeadline: Agregar un archivo adjunto a un PDF en Java
Abstract: Este artículo muestra cómo vincular un PDF, abrir un archivo adjunto como una secuencia, agregar el documento adjunto con una descripción y guardar el archivo actualizado usando la fachada PdfContentEditor en Aspose.PDF para Java.
---
## Agregar un documento adjunto


1. 
Vincule el PDF de origen a la fachada `PdfContentEditor`.

2. 
Abra el archivo adjunto como flujo de entrada.

3. 
Llame a `addDocumentAttachment(...)` con la transmisión, el nombre del archivo y la descripción.

4. 
Guarde el documento PDF actualizado.

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
