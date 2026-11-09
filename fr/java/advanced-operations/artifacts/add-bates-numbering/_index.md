---
title: Ajouter la numérotation Bates au PDF en Java
linktitle: Ajouter la numérotation Bates
type: docs
weight: 10
url: /fr/java/add-bates-numbering/
description: Ajouter des identifiants Bates séquentiels aux pages PDF en Java à l'aide de l'assistant dédié à la numérotation Bates ou de l'API générique de pagination.
lastmod: "2026-11-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Ajouter la numérotation Bates en Java
Abstract: Ajouter des identifiants Bates séquentiels aux pages PDF en Java à l'aide de l'assistant dédié à la numérotation Bates ou de l'API générique de pagination.
---
Les artefacts de numérotation Bates sont utiles dans les flux de travail juridiques, d'archivage et de gestion de documents où chaque page nécessite un identifiant persistant au niveau de la page.

## Ajouter la numérotation Bates avec l'assistant dédié

Utilisez cet exemple lorsque vous souhaitez appliquer la numérotation Bates via l'assistant dédié de collecte de pages.

1. Ouvrez le PDF source avec [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) et ajoutez toutes les pages supplémentaires requises par l'exemple.
1. Configurez un objet [BatesNArtifact](https://reference.aspose.com/pdf/java/com.aspose.pdf/batesnartifact/).
1. Appliquez la numérotation Bates à la collection de pages et enregistrez le fichier de sortie.

```java
public static void addBatesNArtifact(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        for (int i = 0; i < 2; i++) {
            document.getPages().add();
        }

        BatesNArtifact batesArtifact = createBatesArtifact();
        PageCollectionExtensions.addBatesNumbering(document.getPages(), batesArtifact);
        document.save(outputFile.toString());
    }
}
```

## Ajouter la numérotation Bates via des artefacts de pagination

Cet exemple applique la numérotation Bates en passant l'artefact Bates à travers l'API générique de pagination.

1. Ouvrez le PDF source avec [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) et ajoutez les pages requises.
1. Créez le [BatesNArtifact](https://reference.aspose.com/pdf/java/com.aspose.pdf/batesnartifact/) et ajoutez-le à une liste d’artefacts de pagination.
1. Appliquez les artefacts de pagination à la collection de pages et enregistrez le document.

```java
public static void addBatesNArtifactPagination(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        for (int i = 0; i < 2; i++) {
            document.getPages().add();
        }

        BatesNArtifact batesArtifact = createBatesArtifact();
        List<PaginationArtifact> paginationArtifacts = new ArrayList<>();
        paginationArtifacts.add(batesArtifact);
        PageCollectionExtensions.addPagination(document.getPages(), paginationArtifacts);
        document.save(outputFile.toString());
    }
}
```

## Rubriques connexes

- [Supprimer la numérotation Bates](/pdf/fr/java/remove-bates-numbering/)
- [Travailler avec les artefacts PDF en Java](/pdf/fr/java/artifacts/)
