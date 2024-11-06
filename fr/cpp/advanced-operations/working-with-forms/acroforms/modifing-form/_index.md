---
title: Modification d'AcroForm
linktitle: Modification d'AcroForm
type: docs
weight: 40
url: fr/cpp/modifing-form/
description: Modification du formulaire dans votre fichier PDF avec la bibliothèque Aspose.PDF pour C++. Vous pouvez ajouter ou supprimer des champs dans un formulaire existant, obtenir et définir la limite de champ, etc.
lastmod: "2021-12-01"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Obtenir ou Définir la Limite de Champ

La méthode SetFieldLimit(field, limit) de la classe FormEditor vous permet de définir une limite de champ, le nombre maximum de caractères pouvant être saisis dans un champ.

```cpp
void SetFieldLimitDom() {
    String _dataDir("C:\\Samples\\");
    // Ouvrir le document
    auto document = MakeObject<Document>(_dataDir + u"GetValuesFromAllFields.pdf");
    auto textBoxField = System::DynamicCast<TextBoxField>(document->get_Form()->idx_get(u"textbox1"));
    textBoxField->set_MaxLen(15);
    document->Save(_dataDir + u"GetValuesFromAllFields.pdf");
}
```

De même, Aspose.PDF a une méthode qui obtient la limite de champ en utilisant l'approche DOM. Le fragment de code suivant montre les étapes.

```cpp
void GetFieldLimitDom() {
    String _dataDir("C:\\Samples\\");
    // Ouvrir le document
    auto document = MakeObject<Document>(_dataDir + u"GetValuesFromAllFields.pdf");
    auto textBoxField = System::DynamicCast<TextBoxField>(document->get_Form()->idx_get(u"textbox1"));
    Console::WriteLine(u"Limite : {0}", textBoxField->get_MaxLen());        
}
```

Vous pouvez également définir et obtenir la même valeur en utilisant l'espace de noms *Aspose.PDF.Facades* en utilisant le fragment de code suivant.

```cpp
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Forms;

void SetFieldLimitFacade(){
    String _dataDir("C:\\Samples\\");
    // Ajout de champ avec limite
    auto form = MakeObject<Aspose::Pdf::Facades::FormEditor>(_dataDir + u"input.pdf", _dataDir + u"SetFieldLimit_out.pdf");
    form->SetFieldLimit(u"textbox1", 15);
    form->Save();
}
```

```cpp
void GetFieldLimitFacade(){
    String _dataDir("C:\\Samples\\");
    // Ajout de champ avec limite
    auto form = MakeObject<Aspose::Pdf::Facades::Form>(_dataDir + u"input.pdf");
    Console::WriteLine(u"Limite : {0}", form->GetFieldLimit(u"textbox1"));
}
```
## Définir une police personnalisée pour le champ de formulaire

Les champs de formulaire dans les fichiers PDF Adobe peuvent être configurés pour utiliser des polices par défaut spécifiques. Dans les premières versions d'Aspose.PDF, seules les 14 polices par défaut étaient supportées. Les versions ultérieures ont permis aux développeurs d'appliquer n'importe quelle police. Pour définir et mettre à jour la police par défaut utilisée pour les champs de formulaire, utilisez la classe DefaultAppearance (Font font, double size, Color color). Cette classe se trouve sous l'espace de noms Aspose.PDF.InteractiveFeatures. Pour utiliser cet objet, utilisez la propriété DefaultAppearance de la classe Field.

L'extrait de code suivant montre comment définir la police par défaut pour les champs de formulaire PDF.

```cpp
void SetCustomFontForField() {

    String _dataDir("C:\\Samples\\");

    // Ouvrir le document
    auto document = new Document(_dataDir + u"FormFieldFont14.pdf");

    // Obtenir un champ de formulaire particulier du document
    auto textBoxField = System::DynamicCast<TextBoxField>(document->get_Form()->idx_get(u"textbox1"));

    // Créer un objet de police
    auto font = Aspose::Pdf::Text::FontRepository::FindFont(u"ComicSansMS");

    // Définir les informations de police pour le champ de formulaire

    textBoxField->set_DefaultAppearance(MakeObject<Aspose::Pdf::Annotations::DefaultAppearance>(font, 10, System::Drawing::Color::get_Black()));

    // Enregistrer le document mis à jour
    document->Save(_dataDir + u"FormFieldFont14.pdf");
}
```

## Supprimer des champs d'un formulaire existant

Tous les champs de formulaire sont contenus dans la collection Form de l'objet Document. Cette collection fournit différentes méthodes qui gèrent les champs de formulaire, y compris la méthode Delete. Si vous souhaitez supprimer un champ particulier, passez le nom du champ en tant que paramètre à la méthode Delete, puis enregistrez le document PDF mis à jour. L'extrait de code suivant montre comment supprimer un champ particulier d'un document PDF.

```cpp
void DeleteFormField() {    
    String _dataDir("C:\\Samples\\");

    // Open document
    auto document = new Document(_dataDir + u"DeleteFormField.pdf");

    // Delete a particular field by name
    document->get_Form()->Delete(u"textbox1");
    
    // Save modified document
    document->Save(_dataDir + u"DeleteFormField_out.pdf");
}
```