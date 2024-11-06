---
title: 提取 XFA 表单
linktitle: 提取 XFA 表单
type: docs
weight: 30
url: zh/php-java/extract-form/
description: 本节说明如何使用 Aspose.PDF for PHP via Java 从 PDF 文档中提取表单。
lastmod: "2024-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## 从 PDF 文档的表单字段获取值

表单字段的 [getValue() 方法](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextBoxField#getValue--) 允许您获取特定字段的值。

要获取值，请从 [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) 对象的表单集合中获取表单字段。

此示例选择一个 [TextBoxField](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextBoxField) 并使用 [getValue() 方法](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextBoxField#getValue--) 检索其值。

```php

    // 加载 XFA 表单
    $document = new Document($inputFile);
    
    // 获取 XFA 表单字段的名称
    $names = $document->getForm()->getXFA()->getFieldNames();
        
    // 获取字段值
    $document->getForm()->getXFA()->get_Item($names[0]);
    $document->getForm()->getXFA()->get_Item($names[1]);
    
    // 保存修改后的 PDF    
    $document->close();
```