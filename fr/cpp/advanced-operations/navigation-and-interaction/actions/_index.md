---
title: Travailler avec des Actions dans un PDF
linktitle: Actions
type: docs
weight: 20
url: /fr/cpp/actions/
description: Cette section explique comment ajouter des actions au document et aux champs de formulaire par programmation avec C++.
lastmod: "2022-01-25"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Ajouter un Hyperlien dans un Fichier PDF

Les documents PDF sont un excellent moyen de partager des informations. Ils sont faciles à lire, éditer et distribuer. Cependant, créer des liens dans un document PDF peut être difficile. Laissez-nous vous montrer comment.

Il est possible d'ajouter des hyperliens aux fichiers PDF, soit pour permettre aux lecteurs de naviguer vers une autre partie du PDF, soit vers un contenu externe.

Par exemple, vous pouvez vouloir ajouter une table des matières cliquable à vos ebooks, citer des ressources externes pour votre article, ou naviguer rapidement le lecteur vers une page différente sur le site web pour obtenir plus d'informations sur un sujet.

Pour créer des hyperliens en quelques clics, suivez ces étapes simples :

1. Créer un objet de classe [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document).  
1. Obtenez la classe [Page](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page) à laquelle vous souhaitez ajouter le lien.  
1. Créez un objet [LinkAnnotation](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.link_annotation/) en utilisant les objets Page et [Rectangle](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.rectangle/). L'objet rectangle est utilisé pour spécifier l'emplacement sur la page où le lien doit être ajouté.  
1. Définissez la propriété Action sur l'objet [GoToURIAction](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.go_to_u_r_i_action) qui spécifie l'emplacement de l'URI distant.  
1. Pour afficher un texte d'hyperlien, ajoutez une chaîne de texte à un emplacement similaire à celui où l'objet [LinkAnnotation](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.link_annotation) est placé.  
1. Pour ajouter un texte libre :

- Instanciez un objet [FreeTextAnnotation](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.free_text_annotation). Il accepte également les objets Page et Rectangle comme argument, il est donc possible de fournir les mêmes valeurs que celles spécifiées dans le constructeur LinkAnnotation.
- En utilisant la propriété Contents de l'objet [FreeTextAnnotation](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.free_text_annotation), spécifiez la chaîne qui doit être affichée dans le PDF de sortie.
- Facultativement, définissez la largeur de bordure des objets [LinkAnnotation](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.link_annotation/) et FreeTextAnnotation à 0 afin qu'ils n'apparaissent pas dans le document PDF.
- Une fois que les objets [LinkAnnotation](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.link_annotation/) et [FreeTextAnnotation](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.free_text_annotation) ont été définis, ajoutez ces liens à la collection Annotations de l'objet [Page](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page).

- Enfin, enregistrez le PDF mis à jour en utilisant la méthode Save de l'objet [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document).
Le fragment de code suivant vous montre comment ajouter un hyperlien à un fichier PDF.

```cpp
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Text;

void AddHyperlinkInPDFFile() {

String _dataDir("C:\\Samples\\");

// Ouvrir le document

auto document = MakeObject<Document>(_dataDir + u"AddHyperlink.pdf");

// Créer un lien

auto page = document->get_Pages()->idx_get(1);

// Créer un objet d'annotation de lien

auto link = MakeObject<Aspose::Pdf::Annotations::LinkAnnotation>(page, MakeObject<Rectangle>(100, 100, 300, 300));

// Créer un objet de bordure pour LinkAnnotation

auto border = MakeObject<Aspose::Pdf::Annotations::Border>(link);

// Définir la valeur de la largeur de la bordure à 0

border->set_Width(0);

// Définir la bordure pour LinkAnnotation

link->set_Border(border);

// Spécifier le type de lien comme URI distant

link->set_Action(MakeObject<Aspose::Pdf::Annotations::GoToURIAction>("www.aspose.com"));

// Ajouter l'annotation de lien à la collection d'annotations de la première page du fichier PDF

page->get_Annotations()->Add(link);


// Créer une annotation de texte libre

auto textAnnotation = MakeObject<Aspose::Pdf::Annotations::FreeTextAnnotation>(


page,


MakeObject<Rectangle>(100, 100, 300, 300),


MakeObject<Aspose::Pdf::Annotations::DefaultAppearance>(



FontRepository::FindFont(u"TimesNewRoman"), 10, Color::get_Blue()));


// Chaîne à ajouter comme texte libre

textAnnotation->set_Contents(u"Lien vers le site Aspose");

// Définir la bordure pour l'annotation de texte libre

textAnnotation->set_Border(border);

// Ajouter l'annotation FreeText à la collection d'annotations de la première page du document

page->get_Annotations()->Add(textAnnotation);


// Enregistrer le document mis à jour

document->Save(_dataDir + u"AddHyperlink_out.pdf");

}
```

## Créer un lien hypertexte vers des pages dans le même PDF

