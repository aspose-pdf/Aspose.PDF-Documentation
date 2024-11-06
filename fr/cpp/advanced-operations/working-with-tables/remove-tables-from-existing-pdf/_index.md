---
title: Supprimer les tableaux d'un PDF existant
linktitle: Supprimer les tableaux
type: docs
weight: 50
url: fr/cpp/remove-tables-from-existing-pdf/
description: Cette section décrit comment supprimer un tableau d'un document PDF.
lastmod: "2021-11-11"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

Aspose.PDF pour C++ vous permet d'insérer et de créer un tableau à l'intérieur d'un document PDF pendant sa création à partir de zéro, ou vous pouvez également ajouter l'objet tableau dans un document PDF existant. Mais vous pouvez avoir besoin de [manipuler les tableaux dans un PDF existant](https://docs.aspose.com/pdf/cpp/manipulate-tables-in-existing-pdf/) où vous pouvez mettre à jour le contenu des cellules de tableau existantes. De plus, vous pouvez être confronté à une exigence de suppression des objets tableau des documents PDF existants.

Pour supprimer les tableaux, nous devons utiliser la classe [TableAbsorber](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.text.absorbed_table) pour identifier les tableaux dans le PDF existant, puis appeler la méthode 'Remove'.

## Supprimer un tableau d'un document PDF

Nous avons ajouté une nouvelle fonction, c'est-à-dire. [Remove](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.text.table_absorber#ace39006d8f44c9cb776ee26281a1cbb3) à la classe existante TableAbsorber afin de supprimer une table du document PDF. Une fois que l'absorbeur trouve avec succès les tables sur la page, il devient capable de les supprimer. Veuillez vérifier l'extrait de code suivant montrant comment supprimer une table d'un document PDF :

>En-têtes :

```cpp
#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/Page.h>
#include <Aspose.PDF.Cpp/PageCollection.h>
#include <Aspose.PDF.Cpp/Text/TableAbsorber/TableAbsorber.h>
```

>Exemples :

```cpp
using namespace System;
using namespace Aspose::Pdf;

void RemoveTable() {

    String _dataDir("C:\\Samples\\");

    // Charger le document PDF source
    auto document = MakeObject<Document>(_dataDir + u"Table_input.pdf");

    // Créer un objet TableAbsorber pour trouver les tables
    auto absorber = MakeObject<Aspose::Pdf::Text::TableAbsorber>();

    // Visiter la première page avec l'absorbeur
    absorber->Visit(document->get_Pages()->idx_get(1));

    // Obtenir la première table sur la page
    auto table = absorber->get_TableList()->idx_get(0);

    // Supprimer la table
    absorber->Remove(table);

    // Enregistrer le PDF
    document->Save(_dataDir + u"Table_out.pdf");
}
```
## Supprimer plusieurs tableaux d'un document PDF

Certaines tâches seront associées au travail avec plusieurs tableaux dans un document pdf. Et vous aurez besoin de supprimer plusieurs tableaux de celui-ci. Pour supprimer plusieurs tableaux d'un document PDF, utilisez l'extrait de code suivant :

```cpp
void RemoveMultipleTables() {

    String _dataDir("C:\\Samples\\");

    // Charger le document PDF existant
    auto document = MakeObject<Document>(_dataDir + u"Table_input2.pdf");

    // Créer un objet TableAbsorber pour trouver les tableaux
    auto absorber = MakeObject<Aspose::Pdf::Text::TableAbsorber>();

    // Visiter la première page avec l'absorbeur
    absorber->Visit(document->get_Pages()->idx_get(1));

    // Obtenir une copie de la collection de tableaux
    auto tables = absorber->get_TableList();


    // Boucler à travers la copie de la collection et supprimer les tableaux
    for(auto table : tables)
    absorber->Remove(table);

    // Enregistrer le document
    document->Save(_dataDir + u"Table2_out.pdf");
}
```

{{% alert color="primary" %}}

Veuillez prendre en compte que la suppression ou le remplacement d'un tableau modifie la collection TableList. {{% /alert %}}

Par conséquent, en cas de suppression/remplacement des tables dans une boucle, la copie de la collection TableList est essentielle.

