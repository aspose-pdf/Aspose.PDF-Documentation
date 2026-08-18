---
title: Substituir texto por estado
linktitle: Substituir texto por estado
type: docs
weight: 20
url: /java/replace-text-with-state/
description: Aprenda como substituir texto por formatação personalizada em Java usando a fachada PdfContentEditor em Aspose.PDF.
lastmod: "2026-06-09"
TechArticle: true
AlternativeHeadline: Substitua o texto do PDF por formatação personalizada em Java
Abstract: Este artigo mostra como vincular um PDF, configurar um TextState personalizado, substituir todas as ocorrências de texto correspondentes e salvar o documento atualizado usando a fachada PdfContentEditor em Aspose.PDF para Java.
---
## Substitua o texto por um estado de texto personalizado

1. Vincule o PDF de origem à fachada `PdfContentEditor`.
2. Crie e configure um `TextState` com a cor e tamanho de fonte necessários.
3. Defina o escopo do texto de substituição como `ReplaceAll`.
4. Chame `replaceText(...)` com o texto de pesquisa, texto de substituição e `TextState` configurado.
5. Salve o documento PDF atualizado.

```java
public static void replaceTextWithState(Path inputFile, Path outputFile) {
    PdfContentEditor editor = new PdfContentEditor();
    try {
        editor.bindPdf(inputFile.toString());
        TextState textState = new TextState();
        textState.setForegroundColor(com.aspose.pdf.Color.getBlue());
        textState.setFontSize(14);
        editor.getReplaceTextStrategy().setReplaceScope(ReplaceTextStrategy.Scope.ReplaceAll);
        editor.replaceText("software", "SOFTWARE", textState);
        editor.save(outputFile.toString());
    } finally {
        editor.close();
    }
}
```
