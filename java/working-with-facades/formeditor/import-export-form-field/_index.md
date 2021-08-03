---
title: Import and Export Form Field
type: docs
weight: 60
url: /java/import-export-form-field/
description: Fill Form fields using DataTable using FormEditor Class.
lastmod: "2021-06-05"
draft: false
---

Aspose.PDF for Java provides great capabilities for create/manipulating form fields inside PDF document. Using this API, you can programmatically fill form fields inside PDF fil by [Export Data from FDF into a PDF File ](/pdf/java/export-data-into-a-pdf-file-facades/), and  [Import Data from XFDF into a PDF File](/pdf/java/import-data-into-a-pdf-file-facades/). 

```java
public static void ImportData() {
        com.aspose.pdf.facades.Form editor = new com.aspose.pdf.facades.Form();
        editor.bindPdf(_dataDir + "Sample-Form-01.pdf");
        try {
            //editor.importFdf(new FileInputStream(_dataDir + "Sample-Form-01-upd.fdf"));
            editor.importXml(new FileInputStream(_dataDir + "Sample-Form-01-upd.xml"));
            //editor.importXfdf(new FileInputStream(_dataDir + "Sample-Form-01-upd.xfdf"));
        } catch (FileNotFoundException e) {
            e.printStackTrace();
        }
        editor.save(_dataDir + "Sample-Form-01-updated.pdf");
    }
```

## Export Data from FDF into a PDF File 

```java
     public static void ExportData() {
        com.aspose.pdf.facades.Form editor = new com.aspose.pdf.facades.Form();
        editor.bindPdf(_dataDir + "Sample-Form-01.pdf");
        try {
            editor.exportFdf(new FileOutputStream(_dataDir + "Sample-Form-01-mod.fdf"));
            editor.exportXml(new FileOutputStream(_dataDir + "Sample-Form-01-mod.xml"));
            editor.exportXfdf(new FileOutputStream(_dataDir + "Sample-Form-01-mod.xfdf"));
        } catch (FileNotFoundException e) {
            e.printStackTrace();
        }
    }
```


