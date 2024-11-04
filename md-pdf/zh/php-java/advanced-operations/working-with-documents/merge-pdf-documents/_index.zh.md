---
title: 通过编程合并PDF
linktitle: 合并PDF文件
type: docs
weight: 50
url: /php-java/merge-pdf-documents/
description: 本页面解释如何使用PHP将多个PDF文件合并为一个PDF文件。
lastmod: "2024-06-05"
---

现在，合并PDF文件是最受欢迎的任务之一。
本文展示了如何使用Aspose.PDF for PHP via Java将多个PDF文件合并为一个PDF文档。示例是用Java编写的，但该API可以用于其他编程语言。PDF文件的合并方式是将第一个文件连接到另一个文档的末尾。

## 使用PHP合并PDF文件

{{% alert color="primary" %}}

您可以使用Aspose.PDF在线合并PDF文件，并在此链接获取结果：[合并工具](https://products.aspose.app/pdf/merger)

{{% /alert %}}

要连接两个PDF文件：

1. 创建两个[Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/class-use/Document)对象，每个对象包含一个输入的PDF文件。

1. 然后调用 [PageCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf/class-use/PageCollection) 集合的 Add 方法，将其他 PDF 文件添加到您想要的 Document 对象中。
1. 将第二个 Document 对象的 PageCollection 集合传递给第一个 PageCollection 集合的 Add 方法。
1. 最后，使用 Save 方法保存输出 PDF 文件。

以下代码片段展示了如何使用 PHP 连接 PDF 文件。

```php
    // 打开第一个文档
    $document1 = new Document($inputFile1);
    
    // 打开第二个文档
    $document2 = new Document($inputFile2);

    // 将第二个文档的页面添加到第一个文档中
    $document1->getPages()->add($document2->getPages());

    // 保存连接后的输出文件
    $document1->save($outputFile);
    $document1->close();
    $document2->close();
```