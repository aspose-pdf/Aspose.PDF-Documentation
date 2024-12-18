---
title: Supprimer des pages PDF par programmation
linktitle: Supprimer des pages PDF
type: docs
weight: 30
url: /fr/cpp/delete-pages/
description: Vous pouvez supprimer des pages de votre fichier PDF en utilisant une bibliothèque C++.
lastmod: "2021-12-09"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

Vous pouvez supprimer des pages d'un fichier PDF en utilisant Aspose.PDF pour C++. Pour supprimer une page particulière de la collection [PageCollection](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page_collection).

## Supprimer une page d'un fichier PDF

1. Appelez la méthode [Delete](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page#a02bb7a96e66ef6e10bcf4930b299b3b7) et spécifiez l'index de la page
1. Appelez la méthode Save pour enregistrer le fichier PDF mis à jour
Le code suivant montre comment supprimer une page particulière du fichier PDF en utilisant C++.

```cpp
void DeletePDFPages() {
    String _dataDir("C:\\Samples\\");
    String inputFileName("DeleteParticularPage.pdf");

    // Ouvrir le document
    auto document = MakeObject<Document>(_dataDir + inputFileName);

    // Supprimer une page particulière
    document->get_Pages()->Delete(2);

    // Enregistrer le PDF mis à jour
    document->Save(_dataDir + inputFileName);
}
```