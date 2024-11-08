---
title: Optimiser un document PDF pour le Web en PHP
type: docs
weight: 60
url: /fr/java/optimize-pdf-document-for-the-web-in-php/
lastmod: "2021-06-05"
---

## Aspose.PDF - Optimiser PDF pour le Web

Pour optimiser un document PDF pour le web en utilisant **Aspose.PDF Java pour PHP**, il suffit d'invoquer la méthode **optimize_web** de la classe **Optimize**.

Code PHP

```php

 public static function optimize_web($dataDir=null)

{

    # Ouvrir un document pdf.

    $doc = new Document($dataDir . "input1.pdf");

    # Optimiser pour le web

    $doc->optimize();

    #Enregistrer le document de sortie

    $doc->save($dataDir . "Optimized_Web.pdf");

    print "PDF optimisé pour le Web, veuillez vérifier le fichier de sortie." . PHP_EOL;

}    
```

**Télécharger le code en cours d'exécution**

Téléchargez **Optimize PDF for Web (Aspose.PDF)** à partir de l'un des sites de codage social mentionnés ci-dessous :

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithDocumentObject/Optimize.php)