---
title: Convertir DICOM en PDF
linktitle: Convertir DICOM en PDF
type: docs
weight: 250
url: fr/androidjava/convert-dicom-to-pdf/
lastmod: "2021-06-05"
description: Convertir des images médicales enregistrées au format DICOM en un fichier PDF à l'aide d'Aspose.PDF pour Android via Java.
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

<abbr title="Digital Imaging and Communications in Medicine">DICOM</abbr> est une norme pour la gestion, le stockage, l'impression et la transmission d'informations en imagerie médicale. Elle comprend une définition de format de fichier et un protocole de communication réseau.

Aspose.PDF pour Java vous permet de convertir des fichiers DICOM en format PDF, vérifiez le code suivant :

1. Charger l'image dans le flux
1. Initialiser l'[`objet Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document)
1. Charger un fichier d'image DICOM d'exemple
1. Enregistrer le document PDF de sortie

```java
//    Convertir DICOM en PDF
    public void convertDICOMtoPDF () {
        // Initialiser l'objet document
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

        // Charger le fichier d'image BMP d'exemple
        image.setImageStream(inputStream);
        image.setFileType(ImageFileType.Dicom);
        page.getParagraphs().add(image);

        File pdfFileName=new File(fileStorage, "DICOM-to-PDF.pdf");

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