---
title: Extraire des objets de graphique d'un document PDF (facades)
type: docs
weight: 20
url: /java/extract-chart-objects/
description: Cette section explique comment extraire des objets de graphique d'un PDF avec Aspose.PDF Facades en utilisant la classe PdfExtractor.
lastmod: "2021-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Extraire des objets de graphique d'un document PDF (facades)

Le PDF permet de regrouper le contenu des pages en éléments nommés **Contenu Marqué**. Adobe Acrobat les affiche comme "conteneurs". Les objets de graphique sont placés dans de tels objets. Nous avons introduit une nouvelle méthode extractMarkedContentAsImages() dans la classe PdfExtractor pour extraire ces objets. Cette méthode rend chaque **Contenu Marqué** en une image distincte. Veuillez noter que tous les graphiques ne sont pas entièrement placés dans un seul conteneur. À cause de cela, certains graphiques seront enregistrés en images séparées par parties.

Veuillez noter que le regroupement correct du contenu dans les conteneurs est la responsabilité d'un concepteur de document PDF.
 Si vous souhaitez obtenir des graphiques avec un en-tête ou d'autres objets, vous devez soit éditer/créer le document PDF où le graphique entier est placé dans un seul conteneur.

```java

//Ouvrir le document

Document document = new Document("sample.pdf");

//instancier PdfExtractor

PdfExtractor pdfExtractor = new PdfExtractor();

//Extraire les objets graphiques sous forme d'image dans un dossier

pdfExtractor.extractMarkedContentAsImages(document.getPages().get_Item(1), "C:/Temp/Charts_page_1");

document.close();
```