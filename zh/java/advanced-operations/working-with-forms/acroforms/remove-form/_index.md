---
title: 用 Java 删除 PDF 中的表单
linktitle: 删除表格
type: docs
weight: 70
url: /java/remove-form/
description: 使用 Aspose.PDF for Java 从 PDF 页面中删除表单对象，包括完全清理和定向删除。
lastmod: "2026-06-09"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 使用 Java 从 PDF 页面中删除表单资源
Abstract: 本文介绍如何使用 Aspose.PDF for Java 从 PDF 文档中删除表单资源。它包括清除页面中的所有表单以及在过滤页面表单集合后仅删除选定的打字机表单资源。
---
这些示例从页面中删除表单资源，而不仅仅是更改字段值。

## 从页面中删除所有表单资源

当应在一次操作中删除选定页面上的每个表单资源时，请使用此示例。

1. 打开源 PDF [文档](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)。
1. 访问目标页面的 [XFormCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf/xformcollection/)。
1. 清除集合并保存更新的文档。

```java
public static void removeAllForms(Path inputFile, int pageNum, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        XFormCollection forms = document.getPages().get_Item(pageNum).getResources().getForms();
        forms.clear();
        document.save(outputFile.toString());
    }
}
```

## 删除特定的表单资源

当仅应删除选定的表单资源（例如打字机表单）时，请使用此示例。

1. 打开源 PDF [文档](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)。
1. 访问目标页面的 [XFormCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf/xformcollection/)。
1. 过滤要删除的 [XForm](https://reference.aspose.com/pdf/java/com.aspose.pdf/xform/) 资源并将其从集合中删除。
1. 保存更新的 PDF [文档](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)。

```java
public static void removeSpecifiedForm(Path inputFile, int pageNum, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        XFormCollection forms = document.getPages().get_Item(pageNum).getResources().getForms();
        List<String> formNames = new ArrayList<>();
        for (XForm form : forms) {
            if ("Typewriter".equals(form.getIT()) && "Form".equals(form.getSubtype())) {
                formNames.add(forms.getFormName(form));
            }
        }
        for (String formName : formNames) {
            forms.delete(formName);
        }
        document.save(outputFile.toString());
    }
}
```
