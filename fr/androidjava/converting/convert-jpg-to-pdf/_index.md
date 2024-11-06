---
title: Convertir JPG en PDF 
linktitle: Convertir JPG en PDF 
type: docs
weight: 190
url: fr/androidjava/convert-jpg-to-pdf/
lastmod: "2021-06-05"
description: Découvrez comment convertir facilement des images JPG en fichier PDF. Vous pouvez également convertir une image en PDF avec la même hauteur et largeur que la page.
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

Pas besoin de se demander comment convertir un JPG en PDF, car la bibliothèque Apose.PDF pour Android via Java a la meilleure solution.

Vous pouvez très facilement convertir des images JPG en PDF avec Aspose.PDF pour Android via Java en suivant ces étapes :

1. Initialiser un objet de la classe [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document)
1. Charger l'image JPG et l'ajouter au paragraphe
1. Enregistrer le PDF de sortie

L'extrait de code ci-dessous montre comment convertir une image JPG en PDF :

```java
public void convertJPEGtoPDF () {
        // Initialiser l'objet document
        document=new Document();

        Page page=document.getPages().add();
        Image image=new Image();

        File imgFileName=new File(fileStorage, "Conversion/sample.jpg");

        try {
            inputStream=new FileInputStream(imgFileName);
        } catch (FileNotFoundException e) {
            resultMessage.setText(e.getMessage());
            return;
        }

        // Charger le fichier image JPEG échantillon
        image.setImageStream(inputStream);
        page.getParagraphs().add(image);

        File pdfFileName=new File(fileStorage, "JPEG-to-PDF.pdf");

        // Enregistrer le document de sortie
        try {
            document.save(pdfFileName.toString());
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }
        resultMessage.setText(R.string.success_message);
    }
```