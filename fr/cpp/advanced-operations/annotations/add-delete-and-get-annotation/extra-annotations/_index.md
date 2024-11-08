```
titre: Annotations supplémentaires en C++
linktitle: Annotations supplémentaires
type: docs
poids: 60
url: /fr/cpp/extra-annotations/
description: Cette section décrit comment ajouter, obtenir et supprimer différents types d'annotations de votre document PDF.
lastmod: "2021-11-24"
sitemap:
    changefreq: "weekly"
    priority: 0.7

## Comment ajouter une annotation de type Caret dans un fichier PDF existant

L'annotation de type Caret est un symbole qui indique l'édition de texte. L'annotation de type Caret est également une annotation de balisage, donc la classe Caret dérive de la classe Markup et fournit également des fonctions pour obtenir ou définir les propriétés de l'annotation de type Caret et réinitialiser le flux de l'apparence de l'annotation de type Caret.

Étapes avec lesquelles nous créons une annotation de type Caret:

1. Charger le fichier PDF - nouveau [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document).
1.
``` Créer une nouvelle [Annotation de Caret](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.caret_annotation/) et définir les paramètres du Caret (nouveau Rectangle, titre, Sujet, Drapeaux, couleur, largeur, Style de Début et Style de Fin). Cette annotation est utilisée pour indiquer l'insertion de texte.
1. Créer une nouvelle [Annotation de Caret](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.caret_annotation/) et définir les paramètres du Caret (nouveau Rectangle, titre, Sujet, Drapeaux, couleur, largeur, Style de Début et Style de Fin). Cette annotation est utilisée pour indiquer le remplacement du texte.
1. Créer une nouvelle [Annotation de Barré](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.strike_out_annotation/) et définir les paramètres (nouveau Rectangle, titre, couleur, nouveaux QuadPoints et nouveaux points, Sujet, EnRéponseÀ, TypeDeRéponse).
1. Ensuite, nous pouvons ajouter des annotations à la page.

Le code suivant montre comment ajouter une Annotation de Caret à un fichier PDF :

```cpp
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Text;
using namespace Aspose::Pdf::Annotations;

void MarkupAnnotations::AddCaretAnnotation() {
    String _dataDir("C:\\Samples\\");

    // Charger le fichier PDF
    auto document = MakeObject<Document>(_dataDir + u"sample.pdf");
    // Cette annotation est utilisée pour indiquer l'insertion de texte
    auto caretAnnotation1 = MakeObject<CaretAnnotation>(
        document->get_Pages()->idx_get(1),
        MakeObject<Rectangle>(299.988, 713.664, 308.708, 720.769));
    caretAnnotation1->set_Title(u"Utilisateur Aspose");
    caretAnnotation1->set_Subject(u"Texte inséré 1");
    caretAnnotation1->set_Flags(AnnotationFlags::Print);
    caretAnnotation1->set_Color(Color::get_Blue());

    // Cette annotation est utilisée pour indiquer le remplacement du texte
    auto caretAnnotation2 = MakeObject<CaretAnnotation>(
        document->get_Pages()->idx_get(1),
        new Rectangle(361.246, 727.908, 370.081, 735.107));

    caretAnnotation2->set_Title(u"Utilisateur Aspose");
    caretAnnotation2->set_Flags(AnnotationFlags::Print);
    caretAnnotation2->set_Subject(u"Texte inséré 2");
    caretAnnotation2->set_Color(Color::get_Blue());

    auto strikeOutAnnotation = MakeObject<StrikeOutAnnotation>(
        document->get_Pages()->idx_get(1),
        MakeObject<Rectangle>(318.407, 727.826, 368.916, 740.098));

    strikeOutAnnotation->set_Color(Color::get_Blue());

    strikeOutAnnotation->set_QuadPoints(
        MakeArray<System::SharedPtr<Point>>({
            MakeObject<Point>(321.66, 739.416),
            MakeObject<Point>(365.664, 739.416),
            MakeObject<Point>(321.66, 728.508),
            MakeObject<Point>(365.664, 728.508) }));

    strikeOutAnnotation->set_Subject(u"Barrer");
    strikeOutAnnotation->set_InReplyTo(caretAnnotation2);
    strikeOutAnnotation->set_ReplyType(ReplyType::Group);

    document->get_Pages()->idx_get(1)->get_Annotations()->Add(caretAnnotation1);
    document->get_Pages()->idx_get(1)->get_Annotations()->Add(caretAnnotation2);
    document->get_Pages()->idx_get(1)->get_Annotations()->Add(strikeOutAnnotation);

    document->Save(_dataDir + u"sample_caret.pdf");
}
```
### Obtenir une Annotation de Caret

Veuillez essayer d'utiliser l'extrait de code suivant pour obtenir une annotation de caret dans un document PDF

