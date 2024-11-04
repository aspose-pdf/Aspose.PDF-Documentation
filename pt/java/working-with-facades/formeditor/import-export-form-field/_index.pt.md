---
title: Importar e Exportar Campo de Formulário
type: docs
weight: 60
url: /java/import-export-form-field/
description: FormEditor permite importar e exportar dados nos formatos FDF, XFDF e XML.
lastmod: "2021-12-16"
---

Aspose.PDF para Java oferece ótimas capacidades para criar/manipular campos de formulário dentro de um documento PDF. Usando esta API, você pode preencher programaticamente campos de formulário dentro de arquivos PDF por [Exportar Dados de FDF para um Arquivo PDF](/pdf/java/export-data-into-a-pdf-file-facades/), e [Importar Dados de XFDF para um Arquivo PDF](/pdf/java/import-data-into-a-pdf-file-facades/).

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


## Exportar Dados de FDF para um Arquivo PDF

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