---
title: Convertir TIFF en PDF 
linktitle: Convertir TIFF en PDF 
type: docs 
weight: 210 
url: /androidjava/convert-tiff-to-pdf/ 
lastmod: "2021-06-05" 
description: Aspose.PDF pour Android via Java permet de convertir des images TIFF multi-pages ou multi-trames en applications PDF. 
sitemap: 
    changefreq: "weekly" 
    priority: 0.7 
---

**Aspose.PDF pour Android via Java** prend en charge le format de fichier, qu'il s'agisse d'une image <abbr title="Tag Image File Format">TIFF</abbr> à une seule trame ou multi-trame. Cela signifie que vous pouvez convertir l'image TIFF en PDF dans vos applications Java.

TIFF ou TIF, Tagged Image File Format, représente des images raster destinées à être utilisées sur une variété d'appareils conformes à cette norme de format de fichier.
 TIFF image peut contenir plusieurs cadres avec différentes images. Le format de fichier Aspose.PDF est également pris en charge, qu'il s'agisse d'une image TIFF à une seule image ou à plusieurs images. Vous pouvez donc convertir l'image TIFF en PDF dans vos applications Java. Par conséquent, nous examinerons un exemple de conversion d'une image TIFF multipage en document PDF multipage avec les étapes suivantes :

1. Instancier une instance de la classe Document
1. Charger l'image TIFF d'entrée
1. Obtenez FrameDimension des cadres
1. Ajouter une nouvelle page pour chaque cadre
1. Enfin, enregistrer les images sur les pages PDF

De plus, l'extrait de code suivant montre comment convertir une image TIFF multipage ou multi-image en PDF :

```java
 public void convertTIFFtoPDF () {
        // Initialiser l'objet document
        document=new Document();

        Page page=document.getPages().add();
        Image image=new Image();

        File imgFileName=new File(fileStorage, "Conversion/sample.tiff");

        try {
            inputStream=new FileInputStream(imgFileName);
        } catch (FileNotFoundException e) {
            resultMessage.setText(e.getMessage());
            return;
        }

        // Charger le fichier image TIFF d'exemple
        image.setImageStream(inputStream);
        page.getParagraphs().add(image);

        File pdfFileName=new File(fileStorage, "TIFF-to-PDF.pdf");

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