Aspose.PDF pour C++ offre une excellente fonctionnalité pour la création de PDF ainsi que sa manipulation. Il propose également la possibilité d'ajouter des liens vers des pages PDF et un lien peut soit diriger vers des pages dans un autre fichier PDF, une URL web, un lien pour lancer une application ou même un lien vers des pages dans le même fichier PDF. Afin d'ajouter des hyperliens locaux (liens vers des pages dans le même fichier PDF), une classe nommée [LocalHyperlink](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.local_hyperlink) est ajoutée à l'espace de noms Aspose.PDF et cette classe a une propriété nommée TargetPageNumber, qui est utilisée pour spécifier la page cible/destination pour l'hyperlien.

Afin d'ajouter l'hyperlien local, nous devons créer un TextFragment afin que le lien puisse être associé au TextFragment. La classe [TextFragment](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.te_x_fragment) a une propriété nommée Hyperlink qui est utilisée pour associer une instance de LocalHyperlink. Le code suivant montre les étapes pour accomplir cette exigence.

```cpp
void CreateHyperlinkToPagesInSamePDF() {

String _dataDir("C:\\Samples\\");


// Créer une instance de Document

auto document = MakeObject<Document>();


// Ajouter une page à la collection de pages du fichier PDF

auto page = document->get_Pages()->Add();


// Créer une instance de Text Fragment

auto text = MakeObject<TextFragment>(u"tester le numéro de la page du lien vers la page 2");


// Créer une instance de lien hypertexte local

auto link = MakeObject<LocalHyperlink>();


// Définir la page cible pour l'instance de lien

link->set_TargetPageNumber(2);


// Définir le lien hypertexte de TextFragment

text->set_Hyperlink(link);


// Ajouter du texte à la collection de paragraphes de la Page

page->get_Paragraphs()->Add(text);


// Créer une nouvelle instance de TextFragment

text = new TextFragment(u"tester le numéro de la page du lien vers la page 1");


// TextFragment doit être ajouté sur une nouvelle page

text->set_IsInNewPage(true);


// Créer une autre instance de lien hypertexte local

link = new LocalHyperlink();


// Définir la page cible pour le second lien hypertexte

link->set_TargetPageNumber(1);


// Définir le lien pour le second TextFragment

text->set_Hyperlink(link);


// Ajouter du texte à la collection de paragraphes de l'objet page

page->get_Paragraphs()->Add(text);


// Enregistrer le document mis à jour

document->Save(_dataDir + u"CreateLocalHyperlink_out.pdf");
}
```
## Obtenir la destination du lien hypertexte PDF (URL)

Les liens sont représentés comme des annotations dans un fichier PDF et ils peuvent être ajoutés, mis à jour ou supprimés. Aspose.PDF pour C++ prend également en charge l'obtention de la destination (URL) du lien hypertexte dans le fichier PDF.

Pour obtenir l'URL d'un lien :

1. Créez un objet [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document).
1. Obtenez la [Page](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page) dont vous souhaitez extraire les liens.
1. Utilisez la classe [AnnotationSelector](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.annotation_selector/) pour extraire tous les objets [LinkAnnotation](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.link_annotation) de la page spécifiée.
1. Passez l'objet [AnnotationSelector](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.annotation_selector/) à la méthode Accept de l'objet [Page](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page). Obtenez toutes les annotations de lien sélectionnées dans un objet IList à l'aide de la propriété Selected de l'objet [AnnotationSelector](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.annotation_selector/).
1. Enfin, extrayez l'action LinkAnnotation en tant que GoToURIAction.

Le code suivant montre comment obtenir les destinations des hyperliens (URL) à partir d'un fichier PDF.

```cpp
void GetPDFHyperlinkDestination() {

String _dataDir("C:\\Samples\\");


auto document = new Document(_dataDir + u"Aspose-app-list.pdf");

// Extraire les actions

auto page = document->get_Pages()->idx_get(1);


auto selector = MakeObject<Aspose::Pdf::Annotations::AnnotationSelector>(


MakeObject<Aspose::Pdf::Annotations::LinkAnnotation>(page, Rectangle::get_Trivial()));

page->Accept(selector);


auto list = selector->get_Selected();

// Itérer à travers chaque élément individuel dans la liste

if (list->get_Count() == 0)


Console::WriteLine(u"Aucun hyperlien trouvé...");

else {


// Parcourir tous les signets


for (auto annot : list) {



auto la = System::DynamicCast<Aspose::Pdf::Annotations::LinkAnnotation>(annot);



if (la != nullptr) {




auto action = System::DynamicCast<Aspose::Pdf::Annotations::GoToURIAction>(la->get_Action());




// Imprimer l'URL de destination




Console::WriteLine(u"Destination: " + action->get_URI());



}


}

} // fin sinon
}
```
## Obtenir le texte du lien hypertexte

Un lien hypertexte a deux parties : le texte qui apparaît dans le document, et l'URL de destination. Dans certains cas, c'est le texte plutôt que l'URL dont nous avons besoin.

