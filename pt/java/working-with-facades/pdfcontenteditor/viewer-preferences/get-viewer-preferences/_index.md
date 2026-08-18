---
title: Obtenha preferências do visualizador
linktitle: Obtenha preferências do visualizador
type: docs
weight: 10
url: /java/get-viewer-preferences/
description: Aprenda como ler as preferências do visualizador de um documento PDF em Java usando a fachada PdfContentEditor em Aspose.PDF.
lastmod: "2026-06-09"
TechArticle: true
AlternativeHeadline: Leia as preferências do visualizador de PDF em Java
Abstract: Este artigo mostra como vincular um PDF e imprimir o valor de preferência do visualizador atual usando a fachada PdfContentEditor em Aspose.PDF para Java.
---
## Obtenha a preferência atual do visualizador

1. Vincule o PDF de origem à fachada `PdfContentEditor`.
2. Chame `getViewerPreference()` para ler o valor atual.
3. Inspecione ou imprima o sinalizador de preferência retornado.

```java
public static void getViewerPreferences(Path inputFile) {
    PdfContentEditor editor = new PdfContentEditor();
    try {
        editor.bindPdf(inputFile.toString());
        System.out.println("Current viewer preference: " + editor.getViewerPreference());
    } finally {
        editor.close();
    }
}
```
