---
title: Travailler avec des formulaires XFA en utilisant C++
linktitle: Formulaires XFA
type: docs
weight: 20
url: fr/cpp/xfa-forms/
description: Aspose.PDF pour l'API C++ vous permet de travailler avec des champs XFA et XFA Acroform dans un document PDF. Le Aspose.PDF.Facades.
lastmod: "2021-12-01"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

Les formulaires XFA sont l'architecture des formulaires XML, une famille de spécifications XML propriétaires qui ont été proposées et développées par JetForm pour améliorer la gestion des formulaires web. Ils peuvent également être utilisés dans des fichiers PDF à partir de la spécification PDF 1.5.

Remplissez les champs XFA avec la classe [Form](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.facades.form/) par [Aspose.Pdf.Facades](https://reference.aspose.com/pdf/cpp/namespace/aspose.pdf.facades).

## Remplir les champs XFA

L'extrait de code suivant vous montre comment remplir les champs dans un formulaire XFA.

```cpp
using namespace System;
using namespace System::Collections::Generic;

using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Text;

void FillXFA() {
    String _dataDir("C:\\Samples\\");

    // Charger le formulaire XFA
    auto document = MakeObject<Document>(_dataDir + u"FillXFAFields.pdf");

    // Obtenir les noms des champs du formulaire XFA
    auto names = document->get_Form()->get_XFA()->get_FieldNames();

    // Définir les valeurs des champs

    document->get_Form()->get_XFA()->idx_set(names->idx_get(0),u"Champ 0");
    document->get_Form()->get_XFA()->idx_set(names->idx_get(1),u"Champ 1");

    // Enregistrer le document mis à jour
    document->Save(_dataDir + u"Filled_XFA_out.pdf");
}
```

## Convertir XFA en AcroForm

{{% alert color="primary" %}}

Essayer en ligne
Vous pouvez vérifier la qualité de la conversion Aspose.PDF et voir les résultats en ligne à ce lien : [products.aspose.app/pdf/xfa/acroform](https://products.aspose.app/pdf/xfa/acroform)

{{% /alert %}}

Les formulaires dynamiques sont basés sur une spécification XML connue sous le nom de XFA, l'« Architecture des formulaires XML ». Les informations sur le formulaire (en ce qui concerne un PDF) sont très vagues - elles spécifient que des champs existent, avec des propriétés et des événements JavaScript, mais ne spécifient aucun rendu.

Actuellement, le PDF prend en charge deux méthodes différentes pour intégrer des données et des formulaires PDF :

- AcroForms (également connus sous le nom de formulaires Acrobat), introduits et inclus dans la spécification de format PDF 1.2.
- Les formulaires Adobe XML Forms Architecture (XFA), introduits dans la spécification de format PDF 1.5 en tant que fonctionnalité optionnelle (La spécification XFA n'est pas incluse dans la spécification PDF, elle est seulement référencée.)

Nous ne pouvons pas extraire ou manipuler des pages de formulaires XFA, car le contenu du formulaire est généré à l'exécution (lors de la visualisation du formulaire XFA) au sein de l'application essayant d'afficher ou de rendre le formulaire XFA. Aspose.PDF a une fonctionnalité qui permet aux développeurs de convertir des formulaires XFA en AcroForms standard.

```cpp
void ConvertXFAtoAcroForms() {

    String _dataDir("C:\\Samples\\");

    // Charger le formulaire XFA
    auto document = MakeObject<Document>(_dataDir + u"DynamicXFAToAcroForm.pdf");

    // Définir le type des champs de formulaire comme AcroForm standard
    document->get_Form()->set_Type(Aspose::Pdf::Forms::FormType::Standard);

    // Enregistrer le PDF résultant
    document->Save(_dataDir + u"Standard_AcroForm_out.pdf");
}
```

## Obtenir les propriétés des champs XFA

Pour accéder aux propriétés des champs, utilisez d'abord Document.Form.XFA.Teamplate pour accéder au modèle de champ. Le code suivant montre les étapes pour obtenir les coordonnées X et Y d'un champ de formulaire XFA.

```cpp
void GetXFAProprties() {

    String _dataDir("C:\\Samples\\");
    // Charger le formulaire XFA
    auto document = MakeObject<Document>(_dataDir + u"GetXFAProperties.pdf");

    auto names = document->get_Form()->get_XFA()->get_FieldNames();

    // Définir les valeurs des champs
    document->get_Form()->get_XFA()->idx_set(names->idx_get(0), u"Champ 0");
    document->get_Form()->get_XFA()->idx_set(names->idx_get(0), u"Champ 1");

    // Obtenir la position du champ
    Console::WriteLine(document->get_Form()->get_XFA()->GetFieldTemplate(names[0])->get_Attributes()->idx_get(u"x")->get_Value());

    // Obtenir la position du champ
    Console::WriteLine(document->get_Form()->get_XFA()->GetFieldTemplate(names[0])->get_Attributes()->idx_get(u"y")->get_Value());

    // Enregistrer le document mis à jour
    document->Save(_dataDir + u"Filled_XFA_out.pdf");
}
```