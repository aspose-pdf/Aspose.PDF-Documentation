---
title: 获取和设置页面属性
type: docs
weight: 30
url: /java/get-and-set-page-properties/
description: 本主题解释如何在PDF文件中获取页码、获取页面属性以及使用Aspose.PDF for Java确定页面颜色。
lastmod: "2021-06-05"
---

Aspose.PDF for Java 允许您在 Java 应用程序中读取和设置 PDF 文件中页面的属性。本节展示了如何获取 PDF 文件的页数、获取 PDF 页面属性的信息（如颜色）和设置页面属性。

## 获取PDF文件的页数

在处理文档时，您经常想知道它们包含多少页。使用 Aspose.PDF，这只需要两行代码。

要获取 PDF 文件的页数：

1. 使用 [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) 类打开 PDF 文件。

1. 然后使用 [PageCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf.class-use/PageCollection) 集合的 Count 属性（从 Document 对象）获取文档中的总页数。

以下代码片段显示了如何获取 PDF 文件的页数。

```java
package com.aspose.pdf.examples;

import com.aspose.pdf.*;

public class ExampleGetAndSetPageProperties {
    // 文档目录的路径。
    private static String _dataDir = "/home/admin1/pdf-examples/Samples/";

    public static void GetNumberOfPagesInaPDFFile() {

        // 打开文档
        Document pdfDocument = new Document(_dataDir + "GetNumberofPages.pdf");

        // 获取页数
        System.out.println("Page Count : " + pdfDocument.getPages().size());
        _dataDir = _dataDir + "ApplyNumberStyle_out.pdf";
        pdfDocument.save(_dataDir);

    }
```

### 在不保存文档的情况下获取页数

