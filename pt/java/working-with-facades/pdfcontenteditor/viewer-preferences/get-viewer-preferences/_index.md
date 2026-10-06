---
title: Obter Preferências do Visualizador
linktitle: Obter Preferências do Visualizador
type: docs
weight: 10
url: /pt/java/get-viewer-preferences/
description: Aprenda como ler as preferências do visualizador de um documento PDF em Java usando a fachada PdfContentEditor no Aspose.PDF.
lastmod: "2026-10-06"
TechArticle: true
AlternativeHeadline: Ler preferências do visualizador de PDF em Java
Abstract: Este artigo mostra como vincular um PDF e imprimir o valor atual da preferência do visualizador usando a fachada PdfContentEditor no Aspose.PDF para Java.
---
## Obter a preferência atual do visualizador

1. Vincule o PDF de origem ao `PdfContentEditor` fachada.
2. Chamar `getViewerPreference()` para ler o valor atual.
3. Inspecione ou imprima a bandeira de preferência retornada.

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
