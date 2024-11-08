---
title: 操作 PDF 文档
linktitle: 操作 PDF 文档
type: docs
weight: 30
url: /zh/php-java/manipulate-pdf-document/
description: 本文包含有关如何验证 PDF A 标准的 PDF 文档、如何处理目录、如何设置 PDF 到期日期以及如何确定 PDF 文件生成进度的信息。
lastmod: "2024-06-05"
---

## 验证 PDF A 标准的 PDF 文档 (A 1A 和 A 1B)

要验证 PDF 文档是否符合 PDF/A-1a 或 PDF/A-1b 兼容性，请使用 [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) 类的 [validate(...)](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/#validate-java.lang.String-com.aspose.pdf.PdfFormat-) 方法。此方法允许您指定结果要保存的文件名和所需的验证类型 [PdfFormat](https://reference.aspose.com/pdf/java/com.aspose.pdf/PdfFormat) 枚举：PDF_A_1A 或 PDF_A_1B。

输出的 XML 格式是自定义的 Aspose 格式。
 XML 包含一组名为 Problem 的标签；每个标签包含特定问题的详细信息。Problem 标签的 ObjectID 属性表示此问题相关的特定对象的 ID。Clause 属性表示 PDF 规范中的相应规则。

```php

    // 打开文档
    $document = new Document($inputFile);
    
    $pdfFormat =  (new PdfFormat())->PDF_A_1A;
    // 验证PDF是否符合PDF/A-1a
    $document->validate($outputFile, $pdfFormat);
    $document->close();
```

## 处理目录

### 向现有 PDF 添加目录

要向现有 PDF 文件添加目录，请使用 com.aspose.pdf 包中的 [Heading](https://reference.aspose.com/pdf/java/com.aspose.pdf/Heading) 类。com.aspose.pdf 包可以创建新 PDF 文件并操作现有 PDF 文件。要向现有 PDF 添加目录，请使用 com.aspose.pdf 包。

此 PHP 代码片段使用 Aspose.PDF 向现有 PDF 文档添加目录：

```php
    // 打开文档
    $document = new Document($inputFile);

    // 获取 PDF 文件第一页的访问权限
    $tocPage = $document->getPages()->insert(1);

    // 创建对象以表示目录信息
    $tocInfo = new TocInfo();

    $title = new TextFragment("Table Of Contents");
    $title->getTextState()->setFontSize(20);
    $title->getTextState()->setFontStyle(FontStyles::$Bold);

    // 设置目录的标题
    $tocInfo->setTitle($title);
    $tocPage->setTocInfo($tocInfo);

    // 创建将用作目录元素的字符串对象
    $titles = ["First page", "Second page", "Third page", "Fourth page"];

    for ($i = 0; $i < 4; $i++) {
        // 创建 Heading 对象
        $heading2 = new Heading(1);

        $segment2 = new TextSegment();
        $heading2->setTocPage($tocPage);
        $heading2->getSegments()->add($segment2);

        // 指定标题对象的目标页面
        $page = $document->getPages()->get_Item($i + 2);
        $heading2->setDestinationPage($page);

        // 目标页面
        $heading2->setTop($page->getRect()->getHeight());

        // 目标坐标
        $segment2->setText($titles[$i]);

        // 将标题添加到包含目录的页面
        $tocPage->getParagraphs()->add($heading2);
    }
    // 保存更新的文档
    $document->save($outputFile);
    $document->close();
```

### 为不同的目录级别设置不同的 TabLeaderType

Aspose.PDF 还允许为不同的目录级别设置不同的 TabLeaderType。您需要将 FormatArray 的 LineDash 属性设置为 TabLeaderType 枚举的适当值，如下所示。

```php
    // 打开文档
    $document = new Document($inputFile);
    $tocPage = $document->getPages()->add();

    $tocInfo = new TocInfo();

    // 设置 LeaderType
    $tocInfo->setLineDash(TabLeaderType->Solid);

    $title = new TextFragment("目录");
    $title->getTextState()->setFontSize(30);
    $tocInfo->setTitle($title);

    // 将列表部分添加到 Pdf 文档的部分集合中
    $tocPage->setTocInfo($tocInfo);

    // 通过设置左边距和每一级的文本格式设置来定义四级列表的格式
    $fontStyles = new FontStyles();
    $tabLeaderTypes = new TabLeaderType();

    $tocInfo->setFormatArrayLength(4);
    $tocInfo->getFormatArray()[0]->getMargin()->setLeft(0);
    $tocInfo->getFormatArray()[0]->getMargin()->setRight(30);
    $tocInfo->getFormatArray()[0]->setLineDash($tabLeaderTypes->getDot());
    $tocInfo->getFormatArray()[0]->getTextState()->setFontStyle($fontStyles->getBold() | $fontStyles->getItalic());
    $tocInfo->getFormatArray()[1]->getMargin()->setLeft(10);
    $tocInfo->getFormatArray()[1]->getMargin()->setRight(30);
    $tocInfo->getFormatArray()[1]->setLineDash($tabLeaderTypes->getNone());
    $tocInfo->getFormatArray()[1]->getTextState()->setFontSize(10);
    $tocInfo->getFormatArray()[2]->getMargin()->setLeft(20);
    $tocInfo->getFormatArray()[2]->getMargin()->setRight(0);
    $tocInfo->getFormatArray()[2]->getTextState()->setFontStyle($fontStyles->getBold());
    $tocInfo->getFormatArray()[3]->setLineDash($tabLeaderTypes->getSolid());
    $tocInfo->getFormatArray()[3]->getMargin()->setLeft(30);
    $tocInfo->getFormatArray()[3]->getMargin()->setRight(30);
    $tocInfo->getFormatArray()[3]->getTextState()->setFontStyle($fontStyles->getBold());

    // 在 Pdf 文档中创建一个部分
    $page = $document->getPages()->add();

    // 在部分中添加四个标题
    for ($Level = 1; $Level <= 4; $Level++) {
      $heading2 = new Heading($Level);
      $segment2 = new TextSegment();

      $heading2->getSegments()->add($segment2);
      $heading2->setAutoSequence(true);
      $heading2->setTocPage($tocPage);

      $segment2->setText("示例标题" . $Level);
      $fontRepository = new FontRepository();
      $heading2->getTextState()->setFont($fontRepository->findFont("Arial UnicodeMS"));

      // 将标题添加到目录中。
      $heading2->setInList(true);
      $page->getParagraphs()->add($heading2);
    }

    // 保存更新后的文档
    $document->save($outputFile);
    $document->close();
```


### 隐藏目录中的页码

如果您不想在目录中显示页码和标题，可以将 [TOCInfo](https://reference.aspose.com/pdf/java/com.aspose.pdf/tocinfo) 类的 [ShowPageNumbers](https://reference.aspose.com/pdf/java/com.aspose.pdf/tocinfo/#setShowPageNumbers-boolean-) 属性设置为 false。请查看以下代码片段以隐藏目录中的页码：

```php
    // 打开文档
    $document = new Document();
    $tocPage = $document->getPages()->add();
    
    // 创建对象以表示目录信息
    $tocInfo = new TocInfo();

    $title = new TextFragment("Table Of Contents");
    $title->getTextState()->setFontSize(20);
    $title->getTextState()->setFontStyle(FontStyles::$Bold);

    // 设置目录的标题
    $tocInfo->setTitle($title);

    // 将列表部分添加到Pdf文档的部分集合中
    $tocPage->setTocInfo($tocInfo);

    // 通过设置左边距和每个级别的文本格式设置来定义四级列表的格式

    $tocInfo->setShowPageNumbers(false);
    $tocInfo->setFormatArrayLength(4);
    $tocInfo->getFormatArray()[0]->getMargin()->setRight(0);
    $tocInfo->getFormatArray()[0]->getTextState()->setFontStyle(FontStyles::$Bold | FontStyles::$Italic);

    $tocInfo->getFormatArray()[1]->getMargin()->setLeft(30);
    $tocInfo->getFormatArray()[1]->getTextState()->setUnderline(true);
    $tocInfo->getFormatArray()[1]->getTextState()->setFontSize(10);

    $tocInfo->getFormatArray()[2]->getTextState()->setFontStyle(FontStyles::$Bold);
    $tocInfo->getFormatArray()[3]->getTextState()->setFontStyle(FontStyles::$Bold);

    $page = $document->getPages()->add();

    // 在部分中添加四个标题
    for ($Level = 1; $Level < 5; $Level++) {
      $heading2 = new Heading($Level);
      $segment2 = new TextSegment();
      $heading2->setTocPage($tocPage);
      $heading2->getSegments()->add($segment2);
      $heading2->setAutoSequence(true);
      $segment2->setText("this is heading of level " + $Level);
      $heading2->setInList(true);
      $page->getParagraphs()->add($heading2);
    }
     
    // 保存更新后的文档
    $document->save($outputFile);
    $document->close();
```


### 自定义页码同时添加目录

在 PDF 文档中添加目录时，自定义目录中的页码是常见的。例如，我们可能需要在页码前添加一些前缀，如 P1、P2、P3 等。在这种情况下，Aspose.PDF for PHP via Java 提供了 TocInfo 类的 PageNumbersPrefix 属性，可以用来自定义页码，如以下代码示例所示。

```php

    // 打开文档
    $document = new Document($inputFile);

    // 获取 PDF 文件的第一页
    $tocPage = $document->getPages()->insert(1);

    // 创建对象以表示目录信息
    $tocInfo = new TocInfo();

    $title = new TextFragment("目录");
    $title->getTextState()->setFontSize(20);
    $title->getTextState()->setFontStyle(FontStyles::$Bold);

    // 设置目录标题
    $tocInfo->setTitle($title);
    $tocInfo->setPageNumbersPrefix("P");
    $tocPage->setTocInfo($tocInfo);

    // 创建将用作目录元素的字符串对象
    $titles = ["第一页", "第二页", "第三页", "第四页"];

    for ($i = 0; $i < 4; $i++) {
        // 创建 Heading 对象
        $heading2 = new Heading(1);

        $segment2 = new TextSegment();
        $heading2->setTocPage($tocPage);
        $heading2->getSegments()->add($segment2);

        // 指定 Heading 对象的目标页面
        $page = $document->getPages()->get_Item($i + 2);
        $heading2->setDestinationPage($page);

        // 目标页面
        $heading2->setTop($page->getRect()->getHeight());

        // 目标坐标
        $segment2->setText($titles[$i]);

        // 将 Heading 添加到包含目录的页面
        $tocPage->getParagraphs()->add($heading2);
    }
    // 保存更新的文档
    $document->save($outputFile);
    $document->close();
```


## 向 PDF 文件添加图层

图层可以在 PDF 文档中以多种方式使用。您可能有一个多语言文件需要分发，并希望每种语言的文本出现在不同的图层上，而背景设计出现在单独的图层上。您还可以创建在单独图层上显示动画的文档。一个例子可能是将许可协议添加到您的文件中，并且您不希望用户在同意协议条款之前查看内容。

Aspose.PDF for PHP via Java 支持向 PDF 文件添加图层。

要在 PDF 文件中使用图层，请使用以下 API 成员。

[Layer](https://reference.aspose.com/pdf/java/com.aspose.pdf/Layer) 类表示一个图层，并包含以下属性：

- **Name** – 图层的名称。
- **Id** – 图层的 ID。
- **Contents** – 图层操作符的列表。

一旦定义了 [Layer](https://reference.aspose.com/pdf/java/com.aspose.pdf/Layer) 对象，将它们添加到 [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page) 对象的 Layers 集合中。
 以下代码显示了如何向 PDF 文档添加图层。

```php
    // 打开文档
    $document = new Document($inputFile);
    $page = $document->getPages()->add();
    $arrayList = new java("java.util.ArrayList");
    $page->setLayers($arrayList);

    $layer = new $layer("oc1", "红线");
    $layer->getContents()->add(new operators_SetRGBColorStroke(1, 0, 0));
    $layer->getContents()->add(new operators_MoveTo(500, 700));
    $layer->getContents()->add(new operators_LineTo(400, 700));
    $layer->getContents()->add(new operators_Stroke());    
    $page->getLayers()->add($layer);

    $layer = new $layer("oc2", "绿线");
    $layer->getContents()->add(new operators_SetRGBColorStroke(0, 1, 0));
    $layer->getContents()->add(new operators_MoveTo(500, 750));
    $layer->getContents()->add(new operators_LineTo(400, 750));
    $layer->getContents()->add(new operators_Stroke());
    $page->getLayers()->add($layer);

    $layer = new $layer("oc3", "蓝线");
    $layer->getContents()->add(new operators_SetRGBColorStroke(0, 0, 1));
    $layer->getContents()->add(new operators_MoveTo(500, 800));
    $layer->getContents()->add(new operators_LineTo(400, 800));
    $layer->getContents()->add(new operators_Stroke());
    $page->getLayers()->add($layer);
    
    // 保存更新后的文档
    $document->save($outputFile);
    $document->close();
```

## 设置 PDF 过期

PDF 过期功能设置 PDF 文件的有效期。在特定日期，如果有人尝试访问它，会弹出一个窗口，说明文件已过期，需要一个新文件。

Aspose.PDF 允许您在创建和编辑 PDF 文件时设置过期。

下面的代码片段展示了如何为 PDF 文件设置过期日期。您需要使用 JavaScript，因为由第三方组件保存的文件（例如 OwnerGuard）在没有该实用程序的其他工作站上无法查看。

可以使用现有的具有过期日期的文件，通过 PDF OwnerGuard 创建 PDF 文件。但新文件只能在安装了 PDF OwnerGuard 的工作站上打开。没有 PDF OwnerGuard 的工作站将会给出 ExpirationFeatureError。例如，如果安装了 OwnerGuard，PDF Reader 可以打开文件，但 Adobe Acrobat 会返回错误。

```php

    // 打开文档
    $document = new Document($inputFile);
       
    $javaScript = new JavascriptAction(
      "var year=2020;" + 
      "var month=4;" + 
      "var today = new Date(); today = new Date(today.getFullYear(), today.getMonth());" +
      "var expiry = new Date(year, month);" +
      "if (today.getTime() > expiry.getTime())" + 
      "app.alert('该文件已过期。您需要一个新文件。');"
      );
    $document->setOpenAction($javaScript);
    $document->save($outputFile);
    $document->close();
```