---
title: Remover anexos
linktitle: Remover anexos
type: docs
weight: 50
url: /java/remove-attachments/
description: Aprenda como remover todos os anexos de documentos de um PDF em Java usando a fachada PdfContentEditor em Aspose.PDF.
lastmod: "2026-06-09"
TechArticle: true
AlternativeHeadline: Remova todos os anexos de PDF em Java
Abstract: Este artigo mostra como vincular um PDF, excluir todos os anexos do documento e salvar o arquivo atualizado usando a fachada PdfContentEditor em Aspose.PDF para Java.
---
## Remover todos os anexos

1. Vincule o PDF de origem à fachada `PdfContentEditor`.
2. Ligue para `deleteAttachments()` para remover todos os anexos incorporados.
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
