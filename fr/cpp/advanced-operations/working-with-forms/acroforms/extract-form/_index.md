---
title: Extraire les données AcroForm en utilisant C++
linktitle: Extraire les données AcroForm
type: docs
weight: 30
url: fr/cpp/extract-form/
description: Cette section explique comment extraire des formulaires de votre document PDF avec Aspose.PDF pour C++.
lastmod: "2021-12-01"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Obtenir les valeurs de tous les champs du document PDF

Pour obtenir les valeurs de tous les champs d'un document PDF, vous devez naviguer à travers tous les champs de formulaire et ensuite obtenir la valeur en utilisant la propriété Value. Obtenez chaque champ de la collection Form, dans le type de champ de base appelé Field et accédez à sa propriété Value.

Les extraits de code suivants montrent comment obtenir les valeurs de tous les champs d'un document PDF.

```cpp
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Forms;

void ExtractDataFromForm()
{
    String _dataDir("C:\\Samples\\");
    // Ouvrir le document
    auto document = MakeObject<Document>(_dataDir + u"GetValuesFromAllFields.pdf");

    // Obtenir les valeurs de tous les champs
    for(auto wa : document->get_Form())
    {
        auto formField = System::DynamicCast<Aspose::Pdf::Forms::Field>(wa);

        Console::WriteLine(u"Nom du champ : {0} ", formField->get_PartialName());
        Console::WriteLine(u"Valeur : {0} ", formField->get_Value());
    }
}
```

## Obtenir la valeur d'un champ individuel d'un document PDF

La propriété Value du champ de formulaire vous permet d'obtenir la valeur d'un champ particulier. Pour obtenir la valeur, récupérez le champ de formulaire à partir de la collection Form de l'objet Document. Cet exemple sélectionne un [TextBoxField](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.forms.text_box_field) et récupère sa valeur en utilisant la propriété Value.

L'extrait de code suivant montre comment obtenir les valeurs des champs individuels dans un document PDF.

```cpp
void GetValueFromIndividualField(){

    String _dataDir("C:\\Samples\\");

    // Ouvrir le document
    auto document = MakeObject<Document>(_dataDir + u"GetValueFromField.pdf");

    // Obtenir un champ
    auto textBoxField = System::DynamicCast<TextBoxField>(document->get_Form()->idx_get(u"textbox1"));

    // Obtenir la valeur du champ
    Console::WriteLine(u"PartialName : {0} ", textBoxField->get_PartialName());
    Console::WriteLine(u"Value : {0} ", textBoxField->get_Value());
}
```

Pour obtenir l'URL du bouton de soumission, utilisez les lignes de code suivantes.

```cpp
void GetSubmitButtonURL()
{
    String _dataDir("C:\\Samples\\");

    // Open document
    auto document = MakeObject<Document>(_dataDir + u"GetValueFromField.pdf");
    auto act = System::DynamicCast<Aspose::Pdf::Annotations::SubmitFormAction>(document->get_Form()->idx_get(1)->get_OnActivated());

    if (act != nullptr)
        Console::WriteLine(act->get_Url()->get_Name());
}
```

## Obtenir des Champs de Formulaire à partir d'une Région Spécifique d'un Fichier PDF

Parfois, vous pouvez savoir où se trouve un champ de formulaire dans un document sans connaître son nom. Par exemple, si vous n'avez qu'un schéma d'un formulaire imprimé. Avec Aspose.PDF pour C++, ce n'est pas un problème. Vous pouvez découvrir quels champs se trouvent dans une région donnée d'un fichier PDF. Pour obtenir des champs de formulaire à partir d'une région spécifique d'un fichier PDF :

1. Ouvrez le fichier PDF en utilisant l'objet Document.
1. Créez un objet rectangle pour obtenir des champs dans cette zone
1. Obtenez le formulaire à partir de la collection de formulaires du document.
1. Affichez les noms et les valeurs des champs

Le code suivant montre comment obtenir des champs de formulaire dans une région rectangulaire spécifique d'un fichier PDF.
```

```cpp
void GetFormFieldsFromSpecificRegion()
{
    String _dataDir("C:\\Samples\\");

    // Ouvrir le fichier pdf
    auto document = MakeObject<Aspose::Pdf::Document>(_dataDir + u"GetFieldsFromRegion.pdf");

    // Créer un objet rectangle pour obtenir les champs dans cette zone
    auto rectangle = MakeObject<Aspose::Pdf::Rectangle>(35, 30, 500, 500);

    // Obtenir les champs dans la zone rectangulaire
    auto fields = document->get_Form()->GetFieldsInRect(rectangle);

    // Afficher les noms et valeurs des champs
    for(auto field : fields)
    {
        // Afficher les propriétés de placement de l'image pour tous les placements
        Console::WriteLine(u"Nom du champ : {0} - Valeur du champ : {1}", field->get_FullName(), field->get_Value());
    }
}
```