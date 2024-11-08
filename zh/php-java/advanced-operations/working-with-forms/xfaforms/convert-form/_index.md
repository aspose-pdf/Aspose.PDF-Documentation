---
title: 将XFA表单转换为AcroForm
linktitle: 转换XFA表单
type: docs
weight: 10
url: /zh/php-java/convert-form/
description: 本节解释如何使用Aspose.PDF for PHP via Java将XFA表单转换为AcroForm。
lastmod: "2024-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## 将动态XFA表单转换为标准AcroForm

动态表单基于一种称为XFA的XML规范，即“XML表单架构”。它还可以将动态XFA表单转换为标准Acroform。关于表单的信息（就PDF而言）非常模糊——它指定存在字段、属性和JavaScript事件，但不指定任何渲染。XFA表单的对象是在加载文档时绘制的。

目前，PDF支持两种不同的方法来集成数据和PDF表单：

- AcroForms（也称为Acrobat表单），在PDF 1.2格式规范中引入和包含。

- Adobe XML Forms Architecture (XFA) 表单，在 PDF 1.5 格式规范中作为可选功能引入。(XFA 规范未包含在 PDF 规范中，只是被引用。)

无法提取或操作 XFA 表单的页面，因为表单内容是在应用程序尝试显示或呈现 XFA 表单时在运行时生成的。Aspose.PDF 具有允许开发人员将 XFA 表单转换为标准 AcroForms 的功能。

```php

        // 加载 XFA 表单
        $document = new Document($inputFile);
        
        // 将表单字段类型设置为标准 AcroForm
        $formType = new FormType();
        $document->getForm()->setType($formType->getStandard());
            
        // 保存更新后的文档
        $document->save($outputFile);
        
        // 保存修改后的 PDF    
        $document->close();
```