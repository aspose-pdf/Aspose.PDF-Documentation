---
title: Ajouter des tampons de texte au PDF en Java
linktitle: Tampons de texte dans un fichier PDF
type: docs
weight: 20
url: /java/text-stamps-in-the-pdf-file/
description: Découvrez comment ajouter des tampons de texte aux documents PDF en Java.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Ajouter des tampons de texte aux fichiers PDF avec Java
Abstract: Cet article explique comment ajouter des tampons de texte aux fichiers PDF à l'aide d'Aspose.PDF pour Java. Il couvre la création d'un tampon de texte d'arrière-plan, son positionnement, sa rotation et la personnalisation de la police, de la taille, du style et de la couleur.
---
Utilisez des tampons de texte lorsque vous devez ajouter des étiquettes ou des filigranes visibles aux pages PDF.


## 
Ajouter un tampon de texte



Utilisez cet exemple lorsqu'une page doit afficher un tampon de texte pivoté avec un style personnalisé.


1. 
Ouvrez le PDF source [Document] (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

1. 
Créez un [TextStamp] (https://reference.aspose.com/pdf/java/com.aspose.pdf/textstamp/) et configurez son emplacement et l'apparence du texte.
1. Ajoutez le tampon à la page cible et enregistrez le document.

```java
public static void addTextStamp(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        TextStamp textStamp = new TextStamp("Sample Stamp");
        textStamp.setBackground(true);
        textStamp.setXIndent(100);
        textStamp.setYIndent(100);
        textStamp.setRotate(Rotation.on90);
        textStamp.getTextState().setFont(FontRepository.findFont("Arial"));
        textStamp.getTextState().setFontSize(14.0f);
        textStamp.getTextState().setFontStyle(FontStyles.Bold | FontStyles.Italic);
        textStamp.getTextState().setForegroundColor(Color.getDarkGreen());
        document.getPages().get_Item(1).addStamp(textStamp);
        document.save(outputFile.toString());
    }
}
```
