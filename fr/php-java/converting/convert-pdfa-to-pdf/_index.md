---
title: Convertir le format PDF/A en PDF 
linktitle: Convertir le format PDF/A en PDF
type: docs
weight: 110
url: fr/php-java/convert-pdfa-to-pdf/
lastmod: "2024-05-20"
description: Ce sujet vous montre comment Aspose.PDF permet de convertir un fichier PDF/A en document PDF avec la bibliothèque PHP.
sitemap:
    changefreq: "monthly"
    priority: 0.8
---

## Convertir un document PDF/A en PDF

Convertir un document PDF/A en PDF signifie supprimer la restriction <abbr title="Portable Document Format Archive">PDF/A</abbr> du document original. La classe [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) possède la méthode removePdfaCompliance(..) pour supprimer l'information de conformité PDF du fichier source/saisi.

```php
// Créer une nouvelle instance de la classe Document avec le fichier d'entrée
$document = new Document($inputFile);

// Supprimer la conformité PDF/A du document
$document->removePdfaCompliance();

// Enregistrer le document modifié dans le fichier de sortie
$document->save($outputFile);
```

Cette information est également supprimée si vous apportez des modifications au document (par exemple.
 add pages). Dans l'exemple suivant, le document de sortie perd la conformité PDF/A après l'ajout de la page.

```php
// Créez une nouvelle instance de la classe Document avec le fichier d'entrée
$document = new Document($inputFile);

// Supprimez la conformité PDF/A du document
$document->getPages()->add();

// Enregistrez le document modifié dans le fichier de sortie
$document->save($outputFile);
```