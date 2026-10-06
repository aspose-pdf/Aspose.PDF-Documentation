---
title: Substituir Texto Simples
linktitle: Substituir Texto Simples
type: docs
weight: 10
url: /pt/java/replace-text-simple/
description: Saiba como substituir texto em todo um documento PDF em Java usando a fachada PdfContentEditor no Aspose.PDF.
lastmod: "2026-10-06"
TechArticle: true
AlternativeHeadline: Substituir texto em um PDF em Java
Abstract: Este artigo mostra como vincular um PDF, configurar o escopo de substituição de texto, substituir todas as ocorrências de texto correspondentes e salvar o documento atualizado usando a fachada PdfContentEditor no Aspose.PDF for Java.
---
## Substituir texto em todo o documento

1. Vincule o PDF de origem ao `PdfContentEditor` fachada.
2. Defina o escopo de substituição de texto para `ReplaceAll`.
3. Chamar `replaceText(...)` com o texto de pesquisa e o texto de substituição.
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
