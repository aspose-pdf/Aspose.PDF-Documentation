---
title: Alterar Preferências do Visualizador
linktitle: Alterar Preferências do Visualizador
type: docs
weight: 20
url: /pt/java/change-viewer-preferences/
description: Saiba como alterar as preferências de exibição de um documento PDF em Java usando a fachada `PdfContentEditor` no Aspose.PDF.
lastmod: "2026-10-06"
TechArticle: true
AlternativeHeadline: Alterar preferências de exibição de PDF em Java
Abstract: Este artigo mostra como vincular um PDF, modificar o valor da preferência de exibição atual e salvar o documento atualizado usando a fachada `PdfContentEditor` no Aspose.PDF for Java.
---
## Alterar a preferência de exibição

1. Vincule o PDF de origem ao `PdfContentEditor` fachada.
2. Leia o valor atual da preferência do visualizador.
3. Combine-o com a flag adicional desejada e passe o resultado para `changeViewerPreference(...)`.
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
