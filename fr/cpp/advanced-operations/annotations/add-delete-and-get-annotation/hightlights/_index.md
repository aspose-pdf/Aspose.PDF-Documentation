---
title: Annotation de surlignage PDF en C++
linktitle: Annotation de surlignage
type: docs
weight: 20
url: /fr/cpp/highlights-annotation/
description: Les annotations de balisage sont présentées dans le texte sous forme de surlignages, soulignements, barrés ou soulignements en zigzag dans le texte d'un document.
lastmod: "2021-11-24"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

Les annotations de balisage de texte doivent être affichées dans le texte du document sous forme de surlignage, soulignement, barré ou soulignement en zigzag. Lorsqu'elles sont ouvertes, elles doivent afficher une fenêtre contextuelle contenant le texte de la note correspondante.

Vous pouvez modifier les propriétés des annotations de balisage de texte dans un PDF en utilisant la fenêtre Propriétés fournie dans le contrôle du visualiseur PDF. Vous pouvez changer la couleur, l'opacité, l'auteur et le thème des annotations de balisage de texte.

Vous pouvez obtenir ou définir les paramètres d'annotation de surlignage en utilisant la propriété highlightSettings. La propriété highlightSettings est utilisée pour définir les propriétés de couleur, d'opacité, d'auteur, de thème, de date de modification et de verrouillage pour les annotations de surbrillance.

Il est également possible d'obtenir ou de définir les paramètres d'annotation de barré en utilisant la propriété strikethroughSettings. La propriété strikethroughSettings est utilisée pour définir les propriétés de couleur, d'opacité, d'auteur, de thème, de date de modification et de verrouillage des annotations de barré.

La prochaine fonctionnalité est la possibilité d'obtenir ou de définir les paramètres pour les annotations de soulignement en utilisant la propriété underlineSettings. La propriété underlineSettings est utilisée pour définir les propriétés de couleur, d'opacité, d'auteur, de thème, de date de modification et de verrouillage pour les annotations de soulignement.

## Ajouter une Annotation de Mise en Évidence de Texte

Afin d'ajouter une Annotation de Mise en Évidence de Texte au document PDF, nous devons effectuer les actions suivantes :

1. Charger le fichier PDF - nouvel objet [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document).
1. Créer des annotations :

    - [HighlightAnnotation](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.highlight_annotation) et définir les paramètres (titre, couleur).- [StrikeOutAnnotation](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.strike_out_annotation) et définir les paramètres (titre, couleur).
- [SquigglyAnnotation](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.squiggly_annotation) et définir les paramètres (titre, couleur).
- [UnderlineAnnotation](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.underline_annotation) et définir les paramètres (titre, couleur).

1. Après, nous devrions ajouter toutes les annotations à la page.

```cpp
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Text;

void TextMarkupAnnotations::AddTextMarkupAnnotation()
{
    String _dataDir("C:\\Samples\\");

    try
    {
        // Charger le fichier PDF
        auto document = MakeObject<Document>(_dataDir + u"sample.pdf");
        auto tfa = MakeObject<Aspose::Pdf::Text::TextFragmentAbsorber>(u"PDF");
        tfa->Visit(document->get_Pages()->idx_get(1));

        //Créer des annotations
        auto highlightAnnotation = MakeObject<Aspose::Pdf::Annotations::HighlightAnnotation>(
        document->get_Pages()->idx_get(1),
        tfa->get_TextFragments()->idx_get(1)->get_Rectangle());
        highlightAnnotation->set_Title(u"Utilisateur Aspose");
        highlightAnnotation->set_Color(Color::get_LightGreen());

        auto strikeOutAnnotation = MakeObject<Aspose::Pdf::Annotations::StrikeOutAnnotation>(
        document->get_Pages()->idx_get(1),
        tfa->get_TextFragments()->idx_get(2)->get_Rectangle());
        strikeOutAnnotation->set_Title(u"Utilisateur Aspose");
        strikeOutAnnotation->set_Color(Color::get_Blue());

        auto squigglyAnnotation = MakeObject<Aspose::Pdf::Annotations::SquigglyAnnotation>(
        document->get_Pages()->idx_get(1),
        tfa->get_TextFragments()->idx_get(3)->get_Rectangle());
        squigglyAnnotation->set_Title(u"Utilisateur Aspose");
        squigglyAnnotation->set_Color(Color::get_Blue());

        auto underlineAnnotation = MakeObject<Aspose::Pdf::Annotations::UnderlineAnnotation>(
        document->get_Pages()->idx_get(1),
        tfa->get_TextFragments()->idx_get(4)->get_Rectangle());
        underlineAnnotation->set_Title(u"Utilisateur Aspose");
        underlineAnnotation->set_Color(Color::get_Blue());

        // Ajouter l'annotation à la page
        document->get_Pages()->idx_get(1)->get_Annotations()->Add(highlightAnnotation);
        document->get_Pages()->idx_get(1)->get_Annotations()->Add(squigglyAnnotation);
        document->get_Pages()->idx_get(1)->get_Annotations()->Add(strikeOutAnnotation);
        document->get_Pages()->idx_get(1)->get_Annotations()->Add(underlineAnnotation);
        document->Save(_dataDir + u"sample_mod.pdf");
    }
    catch (Exception ex)
    {
        Console::WriteLine(ex->get_Message());
    }
}
```

