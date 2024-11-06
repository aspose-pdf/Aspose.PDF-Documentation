---
title: Faire Pivoter les Pages PDF en Utilisant C++
linktitle: Faire Pivoter les Pages PDF
type: docs
weight: 50
url: fr/cpp/rotate-pages/
description: Ce sujet décrit comment faire pivoter l'orientation des pages dans un fichier PDF existant de manière programmatique avec C++.
lastmod: "2021-12-08"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

Ce sujet décrit comment mettre à jour ou changer l'orientation des pages dans un fichier PDF existant de manière programmatique avec C++.

## Changer l'Orientation de la Page

Aspose.PDF pour C++ vous permet de changer l'orientation des pages de paysage à portrait et vice versa. Pour changer l'orientation de la page, définissez le MediaBox de la page en utilisant l'extrait de code suivant. Vous pouvez également changer l'orientation de la page en définissant l'angle de rotation en utilisant la méthode Rotate().

```cpp
void ChangePageOrientation() {

    String _dataDir("C:\\Samples\\");
    String inputFileName("ChangeOrientation.pdf");
    String outputFileName("ChangeOrientation_out.pdf");
    // Ouvrir le document
    auto document = MakeObject<Document>(_dataDir + inputFileName);

    for (auto page : document->get_Pages())
    {

        auto r = page->get_MediaBox();
        double newHeight = r->get_Width();
        double newWidth = r->get_Height();
        double newLLX = r->get_LLX();

        // Nous devons déplacer la page vers le haut pour compenser le changement de taille de la page
        // (le bord inférieur de la page est 0,0 et l'information est généralement placée depuis le
        // haut de la page. C'est pourquoi nous déplaçons le bord inférieur vers le haut de la différence entre
        // l'ancienne et la nouvelle hauteur.

        double newLLY = r->get_LLY() + (r->get_Height() - newHeight);
        page->set_MediaBox(MakeObject<Rectangle>(newLLX, newLLY, newLLX + newWidth, newLLY + newHeight));
        // Parfois, nous devons également définir CropBox (s'il a été défini dans le fichier original)
        page->set_CropBox(MakeObject<Rectangle>(newLLX, newLLY, newLLX + newWidth, newLLY + newHeight));

        // Définition de l'angle de rotation de la page
        page->set_Rotate(Rotation::on90);
    }

    // Enregistrer le fichier de sortie
    document->Save(_dataDir + outputFileName);
}
```

## Adapter le Contenu de la Page à la Nouvelle Orientation de Page

Veuillez noter que lorsque vous utilisez l'extrait de code ci-dessus, une partie du contenu du document pourrait être coupée en raison de la diminution de la hauteur de la page. Pour éviter cela, augmentez la largeur proportionnellement et laissez la hauteur inchangée. Exemple de calculs :

```cpp
void FittingPageContentToNewPageOrientation()
{
    String _dataDir("C:\\Samples\\");
    String inputFileName("ChangeOrientation.pdf");
    String outputFileName("ChangeOrientation_out.pdf");
    // Ouvrir le document
    auto document = MakeObject<Document>(_dataDir + inputFileName);

    for (auto page : document->get_Pages())
    {
        auto r = page->get_MediaBox();
        // Nouvelle hauteur identique
        double newHeight = r->get_Height();
        // Nouvelle largeur étendue proportionnellement pour rendre l'orientation paysage
        // (nous supposons que l'orientation précédente est portrait)
        double newWidth = r->get_Height() * r->get_Height() / r->get_Width();

        // ...

    }
}
```

Outre l'approche ci-dessus, envisagez d'utiliser la façade PdfPageEditor qui peut appliquer un zoom au contenu des pages.

```cpp
void ZoomPageContent()
{

    String _dataDir("C:\\Samples\\");
    String inputFileName("ZoomToPageContents.pdf");
    String outputFileName("ZoomToPageContents_out.pdf");

    // Ouvrir le document
    auto document = MakeObject<Document>(_dataDir + inputFileName);

    // Obtenir la région rectangulaire de la première page du PDF
    auto rect = document->get_Pages()->idx_get(1)->get_Rect();

    // Instancier l'instance PdfPageEditor
    auto ppe = MakeObject<Aspose::Pdf::Facades::PdfPageEditor>();
    // Lier le PDF source
    ppe->BindPdf(_dataDir + inputFileName);
    // Définir le coefficient de zoom
    ppe->set_Zoom ((float)(rect->get_Width() / rect->get_Height()));
    // Mettre à jour la taille de la page
    ppe->set_PageSize(MakeObject<PageSize>((float)rect->get_Height(), (float)rect->get_Width()));

    // Enregistrer le fichier de sortie
    document->Save(_dataDir + outputFileName);
}
```