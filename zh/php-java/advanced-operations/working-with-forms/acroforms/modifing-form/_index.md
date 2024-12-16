---
title: 修改AcroForms
linktitle: 修改AcroForms
type: docs
weight: 40
url: /zh/java/modifing-form/
description: 本节说明如何使用Aspose.PDF for PHP via Java修改PDF文档中的表单。
lastmod: "2024-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## 设置自定义表单字段字体

Adobe PDF文件中的表单字段可以配置为使用特定的默认字体。Aspose.PDF允许开发人员应用任何字体作为字段的默认字体，无论是14种核心字体之一还是自定义字体。
要设置和更新用于表单字段的默认字体，Aspose.PDF提供了DefaultAppearance (Font font, double size, Color color)类。可以通过com.aspose.pdf.DefaultAppearance访问该类。要使用此对象，请使用Field类的setDefaultAppearance(..)方法。

以下代码片段演示了如何为PDF表单字段设置默认字体。

```php

    // 打开文档
    $document = new Document($inputFile);

    // 从文档中获取特定表单字段
    $field = $document->getForm()->get("textbox1");

    // 创建字体对象
    $fontRepository = new FontRepository();
    $font = $fontRepository->findFont("ComicSansMS");

    $colors = new Color();
    $blackColor = $colors->getBlack();

    // 设置表单字段的字体信息
    $field->setDefaultAppearance(new DefaultAppearance($font, 10, $blackColor));

    // 保存更新后的文档
    $document->save($outputFile);
    $document->close();        

    $document->close();
```


## 获取/设置 FieldLimit

此代码演示了如何使用 [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) 类打开文档，检索表单字段，设置其最大长度，并使用 'setMaxLen' 和 'getMaxLen' 方法检索最大长度。

```php

    // 打开文档
    $document = new Document($inputFile);

    // 从文档中获取特定表单字段
    $field = $document->getForm()->get("textbox1");
    
    $field->setMaxLen(10);

    // 使用 DOM 获取字段的最大限制
    $responseData = "Limit: " . $field->getMaxLen();          

    $document->close();
```

您也可以使用以下代码片段，通过 Aspose.PDF.Facades 命名空间获取相同的值。

```php

    // 打开文档
    $document = new Document($inputFile);

    // 从文档中获取特定表单字段
    $field = $document->getForm()->get("textbox1");

    // 使用 DOM 获取字段的最大限制
    $responseData = "Limit: " . $field->getMaxLen();          

    $document->close();
```


同样，Aspose.PDF 具有一种使用 DOM 方法获取字段限制的方法。以下代码片段展示了这些步骤。

```php

    // 打开文档
    $document = new Document($inputFile);

    // 从文档中获取特定表单字段
    $field = $document->getForm()->get("textbox1");

    // 删除字段
    $field->delete();
    
    $document->close();
```
## 从 PDF 文档中删除特定表单字段

所有表单字段都包含在 [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) 对象的 Form 集合中。此集合提供了管理表单字段的不同方法，包括 delete 方法。如果要删除特定字段，请将字段名称作为参数传递给 delete 方法，然后保存更新后的 PDF 文档。

以下代码片段展示了如何从 PDF 文档中删除命名字段。

```php

    // 打开文档
    $document = new Document($inputFile);

    // 从文档中获取特定表单字段
    $field = $document->getForm()->get("textbox1");

    // 删除字段
    $field->delete();
    
    $document->close();
```


## 修改 PDF 文档中的表单字段

[Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) 对象的 Form 集合允许您管理 PDF 文档中的表单字段。

要修改表单字段，请从 Form 集合中获取字段并设置其属性。然后保存更新的 PDF 文档。

以下代码片段显示了如何修改 PDF 文档中的现有表单字段。

```php
    // 打开文档
    $document = new Document($inputFile);

    // 从文档中获取特定的表单字段
    $field = $document->getForm()->get("textbox1");

    // 修改字段值
    $field->setValue("Updated Value");

    // 将字段设置为只读
    $field->setReadOnly(true);

    // 保存更新后的文档
    $document->save($outputFile);        
    $document->close();
```

### 将表单字段移到 PDF 文件中的新位置

如果您想将表单字段移动到 PDF 页面上的新位置，首先获取字段对象，然后为其 setRect 方法指定一个新值。
 一个具有新坐标的[Rectangle](https://reference.aspose.com/pdf/java/com.aspose.pdf/Rectangle)对象被分配给setRect(..)方法。然后使用[Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document)对象的save方法保存更新后的PDF。

以下代码片段向您展示如何将表单字段移动到新位置。

```php

    // 打开一个文档
    $document = new Document($inputFile);

    // 从文档中获取特定的表单字段
    $field = $document->getForm()->get("textbox1");

    // 修改字段位置
    $field->setRect(new Rectangle(300, 400, 600, 500));

    // 保存更新后的文档
    $document->save($outputFile);        
    $document->close();
```