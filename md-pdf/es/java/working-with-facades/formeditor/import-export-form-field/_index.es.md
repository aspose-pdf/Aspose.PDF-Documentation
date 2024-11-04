---
title: Importar y Exportar Campo de Formulario
type: docs
weight: 60
url: /java/import-export-form-field/
description: FormEditor permite importar y exportar datos en formato FDF, XFDF y XML.
lastmod: "2021-12-16"
---

Aspose.PDF para Java proporciona grandes capacidades para crear/manipular campos de formulario dentro de un documento PDF. Usando esta API, puede completar programáticamente campos de formulario dentro de un archivo PDF mediante [Exportar Datos de FDF a un Archivo PDF](/pdf/java/export-data-into-a-pdf-file-facades/), y [Importar Datos de XFDF a un Archivo PDF](/pdf/java/import-data-into-a-pdf-file-facades/).

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


## Exportar Datos desde FDF a un Archivo PDF

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