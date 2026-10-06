---
title: 在 Java 中删除 PDF 表单
linktitle: 删除表单
type: docs
weight: 70
url: /zh/java/remove-form/
description: 使用 Aspose.PDF for Java 删除 PDF 页面上的 Form 对象，包括完整清理和有针对性的删除。
lastmod: "2026-10-06"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 使用 Java 删除 PDF 页面上的 Form 资源
Abstract: 本文介绍了如何使用 Aspose.PDF for Java 从 PDF 文档中删除 Form 资源。它涵盖了清除页面上的所有 Form，以及在过滤页面 Form 集合后仅删除选定的 Typewriter Form 资源。
---
这些示例从页面中删除 Form 资源，而不是仅更改字段值。

## 从页面中移除所有表单资源

当要在一次操作中移除选定页面上的所有表单资源时，请使用此示例。

1. 打开源 PDF [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)。
1. 访问 [XFormCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf/xformcollection/) 针对目标页面。
1. 清空集合并保存更新后的文档。

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

当仅需删除选定的表单资源（例如打字机表单）时，请使用此示例。

1. 打开源 PDF [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)。
1. 访问 [XFormCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf/xformcollection/) 针对目标页面。
1. 过滤 [XForm](https://reference.aspose.com/pdf/java/com.aspose.pdf/xform/) 您想要移除的资源并将其从集合中删除。
1. 保存更新后的 PDF [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)。

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
