---
title: Convertir JPG en PDF
linktitle: Convertir JPG en PDF
type: docs
weight: 190
url: /fr/androidjava/convert-jpg-to-pdf/
lastmod: "2026-07-01"
description: Apprenez comment convertir facilement des images JPG en fichier PDF. Vous pouvez également convertir une image en PDF avec la même hauteur et la même largeur que la page.
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

Pas besoin de se demander comment convertir JPG en PDF, car la bibliothèque Apose.PDF pour Android via Java offre la meilleure solution.

Vous pouvez très facilement convertir des images JPG en PDF avec Aspose.PDF pour Android via Java en suivant les étapes :

1. Initialiser l'objet de [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) classe
1. Charger l'image JPG et l'ajouter au paragraphe
1. Enregistrer le PDF de sortie

L'extrait de code ci-dessous montre comment convertir une image JPG en PDF :

```java
public void convertJPEGtoPDF () {
        // Initialize document object
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

        // Load sample JPEG image file
        image.setImageStream(inputStream);
        page.getParagraphs().add(image);

        File pdfFileName=new File(fileStorage, "JPEG-to-PDF.pdf");

        // Save output document
        try {
            document.save(pdfFileName.toString());
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }
        resultMessage.setText(R.string.success_message);
    }
```
