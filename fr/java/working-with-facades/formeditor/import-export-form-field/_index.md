---
title: Importer et Exporter un Champ de Formulaire
type: docs
weight: 60
url: /fr/java/import-export-form-field/
description: FormEditor permet d'importer et d'exporter des données aux formats FDF, XFDF et XML.
lastmod: "2021-12-16"
---

Aspose.PDF pour Java offre de grandes capacités pour créer/manipuler des champs de formulaire à l'intérieur d'un document PDF. En utilisant cette API, vous pouvez remplir par programmation des champs de formulaire à l'intérieur d'un fichier PDF en [exportant des données de FDF dans un fichier PDF](/pdf/fr/java/export-data-into-a-pdf-file-facades/), et [en important des données de XFDF dans un fichier PDF](/pdf/fr/java/import-data-into-a-pdf-file-facades/).

```java
public static void ImportData() {
        com.aspose.pdf.facades.Form editor = new com.aspose.pdf.facades.Form();
        editor.bindPdf(_dataDir + "Sample-Form-01.pdf");
        try {
            editor.importFdf(new FileInputStream(_dataDir + "Sample-Form-01-upd.fdf"));
            //editor.importXml(new FileInputStream(_dataDir + "Sample-Form-01-upd.xml"));
            //editor.importXfdf(new FileInputStream(_dataDir + "Sample-Form-01-upd.xfdf"));
        } catch (FileNotFoundException e) {
            e.printStackTrace();
        }
        editor.save(_dataDir + "Sample-Form-01-updated.pdf");
    }
```


## Exporter des données de FDF dans un fichier PDF

```java
     public static void ExportData() {
        com.aspose.pdf.facades.Form editor = new com.aspose.pdf.facades.Form();
        editor.bindPdf(_dataDir + "Sample-Form-01.pdf");
        try {
            editor.exportFdf(new FileOutputStream(_dataDir + "Sample-Form-01-mod.fdf"));
            //editor.exportXml(new FileOutputStream(_dataDir + "Sample-Form-01-mod.xml"));
            //editor.exportXfdf(new FileOutputStream(_dataDir + "Sample-Form-01-mod.xfdf"));
        } catch (FileNotFoundException e) {
            e.printStackTrace();
        }
    }
```