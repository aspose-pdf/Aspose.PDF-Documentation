---
title: 复制内外字段
type: docs
weight: 40
url: /java/copy-inner-and-outer-field/
description: 本节介绍如何使用 FormEditor 类通过 com.aspose.pdf.facades 复制内外字段。
lastmod: "2021-06-05"
draft: false
---

[copyInnerField](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/FormEditor#copyInnerField-java.lang.String-java.lang.String-int-) 方法允许您在同一文件中、指定页面的相同坐标处复制字段。此方法需要您要复制的字段名称、新字段名称以及字段需要复制到的页码。[FormEditor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/FormEditor) 类提供了此方法。以下代码片段向您展示如何在同一文件的相同位置复制字段。

```java
    public static void CopyInnerField() {
        FormEditor editor = new FormEditor();
        Document document = new Document(_dataDir + "Sample-Form-01.pdf");
        document.getPages().add();
        editor.bindPdf(document);
        editor.copyInnerField("Last Name", "Last Name 2", 2);
        editor.save(_dataDir + "Sample-Form-01-mod.pdf");
    }
```


## 复制现有 PDF 文件中的外部字段

[copyOuterField](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/FormEditor#copyOuterField-java.lang.String-java.lang.String-) 方法允许您从外部 PDF 文件中复制表单字段，然后将其添加到输入 PDF 文件的相同位置和指定页面号。此方法需要提供需要复制字段的 PDF 文件、字段名称以及需要复制字段的页面号。此方法由 [FormEditor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/FormEditor) 类提供。以下代码片段演示了如何从外部 PDF 文件中复制字段。

```java
  public static void CopyOuterField() {
        FormEditor editor = new FormEditor();
        Document document = new Document();
        document.getPages().add();
        editor.bindPdf(document);
        editor.copyOuterField(_dataDir + "Sample-Form-01.pdf", "First Name", 1);
        editor.copyOuterField(_dataDir + "Sample-Form-01.pdf", "Last Name", 1);
        editor.save(_dataDir + "Sample-Form-02-mod.pdf");
    }
```