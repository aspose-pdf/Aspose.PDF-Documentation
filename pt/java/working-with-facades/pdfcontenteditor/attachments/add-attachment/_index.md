---
title: Adicionar Anexo
linktitle: Adicionar Anexo
type: docs
weight: 10
url: /pt/java/add-attachment/
description: Saiba como anexar um arquivo externo a um documento PDF em Java usando a fachada PdfContentEditor no Aspose.PDF.
lastmod: "2026-10-06"
TechArticle: true
AlternativeHeadline: Adicionar um anexo de arquivo a um PDF em Java
Abstract: Este artigo mostra como vincular um PDF, abrir um anexo como fluxo, adicionar o anexo do documento com uma descrição e salvar o arquivo atualizado usando a fachada PdfContentEditor no Aspose.PDF for Java.
---
## Adicionar um anexo de documento

1. Vincular o PDF de origem ao `PdfContentEditor` fachada.
2. Abra o arquivo de anexo como um fluxo de entrada.
3. Chamar `addDocumentAttachment(...)` com o fluxo, nome do arquivo e descrição.
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
