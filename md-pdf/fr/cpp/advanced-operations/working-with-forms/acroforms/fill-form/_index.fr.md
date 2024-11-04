---
title: Remplir AcroForm
linktitle: Remplir AcroForm
type: docs
weight: 20
url: /cpp/fill-form/
description: Cette section explique comment remplir un champ de formulaire dans un document PDF avec Aspose.PDF pour C++.
lastmod: "2021-12-01"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

Les documents PDF sont les meilleurs, et vraiment le type de fichier préféré, pour créer des formulaires.

Ce sujet explique comment remplir des formulaires PDF en utilisant Aspose.PDF pour C++.

Aspose.PDF pour C++ vous permet de remplir un champ de formulaire, d'obtenir le champ de la collection de formulaires de l'objet Document.

Voyons l'exemple suivant comment résoudre cette tâche :

```cpp
using namespace System;
using namespace Aspose::Pdf;

void FillAcroform()
{
    String _dataDir("C:\\Samples\\");

    // Ouvrir le document
    auto document = MakeObject<Document>(_dataDir + u"FillFormField.pdf");

    // Obtenir un champ
    auto textBoxField = System::DynamicCast<Aspose::Pdf::Forms::TextBoxField>(document->get_Form()->idx_get(u"textbox1"));

    // Modifier la valeur du champ
    textBoxField->set_Value(u"Valeur à remplir dans le champ");

    // Enregistrer le document mis à jour
    document->Save(_dataDir + u"FillFormField_out.pdf");

}
```