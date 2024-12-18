---
title: 양식 필드 가져오기 및 내보내기
type: docs
weight: 60
url: /ko/java/import-export-form-field/
description: FormEditor는 FDF, XFDF 및 XML 형식으로 데이터를 가져오고 내보낼 수 있습니다.
lastmod: "2021-12-16"
---

Aspose.PDF for Java는 PDF 문서 내에서 양식 필드를 생성/조작할 수 있는 훌륭한 기능을 제공합니다. 이 API를 사용하여 [FDF에서 PDF 파일로 데이터 내보내기](/pdf/ko/java/export-data-into-a-pdf-file-facades/) 및 [XFDF에서 PDF 파일로 데이터 가져오기](/pdf/ko/java/import-data-into-a-pdf-file-facades/)를 통해 프로그래밍 방식으로 PDF 파일 내의 양식 필드를 채울 수 있습니다.

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


## FDF 데이터를 PDF 파일로 내보내기

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