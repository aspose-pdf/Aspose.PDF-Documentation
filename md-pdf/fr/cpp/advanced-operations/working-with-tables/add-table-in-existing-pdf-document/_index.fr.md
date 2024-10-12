---
title: Créer ou Ajouter un Tableau dans un PDF 
linktitle: Créer ou Ajouter un Tableau
type: docs
weight: 10
url: /cpp/add-table-in-existing-pdf-document/
description: Aspose.PDF pour C++ est une bibliothèque utilisée pour créer, lire et éditer des tableaux PDF. En utilisant cette bibliothèque, vous pouvez paginer un tableau sur la page PDF en utilisant C++.
lastmod: "2021-11-11"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Création de Tableau en utilisant C++

Les tableaux sont importants lorsque l'on travaille avec des documents PDF. Ils offrent d'excellentes fonctionnalités pour afficher des informations de manière systématique.

Les tableaux dans un document PDF organisent les données en lignes et colonnes de manière systématique. L'API Aspose.PDF pour C++ vous permet d'ajouter des tableaux à un document PDF, ainsi que d'ajouter des lignes et des colonnes à celui-ci dans vos applications C++. La classe [Table](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.table/) est utilisée pour ajouter un tableau au document. Les étapes suivantes peuvent être suivies pour ajouter un tableau à un document PDF en utilisant C++.

### Ajout de Tableau dans un Document PDF Existant

Pour ajouter un tableau à un fichier PDF existant avec Aspose.PDF pour C++, suivez les étapes suivantes :

1. Chargez le fichier source.
1. Initialisez un tableau et définissez ses colonnes et ses lignes.
1. Définissez les paramètres du tableau (nous avons défini les bordures).
1. Remplissez le tableau.
1. Ajoutez le tableau à une page.
1. Enregistrez le fichier.

Les extraits de code suivants montrent comment ajouter du texte dans un fichier PDF existant.

>En-têtes

```cpp
#include <system/date_time.h>
#include <system/io/file.h>
#include <system/console.h>
#include <data/data_table.h>
#include <data/data_column_collection.h>
#include <system/type_info.h>

#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/Page.h>
#include <Aspose.PDF.Cpp/PageCollection.h>
#include <Aspose.PDF.Cpp/Generator/Paragraphs.h>
#include <Aspose.PDF.Cpp/Generator/BorderSide.h>
#include <Aspose.PDF.Cpp/Generator/BorderInfo.h>
#include <Aspose.PDF.Cpp/Generator/PageInfo.h>
#include <Aspose.PDF.Cpp/Generator/MarginInfo.h>
#include <Aspose.PDF.Cpp/Generator/GraphInfo.h>
#include <Aspose.PDF.Cpp/Generator/BorderCornerStyle.h>
#include <Aspose.PDF.Cpp/Generator/ColumnAdjustment.h>
#include <Aspose.PDF.Cpp/Generator/ImageFileType.h>
#include <Aspose.PDF.Cpp/Generator/Image.h>
#include <Aspose.PDF.Cpp/Generator/HtmlFragment.h>

#include <Aspose.PDF.Cpp/Text/TextFragment.h>

#include <Aspose.PDF.Cpp/Color.h>

#include <Aspose.PDF.Cpp/Table/Table.h>
#include <Aspose.PDF.Cpp/Table/Row.h>
#include <Aspose.PDF.Cpp/Table/Rows.h>
#include <Aspose.PDF.Cpp/Table/Cell.h>
#include <Aspose.PDF.Cpp/Table/Cells.h>
```

>Échantillon

