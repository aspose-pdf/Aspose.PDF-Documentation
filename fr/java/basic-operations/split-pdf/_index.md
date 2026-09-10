---
title: Diviser des fichiers PDF en Java
linktitle: Diviser des fichiers PDF
type: docs
weight: 60
url: /java/split-pdf/
description: Découvrez comment diviser un PDF en fichiers PDF d'une seule page en Java à l'aide d'Aspose.PDF.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Fractionner des pages PDF à l'aide de Java
Abstract: Cet article montre comment diviser un document PDF en fichiers PDF distincts d'une seule page en Java à l'aide d'Aspose.PDF. L'exemple ouvre le document source, parcourt ses pages, crée un nouveau document pour chaque page et enregistre chaque page en tant que fichier PDF individuel.
---
Diviser un PDF en fichiers distincts est utile lorsque vous devez exporter chaque page à des fins de révision, de stockage ou de traitement en aval.


## 
Exemple en direct



[Aspose.PDF Splitter] (https://products.aspose.app/pdf/splitter) est une application en ligne gratuite permettant de tester le fractionnement de PDF dans un navigateur.



[![Aspose Split PDF] (splitter.png)] (https://products.aspose.app/pdf/splitter)



Cet exemple utilise la classe [Document] (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) pour ouvrir un fichier PDF et parcourir ses pages. Pour chaque [Page] (https://reference.aspose.com/pdf/java/com.aspose.pdf/page/), il crée un nouveau document, y ajoute la page et enregistre le résultat dans un fichier PDF distinct.

Pour diviser un PDF en fichiers de pages individuelles en Java :


1. 
Ouvrez le PDF source avec le constructeur [Document] (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

1. 
Parcourez les objets [Page] (https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) renvoyés par `document.getPages()`.

1. 
Créez un nouveau [Document] (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) vide pour chaque page.

1. 
Ajoutez la [Page] actuelle (https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) au nouveau [Document] (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Enregistrez le nouveau [Document] (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) avec un nom de fichier unique.

1. 
Fermez les deux objets [Document] (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) une fois le traitement terminé.


## 
Diviser le PDF en fichiers d'une seule page



L'exemple Java suivant est basé sur `SplitDocumentExamples.java` et enregistre les pages sous `Page_1.pdf`, `Page_2.pdf`, etc.

```java
public static void splitDocument(Path inputFile, Path outputDir) {
    Document document = new Document(inputFile.toString());
    try {
        int pageCount = 1;
        for (Page page : document.getPages()) {
            Document newDocument = new Document();
            try {
                newDocument.getPages().add(page);
                newDocument.save(outputDir.resolve("Page_" + pageCount + ".pdf").toString());
            } finally {
                newDocument.close();
            }
            pageCount++;
        }
    } finally {
        document.close();
    }
}
```
