---
title: Fusionner des fichiers PDF en Java
linktitle: Fusionner des fichiers PDF
type: docs
weight: 50
url: /java/merge-pdf/
description: Découvrez comment fusionner plusieurs fichiers PDF en un seul document en Java à l'aide d'Aspose.PDF.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Combinez des pages PDF à l'aide de Java
Abstract: Cet article explique comment fusionner deux documents PDF en Java à l'aide d'Aspose.PDF. L'exemple ouvre deux documents sources, ajoute les pages du deuxième document au premier et enregistre le résultat fusionné en tant que nouveau fichier PDF.
---
La fusion de fichiers PDF est utile lorsque vous devez combiner des documents associés en un seul fichier à des fins de distribution, d'archivage ou de traitement.


## 
Exemple en direct



[Aspose.PDF Merger] (https://products.aspose.app/pdf/merger) est une application en ligne gratuite permettant de tester la fusion de PDF dans un navigateur.



Cette rubrique montre comment fusionner plusieurs fichiers PDF en un seul document en Java :


1. 
Ouvrez les deux documents sources avec le constructeur [Document] (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Ajoutez la collection [Page] (https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) du deuxième [Document] (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) au premier avec `document1.getPages().add(document2.getPages())`.

1. 
Enregistrez le [Document] fusionné (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) dans le chemin de sortie.


## 
Fusionner deux documents PDF



L'exemple Java suivant est basé sur `MergeDocumentExamples.java`.

```java
public static void mergeTwoDocuments(Path inputFile1, Path inputFile2, Path outputFile) {
    try (Document document1 = new Document(inputFile1.toString());
         Document document2 = new Document(inputFile2.toString())) {
        document1.getPages().add(document2.getPages());
        document1.save(outputFile.toString());
    }
}
```