```cpp
using namespace System;
using namespace Aspose::Pdf;

void AddingTableInExistingPDFDocument() {
    
    String _dataDir("C:\\Samples\\");

    // Charger le document PDF source
    auto document = MakeObject<Document>(_dataDir + u"AddTable.pdf");
    
    // Initialise une nouvelle instance de la Table
    auto table = MakeObject<Table>();
    
    // Définir la couleur de la bordure de la table comme LightGray
    table->set_Border(MakeObject<Aspose::Pdf::BorderInfo>(
        Aspose::Pdf::BorderSide::All, .5f, 
        Aspose::Pdf::Color::get_LightGray()));
    // Définir la bordure pour les cellules de la table
    table->set_DefaultCellBorder (MakeObject<Aspose::Pdf::BorderInfo>(
        Aspose::Pdf::BorderSide::All, .5f, 
        Aspose::Pdf::Color::get_LightGray()));

    // Créer une boucle pour ajouter 10 lignes
    for (int row_count = 1; row_count < 10; row_count++)
    {
        // Ajouter une ligne à la table
        auto row = table->get_Rows()->Add();
        // Ajouter des cellules de table
        row->get_Cells()->Add(String::Format(u"Colonne ({0}, 1)", row_count));
        row->get_Cells()->Add(String::Format(u"Colonne ({0}, 2)", row_count));
        row->get_Cells()->Add(String::Format(u"Colonne ({0}, 3)", row_count));
    }

    // Ajouter l'objet table à la première page du document d'entrée
    document->get_Pages()->idx_get(1)->get_Paragraphs()->Add(table);
    
    // Enregistrer le document mis à jour contenant l'objet table
    document->Save(_dataDir + u"document_with_table_out.pdf");
}
```

### ColSpan et RowSpan dans les Tables