Le texte et les annotations/actions dans un fichier PDF sont représentés par différentes entités. Le texte sur une page n'est qu'un ensemble de mots et de caractères, tandis que les annotations apportent une certaine interactivité, comme celle inhérente à un lien hypertexte.

Pour trouver le contenu de l'URL, vous devez travailler à la fois avec l'annotation et le texte. L'objet [Annotation](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.annotation) n'a pas lui-même le texte mais se situe sous le texte sur la page. Donc, pour obtenir le texte, l'Annotation donne les limites de l'URL, tandis que l'objet Texte donne le contenu de l'URL. Veuillez voir l'extrait de code suivant.

```cpp
  void GetHyperlinkText() {

String _dataDir("C:\\Samples\\");

auto document = MakeObject<Document>(_dataDir + u"aspose-app-list.pdf");

// Extraire les actions

auto page = document->get_Pages()->idx_get(1);


for (auto annot : page->get_Annotations()) {


auto la = System::DynamicCast<Aspose::Pdf::Annotations::LinkAnnotation>(annot);


if (la != nullptr) {



// Imprimer l'URL de chaque annotation de lien



auto action = System::DynamicCast<Aspose::Pdf::Annotations::GoToURIAction>(la->get_Action());



Console::WriteLine(u"URI: " + action->get_URI());




auto absorber = MakeObject<TextAbsorber>();



absorber->get_TextSearchOptions()->set_LimitToPageBounds(true);



absorber->get_TextSearchOptions()->set_Rectangle(annot->get_Rect());



page->Accept(absorber);



String extractedText = absorber->get_Text();



// Imprimer le texte associé au lien hypertexte



Console::WriteLine(extractedText);


}

}
}
```

## Supprimer l'Action d'Ouverture du Document d'un Fichier PDF

[Comment Spécifier la Page PDF lors de l'Affichage du Document](#how-to-specify-pdf-page-when-viewing-document) explique comment indiquer à un document de s'ouvrir sur une page différente de la première. Lors de la concaténation de plusieurs documents, et si un ou plusieurs ont une action GoTo définie, vous voudrez probablement les supprimer. Par exemple, si vous combinez deux documents et que le second a une action GoTo qui vous amène à la deuxième page, le document de sortie s'ouvrira sur la deuxième page du deuxième document au lieu de la première page du document combiné. Pour éviter ce comportement, supprimez la commande d'action d'ouverture.

Pour supprimer une action d'ouverture :

1. Définissez la propriété [OpenAction](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document#a24b876bb6bee957feac48ac8031dc28e) de l'objet [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document) sur null.
1. Enregistrez le PDF mis à jour en utilisant la méthode Save de l'objet Document.

Le fragment de code suivant montre comment supprimer une action d'ouverture de document du fichier PDF.

```cpp
void RemoveDocumentOpenActionFromPDFFile()
{

String _dataDir("C:\\Samples\\");

// Ouvrir le document

auto document = new Document(_dataDir + u"RemoveOpenAction.pdf");

// Supprimer l'action d'ouverture du document

document->set_OpenAction(nullptr);


// Enregistrer le document mis à jour

document->Save(_dataDir + u"RemoveOpenAction_out.pdf");
}
```

## Comment spécifier la page PDF lors de l'affichage d'un document {#how-to-specify-pdf-page-when-viewing-document}

Lors de l'affichage de fichiers PDF dans un lecteur PDF tel qu'Adobe Reader, les fichiers s'ouvrent généralement à la première page. Cependant, il est possible de configurer le fichier pour qu'il s'ouvre sur une autre page.

La classe 'XYZExplicitDestination' vous permet de spécifier une page dans un fichier PDF que vous souhaitez ouvrir. Lors du passage de la valeur de l'objet GoToAction à la propriété OpenAction de la classe [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document), le document s'ouvre à la page spécifiée contre l'objet XYZExplicitDestination. Le code suivant montre comment spécifier une page comme action d'ouverture du document.

```cpp
void HowToSpecifyPDFPageWhenViewingDocument()
{

String _dataDir("C:\\Samples\\");

// Charger le fichier PDF

auto document = new Document(_dataDir + u"SpecifyPageWhenViewing.pdf");

// Obtenir l'instance de la deuxième page du document

auto page2 = document->get_Pages()->idx_get(2);

// Créer la variable pour définir le facteur de zoom de la page cible

double zoom = 1;

// Créer une instance de GoToAction

auto action = MakeObject<Aspose::Pdf::Annotations::GoToAction>(page2);

// Aller à la page 2

action->set_Destination(MakeObject<Aspose::Pdf::Annotations::XYZExplicitDestination>(page2, 0, page2->get_Rect()->get_Height(), zoom));

// Définir l'action d'ouverture du document

document->set_OpenAction(action);

// Enregistrer le document mis à jour

document->Save(_dataDir + u"goto2page_out.pdf");
}
```