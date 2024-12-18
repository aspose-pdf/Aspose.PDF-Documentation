---
title: Ajouter un en-tête et un pied de page au PDF
linktitle: Ajouter un en-tête et un pied de page au PDF
type: docs
weight: 70
url: /fr/cpp/add-headers-and-footers-of-pdf-file/
description: Aspose.PDF pour C++ vous permet d'ajouter des en-têtes et des pieds de page à votre fichier PDF en utilisant la classe TextStamp.
lastmod: "2021-12-08"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

**Aspose.PDF pour C++** vous permet d'ajouter un en-tête et un pied de page dans votre fichier PDF existant. Vous pouvez ajouter des images ou du texte à un document PDF. Essayez également d'ajouter différents en-têtes dans un fichier PDF avec C++.

## Ajout de texte dans l'en-tête du fichier PDF

Vous pouvez utiliser la classe [TextStamp](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.text_stamp) pour ajouter du texte dans l'en-tête d'un fichier PDF. TextStamp class fournit les propriétés nécessaires pour créer un tampon basé sur du texte comme la taille de la police, le style de la police, et la couleur de la police, etc. Pour ajouter du texte dans l'en-tête, vous devez créer un objet Document et un objet TextStamp en utilisant les propriétés requises. Après cela, vous pouvez appeler la méthode AddStamp de la Page pour ajouter le texte dans l'en-tête du PDF.

Vous devez définir la propriété TopMargin de manière à ajuster le texte dans la zone d'en-tête de votre PDF. Vous devez également définir HorizontalAlignment sur Center et VerticalAlignment sur Top.

Le code suivant vous montre comment ajouter du texte dans l'en-tête d'un fichier PDF avec C++.

```cpp
void AddingTextInHeaderOfPdfFile() {
    String _dataDir("C:\\Samples\\");
    String inputFileName("TextinHeader.pdf");
    String outputFileName("TextinHeader_out.pdf");

    // Open document
    auto document = MakeObject<Document>(_dataDir + inputFileName);

    // Create header
    auto textStamp = MakeObject<TextStamp>(u"Header Text");

    // Set properties of the stamp
    textStamp->set_TopMargin(10);
    textStamp->set_HorizontalAlignment(HorizontalAlignment::Center);
    textStamp->set_VerticalAlignment(VerticalAlignment::Top);

    // Add header on all pages
    for(auto page : document->get_Pages())
    {
        page->AddStamp(textStamp);
    }

    // Save updated document
    document->Save(_dataDir + outputFileName);
}
```
## Ajout de texte dans le pied de page d'un fichier PDF

Vous pouvez utiliser la classe TextStamp pour ajouter du texte dans le pied de page d'un fichier PDF. La classe TextStamp fournit les propriétés nécessaires pour créer un tampon basé sur du texte, comme la taille de la police, le style de la police et la couleur de la police, etc. Afin d'ajouter du texte dans le pied de page, vous devez créer un objet Document et un objet TextStamp en utilisant les propriétés requises. Ensuite, vous pouvez appeler la méthode AddStamp de la Page pour ajouter le texte dans le pied de page du PDF.

{{% alert color="primary" %}}

Vous devez définir la propriété Bottom Margin de manière à ce qu'elle ajuste le texte dans la zone du pied de page de votre PDF. Vous devez également définir HorizontalAlignment sur Center et VerticalAlignment sur Bottom

{{% /alert %}}

L'extrait de code suivant vous montre comment ajouter du texte dans le pied de page d'un fichier PDF avec C++.

```cpp
void AddingTextInFooterOfPdfFile() {
    String _dataDir("C:\\Samples\\");
    String inputFileName("TextinFooter.pdf");
    String outputFileName("TextinFooter_out.pdf");

    // Ouvrir le document
    auto document = MakeObject<Document>(_dataDir + inputFileName);

    // Créer le pied de page
    auto textStamp = MakeObject<TextStamp>(u"Footer Text");

    // Définir les propriétés du tampon
    textStamp->set_BottomMargin(10);
    textStamp->set_HorizontalAlignment(HorizontalAlignment::Center);
    textStamp->set_VerticalAlignment(VerticalAlignment::Bottom);

    // Ajouter le pied de page sur toutes les pages
    for (auto page : document->get_Pages())
    {
        page->AddStamp(textStamp);
    }

    // Enregistrer le document mis à jour
    document->Save(_dataDir + outputFileName);
}
```

