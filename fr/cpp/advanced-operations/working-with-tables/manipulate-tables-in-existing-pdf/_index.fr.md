---
title: Manipuler des Tables dans un PDF existant
linktitle: Manipuler des Tables
type: docs
weight: 40
url: /cpp/manipulate-tables-in-existing-pdf/
description: Cette section couvre diverses méthodes de modification de table en utilisant Aspose.PDF for C++
lastmod: "2021-11-11"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Manipuler des tables dans un PDF existant

Aspose.PDF for C++ vous permet de travailler rapidement et efficacement avec des tables, à savoir, les créer de toutes pièces ou les ajouter à des documents PDF existants.

Vous avez également la possibilité d'intégrer la table avec la base de données (DOM) pour créer des tables dynamiques basées sur le contenu de la base de données.

La classe [Aspose.PDF.Text.TableAbsorber](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.text.absorbed_table) vous permet de rechercher et d'analyser des tables simples qui existent déjà sur une page de document PDF. L'extrait de code suivant montre les étapes pour mettre à jour le contenu dans une cellule spécifique d'une table.

>En-têtes:

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
#include <Aspose.PDF.Cpp/Generator/BorderInfo.h>
#include <Aspose.PDF.Cpp/Generator/BorderSide.h>

#include <Aspose.PDF.Cpp/Text/TextFragment.h>
#include <Aspose.PDF.Cpp/Text/TextFragmentCollection.h>

#include <Aspose.PDF.Cpp/Color.h>

#include <Aspose.PDF.Cpp/Table/Table.h>
#include <Aspose.PDF.Cpp/Table/Row.h>
#include <Aspose.PDF.Cpp/Table/Rows.h>
#include <Aspose.PDF.Cpp/Table/Cell.h>
#include <Aspose.PDF.Cpp/Table/Cells.h>
#include <Aspose.PDF.Cpp/Text/TableAbsorber/TableAbsorber.h>
#include <Aspose.PDF.Cpp/Text/TableAbsorber/AbsorbedTable.h>
#include <Aspose.PDF.Cpp/Text/TableAbsorber/AbsorbedRow.h>
#include <Aspose.PDF.Cpp/Text/TableAbsorber/AbsorbedCell.h>
```

>Exemples:

```cpp
using namespace System;
using namespace Aspose::Pdf;

#include "Table-Manipulate.h"

void ManipulateTables() {

    String _dataDir("C:\\Samples\\");

    // Charger un fichier PDF existant
    auto document = MakeObject<Document>(_dataDir + u"input.pdf");

    // Créer un objet TableAbsorber pour trouver des tables
    auto absorber = MakeObject<Aspose::Pdf::Text::TableAbsorber>();

    // Visiter la première page avec l'absorbeur
    absorber->Visit(document->get_Pages()->idx_get(1));

    // Accéder à la première table sur la page, à leur première cellule et aux fragments de texte à l'intérieur
    auto fragment = absorber->get_TableList()->idx_get(0)->get_RowList()->idx_get(0)->get_CellList()->idx_get(0)->get_TextFragments()->idx_get(1);

    // Modifier le texte du premier fragment de texte dans la cellule
    fragment->set_Text(u"salut monde");
    document->Save(_dataDir + u"ManipulateTable_out.pdf");
}
```

## Remplacer une ancienne table par une nouvelle dans un document PDF

Dans le cas où vous devez trouver une table particulière et la remplacer par celle souhaitée, vous pouvez utiliser la méthode Replace() de la classe [TableAbsorber](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.text.absorbed_table) pour le faire.

Le exemple suivant démontre la fonctionnalité pour remplacer la table dans le document PDF :

```cpp
void ReplaceOldTable() {
    String _dataDir("C:\\Samples\\");

    // Charger le fichier PDF existant
    auto document = MakeObject<Document>(_dataDir + u"Table_input2.pdf");

    // Créer un objet TableAbsorber pour trouver les tables
    auto absorber = MakeObject<Aspose::Pdf::Text::TableAbsorber>();

    // Visiter la première page avec l'absorbeur
    absorber->Visit(document->get_Pages()->idx_get(1));

    // Obtenir la première table sur la page
    auto table = absorber->get_TableList()->idx_get(0);

    // Créer une nouvelle table
    auto newTable = MakeObject<Table>();
    newTable->set_ColumnWidths(u"100 100 100");
    newTable->set_DefaultCellBorder (MakeObject<BorderInfo>(BorderSide::All, 1.0F));

    auto row = newTable->get_Rows()->Add();
    row->get_Cells()->Add(u"Col 1");
    row->get_Cells()->Add(u"Col 2");
    row->get_Cells()->Add(u"Col 3");

    // Remplacer la table par une nouvelle
    absorber->Replace(document->get_Pages()->idx_get(1), table, newTable);

    // Enregistrer le document
    document->Save(_dataDir + u"TableReplaced_out.pdf");
}
```