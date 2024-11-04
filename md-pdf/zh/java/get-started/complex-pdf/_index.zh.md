---  
title: 创建复杂的PDF  
linktitle: 创建复杂的PDF  
type: docs  
weight: 60  
url: /java/complex-pdf-example/  
description: Aspose.PDF for Java 允许您创建包含图像、文本片段和表格的更复杂的文档。  
lastmod: "2021-06-05"  
sitemap:  
    changefreq: "weekly"  
    priority: 0.7  
---  

[Hello, World](/pdf/java/hello-world-example/) 示例展示了使用 Java 和 Aspose.PDF 创建 PDF 文档的简单步骤。在本文中，我们将了解如何使用 Java 和 Aspose.PDF for Java 创建更复杂的文档。作为示例，我们将采用一家虚构的运营客运渡轮服务的公司的文档。  
我们的文档将包含一个图像、两个文本片段（标题和段落）以及一个表格。为了构建这样的文档，我们将使用基于DOM的方法。您可以在[DOM API 基础](/pdf/java/basics-of-dom-api/)部分阅读更多信息。  

如果我们从头创建一个文档，我们需要遵循某些步骤：

1. 实例化一个[Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document)对象。在这一步中，我们将创建一个带有一些元数据但没有页面的空PDF文档。
1. 向文档对象添加一个[Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page)。现在，我们的文档将有一页。
1. 添加一个[Image](https://reference.aspose.com/pdf/java/com.aspose.pdf/image)。这是一项基于PDF操作符的低级操作的复杂操作。
    - 从流中加载图像
    - 将图像添加到页面资源的Images集合中
    - 使用GSave操作符：此操作符保存当前图形状态。
    - 创建一个[Matrix](https://reference.aspose.com/pdf/java/com.aspose.pdf/matrix/)对象。
    - 使用ConcatenateMatrix操作符：定义图像的放置方式。
    - 使用Do操作符：此操作符绘制图像。
    - 使用GRestore操作符：此操作符恢复图形状态。

1. 为标题创建一个 [TextFragment](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextFragment)。对于标题，我们将使用 Arial 字体，字体大小为 24pt，居中对齐。
1. 将标题添加到页面的[段落](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page#getParagraphs--)中。
1. 为描述创建一个 [TextFragment](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextFragment)。对于描述，我们将使用 Arial 字体，字体大小为 24pt，居中对齐。
1. 将（描述）添加到页面的段落中。
1. 创建一个表格，添加表格属性。
1. 将（表格）添加到页面的[段落](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page#getParagraphs--)中。
1. 保存文档 "Complex.pdf"。

```java
package com.aspose.pdf.examples;

/**
 * 复杂示例
 */

import java.io.FileNotFoundException;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.time.Duration;
import java.time.LocalTime;

import com.aspose.pdf.*;
import com.aspose.pdf.operators.ConcatenateMatrix;
import com.aspose.pdf.operators.Do;
import com.aspose.pdf.operators.GRestore;
import com.aspose.pdf.operators.GSave;

public final class ComplexExample {

    private ComplexExample() {
    }

    private static Path _dataDir = Paths.get("/home/admin1/pdf-examples/");

    public static void main(String[] args) throws FileNotFoundException {
        // 初始化文档对象
        Document document = new Document();
        // 添加页面
        Page page = document.getPages().add();

        // -------------------------------------------------------------
        // 添加图片
        Path imageFileName = Paths.get(_dataDir.toString(),"logo.png");
        java.io.FileInputStream imageStream = new java.io.FileInputStream(new java.io.File(imageFileName.toString()));
        // 将图像添加到页面资源的图像集合中
        page.getResources().getImages().add(imageStream);

        // 使用 GSave 操作符：该操作符保存当前图形状态
        page.getContents().add(new GSave());
        Rectangle _logoPlaceHolder = new Rectangle(20, 730, 120, 830);

        // 创建矩阵对象
        Matrix matrix = new Matrix(new double[] {
            _logoPlaceHolder.getURX() - _logoPlaceHolder.getLLX(), 0, 0,
            _logoPlaceHolder.getURY() - _logoPlaceHolder.getLLY(),
            _logoPlaceHolder.getLLX(), _logoPlaceHolder.getLLY() });

        // 使用 ConcatenateMatrix（连接矩阵）操作符：定义图像的放置方式
        page.getContents().add(new ConcatenateMatrix(matrix));
        XImage ximage = page.getResources().getImages().get_Item(page.getResources().getImages().size());
        // 使用 Do 操作符：该操作符绘制图像
        page.getContents().add(new Do(ximage.getName()));
        // 使用 GRestore 操作符：该操作符恢复图形状态
        page.getContents().add(new GRestore());

        // -------------------------------------------------------------
        // 添加标题
        TextFragment header = new TextFragment("2020年秋季新渡轮航线");
        header.getTextState().setFont(FontRepository.findFont("Arial"));
        header.getTextState().setFontSize(24);
        header.setHorizontalAlignment(HorizontalAlignment.Center);
        header.setPosition(new Position(130, 720));
        page.getParagraphs().add(header);

        // 添加描述
        String descriptionText = "游客必须在线购票，每天的票数限制为5000张。渡轮服务以半容量和缩减时间表运营。预计会有排队。";
        TextFragment description = new TextFragment(descriptionText);
        description.getTextState().setFont(FontRepository.findFont("Times New Roman"));
        description.getTextState().setFontSize(14);
        description.setHorizontalAlignment(HorizontalAlignment.Left);
        page.getParagraphs().add(description);


        // 添加表格
        Table table = new Table();
        table.setColumnWidths("200");
        table.setBorder(new BorderInfo(BorderSide.Box, 1f, Color.getDarkSlateGray()));
        table.setDefaultCellBorder(new BorderInfo(BorderSide.Box, 0.5f, Color.getBlack()));
        table.getMargin().setBottom(10);
        table.getDefaultCellTextState().setFont(FontRepository.findFont("Helvetica"));

        Row headerRow = table.getRows().add();
        headerRow.getCells().add("离开城市");
        headerRow.getCells().add("离开岛屿");

        for (Cell headerRowCell : headerRow.getCells())
        {
            headerRowCell.setBackgroundColor(Color.getGray());
            headerRowCell.getDefaultCellTextState().setForegroundColor(Color.getWhiteSmoke());
        }

        LocalTime time = LocalTime.of(6,0);
        Duration incTime = Duration.ofMinutes(30);

        for (int i = 0; i < 10; i++)
        {
            Row dataRow = table.getRows().add();
            dataRow.getCells().add(time.toString());
            time=time.plus(incTime);
            dataRow.getCells().add(time.toString());
        }

        page.getParagraphs().add(table);

        document.save(Paths.get(_dataDir.toString(), "Complex.pdf").toString());
    }

}
```