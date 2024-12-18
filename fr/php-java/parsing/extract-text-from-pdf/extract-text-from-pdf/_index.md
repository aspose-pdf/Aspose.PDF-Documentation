---
title: Extraction de texte brut à partir d'un fichier PDF 
linktitle: Extraire du texte d'un PDF
type: docs
weight: 10
url: /fr/php-java/extract-text-from-all-pdf/
description: Cet article décrit diverses façons d'extraire du texte de documents PDF en utilisant Aspose.PDF pour PHP. À partir de pages entières, d'une partie spécifique, basé sur des colonnes, etc.
lastmod: "2024-05-20"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Extraire le texte de toutes les pages d'un document PDF

L'extraction de texte d'un document PDF est une exigence courante. Dans cet exemple, vous verrez comment Aspose.PDF pour PHP permet d'extraire du texte de toutes les pages d'un document PDF.
Pour extraire du texte de toutes les pages PDF :

1. Créez un objet de la classe [TextAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextAbsorber).

1. Ouvrez le PDF en utilisant la classe [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) et appelez la méthode [Accept](https://reference.aspose.com/pdf/java/com.aspose.pdf/PageCollection#accept-com.aspose.pdf.TextAbsorber-) de la collection [Pages](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page).
1. La classe [TextAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextAbsorber) absorbe le texte du document et le renvoie dans la [méthode getText()](https://reference.aspose.com/pdf/java/com.aspose.pdf/textabsorber/#getText--).

Le code suivant vous montre comment extraire le texte de toutes les pages du document PDF.

```php

    // Créez un nouvel objet Document à partir du fichier PDF d'entrée.
    $document = new Document($inputFile);

    // Créez un nouvel objet TextAbsorber pour extraire le texte du document.
    $textAbsorber = new TextAbsorber();

    // Extraire le texte du document.
    $textAbsorber->visit($document);

    // Obtenez le contenu du texte extrait.
    $content = $textAbsorber->getText();

    // Enregistrez le texte extrait dans le fichier de sortie.
    file_put_contents($outputFile, $content);
```