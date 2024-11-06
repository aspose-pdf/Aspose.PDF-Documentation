---
title: Fusionner des PDF en utilisant C++
linktitle: Fusionner des fichiers PDF
type: docs
weight: 50
url: fr/cpp/merge-pdf-documents/
description: Cette page explique comment fusionner des documents PDF en un seul fichier PDF avec C++.
lastmod: "2021-11-11"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

La fusion de fichiers PDF n'est pas une tâche facile, mais elle est très populaire. Vous pouvez utiliser la bibliothèque Aspose.PDF pour C++ pour combiner des fichiers PDF en un seul document rapidement et facilement.

## Fusionner des fichiers PDF en utilisant C++

Pour concaténer deux fichiers PDF :

1. Créez deux objets [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document), chacun contenant l'un des fichiers PDF d'entrée.
1. Ensuite, appelez la méthode Add de la collection [PageCollection](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page_collection) pour l'objet Document auquel vous souhaitez ajouter l'autre fichier PDF.
1. Ajoutez la [Page](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page) du deuxième document au premier fichier.
1. Enfin, enregistrez le fichier PDF de sortie en utilisant la méthode Save.

L'extrait de code suivant montre comment concaténer des fichiers PDF.

```cpp
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Text;
void MergingDocuments() {
    // Chaîne pour le nom du chemin
    String _dataDir("C:\\Samples\\");

    // Chaîne pour le nom du fichier d'entrée
    String pdfDocumentFileName1("Concat1.pdf");
    String pdfDocumentFileName2("Concat2.pdf");
    String outputFileName("ConcatenatePdfFiles.pdf");

    // Ouvrir le document
    auto pdfDocument1 = MakeObject<Document>(_dataDir + pdfDocumentFileName1);
    auto pdfDocument2 = MakeObject<Document>(_dataDir + pdfDocumentFileName2);

    // Ajouter les pages du deuxième document au premier
    pdfDocument1->get_Pages()->Add(pdfDocument2->get_Pages());

    // Enregistrer le fichier de sortie concaténé
    pdfDocument1->Save(_dataDir+outputFileName);
}
```

## Exemple en direct

[Aspose.PDF Merger](https://products.aspose.app/pdf/merger) est une application web gratuite en ligne qui vous permet d'étudier comment fonctionne la fonctionnalité de fusion de présentation.

[![Aspose.PDF Merger](merger.png)](https://products.aspose.app/pdf/merger)