---
title: Alterar preferências do visualizador
linktitle: Alterar preferências do visualizador
type: docs
weight: 20
url: /java/change-viewer-preferences/
description: Aprenda como alterar as preferências do visualizador de um documento PDF em Java usando a fachada PdfContentEditor em Aspose.PDF.
lastmod: "2026-06-09"
TechArticle: true
AlternativeHeadline: Alterar as preferências do visualizador de PDF em Java
Abstract: Este artigo mostra como vincular um PDF, modificar o valor de preferência do visualizador atual e salvar o documento atualizado usando a fachada PdfContentEditor em Aspose.PDF para Java.
---
## Alterar a preferência do visualizador

1. Vincule o PDF de origem à fachada `PdfContentEditor`.
2. Leia o valor de preferência atual do visualizador.
3. Combine-o com o sinalizador adicional desejado e passe o resultado para `changeViewerPreference(...)`.
4. Salve o documento PDF atualizado.

```java
public static void changeViewerPreferences(Path inputFile, Path outputFile) {
    PdfContentEditor editor = new PdfContentEditor();
    try {
        editor.bindPdf(inputFile.toString());
        editor.changeViewerPreference(editor.getViewerPreference() | 1);
        editor.save(outputFile.toString());
    } finally {
        editor.close();
    }
}
```