## Ajout d'une image dans l'en-tête d'un fichier PDF

Vous pouvez utiliser la classe [ImageStamp](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.image_stamp) pour ajouter une image dans l'en-tête d'un fichier PDF. La classe Image Stamp fournit les propriétés nécessaires pour créer un tampon basé sur une image comme la taille de la police, le style de la police et la couleur de la police, etc. Pour ajouter une image dans l'en-tête, vous devez créer un objet Document et un objet Image Stamp en utilisant les propriétés requises. Après cela, vous pouvez appeler la méthode AddStamp de la Page pour ajouter l'image dans l'en-tête du PDF.

Le code suivant vous montre comment ajouter une image dans l'en-tête d'un fichier PDF avec C++.

```cpp
void AddingImageInHeaderOfPdfFile() {

    String _dataDir("C:\\Samples\\");
    String inputFileName("ImageinHeader.pdf");
    String outputFileName("ImageinHeader_out.pdf");

    // Ouvrir le document
    auto document = MakeObject<Document>(_dataDir + inputFileName);

    // Créer l'en-tête
    auto imageStamp = MakeObject<ImageStamp>(_dataDir + u"aspose-logo.jpg");

    // Définir les propriétés du tampon
    imageStamp->set_TopMargin(10);
    imageStamp->set_HorizontalAlignment(HorizontalAlignment::Center);
    imageStamp->set_VerticalAlignment (VerticalAlignment::Top);

    // Ajouter l'en-tête sur toutes les pages
    for(auto page : document->get_Pages())
    {
        page->AddStamp(imageStamp);
    }

    // Enregistrer le document mis à jour
    document->Save(_dataDir + outputFileName);
}
```

## Ajouter une Image dans le Pied de Page d'un Fichier PDF

Vous pouvez utiliser la classe Image Stamp pour ajouter une image dans le pied de page d'un fichier PDF. La classe Image Stamp fournit les propriétés nécessaires pour créer un tampon basé sur une image comme la taille de la police, le style de la police et la couleur de la police, etc. Pour ajouter une image dans le pied de page, vous devez créer un objet Document et un objet Image Stamp en utilisant les propriétés requises. Après cela, vous pouvez appeler la méthode AddStamp de la Page pour ajouter l'image dans le pied de page du PDF.

