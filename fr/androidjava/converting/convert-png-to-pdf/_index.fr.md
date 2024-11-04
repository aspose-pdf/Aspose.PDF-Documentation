---
title: Convertir PNG en PDF 
linktitle: Convertir PNG en PDF
type: docs
weight: 200
url: /androidjava/convert-png-to-pdf/
lastmod: "2021-06-05"
description: Cet article montre comment convertir PNG en PDF avec la bibliothèque Aspose.PDF dans vos applications Android via Java. Vous pouvez convertir des images PNG en format PDF en utilisant des étapes simples.
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

**Aspose.PDF pour Android via Java** prend en charge la fonctionnalité de conversion d'images PNG en format PDF. Consultez l'extrait de code suivant pour réaliser votre tâche.

<abbr title="Portable Network Graphics">PNG</abbr> fait référence à un type de format de fichier d'image raster qui utilise une compression sans perte, ce qui le rend populaire parmi ses utilisateurs.

Vous pouvez convertir PNG en PDF en utilisant les étapes ci-dessous :

1. Charger l'image PNG d'entrée
1. Lire les valeurs de hauteur et de largeur
1. Créer un nouveau document et ajouter une page
1. Définir les dimensions de la page
1. Enregistrer le fichier de sortie

De plus, l'extrait de code ci-dessous montre comment convertir PNG en PDF dans vos applications Java :

```java
    public void convertPNGtoPDF () {
        // Initialiser l'objet document
        document=new Document();

        Page page=document.getPages().add();
        Image image=new Image();

        File imgFileName=new File(fileStorage, "Conversion/sample.png");

        try {
            inputStream=new FileInputStream(imgFileName);
        } catch (FileNotFoundException e) {
            resultMessage.setText(e.getMessage());
            return;
        }
```