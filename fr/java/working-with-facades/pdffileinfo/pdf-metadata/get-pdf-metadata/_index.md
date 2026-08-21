---
title: Obtenir des métadonnées PDF
linktitle: Obtenir des métadonnées PDF
type: docs
weight: 20
url: /java/get-pdf-metadata/
description: Apprenez à lire les métadonnées PDF en Java avec la façade PdfFileInfo.
lastmod: "2026-06-09"
draft: false
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Récupération de métadonnées PDF à l'aide d'Aspose.PDF pour Java.
Abstract: Découvrez comment récupérer des métadonnées PDF avec Aspose.PDF pour Java. L'exemple Java lit les champs standard tels que le sujet, le titre, les mots-clés, le créateur, la date de création et la date de modification, ainsi que les indicateurs d'état du fichier et une entrée de métadonnées personnalisée `Reviewer`.
---
## Obtenir les métadonnées PDF



Cet exemple lit les informations de document standard, les indicateurs d'état de fichier et une clé de métadonnées personnalisée.


### 
Étapes


1. 
Créez un objet `PdfFileInfo` pour le PDF source.

2. 
Lisez les champs de métadonnées standard tels que le sujet, le titre, les mots-clés et le créateur.
3. Inspectez les indicateurs d’état du fichier, par exemple si le fichier est valide, crypté, protégé par mot de passe ou s’il s’agit d’un portefeuille.

4. 
Lisez une valeur de métadonnées personnalisée avec `getMetaInfo`.

5. 
Fermez l'instance `PdfFileInfo`.


### 
Exemple Java

```java
public static void getPdfMetadata(Path inputFile) {
    PdfFileInfo pdfInfo = new PdfFileInfo(inputFile.toString());
    System.out.println("Subject: " + pdfInfo.getSubject());
    System.out.println("Title: " + pdfInfo.getTitle());
    System.out.println("Keywords: " + pdfInfo.getKeywords());
    System.out.println("Creator: " + pdfInfo.getCreator());
    System.out.println("Creation Date: " + pdfInfo.getCreationDate());
    System.out.println("Modification Date: " + pdfInfo.getModDate());
    System.out.println("Is Valid PDF: " + pdfInfo.isPdfFile());
    System.out.println("Is Encrypted: " + pdfInfo.isEncrypted());
    System.out.println("Has Open Password: " + pdfInfo.hasOpenPassword());
    System.out.println("Has Edit Password: " + pdfInfo.hasEditPassword());
    System.out.println("Is Portfolio: " + pdfInfo.hasCollection());
    String reviewer = pdfInfo.getMetaInfo("Reviewer");
    System.out.println("Reviewer: " + (reviewer == null || reviewer.isBlank() ? "No Reviewer metadata found." : reviewer));
    pdfInfo.close();
}
```
