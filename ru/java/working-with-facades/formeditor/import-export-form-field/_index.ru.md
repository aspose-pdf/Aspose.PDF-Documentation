---
title: Импорт и Экспорт Поля Формы
type: docs
weight: 60
url: /java/import-export-form-field/
description: FormEditor позволяет импортировать и экспортировать данные в формате FDF, XFDF и XML.
lastmod: "2021-12-16"
---

Aspose.PDF for Java предоставляет отличные возможности для создания/манипуляции полями формы внутри PDF документа. Используя этот API, вы можете программно заполнять поля формы внутри PDF файла, [Экспортировав данные из FDF в PDF файл](/pdf/java/export-data-into-a-pdf-file-facades/), и [Импортировав данные из XFDF в PDF файл](/pdf/java/import-data-into-a-pdf-file-facades/).

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


## Экспорт данных из FDF в PDF файл

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