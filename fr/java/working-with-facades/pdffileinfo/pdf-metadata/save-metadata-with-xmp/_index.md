---
title: Enregistrer les métadonnées avec XMP
linktitle: Enregistrer les métadonnées avec XMP
type: docs
weight: 30
url: /java/save-metadata-with-xmp/
description: Découvrez comment enregistrer les métadonnées PDF avec XMP en Java avec la façade PdfFileInfo.
lastmod: "2026-06-09"
draft: false
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Enregistrement des métadonnées PDF avec XMP à l'aide d'Aspose.PDF pour Java
Abstract: Découvrez comment enregistrer des métadonnées PDF avec XMP à l'aide d'Aspose.PDF pour Java. L'exemple Java met à jour les champs de métadonnées principaux avec PdfFileInfo et les réécrit en utilisant `saveNewInfoWithXmp()` afin que le document de sortie stocke les informations sous forme XMP.
---
## Enregistrer les métadonnées avec XMP



Utilisez ce flux de travail lorsque vous avez besoin que les informations mises à jour du document soient stockées au format XMP.


### 
Étapes


1. 
Créez un objet `PdfFileInfo` pour le PDF source.

2. 
Définissez les champs de métadonnées que vous souhaitez mettre à jour, tels que le sujet, le titre, les mots-clés et le créateur.
3. Appelez `saveNewInfoWithXmp()` avec le chemin du fichier de sortie.

4. 
Fermez l'instance `PdfFileInfo`.


### 
Exemple Java

```java
public static void saveInfoWithXmp(Path inputFile, Path outputFile) {
    PdfFileInfo pdfInfo = new PdfFileInfo(inputFile.toString());
    pdfInfo.setSubject("Aspose PDF for Java");
    pdfInfo.setTitle("Aspose PDF for Java");
    pdfInfo.setKeywords("Aspose, PDF, Java");
    pdfInfo.setCreator("Aspose Team");
    pdfInfo.saveNewInfoWithXmp(outputFile.toString());
    pdfInfo.close();
}
```
