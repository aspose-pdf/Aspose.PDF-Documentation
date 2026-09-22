---
title: Remplacer le texte avec une mise en forme personnalisée
linktitle: Remplacer le texte avec une mise en forme personnalisée
type: docs
weight: 20
url: /java/replace-text-with-state/
description: Découvrez comment remplacer le texte par une mise en forme personnalisée en Java à l'aide de la façade PdfContentEditor dans Aspose.PDF.
lastmod: "2026-09-22"
TechArticle: true
AlternativeHeadline: Remplacer le texte PDF par un formatage personnalisé en Java
Abstract: Cet article montre comment lier un PDF, configurer un TextState personnalisé, remplacer toutes les occurrences de texte correspondantes et enregistrer le document mis à jour à l'aide de la façade PdfContentEditor dans Aspose.PDF for Java.
---
## Remplacer le texte avec une mise en forme personnalisée

1. Liez le PDF source à la façade `PdfContentEditor`.

2. Créez et configurez un `TextState` avec la couleur et la taille de police requises.

3. Définissez la portée du remplacement de texte sur `ReplaceAll`.

4. Appelez `replaceText(...)` avec le texte de recherche, le texte de remplacement et `TextState` configuré.
5. Enregistrez le document PDF mis à jour.

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
