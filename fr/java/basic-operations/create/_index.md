---
title: Créer un document PDF par programmation
linktitle: Créer un PDF
type: docs
weight: 10
url: /java/create-document/
description: Découvrez comment créer un document PDF à partir de zéro en Java à l'aide d'Aspose.PDF.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Générer des fichiers PDF avec Aspose.PDF pour Java
Abstract: Cet article montre comment créer un fichier PDF en Java à l'aide d'Aspose.PDF. L'exemple crée un nouvel objet Document, ajoute une page, insère un TextFragment avec un exemple de texte et enregistre le résultat sous forme de fichier PDF.
---
La création de fichiers PDF dans le code est une exigence courante pour les rapports, les factures et les documents commerciaux générés. Aspose.PDF pour Java fournit un moyen direct de créer un document à partir de zéro.


## 
Comment créer un fichier PDF en Java



Pour créer un document PDF par programmation :


1. 
Créez un objet [Document] (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

1. 
Ajoutez une [Page] (https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) au document.
1. Ajoutez un [TextFragment] (https://reference.aspose.com/pdf/java/com.aspose.pdf/textfragment/) aux paragraphes de la page.

1. 
Enregistrez le [Document] (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) dans un fichier de sortie.


## 
Créer un simple document PDF



L'exemple Java suivant est basé sur `CreatePdfDocumentExamples.java`.

```java
public static void createNewDocument(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();
        page.getParagraphs().add(new TextFragment("Hello World!"));
        document.save(outputFile.toString());
    }
}
```
