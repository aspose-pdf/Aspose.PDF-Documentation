---
title: Annotation de texte PDF
Texttitle: Annotation de texte
type: docs
weight: 10
url: fr/cpp/text-annotation/
description: Aspose.PDF pour C++ vous permet d'ajouter, d'obtenir et de supprimer des annotations de texte de votre document PDF.
lastmod: "2021-11-24"
sitemap:
    changefreq: "monthly"
    priority: 0.5
---

## Comment ajouter une annotation de texte dans un fichier PDF existant

Une annotation de texte est une annotation attachée à un emplacement spécifique dans un document PDF. Lorsqu'elle est fermée, l'annotation est affichée sous forme d'icône ; lorsqu'elle est ouverte, elle devrait afficher une fenêtre contextuelle contenant le texte de la note dans la police et la taille choisies par le lecteur.

Les annotations sont contenues dans la collection [Annotations](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.annotation) d'une page particulière. Cette collection contient les annotations uniquement pour cette page individuelle ; chaque page a sa propre collection d'Annotations.

Pour ajouter une annotation à une page particulière, ajoutez-la à la collection d'Annotations de cette page avec la méthode [Add](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.annotation_collection#a1f7bf6c38fe2f97904a3575f5241d6c9).

1. Tout d'abord, créez une annotation que vous souhaitez ajouter au PDF.
1. Ensuite, ouvrez le PDF d'entrée.
1. Ajoutez l'annotation à la collection Annotations de l'objet [Page](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page).

L'extrait de code suivant vous montre comment ajouter une annotation dans une page PDF.

```cpp
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Text;

void AddTextAnnotation()
{
    String _dataDir("C:\\Samples\\");

    // Chargez le fichier PDF
    auto document = MakeObject<Document>(_dataDir + u"sample.pdf");

    auto page = document->get_Pages()->idx_get(1);
    auto rect = MakeObject<Rectangle>(200, 750, 400, 790);
    auto textAnnotation = MakeObject<Aspose::Pdf::Annotations::TextAnnotation>(page, rect);

    textAnnotation->set_Title(u"Utilisateur Aspose");
    textAnnotation->set_Subject(u"Sujet d'exemple");
    textAnnotation->set_State(Aspose::Pdf::Annotations::AnnotationState::Accepted);
    textAnnotation->set_Contents(u"Contenu d'exemple pour l'annotation");
    textAnnotation->set_Open(true);
    textAnnotation->set_Icon(Aspose::Pdf::Annotations::TextIcon::Circle);

    auto border = MakeObject<Aspose::Pdf::Annotations::Border>(textAnnotation);
    border->set_Width(5);
    border->set_Dash(MakeObject<Aspose::Pdf::Annotations::Dash>(1, 1));
    textAnnotation->set_Border(border);
    textAnnotation->set_Rect(rect);

    page->get_Annotations()->Add(textAnnotation);
    document->Save(_dataDir + u"sample_textannot.pdf");
}
```

## Obtenir l'annotation de texte

Veuillez essayer d'utiliser l'extrait de code suivant pour obtenir l'annotation de texte dans un document PDF :

```cpp
void GetTextAnnotation() {

    String _dataDir("C:\\Samples\\");

    // Charger le fichier PDF
    auto document = MakeObject<Document>(_dataDir + u"sample_textannot.pdf");

    // Filtrer les annotations en utilisant AnnotationSelector
    auto page = document->get_Pages()->idx_get(1);

    auto annotationSelector = MakeObject<Aspose::Pdf::Annotations::AnnotationSelector>(
        MakeObject<Aspose::Pdf::Annotations::LineAnnotation>(page, Rectangle::get_Trivial(), Point::get_Trivial(), Point::get_Trivial()));
    page->Accept(annotationSelector);
    auto textAnnotations = annotationSelector->get_Selected();

    // imprimer les résultats
    for (auto fa : textAnnotations) {
        Console::WriteLine(fa->get_Rect());
    }
}
```

## Supprimer l'annotation de texte du fichier PDF

L'extrait de code suivant montre comment supprimer l'annotation de texte d'un fichier PDF.

```cpp
void DeleteTextAnnotation() {

    String _dataDir("C:\\Samples\\");
    // Charger le fichier PDF
    auto document = MakeObject<Document>(_dataDir + u"sample_textannot.pdf");

    // Filtrer les annotations en utilisant AnnotationSelector
    auto page = document->get_Pages()->idx_get(1);
    auto annotationSelector = MakeObject<Aspose::Pdf::Annotations::AnnotationSelector>(
        MakeObject<Aspose::Pdf::Annotations::LineAnnotation>(page, Rectangle::get_Trivial(), Point::get_Trivial(), Point::get_Trivial()));
    page->Accept(annotationSelector);
    auto textAnnotations = annotationSelector->get_Selected();

    // supprimer les annotations
    for (auto fa : textAnnotations) {
        page->get_Annotations()->Delete(fa);
    }
    document->Save(_dataDir + u"sample_textannot_del.pdf");
}
```

