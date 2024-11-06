---
title: 设置标记 PDF 中的结构元素属性
linktitle: 设置结构元素属性
type: docs
weight: 30
url: zh/java/set-tagged-pdfs-element-properties/
description: 使用 Aspose.PDF for Java，您可以设置不同的结构元素属性。有设置文本块结构元素、设置内联结构元素、将结构元素添加到元素中等。
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## 设置结构元素属性

为了在标记 PDF 文档中设置结构元素属性，Aspose.PDF 提供了 [ITaggedContent](https://reference.aspose.com/pdf/java/com.aspose.pdf.tagged/ITaggedContent) 接口的 **createSectElement()** 和 **createHeaderElement()** 方法。以下代码片段展示了如何设置标记 PDF 文档的结构元素属性：

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

// 创建结构元素
StructureElement rootElement = taggedContent.getRootElement();

SectElement sect = taggedContent.createSectElement();
rootElement.appendChild(sect);

HeaderElement h1 = taggedContent.createHeaderElement(1);
sect.appendChild(h1);
h1.setText("The Header");

h1.setTitle("Title");
h1.setLanguage("en-US");
h1.setAlternativeText("Alternative Text");
h1.setExpansionText("Expansion Text");
h1.setActualText("Actual Text");

// 保存标记的 Pdf 文档
document.save(path + "StructureElementsProperties.pdf");
```


## 设置文本结构元素

为了设置标记 PDF 文档的文本结构元素，Aspose.PDF 提供了 [ParagraphElement](https://reference.aspose.com/pdf/java/com.aspose.pdf.tagged.logicalstructure.elements.bls/class-use/ParagraphElement) 类。以下代码片段展示了如何设置标记 PDF 文档的文本结构元素：

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

// 获取根结构元素
StructureElement rootElement = taggedContent.getRootElement();

ParagraphElement p = taggedContent.createParagraphElement();
// 将文本设置为文本结构元素
p.setText("Paragraph.");
rootElement.appendChild(p);

// 保存标记的 Pdf 文档
document.save(path + "TextStructureElement.pdf");
```


## 设置文本块结构元素

为了设置标记 PDF 文档的文本块结构元素，Aspose.PDF 提供了 [HeaderElement](https://reference.aspose.com/pdf/java/com.aspose.pdf.tagged.logicalstructure.elements.bls.class-use/headerelement) 和 [ParagraphElement](https://reference.aspose.com/pdf/java/com.aspose.pdf.tagged.logicalstructure.elements.bls/class-use/ParagraphElement) 类。您可以将这些类的对象附加为 **StructureElement** 对象的子对象。以下代码片段显示了如何设置标记 PDF 文档的文本块结构元素：

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

// 获取根结构元素
StructureElement rootElement = taggedContent.getRootElement();

HeaderElement h1 = taggedContent.createHeaderElement(1);
HeaderElement h2 = taggedContent.createHeaderElement(2);
HeaderElement h3 = taggedContent.createHeaderElement(3);
HeaderElement h4 = taggedContent.createHeaderElement(4);
HeaderElement h5 = taggedContent.createHeaderElement(5);
HeaderElement h6 = taggedContent.createHeaderElement(6);
h1.setText("H1. 一级标题");
h2.setText("H2. 二级标题");
h3.setText("H3. 三级标题");
h4.setText("H4. 四级标题");
h5.setText("H5. 五级标题");
h6.setText("H6. 六级标题");
rootElement.appendChild(h1);
rootElement.appendChild(h2);
rootElement.appendChild(h3);
rootElement.appendChild(h4);
rootElement.appendChild(h5);
rootElement.appendChild(h6);

ParagraphElement p = taggedContent.createParagraphElement();
p.setText("P. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean nec lectus ac sem faucibus imperdiet. Sed ut erat ac magna ullamcorper hendrerit. Cras pellentesque libero semper, gravida magna sed, luctus leo. Fusce lectus odio, laoreet nec ullamcorper ut, molestie eu elit. Interdum et malesuada fames ac ante ipsum primis in faucibus. Aliquam lacinia sit amet elit ac consectetur. Donec cursus condimentum ligula, vitae volutpat sem tristique eget. Nulla in consectetur massa. Vestibulum vitae lobortis ante. Nulla ullamcorper pellentesque justo rhoncus accumsan. Mauris ornare eu odio non lacinia. Aliquam massa leo, rhoncus ac iaculis eget, tempus et magna. Sed non consectetur elit. Sed vulputate, quam sed lacinia luctus, ipsum nibh fringilla purus, vitae posuere risus odio id massa. Cras sed venenatis lacus.");
rootElement.appendChild(p);

// 保存标记的 Pdf 文档
document.save(path + "TextBlockStructureElements.pdf");
```


## 设置内联结构元素

为了设置标记 PDF 文档的内联结构元素，Aspose.PDF 提供了 [SpanElement](https://reference.aspose.com/pdf/java/com.aspose.pdf.tagged.logicalstructure.elements.ils/spanelement) 和 [ParagraphElement](https://reference.aspose.com/pdf/java/com.aspose.pdf.tagged.logicalstructure.elements.bls/class-use/ParagraphElement) 类。您可以将这些类的对象作为 **StructureElement** 对象的子元素附加。以下代码片段展示了如何设置标记 PDF 文档的内联结构元素：

```java
// 完整的示例和数据文件，请访问 https://github.com/aspose-pdf/Aspose.PDF-for-Java
// 文档目录的路径。
String path = "pathTodir";
// 创建 PDF 文档
Document document = new Document();

// 获取用于处理 TaggedPdf 的内容
ITaggedContent taggedContent = document.getTaggedContent();

// 设置文档的标题和语言
taggedContent.setTitle("Tagged Pdf Document");
taggedContent.setLanguage("en-US");

// 获取根结构元素
StructureElement rootElement = taggedContent.getRootElement();

HeaderElement h1 = taggedContent.createHeaderElement(1);
HeaderElement h2 = taggedContent.createHeaderElement(2);
HeaderElement h3 = taggedContent.createHeaderElement(3);
HeaderElement h4 = taggedContent.createHeaderElement(4);
HeaderElement h5 = taggedContent.createHeaderElement(5);
HeaderElement h6 = taggedContent.createHeaderElement(6);
rootElement.appendChild(h1);
rootElement.appendChild(h2);
rootElement.appendChild(h3);
rootElement.appendChild(h4);
rootElement.appendChild(h5);
rootElement.appendChild(h6);

SpanElement spanH11 = taggedContent.createSpanElement();
spanH11.setText("H1. ");
h1.appendChild(spanH11);
SpanElement spanH12 = taggedContent.createSpanElement();
spanH12.setText("第一级标题");
h1.appendChild(spanH12);

SpanElement spanH21 = taggedContent.createSpanElement();
spanH21.setText("H2. ");
h2.appendChild(spanH21);
SpanElement spanH22 = taggedContent.createSpanElement();
spanH22.setText("第二级标题");
h2.appendChild(spanH22);

SpanElement spanH31 = taggedContent.createSpanElement();
spanH31.setText("H3. ");
h3.appendChild(spanH31);
SpanElement spanH32 = taggedContent.createSpanElement();
spanH32.setText("第三级标题");
h3.appendChild(spanH32);

SpanElement spanH41 = taggedContent.createSpanElement();
spanH41.setText("H4. ");
h4.appendChild(spanH41);
SpanElement spanH42 = taggedContent.createSpanElement();
spanH42.setText("第四级标题");
h4.appendChild(spanH42);

SpanElement spanH51 = taggedContent.createSpanElement();
spanH51.setText("H5. ");
h5.appendChild(spanH51);
SpanElement spanH52 = taggedContent.createSpanElement();
spanH52.setText("第五级标题");
h5.appendChild(spanH52);

SpanElement spanH61 = taggedContent.createSpanElement();
spanH61.setText("H6. ");
h6.appendChild(spanH61);
SpanElement spanH62 = taggedContent.createSpanElement();
spanH62.setText("第六级标题");
h6.appendChild(spanH62);

ParagraphElement p = taggedContent.createParagraphElement();
p.setText("P. ");
rootElement.appendChild(p);
SpanElement span1 = taggedContent.createSpanElement();
span1.setText("Lorem ipsum dolor sit amet, consectetur adipiscing elit. ");
p.appendChild(span1);
SpanElement span2 = taggedContent.createSpanElement();
span2.setText("Aenean nec lectus ac sem faucibus imperdiet. ");
p.appendChild(span2);
SpanElement span3 = taggedContent.createSpanElement();
span3.setText("Sed ut erat ac magna ullamcorper hendrerit. ");
p.appendChild(span3);
SpanElement span4 = taggedContent.createSpanElement();
span4.setText("Cras pellentesque libero semper, gravida magna sed, luctus leo. ");
p.appendChild(span4);
SpanElement span5 = taggedContent.createSpanElement();
span5.setText("Fusce lectus odio, laoreet nec ullamcorper ut, molestie eu elit. ");
p.appendChild(span5);
SpanElement span6 = taggedContent.createSpanElement();
span6.setText("Interdum et malesuada fames ac ante ipsum primis in faucibus. ");
p.appendChild(span6);
SpanElement span7 = taggedContent.createSpanElement();
span7.setText("Aliquam lacinia sit amet elit ac consectetur. Donec cursus condimentum ligula, vitae volutpat sem tristique eget. ");
p.appendChild(span7);
SpanElement span8 = taggedContent.createSpanElement();
span8.setText("Nulla in consectetur massa. Vestibulum vitae lobortis ante. Nulla ullamcorper pellentesque justo rhoncus accumsan. ");
p.appendChild(span8);
SpanElement span9 = taggedContent.createSpanElement();
span9.setText("Mauris ornare eu odio non lacinia. Aliquam massa leo, rhoncus ac iaculis eget, tempus et magna. Sed non consectetur elit. ");
p.appendChild(span9);
SpanElement span10 = taggedContent.createSpanElement();
span10.setText("Sed vulputate, quam sed lacinia luctus, ipsum nibh fringilla purus, vitae posuere risus odio id massa. Cras sed venenatis lacus.");
p.appendChild(span10);

// 保存标记的 PDF 文档
document.save(path + "InlineStructureElements.pdf");
```


## 设置自定义标签名称

为了设置标记PDF文档元素的自定义标签名称，Aspose.PDF为元素提供了**setTag()**方法。以下代码片段展示了如何设置自定义标签名称：

```java
// 有关完整的示例和数据文件，请访问 https://github.com/aspose-pdf/Aspose.PDF-for-Java
// 文档目录的路径。
String path = "pathTodir";
// 创建 Pdf 文档
Document document = new Document();

// 获取用于处理标记PDF的内容
ITaggedContent taggedContent = document.getTaggedContent();

// 为文档设置标题和语言
taggedContent.setTitle("Tagged Pdf Document");
taggedContent.setLanguage("en-US");

// 创建逻辑结构元素
SectElement sect = taggedContent.createSectElement();
taggedContent.getRootElement().appendChild(sect);

ParagraphElement p1 = taggedContent.createParagraphElement();
ParagraphElement p2 = taggedContent.createParagraphElement();
ParagraphElement p3 = taggedContent.createParagraphElement();
ParagraphElement p4 = taggedContent.createParagraphElement();

p1.setText("P1. ");
p2.setText("P2. ");
p3.setText("P3. ");
p4.setText("P4. ");

p1.setTag("P1");
p2.setTag("Para");
p3.setTag("Para");
p4.setTag("Paragraph");

sect.appendChild(p1);
sect.appendChild(p2);
sect.appendChild(p3);
sect.appendChild(p4);

SpanElement span1 = taggedContent.createSpanElement();
SpanElement span2 = taggedContent.createSpanElement();
SpanElement span3 = taggedContent.createSpanElement();
SpanElement span4 = taggedContent.createSpanElement();

span1.setText("Span 1.");
span2.setText("Span 2.");
span3.setText("Span 3.");
span4.setText("Span 4.");

span1.setTag("SPAN");
span2.setTag("Sp");
span3.setTag("Sp");
span4.setTag("TheSpan");

p1.appendChild(span1);
p2.appendChild(span2);
p3.appendChild(span3);
p4.appendChild(span4);

// 保存标记PDF文档
document.save(path + "CustomTag.pdf");
```


## 添加结构元素到元素中

为了在标记的 PDF 文档中设置链接结构元素，Aspose.PDF 提供了 [ITaggedContent](https://reference.aspose.com/pdf/java/com.aspose.pdf.tagged/ITaggedContent) 接口的 **createLinkElement()** 方法。以下代码片段展示了如何在带有文本的标记 PDF 文档的段落中设置结构元素：

```java
// 有关完整的示例和数据文件，请访问 https://github.com/aspose-pdf/Aspose.PDF-for-Java
// 文档目录的路径。
String dataDir = Utils.getDataDir() + "TaggedPDFs\\";
String outFile = dataDir + "AddStructureElementIntoElement_Output.pdf";
String logFile = dataDir + "46144_log.xml";

// 创建文档并获取标记的 PDF 内容
Document document = new Document();
ITaggedContent taggedContent = document.getTaggedContent();

// 设置文档的标题和语种
taggedContent.setTitle("文本元素示例");
taggedContent.setLanguage("en-US");

// 获取根结构元素（文档结构元素）
StructureElement rootElement = taggedContent.getRootElement();

ParagraphElement p1 = taggedContent.createParagraphElement();
rootElement.appendChild(p1);
SpanElement span11 = taggedContent.createSpanElement();
span11.setText("Span_11");
SpanElement span12 = taggedContent.createSpanElement();
span12.setText(" 和 Span_12。");
p1.setText("段落包含 ");
p1.appendChild(span11);
p1.appendChild(span12);

ParagraphElement p2 = taggedContent.createParagraphElement();
rootElement.appendChild(p2);
SpanElement span21 = taggedContent.createSpanElement();
span21.setText("Span_21");
SpanElement span22 = taggedContent.createSpanElement();
span22.setText("Span_22。");
p2.appendChild(span21);
p2.setText(" 和 ");
p2.appendChild(span22);

ParagraphElement p3 = taggedContent.createParagraphElement();
rootElement.appendChild(p3);
SpanElement span31 = taggedContent.createSpanElement();
span31.setText("Span_31");
SpanElement span32 = taggedContent.createSpanElement();
span32.setText(" 和 Span_32");
p3.appendChild(span31);
p3.appendChild(span32);
p3.setText("。");

ParagraphElement p4 = taggedContent.createParagraphElement();
rootElement.appendChild(p4);
SpanElement span41 = taggedContent.createSpanElement();
SpanElement span411 = taggedContent.createSpanElement();
span411.setText("Span_411，");
span41.setText("Span_41，");
span41.appendChild(span411);
SpanElement span42 = taggedContent.createSpanElement();
SpanElement span421 = taggedContent.createSpanElement();
span421.setText("Span 421 和 ");
span42.appendChild(span421);
span42.setText("Span_42");
p4.appendChild(span41);
p4.appendChild(span42);
p4.setText("。");

// 保存标记的 PDF 文档
document.save(outFile);
```


## 设置注释结构元素

Aspose.PDF for Java API 还允许您在标记的 PDF 文档中添加 **NoteElement**。以下代码片段展示了如何在标记的 PDF 文档中添加注释元素：

```java
// 完整的示例和数据文件，请访问 https://github.com/aspose-pdf/Aspose.PDF-for-Java
// 文档目录的路径。
String dataDir = Utils.getDataDir() + "TaggedPDFs\\";
String outFile = dataDir + "CreateNoteStructureElement.pdf";
String logFile = dataDir + "45929_log.xml";

// 创建 Pdf 文档
Document document = new Document();
ITaggedContent taggedContent = document.getTaggedContent();

taggedContent.setTitle("注释元素示例");
taggedContent.setLanguage("en-US");

// 添加段落元素
ParagraphElement paragraph = taggedContent.createParagraphElement();
taggedContent.getRootElement().appendChild(paragraph);

// 添加注释元素
NoteElement note1 = taggedContent.createNoteElement();
paragraph.appendChild(note1);
note1.setText("自动生成 ID 的注释。");

// 添加注释元素
NoteElement note2 = taggedContent.createNoteElement();
paragraph.appendChild(note2);
note2.setText("ID = 'note_002' 的注释。");
note2.setId("note_002");

// 添加注释元素
NoteElement note3 = taggedContent.createNoteElement();
paragraph.appendChild(note3);
note3.setText("ID = 'note_003' 的注释。");
note3.setId("note_003");
// 保存标记的 Pdf 文档
document.save(outFile);
```