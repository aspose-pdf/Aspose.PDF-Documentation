---
title: Convertir TIFF en PDF
linktitle: Convertir TIFF en PDF
type: docs
weight: 210
url: /fr/androidjava/convert-tiff-to-pdf/
lastmod: "2026-07-01"
description: Aspose.PDF for Android via Java permet de convertir des images TIFF multi-pages ou multi-trames en applications PDF.
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

**Aspose.PDF for Android via Java** format de fichier pris en charge, qu'il s'agisse d'une trame unique ou multi-trame <abbr title="Tag Image File Format">TIFF</abbr> image. Cela signifie que vous pouvez convertir l'image TIFF en PDF dans vos applications Java.

TIFF ou TIF, Tagged Image File Format, représente des images matricielles destinées à être utilisées sur une variété d'appareils compatibles avec cette norme de format de fichier. Une image TIFF peut contenir plusieurs trames avec différentes images. Le format de fichier Aspose.PDF est également pris en charge, qu'il s'agisse d'une trame unique ou d'une image TIFF multi‑trames. Vous pouvez donc convertir l'image TIFF en PDF dans vos applications Java. Par conséquent, nous examinerons un exemple de conversion d'une image TIFF multi‑pages en document PDF multi‑pages avec les étapes ci‑dessous :

1. Instancier une instance de la classe Document
1. Charger l'image TIFF d'entrée
1. Obtenez FrameDimension des cadres
1. Ajoutez une nouvelle page pour chaque cadre
1. Enfin, enregistrez les images dans les pages PDF

De plus, le fragment de code suivant montre comment convertir une image TIFF multipage ou multiframe en PDF :

```java
 public void convertTIFFtoPDF () {
        // Initialize document object
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

        // Load sample TIFF image file
        image.setImageStream(inputStream);
        page.getParagraphs().add(image);

        File pdfFileName=new File(fileStorage, "TIFF-to-PDF.pdf");

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

