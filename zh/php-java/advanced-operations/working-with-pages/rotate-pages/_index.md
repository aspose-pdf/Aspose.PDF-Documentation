---
title: 以编程方式旋转PDF页面
linktitle: 旋转PDF页面
type: docs
weight: 60
url: /zh/php-java/rotate-pages/
description: 使用Java更改页面方向并使页面内容适应新页面方向。
lastmod: "2024-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## 更改页面方向

本文介绍如何更新或更改现有PDF文件中页面的方向。

Aspose.PDF for PHP via Java具有将页面方向从横向更改为纵向，反之亦然的功能。

1. 使用指定的输入文件打开文档。
1. 获取文档的所有页面。
1. 遍历每个页面并将旋转设置为90度。
1. 将修改后的文档保存到指定的输出文件。
1. 关闭文档。

```php

    // 打开文档
    $document = new Document($inputFile);                
    $pages = $document->getPages();
    $pagesSize = java_values($pages->size());
       
    // 遍历所有页面
    for ($pageCount = 1; $pageCount <= $pagesSize; $pageCount++) {
        $page = $pages->get_Item($pageCount);
       
        $page->setRotate((new Rotation())->On90);
    }

    // 保存输出文档
    $document->save($outputFile);
    $document->close();
```