---
title: Ajouter des Pages dans un PDF avec C++
linktitle: Ajouter des Pages
type: docs
weight: 10
url: fr/cpp/add-pages/
description: Cet article enseigne comment insérer (ajouter) une page à l'emplacement souhaité d'un fichier PDF. Apprenez comment déplacer, supprimer (effacer) des pages d'un fichier PDF en utilisant C++.
lastmod: "2021-12-08"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

Cette section montre comment ajouter des pages à un PDF en utilisant la bibliothèque **Aspose.PDF pour C++**.

L'API Aspose.PDF pour C++ offre une flexibilité totale pour travailler avec les pages dans un document PDF en utilisant C++.

Elle gère toutes les pages d'un document PDF dans [PageCollection](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page_collection) qui peut être utilisée pour travailler avec les pages PDF.
Aspose.PDF pour C++ vous permet d'insérer une page dans un document PDF à n'importe quel emplacement dans le fichier ainsi que d'ajouter des pages à la fin d'un fichier PDF.

## Ajouter ou Insérer une Page dans un Fichier PDF

Aspose.PDF pour C++ vous permet d'insérer une page dans un document PDF à n'importe quel emplacement dans le fichier ainsi que d'ajouter des pages à la fin d'un fichier PDF.

### Insérer une Page Vide dans un Fichier PDF à l'Emplacement Souhaité

Le code suivant vous explique comment ajouter une page dans un document PDF.

1. Créez un objet de la classe [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document) avec le fichier PDF d'entrée.
2. Appelez la méthode [Insert](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page_collection#a1fb1fe44df4d325df5ad41b691501bb2) de la collection [PageCollection](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page_collection) avec l'index spécifié.
3. Enregistrez le PDF de sortie

Le code suivant vous montre comment insérer une page dans un fichier PDF.

```cpp
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Text;


void InsertEmptyPageAtDesiredLocation() {
    // Ouvrir le document
    String _dataDir("C:\\Samples\\");

    // Chaîne pour le nom du fichier d'entrée
    String inputFileName("InsertEmptyPage.pdf");

    String outputFileName("InsertEmptyPage_out.pdf");

    auto document = MakeObject<Document>(_dataDir + inputFileName);

    // Insérer une page vide dans un PDF
    document->get_Pages()->Insert(2);

    // Enregistrer le fichier de sortie
    document->Save(_dataDir + outputFileName);
}
```

Dans l'exemple de code suivant, vous pouvez insérer une page vide à l'emplacement souhaité en copiant les paramètres de la page spécifiée :

```cpp
void InsertEmptyPageAtDesiredLocation2() {
    // Ouvrir le document
    String _dataDir("C:\\Samples\\");

    // Chaîne pour le nom du fichier d'entrée
    String inputFileName("InsertEmptyPage.pdf");

    String outputFileName("InsertEmptyPage_out.pdf");

    auto document = MakeObject<Document>(_dataDir + inputFileName);
    auto page = document->get_Pages()->idx_get(1);
    // Insérer une page vide dans un PDF
    auto pageNew = document->get_Pages()->Insert(2);

    // copier les paramètres de la page depuis la page 1
    pageNew->set_ArtBox(page->get_ArtBox());
    pageNew->set_BleedBox(page->get_BleedBox());
    pageNew->set_CropBox(page->get_CropBox());
    pageNew->set_MediaBox(page->get_MediaBox());
    pageNew->set_TrimBox(page->get_TrimBox());

    // Enregistrer le fichier de sortie
    document->Save(_dataDir + outputFileName);
}
```

### Ajouter une Page Vide à la Fin d'un Fichier PDF

Parfois, vous souhaitez vous assurer qu'un document se termine par une page vide. Ce sujet explique comment insérer une page vide à la fin du document PDF.

Pour insérer une page vide à la fin d'un fichier PDF :

1. Créez un objet de classe [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document) avec le fichier PDF d'entrée.
1. Appelez la méthode [Add](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page_collection#abb0362ffa129a1e2e5650a2f2e7057c1) de la collection [PageCollection](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page_collection), sans aucun paramètre.
1. Enregistrez le PDF de sortie à l'aide de la méthode Save.

L'extrait de code suivant vous montre comment insérer une page vide à la fin d'un fichier PDF.

```cpp
void AddEmptyPageEnd() {
    // Ouvrir le document
    String _dataDir("C:\\Samples\\");

    // Chaîne pour le nom du fichier d'entrée
    String inputFileName("InsertEmptyPageAtEnd.pdf");
    String outputFileName("InsertEmptyPageAtEnd_out.pdf");

    auto document = MakeObject<Document>(_dataDir + inputFileName);

    // Insérer une page vide à la fin d'un fichier PDF
    document->get_Pages()->Add();

    // Enregistrer le fichier de sortie
    document->Save(_dataDir + outputFileName);
}
```