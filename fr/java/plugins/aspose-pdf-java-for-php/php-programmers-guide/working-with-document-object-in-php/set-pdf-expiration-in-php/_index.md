---
title: Définir l'expiration PDF en PHP
type: docs
weight: 80
url: fr/java/set-pdf-expiration-in-php/
lastmod: "2021-06-05"
---

## Aspose.PDF - Définir l'expiration PDF

Pour définir l'expiration d'un document Pdf en utilisant **Aspose.PDF Java for PHP**, il suffit d'invoquer la classe **SetExpiration**.

Code PHP

```php

# Ouvrir un document pdf.
$doc = new Document($dataDir . "input1.pdf");

$javascript = new JavascriptAction(
        "var year=2014;
    var month=4;
    today = new Date();
    today = new Date(today.getFullYear(), today.getMonth());
    expiry = new Date(year, month);
    if (today.getTime() > expiry.getTime())
    app.alert('Le fichier est expiré. Vous avez besoin d'un nouveau.');");
$doc->setOpenAction($javascript);

# enregistrer le document mis à jour avec les nouvelles informations
$doc->save($dataDir . "set_expiration.pdf");

print "Mettre à jour les informations du document, veuillez vérifier le fichier de sortie." . PHP_EOL;

```

**Télécharger le Code Exécuté**

Téléchargez **Définir l'expiration PDF (Aspose.PDF)** à partir de n'importe lequel des sites de codage social mentionnés ci-dessous:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithDocumentObject/SetExpiration.php)