---
title: Infobulle PDF en utilisant C++
linktitle: Infobulle PDF
type: docs
weight: 20
url: /fr/cpp/pdf-tooltip/
description: Apprenez à ajouter une infobulle à un fragment de texte dans un PDF en utilisant C++ et Aspose.PDF
lastmod: "2021-12-13"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Ajouter une Infobulle au Texte Recherché en ajoutant un Bouton Invisible

Cet article montre comment ajouter une infobulle au texte d'un document PDF existant en C++. Aspose.PDF prend en charge la création d'infobulles en ajoutant un bouton invisible sur le texte recherché du fichier PDF.

```cpp
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Text;


void AddTooltipToSearchedText() {

    String _dataDir("C:\\Samples\\");

    // Chaîne pour le nom du fichier de sortie
    String outputFileName("Tooltip_out.pdf");

    // Créer un document d'exemple avec du texte
    auto document = MakeObject<Document>();
    document->get_Pages()->Add()->get_Paragraphs()->Add(MakeObject<TextFragment>("Déplacez le curseur de la souris ici pour afficher une infobulle"));

    document->get_Pages()->idx_get(1)->get_Paragraphs()->Add(MakeObject<TextFragment>("Déplacez le curseur de la souris ici pour afficher une infobulle très longue"));

    document->Save(outputFileName);

    // Ouvrir le document avec du texte
    auto document = MakeObject<Document>(outputFileName);
    // Créer un objet TextAbsorber pour trouver toutes les phrases correspondant à l'expression régulière
    auto absorber = MakeObject<TextFragmentAbsorber>("Déplacez le curseur de la souris ici pour afficher une infobulle");
    // Accepter l'absorbeur pour les pages du document
    document->get_Pages()->Accept(absorber);

    // Obtenir les fragments de texte extraits
    auto textFragments = absorber->get_TextFragments();

    // Parcourir les fragments
    for(auto fragment : textFragments)
    {
        // Créer un bouton invisible à la position du fragment de texte
        auto field = MakeObject<Aspose::Pdf::Forms::ButtonField>(fragment->get_Page(), fragment->get_Rectangle());
        // La valeur AlternateName sera affichée comme infobulle par une application de visualisation
        field->set_AlternateName (u"Infobulle pour le texte.");
        // Ajouter le champ du bouton au document
        document->get_Form()->Add(System::DynamicCast<Aspose::Pdf::Forms::Field>(field));
    }

    // Ensuite, un exemple d'infobulle très longue
    absorber = MakeObject<TextFragmentAbsorber>("Déplacez le curseur de la souris ici pour afficher une infobulle très longue");
    document->get_Pages()->Accept(absorber);
    textFragments = absorber->get_TextFragments();

    for(auto fragment : textFragments)
    {
        auto field = MakeObject<Aspose::Pdf::Forms::ButtonField>(fragment->get_Page(), fragment->get_Rectangle());
        // Définir un texte très long
        field->set_AlternateName(String("Lorem ipsum dolor sit amet, consectetur adipiscing elit,\
            sed do eiusmod tempor incididunt ut labore et dolore magna\
            aliqua. Ut enim ad minim veniam, quis nostrud exercitation\
            ullamco laboris nisi ut aliquip ex ea commodo consequat.\
            Duis aute irure dolor in reprehenderit in voluptate velit\
            esse cillum dolore eu fugiat nulla pariatur. Excepteur sint\
            occaecat cupidatat non proident, sunt in culpa qui officia\
            deserunt mollit anim id est laborum."));
        document->get_Form()->Add(System::DynamicCast<Aspose::Pdf::Forms::Field>(field));
    }

    // Enregistrer le document
    document->Save(outputFileName);

}
```

## Créer un Bloc de Texte Caché et l'Afficher au Survol de la Souris

Aspose.PDF pour C++ implémente une fonction d'actions de masquage, avec laquelle vous pouvez afficher/masquer un champ de texte (ou tout autre type d'annotation) lors de l'entrée/sortie de la souris sur un bouton invisible. Pour ce faire, utilisez la classe Aspose.Pdf.Annotations.HideAction pour attribuer une action de masquage/affichage au bloc de texte. Utilisez l'extrait de code suivant pour afficher/masquer le bloc de texte lors de l'entrée/sortie de la souris.

Notez également que les actions PDF sur les documents fonctionnent bien dans leurs lecteurs respectifs (comme Adobe Reader), mais ne garantissent rien pour d'autres lecteurs PDF (comme les plug-ins de navigateur web). Nous avons mené une courte enquête et avons constaté :

