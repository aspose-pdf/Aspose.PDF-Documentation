---
title: 移动 PDF 页面
linktitle: 移动 PDF 页面
type: docs
weight: 20
url: zh/php-java/move-pages/
description: 尝试使用 Aspose.PDF for PHP via Java 将页面移动到所需位置或 PDF 文件的末尾。
lastmod: "2024-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## 将页面从一个 PDF 文档移动到另一个

本主题解释如何使用 PHP 将页面从一个 PDF 文档移动到另一个文档的末尾。
要移动页面，我们应该：

1. 使用源 PDF 文件创建一个 [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) 类对象
1. 使用目标 PDF 文件创建一个 [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) 类对象
1. 将页面添加到输出文档。保存输出文件
1. 从输入文档中删除页面。保存修改后的输入文档
1. 关闭文档
1. 保存并关闭输出文档

以下代码片段显示了如何移动一个页面。

```php

    // 打开文档
    $document = new Document($inputFile1);
    $dstDocument = new Document($outputFile);
    
    $page = $document->getPages()->get_Item(2);
    $dstDocument->getPages()->add($page);

    // 保存输出文件
    $dstDocument->save($srcFileName);
    $document->getPages()->delete(2);
    $document->save($dstFileName);
    $document->close();
    $dstDocument->close();
  
    // 保存输出文档
    $document->save($outputFile);
    $document->close();
```


## 将多个页面从一个 PDF 文档移动到另一个

1. 使用源 PDF 文件创建一个 [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) 类对象。
1. 使用目标 PDF 文件创建一个 [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) 类对象。
1. 定义要从输入文档复制到输出文档的页面。
1. 通过数组运行循环：
    1. 从输入文档中获取指定索引的页面。
    1. 将页面添加到目标文档。
1. 使用 Save 方法保存输出 PDF。
1. 使用数组在源文档中删除页面。
1. 使用 Save 方法保存源 PDF。

下面的代码片段显示了如何在 PDF 文件的末尾插入一个空页面。

```php

    // 打开文档
    $document = new Document($inputFile1);
    $dstDocument = new Document($outputFile);
    
    $pages = [1, 3 ];
    foreach ($pages as $pageIndex) {
      $page = $document->getPages()->get_Item($pageIndex);
      $dstDocument->getPages()->add(page);
    }
    // 保存输出文件
    $dstDocument->save($srcFileName);
    $document->getPages()->delete($pages);

    $document->save(dstFileName);

    $document->close();
    $dstDocument->close();  
```


## 在当前 PDF 文档中移动页面到新位置

1. 使用源 PDF 文件创建一个 [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) 类对象。
1. 从 [pageCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf/class-use/PageCollection) 集合中获取页面。
1. 将页面添加到新位置。
1. 删除索引为 2 的页面。
1. 使用保存方法保存输出 PDF。

```php

    // 打开文档
    $document = new Document($inputFile);
        
    $pageCollection = $document->getPages();
    
    $page = $pageCollection->get_Item(2);
    $pageCollection->add(page);
    $pageCollection->delete(2);

    // 保存输出文件
    $document->save($outputFile);
    $document->close();      
```