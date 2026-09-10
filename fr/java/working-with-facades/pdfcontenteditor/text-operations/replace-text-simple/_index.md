---
title: Remplacer le texte simple
linktitle: Remplacer le texte simple
type: docs
weight: 10
url: /java/replace-text-simple/
description: Découvrez comment remplacer du texte dans un document PDF en Java à l'aide de la façade PdfContentEditor dans Aspose.PDF.
lastmod: "2026-06-09"
TechArticle: true
AlternativeHeadline: Remplacer le texte dans un PDF en Java
Abstract: Cet article montre comment lier un PDF, configurer la portée du texte de remplacement, remplacer toutes les occurrences de texte correspondantes et enregistrer le document mis à jour à l'aide de la façade PdfContentEditor dans Aspose.PDF pour Java.
---
## Remplacer le texte dans tout le document


1. 
Liez le PDF source à la façade `PdfContentEditor`.

2. 
Définissez la portée du texte de remplacement sur `ReplaceAll`.

3. 
Appelez `replaceText(...)` avec le texte de recherche et le texte de remplacement.

4. 
Enregistrez le document PDF mis à jour.

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