Aspose.PDF pour C++ présente une propriété [ColSpan](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.cell#ae79c581d2245258699c98617e78c01d1) pour fusionner les colonnes dans un tableau et une propriété [RowSpan](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.cell#a4eb7337d118314e6c2180670fb32721a) pour fusionner les lignes.

Nous utilisons la propriété [ColSpan](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.cell#ae79c581d2245258699c98617e78c01d1) ou [RowSpan](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.cell#a4eb7337d118314e6c2180670fb32721a) sur l'objet [Cell](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.cell) qui crée la cellule du tableau. Après avoir appliqué les propriétés requises, la cellule créée peut être ajoutée au tableau.

```cpp
void AddTable_RowColSpan()
{
    String _dataDir("C:\\Samples\\");

    // Charger le document PDF source
    auto document = MakeObject<Document>();
    document->get_Pages()->Add();

    // Initialise une nouvelle instance du tableau
    auto table = MakeObject<Table>();
    // Définir la couleur de la bordure du tableau comme GrisClair
    table->set_Border(MakeObject<Aspose::Pdf::BorderInfo>(
        Aspose::Pdf::BorderSide::All, .5f, 
        Color::get_Black()));
    // Définir la bordure pour les cellules du tableau
    table->set_DefaultCellBorder(
        MakeObject<Aspose::Pdf::BorderInfo>(
            Aspose::Pdf::BorderSide::All, .5f, 
            Color::get_Black()));
    

    // Ajouter la 1ère ligne au tableau
    auto row1 = table->get_Rows()->Add();
    for (int cellCount = 1; cellCount < 5; cellCount++)
    {
        // Ajouter des cellules au tableau
        row1->get_Cells()->Add(String::Format(u"Test 1 {0}", cellCount));
    }

    // Ajouter la 2ème ligne au tableau
    auto row2 = table->get_Rows()->Add();
    row2->get_Cells()->Add(u"Test 2 1");
    auto cell = row2->get_Cells()->Add(u"Test 2 2");
    cell->set_ColSpan(2);
    row2->get_Cells()->Add(u"Test 2 4");

    // Ajouter la 3ème ligne au tableau
    auto row3 = table->get_Rows()->Add();
    row3->get_Cells()->Add(u"Test 3 1");
    row3->get_Cells()->Add(u"Test 3 2");
    row3->get_Cells()->Add(u"Test 3 3");
    row3->get_Cells()->Add(u"Test 3 4");

    // Ajouter la 4ème ligne au tableau
    auto row4 = table->get_Rows()->Add();
    row4->get_Cells()->Add(u"Test 4 1");
    cell = row4->get_Cells()->Add(u"Test 4 2");
    cell->set_RowSpan(2);
    row4->get_Cells()->Add(u"Test 4 3");
    row4->get_Cells()->Add(u"Test 4 4");

    // Ajouter la 5ème ligne au tableau
    auto row5 = table->get_Rows()->Add();
    row5->get_Cells()->Add(u"Test 5 1");
    row5->get_Cells()->Add(u"Test 5 3");
    row5->get_Cells()->Add(u"Test 5 4");

    // Ajouter l'objet tableau à la première page du document d'entrée
    document->get_Pages()->idx_get(1)->get_Paragraphs()->Add(table);

    // Enregistrer le document mis à jour contenant l'objet tableau
    document->Save(_dataDir + u"document_with_table_out.pdf");
}
```

Le résultat de l'exécution du code ci-dessous est le tableau illustré sur l'image suivante :

![Démonstration de ColSpan et RowSpan](colspan_rowspan.png)

## Travailler avec les Bordures, Marges et Espacement

Notez qu'il prend également en charge la fonction de définition des bordures, marges et espacement des cellules pour les tableaux. Comprenons d'abord le concept de bordures, marges et espacement, qui sont présentés dans le schéma ci-dessous :

![Bordures, marges et espacement](set-border-style-margins-and-padding-of-table_1.png)

Examinez le dessin en détail. Il montre que les bordures du tableau, des lignes et des cellules se chevauchent. En utilisant Aspose.PDF pour C++, le tableau peut avoir des marges et les cellules peuvent être indentées. Pour définir les marges des cellules, nous devons définir l'espacement des cellules.

## Bordures

Pour définir les bordures des objets Table, [Row](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.row) et [Cell](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.cell), utilisez les propriétés Table.Border, Row.Border et Cell.Border. Les bordures des cellules peuvent également être définies en utilisant la propriété DefaultCellBorder de la classe [Table](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.table) ou Row. Toutes les propriétés liées aux bordures discutées ci-dessus sont attribuées à une instance de la classe Row, qui est créée en appelant son constructeur. La classe Row a de nombreuses surcharges qui prennent presque tous les paramètres nécessaires pour personnaliser la bordure.

## Marges ou Rembourrage

Le rembourrage des cellules peut être géré en utilisant la propriété [DefaultCellPadding](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.table#ac64196de6dfed7550c3278892ed9dbe0) de la classe Table. Toutes les propriétés liées au rembourrage sont attribuées à une instance de la classe [MarginInfo](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.margin_info/) qui prend des informations sur les paramètres `Left`, `Right`, `Top` et `Bottom` pour créer des marges personnalisées.

![Marge et Bordure dans le Tableau PDF](margin-border.png)

```cpp
void AddTable_MergingPadding() {

    String _dataDir("C:\\Samples\\");

    // Instancier l'objet Document en appelant son constructeur vide
    auto document = MakeObject<Document>();
    auto page = document->get_Pages()->Add();

    // Instancier un objet table
    auto tab1 = MakeObject<Table>();
    // Ajouter la table dans la collection de paragraphes de la section souhaitée
    page->get_Paragraphs()->Add(tab1);
    // Définir les largeurs de colonne de la table
    tab1->set_ColumnWidths (u"50 50 50");
    // Définir la bordure par défaut des cellules à l'aide de l'objet BorderInfo
    tab1->set_DefaultCellBorder (
        MakeObject<Aspose::Pdf::BorderInfo>(
            Aspose::Pdf::BorderSide::All, 0.1F));
    // Définir la bordure de la table à l'aide d'un autre objet BorderInfo personnalisé
    tab1->set_Border (
        MakeObject<Aspose::Pdf::BorderInfo>(
            Aspose::Pdf::BorderSide::All, 1.0F));

    // Créer un objet MarginInfo et définir ses marges gauche, bas, droite et haut
    auto margin = MakeObject<MarginInfo>();
    margin->set_Top (5.0f);
    margin->set_Left (5.0f);
    margin->set_Right (5.0f);
    margin->set_Bottom (5.0f);

    // Définir le rembourrage par défaut des cellules sur l'objet MarginInfo
    tab1->set_DefaultCellPadding (margin);
    // Créer des lignes dans la table puis des cellules dans les lignes
    auto row1 = tab1->get_Rows()->Add();
    row1->get_Cells()->Add(u"col1");
    row1->get_Cells()->Add(u"col2");
    row1->get_Cells()->Add();

    auto mytext = MakeObject<Aspose::Pdf::Text::TextFragment>(u"col3 with large text string");
        
    row1->get_Cells()->idx_get(2)->get_Paragraphs()->Add(mytext);
    row1->get_Cells()->idx_get(2)->set_IsWordWrapped(false);
    

    auto row2 = tab1->get_Rows()->Add();
    row2->get_Cells()->Add(u"item1");
    row2->get_Cells()->Add(u"item2");
    row2->get_Cells()->Add(u"item3");
    
    // Sauvegarder le Pdf
    document->Save(_dataDir + u"MarginsOrPadding_out.pdf");
}
```
Pour créer une table avec des coins arrondis, utilisez la classe [BorderInfo](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.border_info) avec la valeur [RoundedBorderRadius](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.border_info#a6a2bed69dd034fba9ce439dcbe1fd3de) et définissez le style des coins de la table sur arrondi.

```cpp
void AddTable_RoundedBorderRadius()
{
    // Le chemin vers le répertoire des documents.
    String _dataDir("C:\\Samples\\");

    auto tab1 = MakeObject<Aspose::Pdf::Table>();

    auto graph = MakeObject<GraphInfo>();
    graph->set_Color(Color::get_Red());
    // Créer un objet BorderInfo vide
    auto bInfo = MakeObject<BorderInfo>(BorderSide::All, graph);

    // Définir la bordure comme une bordure arrondie où le rayon est de 15
    bInfo->set_RoundedBorderRadius(15);
    // Définir le style des coins de la table comme arrondi.
    tab1->set_CornerStyle (Aspose::Pdf::BorderCornerStyle::Round);
    // Définir les informations de bordure de la table
    tab1->set_Border(bInfo);
}
```

### Propriété AutoFitToWindow dans l'énumération ColumnAdjustmentType

```cpp
void AddTable_AutoFitToWindow() {
    
    // Le chemin d'accès au répertoire des documents.
    String _dataDir("C:\\Samples\\");

    // Instancier l'objet Pdf en appelant son constructeur vide
    auto document = MakeObject<Document>();

    // Créer la section dans l'objet Pdf
    auto sec1 = document->get_Pages()->Add();

    // Instancier un objet table
    auto tab1 = MakeObject<Aspose::Pdf::Table>();
    // Ajouter la table dans la collection de paragraphes de la section souhaitée
    sec1->get_Paragraphs()->Add(tab1);

    // Définir les largeurs de colonne de la table
    tab1->set_ColumnWidths (u"50 50 50");
    tab1->set_ColumnAdjustment (ColumnAdjustment::AutoFitToWindow);

    // Définir la bordure de cellule par défaut en utilisant l'objet BorderInfo
    tab1->set_DefaultCellBorder(MakeObject<BorderInfo>(Aspose::Pdf::BorderSide::All, 0.1F));

    // Définir la bordure de la table en utilisant un autre objet BorderInfo personnalisé
    tab1->set_Border (MakeObject<BorderInfo>(Aspose::Pdf::BorderSide::All, 1.0F));

    // Créer un objet MarginInfo et définir ses marges gauche, bas, droite et haut
    auto margin = MakeObject<MarginInfo>();
    margin->set_Top(5.0f);
    margin->set_Left(5.0f);
    margin->set_Right(5.0f);
    margin->set_Bottom(5.0f);

    // Définir le remplissage de cellule par défaut sur l'objet MarginInfo
    tab1->set_DefaultCellPadding(margin);

    // Créer des lignes dans la table puis des cellules dans les lignes
    auto row1 = tab1->get_Rows()->Add();
    row1->get_Cells()->Add(u"col1");
    row1->get_Cells()->Add(u"col2");
    row1->get_Cells()->Add(u"col3");

    auto row2 = tab1->get_Rows()->Add();
    row2->get_Cells()->Add(u"item1");
    row2->get_Cells()->Add(u"item2");
    row2->get_Cells()->Add(u"item3");
    
    // Enregistrer le document mis à jour contenant l'objet table
    document->Save(_dataDir + u"AutoFitToWindow_out.pdf");
}
```

### Obtenir la largeur de la table

Il y a des tâches dans lesquelles vous devez obtenir dynamiquement la largeur de la table. La classe [Aspose.PDF.Table](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.table) dispose d'une méthode [GetWidth] à cet effet (https://reference.aspose.com/pdf/cpp/class/aspose.pdf.table#a3361cc8d4af87eec2e3da616c474ac1c). Par exemple, vous n'avez pas explicitement défini la largeur des colonnes de la table, et vous n'avez pas défini [ColumnAdjustment] (https://reference.aspose.com/pdf/cpp/namespace/aspose.pdf#afc01382935026dd569c96d77d09dc3a4) à AutoFitToContent. Dans ce cas, vous pouvez obtenir la largeur de la table suivante.

```cpp
void GetTableWidth() {
    // Créer un nouveau document
    auto document = MakeObject<Document>();
    
    // Ajouter une page dans le document
    auto page = document->get_Pages()->Add();

    // Initialiser une nouvelle table
    auto table = MakeObject<Table>();
    table->set_ColumnAdjustment(ColumnAdjustment::AutoFitToContent);
    
    // Ajouter une ligne dans la table
    auto row = table->get_Rows()->Add();

    // Ajouter une cellule dans la table
    auto cell = row->get_Cells()->Add(u"Texte de la cellule 1");
    cell = row->get_Cells()->Add(u"Texte de la cellule 2");
    // Obtenir la largeur de la table
    Console::WriteLine(table->GetWidth());
}
```

## Ajouter une image SVG à une cellule de tableau

Aspose.PDF pour C++ vous permet d'ajouter des cellules de tableau à un fichier PDF. Lorsque vous créez un tableau, vous pouvez ajouter du texte ou des images aux cellules. De plus, l'API offre également une fonction pour convertir des fichiers SVG en PDF. En utilisant une combinaison de ces fonctions, il est possible de charger une image SVG et de l'ajouter à une cellule de tableau.

L'extrait de code suivant montre les étapes pour instancier un tableau et ajouter une image SVG à une cellule de tableau.

```cpp
void InsertSVGObject() 
{
    String _dataDir("C:\\Samples\\");

    // Instancier l'objet Document
    auto document = MakeObject<Document>();
    // Créer une instance d'image
    auto img = MakeObject<Aspose::Pdf::Image>();

    // Définir le type d'image comme SVG
    img->set_FileType(Aspose::Pdf::ImageFileType::Svg);
    // Chemin pour le fichier source
    img->set_File (_dataDir + u"SVGToPDF.svg");
    // Définir la largeur pour l'instance d'image
    img->set_FixWidth (50);
    // Définir la hauteur pour l'instance d'image
    img->set_FixHeight(50);
    // Créer une instance de tableau
    auto table = MakeObject<Aspose::Pdf::Table>();
    // Définir la largeur pour les cellules du tableau
    table->set_ColumnWidths (u"100 100");
    // Créer un objet de ligne et l'ajouter à l'instance de tableau
    auto row = table->get_Rows()->Add();
    // Créer un objet de cellule et l'ajouter à l'instance de ligne
    auto cell = row->get_Cells()->Add();
    // Ajouter un fragment de texte à la collection de paragraphes de l'objet cellule
    cell->get_Paragraphs()->Add(MakeObject<Aspose::Pdf::Text::TextFragment>(u"First cell"));
    // Ajouter une autre cellule à l'objet ligne
    cell = row->get_Cells()->Add();
    // Ajouter une image SVG à la collection de paragraphes de l'instance de cellule récemment ajoutée
    cell->get_Paragraphs()->Add(img);
    // Créer un objet page et l'ajouter à la collection de pages de l'instance de document
    auto page = document->get_Pages()->Add();
    // Ajouter le tableau à la collection de paragraphes de l'objet page
    page->get_Paragraphs()->Add(table);    
    // Enregistrer le fichier PDF
    document->Save(_dataDir + u"AddSVGObject_out.pdf");
}
```

## Utilisation des balises HTML à l'intérieur du tableau

Pour certaines tâches, vous devrez importer le contenu de la base de données avec certaines balises HTML, puis importer le contenu dans un objet Table. Lors de l'importation de contenu, les balises HTML doivent être affichées à l'intérieur du document PDF.

Dans l'extrait de code suivant, vous pouvez définir la couleur de la bordure du tableau, définir la bordure pour les cellules du tableau. Ensuite, vous créerez une boucle pour ajouter 10 lignes. Ajoutez l'objet table à la première page du document d'entrée et enregistrez le document mis à jour.

```cpp
void AddHTMLFragmentToTableCell() {
    String _dataDir("C:\\Samples\\");

    auto document = MakeObject<Document>(_dataDir + u"input.pdf");    
    // Initialise une nouvelle instance de la Table
    auto table = MakeObject<Table>();
    // Définir la couleur de la bordure du tableau comme LightGray
    table->set_Border(new BorderInfo(BorderSide::All, .5f, Color::get_LightGray()));
    // définir la bordure pour les cellules du tableau
    table->set_DefaultCellBorder(new BorderInfo(BorderSide::All, .5f, Color::get_LightGray()));
    // créer une boucle pour ajouter 10 lignes       
    for (int row_count = 1; row_count < 10; row_count++) {
        SmartPtr<Cell> cell;
        // ajouter une ligne au tableau
        auto row = table->get_Rows()->Add();
        // ajouter des cellules au tableau
        cell = row->get_Cells()->Add();
        cell->get_Paragraphs()->Add(new HtmlFragment(String::Format(u"Colonne <strong>({0}, 1)</strong>", row_count)));

        cell = row->get_Cells()->Add();
        cell->get_Paragraphs()->Add(new HtmlFragment(String::Format(u"Colonne <span style='color:red'>({0}, 2)</span>",row_count)));

        cell = row->get_Cells()->Add();
        cell->get_Paragraphs()->Add(new HtmlFragment(String::Format(u"Colonne <span style='text-decoration: underline'>([0}, 3)</span>", row_count)));
    }
    // Ajouter l'objet table à la première page du document d'entrée
    document->get_Pages()->idx_get(1)->get_Paragraphs()->Add(table);
    // Enregistrer le document mis à jour contenant l'objet table
    document->Save(_dataDir + u"AddHTMLObject_out.pdf");
}
```

## Insérer un saut de page entre les lignes du tableau

En général, lors de la création d'un tableau dans un PDF, le tableau se prolonge sur les pages suivantes lorsqu'il atteint la marge inférieure du tableau. Mais nous pouvons avoir besoin d'insérer un saut de page lorsque un certain nombre de lignes sont ajoutées au tableau. Le code suivant montre les étapes pour insérer un saut de page lors de l'ajout de 10 lignes à un tableau.

Le code suivant montre les étapes pour insérer un saut de page lorsque 10 lignes sont ajoutées au tableau.

```cpp
void InsertPageBreak() {
    String _dataDir("C:\\Samples\\");

    // Instancier l'objet Document
    auto document = MakeObject<Document>();
    
    // Ajouter une page à la collection de pages du fichier PDF
    auto page = document->get_Pages()->Add();

    // Créer une instance de tableau
    auto tab = MakeObject<Table>();

    // Définir le style de bordure pour le tableau
    tab->set_Border(MakeObject<BorderInfo>(BorderSide::All, Color::get_Red()));
    // Définir le style de bordure par défaut pour le tableau avec la couleur de bordure en rouge
    tab->set_DefaultCellBorder(MakeObject<BorderInfo>(BorderSide::All, Color::get_Red()));
    // Spécifier la largeur des colonnes du tableau
    tab->set_ColumnWidths(u"100 100");

    // Créer une boucle pour ajouter 200 lignes au tableau
    for (int counter = 0; counter <= 200; counter++) {
        auto row = MakeObject<Row>();
        tab->get_Rows()->Add(row);
        auto cell1 = MakeObject<Cell>();
        cell1->get_Paragraphs()->Add(MakeObject<Aspose::Pdf::Text::TextFragment>(String::Format(u"Cell {0}, 0", counter)));
        row->get_Cells()->Add(cell1);

        auto cell2 = new Cell();
        cell2->get_Paragraphs()->Add(MakeObject<Aspose::Pdf::Text::TextFragment>(String::Format(u"Cell {0}, 1", counter)));
        row->get_Cells()->Add(cell2);
        // Lorsque 10 lignes sont ajoutées, rendre la nouvelle ligne dans une nouvelle page
        if (counter % 10 == 0 && counter != 0)
            row->set_IsInNewPage(true);
    }
    // Ajouter le tableau à la collection de paragraphes du fichier PDF
    page->get_Paragraphs()->Add(tab);

    // Enregistrer le document PDF
    document->Save(_dataDir + u"InsertPageBreak_out.pdf");
}
```

## Rendre un Tableau sur une Nouvelle Page

Par défaut, les paragraphes sont ajoutés à la collection Paragraphs d'un objet Page. Cependant, il est possible de rendre un tableau sur une nouvelle page au lieu de le faire directement après l'objet de niveau paragraphe précédemment ajouté sur la page.

### Exemple : Comment Rendre un Tableau sur une Nouvelle Page en Utilisant C++

Pour rendre un tableau sur une nouvelle page, utilisez la propriété [IsInNewPage](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.base_paragraph#a614946048d22afb9dce4cd42346c7561) dans la classe [BaseParagraph](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.base_paragraph).
Le code suivant montre comment faire.

```cpp
void RenderTableOnNewPage()
{
    auto document = MakeObject<Document>();
    auto pageInfo = document->get_PageInfo();
    auto marginInfo = pageInfo->get_Margin();

    marginInfo->set_Left (37);
    marginInfo->set_Right (37);
    marginInfo->set_Top (37);
    marginInfo->set_Bottom (37);

    pageInfo->set_IsLandscape(true);

    auto table = MakeObject<Aspose::Pdf::Table>();
    table->set_ColumnWidths(u"50 100");
    // Page ajoutée.
    auto curPage = document->get_Pages()->Add();
    for (int i = 1; i <= 120; i++)
    {
        auto row = table->get_Rows()->Add();
        row->set_FixedRowHeight(15);
        auto cell1 = row->get_Cells()->Add();
        cell1->get_Paragraphs()->Add(MakeObject<Aspose::Pdf::Text::TextFragment>(u"Content 1"));
        auto cell2 = row->get_Cells()->Add();
        cell2->get_Paragraphs()->Add(MakeObject<Aspose::Pdf::Text::TextFragment>(u"HHHHH"));
    }
    auto paragraphs = curPage->get_Paragraphs();
    paragraphs->Add(table);

    //-------------------------------------

    auto document = MakeObject<Document>();
    auto table1 = MakeObject<Aspose::Pdf::Table>();
    table1->set_ColumnWidths(u"100 100");

    String _dataDir("C:\\Samples\\");

    for (int i = 1; i <= 10; i++)
    {
        auto row = table1->get_Rows()->Add();
        auto cell1 = row->get_Cells()->Add();
        cell1->get_Paragraphs()->Add(MakeObject<Aspose::Pdf::Text::TextFragment>(u"LAAAAAAA"));
        auto cell2 = row->get_Cells()->Add();
        cell2->get_Paragraphs()->Add(MakeObject<Aspose::Pdf::Text::TextFragment>(u"LAAGGGGGG"));
    }
    
    table1->set_IsInNewPage (true);
    // Je veux garder le tableau 1 à la page suivante s'il vous plaît...
    paragraphs->Add(table1);
    
    document->Save(_dataDir + u"IsNewPageProperty_Test_out.pdf");
}
```