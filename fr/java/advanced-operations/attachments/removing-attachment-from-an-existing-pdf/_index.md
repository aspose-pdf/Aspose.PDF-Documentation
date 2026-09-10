---
title: Supprimer les pièces jointes d'un PDF en Java
linktitle: Supprimer une pièce jointe d'un PDF existant
type: docs
weight: 30
url: /java/removing-attachment-from-an-existing-pdf/
description: Découvrez comment supprimer une ou toutes les pièces jointes intégrées des documents PDF en Java à l'aide d'Aspose.PDF.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Supprimer les pièces jointes PDF par programme avec Java
Abstract: Cet article montre comment supprimer les pièces jointes des fichiers PDF à l'aide d'Aspose.PDF pour Java. Les exemples montrent la suppression d'un fichier incorporé par clé et l'effacement de l'intégralité de la collection EmbeddedFiles avant d'enregistrer le document mis à jour.
---
Les pièces jointes stockées dans un document PDF peuvent être supprimées individuellement ou en une seule fois via la collection `EmbeddedFiles`.


## 
Supprimer une seule pièce jointe



Utilisez cet exemple lorsqu'un fichier incorporé nommé doit être supprimé du PDF.


1. 
Ouvrez le PDF source [Document] (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

1. 
Supprimez la pièce jointe par sa clé de la collection de fichiers intégrés.
1. Enregistrez le document de sortie mis à jour.


```java
public static void removeAttachment(Path inputFile, String attachmentName, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        document.getEmbeddedFiles().deleteByKey(attachmentName);
        document.save(outputFile.toString());
    }
}
```

## 
Supprimer toutes les pièces jointes



Utilisez cette approche lorsque la totalité de la collection de fichiers incorporés doit être effacée.


1. 
Ouvrez le PDF source [Document] (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

1. 
Supprimez tous les éléments de la collection de fichiers incorporés.
1. Enregistrez le document de sortie nettoyé.

```java
public static void removeAllAttachments(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        document.getEmbeddedFiles().delete();
        document.save(outputFile.toString());
    }
}
```
