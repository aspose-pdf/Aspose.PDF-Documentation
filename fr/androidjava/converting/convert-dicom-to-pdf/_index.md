---
title: Convertir DICOM en PDF
linktitle: Convertir DICOM en PDF
type: docs
weight: 250
url: /fr/androidjava/convert-dicom-to-pdf/
lastmod: "2026-07-01"
description: Convertir les images médicales enregistrées au format DICOM en fichier PDF en utilisant Aspose.PDF for Android via Java.
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

<abbr title="Digital Imaging and Communications in Medicine">DICOM</abbr> est une norme pour la gestion, le stockage, l'impression et la transmission d'informations en imagerie médicale. Elle comprend une définition de format de fichier et un protocole de communication réseau.

Aspsoe.PDF for Java vous permet de convertir des fichiers DICOM au format PDF, consultez le fragment de code suivant :

1. Charger l'image dans le flux
1. Initialiser [`Document object`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document)
1. Charger le fichier image DICOM d'exemple
1. Enregistrer le document PDF de sortie

```java
//    Convert DICOM to PDF
    public void convertDICOMtoPDF () {
        // Initialize document object
        document=new Document();

        Page page=document.getPages().add();
        Image image=new Image();

        File imgFileName=new File(fileStorage, "Conversion/bmode.dcm");

        try {
            inputStream=new FileInputStream(imgFileName);
        } catch (FileNotFoundException e) {
            resultMessage.setText(e.getMessage());
            return;
        }

        // Load sample BMP image file
        image.setImageStream(inputStream);
        image.setFileType(ImageFileType.Dicom);
        page.getParagraphs().add(image);

        File pdfFileName=new File(fileStorage, "DICOM-to-PDF.pdf");

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

