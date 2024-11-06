---
title: 提取数据AcroForms
linktitle: 提取数据AcroForms
type: docs
weight: 30
url: zh/php-java/extract-form/
description: 本节介绍如何使用Aspose.PDF for PHP通过Java从PDF文档中提取表单。
lastmod: "2024-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## 从PDF文档的单个字段获取值

表单字段的[getValue()方法](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextBoxField#getValue--)允许您获取特定字段的值。

要获取该值，请从[Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document)对象的Form集合中获取表单字段。

此示例选择一个[textBoxField](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextBoxField)并使用[getValue()方法](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextBoxField#getValue--)检索其值。

```php

    // 打开文档
    $document = new Document($inputFile);

    // 获取字段
    $textBoxField = $document->getForm()->get("textbox1");

    // 获取字段名称
    $responseData = "PartialName: " . $textBoxField->getPartialName();

    // 获取字段值
    $responseData = $responseData . " Value: " . $textBoxField->getValue();
    $document->close();
```