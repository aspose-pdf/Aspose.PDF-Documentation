---
title: 从PDF文件中提取原始文本
linktitle: 从PDF中提取文本
type: docs
weight: 10
url: zh/java/extract-text-from-all-pdf/
description: 本文介绍了使用Aspose.PDF for Java从PDF文档中提取文本的各种方法。包括从整个页面、特定部分、基于列等。
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## 从PDF文档的所有页面提取文本

从PDF文档中提取文本是一个常见的需求。在这个例子中，你将看到Aspose.PDF for Java如何允许从PDF文档的所有页面提取文本。
要从所有PDF页面提取文本：

1. 创建一个[TextAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextAbsorber)类的对象。

1. 使用 [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) 类打开 PDF，并调用 [Pages](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page) 集合的 [Accept](https://reference.aspose.com/pdf/java/com.aspose.pdf/PageCollection#accept-com.aspose.pdf.TextAbsorber-) 方法。
1. [TextAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextAbsorber) 类从文档中吸收文本并返回到 **Text** 属性中。

以下代码片段向您展示如何从 PDF 文档的所有页面中提取文本。

```java
public static void ExtractFromAllPages(){
    // 文档目录的路径。
    String _dataDir = "/home/admin1/pdf-examples/Samples/";
    String filePath = _dataDir + "ExtractTextAll.pdf";

    // 打开文档
    com.aspose.pdf.Document pdfDocument = new com.aspose.pdf.Document(filePath);

    // 创建 TextAbsorber 对象以提取文本
    com.aspose.pdf.TextAbsorber textAbsorber = new com.aspose.pdf.TextAbsorber();
    
    // 为所有页面接受吸收器
    pdfDocument.getPages().accept(textAbsorber);
    
    // 获取提取的文本
    String extractedText = textAbsorber.getText();                
    try {
        java.io.FileWriter writer = new java.io.FileWriter(_dataDir + "extracted-text.txt", true);
        // 写入一行文本到文件
        writer.write(extractedText);            
        // 关闭流
        writer.close();
    } catch (java.io.IOException e) {
        e.printStackTrace();
    }

}
```


## 使用文本设备从页面提取文本

您可以使用**TextDevice**类从PDF文件中提取文本。TextDevice在其实现中使用了[TextAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextAbsorber)，因此，实际上它们做的是相同的事情，但TextDevice只是实现了“设备”方法以统一从页面提取任何内容，如ImageDevice、PageDevice等。TextAbsorber可以从页面、整个PDF或XForm中提取文本，这个TextAbsorber更通用。

### 从所有页面提取文本

以下步骤和代码片段展示了如何使用文本设备从PDF中提取文本。

1. 使用指定的输入PDF文件创建Document类的对象
2. 创建TextDevice类的对象
3. 使用TextExtractOptions类的对象指定提取选项
4. 使用TextDevice类的Process方法将内容转换为文本
5. 将文本保存到输出文件

```java
public static void extractTextFromAllPagesOfPDF() throws IOException {
    // 打开文档
    Document pdfDocument = new Document("input.pdf");
    // 将提取的文本保存到的文本文件
    java.io.OutputStream text_stream = new java.io.FileOutputStream("ExtractedText.txt", false);
    // 遍历PDF文件的所有页面
    for (Page page : (Iterable<Page>) pdfDocument.getPages()) {
        // 创建文本设备
        TextDevice textDevice = new TextDevice();
        // 设置文本提取选项 - 设置文本提取模式（Raw或
        // Pure）
        TextExtractionOptions textExtOptions = new TextExtractionOptions(TextExtractionOptions.TextFormattingMode.Raw);
        textDevice.setExtractionOptions(textExtOptions);
        // 从PDF页面获取文本并保存到OutputStream对象
        textDevice.process(page, text_stream);
    }
    // 关闭流对象
    text_stream.close();
}
```


## 从特定页面区域提取文本

[TextAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextAbsorber) 类提供了从 PDF 文档的特定页面或所有页面提取文本的功能。该类在 **Text** 属性中返回提取的文本。然而，如果我们需要从特定页面区域提取文本，可以使用 [TextSearchOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextSearchOptions) 的 **Rectangle** 属性。Rectangle 属性接受一个 Rectangle 对象作为值，使用此属性，我们可以指定需要提取文本的页面区域。

调用页面的 [Accept](https://reference.aspose.com/pdf/java/com.aspose.pdf/PageCollection#accept-com.aspose.pdf.TextAbsorber-) 方法以提取文本。
 创建 [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) 和 [TextAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextAbsorber) 类的对象。在 **Document** 对象的单个页面上调用 [Accept](https://reference.aspose.com/pdf/java/com.aspose.pdf/PageCollection#accept-com.aspose.pdf.TextAbsorber-) 方法，作为 **Page** 索引。**Index** 是需要提取文本的特定页码。您可以从 [TextAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextAbsorber) 类的 **Text** 属性中获取文本。以下代码片段展示了如何从单个页面中提取文本。

```java
public static void ExtractTextFromParticularPageRegion(String[] args) throws IOException {
    // 打开文档
    Document doc = new Document("page_0001.pdf");
    // 创建 TextAbsorber 对象以提取文本
    TextAbsorber absorber = new TextAbsorber();
    absorber.getTextSearchOptions().setLimitToPageBounds(true);
    absorber.getTextSearchOptions().setRectangle(new Rectangle(100, 200, 250, 350));
    // 接受第一页的 absorber
    doc.getPages().get_Item(1).accept(absorber);
    // 获取提取的文本
    String extractedText = absorber.getText();
    // 创建一个 writer 并打开文件
    BufferedWriter writer = new BufferedWriter(new FileWriter(new java.io.File("ExtractedText.txt")));
    // 写入提取的内容
    writer.write(extractedText);
    // 关闭 writer
    writer.close();
}
```

## 基于列提取文本

一个 PDF 文件可能包含文本、图像、注释、附件、图表等元素，而 Aspose.PDF for .NET 提供了添加和操作所有这些元素的功能。当涉及到从 PDF 文档中添加和提取文本时，这个 API 非常出色。我们可能会遇到这样的情况：一个 PDF 文档由多列组成（多列 PDF 文档），我们需要在保持相同布局的同时提取页面内容，那么 Aspose.PDF for .NET 是完成此需求的正确选择。一种方法是减少 PDF 文档内部内容的字体大小，然后执行文本提取。以下代码片段展示了减少文本大小然后尝试从 PDF 文档中提取文本的步骤。

```java
public static void ExtractTextBasedOnColumns() throws IOException {
    // 打开文档
    Document doc = new Document("page_0001.pdf");
    // 创建 TextAbsorber 对象以提取文本
    TextAbsorber absorber = new TextAbsorber();
    absorber.getTextSearchOptions().setLimitToPageBounds(true);
    absorber.getTextSearchOptions().setRectangle(new Rectangle(100, 200, 250, 350));
    // 接受第一页的吸收器
    doc.getPages().get_Item(1).accept(absorber);
    // 获取提取的文本
    String extractedText = absorber.getText();
    // 创建一个写入器并打开文件
    BufferedWriter writer = new BufferedWriter(new FileWriter(new java.io.File("ExtractedText.txt")));
    // 写入提取的内容
    writer.write(extractedText);
    // 关闭写入器
    writer.close();
}
```


### 第二种方法 - 使用 ScaleFactor

在这个新版本中，我们还在 TextAbsorber 和内部文本格式机制中引入了若干改进。因此，现在在使用“纯”模式进行文本提取时，您可以指定 ScaleFactor 选项，这可能是从多列 PDF 文档中提取文本的另一种方法，除了上述方法之外。此比例因子可以设置为调整网格，该网格用于文本提取期间的内部文本格式机制。指定的 ScaleFactor 值介于 1 和 0.1（包括 0.1）之间，其效果与缩小字体相同。

指定的 ScaleFactor 值在 0.1 和 -0.1 之间时被视为零值，但这会使算法在提取文本时自动计算所需的缩放因子。计算基于页面上最流行字体的平均字形宽度，但我们无法保证在提取的文本中没有列字符串达到下一列的开头。请注意，如果未指定 ScaleFactor 值，将使用默认值 1.0。这意味着不会进行缩放。如果指定的 ScaleFactor 值大于 10 或小于 -0.1，将使用默认值 1.0。

我们建议在处理大量 PDF 文件以提取文本内容时使用自动缩放（ScaleFactor = 0）。或者手动设置网格宽度的冗余减少（约 ScaleFactor = 0.5）。然而，您不必确定具体文档是否需要缩放。如果您为不需要的文档设置网格宽度的冗余减少，提取的文本内容将保持完全适当。请查看以下代码片段。

```java
public static void usingSetScaleFactorMethod() {
    Document pdfDocument = new Document("inputFile.pdf");
    TextAbsorber textAbsorber = new TextAbsorber();
    textAbsorber.setExtractionOptions(new TextExtractionOptions(TextExtractionOptions.TextFormattingMode.Pure));
    // 将缩放因子设置为0.5足以拆分大多数文档中的列
    // 设置为零允许算法自动选择缩放因子
    textAbsorber.getExtractionOptions().setScaleFactor((double) 0.5);
    pdfDocument.getPages().accept(textAbsorber);
    String extractedText = textAbsorber.getText();
}
```


{{% alert color="primary" %}}

请注意，新ScaleFactor与旧的手动字体缩小系数之间没有直接对应关系。然而，默认情况下，算法会考虑已经因某些内部原因而缩小的字体大小。例如，将字体大小从10缩小到7与设置缩放因子为5/8（= 0.625）具有相同的效果。

{{% /alert %}}

## 从PDF文档中提取高亮文本

在从PDF文档中提取文本的各种场景中，您可能会需要仅从PDF文档中提取高亮文本。为了实现该功能，我们在API中添加了TextMarkupAnnotation.GetMarkedText()和TextMarkupAnnotation.GetMarkedTextFragments()方法。您可以通过过滤TextMarkupAnnotation并使用上述方法从PDF文档中提取高亮文本。以下代码片段展示了如何从PDF文档中提取高亮文本。

```java
public static void ExtractHighlightedText() {
    Document doc = new Document(_dataDir + "ExtractHighlightedText.pdf");
    // 遍历所有注释
    for (Annotation annotation : doc.getPages().get_Item(1).getAnnotations())
    {
        // 过滤TextMarkupAnnotation
        if (annotation.getAnnotationType()==AnnotationType.Highlight)
        {
            HighlightAnnotation highlightedAnnotation = (HighlightAnnotation) annotation;
            // 检索高亮文本片段
            TextFragmentCollection collection = highlightedAnnotation.getMarkedTextFragments();
            for (TextFragment tf : collection)
            {
                // 显示高亮文本
                System.out.println(tf.getText());
            }
        }
    }        
}
```


## 访问 XML 中的文本片段和段元素

有时在处理从 XML 生成的 PDF 文档时，我们需要访问 TextFragment 或 TextSegment 项。Aspose.PDF for .NET 提供了按名称访问这些项的功能。下面的代码片段展示了如何使用此功能。

```java
public static void AccessTextFragmentAndSegmentElements() {
    String inXml = "40014.xml";        
    Document doc = new Document();
    doc.bindXml(_dataDir + inXml);

    TextSegment segment = (TextSegment) doc.getObjectById("boldHtml");
    segment = (TextSegment) doc.getObjectById("strongHtml");

    System.out.println(segment.getText());
    
}
```