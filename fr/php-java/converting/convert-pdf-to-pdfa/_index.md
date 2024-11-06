---
title: Convertir PDF en formats PDF/A 
linktitle: Convertir PDF en formats PDF/A
type: docs
weight: 100
url: fr/php-java/convert-pdf-to-pdfa/
lastmod: "2024-05-20"
description: Ce sujet vous montre comment Aspose.PDF permet de convertir un fichier PDF en un fichier PDF conforme au PDF/A.
sitemap:
    changefreq: "monthly"
    priority: 0.8
---

**Aspose.PDF pour PHP** vous permet de convertir un fichier PDF en un fichier PDF conforme au PDF/A. Avant de le faire, le fichier doit être validé. Cet article explique comment.

Veuillez noter que nous suivons Adobe Preflight pour valider la conformité au PDF/A. Tous les outils sur le marché ont leur propre "représentation" de la conformité PDF/A. Veuillez consulter cet article sur les [outils de validation PDF/A](http://wiki.opf-labs.org/display/SPR/PDFA+Validation+tools+give+different+results) pour référence. Nous avons choisi les produits Adobe pour vérifier comment Aspose.PDF produit des fichiers PDF car Adobe est au centre de tout ce qui est lié au PDF.

Avant de convertir le PDF en un fichier conforme au PDF/A, validez le PDF en utilisant la méthode validate.
 Le résultat de la validation est stocké dans un fichier XML et ensuite ce résultat est également passé à la méthode de conversion. Vous pouvez également spécifier l'action pour les éléments qui ne peuvent pas être convertis en utilisant l'énumération [ConvertErrorAction](https://reference.aspose.com/pdf/java/com.aspose.pdf/converterroraction).

## Conversion PDF vers PDF/A

Le code suivant montre comment convertir des fichiers PDF en PDF conforme à PDF/A-1b.

```php
// Créez un nouvel objet Document et chargez le fichier PDF d'entrée.
$document = new Document($inputFile);

// Convertissez le document au format PDF/A-1a et spécifiez le fichier de log et l'action en cas d'erreur.
$res = $document->convert($logFile, PdfFormat::$PDF_A_1A, ConvertErrorAction::$Delete);

// Enregistrez le document converti dans le fichier de sortie.
$document->save($outputFile);
```

Pour effectuer uniquement la validation, utilisez la ligne de code suivante :

```php
// Créez un nouvel objet Document et chargez le fichier PDF d'entrée.
$document = new Document($inputFile);

// Convertissez le document au format PDF/A-1a et spécifiez le fichier de log et l'action en cas d'erreur.
$res = $document->convert($logFile, PdfFormat::$PDF_A_1A, ConvertErrorAction::$Delete);

// Valider le PDF pour PDF/A-1a
if ($document->validate("validation-result-A1A.xml", PdfFormat.PDF_A_1A))
{
    echo "Valide";
}
else
{
    echo "Non valide";
}
```

{{% alert color="primary" %}}
**Essayez de convertir un PDF en PDF/A en ligne**

Aspose.PDF pour PHP vous présente l'application en ligne gratuite ["PDF to PDF/A-1A"](https://products.aspose.app/pdf/conversion/pdf-to-pdfa1a), où vous pouvez essayer d'examiner la fonctionnalité et la qualité de son fonctionnement.

[![Aspose.PDF Conversion PDF en PDF/A avec application gratuite](pdf_to_pdfa.png)](https://products.aspose.app/pdf/conversion/pdf-to-pdfa1a)
{{% /alert %}}