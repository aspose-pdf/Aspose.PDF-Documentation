---
title: Action Ajouter un document
linktitle: Action Ajouter un document
type: docs
weight: 10
url: /java/add-document-action/
description: Découvrez comment ajouter une action d'ouverture de document à un PDF en Java à l'aide de la façade PdfContentEditor dans Aspose.PDF.
lastmod: "2026-06-09"
TechArticle: true
AlternativeHeadline: Ajouter une action d'ouverture de document à un PDF en Java
Abstract: Cet article montre comment lier un PDF, attacher une action JavaScript à l'événement d'ouverture de document et enregistrer le document mis à jour à l'aide de la façade PdfContentEditor dans Aspose.PDF pour Java.
---
## Ajouter une action d'ouverture de document


1. 
Liez le PDF source à la façade `PdfContentEditor`.

2. 
Appelez `addDocumentAdditionalAction(...)` avec l'événement `DOCUMENT_OPEN` et le texte de l'action JavaScript.

3. 
Enregistrez le document PDF mis à jour.

```java
public static void addDocumentAction(Path inputFile, Path outputFile) {
    PdfContentEditor editor = new PdfContentEditor();
    try {
        editor.bindPdf(inputFile.toString());
        editor.addDocumentAdditionalAction(PdfContentEditor.DOCUMENT_OPEN, "app.alert('Document opened with PdfContentEditor action');");
        editor.save(outputFile.toString());
    } finally {
        editor.close();
    }
}
```
