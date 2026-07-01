---
title: Convertir PNG en PDF
linktitle: Convertir PNG en PDF
type: docs
weight: 200
url: /fr/androidjava/convert-png-to-pdf/
lastmod: "2026-07-01"
description: Cet article montre comment convertir PNG en PDF avec la bibliothèque Aspose.PDF dans vos applications Android via Java. Vous pouvez convertir des images PNG au format PDF en suivant des étapes simples.
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

**Aspose.PDF for Android via Java** prend en charge la fonctionnalité de conversion des images PNG au format PDF. Consultez le fragment de code suivant pour réaliser votre tâche.

<abbr title="Portable Network Graphics">PNG</abbr> fait référence à un type de format de fichier image raster qui utilise une compression sans perte, ce qui le rend populaire auprès de ses utilisateurs.

Vous pouvez convertir une image PNG en PDF en suivant les étapes ci-dessous :

1. Charger l'image PNG d'entrée
1. Lire les valeurs de hauteur et de largeur
1. Créer un nouveau document et ajouter une page
1. Définir les dimensions de la page
1. Enregistrer le fichier de sortie

De plus, l'extrait de code ci‑dessous montre comment convertir un PNG en PDF dans vos applications Java :

```java
    public void convertPNGtoPDF () {
        // Initialize document object
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

