---
title: インポートとエクスポートフォームフィールド
type: docs
weight: 60
url: /java/import-export-form-field/
description: FormEditorはFDF、XFDF、XML形式でデータのインポートとエクスポートを可能にします。
lastmod: "2021-12-16"
---

Aspose.PDF for Javaは、PDFドキュメント内のフォームフィールドを作成/操作するための優れた機能を提供します。このAPIを使用すると、PDFファイル内のフォームフィールドをプログラムで[PDFファイルにFDFからデータをエクスポートする](/pdf/java/export-data-into-a-pdf-file-facades/)や[XFDFからPDFファイルにデータをインポートする](/pdf/java/import-data-into-a-pdf-file-facades/)ことができます。

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


## FDFからPDFファイルへのデータのエクスポート

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