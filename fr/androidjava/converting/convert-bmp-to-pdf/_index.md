---
title: Convertir BMP en PDF
linktitle: Convertir BMP en PDF
type: docs
weight: 220
url: /fr/androidjava/convert-bmp-to-pdf/
lastmod: "2026-07-01"
description: Vous pouvez facilement convertir des fichiers BMP bitmap en PDF, qui sont utilisés pour stocker des images bitmap numériques séparément du dispositif d’affichage, à l’aide d’Aspose.PDF. pour Android via Java.
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

Les images BMP sont des fichiers portant l’extension .BMP représentant des fichiers d’image bitmap qui sont utilisés pour stocker des images numériques bitmap. Ces images sont indépendantes de l’adaptateur graphique et sont également appelées format de fichier bitmap indépendant du dispositif (DIB).
Vous pouvez convertir BMP en PDF avec l’API Aspose.PDF pour Java. Par conséquent, vous pouvez suivre les étapes suivantes pour convertir les images BMP :

1. Initialisez un nouveau Document
1. Chargez le fichier d’image BMP d’exemple
1. Enfin, enregistrez le fichier PDF de sortie

Ainsi, le fragment de code suivant suit ces étapes et montre comment convertir un BMP en PDF en utilisant Java :

```java
public void convertBMPtoPDF () {
        // Initialize document object
        document=new Document();

        Page page=document.getPages().add();
        Image image=new Image();

        File imgFileName=new File(fileStorage, "Conversion/sample.bmp");

        try {
            inputStream=new FileInputStream(imgFileName);
        } catch (FileNotFoundException e) {
            resultMessage.setText(e.getMessage());
            return;
        }

        // Load sample BMP image file
        image.setImageStream(inputStream);
        page.getParagraphs().add(image);

        File pdfFileName=new File(fileStorage, "BMP-to-PDF.pdf");

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

