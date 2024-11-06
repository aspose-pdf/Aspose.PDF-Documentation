---
title: 填写 AcroForms
linktitle: 填写 AcroForms
type: docs
weight: 20
url: zh/php-java/fill-form/
description: 本节介绍如何使用 Aspose.PDF for PHP via Java 在 PDF 文档中填写表单字段。
lastmod: "2024-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

PDF 文档是创建表单的绝佳文件类型，实际上是首选的文件类型。

Aspose.PDF for PHP via Java 允许您填写表单字段，从文档对象的表单集合中获取字段。

让我们看看以下示例如何解决此任务：

```php

    // 加载 XFA 表单
    $document = new Document($inputFile);
    
    // 获取 XFA 表单字段的名称
    $names = $document->getForm()->getXFA()->getFieldNames();
        
    // 设置字段值        
    $document->getForm()->getXFA()->set_Item($names[0],"Field 0");
    $document->getForm()->getXFA()->set_Item($names[1],"Field 1");
        
    // 保存更新后的文档
    $document->save($outputFile);
    
    // 保存修改后的 PDF    
    $document->close();
```