---
title: 创建带标签的PDF
linktitle: 创建带标签的PDF
type: docs
weight: 10
lastmod: "2021-06-05"
url: /zh/java/create-tagged-pdf-documents/
description: 本文解释了如何使用Aspose.PDF for Java以编程方式为带标签的PDF文档创建结构元素。
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## 创建结构元素

为了在带标签的PDF文档中创建结构元素，Aspose.PDF提供了使用[ITaggedContent](https://reference.aspose.com/pdf/java/com.aspose.pdf.tagged/ITaggedContent)接口创建结构元素的方法。以下代码片段展示了如何创建带标签的PDF的结构元素：

```java
// 有关完整的示例和数据文件，请访问https://github.com/aspose-pdf/Aspose.PDF-for-Java
// 文档目录的路径。
String path = "pathTodir";

// 创建PDF文档
Document document = new Document();

// 获取用于处理带标签PDF的内容
ITaggedContent taggedContent = document.getTaggedContent();

// 设置文档的标题和语言
taggedContent.setTitle("Tagged Pdf Document");
taggedContent.setLanguage("en-US");

// 创建分组元素
PartElement partElement = taggedContent.createPartElement();
ArtElement artElement = taggedContent.createArtElement();
SectElement sectElement = taggedContent.createSectElement();
DivElement divElement = taggedContent.createDivElement();
BlockQuoteElement blockQuoteElement = taggedContent.createBlockQuoteElement();
CaptionElement captionElement = taggedContent.createCaptionElement();
TOCElement tocElement = taggedContent.createTOCElement();
TOCIElement tociElement = taggedContent.createTOCIElement();
IndexElement indexElement = taggedContent.createIndexElement();
NonStructElement nonStructElement = taggedContent.createNonStructElement();
PrivateElement privateElement = taggedContent.createPrivateElement();

// 创建文本块级结构元素
ParagraphElement paragraphElement = taggedContent.createParagraphElement();
HeaderElement headerElement = taggedContent.createHeaderElement();
HeaderElement h1Element = taggedContent.createHeaderElement(1);

// 创建文本行内结构元素
SpanElement spanElement = taggedContent.createSpanElement();
QuoteElement quoteElement = taggedContent.createQuoteElement();
NoteElement noteElement = taggedContent.createNoteElement();

// 创建插图结构元素
FigureElement figureElement = taggedContent.createFigureElement();
FormulaElement formulaElement = taggedContent.createFormulaElement();

// 方法正在开发中
ListElement listElement = taggedContent.createListElement();
TableElement tableElement = taggedContent.createTableElement();
ReferenceElement referenceElement = taggedContent.createReferenceElement();
BibEntryElement bibEntryElement = taggedContent.createBibEntryElement();
CodeElement codeElement = taggedContent.createCodeElement();
LinkElement linkElement = taggedContent.createLinkElement();
AnnotElement annotElement = taggedContent.createAnnotElement();
RubyElement rubyElement = taggedContent.createRubyElement();
WarichuElement warichuElement = taggedContent.createWarichuElement();
FormElement formElement = taggedContent.createFormElement();

// 保存带标签的PDF文档
document.save(path + "StructureElements.pdf");
```


## 创建结构元素树

为了在标记的 PDF 文档中创建结构元素树，Aspose.PDF 提供了使用 [ITaggedContent](https://reference.aspose.com/pdf/java/com.aspose.pdf.tagged/ITaggedContent) 接口创建结构元素树的方法。以下代码片段展示了如何创建标记的 PDF 文档的结构元素树：

```java
// 有关完整的示例和数据文件，请访问 https://github.com/aspose-pdf/Aspose.PDF-for-Java
// 文档目录的路径。
String path = "pathTodir";
// 创建 PDF 文档
Document document = new Document();

// 获取用于处理 TaggedPdf 的内容
ITaggedContent taggedContent = document.getTaggedContent();

// 设置文档的标题和语言
taggedContent.setTitle("Tagged Pdf Document");
taggedContent.setLanguage("en-US");

// 获取根结构元素（文档）
StructureElement rootElement = taggedContent.getRootElement();

// 创建逻辑结构
SectElement sect1 = taggedContent.createSectElement();
rootElement.appendChild(sect1);

SectElement sect2 = taggedContent.createSectElement();
rootElement.appendChild(sect2);

DivElement div11 = taggedContent.createDivElement();
sect1.appendChild(div11);

DivElement div12 = taggedContent.createDivElement();
sect1.appendChild(div12);

ArtElement art21 = taggedContent.createArtElement();
sect2.appendChild(art21);

ArtElement art22 = taggedContent.createArtElement();
sect2.appendChild(art22);

DivElement div211 = taggedContent.createDivElement();
art21.appendChild(div211);

DivElement div212 = taggedContent.createDivElement();
art21.appendChild(div212);

DivElement div221 = taggedContent.createDivElement();
art22.appendChild(div221);

DivElement div222 = taggedContent.createDivElement();
art22.appendChild(div222);

SectElement sect3 = taggedContent.createSectElement();
rootElement.appendChild(sect3);

DivElement div31 = taggedContent.createDivElement();
sect3.appendChild(div31);

// 保存标记的 PDF 文档
document.save(path + "StructureElementsTree.pdf");
```


## 文本结构样式

为了在标记的 PDF 文档中设置文本结构的样式，Aspose.PDF 提供了 [StructureTextState](https://reference.aspose.com/pdf/java/com.aspose.pdf.tagged.logicalstructure.elements.class-use/StructureTextState) 类的 **setFont()**、**setFontSize()**、**setFontStyle()** 和 **setForegroundColor()** 属性。以下代码片段展示了如何在标记的 PDF 文档中设置文本结构的样式：

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

ParagraphElement p = taggedContent.createParagraphElement();
taggedContent.getRootElement().appendChild(p);

// 开发中
p.getStructureTextState().setFontSize(18F);
p.getStructureTextState().setForegroundColor(Color.getRed());
p.getStructureTextState().setFontStyle(FontStyles.Italic);

p.setText("红色斜体文本。");

// 保存标记的 Pdf 文档
document.save(path + "StyleTextStructure.pdf");
```


## 说明结构元素

为了在标记的 PDF 文档中说明结构元素，Aspose.PDF 提供了 [IllustrationElement](https://reference.aspose.com/pdf/java/com.aspose.pdf.tagged.logicalstructure.elements.class-use/IllustrationElement) 类。以下代码片段展示了如何在标记的 PDF 文档中说明结构元素：

```java
// 有关完整的示例和数据文件，请访问 https://github.com/aspose-pdf/Aspose.PDF-for-Java
// 文档目录的路径。
String path = "pathTodir";
// 创建 PDF 文档
Document document = new Document();

// 获取用于处理 TaggedPdf 的内容
ITaggedContent taggedContent = document.getTaggedContent();

// 为文档设置标题和语言
taggedContent.setTitle("Tagged Pdf Document");
taggedContent.setLanguage("en-US");

// 开发中
IllustrationElement figure1 = taggedContent.createFigureElement();
taggedContent.getRootElement().appendChild(figure1);
figure1.setActualText("图一");
figure1.setTitle("图片 1");
figure1.setTag("Fig1");
figure1.setImage("image.png");

// 保存标记的 PDF 文档
document.save(path + "IllustrationStructureElements.pdf");
```


## **使用标记图像创建 PDF**

为了使用标记图像创建 PDF，Aspose.PDF 提供了 [createFigureElement()](https://reference.aspose.com/pdf/java/com.aspose.pdf.tagged/ITaggedContent#createFigureElement--) 方法，该方法属于 [ITaggedContent](https://reference.aspose.com/pdf/java/com.aspose.pdf.tagged/ITaggedContent) 接口。以下代码片段展示了该功能。

```java
// 有关完整的示例和数据文件，请访问 https://github.com/aspose-pdf/Aspose.PDF-for-Java
Document document = new Document();
ITaggedContent taggedContent = document.getTaggedContent();

taggedContent.setTitle("CreatePDFwithTaggedImage");
taggedContent.setLanguage("en-US");

IllustrationElement figure1 = taggedContent.createFigureElement();
taggedContent.getRootElement().appendChild(figure1);
figure1.setAlternativeText("Aspose Logo");
figure1.setTitle("Image 1");
figure1.setTag("Fig");
// 添加分辨率为 300 DPI 的图像（默认值）
figure1.setImage("aspose-logo.jpg");
// 保存 PDF 文档
document.save("PDFwithTaggedImage.pdf");
```


## 创建带标记文本的 PDF

为了创建带标记文本的 PDF，Aspose.PDF 提供了 [ITaggedContent](https://reference.aspose.com/pdf/java/com.aspose.pdf.tagged/ITaggedContent) 接口。以下代码片段展示了该功能。

```java
// 有关完整的示例和数据文件，请访问 https://github.com/aspose-pdf/Aspose.PDF-for-Java
// 文档目录的路径。
String dataDir = Utils.getDataDir() + "TaggedPDFs\\";
// 创建 PDF 文档
Document document = new Document();

// 获取用于处理 TaggedPdf 的内容
ITaggedContent taggedContent = document.getTaggedContent();

// 设置文档的标题和语言
taggedContent.setTitle("带标记的 PDF 文档");
taggedContent.setLanguage("en-US");

// 创建文本块级结构元素
HeaderElement headerElement = taggedContent.createHeaderElement();
headerElement.setActualText("标题 1");
ParagraphElement paragraphElement1 = taggedContent.createParagraphElement();
paragraphElement1.setActualText("测试 1");
ParagraphElement paragraphElement2 = taggedContent.createParagraphElement();
paragraphElement2.setActualText("测试 2");
ParagraphElement paragraphElement3 = taggedContent.createParagraphElement();
paragraphElement3.setActualText("测试 3");
ParagraphElement paragraphElement4 = taggedContent.createParagraphElement();
paragraphElement4.setActualText("测试 4");
ParagraphElement paragraphElement5 = taggedContent.createParagraphElement();
paragraphElement5.setActualText("测试 5");
ParagraphElement paragraphElement6 = taggedContent.createParagraphElement();
paragraphElement6.setActualText("测试 6");
ParagraphElement paragraphElement7 = taggedContent.createParagraphElement();
paragraphElement7.setActualText("测试 7");

// 保存 PDF 文档
document.save( dataDir + "PDFwithTaggedText.pdf");
```