---
title: 创建一个复杂的PDF
linktitle: 创建一个复杂的PDF
type: docs
weight: 60
url: zh/php-java/complex-pdf-example/
description: Aspose.PDF for PHP via Java 允许您创建包含图像、文本片段和表格的更复杂的文档。
lastmod: "2024-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

[Hello, World](/pdf/php-java/hello-world-example/) 示例展示了使用 Aspose.PDF 创建 PDF 文档的简单步骤。在本文中，我们将了解如何使用 Aspose.PDF for PHP via Java 创建更复杂的文档。作为一个示例，我们将使用一家虚构的提供客运渡轮服务的公司的文档。

如果我们从头开始创建一个文档，我们需要遵循以下步骤：

1. 实例化一个 [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document) 对象。在这一步中，我们将创建一个带有一些元数据但没有页面的空PDF文档。

1. 向文档对象添加一个[页面](https://reference.aspose.com/pdf/java/com.aspose.pdf/page)。现在，我们的文档将有一页。

1. 添加一个[图像](https://reference.aspose.com/pdf/java/com.aspose.pdf/image)。这是一种基于PDF操作符的低级操作的复杂操作。
    - 从流中加载图像
    - 将图像添加到页面资源的图像集合中
    - 使用GSave操作符：此操作符保存当前图形状态。
    - 创建一个[矩阵](https://reference.aspose.com/pdf/java/com.aspose.pdf/matrix/)对象。
    - 使用ConcatenateMatrix操作符：定义图像的放置方式。
    - 使用Do操作符：此操作符绘制图像。
    - 使用GRestore操作符：此操作符恢复图形状态。

1. 为标题创建一个[文本片段](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextFragment)。对于标题，我们将使用Arial字体，字体大小为24pt，并居中对齐。

1. 为页面添加标题 [段落](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page#getParagraphs--).
1. 为描述创建一个 [TextFragment](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextFragment)。对于描述，我们将使用 Arial 字体，字体大小 24pt，居中对齐。
1. 将（描述）添加到页面段落。
1. 创建一个表格，添加表格属性。
1. 将（表格）添加到页面 [段落](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page#getParagraphs--).
1. 保存文档 "Complex.pdf".

```php

    $document = new Document();
    //添加页面
    $page = $document->getPages()->add();
    // -------------------------------------------------------------
    // 添加图像
    $imageFileName = $dataDir . DIRECTORY_SEPARATOR . 'logo.png';
    $page->AddImage($imageFileName, new Rectangle(20, 730, 120, 830));

    // -------------------------------------------------------------
    // 添加标题
    $fontRepository = new FontRepository();
    $fontArial = $fontRepository->findFont("Arial");

    $header = new TextFragment("New ferry routes in Fall 2020");
    $header->getTextState()->setFont($fontArial);
    $header->getTextState()->setFontSize(24);
    $header->setHorizontalAlignment(2);
    $header->setPosition(new Position(130, 720));
    $page->getParagraphs()->add($header);

    // 添加描述
    $descriptionText = "Visitors must buy tickets online and tickets are limited to 5,000 per day. Ferry service is operating at half capacity and on a reduced schedule. Expect lineups.";
    $description = new TextFragment($descriptionText);
    $description->getTextState()->setFont($fontRepository->findFont("Times New Roman"));
    $description->getTextState()->setFontSize(14);
    $header->setHorizontalAlignment(1);
    $page->getParagraphs()->add($description);

    // 添加表格
    $table = new Table();
    $table->setColumnWidths("200");

    $colors = new Color();
    $darkSlateGrayColor = $colors->getDarkSlateGray();
    $blackColor = $colors->getBlack();
    $grayColor = $colors->getGray();
    $whiteSmokeColor = $colors->getWhiteSmoke();

    $table->setBorder(new BorderInfo(BorderSide::$Box, 1.0, $darkSlateGrayColor));
    $table->setDefaultCellBorder(new BorderInfo(BorderSide::$Box, 0.5, $blackColor));
    $table->getMargin()->setBottom(10);
    $table->getDefaultCellTextState()->setFont($fontRepository->findFont("Helvetica"));

    $headerRow = $table->getRows()->add();

    $headerRowCell = $headerRow->getCells()->add("Departs City");
    $headerRowCell->setBackgroundColor($grayColor);
    $headerRowCell->getDefaultCellTextState()->setForegroundColor($whiteSmokeColor);

    $headerRowCell = $headerRow->getCells()->add("Departs Island");
    $headerRowCell->setBackgroundColor($grayColor);
    $headerRowCell->getDefaultCellTextState()->setForegroundColor($whiteSmokeColor);

    $timenow = new DateTime('06:00');

    for ($i = 0; $i < 10; $i++) {
        $dataRow = $table->getRows()->add();
        $cell = $dataRow->getCells()->add($timenow->format('H:i'));
        $timenow->add(new DateInterval('PT30M'));
        $dataRow->getCells()->add($timenow->format('H:i'));
    }

    $page->getParagraphs()->add($table);

    $document->save($outputFile);
```