---
title: Extraire les polices d'un PDF 
linktitle: Extraire les polices
type: docs
weight: 30
url: /java/extract-fonts-from-pdf/
description: Comment extraire les polices d'un PDF en utilisant Aspose.PDF pour Java
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

Si vous souhaitez obtenir toutes les polices d'un document PDF, vous pouvez utiliser la méthode `Document.IDocumentFontUtilities.getAllFonts()` fournie dans la classe Document.
Veuillez consulter l'extrait de code suivant pour obtenir toutes les polices d'un document PDF existant :

```java
public static void Extract_Fonts() throws FileNotFoundException
{
    // Le chemin vers le répertoire des documents.
    String filePath = "<... entrer le nom du fichier ...>";
    
    // Charger le document PDF
    com.aspose.pdf.Document pdfDocument = new com.aspose.pdf.Document(filePath);
    com.aspose.pdf.Font[] fonts = pdfDocument.getFontUtilities().getAllFonts();

    for (com.aspose.pdf.Font font : fonts)
    {
        font.save(new FileOutputStream(font.getFontName()));
    }
}
```