---
title: 将图像添加到现有PDF文件
linktitle: 添加图像
type: docs
weight: 10
url: /php-java/add-image-to-existing-pdf-file/
description: 本节描述如何使用PHP将图像添加到现有PDF文件。
lastmod: "2024-06-05"
---

每个PDF页面包含资源和内容属性。资源可以是图像和表单，例如，内容则由一组PDF操作符表示。每个操作符都有其名称和参数。本例使用操作符将图像添加到PDF文件中。

要将图像添加到现有的PDF文件中：

- 创建一个[Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document)对象并打开输入PDF文档。
- 获取您想要添加图像的页面。
- 向文档中添加一个新页面。
- 将页面大小设置为1190.7 x 841.995。
- 使用指定的图像文件和页面的裁剪框将图像添加到页面。
- 保存文件。

以下代码片段显示了如何在PDF文档中添加图像。

```php

    // 使用指定的输入文件打开文档。
    $document = new Document($inputFile);
    
    // 向文档中添加一个新页面。
    $page = $document->getPages()->add();
    
    // 将页面大小设置为1190.7 x 841.995。
    $page->setPageSize(1190.7, 841.995);
    
    // 使用指定的图像文件和页面的裁剪框将图像添加到页面。
    $page->addImage($imageFileName, $page->getCropBox());
    
    // 将修改后的文档保存到指定的输出文件。
    $document->save($outputFile);
    
    // 关闭文档。
    $document->close();
```