---
title: 在 PDF 中创建或添加表格
linktitle: 创建或添加表格
type: docs
weight: 10
url: /php-java/add-table-in-existing-pdf-document/
description: 学习如何在 PDF 文档中创建或添加表格，应用单元格样式，跨页分割表格，以及自定义行和列等。
lastmod: "2024-05-16"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## 在现有 PDF 文档中添加表格

要使用 Aspose.PDF for PHP 向现有 PDF 文件添加表格，请执行以下步骤：

1. 加载源文件。
1. 初始化一个表格
1. 将表格边框颜色设置为 LightGray
1. 设置表格单元格的边框
1. 创建一个循环以添加 10 行
1. 将表格对象添加到输入文档的第一页
1. 保存文件。

以下代码片段显示了如何在现有 PDF 文件中添加文本。

```php

    // 打开文档
    $document = new Document($inputFile);        
    // 初始化 Table 的新实例
    $table = new Table();
    $colors= new Color();
    // 将表格边框颜色设置为 LightGray
    $borderSide = new BorderSide();
    $borderInfo = new BorderInfo($borderSide->All, 0.5, $colors->getLightGray());
    $table->setBorder($borderInfo);
    // 设置表格单元格的边框
    $table->setDefaultCellBorder($borderInfo);
    // 创建一个循环以添加 10 行
    for ($row_count = 1; $row_count < 10; $row_count++) {
        // 向表格添加行
        $row = $table->getRows()->add();
        // 添加表格单元格
        $row->getCells()->add("Column (" . $row_count . ", 1)");
        $row->getCells()->add("Column (" . $row_count . ", 2)");
        $row->getCells()->add("Column (" . $row_count . ", 3)");
    }
    // 将表格对象添加到输入文档的第一页
    $document->getPages()->add()->getParagraphs()->add($table);

    // 保存结果 PDF 文档。
    $document->save($outputFile);
    $document->close();
```