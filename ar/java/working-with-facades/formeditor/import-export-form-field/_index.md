---
title: استيراد وتصدير حقل النموذج
type: docs
weight: 60
url: /ar/java/import-export-form-field/
description: يتيح FormEditor استيراد وتصدير البيانات بتنسيق FDF و XFDF و XML.
lastmod: "2021-12-16"
---

يوفر Aspose.PDF لـ Java إمكانيات رائعة لإنشاء/معالجة حقول النماذج داخل مستند PDF. باستخدام هذه الواجهة البرمجية، يمكنك برمجيًا ملء حقول النماذج داخل ملف PDF عن طريق [تصدير البيانات من FDF إلى ملف PDF](/pdf/ar/java/export-data-into-a-pdf-file-facades/)، و[استيراد البيانات من XFDF إلى ملف PDF](/pdf/ar/java/import-data-into-a-pdf-file-facades/).

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


## تصدير البيانات من FDF إلى ملف PDF

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