Si vous voulez mettre en évidence un fragment multi-lignes, vous devriez utiliser l'exemple avancé :

```cpp
/// <summary>
/// Exemple avancé pour mettre en évidence un fragment multi-lignes
/// </summary>

System::SmartPtr<Aspose::Pdf::Annotations::HighlightAnnotation> HighLightTextFragment(
    System::SmartPtr<Aspose::Pdf::Page> page,
    System::SmartPtr<TextFragment> textFragment,
    System::SharedPtr<Color> color);

void TextMarkupAnnotations::AddHighlightAnnotationAdvanced()
{
    String _dataDir("C:\\Samples\\");

    auto document = MakeObject<Document>(_dataDir + u"sample_mod.pdf");
    auto page = document->get_Pages()->idx_get(1);

    auto tfa = MakeObject<TextFragmentAbsorber>(
        u"Adobe\\W+Acrobat\\W+Reader",
        MakeObject<Aspose::Pdf::Text::TextSearchOptions>(true));

    tfa->Visit(page);

    for (auto textFragment : tfa->get_TextFragments())
    {
        auto highlightAnnotation = HighLightTextFragment(page, textFragment, Color::get_Yellow());
        page->get_Annotations()->Add(highlightAnnotation);
    }
    document->Save(_dataDir + u"sample_mod.pdf");
}


System::SmartPtr<Aspose::Pdf::Annotations::HighlightAnnotation> HighLightTextFragment(
    System::SmartPtr<Aspose::Pdf::Page> page,
    System::SmartPtr<TextFragment> textFragment,
    System::SharedPtr<Color> color)
{
    if (textFragment->get_Segments()->get_Count() == 1)
    {
        auto ha = MakeObject<Aspose::Pdf::Annotations::HighlightAnnotation>
        (page, textFragment->get_Segments()->idx_get(1)->get_Rectangle());
        ha->set_Title(u"Utilisateur Aspose");
        ha->set_Color(color);

        ha->set_Modified(DateTime::get_Now());

        auto quadPoints = MakeArray<System::SharedPtr<Point>>(4);

        quadPoints[0] = MakeObject<Point>(textFragment->get_Segments()->idx_get(1)->get_Rectangle()->get_LLX(),
        textFragment->get_Segments()->idx_get(1)->get_Rectangle()->get_URY());
        quadPoints[1] = MakeObject<Point>(textFragment->get_Segments()->idx_get(1)->get_Rectangle()->get_URX(),
        textFragment->get_Segments()->idx_get(1)->get_Rectangle()->get_URY());
        quadPoints[2] = MakeObject<Point>(textFragment->get_Segments()->idx_get(1)->get_Rectangle()->get_LLX(),
        textFragment->get_Segments()->idx_get(1)->get_Rectangle()->get_LLY());
        quadPoints[3] = MakeObject<Point>(textFragment->get_Segments()->idx_get(1)->get_Rectangle()->get_URX(),
        textFragment->get_Segments()->idx_get(1)->get_Rectangle()->get_LLY());
        ha->set_QuadPoints(quadPoints);
        return ha;
    }

    auto offset = 0;
    auto quadPoints = MakeArray<System::SharedPtr<Point>>(textFragment->get_Segments()->get_Count() * 4);

    for (auto segment : textFragment->get_Segments())
    {
        quadPoints[offset + 0] = MakeObject<Point>(segment->get_Rectangle()->get_LLX(), segment->get_Rectangle()->get_URY());
        quadPoints[offset + 1] = MakeObject<Point>(segment->get_Rectangle()->get_URX(), segment->get_Rectangle()->get_URY());
        quadPoints[offset + 2] = MakeObject<Point>(segment->get_Rectangle()->get_LLX(), segment->get_Rectangle()->get_LLY());
        quadPoints[offset + 3] = MakeObject<Point>(segment->get_Rectangle()->get_URX(), segment->get_Rectangle()->get_LLY());
        offset += 4;
    }

    double llx = quadPoints[0]->get_X();
    double lly = quadPoints[0]->get_Y();
    double urx = quadPoints[0]->get_X();
    double ury = quadPoints[0]->get_Y();
    for (auto &pt : quadPoints) {
        if (llx > pt->get_X())
        llx = pt->get_X();
        if (lly > pt->get_Y())
        lly = pt->get_Y();
        if (urx < pt->get_X())
        urx = pt->get_X();
        if (ury < pt->get_Y())
        ury = pt->get_Y();
    }

    auto ha = MakeObject<Aspose::Pdf::Annotations::HighlightAnnotation>
        (page, textFragment->get_Segments()->idx_get(1)->get_Rectangle());
    ha->set_Title(u"Utilisateur Aspose");
    ha->set_Color(color);

    ha->set_Modified(DateTime::get_Now());

    ha->set_QuadPoints(quadPoints);
    return ha;
}


/// <summary>
/// Comment obtenir un texte surligné
/// </summary>
void TextMarkupAnnotations::GetHighlightedText()
{
    String _dataDir("C:\\Samples\\");

    // Charger le fichier PDF
    auto document = MakeObject<Document>(_dataDir + u"sample_mod.pdf");
    auto page = document->get_Pages()->idx_get(1);
    auto annotationSelector = MakeObject<Aspose::Pdf::Annotations::AnnotationSelector>(
        MakeObject<Aspose::Pdf::Annotations::HighlightAnnotation>(page, Rectangle::get_Trivial()));

    for (auto ta : annotationSelector->get_Selected())
    {
        auto ha = System::DynamicCast<Aspose::Pdf::Annotations::HighlightAnnotation>(ta);
        Console::WriteLine(ha->GetMarkedText());
    }
}
```

