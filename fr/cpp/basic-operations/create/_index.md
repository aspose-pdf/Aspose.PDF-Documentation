---
title: Créer un document PDF en utilisant C++
linktitle: Créer
type: docs
weight: 10
url: fr/cpp/create-document/
description: La tâche la plus populaire et basique de travail avec un fichier PDF est de créer un document à partir de zéro. Utilisez la bibliothèque Aspose.PDF pour C++.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

**Aspose.PDF pour C++** API permet aux développeurs d'applications C++ d'incorporer des fonctionnalités de traitement de documents PDF dans leurs applications. Il peut être utilisé pour créer et lire des fichiers PDF sans besoin d'aucun autre logiciel installé sur la machine sous-jacente. Aspose.PDF pour C++ peut être utilisé dans une variété de types d'applications C++ tels que QT, MFC et les applications console.

## Comment créer un fichier PDF en utilisant C++

Pour créer un fichier PDF en utilisant C++, les étapes suivantes peuvent être utilisées.

1. Instancier un objet [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document)
1. Ajouter une [Page](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page/) à l'objet document
1. Créer un objet [TextFragment](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.te_x_fragment/)
1. Ajouter [TextFragment](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.te_x_fragment/) à la collection [Paragraph](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.paragraphs/) de la page
1. Enregistrer le document PDF résultant

```cpp
void CreatePDF() {
    // Chaîne pour le nom du chemin.
    String _dataDir("C:\\Samples\\");

    // Chaîne pour le nom du fichier.
    String filename("sample-new.pdf");

    // Initialiser l'objet document
    auto document = MakeObject<Document>();
    // Ajouter une page
    auto page = document->get_Pages()->Add();

    // Ajouter du texte à la nouvelle page
    auto textFragment = MakeObject<TextFragment>(u"Hello World!");
    page->get_Paragraphs()->Add(textFragment);

    // Enregistrer le PDF mis à jour
    String outputFileName = _dataDir + filename;

    document->Save(outputFileName);
}
```