Vous devez définir la propriété [BottomMargin](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.stamp#aeab91949cf3eb473018b31a74fed7173) de manière à ajuster l'image dans la zone de pied de page de votre PDF. Vous devez également définir [HorizontalAlignment](https://reference.aspose.com/pdf/cpp/namespace/aspose.pdf#aefec9c0bf30ee5e6fb2640e69aed6cd9) sur `Center` et [VerticalAlignment](https://reference.aspose.com/pdf/cpp/namespace/aspose.pdf#ad4956d03096fc515eaa34319a6bf636a) sur `Bottom`.

Le fragment de code suivant vous montre comment ajouter une image dans le pied de page d'un fichier PDF avec C++.

```cpp
void AddingImageInFooterOfPdfFile() {

    String _dataDir("C:\\Samples\\");
    String inputFileName("ImageinFooter.pdf");
    String outputFileName("ImageinFooter_out.pdf");

    // Ouvrir le document
    auto document = MakeObject<Document>(_dataDir + inputFileName);

    // Créer un en-tête
    auto imageStamp = MakeObject<ImageStamp>(_dataDir + u"aspose-logo.jpg");

    // Définir les propriétés du tampon
    imageStamp->set_TopMargin(10);
    imageStamp->set_HorizontalAlignment(HorizontalAlignment::Center);
    imageStamp->set_VerticalAlignment(VerticalAlignment::Top);

    // Ajouter un en-tête sur toutes les pages
    for (auto page : document->get_Pages())
    {
        page->AddStamp(imageStamp);
    }

    // Enregistrer le document mis à jour
    document->Save(_dataDir + outputFileName);
}
```

## Ajouter différents en-têtes dans un fichier PDF

Nous savons que nous pouvons ajouter un TextStamp dans la section En-tête/Pied de page du document en utilisant les propriétés de marge supérieure ou inférieure, mais parfois nous pouvons avoir le besoin d'ajouter plusieurs en-têtes/pieds de page dans un seul document PDF. **Aspose.PDF for C++** explique comment faire cela.

Afin de répondre à cette exigence, nous allons créer des objets TextStamp individuels (le nombre d'objets dépend du nombre d'en-têtes/pieds de page requis) et les ajouterons au document PDF. Nous pouvons également spécifier différentes informations de formatage pour chaque objet de tampon. Dans l'exemple suivant, nous avons créé un objet Document et trois objets TextStamp, puis nous avons utilisé la méthode [AddStamp](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page#a3b998038dedf5266b4d60586b1b53d02) de la Page pour ajouter le texte dans la section d'en-tête du PDF. L'extrait de code suivant vous montre comment ajouter une image dans le pied de page d'un fichier PDF avec Aspose.PDF pour C++.

```cpp
void AddingDifferentHeadersInOnePDFFile()
{
    String _dataDir("C:\\Samples\\");
    String inputFileName("multiheader.pdf");
    String outputFileName("multiheader_out.pdf");

    // Ouvrir le document source
    auto document = MakeObject<Document>(_dataDir + inputFileName);

    // Créer trois tampons
    auto stamp1 = MakeObject<TextStamp>("Header 1");
    auto stamp2 = MakeObject<TextStamp>("Header 2");
    auto stamp3 = MakeObject<TextStamp>("Header 3");

    // Définir l'alignement du tampon (placer le tampon en haut de la page, centré horizontalement)
    stamp1->set_VerticalAlignment(VerticalAlignment::Top);
    stamp1->set_HorizontalAlignment(HorizontalAlignment::Center);
    // Spécifier le style de police comme Gras
    stamp1->get_TextState()->set_FontStyle(FontStyles::Bold);
    // Définir la couleur de premier plan du texte comme rouge
    stamp1->get_TextState()->set_ForegroundColor(Color::get_Red());
    // Spécifier la taille de police comme 14
    stamp1->get_TextState()->set_FontSize(14);

    // Maintenant, nous devons définir l'alignement vertical du deuxième objet tampon comme Haut
    stamp2->set_VerticalAlignment(VerticalAlignment::Top);
    // Définir les informations d'alignement horizontal pour le tampon comme centré
    stamp2->set_HorizontalAlignment (HorizontalAlignment::Center);
    // Définir le facteur de zoom pour l'objet tampon
    stamp2->set_Zoom(10);

    // Définir le formatage du troisième objet tampon
    // Spécifier les informations d'alignement vertical pour l'objet tampon comme HAUT
    stamp3->set_VerticalAlignment(VerticalAlignment::Top);
    // Définir les informations d'alignement horizontal pour l'objet tampon comme centré
    stamp3->set_HorizontalAlignment(HorizontalAlignment::Center);
    // Définir l'angle de rotation pour l'objet tampon
    stamp3->set_RotateAngle(35);
    // Définir la couleur de fond rose pour le tampon
    stamp3->get_TextState()->set_BackgroundColor(Color::get_Pink());
    // Changer les informations de police pour le tampon en Verdana
    stamp3->get_TextState()->set_Font(FontRepository::FindFont(u"Verdana"));

    // Le premier tampon est ajouté sur la première page ;
    document->get_Pages()->idx_get(1)->AddStamp(stamp1);
    // Le deuxième tampon est ajouté sur la deuxième page ;
    document->get_Pages()->idx_get(2)->AddStamp(stamp2);
    // Le troisième tampon est ajouté sur la troisième page.
    document->get_Pages()->idx_get(3)->AddStamp(stamp3);

    // Enregistrer le document mis à jour
    document->Save(_dataDir + outputFileName);
}
```