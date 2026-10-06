---
title: Remover anexos
linktitle: Remover anexos
type: docs
weight: 50
url: /pt/java/remove-attachments/
description: Saiba como remover todos os anexos de documento de um PDF em Java usando a fachada PdfContentEditor no Aspose.PDF.
lastmod: "2026-10-06"
TechArticle: true
AlternativeHeadline: Remover todos os anexos de PDF em Java
Abstract: Este artigo mostra como vincular um PDF, excluir todos os anexos de documento e salvar o arquivo atualizado usando a fachada PdfContentEditor no Aspose.PDF for Java.
---
## Remover todos os anexos

1. Vincule o PDF de origem à fachada `PdfContentEditor`.
2. Chame `deleteAttachments()` para remover todos os anexos incorporados.
3. Salve o documento PDF atualizado.

```java
public static void removeAttachments(Path inputFile, Path outputFile) {
    PdfContentEditor editor = new PdfContentEditor();
    try {
        editor.bindPdf(inputFile.toString());
        editor.deleteAttachments();
        editor.save(outputFile.toString());
    } finally {
        editor.close();
    }
}
```
