---
title: 格式化 PDF 文档
linktitle: 格式化 PDF 文档
type: docs
weight: 20
url: zh/php-java/formatting-pdf-document/
description: 使用 Aspose.PDF for PHP via Java 格式化 PDF 文档。使用下一个代码片段来解决您的任务。
lastmod: "2024-06-05"
---

## 获取文档窗口和页面显示属性

本主题帮助您了解如何获取文档窗口的属性、查看器应用程序以及页面的显示方式。

要设置这些不同的属性，请使用 [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) 类打开 PDF 文件。您现在可以获得 [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) 对象的方法，例如：

- [isCenterWindow](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#isCenterWindow--) – 在屏幕上居中文档窗口。默认值：false。
- [setDirection](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#setDirection-int-) – 阅读顺序。
 这决定了页面在并排显示时的布局方式。默认：从左到右。

- [isDisplayDocTitle](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#isDisplayDocTitle--) – 在文档窗口标题栏中显示文档标题。默认：false（显示标题）。
- [isHideMenubar](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/#isHideMenubar--) – 获取标志，指定当文档处于活动状态时是否应隐藏菜单栏。
- [isHideToolBar](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/#isHideToolBar--) – 获取标志，指定当文档处于活动状态时是否应隐藏工具栏。
- [isHideWindowUI](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/#isHideWindowUI--) – 获取标志，指定当文档处于活动状态时是否应隐藏用户界面元素。

- [getNonFullScreenPageMode](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/#getNonFullScreenPageMode--) – 获取页面模式，指定在退出全屏模式时如何显示文档。- [getPageLayout](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/#getPageLayout--) – 页面布局。
- [getPageMode](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/#getPageMode--) – 获取页面模式，指定文档打开时的显示方式。

以下代码片段向您展示如何使用 [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) 类获取属性。

```php  

    // 打开文档
    $document = new Document($inputFile);

    // 获取不同的文档属性
    // 文档窗口的位置 - 默认值：false
    $responseData = "CenterWindow : " . $document->isCenterWindow();

    // 主要阅读顺序；确定页面的位置
    // 并排显示时 - 默认值：L2R
    $responseData = $responseData . "Direction : " . $document->getDirection();

    // 窗口的标题栏是否应显示文档标题。
    // 如果为 false，标题栏显示 PDF 文件名 - 默认值：false
    $responseData = $responseData . "DisplayDocTitle : " . $document->isDisplayDocTitle();

    // 是否调整文档窗口的大小以适应
    // 第一个显示页面的大小 - 默认值：false
    $responseData = $responseData . "FitWindow : " . $document->isFitWindow();

    // 是否隐藏查看器应用程序的菜单栏 - 默认值：false
    $responseData = $responseData . "HideMenuBar :" . $document->isHideMenubar();

    // 是否隐藏查看器应用程序的工具栏 - 默认值：false
    $responseData = $responseData . "HideToolBar :" . $document->isHideToolBar();

    // 是否隐藏 UI 元素如滚动条
    // 只显示页面内容 - 默认值：false
    $responseData = $responseData . "HideWindowUI :" . $document->isHideWindowUI();

    // 文档的页面模式。退出全屏模式时如何显示文档。
    $responseData = $responseData . "NonFullScreenPageMode :" . $document->getNonFullScreenPageMode();

    // 页面布局，即单页、一列
    $responseData = $responseData . "PageLayout :" . $document->getPageLayout();

    // 文档打开时的显示方式。
    $responseData = $responseData . "Page Mode :" . $document->getPageMode();
    $document->close();  
```


## 设置文档窗口和页面显示属性

本主题解释如何设置文档窗口、查看器应用程序和页面显示的属性。

要设置这些不同的属性：

1. 使用 [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) 类打开 PDF 文件。
1. 设置 Document 对象的属性。
1. 使用 Save 方法保存更新后的 PDF 文件。

可用的方法有：

- [setCenterWindow](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#setCenterWindow-boolean-)
- [setDirection](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#setDirection-int-)
- [setDisplayDocTitle](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#setDisplayDocTitle-boolean-)
- [setFitWindow](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#setFitWindow-boolean-)
- [setHideMenuBar](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#setHideMenubar-boolean-)

- [setHideToolBar](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#setHideToolBar-boolean-)
- [setHideWindowUI](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#setHideWindowUI-boolean-)
- [setNonFullScreenPageMode](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#setNonFullScreenPageMode-int-)
- [setPageLayout](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#setPageLayout-int-)
- [setPageMode](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#setPageMode-int-)

以下代码片段展示了如何使用 [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) 类设置属性。

```php

    // 打开文档
    $document = new Document($inputFile);
    // 设置不同的文档属性
    // 指定文档窗口的位置 - 默认: false
    $document->setCenterWindow(true);
    // 主要阅读顺序；确定页面的位置
    // 当并排显示时 - 默认: L2R
    $document->setDirection(Direction::$R2L);
    // 指定窗口的标题栏是否应显示文档标题
    // 如果为false，标题栏显示PDF文件名 - 默认: false
    $document->setDisplayDocTitle(true);
    // 指定是否调整文档窗口的大小以适应
    // 首次显示的页面大小 - 默认: false
    $document->setFitWindow(true);
    // 指定是否隐藏查看器应用程序的菜单栏 - 默认:
    // false
    $document->setHideMenubar(true);
    // 指定是否隐藏查看器应用程序的工具栏 - 默认:
    // false
    $document->setHideToolBar(true);
    // 指定是否隐藏UI元素如滚动条
    // 仅显示页面内容 - 默认: false
    $document->setHideWindowUI(true);
    // 文档的页面模式。指定如何显示文档在退出
    // 全屏模式时。
    $document->setNonFullScreenPageMode(PageMode::$UseOC);
    // 指定页面布局，即单页，一列
    $document->setPageLayout(PageLayout::$TwoColumnLeft);
    // 指定文档打开时应如何显示
    // 即显示缩略图，全屏，显示附件面板
    $document->setPageMode(PageMode::$UseThumbs);
    // 保存更新的PDF文件
    $document->save($outputFile);
    $document->close();

```


## 在现有 PDF 文件中嵌入字体

PDF 阅读器支持[14 种核心字体](http://en.wikipedia.org/wiki/Portable_Document_Format#Fonts)，以便文件可以在任何平台上以相同的方式显示。当 PDF 包含超出核心字体的字体时，嵌入字体以避免字体替换。

Aspose.PDF for PHP via Java 支持在现有 PDF 文档中嵌入字体。您可以嵌入完整字体或子集。要嵌入字体：

1. 使用 [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) 类打开现有的 PDF 文件。
1. 使用 [com.aspose.pdf.Font](https://reference.aspose.com/pdf/java/com.aspose.pdf/Font) 类嵌入字体。
   1. setEmbedded(true) 方法嵌入完整字体。
   1. [isSubset(true) 方法](https://reference.aspose.com/pdf/java/com.aspose.pdf/font/#isSubset--) 嵌入字体的子集。

字体子集仅嵌入使用到的字符，适用于字体用于短句或口号的情况，例如，公司字体用于标志而不是正文时。
 使用子集可以减少输出 PDF 的文件大小。

然而，如果正文文本使用自定义字体，则将其全部嵌入。

以下代码片段显示了如何在 PDF 文件中嵌入字体。

```php

    // 打开文档
    $document = new Document($inputFile);
    $pages = $document->getPages();
    for ($i = 1; $i <= $pages->size(); $i++) {
      $page = $pages->get_Item($i);
      $fonts = $page->getResources()->getFonts();
      if (!is_null($fonts)) {
        for ($fontIndex = 1; $fontIndex <= $fonts->size(); $fontIndex++) {
          $pageFont = $fonts->get_Item($fontIndex);
          // 检查字体是否已经嵌入
          if (!$pageFont->isEmbedded())
            $pageFont->setEmbedded(true);
        }
      }
      $forms = $page->getResources()->getForms();
      // 检查表单对象
      for ($formIndex = 0; $formIndex < -$forms->size(); $formIndex++) {
        $formFonts = $forms->get_Item($formIndex)->getResources()->getFonts();
        if (!is_null($formFonts)) {
          for ($fontIndex = 1; $fontIndex <= $formFonts->size(); $fontIndex++) {
            $pageFont = $formFonts->get_Item($fontIndex);
            // 检查字体是否已经嵌入
            if (!$pageFont->isEmbedded())
              $pageFont->setEmbedded(true);
          }
        }
      }
      $responseData = "Ok";
    }

    // 保存更新后的 PDF 文件
    $document->save($outputFile);
    $document->close();
```

## 创建PDF时嵌入字体

如果需要使用Adobe Reader支持的14种核心字体以外的任何字体，那么在生成PDF文件时必须嵌入字体描述。如果字体信息没有嵌入，Adobe Reader会从操作系统中获取它（如果系统中安装了该字体），或者根据PDF中的字体描述构造一个替代字体。请注意，嵌入的字体必须安装在主机上，即在以下代码中‘Univers Condensed’字体已安装在系统上。

我们使用[Font](https://reference.aspose.com/pdf/java/com.aspose.pdf/Font)类的setEmbedded属性将字体信息嵌入到PDF文件中。将此属性的值设置为‘true’将会把完整的字体文件嵌入到PDF中，需注意这会增加PDF文件的大小。以下是可用于将字体信息嵌入PDF的代码片段。

```php

    // 通过调用其空构造函数实例化PDF对象
    $document = new Document();

    // 在Pdf对象中创建一个部分
    $page = $document->getPages()->add();
    $fragment = new TextFragment("");
    $segment = new TextSegment("This is a sample text using Custom font.");

    $fontRepository = new FontRepository();

    $ts = new TextState();
    $ts->setFont($fontRepository->findFont("Univers Condensed"));
    $ts->getFont()->setEmbedded(true);
    $segment->setTextState($ts);
    $fragment->getSegments()->add($segment);
    $page->getParagraphs()->add($fragment);

    // 保存更新的PDF文件
    $document->save($outputFile);
    $document->close();
```


## 设置默认字体名称保存 PDF

当 PDF 文档包含的字体在文档本身和设备上都不可用时，API 会用默认字体替换这些字体。当字体可用时（即安装在设备上或嵌入到文档中），输出 PDF 应该使用相同的字体（不应替换为默认字体）。默认字体的值应包含字体的名称（而不是字体文件的路径）。我们实现了一个功能，可以在将文档保存为 PDF 时设置默认字体名称。以下代码片段可以用来设置默认字体：

```php

    // 加载现有的 PDF 文档
    $document = new Document($inputFile);
    $newName = "Arial";

    // 初始化 PDF 格式的保存选项
    $ops = new PdfSaveOptions();

    // 设置默认字体名称
    $ops->setDefaultFontName($newName);

    // 保存 PDF 文件
    $document->save($outputFile, $ops);
    // 保存更新后的 PDF 文件
    $document->close();
```

## 从 PDF 文档中获取所有字体

如果您想从 PDF 文档中获取所有字体，可以使用 [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) 类中提供的 **Document.getFontUtilities().getAllFonts()** 方法。
 请检查以下代码片段以获取现有 PDF 文档中的所有字体：

```php

    // 加载现有的 PDF 文档
    $document = new Document($inputFile);

    // 从文档中获取所有字体
    $fonts = $document->getFontUtilities()->getAllFonts();
    foreach ($fonts as $font) {
      $responseData = $responseData . $f->getFontName() . PHP_EOL;
    }

    // 保存更新后的 PDF 文件
    $document->close();
```

## 获取设置 PDF 文件的缩放因子

有时，你可能想设置或获取 PDF 文档的缩放因子。你可以使用 Aspose.PDF 轻松完成此需求。

[GoToAction](https://reference.aspose.com/pdf/java/com.aspose.pdf/GoToAction) 对象允许你获取与 PDF 文件关联的缩放值。同样，它也可以用于设置文件的缩放因子。

```php

    // 加载现有的 PDF 文档
    $document = new Document($inputFile);

    // 创建 GoToAction 对象
    $action = $document->getOpenAction();

    // 获取 PDF 文件的缩放因子
    $responseData = $action->getDestination()->getZoom();

    // 保存更新后的 PDF 文件
    $document->close();  
```

以下代码片段显示了如何获取 PDF 文件的缩放因子。

```php

    // 加载现有的 PDF 文档
    $document = new Document($inputFile);
    $zoom = 0.5;
    // 设置文档的缩放因子
    $page = $document->getPages()->get_Item(1);
    $actionzoom = new GoToAction(
      new XYZExplicitDestination($page, $page->getMediaBox()->getWidth(), $page->getMediaBox()->getHeight(), $zoom)
    );

    // 设置操作以适应页面宽度缩放
    $actionFitToWidth = new GoToAction(
      new FitHExplicitDestination($page, $page->getMediaBox()->getWidth())
    );

    // 设置操作以适应页面高度缩放
    $actionFittoHeight = new GoToAction(
      new FitVExplicitDestination($page, $page->getMediaBox()->getHeight())
    );

    $document->setOpenAction($actionzoom);
    $document->setOpenAction($actionFittoWidth);
    $document->setOpenAction($actionFittoHeight);

    // 保存更新的 PDF 文件
    $document->save($outputFile);
    $document->close();  
```