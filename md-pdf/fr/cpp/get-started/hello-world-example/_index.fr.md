---
title: Aspose.PDF С++ Exemple
linktitle: Exemple Bonjour Monde
type: docs
weight: 40
url: /cpp/hello-world-example/
description: Cette page montre comment utiliser une programmation simple pour créer un document PDF contenant le texte - Bonjour Monde.
lastmod: "2021-11-01"
sitemap:
    changefreq: "monthly"
    priority: 0.6
---

Un exemple "Bonjour Monde" est traditionnellement utilisé pour introduire les fonctionnalités d'un langage de programmation ou d'un logiciel avec un cas d'utilisation simple.

Aspose.PDF pour C++ est une API PDF riche en fonctionnalités qui permet aux développeurs d'intégrer des capacités de création, de manipulation et de conversion de documents PDF dans leurs applications C++. Elle prend en charge le travail avec de nombreux formats de fichiers populaires, y compris PDF, XFA, TXT, HTML, PCL, XML, XPS, EPUB, TEX et les formats de fichiers image. Dans cet article, nous créons un document PDF contenant le texte "Bonjour Monde!". Après avoir installé Aspose.PDF pour C++ dans votre environnement, vous pouvez exécuter l'exemple de code ci-dessous pour voir comment fonctionne l'API Aspose.PDF.

L'extrait de code ci-dessous suit ces étapes :

1. Créer une [classe String](https://reference.aspose.com/pdf/cpp/class/system.string) pour le nom du chemin et le nom du fichier.
1. Instancier un objet [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document). Dans cette étape, nous créerons un document PDF vide avec des métadonnées mais sans pages.
1. Ajouter une [Page](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page) à l'objet document. Ainsi, notre document aura maintenant une page.
1. [Enregistrer](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document/#ac082fe8e67b25685fc51d33e804269fa) le document PDF résultant

L'extrait de code suivant est un programme Hello World pour démontrer le fonctionnement de l'API Aspose.PDF pour C++.

```cpp
void ExampleSimple()
{
    // Buffer pour contenir le chemin combiné.
    String outputFileName;

    // Chaîne pour le nom du chemin.
    String _dataDir("C:\\Samples\\");

    // Chaîne pour le nom du fichier.
    String filename("HelloWorld_out.pdf");

    auto document = MakeObject<Document>();
    auto page = document->get_Pages()->Add();

    // Ajouter du texte à la nouvelle page
    auto text = MakeObject<TextFragment>(u"Hello world!");

    auto paragraphs = page->get_Paragraphs();
    paragraphs->Add(text);

    // Enregistrer le PDF mis à jour
    outputFileName = _dataDir + filename;

    document->Save(outputFileName);
}
```