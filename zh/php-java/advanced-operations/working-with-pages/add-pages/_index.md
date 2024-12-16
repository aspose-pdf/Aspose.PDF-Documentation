---
title: 在 PDF 中添加页面
linktitle: 添加页面
type: docs
weight: 10
url: /zh/php-java/add-pages/
description: 本文教您如何在所需位置插入（添加）PDF 文件中的页面。了解如何使用 PHP 移动、删除（删除）PDF 文件中的页面。
lastmod: "2024-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## 在 PDF 文件中添加或插入页面

Aspose.PDF for PHP via Java 允许您在文件的任何位置插入页面到 PDF 文档中，也可以在 PDF 文件的末尾添加页面。您需要将要插入空白页面的位置传递给插入方法。
本节显示如何使用 Aspose.PDF for PHP via Java 向 PDF 添加页面。

### 在所需位置向 PDF 文件插入空白页面

以下代码片段显示了如何在 PDF 文件中插入空白页面：

1. 使用输入 PDF 文件创建一个 [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) 类对象。
1. 添加页面，并在 PDF 中插入它。

1. 使用 Save 方法保存输出 PDF。

以下代码片段展示了如何在 PDF 文件中插入页面。

```php

    // 打开文档
    $document = new Document($inputFile);

    // 添加页面
    $document->getPages()->add();

    // 在 PDF 中插入空白页面
    $document->getPages()->insert(2);

    // 保存输出文档
    $document->save($outputFile);
    $document->close();
```

在上面的例子中，我们添加了具有默认参数的空白页面。如果您需要使页面大小与文档中的另一个页面相同，您应该添加几行代码：

```php

    // 打开文档
    $document = new Document($inputFile);

    // 添加页面
    $page1 = $document->getPages()->add();

    // 在 PDF 中插入空白页面
    $page2 = $document->getPages()->insert(2);

    // 从页面 1 复制页面参数
    $page2->setCropBox($page1->getCropBox());
    $page2->setMediaBox($page1->getMediaBox());
    $page2->setTrimBox($page1->getTrimBox());
    $page2->setArtBox($page1->getArtBox());
    $page2->setBleedBox($page1->getBleedBox());
    
    // 保存输出文档
    $document->save($outputFile);
    $document->close();
```


### 在 PDF 文件末尾添加空白页

有时，您需要确保文档以空白页结束。此主题说明如何在 PDF 文档末尾插入空白页。

要在 PDF 文件末尾插入空白页：

1. 使用输入 PDF 文件创建一个 [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) 类对象。
2. 添加页面，并将其插入到 PDF 中。
3. 使用保存方法保存输出 PDF。

以下代码片段展示了如何在 PDF 文件的末尾插入一个空白页。

```php

    // 打开文档
    $document = new Document($inputFile);

    // 添加页面
    $document->getPages()->add();

    // 在 PDF 中插入一个空白页
    $document->getPages()->insert(2);

    // 保存输出文档
    $document->save($outputFile);
    $document->close();
```