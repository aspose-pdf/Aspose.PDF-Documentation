---
title: Définir les métadonnées PDF
linktitle: Définir les métadonnées PDF
type: docs
weight: 50
url: /java/set-pdf-metadata/
description: Découvrez comment mettre à jour les métadonnées PDF en Java avec la façade PdfFileInfo.
lastmod: "2026-06-09"
draft: false
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Mise à jour des métadonnées PDF à l'aide d'Aspose.PDF pour Java
Abstract: Découvrez comment mettre à jour les métadonnées PDF avec Aspose.PDF pour Java. L'exemple Java utilise PdfFileInfo pour définir des champs de métadonnées standard tels que le sujet, le titre, les mots-clés et le créateur, ajoute une entrée de métadonnées personnalisée et enregistre le résultat dans un nouveau PDF.
---
## Définir les métadonnées PDF



Utilisez ce flux de travail lorsque vous devez normaliser ou enrichir les informations du document avant d'enregistrer le PDF.


### 
Étapes


1. 
Créez un objet `PdfFileInfo` pour le PDF source.

2. 
Définissez les champs de métadonnées standard que vous souhaitez mettre à jour.
3. Ajoutez des métadonnées personnalisées avec `setMetaInfo`.

4. 
Enregistrez le document mis à jour avec `save()`.

5. 
Fermez l'instance `PdfFileInfo`.


### 
Exemple Java

```java
public static void setPdfMetadata(Path inputFile, Path outputFile) {
    PdfFileInfo pdfInfo = new PdfFileInfo(inputFile.toString());
    pdfInfo.setSubject("Aspose PDF for Java");
    pdfInfo.setTitle("Aspose PDF for Java");
    pdfInfo.setKeywords("Aspose, PDF, Java");
    pdfInfo.setCreator("Aspose Team");
    pdfInfo.setMetaInfo("CustomKey", "CustomValue");
    pdfInfo.save(outputFile.toString());
    pdfInfo.close();
}
```
