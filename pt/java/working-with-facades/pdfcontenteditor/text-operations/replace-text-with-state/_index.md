---
title: Substituir texto com Estado
linktitle: Substituir texto com Estado
type: docs
weight: 20
url: /pt/java/replace-text-with-state/
description: Saiba como substituir texto com formatação personalizada em Java usando a fachada `PdfContentEditor` no Aspose.PDF.
lastmod: "2026-10-06"
TechArticle: true
AlternativeHeadline: Substituir texto PDF com formatação personalizada em Java
Abstract: Este artigo mostra como vincular um PDF, configurar um TextState personalizado, substituir todas as ocorrências de texto correspondentes e salvar o documento atualizado usando a fachada `PdfContentEditor` no Aspose.PDF for Java.
---
## Substituir texto com um estado de texto personalizado

1. Vincule o PDF de origem à fachada `PdfContentEditor`.
2. Crie e configure um `TextState` com a cor e o tamanho de fonte necessários.
3. Defina o escopo de substituição de texto para `ReplaceAll`.
4. Chame `replaceText(...)` com o texto de pesquisa, texto de substituição e configurado `TextState`.
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
