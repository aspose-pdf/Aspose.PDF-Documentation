---
title: 在 PDF 中处理标题
type: docs
weight: 70
url: /zh/java/working-with-headings/
lastmod: "2021-06-05"
description: 使用 Java 在 PDF 文档中创建标题编号。Aspose.PDF for Java 提供不同种类的编号样式。
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## 在标题中应用编号样式

标题是任何文档的重要部分。作者总是试图使标题更加突出和有意义。如果一个文档中有多个标题，作者有几种选项来组织这些标题。组织标题的最常见方法之一是以编号样式书写标题。

Aspose.PDF for Java 提供了许多预定义的编号样式。这些预定义的编号样式存储在一个枚举中，NumberingStyle。NumberingStyle 枚举的预定义值及其描述如下：

|**标题类型**|**描述**|
| :- | :- |
|NumeralsArabic|阿拉伯类型，例如，1,1.1，...|

|NumeralsRomanUppercase|罗马大写类型，例如，I,I.II，...|
|NumeralsRomanLowercase|罗马小写类型，例如 i,i.ii, ...|
|LettersUppercase|英文大写类型，例如 A,A.B, ...|
|LettersLowercase|英文小写类型，例如 a,a.b, ...|
[com.aspose.pdf.Heading](https://reference.aspose.com/pdf/java/com.aspose.pdf/Heading) 类的 [setStyle](https://reference.aspose.com/pdf/java/com.aspose.pdf/Heading) 属性用于设置标题的编号样式。

下面示例中给出了获取上图所示输出的源代码。

```java
package com.aspose.pdf.examples;

import com.aspose.pdf.*;

public class ExampleHeading {
    // 文档目录的路径。
    private static String _dataDir = "/home/admin1/pdf-examples/Samples/";

    public static void ApplyNumberingStyleinHeading() {

        Document pdfDoc = new Document();
        pdfDoc.getPageInfo().setWidth(612.0);
        pdfDoc.getPageInfo().setHeight(792.0);
        pdfDoc.getPageInfo().setMargin(new MarginInfo());
        pdfDoc.getPageInfo().getMargin().setLeft(72);
        pdfDoc.getPageInfo().getMargin().setRight(72);
        pdfDoc.getPageInfo().getMargin().setTop(72);
        pdfDoc.getPageInfo().getMargin().setBottom(72);

        Page pdfPage = pdfDoc.getPages().add();
        pdfPage.getPageInfo().setWidth(612.0);
        pdfPage.getPageInfo().setHeight(792.0);
        pdfDoc.getPageInfo().setMargin(new MarginInfo());
        pdfDoc.getPageInfo().getMargin().setLeft(72);
        pdfDoc.getPageInfo().getMargin().setRight(72);
        pdfDoc.getPageInfo().getMargin().setTop(72);
        pdfDoc.getPageInfo().getMargin().setBottom(72);

        FloatingBox floatBox = new FloatingBox();
        floatBox.setMargin(pdfPage.getPageInfo().getMargin());

        pdfPage.getParagraphs().add(floatBox);

        Heading heading = new Heading(1);
        heading.setInList(true);
        heading.setStartNumber(1);
        heading.setText("列表 1");
        heading.setStyle(NumberingStyle.NumeralsRomanLowercase);
        heading.setAutoSequence(true);

        floatBox.getParagraphs().add(heading);
        Heading heading2 = new Heading(1);
        heading2.setInList(true);
        heading2.setStartNumber(13);
        heading2.setText("列表 2");
        heading2.setStyle(NumberingStyle.NumeralsRomanLowercase);
        heading2.setAutoSequence(true);

        floatBox.getParagraphs().add(heading2);

        Heading heading3 = new Heading(2);
        heading3.setInList(true);
        heading3.setStartNumber(1);
        heading3.setText("根据计划生效日期分配的财产价值，针对每个批准的");
        heading3.setStyle (NumberingStyle.LettersLowercase);
        heading3.setAutoSequence(true);

        floatBox.getParagraphs().add(heading3);
        _dataDir = _dataDir + "ApplyNumberStyle_out.pdf";
        pdfDoc.save(_dataDir);

    }

}
```