---
title: Supprimer les pièces jointes
linktitle: Supprimer les pièces jointes
type: docs
weight: 50
url: /java/remove-attachments/
description: Découvrez comment supprimer toutes les pièces jointes d'un document PDF en Java à l'aide de la façade PdfContentEditor dans Aspose.PDF.
lastmod: "2026-06-09"
TechArticle: true
AlternativeHeadline: Supprimer toutes les pièces jointes PDF en Java
Abstract: Cet article montre comment lier un PDF, supprimer toutes les pièces jointes du document et enregistrer le fichier mis à jour à l'aide de la façade PdfContentEditor dans Aspose.PDF pour Java.
---
## Supprimer toutes les pièces jointes


1. 
Liez le PDF source à la façade `PdfContentEditor`.

2. 
Appelez `deleteAttachments()` pour supprimer toutes les pièces jointes intégrées.

3. 
Enregistrez le document PDF mis à jour.

```java
public static void removeAttachments(Path inputFile, Path outputFile) {
    PdfContentEditor editor = new PdfContentEditor();
    try {
        editor.bindPdf(inputFile.toString());
        editor.deleteAttachments();
        editor.save(outputFile.toString());
    } finally {
        editor.close();
    }
}
```