- Toutes les implémentations de l'action de masquage dans les documents PDF fonctionnent bien dans Internet Explorer v.11.0.
- Toutes les implémentations de l'action de masquage fonctionnent également dans Opera v.12.14, mais nous avons remarqué un certain délai de réponse lors de la première ouverture du document.

- Seule l'implémentation utilisant le constructeur HideAction acceptant le nom du champ fonctionne si Google Chrome v.61.0 affiche le document ; Veuillez utiliser les constructeurs correspondants si la navigation dans Google Chrome est significative :

>buttonField.Actions.OnEnter = new HideAction(floatingField.FullName, false);
>buttonField.Actions.OnExit = new HideAction(floatingField.FullName);

```cpp
void CreateHiddenTextBlock() {

    String _dataDir("C:\\Samples\\");

    // Chaîne pour le nom du fichier de sortie
    String outputFileName("TextBlock_HideShow_MouseOverOut_out.pdf");

    // Créer un document exemple avec du texte
    auto document = MakeObject<Document>();

    document->get_Pages()->Add()->get_Paragraphs()->Add(MakeObject<TextFragment>("Déplacez le curseur de la souris ici pour afficher le texte flottant"));
    document->Save(outputFileName);

    // Ouvrir le document avec du texte
    auto document = MakeObject<Document>(outputFileName);

    // Créer un objet TextAbsorber pour trouver toutes les phrases correspondant à l'expression régulière
    auto absorber = MakeObject<TextFragmentAbsorber>("Déplacez le curseur de la souris ici pour afficher le texte flottant");
    // Accepter l'absorbeur pour les pages du document
    document->get_Pages()->Accept(absorber);
    // Obtenir le premier fragment de texte extrait
    auto textFragments = absorber->get_TextFragments();
    auto fragment = textFragments->idx_get(1);

    // Créer un champ de texte caché pour le texte flottant dans le rectangle spécifié de la page
    auto floatingField = MakeObject<Aspose::Pdf::Forms::TextBoxField>(fragment->get_Page(), MakeObject<Rectangle>(100, 700, 220, 740));
    // Définir le texte à afficher comme valeur du champ
    floatingField->set_Value(u"Ceci est le \"champ de texte flottant\".");
    // Nous recommandons de rendre le champ 'readonly' pour ce scénario
    floatingField->set_ReadOnly(true);
    // Définir le drapeau 'hidden' pour rendre le champ invisible à l'ouverture du document
    floatingField->set_Flags(floatingField->get_Flags() | Aspose::Pdf::Annotations::AnnotationFlags::Hidden);

    // Définir un nom unique pour le champ n'est pas nécessaire mais autorisé
    floatingField->set_PartialName (u"FloatingField_1");

    // Définir les caractéristiques de l'apparence du champ n'est pas nécessaire mais l'améliore
    floatingField->set_DefaultAppearance(MakeObject<Aspose::Pdf::Annotations::DefaultAppearance>("Helv", 10, Color::get_Blue()));
    floatingField->get_Characteristics()->set_Background (System::Drawing::Color::get_LightBlue());
    floatingField->get_Characteristics()->set_Border (System::Drawing::Color::get_DarkBlue());
    floatingField->set_Border(MakeObject<Aspose::Pdf::Annotations::Border>(floatingField));
    floatingField->get_Border()->set_Width (1);
    floatingField->set_Multiline (true);

    // Ajouter un champ de texte au document
    document->get_Form()->Add(System::DynamicCast<Aspose::Pdf::Forms::Field>(floatingField));

    // Créer un bouton invisible à la position du fragment de texte
    auto buttonField = MakeObject<Aspose::Pdf::Forms::ButtonField>(fragment->get_Page(), fragment->get_Rectangle());
    // Créer une nouvelle action de masquage pour le champ spécifié (annotation) et le drapeau d'invisibilité.
    // (Vous pouvez également référencer le champ flottant par le nom si vous l'avez spécifié ci-dessus.)
    // Ajouter des actions à l'entrée/sortie de la souris sur le champ de bouton invisible
    buttonField->get_Actions()->set_OnEnter(MakeObject<Aspose::Pdf::Annotations::HideAction>(floatingField, false));
    buttonField->get_Actions()->set_OnExit(MakeObject<Aspose::Pdf::Annotations::HideAction>(floatingField));

    // Ajouter un champ de bouton au document
    document->get_Form()->Add(System::DynamicCast<Aspose::Pdf::Forms::Field>(buttonField));

    // Enregistrer le document
    document->Save(outputFileName);
}
```