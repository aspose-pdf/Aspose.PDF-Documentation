---
title: Aspose.PDF for Java 9.0.0 におけるパブリック API の変更
type: docs
weight: 30
url: /ja/java/public-api-changes-in-aspose-pdf-for-java-9-0-0/
lastmod: "2022-01-27"
---

{{% alert color="primary" %}}

このページでは、Aspose.PDF for Java 9.0.0 で導入されたパブリック API の変更を一覧表示します。新規および廃止されたパブリックメソッドだけでなく、Aspose.PDF for Java の裏で動作する動作の変更で既存のコードに影響を与える可能性のあるものについても説明します。回帰と見なされ、既存の動作を変更する可能性のある動作は特に重要であり、ここに文書化されています。

{{% /alert %}}

## 移動

com.aspose.pdf.Text.FontSourceCollection は com.aspose.pdf.FontSourceCollection に移動しました

## 追加

- com.aspose.pdf.LoadFormat.MHT
- com.aspose.pdf.SoundSampleData
- com.aspose.pdf.SoundSampleDataEncodingFormat
- com.aspose.security.impl.digests.Sha1
- com.aspose.security.impl.digests.Sha384
- com.aspose.security.impl.digests.HashAlgorithm

## 変更されたクラス

**com.aspose.pdf.facades.AForm**

追加:

- java.util.Map getButtonOptionValues(String fieldName)

**com.aspose.pdf.IForm**

追加:

- java.util.Map getButtonOptionValues(String fieldName)

**com.aspose.pdf.facades.PdfAnnotationEditor**

追加:

- void importAnnotations(InputStream[] annotFileInputStream, int[] annotType)
- void importAnnotations(InputStream[] annotFileInputStream)
- void exportBookmarksToXML(OutputStream output)
- void importBookmarksWithXML(InputStream stream)

**com.aspose.pdf.facades.PdfFileSignature**

追加:

- InputStream extractImage(String signName)
- InputStream extractCertificate(String signName)

**com.aspose.pdf.ApsToPdfConverter**

追加:

- boolean getShowFieldsBorders()
- void setShowFieldsBorders(boolean value)

**com.aspose.pdf.DocumentInfo**

追加:

- String getTrapped()
- void setTrapped(String value)

**com.aspose.pdf.LevelFormat**

追加:

- float getSubsequentLinesIndent()
- void setSubsequentLinesIndent(float value)

**com.aspose.pdf.MarkupAnnotation**

追加:

- public MarkupAnnotation()


**com.aspose.pdf.TextAnnotation**

追加:

- public TextAnnotation()

**com.aspose.pdf.facades.PdfAnnotationEditor**

変更:

- void modifyAnnotations(int start, int end, Enum annotType, Annotation annotation) が void modifyAnnotations(int start, int end, int annotType, Annotation annotation) に変更されました
- IList extractAnnotations(int start, int end, String[] annotTypes) が Iterable extractAnnotations(int start, int end, String[] annotTypes) に変更されました
- ArrayList getAttachmentInfo() が Iterable PdfExtractor.getAttachmentInfo() に変更されました

**com.aspose.pdf.Field**

変更:

- void recalculate() が boolean recalculate() に変更されました

**com.aspose.pdf.TextState**

変更:

- boolean isFontSizeSet() が boolean getIsFontSizeSet() に変更されました
- void isFontSizeSet(boolean value) が void setIsFontSizeSet(boolean value) に変更されました

**com.aspose.pdf.BidiLine**

変更:

- static boolean hasRTLChar(String text) が static boolean containsRTLChar(String text) に変更されました

**com.aspose.pdf.Element**

変更:

- getStructureType() は .NET API に類似して内部化されました。

- getgetAttributes() は .NET API に類似して内部化されました。