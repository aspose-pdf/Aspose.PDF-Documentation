---
title: Ajouter la numérotation Bates au PDF en Java
linktitle: Ajout d'une numérotation Bates
type: docs
weight: 10
url: /java/add-bates-numbering/
description: Découvrez comment ajouter et supprimer la numérotation Bates dans les documents PDF à l'aide de Java avec Aspose.PDF.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Ajouter la numérotation Bates via Java
Abstract: Cet article explique comment créer et supprimer des artefacts de numérotation Bates dans des documents PDF à l'aide d'Aspose.PDF pour Java. Il couvre la configuration d'un `BatesNArtifact`, son application via les assistants de numérotation Bates ou les assistants de pagination génériques, et la suppression de la numérotation Bates d'un document.
---
Les artefacts de numérotation Bates sont utiles dans les flux de travail juridiques, d'archivage et de contrôle de documents où chaque page nécessite un identifiant persistant au niveau de la page.


## 
Ajoutez la numérotation Bates avec l'assistant dédié



Utilisez cet exemple lorsque vous souhaitez appliquer la numérotation Bates via l'assistant de collecte de pages dédié.


1. 
Ouvrez le PDF source [Document] (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) et ajoutez toutes les pages supplémentaires requises par l'échantillon.

1. 
Créez la configuration [BatesNArtifact] (https://reference.aspose.com/pdf/java/com.aspose.pdf/batesnartifact/).
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

## 
Ajouter une numérotation Bates via des artefacts de pagination



Cet exemple applique la numérotation Bates en transmettant l'artefact Bates via l'API de pagination générique.


1. 
Ouvrez le PDF source [Document] (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) et ajoutez les pages requises.

1. 
Créez le [BatesNArtifact] (https://reference.aspose.com/pdf/java/com.aspose.pdf/batesnartifact/) et ajoutez-le à une liste d'artefacts de pagination.
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

## 
Supprimer la numérotation Bates



Utilisez cette approche lorsque les artefacts de numérotation Bates existants doivent être supprimés du document.


1. 
Ouvrez le PDF source [Document] (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

1. 
Appelez l'assistant de collecte de pages qui supprime la numérotation Bates.
1. Enregistrez le fichier de sortie nettoyé.

```java
public static void deleteBatesNumbering(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        PageCollectionExtensions.deleteBatesNumbering(document.getPages());
        document.save(outputFile.toString());
    }
}
```
