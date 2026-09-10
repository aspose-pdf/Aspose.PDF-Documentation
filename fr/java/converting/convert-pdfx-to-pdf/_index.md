---
title: Convertir PDF/A et PDF/UA en PDF en Java
linktitle: Convertir PDF/A et PDF/UA en PDF
type: docs
weight: 120
url: /java/convert-pdf_x-to-pdf/
lastmod: "2026-06-16"
description: Découvrez comment supprimer la conformité PDF/A et PDF/UA des fichiers PDF basés sur des normes en Java et les enregistrer en tant que documents PDF standard.
sitemap:
    changefreq: "monthly"
    priority: 0.8
TechArticle: true
AlternativeHeadline: Comment convertir PDF/A et PDF/UA en PDF standard en Java
Abstract: Cet article explique comment supprimer la conformité PDF/A et PDF/UA des documents PDF basés sur des normes à l'aide d'Aspose.PDF pour Java, puis enregistrer le résultat sous forme de fichier PDF standard.
---
Aspose.PDF pour Java peut reconvertir les variantes PDF conformes aux normes en un document PDF standard.


## 
Convertir un PDF/A en PDF standard



Utilisez cet exemple lorsqu'un document d'archive PDF/A doit être rétrogradé en PDF standard.


1. 
Ouvrez le fichier PDF/A source dans une instance [`Document`] (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

1. 
Appelez `removePdfaCompliance()` pour détacher le profil de conformité d'archivage du document chargé.
1. Enregistrez le fichier PDF standard résultant sans le jeu de restrictions PDF/A.


```java
public static void convertPdfAToPdf(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        document.removePdfaCompliance();
        document.save(outputFile.toString());
    }
}
```

## 
Convertir PDF/UA en PDF standard



Utilisez cet exemple lorsqu'un document PDF/UA accessible doit être reconverti en PDF standard.


1. 
Ouvrez le fichier PDF/UA source dans une instance [`Document`] (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

1. 
Appelez `removePdfUaCompliance()` pour supprimer le profil de conformité d’accessibilité des métadonnées et des exigences de structure du document.
1. Enregistrez le document PDF obtenu en tant que fichier PDF standard.

```java
public static void convertPdfUaToPdf(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        document.removePdfUaCompliance();
        document.save(outputFile.toString());
    }
}
```
