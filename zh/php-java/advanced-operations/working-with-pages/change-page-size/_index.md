---
title: 使用编程方式更改 PDF 页面大小
linktitle: 更改 PDF 页面大小
type: docs
weight: 50
url: zh/php-java/change-page-size/
description: 使用 PHP 更改 PDF 文件的页面大小。
lastmod: "2024-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## 更改 PDF 页面大小

通过 Java 的 Aspose.PDF for PHP 允许您在 Java 应用程序中仅用简单的代码行更改 PDF 页面大小。本主题说明如何更新/更改现有 PDF 文件的页面尺寸（大小）。

[Page](https://reference.aspose.com/pdf//java/com.aspose.pdf/page) 类包含 SetPageSize(...) 方法，允许您设置页面大小。下面的代码片段通过几个简单的步骤更新页面尺寸：

1. 加载源 PDF 文件。
2. 将页面获取到 [pageCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf.class-use/pagecollection) 对象中。
3. 获取给定的页面。
4. 调用 setPageSize(..) 方法以更新其尺寸。

1. 调用 [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) 类的 save(..) 方法，以生成具有更新页面尺寸的 PDF 文件。

以下代码片段展示了如何将 PDF 页面尺寸更改为 A4 大小。

```php

    // 打开文档
    $document = new Document($inputFile);
      
    // 获取页面集合
    $pageCollection = $document->getPages();

    // 获取特定页面
    $page = $pageCollection->get_Item(1);

    // 将页面大小设置为 A4 (11.7 x 8.3 英寸)，在 Aspose.Pdf 中，1 英寸 = 72 点
    // 因此 A4 尺寸以点为单位为 (842.4, 597.6)
    $page.setPageSize(597.6, 842.4);

    // 保存输出文档
    $document->save($outputFile);
    $document->close();
```

## 获取 PDF 页面大小

您可以使用通过 Java 的 Aspose.PDF for PHP 读取现有 PDF 文件的页面大小。以下代码示例展示了如何使用 PHP 读取 PDF 页面的尺寸。

```php

    // 打开文档
    $document = new Document($inputFile);
      
    // 向 PDF 文档添加一个空白页
    $page = $document->getPages()->size() > 0 
        ? $document->getPages()->get_Item(1) 
        : $document->getPages()->add();
    
    // 获取页面高度和宽度信息
    $responseData = $page->getPageRect(true)->getWidth() . ":" . $page->getPageRect(true)->getHeight();
    
    // 将页面旋转 90 度
    $rotation = new Rotation();
    $page->setRotate($rotation->getOn90());

    // 获取页面高度和宽度信息
    $responseData = $responseData . $page->getPageRect(true)->getWidth() . ":" . $page->getPageRect(true)->getHeight();
    
    // 保存输出文档
    $document->save($outputFile);
    $document->close();
```