---
title: Créer ou Ajouter un Tableau dans un PDF
linktitle: Créer ou Ajouter un Tableau
type: docs
weight: 10
url: fr/php-java/add-table-in-existing-pdf-document/
description: Apprenez à créer ou ajouter un tableau à un document PDF, appliquer le style des cellules, diviser le tableau sur les pages et personnaliser les lignes et colonnes, etc.
lastmod: "2024-05-16"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Ajouter un Tableau dans un Document PDF Existant

Pour ajouter un tableau à un fichier PDF existant avec Aspose.PDF pour PHP, suivez les étapes suivantes :

1. Charger le fichier source.
1. Initialiser un tableau
1. Définir la couleur de la bordure du tableau comme LightGray
1. Définir la bordure pour les cellules du tableau
1. Créer une boucle pour ajouter 10 lignes
1. Ajouter l'objet tableau à la première page du document d'entrée
1. Sauvegarder le fichier.

Les extraits de code suivants montrent comment ajouter du texte dans un fichier PDF existant.

```php

    // Ouvrir le document
    $document = new Document($inputFile);        
    // Initialise une nouvelle instance de Table
    $table = new Table();
    $colors= new Color();
    // Définir la couleur de la bordure du tableau comme LightGray
    $borderSide = new BorderSide();
    $borderInfo = new BorderInfo($borderSide->All, 0.5, $colors->getLightGray());
    $table->setBorder($borderInfo);
    // définir la bordure pour les cellules du tableau
    $table->setDefaultCellBorder($borderInfo);
    // créer une boucle pour ajouter 10 lignes
    for ($row_count = 1; $row_count < 10; $row_count++) {
        // ajouter une ligne au tableau
        $row = $table->getRows()->add();
        // ajouter des cellules au tableau
        $row->getCells()->add("Colonne (" . $row_count . ", 1)");
        $row->getCells()->add("Colonne (" . $row_count . ", 2)");
        $row->getCells()->add("Colonne (" . $row_count . ", 3)");
    }
    // Ajouter l'objet tableau à la première page du document d'entrée
    $document->getPages()->add()->getParagraphs()->add($table);

    // Sauvegarder le document PDF résultant.
    $document->save($outputFile);
    $document->close();
```