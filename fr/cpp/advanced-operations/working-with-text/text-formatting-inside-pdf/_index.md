---
title: Formatage du texte dans un PDF en utilisant C++
linktitle: Formatage du texte dans un PDF
type: docs
weight: 30
url: /fr/cpp/text-formatting-inside-pdf/
description: Cette page explique comment formater le texte dans votre fichier PDF. Il s'agit d'ajouter un retrait de ligne, d'ajouter une bordure de texte, d'ajouter du texte souligné, d'ajouter une bordure autour du texte ajouté, d'aligner le texte pour le contenu des boîtes flottantes, etc.
lastmod: "2021-12-13"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Comment ajouter un retrait de ligne au PDF

Pour ajouter un retrait de ligne au PDF, Aspose.PDF pour C++ utilise la propriété [SubsequentLinesIndent](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.text.text_formatting_options#a89b064ab1f39d56040625d7d98194ad3) dans la classe [TextFormattingOptions](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.text.text_formatting_options/) et utilise également les collections [TextFragment](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.text.text_fragment/) et [Paragraphs](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.paragraphs).

Veuillez utiliser l'extrait de code suivant pour utiliser la propriété :

```cpp
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Text;

void AddLineIndent() {

    String _dataDir("C:\\Samples\\");

    // Chaîne pour le nom du fichier de sortie
    String outputFileName("SubsequentIndent_out.pdf");


    // Créez un nouvel objet document
    auto document = MakeObject<Document>();
    auto page = document->get_Pages()->Add();

    auto text = MakeObject<TextFragment>("Un renard brun rapide a sauté par-dessus le chien paresseux. Un renard brun rapide a sauté par-dessus le chien paresseux. Un renard brun rapide a sauté par-dessus le chien paresseux. Un renard brun rapide a sauté par-dessus le chien paresseux. Un renard brun rapide a sauté par-dessus le chien paresseux. Un renard brun rapide a sauté par-dessus le chien paresseux. Un renard brun rapide a sauté par-dessus le chien paresseux. Un renard brun rapide a sauté par-dessus le chien paresseux.");

    // Initialiser les TextFormattingOptions pour le fragment de texte et spécifier la valeur SubsequentLinesIndent

    text->get_TextState()->set_FormattingOptions(MakeObject<Aspose::Pdf::Text::TextFormattingOptions>());
    text->get_TextState()->get_FormattingOptions()->set_SubsequentLinesIndent(20);

    page->get_Paragraphs()->Add(text);

    text = MakeObject<Aspose::Pdf::Text::TextFragment>(u"Ligne2");
    page->get_Paragraphs()->Add(text);

    text = MakeObject<Aspose::Pdf::Text::TextFragment>(u"Ligne3");
    page->get_Paragraphs()->Add(text);

    text = MakeObject<Aspose::Pdf::Text::TextFragment>(u"Ligne4");
    page->get_Paragraphs()->Add(text);

    text = MakeObject<Aspose::Pdf::Text::TextFragment>(u"Ligne5");
    page->get_Paragraphs()->Add(text);

    document->Save(_dataDir + outputFileName);

}
```

## Comment ajouter une bordure de texte

L'extrait de code suivant montre comment ajouter une bordure à un texte en utilisant TextBuilder et en définissant la propriété DrawTextRectangleBorder de [TextState](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.text.text_state)

```cpp
void AddTextBorder() {

    String _dataDir("C:\\Samples\\");

    // Chaîne pour le nom de fichier de sortie
    String outputFileName("PDFWithTextBorder_out.pdf");

    // Créer un nouvel objet document
    auto document = MakeObject<Document>();
    // Obtenir une page particulière
    auto page = document->get_Pages()->Add();

    // Créer un fragment de texte
    auto textFragment = MakeObject<TextFragment>("main text");
    textFragment->set_Position(MakeObject<Position>(100, 600));

    // Définir les propriétés du texte
    textFragment->get_TextState()->set_FontSize(12);
    textFragment->get_TextState()->set_Font(FontRepository::FindFont(u"DejaVu Serif"));
    textFragment->get_TextState()->set_BackgroundColor(Color::get_LightGray());
    textFragment->get_TextState()->set_ForegroundColor(Color::get_Red());
    // Définir la propriété StrokingColor pour dessiner une bordure (tracé) autour du texte
    // rectangle
    textFragment->get_TextState()->set_StrokingColor(Color::get_DarkRed());
    // Définir la valeur de la propriété DrawTextRectangleBorder à true
    textFragment->get_TextState()->set_DrawTextRectangleBorder(true);
    auto tb = MakeObject<TextBuilder>(page);
    tb->AppendText(textFragment);
    // Enregistrer le document
    document->Save(_dataDir + outputFileName);
}
```

## Comment ajouter du texte souligné

Le fragment de code suivant vous montre comment ajouter du texte souligné lors de la création d'un nouveau fichier PDF.

```cpp
void AddUnderlineText() {
    String _dataDir("C:\\Samples\\");

    // Chaîne pour le nom du fichier de sortie
    String outputFileName("AddUnderlineText_out.pdf");

    // Créer un nouvel objet document
    auto document = MakeObject<Document>();
    // Obtenir une page particulière
    auto page = document->get_Pages()->Add();

    // TextFragment avec du texte d'exemple
    auto fragment = MakeObject<TextFragment>("Texte avec décoration de soulignement");
    // Définir la police pour TextFragment
    fragment->get_TextState()->set_Font(FontRepository::FindFont(u"DejaVu Serif"));
    fragment->get_TextState()->set_FontSize(10);

    // Définir la mise en forme du texte comme souligné
    fragment->get_TextState()->set_Underline(true);

    // Spécifiez la position où TextFragment doit être placé
    fragment->set_Position(MakeObject<Position>(10, 800));

    auto tb = MakeObject<TextBuilder>(page);
    // Ajouter TextFragment au fichier PDF
    tb->AppendText(fragment);

    // Enregistrer le document PDF résultant.
    document->Save(_dataDir + outputFileName);
}
```

## Comment ajouter une bordure autour du texte ajouté

Vous avez le contrôle sur l'apparence du texte que vous ajoutez. L'exemple ci-dessous montre comment ajouter une bordure autour d'un texte que vous avez ajouté en dessinant un rectangle autour de celui-ci. Découvrez-en plus sur la classe [PdfContentEditor](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.facades.pdf_content_editor/).

```cpp
void AddBorderAroundAddedText() {

    String _dataDir("C:\\Samples\\");

    // Chaîne pour le nom du fichier d'entrée
    String inputFileName("sample.pdf");

    // Chaîne pour le nom du fichier de sortie
    String outputFileName("AddingBorderAroundAddedText_out.pdf");

    auto editor = MakeObject<Aspose::Pdf::Facades::PdfContentEditor>();

    editor->BindPdf(_dataDir + inputFileName);
    auto lineInfo = MakeObject<Aspose::Pdf::Facades::LineInfo>();

    lineInfo->set_LineWidth(2);
    lineInfo->set_VerticeCoordinate(MakeArray<float>({ 0, 0, 100, 100, 50, 100 }));
    lineInfo->set_Visibility(true);
    auto rect = MakeObject<System::Drawing::Rectangle>(0, 0, 0, 0);
    editor->CreatePolygon(lineInfo, 1, System::Drawing::Rectangle(0, 0, 0, 0), String::Empty);

    // Enregistrer le document PDF résultant.
    editor->Save(_dataDir + outputFileName);
}
```

## Comment ajouter un saut de ligne

Pour ajouter du texte avec un saut de ligne, veuillez utiliser [TextFragment](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.text.text_fragment) avec [TextParagraph](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.text.text_paragraph).

L'extrait de code suivant vous montre comment ajouter un saut de ligne dans votre fichier PDF :

```cpp
void AddNewLineFeed() {
    String _dataDir("C:\\Samples\\");

    // Chaîne pour le nom du fichier de sortie
    String outputFileName("AddNewLineFeed_out.pdf");

    // Créer un nouvel objet document
    auto document = MakeObject<Document>();
    // Obtenir une page particulière
    auto page = document->get_Pages()->Add();

    // Initialiser un nouveau TextFragment avec du texte contenant les marqueurs de saut de ligne requis
    auto textFragment = MakeObject<TextFragment>("Nom du candidat : \r\n Joe Smoe");

    // Définir les propriétés du fragment de texte si nécessaire
    textFragment->get_TextState()->set_FontSize(12);
    textFragment->get_TextState()->set_Font(FontRepository::FindFont(u"DejaVu Serif"));
    textFragment->get_TextState()->set_BackgroundColor(Color::get_LightGray());
    textFragment->get_TextState()->set_ForegroundColor(Color::get_Red());

    // Créer un objet TextParagraph
    auto par = MakeObject<TextParagraph>();

    // Ajouter un nouveau TextFragment au paragraphe
    par->AppendLine(textFragment);

    // Définir la position du paragraphe
    par->set_Position(MakeObject<Position>(100, 600));

    // Créer un objet TextBuilder
    auto textBuilder = new TextBuilder(page);
    // Ajouter le TextParagraph en utilisant TextBuilder
    textBuilder->AppendParagraph(par);

    // Enregistrer le document PDF résultant.
    document->Save(_dataDir + outputFileName);
}
```

## Comment ajouter du texte barré

Vous pouvez utiliser la classe [TextState](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.text.text_state) pour définir la mise en forme du texte comme Gras, Italique, Souligné, et aussi, l'API a fourni les capacités de marquer la mise en forme du texte comme Barré.

Veuillez essayer d'utiliser le code suivant pour ajouter un TextFragment avec une mise en forme Barré.

```cpp
void AddStrikeOutText() {
    String _dataDir("C:\\Samples\\");

    // String pour le nom du fichier de sortie
    String outputFileName("AddStrikeOutText_out.pdf");

    // Ouvrir le document
    auto document = MakeObject<Document>();
    // Obtenir une page particulière
    auto page = document->get_Pages()->Add();

    // Créer un fragment de texte
    auto textFragment = MakeObject<TextFragment>("main text");
    textFragment->set_Position(MakeObject<Position>(100, 600));

    // Définir les propriétés du texte
    textFragment->get_TextState()->set_FontSize(12);
    textFragment->get_TextState()->set_Font(FontRepository::FindFont(u"DejaVu Serif"));
    textFragment->get_TextState()->set_BackgroundColor(Color::get_LightGray());
    textFragment->get_TextState()->set_ForegroundColor(Color::get_Red());
    // Définir la propriété Barré
    textFragment->get_TextState()->set_StrikeOut(true);
    // Marquer le texte comme Gras
    textFragment->get_TextState()->set_FontStyle(FontStyles::Bold);

    // Créer un objet TextBuilder
    auto textBuilder = MakeObject<TextBuilder>(page);
    // Ajouter le fragment de texte à la page PDF
    textBuilder->AppendText(textFragment);

    // Enregistrer le document PDF résultant.
    document->Save(_dataDir + outputFileName);
}
```

## Appliquer un ombrage en dégradé au texte

La classe [Aspose.Pdf.Color](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.color) a été encore améliorée en introduisant une nouvelle propriété de [PatternColorSpace](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.color#a8be6d8ab626d2ba6935a13a9c5b0de54), qui peut être utilisée pour spécifier des couleurs d'ombrage pour le texte. Cette nouvelle propriété ajoute différents ombrages en dégradé au texte, par exemple, ombrage axial, ombrage radial (Type 3) comme illustré dans l'extrait de code suivant :

```cpp
void ApplyGradientShading() {

    String _dataDir("C:\\Samples\\");

    // Chaîne pour le nom de fichier d'entrée
    String inputFileName("sample.pdf");

    // Chaîne pour le nom de fichier de sortie
    String outputFileName("ApplyGradientShading_out.pdf");

    // Ouvrir le document
    auto document = MakeObject<Document>(_dataDir + inputFileName);

    auto absorber = MakeObject<TextFragmentAbsorber>("always print correctly");

    document->get_Pages()->Accept(absorber);

    auto textFragment = absorber->get_TextFragments()->idx_get(1);

    auto foregroundColor = MakeObject<Aspose::Pdf::Color>();
    foregroundColor->set_PatternColorSpace(MakeObject<Aspose::Pdf::Drawing::GradientAxialShading>(Color::get_Red(), Color::get_Blue()));

    // Créer une nouvelle couleur avec l'espace de couleurs de motif
    textFragment->get_TextState()->set_ForegroundColor(foregroundColor);

    textFragment->get_TextState()->set_Underline(true);

    document->Save(_dataDir + outputFileName);

}
```

>Pour appliquer un dégradé radial, vous pouvez définir la propriété 'PatternColorSpace' égale à 'Aspose.Pdf.Drawing.GradientRadialShading(startingColor, endingColor)' dans l'extrait de code ci-dessus.

## Comment aligner le texte avec le contenu flottant

Aspose.PDF prend en charge le réglage de l'alignement du texte pour les contenus à l'intérieur d'un élément Floating Box. Les propriétés d'alignement de l'instance [Aspose.Pdf.FloatingBox](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.floating_box) peuvent être utilisées pour y parvenir comme indiqué dans l'exemple de code suivant.

```cpp
void ApplyGradientShadingRadial() {

    String _dataDir("C:\\Samples\\");

    // Chaîne pour le nom du fichier d'entrée
    String inputFileName("sample.pdf");

    // Chaîne pour le nom du fichier de sortie
    String outputFileName("ApplyGradientShadingRadial_out.pdf");

    auto document = MakeObject<Document>(_dataDir + inputFileName);

    auto absorber = MakeObject<TextFragmentAbsorber>(u"always print correctly");
    document->get_Pages()->Accept(absorber);

    auto textFragment = absorber->get_TextFragments()->idx_get(1);

    auto foregroundColor = MakeObject<Aspose::Pdf::Color>();
    foregroundColor->set_PatternColorSpace(MakeObject<Aspose::Pdf::Drawing::GradientRadialShading>(Color::get_Red(), Color::get_Blue()));

    // Créer une nouvelle couleur avec un espace colorimétrique de motif
    textFragment->get_TextState()->set_ForegroundColor(foregroundColor);

    textFragment->get_TextState()->set_Underline(true);

    document->Save(_dataDir + outputFileName);
}
```