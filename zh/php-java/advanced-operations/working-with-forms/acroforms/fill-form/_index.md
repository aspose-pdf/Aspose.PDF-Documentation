---
title: 填写AcroForms
linktitle: 填写AcroForms
type: docs
weight: 20
url: /zh/php-java/fill-form/
description: 本节介绍如何使用Aspose.PDF for PHP通过Java在PDF文档中填写表单字段。
lastmod: "2024-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

PDF文档是极好的，而且确实是创建表单的首选文件类型。

Aspose.PDF for PHP通过Java允许您填写表单字段，从Document对象的Form集合中获取该字段。

让我们看看以下示例如何解决这个任务：

```php

    // 打开文档
    $document = new Document($inputFile);
    $page = $document->getPages()->get_Item(1);
    
    // 获取一个字段    
    $textBoxField = $document->getForm()->get("textbox1");

    // 修改字段值
    $textBoxField->setValue("要填写在字段中的值");
        
    // 保存更新后的文档
    $document->save($outputFile);
    $document->close();
```