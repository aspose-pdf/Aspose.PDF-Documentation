---
title: 使用工件
linktitle: 使用工件
type: docs
weight: 110
url: zh/java/artifacts/
description: 本页介绍如何使用 Aspose.PDF for Java 处理 Artifact 类。代码示例展示了如何向 PDF 页面添加背景图像以及如何获取 PDF 文件第一页上的每个水印。
lastmod: "2021-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

工件通常是图形对象或其他标记，不属于创作内容的一部分。在您的 PDF 示例中，工件包括不同的信息，例如页面的页眉或页脚、分隔页面部分的线条或其他图形，或装饰图像。

[Artifact](https://reference.aspose.com/pdf/java/com.aspose.pdf/Artifact) 类包含：

- [Artifact.Type](https://reference.aspose.com/pdf/java/com.aspose.pdf/Artifact.ArtifactType) – 获取工件类型（支持 Artifact.ArtifactType 枚举的值，其中值包括 Background、Layout、Page、Pagination 和 Undefined）。
- [Artifact.Subtype](https://reference.aspose.com/pdf/java/com.aspose.pdf/Artifact.ArtifactSubtype) – 获取工件子类型（支持Artifact.ArtifactSubtype枚举的值，其中包括Background, Footer, Header, Undefined, Watermark）。

使用Adobe Acrobat创建的水印称为工件（如PDF规范的14.8.2.2节中描述的真实内容和工件）。为了处理工件，Aspose.PDF提供了两个类：[Artifact](https://reference.aspose.com/pdf/java/com.aspose.pdf/Artifact) 和 [ArtifactCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf/ArtifactCollection)。

为了获取特定页面上的所有工件，[Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page) 类具有Artifacts属性。本主题解释了如何在PDF文件中处理工件。

以下代码片段显示了如何在PDF文件的第一页设置水印。

```java

 public class ExamplesArtifacts {

    private static String _dataDir = "/home/aspose/pdf-examples/Samples/Artifacts/";

    public static void SetWatermark(){
        Document doc = new Document(_dataDir + "sample.pdf");
        WatermarkArtifact artifact = new WatermarkArtifact();        
        artifact.setText(new FormattedText("WATERMARK", java.awt.Color.BLUE, 
                            FontStyle.Courier,
                            EncodingType.Identity_h, true, 72));
        artifact.setArtifactHorizontalAlignment (HorizontalAlignment.Center);
        artifact.setArtifactVerticalAlignment (VerticalAlignment.Center);
        artifact.setRotation (45);
        artifact.setOpacity (0.5);
        artifact.setBackground (true);
        doc.getPages().get_Item(1).getArtifacts().add(artifact);
        doc.save(_dataDir + "watermark.pdf");
    }
```


背景图像可以用于为文档添加水印或其他细微的设计。在 Aspose.PDF for Java 中，每个 PDF 文档是一个页面的集合，每个页面包含一个工件的集合。[BackgroundArtifact](https://reference.aspose.com/pdf/java/com.aspose.pdf/BackgroundArtifact) 类可以用于向页面对象添加背景图像。

以下代码片段显示了如何使用 BackgroundArtifact 对象向 PDF 页面添加背景图像。

```java

    public static void SetBackground() throws FileNotFoundException {

        // 打开文档
        Document pdfDocument = new Document();
                
        // 向文档对象添加新页面
        Page page = pdfDocument.getPages().add();

        // 创建背景工件对象
        BackgroundArtifact background = new BackgroundArtifact();

        // 为 backgroundartifact 对象指定图像
        background.setBackgroundImage(new java.io.FileInputStream(new java.io.File(_dataDir + "background.png")));
        
        // 将 BackgroundArtifact 添加到页面的工件集合中
        page.getArtifacts().add(background);

        // 保存修改后的 PDF
        pdfDocument.save(_dataDir + "ImageAsBackground_out.pdf");

    }
```


## 编程示例: 获取水印

以下代码片段展示了如何获取 PDF 文件第一页上的每个水印。

```java
    public static void GettingWatermarks() {
        // 打开文档
        Document pdfDocument = new Document(_dataDir +  "watermark_new.pdf");
        // 迭代并获取工件的子类型、文本和位置
        for (Artifact artifact : pdfDocument.getPages().get_Item(1).getArtifacts())
        {
            System.out.println(artifact.getSubtype() + " " + artifact.getText() + " " + artifact.getRectangle().toString());
        }
```

## 编程示例: 计算特定类型的工件数量

要计算特定类型的工件总数（例如，水印总数），请使用以下代码：

```java
    public static void CountingArtifacts() {
        // 打开文档
        Document pdfDocument = new Document(_dataDir +  "watermark_new.pdf");
        int count = 0;
        for (Artifact artifact : pdfDocument.getPages().get_Item(1).getArtifacts())
        {
            // 如果工件类型是水印，增加计数器
            if (artifact.getSubtype() == Artifact.ArtifactSubtype.Watermark) count++;
        }
        System.out.println("页面包含 " + count + " 个水印");
    }
```