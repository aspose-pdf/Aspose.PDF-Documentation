---
title: 程序化删除 PDF 页面 
linktitle: 删除 PDF 页面
type: docs
weight: 40
url: /php-java/delete-pages/
description: 您可以使用 PHP 从 PDF 文件中删除页面。
lastmod: "2024-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## 从 PDF 文件中删除页面

1. 调用删除方法并指定页面索引
1. 调用保存方法以保存更新后的 PDF 文件
以下代码片段展示了如何使用 PHP 从 PDF 文件中删除特定页面。

```php

    // 打开文档
    $document = new Document($inputFile);      

    $pages = $document->getPages();

    // 删除特定页面
    $pages->delete(2);

    // 保存输出文档
    $document->save($outputFile);
    $document->close();
```