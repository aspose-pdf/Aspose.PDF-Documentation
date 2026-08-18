---
title: Substituir Texto Simples
linktitle: Substituir Texto Simples
type: docs
weight: 10
url: /java/replace-text-simple/
description: Aprenda como substituir texto em um documento PDF em Java usando a fachada PdfContentEditor em Aspose.PDF.
lastmod: "2026-06-09"
TechArticle: true
AlternativeHeadline: Substitua o texto em um PDF em Java
Abstract: Este artigo mostra como vincular um PDF, configurar o escopo de substituição de texto, substituir todas as ocorrências de texto correspondentes e salvar o documento atualizado usando a fachada PdfContentEditor em Aspose.PDF para Java.
---
## Substitua o texto em todo o documento

1. Vincule o PDF de origem à fachada `PdfContentEditor`.
2. Defina o escopo do texto de substituição como `ReplaceAll`.
3. Chame `replaceText(...)` com o texto de pesquisa e o texto de substituição.
4. Salve o documento PDF atualizado.

```java
public static void replaceTextSimple(Path inputFile, Path outputFile) {
    PdfContentEditor editor = new PdfContentEditor();
    try {
        editor.bindPdf(inputFile.toString());
        editor.getReplaceTextStrategy().setReplaceScope(ReplaceTextStrategy.Scope.ReplaceAll);
        editor.replaceText("33", "XXXIII ");
        editor.save(outputFile.toString());
    } finally {
        editor.close();
    }
}
```