```cpp
void MarkupAnnotations::GetCaretAnnotation() {

    String _dataDir("C:\\Samples\\");
    // Charger le fichier PDF
    auto document = MakeObject<Document>(_dataDir + u"sample_caret.pdf");

    // Filtrer les annotations à l'aide de AnnotationSelector
    auto page = document->get_Pages()->idx_get(1);
    auto annotationSelector = MakeObject<AnnotationSelector>(
        MakeObject<CaretAnnotation>(page, Rectangle::get_Trivial()));
    page->Accept(annotationSelector);
    auto caretAnnotations = annotationSelector->get_Selected();

    // afficher les résultats
    for (auto ca : caretAnnotations) {
        Console::WriteLine(ca->get_Rect());
    }
}
```

### Supprimer une Annotation de Caret

L'extrait de code suivant montre comment supprimer une annotation de caret d'un fichier PDF.

```cpp

void MarkupAnnotations::DeleteCaretAnnotation() {

    String _dataDir("C:\\Samples\\");
    // Charger le fichier PDF
    auto document = MakeObject<Document>(_dataDir + u"sample_caret.pdf");

    // Filtrer les annotations à l'aide de AnnotationSelector
    auto page = document->get_Pages()->idx_get(1);
    auto annotationSelector = MakeObject<AnnotationSelector>(
        MakeObject<CaretAnnotation>(page, Rectangle::get_Trivial()));
    page->Accept(annotationSelector);
    auto caretAnnotations = annotationSelector->get_Selected();

    // supprimer l'annotation
    for (auto ca : caretAnnotations) {
        document->get_Pages()->idx_get(1)->get_Annotations()->Delete(ca);
    }
    document->Save(_dataDir + u"sample_caret_del.pdf");
}
```

## Comment ajouter une annotation de lien

Une [annotation de lien](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.link_annotation) est un lien hypertexte qui mène à une destination ailleurs dans le document ou à une action à effectuer.

Un lien est une zone rectangulaire qui peut être placée n'importe où sur la page. Chaque lien a une action PDF correspondante associée. Cette action est exécutée lorsque l'utilisateur clique dans la zone de ce lien.

L'extrait de code suivant montre comment ajouter une annotation de lien à un fichier PDF en utilisant un exemple de numéro de téléphone :

```cpp
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Text;

void AddLinkAnnotation() {
    String _dataDir("C:\\Samples\\");

    // Charger le fichier PDF
    auto document = MakeObject<Document>(_dataDir + u"sample.pdf");

    auto page = document->get_Pages()->idx_get(1);

    // Créer un objet TextFragmentAbsorber pour trouver un numéro de téléphone
    auto textFragmentAbsorber = MakeObject<Aspose::Pdf::Text::TextFragmentAbsorber>("678-555-0103");

    // Accepter l'absorbeur uniquement pour la 1ère page
    page->Accept(textFragmentAbsorber);

    auto phoneNumberFragment = textFragmentAbsorber->get_TextFragments()->idx_get(1);

    // Créer une annotation de lien et définir l'action pour appeler un numéro de téléphone
    auto linkAnnotation = MakeObject<Aspose::Pdf::Annotations::LinkAnnotation>(page, phoneNumberFragment->get_Rectangle());
    linkAnnotation->set_Action(MakeObject<Aspose::Pdf::Annotations::GoToURIAction>("callto:678-555-0103"));

    // Ajouter l'annotation à la page
    page->get_Annotations()->Add(linkAnnotation);
    document->Save(_dataDir + u"SimpleResume_mod.pdf");
}
```

### Obtenir une Annotation de Lien

Veuillez essayer d'utiliser l'extrait de code suivant pour obtenir une LinkAnnotation à partir d'un document PDF.

```cpp
void GetLinkAnnotations() {

    String _dataDir("C:\\Samples\\");
    // Charger le fichier PDF
    auto document = MakeObject<Document>(_dataDir + u"SimpleResume_mod.pdf");

    // Filtrer les annotations en utilisant AnnotationSelector
    auto page = document->get_Pages()->idx_get(1);
    auto annotationSelector = MakeObject<Aspose::Pdf::Annotations::AnnotationSelector>(
        MakeObject<Aspose::Pdf::Annotations::LinkAnnotation>(page, Rectangle::get_Trivial(), Point::get_Trivial(), Point::get_Trivial()));
    page->Accept(annotationSelector);

    auto linkAnnotations = annotationSelector->get_Selected();

    // imprimer les résultats
    for (auto la : linkAnnotations) {

        auto l = System::DynamicCast<Aspose::Pdf::Annotations::LinkAnnotation>(la);

        // Imprimer l'URL de chaque annotation de lien
        Console::WriteLine(u"URI: " + System::DynamicCast<Aspose::Pdf::Annotations::GoToURIAction>(l->get_Action())->get_URI());

        auto absorber = MakeObject<TextAbsorber>();
        absorber->get_TextSearchOptions()->set_LimitToPageBounds(true);
        absorber->get_TextSearchOptions()->set_Rectangle(l->get_Rect());
        page->Accept(absorber);

        String extractedText = absorber->get_Text();

        // Imprimer le texte associé à l'hyperlien
        Console::WriteLine(extractedText);
    }
}
```

