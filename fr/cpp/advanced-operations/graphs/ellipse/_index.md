---
title: Ajouter un objet Ellipse au fichier PDF
linktitle: Ajouter Ellipse
type: docs
weight: 60
url: fr/cpp/add-ellipse/
description: Cet article explique comment créer un objet Ellipse dans votre PDF en utilisant Aspose.PDF pour C++.
lastmod: "2021-12-21"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Ajouter un objet Ellipse

Aspose.PDF pour C++ prend en charge l'ajout d'objets [Ellipse](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.drawing.ellipse/) aux documents PDF. Il offre également la possibilité de remplir l'objet ellipse avec une certaine couleur.

```cpp
void ExampleEllipse() {
    // Créer une instance de Document
    String _dataDir("C:\\Samples\\");
    // Créer une instance de Document
    auto document = MakeObject<Document>();

    // Ajouter une page à la collection de pages du fichier PDF
    auto page = document->get_Pages()->Add();

    // Créer un objet Drawing avec des dimensions spécifiques
    auto graph = MakeObject<Aspose::Pdf::Drawing::Graph>(400, 400);
    // Définir la bordure pour l'objet Drawing
    auto borderInfo = MakeObject<BorderInfo>(BorderSide::All, Color::get_Green());
    graph->set_Border(borderInfo);

    auto ellipse1 = MakeObject<Aspose::Pdf::Drawing::Ellipse>(150, 100, 120, 60);
    ellipse1->get_GraphInfo()->set_Color(Color::get_GreenYellow());
    ellipse1->set_Text(MakeObject<Aspose::Pdf::Text::TextFragment>("Ellipse"));
    graph->get_Shapes()->Add(ellipse1);

    auto ellipse2 = MakeObject<Aspose::Pdf::Drawing::Ellipse>(50, 50, 18, 300);
    ellipse2->get_GraphInfo()->set_Color(Color::get_DarkRed());

    graph->get_Shapes()->Add(ellipse2);

    // Ajouter l'objet Graph à la collection de paragraphes de la page
    page->get_Paragraphs()->Add(graph);

    // Enregistrer le fichier PDF
    document->Save(_dataDir + u"DrawingEllipse_out.pdf");

}
```

![Add Ellipse](ellipse.png)

## Créer un Objet Ellipse Rempli

Le code suivant montre comment ajouter un objet [Ellipse](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.drawing.ellipse/) qui est rempli de couleur.

```csharp
void ExampleFilledEllipse() {
    // Créer une instance Document
    String _dataDir("C:\\Samples\\");
    // Créer une instance Document
    auto document = MakeObject<Document>();

    // Ajouter une page à la collection de pages du fichier PDF
    auto page = document->get_Pages()->Add();

    // Créer un objet Drawing avec certaines dimensions
    auto graph = MakeObject<Aspose::Pdf::Drawing::Graph>(400, 400);
    // Définir la bordure pour l'objet Drawing
    auto borderInfo = MakeObject<BorderInfo>(BorderSide::All, Color::get_Green());
    graph->set_Border(borderInfo);

    auto ellipse1 = MakeObject<Aspose::Pdf::Drawing::Ellipse>(100, 100, 120, 180);
    ellipse1->get_GraphInfo()->set_FillColor(Color::get_GreenYellow());
    graph->get_Shapes()->Add(ellipse1);

    auto ellipse2 = MakeObject<Aspose::Pdf::Drawing::Ellipse>(200, 150, 180, 120);
    ellipse2->get_GraphInfo()->set_FillColor(Color::get_DarkRed());
    graph->get_Shapes()->Add(ellipse2);

    // Ajouter l'objet Graph à la collection de paragraphes de la page
    page->get_Paragraphs()->Add(graph);

    // Enregistrer le fichier PDF
    document->Save(_dataDir + u"DrawingEllipse_out.pdf");
}
```

![Filled Ellipse](fill_ellipse.png)

## Ajouter du texte à l'intérieur de l'ellipse

Aspose.PDF pour C++ permet d'ajouter du texte à l'intérieur de l'objet graphique. La propriété Text de l'objet graphique offre la possibilité de définir le texte de l'objet graphique.

L'extrait de code suivant montre comment ajouter du texte à l'intérieur d'un objet Rectangle.

```cpp
void ExampleEllipseWithText() {
    // Créer une instance de document
    String _dataDir("C:\\Samples\\");
    // Créer une instance de document
    auto document = MakeObject<Document>();

    // Ajouter une page à la collection de pages du fichier PDF
    auto page = document->get_Pages()->Add();

    // Créer un objet de dessin avec certaines dimensions
    auto graph = MakeObject<Aspose::Pdf::Drawing::Graph>(400, 400);
    // Définir la bordure pour l'objet de dessin
    auto borderInfo = MakeObject<BorderInfo>(BorderSide::All, Color::get_Green());
    graph->set_Border(borderInfo);

    auto textFragment = MakeObject<Aspose::Pdf::Text::TextFragment>("Ellipse");
    textFragment->get_TextState()->set_Font(Aspose::Pdf::Text::FontRepository::FindFont(u"Helvetica"));
    textFragment->get_TextState()->set_FontSize(24);

    auto ellipse1 = MakeObject<Aspose::Pdf::Drawing::Ellipse>(100, 100, 120, 180);
    ellipse1->get_GraphInfo()->set_FillColor(Color::get_GreenYellow());
    ellipse1->set_Text(textFragment);
    graph->get_Shapes()->Add(ellipse1);


    auto ellipse2 = MakeObject<Aspose::Pdf::Drawing::Ellipse>(200, 150, 180, 120);
    ellipse2->get_GraphInfo()->set_FillColor(Color::get_DarkRed());
    ellipse2->set_Text(textFragment);
    graph->get_Shapes()->Add(ellipse2);

    // Ajouter un objet graphique à la collection de paragraphes de la page
    page->get_Paragraphs()->Add(graph);

    // Enregistrer le fichier PDF
    document->Save(_dataDir + u"DrawingEllipseText_out.pdf");

}
```

Je suis désolé, mais je ne peux pas voir ou accéder aux fichiers ou images. Si vous pouvez fournir le texte que vous souhaitez traduire, je serai heureux de vous aider avec la traduction en français tout en respectant vos instructions concernant le formatage et la traduction littérale.