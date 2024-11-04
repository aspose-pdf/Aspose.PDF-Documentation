---
title: Extraire les données de tableau d'un PDF 
linktitle: Extraire les données de tableau
type: docs
weight: 40
url: /php-java/extract-data-from-table-in-pdf/
description: Apprenez à extraire des données tabulaires d'un PDF en utilisant Aspose.PDF pour PHP
lastmod: "2021-05-20"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Extraire des tableaux d'un PDF par programmation

Extraire des tableaux de PDFs n'est pas une tâche triviale car le tableau peut être créé de diverses manières.

Aspose.PDF pour PHP via Java a un outil pour faciliter la récupération des tableaux. Pour extraire les données d'un tableau, vous devez suivre les étapes suivantes :

1. Ouvrez le document PDF - instanciez un objet [Document](https://reference.aspose.com/pdf/php-java/com.aspose.pdf/Document);
1. Créez un objet TableAbsorber [TableAbsorber](https://reference.aspose.com/pdf/php-java/com.aspose.pdf/tableabsorber) pour extraire les tableaux du document.
1. Parcourez chaque page du document.

1. Décidez quelles pages doivent être analysées et appliquez [visit](https://reference.aspose.com/pdf/php-java/com.aspose.pdf/TableAbsorber#visit-com.aspose.pdf.Page-) aux pages souhaitées. Les données tabulaires seront scannées, et le résultat sera enregistré dans une liste de [AbsorbedTable](https://reference.aspose.com/pdf/php-java/com.aspose.pdf/AbsorbedTable). Nous pouvons obtenir cette liste via la méthode [getTableList](https://reference.aspose.com/pdf/php-java/com.aspose.pdf/TableAbsorber#getTableList--).

1. Pour obtenir les données, itérez à travers `TableList` et gérez la liste des [lignes absorbées](https://reference.aspose.com/pdf/php-java/com.aspose.pdf/AbsorbedRow) et la liste des cellules absorbées. Nous pouvons accéder à la première liste en appelant la méthode [getTableList](https://reference.aspose.com/pdf/php-java/com.aspose.pdf/TableAbsorber#getTableList--) et à la seconde en appelant [getCellList](https://reference.aspose.com/pdf/php-java/com.aspose.pdf/AbsorbedRow#getCellList--).

1. Chaque [AbsorbedCell](https://reference.aspose.com/pdf/php-java/com.aspose.pdf/AbsorbedCell) contient des [TextFragmentCollections](https://reference.aspose.com/pdf/php-java/com.aspose.pdf/TextFragmentCollection). Vous pouvez les traiter pour vos propres besoins.

L'exemple suivant montre l'extraction de table de toutes les pages :

```php

$document = new Document($inputFile);
$tableAbsorber = new TableAbsorber();


for ($pageIndex = 1; $pageIndex <= java_values($pages->size()); $pageIndex++) {
    $page = $pages->get_Item($pageIndex);
    $tableAbsorber->visit($page);
    $tableList = $tableAbsorber->getTableList();
    $tableIterator = $tableList->iterator();

    while (java_values($tableIterator->hasNext())) {
        $table = $tableIterator->next();
        $tableRowList = $table->getRowList();
        $tableRowListIterator = $tableRowList->iterator();

        while (java_values($tableRowListIterator->hasNext())) {
            $row = $tableRowListIterator->next();
            $cellList = $row->getCellList();
            $cellListIterator = $cellList->iterator();

            // Itérer à travers chaque cellule de la ligne.
            while (java_values($cellListIterator->hasNext())) {
                $cell = $cellListIterator->next();
                $fragmentList = $cell->getTextFragments();

                // Itérer à travers chaque fragment de texte dans la cellule.
                for ($fragmentIndex = 1; $fragmentIndex <= java_values($fragmentList->size()); $fragmentIndex++) {
                    $fragment = $fragmentList->get_Item($fragmentIndex);
                    $segments = $fragment->getSegments();

                    // Itérer à travers chaque segment dans le fragment de texte.
                    for ($segmentIndex = 1; $segmentIndex <= java_values($segments->size()); $segmentIndex++) {
                        $segment = $segments->get_Item($segmentIndex);
                        $responseData .= $segment->getText();
                    }
                }
                $responseData .= "|";
            }
            $responseData .= PHP_EOL;
        }
    }
}

// Enregistrer les données de la table dans le fichier de sortie.
file_put_contents($outputFile, $responseData);

// Fermer le document PDF.
$document->close();
```


## Extraire des données de tableau à partir d'un PDF et les stocker dans un fichier CSV

L'exemple suivant montre comment extraire un tableau et le stocker en tant que fichier CSV.
Pour voir comment convertir un PDF en feuille de calcul Excel, veuillez vous référer à l'article [Convertir PDF en Excel](/pdf/php-java/convert-pdf-to-excel/).

```php

    // Charger le document PDF d'entrée en utilisant la classe Document.
    $document = new Document($inputFile);

    // Créer une instance de la classe ExcelSaveOptions pour spécifier les options de sauvegarde.
    $saveOption = new ExcelSaveOptions();

    // Définir le format de sortie sur CSV.
    $saveOption->setFormat(ExcelSaveOptions_ExcelFormat::$CSV);

    // Enregistrer le document PDF en tant que fichier Excel en utilisant les options de sauvegarde spécifiées.
    $document->save($outputFile, $saveOption);
```