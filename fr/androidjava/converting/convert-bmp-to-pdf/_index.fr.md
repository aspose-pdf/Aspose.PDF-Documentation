---
title: Convertir BMP en PDF 
linktitle: Convertir BMP en PDF
type: docs
weight: 220
url: /androidjava/convert-bmp-to-pdf/
lastmod: "2021-06-05"
description: Vous pouvez facilement convertir des fichiers bitmap BMP en PDF utilisés pour stocker des images bitmap numériques séparément de l'appareil d'affichage à l'aide d'Aspose.PDF pour Android via Java.
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

Les images BMP sont des fichiers ayant l'extension .BMP représentant des fichiers d'image bitmap utilisés pour stocker des images numériques bitmap. Ces images sont indépendantes de l'adaptateur graphique et sont également appelées format de fichier bitmap indépendant de l'appareil (DIB).
Vous pouvez convertir BMP en PDF avec l'API Aspose.PDF pour Java. Par conséquent, vous pouvez suivre les étapes suivantes pour convertir des images BMP :

1. Initialiser un nouveau Document
1. Charger le fichier d'image BMP d'exemple
1. Enfin, enregistrer le fichier PDF de sortie

Ainsi, l'extrait de code suivant suit ces étapes et montre comment convertir BMP en PDF en utilisant Java :

```java
public void convertBMPtoPDF () {
        // Initialiser l'objet document
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

        // Charger le fichier d'image BMP d'exemple
        image.setImageStream(inputStream);
        page.getParagraphs().add(image);

        File pdfFileName=new File(fileStorage, "BMP-to-PDF.pdf");

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