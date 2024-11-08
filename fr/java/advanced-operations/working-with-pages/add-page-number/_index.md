---
title: Ajouter un Numéro de Page au PDF
linktitle: Ajouter un Numéro de Page
type: docs
weight: 100
url: /fr/java/add-page-number/
description: Aspose.PDF pour Java vous permet d'ajouter un tampon de numéro de page à votre fichier PDF en utilisant la classe PageNumberStamp.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

Tous les documents doivent avoir des numéros de page. Le numéro de page facilite la localisation des différentes parties du document pour le lecteur.
**Aspose.PDF pour Java** vous permet d'ajouter des numéros de page avec PageNumberStamp.

{{% alert color="primary" %}}

Essayez en ligne. Vous pouvez vérifier la qualité de la conversion Aspose.PDF et voir les résultats en ligne à ce lien [products.aspose.app/pdf/page-number](https://products.aspose.app/pdf/page-number)

{{% /alert %}}

Vous pouvez utiliser la classe [PageNumberStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf/PageNumberStamp) pour ajouter un tampon de numéro de page dans un document PDF.
 Le [PageNumberStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf/PageNumberStamp) classe fournit des méthodes pour créer un tampon de type numéro de page, comme le format, les marges, les alignements, le numéro de départ, etc. Afin d'ajouter un tampon de numéro de page, vous devez créer un objet [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) et un objet [PageNumberStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf/PageNumberStamp) avec les propriétés requises. Après cela, vous pouvez appeler la méthode [addStamp(..)](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page#addStamp-com.aspose.pdf.Stamp-) de la classe [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page) pour ajouter le tampon dans le fichier PDF. Vous pouvez également définir les attributs de police du tampon de numéro de page.

Le code suivant vous montre comment ajouter des numéros de page dans un fichier PDF.

```java
package com.aspose.pdf.examples;

import com.aspose.pdf.Color;
import com.aspose.pdf.Document;
import com.aspose.pdf.FontRepository;
import com.aspose.pdf.FontStyles;
import com.aspose.pdf.HorizontalAlignment;
import com.aspose.pdf.PageNumberStamp;

public class ExampleAddPageNumberToPDF {

    private static String _dataDir = "/home/admin1/pdf-examples/Samples/";

    public static void ExampleAddPageNumber() {

        // Ouvrir le document
        Document pdfDocument = new Document(_dataDir + "PageNumberStamp.pdf");

        // Créer un tampon de numéro de page
        PageNumberStamp pageNumberStamp = new PageNumberStamp();

        // Si le tampon est en arrière-plan
        pageNumberStamp.setBackground(false);
        pageNumberStamp.setFormat("Page # de " + pdfDocument.getPages().size());
        pageNumberStamp.setBottomMargin (10);
        pageNumberStamp.setHorizontalAlignment ( HorizontalAlignment.Center);
        pageNumberStamp.setStartingNumber(1);
        // Définir les propriétés du texte
        pageNumberStamp.getTextState().setFont (FontRepository.findFont("Arial"));
        pageNumberStamp.getTextState().setFontSize (14.0F);
        pageNumberStamp.getTextState().setFontStyle (FontStyles.Bold);        
        pageNumberStamp.getTextState().setForegroundColor (Color.getAqua());

        // Ajouter le tampon à une page particulière
        pdfDocument.getPages().get_Item(1).addStamp(pageNumberStamp);

        _dataDir = _dataDir + "PageNumberStamp_out.pdf";
        // Enregistrer le document de sortie
        pdfDocument.save(_dataDir);

    }
}
```