---
title: 获取和设置页面属性
type: docs
weight: 30
url: /php-java/get-and-set-page-properties/
description: 本主题解释如何在 PDF 文件中获取数字，获取页面属性并使用 Aspose.PDF for PHP via Java 确定页面颜色。
lastmod: "2024-06-05"
---

Aspose.PDF for PHP via Java 使您可以在 Java 应用程序中读取和设置 PDF 文件页面的属性。本节展示如何获取 PDF 文件中的页数，获取有关 PDF 页面属性的信息（例如颜色）以及设置页面属性。

## 获取 PDF 文件中的页数

在处理文档时，您通常想知道它们包含多少页。使用 Aspose.PDF，这只需要两行代码。

要获取 PDF 文件中的页数：

1. 使用 [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) 类打开 PDF 文件。
1. 然后检索文档的页面。尝试从检索到的页面中获取页数。

以下代码片段展示了如何获取 PDF 文件的页数。

```php

    // 打开文档
    $document = new Document($inputFile);      

    $pages = $document->getPages();

    // 获取页面数量
    $responseData = $responseData . "页面数量 : " + $pages->size();
```

### 获取页面数量而不保存文档

除非PDF文件被保存并且所有元素实际被放置在PDF文件中，否则我们无法获取特定文档的页面数量（因为我们无法确定所有元素将被容纳在多少页中）。然而，从通过Java的Aspose.PDF for PHP版本开始，我们引入了一种名为[processParagraphs(...)](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#processParagraphs--)的方法，该方法提供了获取PDF文档页面数量的功能，而无需保存文件。因此，我们可以实时获取页面数量信息。请尝试使用以下代码片段来实现此要求。

```php

    // 打开文档
    $document = new Document($inputFile);      

    // 将页面添加到PDF文件的页面集合中
    $page = $document->getPages()->add();
    
    // 创建一个循环以添加300个TextFragment实例
    for ($i=0; $i < 300; $i++) { 
       // 将TextFragment添加到PDF第一页的段落集合中
       $page->getParagraphs()->add(new TextFragment("页面数量测试"));
    }
    
    // 处理段落以获取页面数量信息
    $document->processParagraphs();

    $pages = $document->getPages();

    // 获取页面数量
    $responseData = $responseData . "页面数量 : " + $pages->size();
```


## 获取页面属性

每个 PDF 文件中的页面都有许多属性，例如宽度、高度、出血框、裁剪框和修整框。Aspose.PDF 允许您访问这些属性。

### **理解页面属性：Artbox、BleedBox、CropBox、MediaBox、TrimBox 和 Rect 属性之间的区别**

- **媒体框**：媒体框是最大的页面框。它对应于打印到 PostScript 或 PDF 时选择的页面大小（例如 A4、A5、US Letter 等）。换句话说，媒体框决定了显示或打印 PDF 文档的媒体的物理大小。
- **出血框**：如果文档有出血，PDF 也将有一个出血框。
 出血是超出页面边缘的颜色（或艺术作品）的量。它用于确保当文档打印并切割到尺寸（“修剪”）时，墨水会覆盖到页面的边缘。即使页面修剪不当 - 略微偏离修剪标记切割 - 页面上也不会出现白色边缘。
- **修剪框**: 修剪框表示文档在打印和修剪后的最终尺寸。
- **艺术框**: 艺术框是在文档中页面的实际内容周围绘制的框。当在其他应用程序中导入 PDF 文档时使用此页面框。
- **裁剪框**: 裁剪框是您的 PDF 文档在 Adobe Acrobat 中显示的“页面”尺寸。在正常视图中，Adobe Acrobat 中仅显示裁剪框的内容。
  有关这些属性的详细描述，请阅读 Adobe.Pdf 规范，特别是 10.10.1 页边界。
- **页面.矩形**: MediaBox 和 DropBox 的交集（通常是可见矩形）。 下图说明了这些属性。

有关更多详细信息，请访问[此页面](http://www.enfocus.com/manuals/ReferenceGuide/PP/10/enUS/en-us/concept/c_aa1095731.html)。

### 访问页面属性

以下代码片段获取文档中特定页面的属性，例如ArtBox、BleedBox、CropBox、MediaBox、TrimBox、Rect、页码和旋转。然后将提取的数据存储在单独的变量中，并将它们连接成一个响应字符串。

1. 使用 $inputFile 变量创建一个新的 Document 对象。
1. 使用 getPages() 方法从文档中获取页面集合。
1. 使用 get_Item() 方法从页面集合中获取特定页面。
1. 从特定页面对象中提取各种属性（ArtBox、BleedBox、CropBox、MediaBox、TrimBox、Rect、页码、旋转）并将它们存储在单独的变量中。
1. 代码将提取的属性值连接成单独的响应字符串（$responseData1，$responseData2 等）。
1. 接下来，它尝试使用 $pages 对象的 size() 方法检索页数，但 $pages 变量未定义。

以下代码片段展示了如何获取页面属性。

```php

   // 打开文档
    $document = new Document($inputFile);

    // 获取页面集合
    $pageCollection = $document->getPages();

    // 获取特定页面
    $page = $pageCollection->get_Item(1);

    // 获取页面属性
    $responseData1 = "ArtBox : Height = " . $page->getArtBox()->getHeight()
        . ", Width = " . $page->getArtBox()->getWidth()
        . ", LLX = " . $page->getArtBox()->getLLX()
        . ", LLY = " . $page->getArtBox()->getLLY()
        . ", URX = " . $page->getArtBox()->getURX()
        . ", URY = " . $page->getArtBox()->getURY()
        . PHP_EOL;

    $responseData2 = "BleedBox : Height = " . $page->getBleedBox()->getHeight() . ", Width = "
        . $page->getBleedBox()->getWidth() . ", LLX = " . $page->getBleedBox()->getLLX() . ", LLY = "
        . $page->getBleedBox()->getLLY() . ", URX = " . $page->getBleedBox()->getURX() . ", URY = "
        . $page->getBleedBox()->getURY()
        . PHP_EOL;

    $responseData3 = "CropBox : Height = " . $page->getCropBox()->getHeight() . ", Width = "
        . $page->getCropBox()->getWidth() . ", LLX = " . $page->getCropBox()->getLLX() . ", LLY = "
        . $page->getCropBox()->getLLY() . ", URX = " . $page->getCropBox()->getURX() . ", URY = "
        . $page->getCropBox()->getURY()
        . PHP_EOL;

    $responseData4 = " MediaBox : Height = " . $page->getMediaBox()->getHeight() . ", Width = "
        . $page->getMediaBox()->getWidth() . ", LLX = " . $page->getMediaBox()->getLLX() . ", LLY = "
        . $page->getMediaBox()->getLLY() . ", URX = " . $page->getMediaBox()->getURX() . ", URY = "
        . $page->getMediaBox()->getURY()
        . PHP_EOL;

    $responseData5 = " TrimBox : Height = " . $page->getTrimBox()->getHeight() . ", Width = "
        . $page->getTrimBox()->getWidth() . ", LLX = " . $page->getTrimBox()->getLLX() . ", LLY = "
        . $page->getTrimBox()->getLLY() . ", URX = " . $page->getTrimBox()->getURX() . ", URY = "
        . $page->getTrimBox()->getURY()
        . PHP_EOL;

    $responseData5 = " Rect : Height = " . $page->getRect()->getHeight() . ", Width = " . $page->getRect()->getWidth()
        . ", LLX = " . $page->getRect()->getLLX() . ", LLY = " . $page->getRect()->getLLY() . ", URX = "
        . $page->getRect()->getURX() . ", URY = " . $page->getRect()->getURY()
        . PHP_EOL;
        
    $responseData6 = " Page Number :- " . $page->getNumber() . PHP_EOL;
    $responseData7 = " Rotate :-" . $page->getRotate() . PHP_EOL;

    // 获取页数
    $responseData8 = $responseData8 . "Page Count : " . $pages->size();
```


## 确定页面颜色

[Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page) 类提供了与 PDF 文档中特定页面相关的属性，包括页面使用的颜色类型 - RGB、黑白、灰度或未定义。

PDF 文件的所有页面都包含在 [PageCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf/PageCollection) 集合中。[ColorType](https://reference.aspose.com/pdf/java/com.aspose.pdf/ColorType) 属性指定页面上元素的颜色。要获取或确定特定 PDF 页面的颜色信息，请使用 [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page) 类对象的 [ColorType](https://reference.aspose.com/pdf/java/com.aspose.pdf/ColorType) 属性。

以下代码片段展示了如何遍历 PDF 文件的各个页面以获取颜色信息。

```php

    // 打开文档
    $document = new Document($inputFile);

    // 遍历 PDF 文件的所有页面
    for ($pageCount = 1; $pageCount <= $document->getPages()->size(); $pageCount++) {

        // 获取特定 PDF 页面的颜色类型信息
        $pageColorType = $document->getPages()->get_Item($pageCount)->getColorType();

        switch ($pageColorType) {
            case 2:
                $responseData ="页面 # -" . $pageCount . " 是黑白的..";
                break;
            case 1:
                $responseData ="页面 # -" . $pageCount . " 是灰度..";
                break;
            case 0:
                $responseData ="页面 # -" . $pageCount . " 是 RGB..";
                break;
            case 3:
                $responseData ="页面 # -" . $pageCount . " 颜色未定义..";
                break;
        }
    }
```