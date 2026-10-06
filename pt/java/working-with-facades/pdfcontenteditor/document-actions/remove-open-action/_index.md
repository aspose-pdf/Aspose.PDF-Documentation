---
title: Remover ação de abertura
linktitle: Remover ação de abertura
type: docs
weight: 20
url: /pt/java/remove-open-action/
description: Saiba como remover a ação de abertura de documento de um PDF em Java usando a fachada PdfContentEditor no Aspose.PDF.
lastmod: "2026-10-06"
TechArticle: true
AlternativeHeadline: Remover a ação de abertura de documento PDF em Java
Abstract: Este artigo mostra como vincular um PDF, remover a ação de abertura de documento e salvar o documento atualizado usando a fachada PdfContentEditor no Aspose.PDF for Java.
---
## Remover a ação de abertura de documento

1. Vincule o PDF de origem à fachada `PdfContentEditor`.
2. Chame `removeDocumentOpenAction()`.
3. Salve o documento PDF atualizado.

```java
public static void removeOpenAction(Path inputFile, Path outputFile) {
    PdfContentEditor editor = new PdfContentEditor();
    try {
        editor.bindPdf(inputFile.toString());
        editor.removeDocumentOpenAction();
        editor.save(outputFile.toString());
    } finally {
        editor.close();
    }
}
```
