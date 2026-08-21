---
title: Remplacer le texte par l'état
linktitle: Remplacer le texte par l'état
type: docs
weight: 20
url: /java/replace-text-with-state/
description: Découvrez comment remplacer le texte par une mise en forme personnalisée en Java à l'aide de la façade PdfContentEditor dans Aspose.PDF.
lastmod: "2026-06-09"
TechArticle: true
AlternativeHeadline: Remplacer le texte PDF par un formatage personnalisé en Java
Abstract: Cet article montre comment lier un PDF, configurer un TextState personnalisé, remplacer toutes les occurrences de texte correspondantes et enregistrer le document mis à jour à l'aide de la façade PdfContentEditor dans Aspose.PDF pour Java.
---
## Remplacer le texte par un état de texte personnalisé


1. 
Liez le PDF source à la façade `PdfContentEditor`.

2. 
Créez et configurez un `TextState` avec la couleur et la taille de police requises.

3. 
Définissez la portée du texte de remplacement sur `ReplaceAll`.

4. 
Appelez `replaceText(...)` avec le texte de recherche, le texte de remplacement et `TextState` configuré.
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
