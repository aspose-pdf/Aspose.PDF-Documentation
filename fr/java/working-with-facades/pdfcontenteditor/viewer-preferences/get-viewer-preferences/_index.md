---
title: Obtenir les préférences de la visionneuse
linktitle: Obtenir les préférences de la visionneuse
type: docs
weight: 10
url: /java/get-viewer-preferences/
description: Découvrez comment lire les préférences de visualisation d'un document PDF en Java à l'aide de la façade PdfContentEditor dans Aspose.PDF.
lastmod: "2026-09-23"
TechArticle: true
AlternativeHeadline: Lire les préférences de la visionneuse PDF en Java
Abstract: Cet article montre comment lier un PDF et afficher la valeur de préférence actuelle de la visionneuse à l'aide de la façade PdfContentEditor dans Aspose.PDF for Java.
---
## Obtenir les préférences actuelles de la visionneuse

1. Liez le PDF source à la façade `PdfContentEditor`.
2. Appelez `getViewerPreference()` pour lire la valeur actuelle.
3. Inspectez ou affichez l’indicateur de préférence renvoyé.

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