## Comment ajouter (ou créer) une nouvelle annotation de texte libre

Une annotation de texte libre affiche du texte directement sur la page. Dans l'extrait suivant, nous ajoutons une annotation de texte libre au-dessus de la première occurrence de la chaîne.

```cpp
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Text;
using namespace Aspose::Pdf::Annotations;

void FreeTextAnnotations::AddFreeTextAnnotationDemo()
{
    String _dataDir("C:\\Samples\\");

    // Charger le fichier PDF
    auto document = MakeObject<Document>(_dataDir + u"sample.pdf");
    auto page = document->get_Pages()->idx_get(1);

    auto defaultAppearance = MakeObject<DefaultAppearance>();
    defaultAppearance->set_FontName(u"Helvetica");
    defaultAppearance->set_FontSize(12);
    defaultAppearance->set_TextColor(System::Drawing::Color::get_Blue());

    auto freeTextAnnotation = MakeObject<FreeTextAnnotation>(page, new Rectangle(300.0, 770.0, 400.0, 790.0), defaultAppearance);

    freeTextAnnotation->set_RichText(u"Démo de texte libre");
    page->get_Annotations()->Add(freeTextAnnotation);
    document->Save(_dataDir + u"sample_freetext.pdf");
}
```

## Obtenir l'Annotation de Texte Libre

Veuillez essayer d'utiliser l'extrait de code suivant pour obtenir l'annotation de texte dans le document PDF :

```cpp
void FreeTextAnnotations::GetFreeTextAnnotation() {

    String _dataDir("C:\\Samples\\");

    // Charger le fichier PDF
    auto document = MakeObject<Document>(_dataDir + u"sample_freetext.pdf");
    auto page = document->get_Pages()->idx_get(1);

    // Filtrer les annotations en utilisant AnnotationSelector
    auto annotationSelector = MakeObject<AnnotationSelector>(
        new FreeTextAnnotation(page, Rectangle::get_Trivial(), new DefaultAppearance()));
    page->Accept(annotationSelector);
    auto freeTextAnnotations = annotationSelector->get_Selected();

    // imprimer les résultats
    for (auto fa : freeTextAnnotations) {
        Console::WriteLine(fa->get_Rect());
    }
}
```

### Rendre l'Annotation de Texte Libre Invisible

Parfois, il est nécessaire de créer un filigrane qui n'est pas visible dans le document lors de sa visualisation, mais qui doit être visible lors de l'impression du document. Utilisez des drapeaux d'annotation pour cet objectif. L'extrait de code suivant montre comment.

```cpp
void FreeTextAnnotations::MakeFreeTextAnnotationInvisble() {

    String _dataDir("C:\\Samples\\");

    // Ouvrir le document
    auto doc = MakeObject<Document>(_dataDir + u"input.pdf");

    auto annotation = new FreeTextAnnotation(doc->get_Pages()->idx_get(1),
        MakeObject<Rectangle>(50, 600, 250, 650),
        MakeObject<DefaultAppearance>(u"Helvetica", 16,
            System::Drawing::Color::get_Red()));
    annotation->set_Contents(u"ABCDEFG");
    annotation->get_Characteristics()->set_Border(System::Drawing::Color::get_Red());
    annotation->set_Flags (AnnotationFlags::Print | AnnotationFlags::NoView);
    doc->get_Pages()->idx_get(1)->get_Annotations()->Add(annotation);

    // Enregistrer le fichier de sortie
    doc->Save(_dataDir + u"InvisibleAnnotation_out.pdf");
}
```

## Supprimer l'annotation FreeText

L'extrait de code suivant montre comment supprimer l'annotation FreeText d'un fichier PDF.

```cpp
void FreeTextAnnotations::DeleteFreeTextAnnotation() {

    String _dataDir("C:\\Samples\\");

    // Charger le fichier PDF
    auto document = MakeObject<Document>(_dataDir + u"sample_freetext.pdf");

    // Filtrer les annotations en utilisant AnnotationSelector
    auto page = document->get_Pages()->idx_get(1);

    auto annotationSelector = MakeObject<AnnotationSelector>(
        new FreeTextAnnotation(page, Rectangle::get_Trivial(), new DefaultAppearance()));
    page->Accept(annotationSelector);
    auto freeTextAnnotations = annotationSelector->get_Selected();

    // supprimer les annotations
    for (auto fa : freeTextAnnotations) {
        page->get_Annotations()->Delete(fa);
    }
    document->Save(_dataDir + u"sample_freetext_del.pdf");
}
```