---
title: Création d'un PDF complexe
linktitle: Création d'un PDF complexe
type: docs
weight: 60
url: /cpp/complex-pdf-example/
description: Aspose.PDF pour C++ vous permet de créer des documents plus complexes contenant des images, des fragments de texte et des tableaux dans un seul document.
lastmod: "2021-11-05"
sitemap:
    changefreq: "monthly"
    priority: 0.5
---

L'exemple [Hello, World](/pdf/cpp/hello-world-example/) a montré des étapes simples pour créer un document PDF en utilisant C++ et Aspose.PDF. Dans cet article, nous allons examiner la création d'un document plus complexe avec C++ et Aspose.PDF pour C++. À titre d'exemple, nous prendrons un document d'une entreprise fictive qui exploite des services de ferry pour passagers.
Notre document contiendra une image, deux fragments de texte (en-tête et paragraphe) et un tableau. Pour construire un tel document, nous utiliserons une approche basée sur le DOM. Vous pouvez en savoir plus dans la section [Bases de l'API DOM](/pdf/cpp/basics-of-dom-api/).

Si nous créons un document à partir de zéro, nous devons suivre certaines étapes :

1. Créez une [Classe String](https://reference.aspose.com/pdf/cpp/class/system.string) pour le nom de chemin et le nom de fichier.
1. Instanciez un objet [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document). Dans cette étape, nous créerons un document PDF vide avec quelques métadonnées mais sans pages.
1. Ajoutez une [Page](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page) à l'objet document. Ainsi, notre document aura désormais une page.
1. Ajoutez une [Image](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.image) à la Page.
1. Créez un [TextFragment](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.text.text_fragment/) pour l'en-tête. Pour l'en-tête, nous utiliserons la police Arial avec une taille de police de 24pt et un alignement centré.
1. Ajoutez l'en-tête aux [Paragraphs](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page#ac5c48bedc9fe8a7e0800a1d9b2c28170) de la page. Créez un [TextFragment](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.text.text_fragment/) pour la description. Pour la description, nous utiliserons la police Arial avec une taille de police de 24pt et un alignement centré.
1. Ajoutez (description) aux Paragraphes de la page.
1. Créez un tableau, ajoutez des propriétés au tableau.
1. Ajoutez (table) aux [Paragraphes](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page#ac5c48bedc9fe8a7e0800a1d9b2c28170) de la page.
1. Enregistrez un document "Complex.pdf".

```cpp
void ExampleComplex()
{
    String outputFileName;

    // Chaîne pour le nom du chemin.
    String _dataDir("C:\\Samples\\");

    // Chaîne pour le nom du fichier.
    String filename("Complex.pdf");

    // Initialiser l'objet document
    auto document = MakeObject<Document>();
    // Ajouter une page
    auto page = document->get_Pages()->Add();

    // Ajouter une image
    String imageFileName = _dataDir + String(u"logo.png");

    // Ajouter une image à la collection Images des ressources de la page
    auto rectangle = MakeObject<Rectangle>(20, 730, 120, 830);
    page->AddImage(imageFileName, rectangle);

    // Ajouter un en-tête
    auto header = MakeObject<TextFragment>(u"Nouvelles routes de ferry à l'automne 2020");
    auto textFragementState = header->get_TextState();
    textFragementState->set_Font(FontRepository::FindFont(u"Arial"));
    textFragementState->set_FontSize(24);
    header->set_HorizontalAlignment(HorizontalAlignment::Center);
    auto position = MakeObject<Aspose::Pdf::Text::Position>(130, 720);
    header->set_Position(position);
    page->get_Paragraphs()->Add(header);

    // Ajouter une description
    String descriptionText(u"Les visiteurs doivent acheter des billets en ligne et les billets sont limités à 5 000 par jour. Le service de ferry fonctionne à moitié de sa capacité et selon un horaire réduit. Attendez-vous à des files d'attente.");
    auto description = MakeObject<TextFragment>(descriptionText);
    description->get_TextState()->set_Font(FontRepository::FindFont(u"Times New Roman"));
    description->get_TextState()->set_FontSize(14);
    description->set_HorizontalAlignment(HorizontalAlignment::Left);
    page->get_Paragraphs()->Add(description);

    // Ajouter un tableau
    auto table = MakeObject<Table>();
    table->set_ColumnWidths(u"200");

    table->set_Border(MakeObject<BorderInfo>(Aspose::Pdf::BorderSide::Box, 1.0f, Aspose::Pdf::Color::get_DarkSlateGray()));
    table->set_DefaultCellBorder(MakeObject<BorderInfo>(Aspose::Pdf::BorderSide::Box, .5f, Aspose::Pdf::Color::get_Black()));
    table->get_Margin()->set_Bottom(10);
    table->get_DefaultCellTextState()->set_Font(FontRepository::FindFont(u"Helvetica"));

    auto headerRow = table->get_Rows()->Add();
    headerRow->get_Cells()->Add(u"Départs ville");
    headerRow->get_Cells()->Add(u"Départs île");

    for (auto headerRowCell : headerRow->get_Cells())
    {
        headerRowCell->set_BackgroundColor(Color::get_Gray());
        headerRowCell->get_DefaultCellTextState()->set_ForegroundColor(Color::get_WhiteSmoke());
    }

    String arrivals[10] = { u"6:00",u"6:45", u"7:00", u"7:45", u"8:00", u"8:45", u"9:00", u"9:45", u"10:00", u"10:45" };
    String departures[10] = { u"7:00", u"7:45", u"8:00", u"8:45", u"9:00", u"9:45", u"10:00", u"10:45", u"11:00", u"11:45" };

    for (int i = 0; i < 10; i++)
    {
        auto dataRow = table->get_Rows()->Add();
        dataRow->get_Cells()->Add(arrivals[i]);
        dataRow->get_Cells()->Add(departures[i]);
    }

    page->get_Paragraphs()->Add(table);

    // Enregistrer le PDF mis à jour
    outputFileName = _dataDir + filename;

    document->Save(outputFileName);
}
```