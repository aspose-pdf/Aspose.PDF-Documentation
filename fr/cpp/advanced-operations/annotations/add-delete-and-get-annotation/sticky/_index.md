---
title: Annotations Collantes PDF en C++
linktitle: Annotation Collante
type: docs
weight: 50
url: fr/cpp/sticky-annotations/
description: Ce sujet concerne les annotations collantes, comme exemple nous montrons l'annotation de filigrane dans le texte. Elle est utilisée pour représenter des graphiques sur la page. Consultez l'extrait de code pour résoudre cette tâche.
lastmod: "2021-11-24"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Ajouter une Annotation de Filigrane

Une annotation de filigrane doit être utilisée pour représenter des graphiques qui doivent être imprimés à une taille et une position fixes sur une page, indépendamment des dimensions de la page imprimée.

Vous pouvez ajouter du texte de filigrane en utilisant [WatermarkAnnotation](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.watermark_annotation/) à une position spécifique de la page PDF. L'opacité du filigrane peut également être contrôlée en utilisant la propriété d'opacité.

Veuillez consulter l'extrait de code suivant pour ajouter WatermarkAnnotation.

```cpp
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Text;
using namespace Aspose::Pdf::Annotations;

void ExampleWatermarkAnnotation::AddWaterMarkAnnotation()
{
    String _dataDir("C:\\Samples\\");

    // Charger le fichier PDF
    auto document = MakeObject<Document>(_dataDir + u"sample.pdf");
    auto page = document->get_Pages()->idx_get(1);

    //Créer une Annotation
    auto wa = MakeObject<WatermarkAnnotation>(page, MakeObject<Rectangle>(100, 500, 400, 600));

    //Ajouter l'annotation dans la collection d'annotations de la page
    page->get_Annotations()->Add(wa);

    //Créer TextState pour les paramètres de police
    auto ts = MakeObject<TextState>();

    ts->set_ForegroundColor(Color::get_Blue());
    ts->set_Font(Aspose::Pdf::Text::FontRepository::FindFont(u"Times New Roman"));
    ts->set_FontSize(32);

    //Définir le niveau d'opacité du texte de l'annotation
    wa->set_Opacity(0.5);

    //Ajouter du texte à l'annotation
    wa->SetTextAndState(MakeArray<String>({ u"Aspose.PDF", u"Watermark", u"Demo" }), ts);

    //Enregistrer le document
    document->Save(_dataDir + u"sample_watermark.pdf");
}
```

## Obtenir l'Annotation de Filigrane

Veuillez essayer d'utiliser l'extrait de code suivant pour obtenir l'annotation de filigrane à partir d'un document PDF.

```cpp
void ExampleWatermarkAnnotation::GetWatermarkAnnotation() {

    String _dataDir("C:\\Samples\\");

    // Charger le fichier PDF
    auto document = MakeObject<Document>(_dataDir + u"sample_watermark.pdf");
    auto page = document->get_Pages()->idx_get(1);

    // Filtrer les annotations en utilisant AnnotationSelector
    auto annotationSelector = MakeObject<AnnotationSelector>(
        MakeObject<WatermarkAnnotation>(page, Rectangle::get_Trivial()));
    page->Accept(annotationSelector);
    auto watermarkAnnotations = annotationSelector->get_Selected();

    // imprimer les résultats
    for (auto wa : watermarkAnnotations) {
        Console::WriteLine(wa->get_Rect());
    }
}
```

## Supprimer l'Annotation de Filigrane

Veuillez essayer d'utiliser l'extrait de code suivant pour supprimer l'annotation de filigrane d'un document PDF.

```cpp
void ExampleWatermarkAnnotation::DeleteWatermarkAnnotation() {

    String _dataDir("C:\\Samples\\");

    // Charger le fichier PDF
    auto document = MakeObject<Document>(_dataDir + u"sample_watermark.pdf");
    auto page = document->get_Pages()->idx_get(1);

    // Filtrer les annotations en utilisant AnnotationSelector
    auto annotationSelector = MakeObject<AnnotationSelector>(
        MakeObject<WatermarkAnnotation>(page, Rectangle::get_Trivial()));
    page->Accept(annotationSelector);
    auto watermarkAnnotations = annotationSelector->get_Selected();

    // supprimer les annotations
    for (auto wa : watermarkAnnotations) {
        page->get_Annotations()->Delete(wa);
    }
    document->Save(_dataDir + u"sample_watermark_del.pdf");
}
```