---
title: Ajouter des tampons de texte dans un fichier PDF
linktitle: Tampons de texte dans un fichier PDF
type: docs
weight: 20
url: fr/cpp/text-stamps-in-the-pdf-file/
description: Ajoutez un tampon de texte à un fichier PDF en utilisant la classe TextStamp avec C++.
lastmod: "2021-12-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Ajouter un tampon de texte avec C++

Vous pouvez utiliser la classe [TextStamp](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.text_stamp) pour ajouter un tampon de texte dans un fichier PDF. La classe TextStamp fournit les propriétés nécessaires pour créer un tampon basé sur du texte, comme la taille de la police, le style de la police, et la couleur de la police, etc. Pour ajouter un tampon de texte, vous devez créer un objet Document et un objet TextStamp en utilisant les propriétés requises. Après cela, vous pouvez appeler la méthode AddStamp de la Page pour ajouter le tampon dans le PDF. Le code suivant vous montre comment ajouter un tampon de texte dans le fichier PDF.

```cpp
void AddTextStampToPDFFile() {

    String _dataDir("C:\\Samples\\");

    // String pour le nom du fichier d'entrée
    String inputFileName("AddTextStamp.pdf");
    String outputFileName("AddTextStamp_out.pdf");

    // Ouvrir le document
    auto document = MakeObject<Document>(_dataDir + inputFileName);

    // Créer un tampon de texte
    auto textStamp =MakeObject<TextStamp>(u"Sample Stamp");

    // Définir si le tampon est en arrière-plan
    textStamp->set_Background(true);
    // Définir l'origine
    textStamp->set_XIndent(100);
    textStamp->set_YIndent(100);
    // Faire pivoter le tampon
    textStamp->set_Rotate(Rotation::on90);

    // Définir les propriétés du texte
    textStamp->get_TextState()->set_Font(FontRepository::FindFont(u"Arial"));
    textStamp->get_TextState()->set_FontSize(14.0F);
    textStamp->get_TextState()->set_FontStyle(FontStyles::Bold);
    textStamp->get_TextState()->set_FontStyle(FontStyles::Italic);
    textStamp->get_TextState()->set_ForegroundColor(Color::get_Green());
    // Ajouter le tampon à une page particulière
    document->get_Pages()->idx_get(1)->AddStamp(textStamp);

    // Enregistrer le document de sortie
    document->Save(_dataDir + outputFileName);
}
```

## Définir l'alignement pour l'objet TextStamp

Ajouter des filigranes aux documents PDF est l'une des fonctionnalités fréquemment demandées et Aspose.PDF pour C++ est tout à fait capable d'ajouter des filigranes d'image ainsi que de texte. Nous avons une classe nommée [TextStamp](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.text_stamp) qui offre la possibilité d'ajouter des tampons de texte sur le fichier PDF. Récemment, il y a eu une demande pour prendre en charge la fonctionnalité de spécification de l'alignement du texte lors de l'utilisation de l'objet TextStamp. Ainsi, afin de répondre à cette demande, nous avons introduit la propriété TextAlignment dans la classe TextStamp. En utilisant cette propriété, nous pouvons spécifier l'alignement horizontal du texte.

Les extraits de code suivants montrent un exemple sur la façon de charger un document PDF existant et d'y ajouter un TextStamp.

```cpp
void DefineAlignmentTextStamp() {

    String _dataDir("C:\\Samples\\");

    // String pour le nom du fichier d'entrée
    String inputFileName("AddTextStamp.pdf");
    String outputFileName("AddTextStamp_out.pdf");

    // Ouvrir le document
    auto document = MakeObject<Document>(_dataDir + inputFileName);

    // instancier un objet FormattedText avec une chaîne d'exemple
    auto text = MakeObject<Aspose::Pdf::Facades::FormattedText>("This");

    // ajouter une nouvelle ligne de texte à FormattedText
    text->AddNewLineText(u"is sample");
    text->AddNewLineText(u"Center Aligned");
    text->AddNewLineText(u"TextStamp");
    text->AddNewLineText(u"Object");

    // créer un objet TextStamp en utilisant FormattedText
    auto stamp = MakeObject<TextStamp>(text);
    // spécifier l'alignement horizontal du tampon de texte comme étant centré
    stamp->set_HorizontalAlignment(HorizontalAlignment::Center);
    // spécifier l'alignement vertical du tampon de texte comme étant centré
    stamp->set_VerticalAlignment(VerticalAlignment::Center);
    // spécifier l'alignement horizontal du texte de TextStamp comme étant centré
    stamp->set_TextAlignment(HorizontalAlignment::Center);
    // définir la marge supérieure pour l'objet tampon
    stamp->set_TopMargin(20);
    // ajouter le tampon à toutes les pages du fichier PDF
    document->get_Pages()->idx_get(1)->AddStamp(stamp);

    // enregistrer le document de sortie
    document->Save(_dataDir + outputFileName);
}
```

## Remplir le texte de contour comme un tampon dans le fichier PDF

Nous avons mis en œuvre le paramétrage du mode de rendu pour les scénarios d'ajout et de modification de texte. Pour rendre le texte en contour, veuillez créer un objet TextState et définir RenderingMode sur TextRenderingMode.StrokeText et également sélectionner la couleur pour la propriété StrokingColor. Ensuite, liez TextState au tampon en utilisant la méthode BindTextState().

Le code ci-dessous montre l'ajout de texte de contour rempli :

```cpp
void FillStrokeTextAsStampInPDFFile() {

    String _dataDir("C:\\Samples\\");

    // Chaîne pour le nom du fichier d'entrée
    String inputFileName("AddTextStamp.pdf");
    String outputFileName("AddTextStamp_out.pdf");

    // Créer un objet TextState pour transférer des propriétés avancées
    auto ts = MakeObject<TextState>();

    // Définir la couleur pour le contour
    ts->set_StrokingColor(Color::get_Gray());

    // Définir le mode de rendu du texte
    ts->set_RenderingMode(TextRenderingMode::StrokeText);

    // Charger un document PDF d'entrée
    auto fileStamp = MakeObject<Aspose::Pdf::Facades::PdfFileStamp>(MakeObject<Document>(_dataDir + inputFileName));

    auto stamp = MakeObject<Aspose::Pdf::Facades::Stamp>();

    auto formattedText = MakeObject<Aspose::Pdf::Facades::FormattedText>(u"PAID IN FULL", Color::get_Gray(), Aspose::Pdf::Facades::EncodingType::Winansi, true, 78);
    stamp->BindLogo(formattedText);

    // Lier TextState
    stamp->BindTextState(ts);

    // Définir l'origine X,Y
    stamp->SetOrigin(100, 100);
    stamp->set_Opacity(5);
    stamp->set_BlendingSpace(Aspose::Pdf::Facades::BlendingColorSpace::DeviceRGB);
    stamp->set_Rotation(45.0F);
    stamp->set_IsBackground(false);

    // Ajouter un tampon
    fileStamp->AddStamp(stamp);
    fileStamp->Save(_dataDir + outputFileName);
    fileStamp->Close();
}
```