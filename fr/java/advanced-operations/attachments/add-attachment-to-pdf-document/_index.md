---
title: Ajouter des pièces jointes au PDF en Java
linktitle: Ajouter une pièce jointe à un document PDF
type: docs
weight: 10
url: /java/add-attachment-to-pdf-document/
description: Découvrez comment ajouter des pièces jointes à des documents PDF en Java à l'aide d'Aspose.PDF.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Ajouter des fichiers incorporés aux documents PDF avec Java
Abstract: Cet article montre comment joindre un fichier externe à un document PDF à l'aide d'Aspose.PDF pour Java. L'exemple ouvre un PDF existant, crée une FileSpecification pour la pièce jointe, l'ajoute à la collection EmbeddedFiles du document et enregistre le fichier mis à jour.
---
Pour joindre un fichier à un PDF, chargez le document source, créez un `FileSpecification`, ajoutez-le à la collection de fichiers incorporés et enregistrez le résultat.


## 
Ajouter une pièce jointe à un document PDF



Utilisez cet exemple lorsqu'un fichier externe doit être intégré dans un PDF existant.


1. 
Ouvrez le PDF source [Document] (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

1. 
Créez un [FileSpecification] (https://reference.aspose.com/pdf/java/com.aspose.pdf/filespecification/) pour le fichier que vous souhaitez intégrer.
1. Ajoutez la spécification du fichier à la collection `EmbeddedFiles` et enregistrez le document mis à jour.

```java
public static void addAttachments(Path inputFile, Path attachmentPath, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        FileSpecification fileSpecification = new FileSpecification(attachmentPath.toString(), "Sample text file");
        document.getEmbeddedFiles().add(attachmentPath.getFileName().toString(), fileSpecification);
        document.save(outputFile.toString());
    }
}
```
