---
title: 从PDF中提取表格数据 
linktitle: 提取表格数据
type: docs
weight: 40
url: /php-java/extract-data-from-table-in-pdf/
description: 学习如何使用Aspose.PDF for PHP从PDF中提取表格
lastmod: "2021-05-20"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## 程序化地从PDF中提取表格

从PDF中提取表格并不是一项简单的任务，因为表格可以以各种方式创建。

Aspose.PDF for PHP通过Java提供了一种工具，可以轻松检索表格。要提取表格数据，您应该执行以下步骤：

1. 打开PDF文档 - 实例化一个[Document](https://reference.aspose.com/pdf/php-java/com.aspose.pdf/Document)对象；
1. 创建一个TableAbsorber [TableAbsorber](https://reference.aspose.com/pdf/php-java/com.aspose.pdf/tableabsorber)对象以从文档中提取表格。
1. 遍历文档的每一页。

1. 决定要分析哪些页面，并将[visit](https://reference.aspose.com/pdf/php-java/com.aspose.pdf/TableAbsorber#visit-com.aspose.pdf.Page-)应用于所需的页面。表格数据将被扫描，结果将保存在[AbsorbedTable](https://reference.aspose.com/pdf/php-java/com.aspose.pdf/AbsorbedTable)列表中。我们可以通过[getTableList](https://reference.aspose.com/pdf/php-java/com.aspose.pdf/TableAbsorber#getTableList--)方法获取此列表。
1. 要获取数据，遍历`TableList`并处理[absorbed rows](https://reference.aspose.com/pdf/php-java/com.aspose.pdf/AbsorbedRow)列表和吸收的单元格列表。我们可以通过调用[getTableList](https://reference.aspose.com/pdf/php-java/com.aspose.pdf/TableAbsorber#getTableList--)方法访问第一个列表，通过调用[getCellList](https://reference.aspose.com/pdf/php-java/com.aspose.pdf/AbsorbedRow#getCellList--)方法访问第二个列表。

1. 每个 [AbsorbedCell](https://reference.aspose.com/pdf/php-java/com.aspose.pdf/AbsorbedCell) 包含 [TextFragmentCollections](https://reference.aspose.com/pdf/php-java/com.aspose.pdf/TextFragmentCollection)。您可以根据自己的需要处理它。

以下示例显示了从所有页面提取表格：

```php

$document = new Document($inputFile);
$tableAbsorber = new TableAbsorber();


for ($pageIndex = 1; $pageIndex <= java_values($pages->size()); $pageIndex++) {
    $page = $pages->get_Item($pageIndex);
    $tableAbsorber->visit($page);
    $tableList = $tableAbsorber->getTableList();
    $tableIterator = $tableList->iterator();

    while (java_values($tableIterator->hasNext())) {
        $table = $tableIterator->next();
        $tableRowList = $table->getRowList();
        $tableRowListIterator = $tableRowList->iterator();

        while (java_values($tableRowListIterator->hasNext())) {
            $row = $tableRowListIterator->next();
            $cellList = $row->getCellList();
            $cellListIterator = $cellList->iterator();

            // 迭代行中的每个单元格。
            while (java_values($cellListIterator->hasNext())) {
                $cell = $cellListIterator->next();
                $fragmentList = $cell->getTextFragments();

                // 迭代单元格中的每个文本片段。
                for ($fragmentIndex = 1; $fragmentIndex <= java_values($fragmentList->size()); $fragmentIndex++) {
                    $fragment = $fragmentList->get_Item($fragmentIndex);
                    $segments = $fragment->getSegments();

                    // 迭代文本片段中的每个段。
                    for ($segmentIndex = 1; $segmentIndex <= java_values($segments->size()); $segmentIndex++) {
                        $segment = $segments->get_Item($segmentIndex);
                        $responseData .= $segment->getText();
                    }
                }
                $responseData .= "|";
            }
            $responseData .= PHP_EOL;
        }
    }
}

// 将表格数据保存到输出文件。
file_put_contents($outputFile, $responseData);

// 关闭 PDF 文档。
$document->close();
```


## 从PDF中提取表格数据并存储到CSV文件

以下示例展示了如何提取表格并将其存储为CSV文件。 要了解如何将PDF转换为Excel电子表格，请参阅[将PDF转换为Excel](/pdf/php-java/convert-pdf-to-excel/)文章。

```php

    // 使用Document类加载输入PDF文档。
    $document = new Document($inputFile);

    // 创建ExcelSaveOptions类的实例以指定保存选项。
    $saveOption = new ExcelSaveOptions();

    // 将输出格式设置为CSV。
    $saveOption->setFormat(ExcelSaveOptions_ExcelFormat::$CSV);

    // 使用指定的保存选项将PDF文档保存为Excel文件。
    $document->save($outputFile, $saveOption);
```