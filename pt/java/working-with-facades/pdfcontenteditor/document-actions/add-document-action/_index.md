---
title: Adicionar ação de documento
linktitle: Adicionar ação de documento
type: docs
weight: 10
url: /java/add-document-action/
description: Aprenda como adicionar uma ação de abertura de documento a um PDF em Java usando a fachada PdfContentEditor em Aspose.PDF.
lastmod: "2026-06-09"
TechArticle: true
AlternativeHeadline: Adicione uma ação de abertura de documento a um PDF em Java
Abstract: Este artigo mostra como vincular um PDF, anexar uma ação JavaScript ao evento document-open e salvar o documento atualizado usando a fachada PdfContentEditor em Aspose.PDF para Java.
---
## Adicione uma ação de abertura de documento

1. Vincule o PDF de origem à fachada `PdfContentEditor`.
2. Chame `addDocumentAdditionalAction(...)` com o evento `DOCUMENT_OPEN` e o texto da ação JavaScript.
3. Salve o documento PDF atualizado.

```java
public static void addDocumentAction(Path inputFile, Path outputFile) {
    PdfContentEditor editor = new PdfContentEditor();
    try {
        editor.bindPdf(inputFile.toString());
        editor.addDocumentAdditionalAction(PdfContentEditor.DOCUMENT_OPEN, "app.alert('Document opened with PdfContentEditor action');");
        editor.save(outputFile.toString());
    } finally {
        editor.close();
    }
}
```
