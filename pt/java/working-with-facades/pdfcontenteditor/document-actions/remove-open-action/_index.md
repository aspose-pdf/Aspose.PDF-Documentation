---
title: Remover ação aberta
linktitle: Remover ação aberta
type: docs
weight: 20
url: /java/remove-open-action/
description: Aprenda como remover a ação de abertura de documento de um PDF em Java usando a fachada PdfContentEditor em Aspose.PDF.
lastmod: "2026-06-09"
TechArticle: true
AlternativeHeadline: Remover uma ação de abertura de documento PDF em Java
Abstract: Este artigo mostra como vincular um PDF, remover a ação de abertura de documento e salvar o documento atualizado usando a fachada PdfContentEditor em Aspose.PDF para Java.
---
## Remova a ação de abertura de documento

1. Vincule o PDF de origem à fachada `PdfContentEditor`.
2. Ligue para `removeDocumentOpenAction()`.
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
