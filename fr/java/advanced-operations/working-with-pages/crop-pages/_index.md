---
title: Rogner les pages PDF par programmation
linktitle: Rogner les pages
type: docs
weight: 80
url: /fr/java/crop-pages/
description: Vous pouvez obtenir les propriétés de la page, telles que la largeur, la hauteur, la boîte de fond perdu, de rognage et de découpe à l'aide de Aspose.PDF pour Java.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Obtenir les propriétés de la page

Chaque page dans un fichier PDF possède un certain nombre de propriétés, telles que la largeur, la hauteur, la boîte de fond perdu, de rognage et de découpe. Aspose.PDF pour Java vous permet d'accéder à ces propriétés.

- **Boîte des médias** : La boîte des médias est la plus grande boîte de page. Elle correspond à la taille de la page (par exemple A4, A5, Lettre US, etc.) sélectionnée lorsque le document a été imprimé en PostScript ou PDF. En d'autres termes, la boîte des médias détermine la taille physique du support sur lequel le document PDF est affiché ou imprimé.
- **Boîte de fond perdu** : Si le document a une fond perdu, le PDF aura également une boîte de fond perdu.
 Bleed est la quantité de couleur (ou d'œuvre) qui s'étend au-delà du bord d'une page. Il est utilisé pour s'assurer que lorsque le document est imprimé et coupé à la taille ("rogné"), l'encre ira jusqu'au bord de la page. Même si la page est mal rognée - coupée légèrement à côté des marques de rognage - aucun bord blanc n'apparaîtra sur la page.
- **Trim box**: La boîte de rognage indique la taille finale d'un document après impression et rognage.
- **Art box**: La boîte d'art est la boîte dessinée autour du contenu réel des pages de vos documents. Cette boîte de page est utilisée lors de l'importation de documents PDF dans d'autres applications.
- **Crop box**: La boîte de recadrage est la taille de "page" à laquelle votre document PDF est affiché dans Adobe Acrobat. En vue normale, seuls les contenus de la boîte de recadrage sont affichés dans Adobe Acrobat. Pour des descriptions détaillées de ces propriétés, lisez la spécification Adobe.Pdf, en particulier 10.10.1 Page Boundaries.
- **Page.Rect**: l'intersection (rectangle communément visible) du MediaBox et du DropBox. La figure ci-dessous illustre ces propriétés.  
Pour plus de détails, veuillez visiter [cette page](http://www.enfocus.com/manuals/ReferenceGuide/PP/10/enUS/en-us/concept/c_aa1095731.html).

L'extrait ci-dessous montre comment recadrer la page :

```java
package com.aspose.pdf.examples;

import com.aspose.pdf.*;

public class ExampleCropPages {

    private static String _dataDir = "/home/admin1/pdf-examples/Samples/";

    // Ouvrir le document
    Document pdfDocument = new Document(_dataDir + "sample.pdf");

    public static void CropPagesPDF() {
        Document pdfDocument = new Document("crop_page.pdf");
        Page page = pdfDocument.getPages().get_Item(1);

        System.out.println(page.getCropBox());
        System.out.println(page.getTrimBox());
        System.out.println(page.getArtBox());
        System.out.println(page.getBleedBox());
        System.out.println(page.getMediaBox());

        // Créer un nouveau rectangle Box
        Rectangle newBox = new Rectangle(200, 220, 2170, 1520);

        page.setCropBox(newBox);
        page.setTrimBox(newBox);
        page.setArtBox(newBox);
        page.setBleedBox(newBox);

        // Enregistrer le document de sortie
        pdfDocument.save(_dataDir + "crop_page_modified.pdf");
    }
}
```

In this example we used a sample file [here](crop_page.pdf). Initialement, notre page ressemble à celle montrée sur la Figure 1.
![Figure 1. Page rognée](crop_page.png)

Après la modification, la page ressemblera à la Figure 2.
![Figure 2. Page rognée](crop_page2.png)