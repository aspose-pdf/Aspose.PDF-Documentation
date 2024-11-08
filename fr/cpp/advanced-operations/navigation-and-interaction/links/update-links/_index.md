---
title: Mettre à jour les liens dans le PDF
linktitle: Mettre à jour les liens
type: docs
weight: 20
url: /fr/cpp/update-links/
description: Mettez à jour les liens dans le PDF par programmation avec Aspose.PDF pour C++. Ce guide explique comment mettre à jour les liens dans un fichier PDF.
lastmod: "2022-01-31"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Mettre à jour les liens dans un fichier PDF

Comme discuté dans Ajouter un lien hypertexte dans un fichier PDF, la classe [LinkAnnotation](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.link_annotation/) permet d'ajouter des liens dans un fichier PDF. Il existe également une classe similaire utilisée pour obtenir des liens existants à l'intérieur des fichiers PDF. Utilisez ceci si vous avez besoin de mettre à jour un lien existant. Pour mettre à jour un lien existant :

1. Chargez un fichier PDF.
1. Allez à une page spécifique dans le fichier PDF.
1. Spécifiez la destination du lien à l'aide de la propriété Destination de l'objet [GoToAction](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.go_to_action).
1. La page de destination est spécifiée en utilisant le constructeur [XYZExplicitDestination](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.x_y_z_explicit_destination).

### Définir la cible du lien vers une page dans le même document

Le code suivant vous montre comment mettre à jour un lien dans un fichier PDF et définir sa cible sur la deuxième page du document.

```cpp
void SetLinkTargetToAPageInTheSameDocument()
{
    String _dataDir("C:\\Samples\\");
    // Créer une instance de Document
    auto document = MakeObject<Document>(_dataDir + u"UpdateLinks.pdf");

    // Ajouter une page à la collection de pages du fichier PDF
    auto page = document->get_Pages()->idx_get(1);
    auto link = System::DynamicCast<Aspose::Pdf::Annotations::LinkAnnotation>(page->get_Annotations()->idx_get(1));

    // Modification du lien : changer la destination du lien
    auto goToAction = System::DynamicCast<Aspose::Pdf::Annotations::GoToAction>(link->get_Action());

    // Spécifier la destination pour l'objet lien
    // Représente une destination explicite qui affiche la page avec les coordonnées (gauche, haut) positionnées dans le coin supérieur gauche de
    // la fenêtre et le contenu de la page agrandi par le facteur de zoom.
    // Le 1er paramètre est le numéro de la page de destination.
    // Le 2e est la coordonnée gauche
    // Le 3e est la coordonnée haut
    // Le 4e argument est le facteur de zoom lors de l'affichage de la page respective. Utiliser 2 signifie que la page sera affichée avec un zoom de 200%
    goToAction->set_Destination(MakeObject<Aspose::Pdf::Annotations::XYZExplicitDestination>(1, 1, 2, 2));

    // Enregistrer le document avec le lien mis à jour
    document->Save(_dataDir + u"UpdateLinks_out.pdf");
}
```
### Définir la Destination du Lien vers une Adresse Web

Pour mettre à jour l'hyperlien afin qu'il pointe vers une adresse web, instanciez l'objet [GoToURIAction](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.go_to_u_r_i_action) et passez-le à la propriété Action de LinkAnnotation. Le fragment de code suivant montre comment mettre à jour un lien dans un fichier PDF et définir sa cible vers une adresse web.

```cpp
void SetLinkDestinationToWebAddress() 
{
    // Charger le fichier PDF
    String _dataDir("C:\\Samples\\");
    // Créer une instance de Document
    auto document = MakeObject<Document>(_dataDir + u"UpdateLinks.pdf");

    // Ajouter une page à la collection de pages du fichier PDF
    auto page = document->get_Pages()->idx_get(1);
    auto link = System::DynamicCast<Aspose::Pdf::Annotations::LinkAnnotation>(page->get_Annotations()->idx_get(1));

    // Modification du lien : changer l'action du lien et définir la cible comme adresse web
    link->set_Action(MakeObject<Aspose::Pdf::Annotations::GoToURIAction>("www.aspose.com"));

    // Enregistrer le document avec le lien mis à jour
    document->Save(_dataDir + u"UpdateLinks_out.pdf");
}
```

### Définir la Cible du Lien vers un Autre Fichier PDF

Le code suivant montre comment mettre à jour un lien dans un fichier PDF et définir sa cible vers un autre fichier PDF.

```cpp
void SetLinkTargetToAnotherPDFFile()
{
    // Charger le fichier PDF
    String _dataDir("C:\\Samples\\");
    // Créer une instance de Document
    auto document = MakeObject<Document>(_dataDir + u"UpdateLinks.pdf");

    // Ajouter une page à la collection de pages du fichier PDF
    auto page = document->get_Pages()->idx_get(1);
    auto linkAnnot = System::DynamicCast<Aspose::Pdf::Annotations::LinkAnnotation>(page->get_Annotations()->idx_get(1));

    // Lien de modification : changer l'action du lien et définir la cible comme adresse web
    auto goToR = System::DynamicCast<Aspose::Pdf::Annotations::GoToRemoteAction>(linkAnnot->get_Action());
    // La ligne suivante met à jour la destination, ne met pas à jour le fichier
    goToR->set_Destination(MakeObject<Aspose::Pdf::Annotations::XYZExplicitDestination>(2, 0, 0, 1.5));
    // La ligne suivante met à jour le fichier
    goToR->set_File(MakeObject<FileSpecification>(_dataDir + u"input.pdf"));

    // Enregistrer le document avec le lien mis à jour
    document->Save(_dataDir + u"UpdateLinks_out.pdf");
}
```

### Mettre à jour la couleur du texte de l'annotation de lien

L'annotation de lien ne contient pas de texte. Au lieu de cela, le texte est placé dans le contenu de la page sous l'annotation. Par conséquent, pour changer la couleur du texte, remplacez la couleur du texte de la page au lieu d'essayer de changer la couleur de l'annotation. Le fragment de code suivant montre comment mettre à jour la couleur de l'annotation de lien dans un fichier PDF.

```cpp
void UpdateLinkAnnotationTextColor() 
{
    // Charger le fichier PDF
    String _dataDir("C:\\Samples\\");

    // Créer une instance de Document
    auto document = MakeObject<Document>(_dataDir + u"UpdateLinks.pdf");

    // Ajouter une page à la collection de pages du fichier PDF
    auto page = document->get_Pages()->idx_get(1);

    for (auto annotation : page->get_Annotations())
    {
        if (annotation->get_AnnotationType() == Aspose::Pdf::Annotations::AnnotationType::Link)
        {
            // Rechercher le texte sous l'annotation
            auto ta = MakeObject<Aspose::Pdf::Text::TextFragmentAbsorber>();
            auto rect = annotation->get_Rect();
            rect->set_LLX(rect->get_LLX() - 10);
            rect->set_LLY(rect->get_LLY() - 10);
            rect->set_URX(rect->get_URX() + 10);
            rect->set_URY(rect->get_URY() + 10);

            ta->set_TextSearchOptions(MakeObject<Aspose::Pdf::Text::TextSearchOptions>(rect));
            ta->Visit(page);
            // Changer la couleur du texte.
            for (auto tf : ta->get_TextFragments())
            {
                tf->get_TextState()->set_ForegroundColor(Color::get_Red());
            }
        }

    }
    // Enregistrer le document avec le lien mis à jour
    document->Save(_dataDir + u"UpdateLinkTextColor_out.pdf");
}
```