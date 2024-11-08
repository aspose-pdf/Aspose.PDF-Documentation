---
title: 从 PDF 中提取标记内容
linktitle: 提取标记内容
type: docs
weight: 20
url: /zh/java/extract-tagged-content-from-tagged-pdfs/
description: 本文解释了如何使用 Aspose.PDF for Java 从 PDF 文档中提取标记内容
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## 获取标记的 PDF 内容

为了获取包含标记文本的 PDF 文档的内容，Aspose.PDF 提供了 [getTaggedContent()](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#getTaggedContent--) 方法，该方法属于 [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) 类。以下代码片段展示了如何获取包含标记文本的 PDF 文档的内容：

```java
// 完整的示例和数据文件，请访问 https://github.com/aspose-pdf/Aspose.PDF-for-Java
// 文档目录的路径。
String path = "pathTodir";

// 创建 Pdf 文档
Document document = new Document();

// 获取用于处理 TaggedPdf 的内容
ITaggedContent taggedContent = document.getTaggedContent();

//
// 处理标记的 Pdf 内容
//

// 设置文档的标题和语言
taggedContent.setTitle("Simple Tagged Pdf Document");
taggedContent.setLanguage("en-US");

// 保存标记的 Pdf 文档
document.save(path + "TaggedPDFContent.pdf");
```


## 获取根结构

为了获取标记 PDF 文档的根结构，Aspose.PDF 提供了 [getStructTreeRootElement](https://reference.aspose.com/pdf/java/com.aspose.pdf.tagged/ITaggedContent#getStructTreeRootElement--) 和 **getStructureElement()** 方法，通过 [ITaggedContent](https://reference.aspose.com/pdf/java/com.aspose.pdf.tagged/ITaggedContent) 接口实现。以下代码片段展示了如何获取标记 PDF 文档的根结构：

```java
// 有关完整的示例和数据文件，请访问 https://github.com/aspose-pdf/Aspose.PDF-for-Java
// 文档目录的路径。
String path = "pathTodir";
// 创建 Pdf 文档
Document document = new Document();

// 获取用于处理 TaggedPdf 的内容
ITaggedContent taggedContent = document.getTaggedContent();

// 设置文档的标题和语言
taggedContent.setTitle("Tagged Pdf Document");
taggedContent.setLanguage("en-US");

// 属性 StructTreeRootElement 和 RootElement 用于访问
// PDF 文档的 StructTreeRoot 对象和根结构元素（文档结构元素）。
StructTreeRootElement structTreeRootElement = taggedContent.getStructTreeRootElement();
StructureElement rootElement = taggedContent.getRootElement();
```


## 访问子元素

为了访问标记 PDF 文档的子元素，Aspose.PDF 提供了 **ElementList** 类。以下代码片段展示了如何访问标记 PDF 文档的子元素：

```java
// 有关完整的示例和数据文件，请访问 https://github.com/aspose-pdf/Aspose.PDF-for-Java
String path = "pathTodir";
// 打开 Pdf 文档
Document document = new Document( path +"StructureElements.pdf");

// 获取用于处理 TaggedPdf 的内容
ITaggedContent taggedContent = document.getTaggedContent();

// 访问根元素
ElementList elementList = taggedContent.getStructTreeRootElement().getChildElements();
for (Element element : elementList)
{
    if (element instanceof StructureElement)
    {
        StructureElement structureElement =  (StructureElement)element;

        // 获取属性
        String title = structureElement.getTitle();
        String language = structureElement.getLanguage();
        String actualText = structureElement.getActualText();
        String expansionText = structureElement.getExpansionText();
        String alternativeText = structureElement.getAlternativeText();
    }
}

// 访问根元素中第一个元素的子元素
elementList = taggedContent.getRootElement().getChildElements().get_Item(1).getChildElements();
for (Element element : elementList)
{
    if (element instanceof StructureElement)
    {
        StructureElement structureElement = (StructureElement)element;

        // 设置属性
        structureElement.setTitle("title");
        structureElement.setLanguage("fr-FR");
        structureElement.setActualText("actual text");
        structureElement.setExpansionText("exp");
        structureElement.setAlternativeText("alt");
    }
}

// 保存标记的 Pdf 文档
document.save( path +"AccessChildrenElements.pdf");
```