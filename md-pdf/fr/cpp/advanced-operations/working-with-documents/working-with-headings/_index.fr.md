---
title: Travailler avec les en-têtes dans PDF
type: docs
weight: 90
url: /cpp/working-with-headings/
lastmod: "2021-11-11"
description: Créez une numérotation dans l'en-tête de votre document PDF avec C++. Aspose.PDF pour C++ montre différents styles de numérotation.
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Appliquer un style de numérotation dans l'en-tête

Tout texte dans un document commence par un en-tête. Les en-têtes sont une partie intégrante du contenu, quel que soit le style et le thème.
Les en-têtes aident à attirer l'attention sur le texte et aident les utilisateurs à trouver l'information dont ils ont besoin dans le document, améliorant ainsi la lisibilité et la perception visuelle. En utilisant des styles d'en-tête, vous pouvez également créer rapidement une table des matières, modifier la structure du document.
Alors, voyons comment travailler avec les en-têtes en utilisant la bibliothèque Aspose.PDF pour C++.

[Aspose.PDF pour C++](/pdf/cpp/) offre de nombreux styles de numérotation prédéfinis. Ces styles de numérotation prédéfinis sont stockés dans une énumération, NumberingStyle. Les valeurs prédéfinies de l'énumération NumberingStyle et leurs descriptions sont données ci-dessous :

|**Types de Titres**|**Description**|
| :- | :- |
|NumeralsArabic|Type arabe, par exemple, 1,1.1,...|
|NumeralsRomanUppercase|Type romain majuscule, par exemple, I,I.II, ...|
|NumeralsRomanLowercase|Type romain minuscule, par exemple, i,i.ii, ...|
|LettersUppercase|Type anglais majuscule, par exemple, A,A.B, ...|
|LettersLowercase|Type anglais minuscule, par exemple, a,a.b, ...|
La propriété **Style** de la classe **Aspose.PDF.Heading** est utilisée pour définir les styles de numérotation des titres.

|**Figure: Styles de numérotation prédéfinis**|
| :- |
Le code source, pour obtenir la sortie montrée dans la figure ci-dessus, est donné ci-dessous dans l'exemple.

```cpp
void WorkingWithHeadingsInPDF() {
    // Chaîne pour le nom du chemin
    String _dataDir("C:\\Samples\\");

    // Chaîne pour le nom du fichier d'entrée
    String outputFileName("ApplyNumberStyle_out.pdf");

    // Ouvrir le document
    auto document = MakeObject<Document>();

    document->get_PageInfo()->set_Width(612.0);
    document->get_PageInfo()->set_Height(792.0);
    document->get_PageInfo()->set_Margin (MakeObject<MarginInfo>());
    document->get_PageInfo()->get_Margin()->set_Left(72);
    document->get_PageInfo()->get_Margin()->set_Right(72);
    document->get_PageInfo()->get_Margin()->set_Top (72);
    document->get_PageInfo()->get_Margin()->set_Bottom (72);
            
    auto pdfPage = document->get_Pages()->Add();
    pdfPage->get_PageInfo()->set_Width (612.0);
    pdfPage->get_PageInfo()->set_Height (792.0);
    pdfPage->get_PageInfo()->set_Margin(MakeObject<MarginInfo>());
    pdfPage->get_PageInfo()->get_Margin()->set_Left(72);
    pdfPage->get_PageInfo()->get_Margin()->set_Right(72);
    pdfPage->get_PageInfo()->get_Margin()->set_Top(72);
    pdfPage->get_PageInfo()->get_Margin()->set_Bottom(72);

    auto floatBox = MakeObject<FloatingBox>();
    floatBox->set_Margin(pdfPage->get_PageInfo()->get_Margin());

    pdfPage->get_Paragraphs()->Add(floatBox);

    auto textFragment = MakeObject<TextFragment>();
    auto segment = MakeObject<TextSegment>();

    auto heading = MakeObject<Heading>(1);
    heading->set_IsInList(true);
    heading->set_StartNumber(1);
    heading->set_Text (u"Liste 1");
    heading->set_Style(NumberingStyle::NumeralsRomanLowercase);
    heading->set_IsAutoSequence(true);

    floatBox->get_Paragraphs()->Add(heading);

    auto heading2 = MakeObject<Heading>(1);
    heading2->set_IsInList (true);
    heading2->set_StartNumber(13);
    heading2->set_Text (u"Liste 2");
    heading2->set_Style(NumberingStyle::NumeralsRomanLowercase);
    heading2->set_IsAutoSequence(true);;

    floatBox->get_Paragraphs()->Add(heading2);

    auto heading3 = MakeObject<Heading>(2);
    heading3->set_IsInList (true);
    heading3->set_StartNumber(1);
    heading3->set_Text (u"la valeur, à la date d'effet du plan, des biens à distribuer selon le plan en raison de chaque autorisation");
    heading3->set_Style(NumberingStyle::LettersLowercase);
    heading3->set_IsAutoSequence(true);

    floatBox->get_Paragraphs()->Add(heading3); 

    // Enregistrer le fichier de sortie concaténé
    document->Save(_dataDir + outputFileName);
}
```