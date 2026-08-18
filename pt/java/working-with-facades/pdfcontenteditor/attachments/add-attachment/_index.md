---
title: Adicionar anexo
linktitle: Adicionar anexo
type: docs
weight: 10
url: /java/add-attachment/
description: Aprenda como anexar um arquivo externo a um documento PDF em Java usando a fachada PdfContentEditor em Aspose.PDF.
lastmod: "2026-06-09"
TechArticle: true
AlternativeHeadline: Adicione um anexo de arquivo a um PDF em Java
Abstract: Este artigo mostra como vincular um PDF, abrir um anexo como um fluxo, adicionar o anexo do documento com uma descrição e salvar o arquivo atualizado usando a fachada PdfContentEditor em Aspose.PDF para Java.
---
## Adicionar um anexo de documento

1. Vincule o PDF de origem à fachada `PdfContentEditor`.
2. Abra o arquivo anexo como um fluxo de entrada.
3. Chame `addDocumentAttachment(...)` com o fluxo, nome do arquivo e descrição.
4. Salve o documento PDF atualizado.

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
