---
title: Supprimer la numérotation Bates du PDF en Java
linktitle: Supprimer la numérotation Bates
type: docs
weight: 100
url: /fr/java/remove-bates-numbering/
description: Supprimer la numérotation Bates de toutes les pages d'un PDF en Java.
lastmod: "2026-11-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Supprimer la numérotation Bates en Java
Abstract: Supprimer la numérotation Bates de toutes les pages d'un PDF en Java.
---
Supprimer la numérotation Bates de toutes les pages d'un PDF en Java.

## Supprimer la numérotation Bates

Utilisez cette approche lorsque les artefacts de numérotation Bates existants doivent être supprimés du document.

1. Ouvrez le PDF source avec [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Appelez l'assistant de collection de pages qui supprime la numérotation Bates.
1. Enregistrez le fichier de sortie nettoyé.

```java
public static void deleteBatesNumbering(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        PageCollectionExtensions.deleteBatesNumbering(document.getPages());
        document.save(outputFile.toString());
    }
}
```

## Rubriques connexes

- [Ajouter la numérotation Bates](/pdf/fr/java/add-bates-numbering/)
- [Travailler avec les artefacts PDF en Java](/pdf/fr/java/artifacts/)
