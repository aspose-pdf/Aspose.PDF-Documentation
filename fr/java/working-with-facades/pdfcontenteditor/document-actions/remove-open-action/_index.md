---
title: Supprimer l'action d'ouverture
linktitle: Supprimer l'action d'ouverture
type: docs
weight: 20
url: /java/remove-open-action/
description: Découvrez comment supprimer l'action d'ouverture de document d'un PDF en Java à l'aide de la façade PdfContentEditor dans Aspose.PDF.
lastmod: "2026-06-09"
TechArticle: true
AlternativeHeadline: Supprimer une action d'ouverture de document PDF en Java
Abstract: Cet article montre comment lier un PDF, supprimer l'action d'ouverture du document et enregistrer le document mis à jour à l'aide de la façade PdfContentEditor dans Aspose.PDF pour Java.
---
## Supprimer l'action d'ouverture du document


1. 
Liez le PDF source à la façade `PdfContentEditor`.

2. 
Appelez `removeDocumentOpenAction()`.

3. 
Enregistrez le document PDF mis à jour.

```java
public static void removeOpenAction(Path inputFile, Path outputFile) {
    PdfContentEditor editor = new PdfContentEditor();
    try {
        editor.bindPdf(inputFile.toString());
        editor.removeDocumentOpenAction();
        editor.save(outputFile.toString());
    } finally {
        editor.close();
    }
}
```
