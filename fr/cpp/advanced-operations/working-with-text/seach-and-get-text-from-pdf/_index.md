---
title: Rechercher et Obtenir du Texte des Pages d'un Document PDF
linktitle: Rechercher et Obtenir du Texte
type: docs
weight: 60
url: /fr/cpp/search-and-get-text-from-pdf/
description: Cet article explique comment utiliser divers outils pour rechercher et obtenir du texte à partir de documents PDF. Nous pouvons rechercher avec une expression régulière à partir de pages particulières ou de l'ensemble des pages.
lastmod: "2021-12-13"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Rechercher et Obtenir du Texte de Toutes les Pages d'un Document PDF

La classe [TextFragmentAbsorber](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.text.text_fragment_absorber/) vous permet de trouver un texte, correspondant à une phrase particulière, à partir de toutes les pages d'un document PDF. Afin de rechercher du texte dans l'ensemble du document, vous devez appeler la méthode Accept de la collection [Pages](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page). La méthode 'Accept' prend un objet TextFragmentAbsorber comme paramètre, qui renvoie une collection d'objets TextFragment.

Le code suivant vous montre comment rechercher du texte à partir de toutes les pages.

```cpp
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Text;

void SearchAndGetTextFromAllThePagesOfPDFDocument() {
    String _dataDir("C:\\Samples\\");

    auto document = new Document(_dataDir + u"sample.pdf");

    // Créer un objet TextAbsorber pour trouver toutes les instances de la phrase de recherche entrée
    auto textFragmentAbsorber = MakeObject<TextFragmentAbsorber>("document");

    // Accepter l'absorbeur pour toutes les pages
    document->get_Pages()->Accept(textFragmentAbsorber);

    // Obtenez les fragments de texte extraits dans la collection
    auto textFragmentCollection = textFragmentAbsorber->get_TextFragments();

    // Parcourir les fragments
    for (auto textFragment : textFragmentCollection) {
        Console::WriteLine(u"Texte :- {0}", textFragment->get_Text());
        Console::WriteLine(u"Position :- {0}", textFragment->get_Position());
        Console::WriteLine(u"XIndent :- {0}", textFragment->get_Position()->get_XIndent());
        Console::WriteLine(u"YIndent :- {0}", textFragment->get_Position()->get_YIndent());
        Console::WriteLine(u"Police - Nom :- {0}", textFragment->get_TextState()->get_Font()->get_FontName());
        Console::WriteLine(u"Police - Est accessible :- {0}", textFragment->get_TextState()->get_Font()->get_IsAccessible());
        Console::WriteLine(u"Police - Est intégrée - {0}", textFragment->get_TextState()->get_Font()->get_IsEmbedded());
        Console::WriteLine(u"Police - Est sous-ensemble :- {0}", textFragment->get_TextState()->get_Font()->get_IsSubset());
        Console::WriteLine(u"Taille de la police :- {0}", textFragment->get_TextState()->get_FontSize());
        Console::WriteLine(u"Couleur de premier plan :- {0}", textFragment->get_TextState()->get_ForegroundColor());
    }
}
```

## Recherche et extraction de texte de toutes les pages à l'aide d'une expression régulière

TextFragmentAbsorber vous aide à rechercher et récupérer du texte, de toutes les pages, en fonction d'une expression régulière. D'abord, vous devez passer une expression régulière au constructeur [TextFragmentAbsorber](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.text.text_fragment_absorber/) comme la phrase. Après cela, vous devez définir la propriété [TextSearchOptions](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.text.text_search_options/) de l'objet TextFragmentAbsorber. Cette propriété nécessite un objet TextSearchOptions et vous devez passer true en tant que paramètre à son constructeur lors de la création de nouveaux objets. Comme vous voulez récupérer le texte correspondant de toutes les pages, vous devez appeler la méthode Accept de la collection Pages. [TextFragmentAbsorber](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.text.text_fragment_absorber/) renvoie une TextFragmentCollection contenant tous les fragments correspondant aux critères spécifiés par l'expression régulière. L'extrait de code suivant vous montre comment rechercher et obtenir du texte de toutes les pages en fonction d'une expression régulière.

```cpp
void SearchAndGetTextFromPagesUsingRegularExpression()
{
    String _dataDir("C:\\Samples\\");

    auto document = new Document(_dataDir + u"sample.pdf");

    // Créer un objet TextAbsorber pour trouver toutes les instances de la phrase de recherche saisie
    auto textFragmentAbsorber = MakeObject<TextFragmentAbsorber>(u"\\d{4}-\\d{4}"); // comme 1999-2000

    // Définir l'option de recherche de texte pour spécifier l'utilisation d'expressions régulières
    auto textSearchOptions = MakeObject<TextSearchOptions>(true);
    textFragmentAbsorber->set_TextSearchOptions(textSearchOptions);

    // Accepter l'absorbeur pour la première page du document
    document->get_Pages()->Accept(textFragmentAbsorber);

    // Obtenir les fragments de texte extraits dans la collection
    auto textFragmentCollection = textFragmentAbsorber->get_TextFragments();

    // Parcourir les fragments
    for (auto textFragment : textFragmentCollection) {
        Console::WriteLine(u"Texte :- {0}", textFragment->get_Text());
        Console::WriteLine(u"Position :- {0}", textFragment->get_Position());
        Console::WriteLine(u"XIndent :- {0}", textFragment->get_Position()->get_XIndent());
        Console::WriteLine(u"YIndent :- {0}", textFragment->get_Position()->get_YIndent());
        Console::WriteLine(u"Police - Nom :- {0}", textFragment->get_TextState()->get_Font()->get_FontName());
        Console::WriteLine(u"Police - Est accessible :- {0}", textFragment->get_TextState()->get_Font()->get_IsAccessible());
        Console::WriteLine(u"Police - Est intégrée - {0}", textFragment->get_TextState()->get_Font()->get_IsEmbedded());
        Console::WriteLine(u"Police - Est sous-ensemble :- {0}", textFragment->get_TextState()->get_Font()->get_IsSubset());
        Console::WriteLine(u"Taille de la police :- {0}", textFragment->get_TextState()->get_FontSize());
        Console::WriteLine(u"Couleur de premier plan :- {0}", textFragment->get_TextState()->get_ForegroundColor());
    }
}
```