### Supprimer l'Annotation de Lien

Le fragment de code suivant montre comment supprimer une annotation de lien d'un fichier PDF. Pour cela, nous devons trouver et supprimer toutes les annotations de lien sur la première page. Après cela, nous enregistrerons le document avec l'annotation supprimée.

```cpp
void DeleteLinkAnnotations()
{
    String _dataDir("C:\\Samples\\");
    // Charger le fichier PDF
    auto document = MakeObject<Document>(_dataDir + u"SimpleResume_mod.pdf");

    // Filtrer les annotations en utilisant AnnotationSelector
    auto page = document->get_Pages()->idx_get(1);

    auto annotationSelector = MakeObject<Aspose::Pdf::Annotations::AnnotationSelector>(
        MakeObject<Aspose::Pdf::Annotations::LinkAnnotation>(page, Rectangle::get_Trivial(), Point::get_Trivial(), Point::get_Trivial()));
    page->Accept(annotationSelector);

    auto lineAnnotations = annotationSelector->get_Selected();

    // imprimer les résultats
    for (auto la : lineAnnotations) {
        page->get_Annotations()->Delete(la);
    }

    // Enregistrer le document avec l'annotation supprimée
    document->Save(_dataDir + u"SimpleResume_del.pdf");
}
```

## Rédiger une certaine région de page avec l'annotation de rédaction en utilisant Aspose.PDF pour C++

Aspose.PDF pour C++ prend en charge la fonctionnalité d'ajouter ainsi que de manipuler des annotations dans un fichier PDF existant. Récemment, certains de nos clients ont demandé à rédiger (supprimer du texte, des images, etc. des éléments de) une certaine région de page d'un document PDF. Afin de répondre à cette exigence, une classe nommée RedactionAnnotation est fournie, qui peut être utilisée pour rédiger certaines régions de page ou elle peut être utilisée pour manipuler les RedactionAnnotations existantes et les rédiger (c'est-à-dire aplatir l'annotation et supprimer le texte sous celle-ci).

```cpp
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Text;
using namespace Aspose::Pdf::Annotations;


void RedactAnnotation::AddRedactionAnnotation() {

    String _dataDir("C:\\Samples\\");

    // Ouvrir le document
    auto document = MakeObject<Document>(_dataDir + u"sample.pdf");
    auto page = document->get_Pages()->idx_get(1);

    // Créer une instance de RedactionAnnotation pour une région spécifique de la page
    auto annot = MakeObject<RedactionAnnotation>(page, MakeObject<Rectangle>(200, 500, 300, 600));
    annot->set_FillColor(Color::get_Green());
    annot->set_BorderColor(Color::get_Yellow());
    annot->set_Color(Color::get_Blue());

    // Texte à imprimer sur l'annotation de rédaction
    annot->set_OverlayText(u"REDACTED");
    annot->set_TextAlignment(HorizontalAlignment::Center);

    // Répéter le texte de superposition sur l'annotation de rédaction
    annot->set_Repeat(true);

    // Ajouter l'annotation à la collection d'annotations de la première page
    page->get_Annotations()->Add(annot);

    // Aplatit l'annotation et rédige le contenu de la page (c'est-à-dire supprime le texte et l'image
    // Sous l'annotation rédigée)
    annot->Redact();
    document->Save(_dataDir + u"RedactPage_out.pdf");
}
```

## Approche des façades

Aspose.PDF.Facades prend en charge la classe [PdfAnnotationEditor](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.facades.pdf_annotation_editor/), qui offre la fonctionnalité de manipuler les annotations existantes à l'intérieur d'un fichier PDF.

Cette classe contient une méthode nommée [RedactArea(..)](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.facades.pdf_annotation_editor#a35ebd333b63b6df2c0c299c7331e3c63) qui permet de supprimer certaines régions de la page.

```cpp
void RedactAnnotation::AddRedactionAnnotationViaFacades() {

    String _dataDir("C:\\Samples\\");

    auto editor = MakeObject<Aspose::Pdf::Facades::PdfAnnotationEditor>();

    editor->BindPdf(_dataDir + u"sample.pdf");

    // Caviarder une certaine région de la page
    editor->RedactArea(1, MakeObject<Rectangle>(100, 100, 20, 70), System::Drawing::Color::get_White());
    editor->BindPdf(_dataDir + u"sample.pdf");
    editor->Save(_dataDir + u"FacadesApproach_out.pdf");
}
```