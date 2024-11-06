---
title: Ajouter un Numéro de Page au PDF
linktitle: Ajouter un Numéro de Page
type: docs
weight: 100
url: fr/php-java/add-page-number/
description: Aspose.PDF pour PHP via Java vous permet d'ajouter un tampon de numéro de page à votre fichier PDF en utilisant la classe PageNumberStamp.
lastmod: "2024-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

Tous les documents doivent avoir des numéros de page. Le numéro de page facilite la localisation des différentes parties du document par le lecteur.
**Aspose.PDF pour PHP via Java** vous permet d'ajouter des numéros de page avec PageNumberStamp.

{{% alert color="primary" %}}

Essayez en ligne. Vous pouvez vérifier la qualité de la conversion Aspose.PDF et voir les résultats en ligne à ce lien [products.aspose.app/pdf/page-number](https://products.aspose.app/pdf/page-number)

{{% /alert %}}

Vous pouvez utiliser la classe [PageNumberStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf/PageNumberStamp) pour ajouter un tampon de numéro de page dans un document PDF.
 Le [PageNumberStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf/PageNumberStamp) classe fournit des méthodes pour créer un tampon basé sur un numéro de page, comme le format, les marges, les alignements, le numéro de départ, etc. Pour ajouter un tampon de numéro de page, vous devez créer un objet [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) et un objet [PageNumberStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf/PageNumberStamp) avec les propriétés de texte requises. Après cela, vous pouvez appeler la méthode [addStamp(..)](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page#addStamp-com.aspose.pdf.Stamp-) de la classe [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page) pour ajouter le tampon dans le fichier PDF. Vous pouvez également définir les attributs de police du tampon de numéro de page.

Le snippet de code suivant vous montre comment ajouter des numéros de page dans un fichier PDF.

```php

    // Ouvrir le document
    $document = new Document($inputFile);

    // Créer un tampon de numéro de page
    $pageNumberStamp = new PageNumberStamp();

    // Si le tampon est en arrière-plan
    $Center = (new HorizontalAlignment())->getCenter();
    $pageNumberStamp->setBackground(false);
    $pageNumberStamp->setFormat("Page # sur " . $document->getPages()->size());
    $pageNumberStamp->setBottomMargin(10);
    $pageNumberStamp->setHorizontalAlignment($Center);
    $pageNumberStamp->setStartingNumber(1);

    $fontRepository = new FontRepository();
    // Définir les propriétés du texte
    $pageNumberStamp->getTextState()->setFont($fontRepository->findFont("Arial"));
    $pageNumberStamp->getTextState()->setFontSize(14.0);
    $pageNumberStamp->getTextState()->setFontStyle(FontStyles::$Bold);
    $pageNumberStamp->getTextState()->setForegroundColor((new Color())->getAqua());

    // Ajouter le tampon à une page particulière
    $document->getPages()->get_Item(1)->addStamp($pageNumberStamp);

    // Enregistrer le document de sortie
    $document->save($outputFile);
    $document->close();
```