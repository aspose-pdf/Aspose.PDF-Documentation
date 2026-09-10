---
title: Ajouter des numéros de page au PDF en Java
linktitle: Ajout d'un numéro de page
type: docs
weight: 30
url: /java/add-page-number/
description: Découvrez comment ajouter des tampons de numéro de page aux documents PDF en Java.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Ajouter des tampons de numéro de page aux fichiers PDF avec Java
Abstract: Cet article explique comment ajouter des tampons de numéro de page à l'aide d'Aspose.PDF pour Java. Il couvre la numérotation des pages standard avec un style de police personnalisé et la numérotation des chiffres romains avec un numéro de départ configurable.
---
## Ajouter un tampon de numéro de page


1. 
Ouvrez le PDF source [Document] (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

1. 
Créez l'objet [PageNumberStamp] (https://reference.aspose.com/pdf/java/com.aspose.pdf/pagenumberstamp/).

1. 
Configurez les options de placement et de numérotation du tampon requises.

1. 
Définissez les options de formatage de texte requises, notamment [FontRepository] (https://reference.aspose.com/pdf/java/com.aspose.pdf/fontrepository/) et [Color] (https://reference.aspose.com/pdf/java/com.aspose.pdf/color/).
1. Ajoutez le [PageNumberStamp] (https://reference.aspose.com/pdf/java/com.aspose.pdf/pagenumberstamp/) configuré à la [Page] (https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) cible.

1. 
Enregistrez le [Document] PDF mis à jour (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

```java
public static void addPageNumStamp(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        PageNumberStamp pageNumberStamp = new PageNumberStamp();
        pageNumberStamp.setBackground(false);
        pageNumberStamp.setFormat("Page # of " + document.getPages().size());
        pageNumberStamp.setBottomMargin(10);
        pageNumberStamp.setHorizontalAlignment(HorizontalAlignment.Center);
        pageNumberStamp.setStartingNumber(1);
        pageNumberStamp.getTextState().setFont(FontRepository.findFont("Arial"));
        pageNumberStamp.getTextState().setFontSize(14.0f);
        pageNumberStamp.getTextState().setFontStyle(FontStyles.Bold | FontStyles.Italic);
        pageNumberStamp.getTextState().setForegroundColor(Color.getBlueViolet());

        document.getPages().get_Item(1).addStamp(pageNumberStamp);
        document.save(outputFile.toString());
    }
}
```
