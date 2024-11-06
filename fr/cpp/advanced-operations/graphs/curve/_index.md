---
title: Ajouter un objet courbe au fichier PDF
linktitle: Ajouter une courbe
type: docs
weight: 30
url: fr/cpp/add-curve/
description: Cet article explique comment créer un objet courbe dans votre PDF en utilisant Aspose.PDF pour C++.
lastmod: "2021-12-18"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Ajouter un objet courbe

Un graphique [Curve](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.drawing.curve/) est une union connectée de lignes projectives, chaque ligne rencontrant trois autres en des points doubles ordinaires.

Les courbes de Bézier sont largement utilisées en infographie pour modéliser des courbes lisses. La courbe est entièrement contenue dans l'enveloppe convexe de ses points de contrôle, les points peuvent être affichés graphiquement et utilisés pour manipuler la courbe de manière intuitive. La courbe entière est contenue dans le quadrilatère dont les coins sont les quatre points donnés (leur enveloppe convexe).

Dans cet article, nous allons examiner les courbes graphiques simples et les courbes remplies que vous pouvez créer dans votre document PDF.

Suivez les étapes ci-dessous :

1. Create [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document) instance

1. Créer un [objet Drawing](https://reference.aspose.com/pdf/cpp/namespace/aspose.pdf.drawing) avec certaines dimensions

1. Définir une [Bordure](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.drawing.graph#ab63dde9501441515b915fd68f66a01bd) pour l'objet Drawing

1. Ajouter un objet [Graph](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.drawing.graph) à la collection de paragraphes de la page

1. Enregistrer notre fichier PDF

```cpp
void ExampleCurve() {

    // Create Document instance
    String _dataDir("C:\\Samples\\");
    // Créer une instance Document
    auto document = MakeObject<Document>();

    // Ajouter une page à la collection de pages du fichier PDF
    auto page = document->get_Pages()->Add();

    // Créer un objet Drawing avec certaines dimensions
    auto graph = MakeObject<Aspose::Pdf::Drawing::Graph>(400, 200);
    
    // Définir une bordure pour l'objet Drawing
    auto borderInfo = MakeObject<BorderInfo>(BorderSide::All, Color::get_Green());
    graph->set_Border(borderInfo);

    auto curve1 = MakeObject<Aspose::Pdf::Drawing::Curve>(MakeArray<double> ({ 10, 10, 50, 60, 70, 10, 100, 120}));
    curve1->get_GraphInfo()->set_Color(Color::get_GreenYellow());
    graph->get_Shapes()->Add(curve1);

    // Ajouter l'objet Graph à la collection de paragraphes de la page
    page->get_Paragraphs()->Add(graph);

    // Enregistrer le fichier PDF
    document->Save(_dataDir + u"DrawingCurve1_out.pdf");
}
```
La photo suivante montre le résultat exécuté avec notre extrait de code :

![Drawing Curve](drawing_curve.png)

## Créer un Objet Courbe Rempli

Cet exemple montre comment ajouter un objet Courbe rempli de couleur.

```cpp
void ExampleFilledCurve() {

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

    auto curve1 = MakeObject<Aspose::Pdf::Drawing::Curve>(MakeArray<double>({ 10, 10, 50, 60, 70, 10, 100, 120}));
    curve1->get_GraphInfo()->set_FillColor(Color::get_GreenYellow());
    graph->get_Shapes()->Add(curve1);

    // Ajouter l'objet Graph à la collection de paragraphes de la page
    page->get_Paragraphs()->Add(graph);

    // Enregistrer le fichier PDF
    document->Save(_dataDir + u"DrawingCurve2_out.pdf");
}
```

Look at the result of adding a filled Curve:

![Courbe Remplie](filled_curve.png)