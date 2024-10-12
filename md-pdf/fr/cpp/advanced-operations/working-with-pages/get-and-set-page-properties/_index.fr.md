---
title: Obtenir et Définir les Propriétés de Page
type: docs
weight: 20
url: /cpp/get-and-set-page-properties/
description: Vous pouvez obtenir et définir les propriétés de page de votre fichier PDF en utilisant la bibliothèque C++.
lastmod: "2021-12-09"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

**Aspose.PDF for C++** vous permet de lire et de définir les propriétés des pages dans un fichier PDF dans vos applications C++. Cette section montre comment obtenir le nombre de pages dans un fichier PDF, obtenir des informations sur les propriétés des pages PDF telles que la couleur et définir les propriétés de page, obtenir une page particulière du fichier PDF, etc.

## Obtenir le Nombre de Pages dans un Fichier PDF

Lorsque vous travaillez avec des documents, vous souhaitez souvent savoir combien de pages ils contiennent. Avec Aspose.PDF, cela ne prend pas plus de deux lignes de code.

Pour obtenir le nombre de pages dans un fichier PDF :

1. Ouvrez le fichier PDF en utilisant la classe [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document).
1. Ensuite, utilisez la propriété Count de la collection [PageCollection](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page_collection) (à partir de l'objet Document) pour obtenir le nombre total de pages dans le document.

L'extrait de code suivant montre comment obtenir le nombre de pages d'un fichier PDF.

```cpp
void GetNumberOfPages() {
    // Ouvrir le document
    String _dataDir("C:\\Samples\\");
    String srcFileName("GetNumberofPages.pdf");

    auto srcDocument = MakeObject<Document>(_dataDir + srcFileName);

    // Obtenir le nombre de pages
    std::cout << "Nombre de pages : " << srcDocument->get_Pages()->get_Count() << std::endl;
}
```

### Obtenir le nombre de pages sans enregistrer le document

Parfois, nous générons les fichiers PDF à la volée et lors de la création du fichier PDF, nous pouvons rencontrer le besoin (création de Table des matières etc.) d'obtenir le nombre de pages du fichier PDF sans enregistrer le fichier sur le système ou le flux. So in order to cater to this requirement, a method [ProcessParagraphs](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document#a1773e7b6a887eaddd602073e29939a6f) has been introduced in Document class. Please take a look over the following code snippet which shows the steps to get page count without saving the document.

```cpp
void GetPageCountWithoutSavingTheDocument() {
    // Instancier une instance de Document
    auto document = MakeObject<Document>();

    // Ajouter une page à la collection de pages du fichier PDF
    auto page = document->get_Pages()->Add();
    // Créer une instance de boucle
    for (int i = 0; i < 300; i++)
        // Ajouter TextFragment à la collection de paragraphes de l'objet page
        page->get_Paragraphs()->Add(MakeObject<TextFragment>(u"Test du nombre de pages"));
    // Traiter les paragraphes dans le fichier PDF pour obtenir un nombre de pages précis
    document->ProcessParagraphs();
    // Imprimer le nombre de pages dans le document
    std::cout << "Nombre de pages dans le document = " << document->get_Pages()->get_Count();
}
```

## Obtenir les propriétés de la page
### Accéder aux Propriétés de la Page

La classe [Page](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page) fournit toutes les propriétés liées à une page PDF particulière. Toutes les pages des fichiers PDF sont contenues dans la collection [PageCollection](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page_collection) de l'objet [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document).

À partir de là, il est possible d'accéder soit à des objets Page individuels en utilisant leur index, soit de parcourir la collection en utilisant une boucle foreach pour obtenir toutes les pages. Une fois qu'une page individuelle est accessible, nous pouvons obtenir ses propriétés. Le code suivant montre comment obtenir les propriétés de la page.

```cpp
void AccessingPageProperties() {

    String _dataDir("C:\\Samples\\");
    String pdfDocument("GetProperties.pdf");

    // Ouvrir le document
    auto document = MakeObject<Document>(_dataDir + pdfDocument);

    // Obtenir une page particulière
    auto pdfPage = document->get_Pages()->idx_get(1);
    // Obtenir les propriétés de la page
    Console::WriteLine(u"ArtBox : Hauteur={0},Largeur={1},LLX={2},LLY={3},URX={4},URY={5}",
        pdfPage->get_ArtBox()->get_Height(), pdfPage->get_ArtBox()->get_Width(),
        pdfPage->get_ArtBox()->get_LLX(), pdfPage->get_ArtBox()->get_LLY(),
        pdfPage->get_ArtBox()->get_URX(), pdfPage->get_ArtBox()->get_URY());

    Console::WriteLine(u"->get_BleedBox() : Hauteur={0},Largeur={1},LLX={2},LLY={3},URX={4},URY={5}",
        pdfPage->get_BleedBox()->get_Height(), pdfPage->get_BleedBox()->get_Width(),
        pdfPage->get_BleedBox()->get_LLX(), pdfPage->get_BleedBox()->get_LLY(),
        pdfPage->get_BleedBox()->get_URX(), pdfPage->get_BleedBox()->get_URY());

    Console::WriteLine(u"get_CropBox() : Hauteur={0},Largeur={1},LLX={2},LLY={3},URX={4},URY={5}",
        pdfPage->get_CropBox()->get_Height(), pdfPage->get_CropBox()->get_Width(),
        pdfPage->get_CropBox()->get_LLX(), pdfPage->get_CropBox()->get_LLY(),
        pdfPage->get_CropBox()->get_URX(), pdfPage->get_CropBox()->get_URY());

    Console::WriteLine(u"get_MediaBox() : Hauteur={0},Largeur={1},LLX={2},LLY={3},URX={4},URY={5}",
        pdfPage->get_MediaBox()->get_Height(), pdfPage->get_MediaBox()->get_Width(),
        pdfPage->get_MediaBox()->get_LLX(), pdfPage->get_MediaBox()->get_LLY(),
        pdfPage->get_MediaBox()->get_URX(), pdfPage->get_MediaBox()->get_URY());

    Console::WriteLine(u"get_TrimBox() : Hauteur={0},Largeur={1},LLX={2},LLY={3},URX={4},URY={5}",
        pdfPage->get_TrimBox()->get_Height(), pdfPage->get_TrimBox()->get_Width(),
        pdfPage->get_TrimBox()->get_LLX(), pdfPage->get_TrimBox()->get_LLY(),
        pdfPage->get_TrimBox()->get_URX(), pdfPage->get_TrimBox()->get_URY());

    Console::WriteLine(u"Rect : Hauteur={0},Largeur={1},LLX={2},LLY={3},URX={4},URY={5}",
        pdfPage->get_Rect()->get_Height(), pdfPage->get_Rect()->get_Width(),
        pdfPage->get_Rect()->get_LLX(), pdfPage->get_Rect()->get_LLY(),
        pdfPage->get_Rect()->get_URX(), pdfPage->get_Rect()->get_URY());

    Console::WriteLine(u"Numéro de Page : {0}", pdfPage->get_Number());
    Console::WriteLine(u"Rotation : {0}", pdfPage->get_Rotate());
}
```