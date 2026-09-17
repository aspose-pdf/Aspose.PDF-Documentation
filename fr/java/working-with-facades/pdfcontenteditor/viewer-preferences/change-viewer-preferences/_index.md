---
title: Modifier les préférences de la visionneuse
linktitle: Modifier les préférences de la visionneuse
type: docs
weight: 20
url: /java/change-viewer-preferences/
description: Découvrez comment modifier les préférences de visualisation d'un document PDF en Java à l'aide de la façade PdfContentEditor dans Aspose.PDF.
lastmod: "2026-06-09"
TechArticle: true
AlternativeHeadline: Modifier les préférences de la visionneuse PDF en Java
Abstract: Cet article montre comment lier un PDF, modifier la valeur de préférence actuelle de la visionneuse et enregistrer le document mis à jour à l'aide de la façade PdfContentEditor dans Aspose.PDF pour Java.
---
## Modifier les préférences du spectateur


1. 
Liez le PDF source à la façade `PdfContentEditor`.

2. 
Lisez la valeur actuelle des préférences du spectateur.

3. 
Combinez-le avec l'indicateur supplémentaire souhaité et transmettez le résultat à `changeViewerPreference(...)`.

4. 
Enregistrez le document PDF mis à jour.

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
