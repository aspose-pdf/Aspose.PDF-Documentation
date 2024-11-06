---
title: Diviser un PDF par programmation
linktitle: Diviser des fichiers PDF
type: docs
weight: 60
url: fr/cpp/split-pdf-document/
description: Ce sujet montre comment diviser des pages PDF en fichiers PDF individuels avec C++.
lastmod: "2022-09-01"
sitemap:
    changefreq: "monthy"
    priority: 0.7
---

## Exemple en direct

[Aspose.PDF Splitter](https://products.aspose.app/pdf/splitter) est une application web gratuite en ligne qui vous permet d'examiner comment fonctionne la fonctionnalité de division de présentation.

[![Aspose Diviser PDF](splitter.png)](https://products.aspose.app/pdf/splitter)

Ce sujet montre comment diviser des pages PDF en fichiers PDF individuels dans vos applications C++. Pour diviser des pages PDF en fichiers PDF d'une seule page à l'aide de C++, les étapes suivantes peuvent être suivies :

1. Parcourez les pages du document PDF via la collection [PageCollection](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page_collection) de l'objet [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document)
1. Pour chaque itération, créez un nouvel objet Document et copiez l'objet [Page](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page) individuel dans le document vide.  
1. Enregistrez le nouveau PDF en utilisant la méthode Save

Le fragment de code C++ suivant vous montre comment diviser les pages PDF en fichiers PDF individuels.

```cpp
void SplittingDocuments() {
    // Chaîne pour le nom du chemin
    String _dataDir("C:\\Samples\\");

    // Chaîne pour le nom du fichier d'entrée
    String documentFileName("sample.pdf");
    
    // Ouvrir le document
    auto document = MakeObject<Document>(_dataDir + documentFileName);

    int pageCount = 1;

    // Boucle à travers toutes les pages
    for(auto page : document->get_Pages())
    {
        auto newDocument = MakeObject<Document>(_dataDir + documentFileName);
        newDocument->get_Pages()->CopyPage(page);
        newDocument->Save(_dataDir + u"page_" + pageCount + u"_out.pdf");
        pageCount++;
    }
}
```