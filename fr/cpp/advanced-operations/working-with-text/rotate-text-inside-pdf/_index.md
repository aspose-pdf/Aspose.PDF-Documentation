---
title: Tourner le texte à l'intérieur du PDF en utilisant C++
linktitle: Tourner le texte à l'intérieur du PDF
type: docs
weight: 50
url: fr/cpp/rotate-text-inside-pdf/
description: Découvrez différentes façons de faire pivoter le texte vers le PDF. Aspose.PDF vous permet de faire pivoter le texte à n'importe quel angle, de faire pivoter un fragment de texte ou un paragraphe entier.
lastmod: "2021-12-13"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Tourner le texte à l'intérieur du PDF en utilisant la propriété de rotation

En utilisant la propriété Rotation de la classe [TextFragment](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.text.text_fragment/), vous pouvez faire pivoter le texte à divers angles. La rotation du texte peut être utilisée dans différents scénarios de génération de documents. Vous pouvez spécifier l'angle de rotation en degrés pour faire pivoter le texte selon vos besoins. Veuillez vérifier les différents scénarios suivants, dans lesquels vous pouvez implémenter la rotation du texte.

## Implémenter la rotation en utilisant TextFragment et TextBuilder

```cpp
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Text;

void ImplementRotationUsingTextFragmentAndTextBuilder() {

    String _dataDir("C:\\Samples\\");

    // Initialize document object
    auto document = MakeObject<Document>();
    // Get particular page
    auto page = document->get_Pages()->Add();
    // Create text fragment
    auto textFragment1 = MakeObject<TextFragment>("main text");
    textFragment1->set_Position(MakeObject<Position>(100, 600));

    // Set text properties
    textFragment1->get_TextState()->set_FontSize(12);
    textFragment1->get_TextState()->set_Font(FontRepository::FindFont(u"TimesNewRoman"));

    // Create rotated text fragment
    auto textFragment2 = MakeObject<TextFragment>("rotated text");
    textFragment2->set_Position(MakeObject<Position>(200, 600));
    // Set text properties
    textFragment2->get_TextState()->set_FontSize(12);
    textFragment2->get_TextState()->set_Font(FontRepository::FindFont(u"TimesNewRoman"));
    textFragment2->get_TextState()->set_Rotation(45);

    // Create rotated text fragment
    auto textFragment3 = MakeObject<TextFragment>("rotated text");
    textFragment3->set_Position(MakeObject<Position>(300, 600));

    // Set text properties
    textFragment3->get_TextState()->set_FontSize(12);
    textFragment3->get_TextState()->set_Font(FontRepository::FindFont(u"TimesNewRoman"));
    textFragment3->get_TextState()->set_Rotation(90);

    // create TextBuilder object
    auto textBuilder = MakeObject<TextBuilder>(page);
    // Append the text fragment to the PDF page
    textBuilder->AppendText(textFragment1);
    textBuilder->AppendText(textFragment2);
    textBuilder->AppendText(textFragment3);

    // Save document
    document->Save(_dataDir + u"TextFragmentTests_Rotated1_out.pdf");
}
```

## Implémenter la rotation en utilisant TextParagraph et TextBuilder (Fragments Tournés)

```cpp
void ImplementRotationUsingTextParagraphAndTextBuilder_RotatedFragments() {

    String _dataDir("C:\\Samples\\");

    // Initialiser l'objet document
    auto document = MakeObject<Document>();
    // Obtenir une page particulière
    auto page = document->get_Pages()->Add();
    auto paragraph = MakeObject<TextParagraph>();
    paragraph->set_Position(MakeObject<Position>(200, 600));

    // Créer un fragment de texte
    auto textFragment1 = MakeObject<TextFragment>("texte tourné");
    // Définir les propriétés du texte
    textFragment1->get_TextState()->set_FontSize(12);
    textFragment1->get_TextState()->set_Font(FontRepository::FindFont(u"TimesNewRoman"));
    // Définir la rotation
    textFragment1->get_TextState()->set_Rotation(45);

    // Créer un fragment de texte
    auto textFragment2 = MakeObject<TextFragment>("texte principal");
    // Définir les propriétés du texte
    textFragment2->get_TextState()->set_FontSize(12);
    textFragment2->get_TextState()->set_Font(FontRepository::FindFont(u"TimesNewRoman"));

    // Créer un fragment de texte
    auto textFragment3 = MakeObject<TextFragment>("un autre texte tourné");
    // Définir les propriétés du texte
    textFragment3->get_TextState()->set_FontSize(12);
    textFragment3->get_TextState()->set_Font(FontRepository::FindFont(u"TimesNewRoman"));
    // Définir la rotation
    textFragment3->get_TextState()->set_Rotation(-45);

    // Ajouter les fragments de texte au paragraphe
    paragraph->AppendLine(textFragment1);
    paragraph->AppendLine(textFragment2);
    paragraph->AppendLine(textFragment3);
    // Créer un objet TextBuilder
    auto textBuilder = MakeObject<TextBuilder>(page);
    // Ajouter le paragraphe de texte à la page PDF
    textBuilder->AppendParagraph(paragraph);
    // Enregistrer le document
    document->Save(_dataDir + u"TextFragmentTests_Rotated2_out.pdf");

}
```

