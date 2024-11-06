---
title: Publication de données AcroForm
linktitle: Publication d'AcroForm
type: docs
weight: 50
url: fr/cpp/posting-acroform-data/
description: Vous pouvez importer et exporter des données de formulaire vers un fichier XML avec l'espace de noms Aspose.Pdf.Facades dans Aspose.PDF pour C++.
lastmod: "2021-12-01"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

{{% alert color="primary" %}}

AcroForm est un type important de document PDF. Vous pouvez non seulement créer et éditer un AcroForm en utilisant [Aspose.Pdf.Facades namespace](https://reference.aspose.com/pdf/cpp/namespace/aspose.pdf.facades), mais aussi importer et exporter les données du formulaire vers un fichier XML. Le namespace Aspose.Pdf.Facades dans Aspose.PDF pour C++ vous permet de mettre en œuvre une autre fonctionnalité d'AcroForm, qui vous aide à poster des données AcroForm sur une page web externe. Cette page web lit ensuite les variables postées et utilise ces données pour un traitement ultérieur. Cette fonctionnalité est utile dans les cas où vous ne souhaitez pas simplement conserver les données dans le fichier PDF, mais plutôt les envoyer à votre serveur et ensuite les enregistrer dans une base de données, etc.

{{% /alert %}}

## Détails de l'implémentation

Dans cet article, nous avons essayé de créer un AcroForm en utilisant [Aspose.Pdf.Facades namespace](https://reference.aspose.com/pdf/cpp/namespace/aspose.pdf.facades) et la classe [FormEditor](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.facades.form_editor/). Nous avons également ajouté un bouton de soumission et défini son URL cible.

Les extraits de code suivants vous montrent comment créer le formulaire puis recevoir les données postées sur la page web.
```cpp
using namespace System;
using namespace Aspose::Pdf;

void PostingExample() {

    // Chaîne _dataDir("C:\\Samples\\");
    // Créer une instance de la classe FormEditor et lier les fichiers pdf d'entrée et de sortie
    auto editor = MakeObject<Aspose::Pdf::Facades::FormEditor>("input.pdf", "output.pdf");

    // Créer des champs AcroForm - J'ai créé seulement deux champs pour simplifier
    editor->AddField(Aspose::Pdf::Facades::FieldType::Text, u"firstname", 1, 100, 600, 200, 625);
    editor->AddField(Aspose::Pdf::Facades::FieldType::Text, u"lastname", 1, 100, 550, 200, 575);

    // Ajouter un bouton de soumission et définir l'URL cible
    editor->AddSubmitBtn(u"submitbutton", 1, u"Submit", u"http://localhost/csharptesting/show.aspx", 100, 450, 150, 475);

    // Enregistrer le fichier pdf de sortie
    editor->Save();
}
```