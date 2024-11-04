---
title: Aspose.PDF for Java 9.0.0 中的公共 API 更改
type: docs
weight: 30
url: /java/public-api-changes-in-aspose-pdf-for-java-9-0-0/
lastmod: "2022-01-27"
---

{{% alert color="primary" %}}

此页面列出了 Aspose.PDF for Java 9.0.0 中引入的公共 API 更改。它不仅包括新的和过时的公共方法，还包括对 Aspose.PDF for Java 背后行为的任何更改的描述，这些更改可能会影响现有代码。任何被视为回归并修改现有行为的行为尤其重要，并在此记录。

{{% /alert %}}

## 移动

com.aspose.pdf.Text.FontSourceCollection 移动到 com.aspose.pdf.FontSourceCollection

## 新增

- com.aspose.pdf.LoadFormat.MHT
- com.aspose.pdf.SoundSampleData
- com.aspose.pdf.SoundSampleDataEncodingFormat 
- com.aspose.security.impl.digests.Sha1
- com.aspose.security.impl.digests.Sha384 
- com.aspose.security.impl.digests.HashAlgorithm

## 更改的类

**com.aspose.pdf.facades.AForm**

添加:

- java.util.Map 获取按钮选项值(String fieldName)

**com.aspose.pdf.IForm**

新增:

- java.util.Map 获取按钮选项值(String fieldName)

**com.aspose.pdf.facades.PdfAnnotationEditor**

新增:

- void 导入注释(InputStream[] annotFileInputStream, int[] annotType)
- void 导入注释(InputStream[] annotFileInputStream)
- void 导出书签到XML(OutputStream output)
- void 使用XML导入书签(InputStream stream)

**com.aspose.pdf.facades.PdfFileSignature**

新增:

- InputStream 提取图像(String signName)
- InputStream 提取证书(String signName)

**com.aspose.pdf.ApsToPdfConverter**

新增:

- boolean 获取显示字段边框()
- void 设置显示字段边框(boolean value)

**com.aspose.pdf.DocumentInfo**

新增:

- String 获取捕捉()
- void 设置捕捉(String value)

**com.aspose.pdf.LevelFormat**

新增:

- float 获取后续行缩进()
- void 设置后续行缩进(float value)

**com.aspose.pdf.MarkupAnnotation**

新增:

- public MarkupAnnotation()

**com.aspose.pdf.TextAnnotation**

添加：

- public TextAnnotation()

**com.aspose.pdf.facades.PdfAnnotationEditor**

更改：

- void modifyAnnotations(int start, int end, Enum annotType, Annotation annotation) 改为 void modifyAnnotations(int start, int end, int annotType, Annotation annotation)
- IList extractAnnotations(int start, int end, String[] annotTypes) 改为 Iterable extractAnnotations(int start, int end, String[] annotTypes)
- ArrayList getAttachmentInfo() 改为 Iterable PdfExtractor.getAttachmentInfo()

**com.aspose.pdf.Field**

更改：

- void recalculate() 改为 boolean recalculate()

**com.aspose.pdf.TextState**

更改：

- boolean isFontSizeSet() 改为 boolean getIsFontSizeSet()
- void isFontSizeSet(boolean value) 改为 void setIsFontSizeSet(boolean value)

**com.aspose.pdf.BidiLine**

更改：

- static boolean hasRTLChar(String text) 改为 static boolean containsRTLChar(String text)

**com.aspose.pdf.Element**

更改：

- getStructureType() 内部化，类似于 .NET API。

- getgetAttributes() 内部化，类似于 .NET API。