## Obtenir l'annotation de balisage de texte

Veuillez essayer d'utiliser le code suivant pour obtenir l'annotation de balisage de texte à partir d'un document PDF.

```cpp
void TextMarkupAnnotations::GetTextMarkupAnnotation()
{
    String _dataDir("C:\\Samples\\");

    // Charger le fichier PDF
    auto document = MakeObject<Document>(_dataDir + u"sample_mod.pdf");
    auto page = document->get_Pages()->idx_get(1);

    auto annotationSelector = MakeObject<Aspose::Pdf::Annotations::AnnotationSelector>(
        MakeObject<Aspose::Pdf::Annotations::HighlightAnnotation>(page, Rectangle::get_Trivial()));

    for (auto ta : annotationSelector->get_Selected())
    {
        Console::WriteLine(u"{0} {1}", ta->get_AnnotationType(), ta->get_Rect());
    }
}
```

## Supprimer l'annotation de balisage de texte

Le code suivant montre comment supprimer l'annotation de balisage de texte d'un fichier PDF.

```cpp
void TextMarkupAnnotations::DeleteTextMarkupAnnotation() {

    String _dataDir("C:\\Samples\\");

    // Charger le fichier PDF
    auto document = MakeObject<Document>(_dataDir + u"sample_mod.pdf");
    auto page = document->get_Pages()->idx_get(1);

    auto annotationSelector1 = MakeObject<Aspose::Pdf::Annotations::AnnotationSelector>(
        MakeObject<Aspose::Pdf::Annotations::HighlightAnnotation>(page, Rectangle::get_Trivial()));
    page->Accept(annotationSelector1);
    auto annotationSelector2 = MakeObject<Aspose::Pdf::Annotations::AnnotationSelector>(
        MakeObject<Aspose::Pdf::Annotations::SquigglyAnnotation>(page, Rectangle::get_Trivial()));
    page->Accept(annotationSelector2);

    for (auto ta : annotationSelector1->get_Selected()) {
        page->get_Annotations()->Delete(ta);
    }
    for (auto ta : annotationSelector2->get_Selected()) {
        page->get_Annotations()->Delete(ta);
    }
    document->Save(_dataDir + u"sample_del.pdf");
}
```