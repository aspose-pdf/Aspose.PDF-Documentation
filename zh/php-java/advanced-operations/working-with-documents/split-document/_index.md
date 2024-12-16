---
title: 程序化拆分PDF
linktitle: 拆分PDF文件
type: docs
weight: 60
url: /zh/php-java/split-document/
description: 本主题展示如何在您的PHP应用程序中将PDF页面拆分为单独的PDF文件。
lastmod: "2024-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

{{% alert color="primary" %}}

您可以使用Aspose.PDF拆分PDF文件，并在此链接上在线获取结果：[products.aspose.app/pdf/splitter](https://products.aspose.app/pdf/splitter)

{{% /alert %}}

本主题展示如何在PHP应用程序中通过Java使用Aspose.PDF将PDF页面拆分为单独的PDF文件。要使用PHP将PDF页面拆分为单页PDF文件，可以遵循以下步骤：

1. 通过[Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document)对象的[PageCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf.class-use/pagecollection)集合循环遍历PDF文档的页面。

1. 对于每次迭代，创建一个新的 Document 对象并将单个 [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page) 对象添加到空文档中。
1. 使用 Save 方法保存新的 PDF。

以下 PHP 代码片段展示了如何将 PDF 页面拆分为单独的 PDF 文件。

```php

    // 打开文档
    $document = new Document($inputFile);
    $pages = $document->getPages();
    $pagesSize = java_values($pages->size());
       
    // 遍历所有页面
    for ($pageCount = 1; $pageCount <= $pagesSize; $pageCount++) {
        $page = $pages->get_Item($pageCount);
        $newDocument = new Document();
        $newDocument->getPages()->add($page);
        $newDocument->save($outputFile . "page_" . $pageCount . ".pdf");
        $newDocument->close();
    }
    $document->close();
```