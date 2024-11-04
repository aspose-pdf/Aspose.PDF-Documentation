---
title: Ajouter un Objet Cercle au Fichier PDF
linktitle: Ajouter un Cercle
type: docs
weight: 20
url: /cpp/add-circle/
description: Cet article explique comment créer un objet cercle dans votre PDF en utilisant Aspose.PDF pour C++.
lastmod: "2021-12-18"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Ajouter un objet Cercle

Comme les graphiques en barres, les graphiques en cercles peuvent être utilisés pour afficher des données dans plusieurs catégories distinctes. Contrairement aux graphiques en barres, cependant, les graphiques en cercles peuvent être utilisés uniquement lorsque vous avez des données pour toutes les catégories qui constituent l'ensemble. Voyons donc comment ajouter un objet [Cercle](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.drawing.circle/) avec Aspose.PDF pour C++.

Suivez les étapes ci-dessous :

1. Créer une instance de [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document)

1. Créer un [objet Dessin](https://reference.aspose.com/pdf/cpp/namespace/aspose.pdf.drawing) avec certaines dimensions

1. Définir [Border](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.drawing.graph#ab63dde9501441515b915fd68f66a01bd) pour l'objet Drawing

1. Ajouter l'objet [Graph](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.drawing.graph) à la collection de paragraphes de la page

1. Enregistrer notre fichier PDF

```cpp
void ExampleCircle() {

    // Créer une instance de Document
    String _dataDir("C:\\Samples\\");
    // Créer une instance de Document
    auto document = MakeObject<Document>();

    // Ajouter une page à la collection de pages du fichier PDF
    auto page = document->get_Pages()->Add();

    // Créer un objet Drawing avec certaines dimensions
    auto graph = MakeObject<Aspose::Pdf::Drawing::Graph>(400, 200);
    // Définir la bordure pour l'objet Drawing
    auto borderInfo = MakeObject<BorderInfo>(BorderSide::All, Color::get_Green());
    graph->set_Border(borderInfo);

    auto circle = MakeObject<Aspose::Pdf::Drawing::Circle>(100, 100, 40);

    circle->get_GraphInfo()->set_Color(Color::get_GreenYellow());
    graph->get_Shapes()->Add(circle);

    // Ajouter l'objet Graph à la collection de paragraphes de la page
    page->get_Paragraphs()->Add(graph);

    // Enregistrer le fichier PDF
    document->Save(_dataDir + u"DrawingCircle1_out.pdf");
}
```
Notre cercle dessiné ressemblera à ceci :

![Cercle Dessiné](drawing_circle.png)

## Créer un Objet Cercle Rempli

Cet exemple montre comment ajouter un objet Cercle qui est rempli de couleur.

```cpp
void ExampleFilledCircle() {
    // Créer une instance de Document
    String _dataDir("C:\\Samples\\");
    // Créer une instance de Document
    auto document = MakeObject<Document>();

    // Ajouter une page à la collection de pages du fichier PDF
    auto page = document->get_Pages()->Add();

    // Créer un objet Drawing avec certaines dimensions
    auto graph = MakeObject<Aspose::Pdf::Drawing::Graph>(400, 200);
    
    // Définir une bordure pour l'objet Drawing
    auto borderInfo = MakeObject<BorderInfo>(BorderSide::All, Color::get_Green());
    graph->set_Border(borderInfo);

    auto circle = MakeObject<Aspose::Pdf::Drawing::Circle>(100, 100, 40);
    circle->get_GraphInfo()->set_Color(Color::get_GreenYellow());
    circle->get_GraphInfo()->set_FillColor(Color::get_Green());

    circle->set_Text(MakeObject<Aspose::Pdf::Text::TextFragment>(u"Cercle"));

    graph->get_Shapes()->Add(circle);

    // Ajouter l'objet Graph à la collection de paragraphes de la page
    page->get_Paragraphs()->Add(graph);

    // Enregistrer le fichier PDF
    document->Save(_dataDir + u"DrawingCircle2_out.pdf");
}
```

Let's see the result of adding a filled Circle:

![Cercle Rempli](filled_circle.png)