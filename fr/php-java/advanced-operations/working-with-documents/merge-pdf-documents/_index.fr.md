---
title: Fusionner des PDF par programmation
linktitle: Fusionner des fichiers PDF
type: docs
weight: 50
url: /php-java/merge-pdf-documents/
description: Cette page explique comment fusionner des documents PDF en un seul fichier PDF en utilisant PHP.
lastmod: "2024-06-05"
---

Maintenant, la fusion de fichiers PDF est l'une des tâches les plus demandées.
Cet article montre comment fusionner plusieurs fichiers PDF en un seul document PDF en utilisant Aspose.PDF pour PHP via Java. L'exemple est écrit en Java, mais l'API peut être utilisée dans d'autres langages de programmation. Les fichiers PDF sont fusionnés de sorte que le premier soit joint à la fin de l'autre document.

## Fusionner des fichiers PDF en utilisant PHP

{{% alert color="primary" %}}

Vous pouvez fusionner des fichiers PDF en utilisant Aspose.PDF et obtenir les résultats en ligne à ce lien : [Fusionneur](https://products.aspose.app/pdf/merger)

{{% /alert %}}

Pour concaténer deux fichiers PDF :

1. Créez deux objets [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/class-use/Document), chacun contenant l'un des fichiers PDF d'entrée.

1. Ensuite, appelez la méthode Add de la collection [PageCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf/class-use/PageCollection) pour l'objet Document auquel vous souhaitez ajouter l'autre fichier PDF.
1. Passez la collection PageCollection du deuxième objet Document à la méthode Add de la première collection PageCollection.
1. Enfin, enregistrez le fichier PDF de sortie à l'aide de la méthode Save.

Le code suivant montre comment concaténer des fichiers PDF en utilisant PHP.

```php
    // Ouvrir le premier document
    $document1 = new Document($inputFile1);
    
    // Ouvrir le deuxième document
    $document2 = new Document($inputFile2);

    // Ajouter les pages du deuxième document au premier
    $document1->getPages()->add($document2->getPages());

    // Enregistrer le fichier de sortie concaténé
    $document1->save($outputFile);
    $document1->close();
    $document2->close();
```