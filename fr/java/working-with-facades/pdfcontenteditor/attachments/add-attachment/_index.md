---
title: Ajouter une pièce jointe
linktitle: Ajouter une pièce jointe
type: docs
weight: 10
url: /java/add-attachment/
description: Découvrez comment joindre un fichier externe à un document PDF en Java à l'aide de la façade PdfContentEditor dans Aspose.PDF.
lastmod: "2026-06-09"
TechArticle: true
AlternativeHeadline: Ajouter une pièce jointe à un PDF en Java
Abstract: Cet article montre comment lier un PDF, ouvrir une pièce jointe sous forme de flux, ajouter la pièce jointe au document avec une description et enregistrer le fichier mis à jour à l'aide de la façade PdfContentEditor dans Aspose.PDF pour Java.
---
## Ajouter une pièce jointe à un document


1. 
Liez le PDF source à la façade `PdfContentEditor`.

2. 
Ouvrez le fichier joint en tant que flux d'entrée.

3. 
Appelez `addDocumentAttachment(...)` avec le flux, le nom du fichier et la description.

4. 
Enregistrez le document PDF mis à jour.

```java
public static void addAttachment(Path inputFile, Path attachmentFile, Path outputFile) throws Exception {
    PdfContentEditor editor = new PdfContentEditor();
    try (InputStream attachmentStream = Files.newInputStream(attachmentFile)) {
        editor.bindPdf(inputFile.toString());
        editor.addDocumentAttachment(attachmentStream, attachmentFile.getFileName().toString(), "Sample attachment.");
        editor.save(outputFile.toString());
    } finally {
        editor.close();
    }
}
```
