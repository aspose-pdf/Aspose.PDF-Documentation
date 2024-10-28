---

title: 从 PDF 文档中提取图表对象（外观）
type: docs
weight: 20
url: /java/extract-chart-objects/
description: 本节介绍如何使用 PdfExtractor 类从 PDF 中提取图表对象。
lastmod: "2021-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## 从 PDF 文档中提取图表对象（外观）

PDF 允许将页面内容分组为名为 **标记内容** 的元素。Adobe Acrobat 将它们显示为“容器”。图表对象放置在这样的对象中。我们在 PdfExtractor 类中引入了一个新方法 extractMarkedContentAsImages() 来提取这些对象。此方法将每个 **标记内容** 渲染为单独的图像。请注意，并不是所有的图表都完全放置在一个容器中。因此，一些图表将被部分保存为单独的图像。

请注意，将内容正确分组到容器是 PDF 文档设计者的责任。
 如果您希望获取包含标题或其他对象的图表，您应该编辑/创建将整个图表放置在一个容器中的PDF文档。

```java

//打开文档

Document document = new Document("sample.pdf");

//实例化 PdfExtractor

PdfExtractor pdfExtractor = new PdfExtractor();

//将图表对象提取为图像到文件夹中

pdfExtractor.extractMarkedContentAsImages(document.getPages().get_Item(1), "C:/Temp/Charts_page_1");

document.close();
```