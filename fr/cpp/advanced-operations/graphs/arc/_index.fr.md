---
title: Ajouter un objet Arc au fichier PDF
linktitle: Ajouter un Arc
type: docs
weight: 10
url: /cpp/add-arc/
description: Cet article explique comment créer un objet arc dans votre PDF en utilisant Aspose.PDF pour C++.
lastmod: "2021-12-18"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Ajouter un objet Arc

Aspose.PDF pour C++ prend en charge la fonctionnalité d'ajout d'objets graphiques (par exemple graphe, ligne, rectangle, etc.) aux documents PDF. Il offre également la possibilité de remplir l'objet [Arc](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.drawing.arc) avec une certaine couleur.

Suivez les étapes ci-dessous :

1. Créez une instance de [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document)

1. Créez un [objet de dessin](https://reference.aspose.com/pdf/cpp/namespace/aspose.pdf.drawing) avec des dimensions spécifiques

1. Définissez la [Bordure](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.drawing.graph#ab63dde9501441515b915fd68f66a01bd) pour l'objet de dessin

1. Ajouter un objet [Graph](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.drawing.graph) à la collection de paragraphes de la page

1. Enregistrez notre fichier PDF

Le code suivant montre comment ajouter un objet [Arc](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.drawing.arc/).

```cpp
void ExampleArc() {
    // Créer une instance de Document
    String _dataDir("C:\\Samples\\");
    // Créer une instance de Document
    auto document = MakeObject<Document>();

    // Ajouter une page à la collection de pages du fichier PDF
    auto page = document->get_Pages()->Add();

    // Créer un objet Drawing avec certaines dimensions
    auto graph = MakeObject<Aspose::Pdf::Drawing::Graph>(400, 400);
    // Définir la bordure pour l'objet Drawing
    auto borderInfo = MakeObject<BorderInfo>(BorderSide::All, Color::get_Green());
    graph->set_Border(borderInfo);

    auto arc1 = MakeObject<Aspose::Pdf::Drawing::Arc>(100, 100, 95, 0, 90);
    arc1->get_GraphInfo()->set_Color(Color::get_GreenYellow());
    graph->get_Shapes()->Add(arc1);

    auto arc2 = MakeObject<Aspose::Pdf::Drawing::Arc>(100, 100, 90, 70, 180);
    arc2->get_GraphInfo()->set_Color(Color::get_DarkBlue());
    graph->get_Shapes()->Add(arc2);

    auto arc3 = MakeObject<Aspose::Pdf::Drawing::Arc>(100, 100, 85, 120, 210);
    arc3->get_GraphInfo()->set_Color(Color::get_Red());
    graph->get_Shapes()->Add(arc3);

    // Ajouter l'objet Graph à la collection de paragraphes de la page
    page->get_Paragraphs()->Add(graph);

    // Enregistrer le fichier PDF
    document->Save(_dataDir + u"DrawingArc_out.pdf");

}
```
## Créer un Objet Arc Rempli

L'exemple suivant montre comment ajouter un objet Arc qui est rempli de couleur et avec certaines dimensions.

```cpp
void ExampleFilledArc() {

    // Créer une instance de Document
    String _dataDir("C:\\Samples\\");
    // Créer une instance de Document
    auto document = MakeObject<Document>();

    // Ajouter une page à la collection de pages du fichier PDF
    auto page = document->get_Pages()->Add();

    // Créer un objet Drawing avec certaines dimensions
    auto graph = MakeObject<Aspose::Pdf::Drawing::Graph>(400, 400);
    // Définir une bordure pour l'objet Drawing
    auto borderInfo = MakeObject<BorderInfo>(BorderSide::All, Color::get_Green());
    graph->set_Border(borderInfo);

    auto arc = MakeObject<Aspose::Pdf::Drawing::Arc>(100, 100, 95, 0, 90);
    arc->get_GraphInfo()->set_FillColor(Color::get_GreenYellow());
    graph->get_Shapes()->Add(arc);

    auto line = MakeObject<Aspose::Pdf::Drawing::Line>(MakeArray<double>({ 195, 100, 100, 100, 100, 195 }));
    line->get_GraphInfo()->set_FillColor(Color::get_GreenYellow());
    graph->get_Shapes()->Add(line);

    // Ajouter l'objet Graph à la collection de paragraphes de la page
    page->get_Paragraphs()->Add(graph);

    // Enregistrer le fichier PDF
    document->Save(_dataDir + u"DrawingArc_out.pdf");

}
```


Voyons le résultat de l'ajout d'un Arc rempli :

![Filled Arc](filled_arc.png)
```