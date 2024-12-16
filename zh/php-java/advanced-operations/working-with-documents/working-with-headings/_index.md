title: 在PDF中处理标题
type: docs
weight: 70
url: /zh/php-java/working-with-headings/
lastmod: "2024-06-05"
description: 使用PHP在PDF文档的标题中创建编号。Aspose.PDF for PHP via Java提供不同类型的编号样式。
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## 在标题中应用编号样式

标题是任何文档的重要部分。作者总是试图使标题对读者更加突出和有意义。如果文档中有多个标题，作者有多种选项来组织这些标题。组织标题最常见的方法之一是以编号样式书写标题。

Aspose.PDF for PHP via Java提供了许多预定义的编号样式。这些预定义的编号样式存储在一个枚举中，称为NumberingStyle。NumberingStyle枚举的预定义值及其描述如下：

|**标题类型**|**描述**|
| :- | :- |

|NumeralsArabic|阿拉伯类型，例如，1,1.1,...|
|NumeralsRomanUppercase|罗马大写类型，例如，I,I.II,...|
|NumeralsRomanLowercase|罗马小写类型，例如，i,i.ii,...|
|LettersUppercase|英文大写类型，例如，A,A.B,...|
|LettersLowercase|英文小写类型，例如，a,a.b,...|
[com.aspose.pdf.Heading](https://reference.aspose.com/pdf/java/com.aspose.pdf/Heading) 类的 [setStyle](https://reference.aspose.com/pdf/java/com.aspose.pdf/Heading) 属性用于设置标题的编号样式。

下面的示例提供了获取上图所示输出的源代码。

```php

    // 打开文档
    $document = new Document($inputFile);
    $document->getPageInfo()->setWidth(612.0);
    $document->getPageInfo()->setHeight(792.0);
    $document->getPageInfo()->setMargin(new MarginInfo());
    $document->getPageInfo()->getMargin()->setLeft(72);
    $document->getPageInfo()->getMargin()->setRight(72);
    $document->getPageInfo()->getMargin()->setTop(72);
    $document->getPageInfo()->getMargin()->setBottom(72);

    $page = $document->getPages()->add();
    $page->getPageInfo()->setWidth(612.0);
    $page->getPageInfo()->setHeight(792.0);
    $document->getPageInfo()->setMargin(new MarginInfo());
    $document->getPageInfo()->getMargin()->setLeft(72);
    $document->getPageInfo()->getMargin()->setRight(72);
    $document->getPageInfo()->getMargin()->setTop(72);
    $document->getPageInfo()->getMargin()->setBottom(72);

    $floatBox = new FloatingBox();
    $floatBox->setMargin($page->getPageInfo()->getMargin());

    $page->getParagraphs()->add($floatBox);

    $heading = new Heading(1);
    $heading->setInList(true);
    $heading->setStartNumber(1);
    $heading->setText("列表 1");
    $heading->setStyle(NumberingStyle::$NumeralsRomanLowercase);
    $heading->setAutoSequence(true);

    $floatBox->getParagraphs()->add($heading);
    $heading2 = new Heading(1);
    $heading2->setInList(true);
    $heading2->setStartNumber(13);
    $heading2->setText("列表 2");
    $heading2->setStyle(NumberingStyle::$NumeralsRomanLowercase);
    $heading2->setAutoSequence(true);

    $floatBox->getParagraphs()->add($heading2);

    $heading3 = new Heading(2);
    $heading3->setInList(true);
    $heading3->setStartNumber(1);
    $heading3->setText("计划生效日时计划下待分配财产的价值，用于每个被允许的账户");
    $heading3->setStyle (NumberingStyle::$LettersLowercase);
    $heading3->setAutoSequence(true);

    $floatBox->getParagraphs()->add($heading3);
    
    $document->save($outputFile);
    $document->close();
```