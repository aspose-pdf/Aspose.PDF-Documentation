---
title: Adicionar ação de documento
linktitle: Adicionar ação de documento
type: docs
weight: 10
url: /pt/java/add-document-action/
description: Saiba como adicionar uma ação de abertura de documento a um PDF em Java usando a fachada PdfContentEditor no Aspose.PDF.
lastmod: "2026-10-06"
TechArticle: true
AlternativeHeadline: Adicionar uma ação de abertura de documento a um PDF em Java
Abstract: Este artigo mostra como vincular um PDF, anexar uma ação JavaScript ao evento de abertura de documento e salvar o documento atualizado usando a fachada PdfContentEditor no Aspose.PDF for Java.
---
## Adicionar uma ação de abertura de documento

1. Vincular o PDF de origem ao `PdfContentEditor` fachada.
2. Chamar `addDocumentAdditionalAction(...)` com o `DOCUMENT_OPEN` evento e o texto da ação JavaScript.
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
