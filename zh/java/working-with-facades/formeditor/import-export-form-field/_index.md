---
title: 导入和导出表单字段
type: docs
weight: 60
url: zh/java/import-export-form-field/
description: FormEditor允许以FDF、XFDF和XML格式导入和导出数据。
lastmod: "2021-12-16"
---

Aspose.PDF for Java 提供了在 PDF 文档中创建/操作表单字段的强大功能。使用此 API，您可以通过[将数据从 FDF 导出到 PDF 文件](/pdf/java/export-data-into-a-pdf-file-facades/)和[从 XFDF 导入数据到 PDF 文件](/pdf/java/import-data-into-a-pdf-file-facades/)以编程方式填充 PDF 文件中的表单字段。

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


## 从 FDF 导出数据到 PDF 文件

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