## Implémenter la Rotation en utilisant TextFragment et Page.Paragraphs

```cpp
void ImplementRotationUsingTextFragmentAndPageParagraphs() {

    String _dataDir("C:\\Samples\\");

    // Initialiser l'objet document
    auto document = MakeObject<Document>();
    // Obtenir une page particulière
    auto page = document->get_Pages()->Add();
    // Créer un fragment de texte
    auto textFragment1 = MakeObject<TextFragment>("texte principal");
    // Définir les propriétés du texte
    textFragment1->get_TextState()->set_FontSize(12);
    textFragment1->get_TextState()->set_Font(FontRepository::FindFont(u"TimesNewRoman"));

    // Créer un fragment de texte
    auto textFragment2 = MakeObject<TextFragment>("texte tourné");

    // Définir les propriétés du texte
    textFragment2->get_TextState()->set_FontSize(12);
    textFragment2->get_TextState()->set_Font(FontRepository::FindFont(u"TimesNewRoman"));

    // Définir la rotation
    textFragment2->get_TextState()->set_Rotation(315);

    // Créer un fragment de texte
    auto textFragment3 = MakeObject<TextFragment>("texte tourné");
    // Définir les propriétés du texte
    textFragment3->get_TextState()->set_FontSize(12);
    textFragment3->get_TextState()->set_Font(FontRepository::FindFont(u"TimesNewRoman"));

    // Définir la rotation
    textFragment3->get_TextState()->set_Rotation(270);
    page->get_Paragraphs()->Add(textFragment1);
    page->get_Paragraphs()->Add(textFragment2);
    page->get_Paragraphs()->Add(textFragment3);

    // Enregistrer le document
    document->Save(_dataDir + u"TextFragmentTests_Rotated3_out.pdf");
}
```

## Implémenter la Rotation en utilisant TextParagraph et TextBuilder (Tout le Paragraphe est Tourné)

```cpp
void ImplementRotationUsingTextParagraphAndTextBuilder() {

    String _dataDir("C:\\Samples\\");

    // Initialiser l'objet document
    auto document = MakeObject<Document>();
    // Obtenir une page particulière
    auto page = document->get_Pages()->Add();
    for (int i = 0; i < 4; i++) {
        auto paragraph = MakeObject<TextParagraph>();
        paragraph->set_Position(MakeObject<Position>(200, 600));
        // Spécifier la rotation
        paragraph->set_Rotation(i * 90 + 45);
        // Créer un fragment de texte
        auto textFragment1 = MakeObject<TextFragment>("Texte du paragraphe");
        // Créer un fragment de texte
        textFragment1->get_TextState()->set_FontSize(12);
        textFragment1->get_TextState()->set_Font(FontRepository::FindFont(u"TimesNewRoman"));
        textFragment1->get_TextState()->set_BackgroundColor(Color::get_LightGray());
        textFragment1->get_TextState()->set_ForegroundColor(Color::get_Blue());

        // Créer un fragment de texte
        auto textFragment2 = MakeObject<TextFragment>("Deuxième ligne de texte");
        // Définir les propriétés du texte
        textFragment2->get_TextState()->set_FontSize(12);
        textFragment2->get_TextState()->set_Font(FontRepository::FindFont(u"TimesNewRoman"));
        textFragment2->get_TextState()->set_BackgroundColor(Color::get_LightGray());
        textFragment2->get_TextState()->set_ForegroundColor(Color::get_Blue());

        // Créer un fragment de texte
        auto textFragment3 = MakeObject<TextFragment>("Et encore un peu de texte...");
        // Définir les propriétés du texte
        textFragment3->get_TextState()->set_FontSize(12);
        textFragment3->get_TextState()->set_Font(FontRepository::FindFont(u"TimesNewRoman"));
        textFragment3->get_TextState()->set_BackgroundColor(Color::get_LightGray());
        textFragment3->get_TextState()->set_ForegroundColor(Color::get_Blue());
        textFragment3->get_TextState()->set_Underline(true);

        paragraph->AppendLine(textFragment1);
        paragraph->AppendLine(textFragment2);
        paragraph->AppendLine(textFragment3);
        // Créer un objet TextBuilder
        auto textBuilder = MakeObject<TextBuilder>(page);
        // Ajouter le fragment de texte à la page PDF
        textBuilder->AppendParagraph(paragraph);
    }
    // Enregistrer le document
    document->Save(_dataDir + u"TextFragmentTests_Rotated4_out.pdf");
}
```