除非 PDF 文件被保存并且所有元素实际被放置在 PDF 文件中，否则我们无法获取特定文档的页数（因为我们无法确定所有元素将适应的页数）。
 然而，从 Aspose.PDF for Java 10.1.0 版本开始，我们引入了一个名为 [processParagraphs(...)](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#processParagraphs--) 的方法，该方法提供了获取 PDF 文档页数的功能，而无需保存文件。因此，我们可以即时获取页数信息。请尝试使用以下代码片段来完成此需求。

```java
public static void GetPageCountWithoutSavingTheDocument() {

        // 有关完整的示例和数据文件，请访问
        // https://github.com/aspose-pdf/Aspose.Pdf-for-Java
        // 实例化 Document 实例
        Document doc = new Document();
        // 向 PDF 文件的页面集合中添加页面
        Page page = doc.getPages().add();
        // 创建一个循环以添加 300 个 TextFragment 实例
        for (int i = 0; i < 300; i++)
            // 将 TextFragment 添加到 PDF 第一页的段落集合中
            page.getParagraphs().add(new TextFragment("页数测试"));
        // 处理段落以获取页数信息
        doc.processParagraphs();
        System.out.println("PDF 中的页数 = " + doc.getPages().size());
    }
```

## 获取页面属性

PDF 文件中的每个页面都有许多属性，例如宽度、高度、出血框、裁剪框和修整框。Aspose.PDF 允许您访问这些属性。

### **理解页面属性：Artbox、BleedBox、CropBox、MediaBox、TrimBox 和 Rect 属性之间的区别**

- **媒体框**：媒体框是最大的页面框。它对应于在将文档打印为 PostScript 或 PDF 时选择的页面大小（例如 A4、A5、US Letter 等）。换句话说，媒体框决定了显示或打印 PDF 文档的介质的物理尺寸。
- **出血框**：如果文档有出血，PDF 也会有出血框。
 出血是颜色（或艺术作品）超出页面边缘的部分。它用于确保当文件被打印并裁切到尺寸（“修剪”）时，墨水能够一直延伸到页面的边缘。即使页面被错误地修剪——稍微偏离修剪标记——页面上也不会出现白色边缘。

- **修剪框**：修剪框指示文件在打印和修剪后的最终大小。
- **艺术框**：艺术框是围绕文档中页面实际内容绘制的框。当在其他应用程序中导入 PDF 文档时使用此页面框。
- **裁剪框**：裁剪框是您的 PDF 文档在 Adobe Acrobat 中显示的“页面”大小。在正常视图中，Adobe Acrobat 中仅显示裁剪框的内容。
  有关这些属性的详细描述，请阅读 Adobe.Pdf 规范，特别是 10.10.1 页边界。
- **Page.Rect**：MediaBox 和 DropBox 的交集（通常是可见矩形）。 下面的图片说明了这些属性。

有关详细信息，请访问[此页面](http://www.enfocus.com/manuals/ReferenceGuide/PP/10/enUS/en-us/concept/c_aa1095731.html)。

### 访问页面属性

[Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page) 类提供了与特定 PDF 页面相关的所有属性。PDF 文件的所有页面都包含在 [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) 对象的 [PageCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf.class-use/PageCollection) 集合中。

从那里，可以使用其索引访问单个 Page 对象，或者使用 foreach 循环遍历集合以获取所有页面。一旦访问到单个页面，我们就可以获取其属性。以下代码片段显示了如何获取页面属性。

```java
    public static void AccessingPageProperties() {

        Document pdfDocument = new Document("input.pdf");

        // 获取页面集合
        PageCollection pageCollection = pdfDocument.getPages();

        // 获取特定页面
        Page pdfPage = pageCollection.get_Item(1);

        // 获取页面属性
        System.out.printf("\n ArtBox : Height = " + pdfPage.getArtBox().getHeight() + ", Width = "
                + pdfPage.getArtBox().getWidth() + ", LLX = " + pdfPage.getArtBox().getLLX() + ", LLY = "
                + pdfPage.getArtBox().getLLY() + ", URX = " + pdfPage.getArtBox().getURX() + ", URY = "
                + pdfPage.getArtBox().getURY());
        System.out.printf("\n BleedBox : Height = " + pdfPage.getBleedBox().getHeight() + ", Width = "
                + pdfPage.getBleedBox().getWidth() + ", LLX = " + pdfPage.getBleedBox().getLLX() + ", LLY = "
                + pdfPage.getBleedBox().getLLY() + ", URX = " + pdfPage.getBleedBox().getURX() + ", URY = "
                + pdfPage.getBleedBox().getURY());
        System.out.printf("\n CropBox : Height = " + pdfPage.getCropBox().getHeight() + ", Width = "
                + pdfPage.getCropBox().getWidth() + ", LLX = " + pdfPage.getCropBox().getLLX() + ", LLY = "
                + pdfPage.getCropBox().getLLY() + ", URX = " + pdfPage.getCropBox().getURX() + ", URY = "
                + pdfPage.getCropBox().getURY());
        System.out.printf("\n MediaBox : Height = " + pdfPage.getMediaBox().getHeight() + ", Width = "
                + pdfPage.getMediaBox().getWidth() + ", LLX = " + pdfPage.getMediaBox().getLLX() + ", LLY = "
                + pdfPage.getMediaBox().getLLY() + ", URX = " + pdfPage.getMediaBox().getURX() + ", URY = "
                + pdfPage.getMediaBox().getURY());
        System.out.printf("\n TrimBox : Height = " + pdfPage.getTrimBox().getHeight() + ", Width = "
                + pdfPage.getTrimBox().getWidth() + ", LLX = " + pdfPage.getTrimBox().getLLX() + ", LLY = "
                + pdfPage.getTrimBox().getLLY() + ", URX = " + pdfPage.getTrimBox().getURX() + ", URY = "
                + pdfPage.getTrimBox().getURY());
        System.out.printf(
                "\n Rect : Height = " + pdfPage.getRect().getHeight() + ", Width = " + pdfPage.getRect().getWidth()
                        + ", LLX = " + pdfPage.getRect().getLLX() + ", LLY = " + pdfPage.getRect().getLLY() + ", URX = "
                        + pdfPage.getRect().getURX() + ", URY = " + pdfPage.getRect().getURY());
        System.out.printf("\n Page Number :- " + pdfPage.getNumber());
        System.out.printf("\n Rotate :-" + pdfPage.getRotate());
    }
```

## 确定页面颜色

[Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page) 类提供了与 PDF 文档中特定页面相关的属性，包括页面使用的颜色类型 - RGB、黑白、灰度或未定义。

PDF 文件的所有页面都包含在 [PageCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf/PageCollection) 集合中。[ColorType](https://reference.aspose.com/pdf/java/com.aspose.pdf/ColorType) 属性指定页面上元素的颜色。要获取或确定特定 PDF 页面的颜色信息，请使用 [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page) 类对象的 [ColorType](https://reference.aspose.com/pdf/java/com.aspose.pdf/ColorType) 属性。

以下代码片段展示了如何遍历 PDF 文件的各个页面以获取颜色信息。

```java
    public static void DeterminePageColor () {

        Document pdfDocument = new Document("input.pdf");
        // 遍历 PDF 文件的所有页面
        for (int pageCount = 1; pageCount <= pdfDocument.getPages().size(); pageCount++) {
            // 获取特定 PDF 页面的颜色类型信息
            int pageColorType = pdfDocument.getPages().get_Item(pageCount).getColorType();
            switch (pageColorType) {
            case 2:
                System.out.println("页面 # -" + pageCount + " 是黑白色..");
                break;
            case 1:
                System.out.println("页面 # -" + pageCount + " 是灰度...");
                break;
            case 0:
                System.out.println("页面 # -" + pageCount + " 是 RGB..");
                break;
            case 3:
                System.out.println("页面 # -" + pageCount + " 颜色未定义..");
                break;
            }
        }
    }
}
```