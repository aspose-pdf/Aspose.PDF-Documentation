---
title: Ajouter un objet Ligne au fichier PDF
linktitle: Ajouter Ligne
type: docs
weight: 40
url: fr/cpp/add-line/
description: Cet article explique comment créer un objet ligne dans votre PDF en utilisant Aspose.PDF pour C++.
lastmod: "2021-12-18"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Ajouter un objet Ligne

Aspose.PDF pour C++ prend en charge la fonctionnalité d'ajouter des objets graphiques (par exemple graph, ligne, rectangle etc.) aux documents PDF. Vous avez également la possibilité d'ajouter un objet [Line](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.drawing.line/) où vous pouvez également spécifier le motif de tirets, la couleur et d'autres formats pour l'élément Ligne.

Suivez les étapes ci-dessous :

1. Créez un nouveau [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document/) PDF

1. Ajoutez une [Page](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page/) à la collection de pages du fichier PDF

1. Créez une instance de [Graph](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.drawing.graph/).

1. Ajoutez l'objet Graph à la collection de paragraphes de l'instance de page.

1. Créer une instance de [Rectangle](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.drawing.rectangle/).

1. Définir la largeur de ligne.

1. Ajouter l'objet [Rectangle](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.drawing.rectangle/) à la collection de formes de l'objet Graph.

1. Enregistrer votre fichier PDF.

Le fragment de code suivant montre comment ajouter un objet [Rectangle](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.drawing.rectangle/) qui est rempli de couleur.

```cpp

void AddLineObjectToPDF()
{

String _dataDir("C:\\Samples\\");

// Créer une instance de Document

auto document = MakeObject<Document>();


// Ajouter une page à la collection de pages du fichier PDF

auto page = document->get_Pages()->Add();


// Créer une instance de Graph

auto graph = MakeObject<Aspose::Pdf::Drawing::Graph>(100, 400);


// Ajouter l'objet graph à la collection de paragraphes de l'instance de page

page->get_Paragraphs()->Add(graph);


// Créer une instance de Rectangle

auto line = MakeObject<Aspose::Pdf::Drawing::Line>(new float[] { 100, 100, 200, 100 });



// Spécifier la couleur de remplissage pour l'objet Graph

line->get_GraphInfo()->set_DashArray (MakeArray<int>({ 0, 1, 0 }));

line->get_GraphInfo()->set_DashPhase (1);



// Ajouter l'objet rectangle à la collection de formes de l'objet Graph

graph->get_Shapes()->Add(line);



// Enregistrer le fichier PDF

document->Save(_dataDir + u"AddLineObject_out.pdf");
}

```
![Add Line](add_line.png)

## Comment ajouter une ligne pointillée à votre document PDF

```cpp
void DashLengthInBlackAndDashLengthInWhite()
{

String _dataDir("C:\\Samples\\");

// Créer une instance de Document

auto document = MakeObject<Document>();


// Ajouter une page à la collection de pages du fichier PDF

auto page = document->get_Pages()->Add();


// Créer un objet de dessin avec des dimensions spécifiques

auto canvas = MakeObject<Aspose::Pdf::Drawing::Graph>(100, 400);

// Ajouter l'objet de dessin à la collection de paragraphes de l'instance de la page

page->get_Paragraphs()->Add(canvas);



// Créer un objet Ligne

auto line = MakeObject<Aspose::Pdf::Drawing::Line>(MakeArray<float>({ 100, 100, 200, 100 }));

// Définir la couleur pour l'objet Ligne

line->get_GraphInfo()->set_Color (Aspose::Pdf::Color::get_Red());

// Spécifier le tableau de tirets pour l'objet ligne

line->get_GraphInfo()->set_DashArray(MakeArray<int>({ 0, 1, 0 }));

// Définir la phase de tiret pour l'instance Ligne

line->get_GraphInfo()->set_DashPhase(1);

// Ajouter la ligne à la collection de formes de l'objet de dessin

canvas->get_Shapes()->Add(line);


// Enregistrer le fichier PDF

document->Save(_dataDir + u"DashLength_out.pdf");
}
```

Let's check the result:

![Dashed Line](dash_line.png)

## Tracer une ligne à travers la page

Nous pouvons également utiliser un objet ligne pour dessiner une croix commençant du coin inférieur gauche au coin supérieur droit et du coin supérieur gauche au coin inférieur droit.

Veuillez jeter un coup d'œil au code suivant pour accomplir cette exigence.

```cpp
void ExampleLineAcrossPage() {

    // Créer une instance de Document
    String _dataDir("C:\\Samples\\");
    // Créer une instance de Document
    auto document = MakeObject<Document>();
   
    // Ajouter une page à la collection de pages du fichier PDF
    auto page = document->get_Pages()->Add();
    // Définir la marge de la page sur tous les côtés à 0

    page->get_PageInfo()->get_Margin()->set_Left(0);
    page->get_PageInfo()->get_Margin()->set_Right(0);
    page->get_PageInfo()->get_Margin()->set_Bottom(0);
    page->get_PageInfo()->get_Margin()->set_Top(0);

    // Créer un objet Graph avec une largeur et une hauteur égales aux dimensions de la page
    auto graph = MakeObject<Aspose::Pdf::Drawing::Graph>(
        page->get_PageInfo()->get_Width(), 
        page->get_PageInfo()->get_Height());

    // Créer le premier objet ligne commençant du coin inférieur gauche au coin supérieur droit de la page
    auto line = MakeObject<Aspose::Pdf::Drawing::Line>(
        MakeArray<double>({ 
                      page->get_Rect()->get_LLX(), 0, 
                      page->get_PageInfo()->get_Width(),
                      page->get_Rect()->get_URY() }));

    // Ajouter la ligne à la collection de formes de l'objet Graph
    graph->get_Shapes()->Add(line);
    // Dessiner une ligne du coin supérieur gauche de la page au coin inférieur droit de la page
    auto line2 = MakeObject<Aspose::Pdf::Drawing::Line>( MakeArray<double>({0, 
        page->get_Rect()->get_URY(), page->get_PageInfo()->get_Width(), page->get_Rect()->get_LLX() }));

    // Ajouter la ligne à la collection de formes de l'objet Graph
    graph->get_Shapes()->Add(line2);
    // Ajouter l'objet Graph à la collection de paragraphes de la page
    page->get_Paragraphs()->Add(graph);

    // Enregistrer le fichier PDF
    document->Save(_dataDir + u"DrawingLine_out.pdf");
}
```

![Dessiner une ligne](draw_line.png)