---
title: Aspose.PDF for Java 9.0.0의 공개 API 변경 사항
type: docs
weight: 30
url: ko/java/public-api-changes-in-aspose-pdf-for-java-9-0-0/
lastmod: "2022-01-27"
---

{{% alert color="primary" %}}

이 페이지는 Aspose.PDF for Java 9.0.0에서 도입된 공개 API 변경 사항을 나열합니다. 새로운 공개 메서드와 사용되지 않는 메서드뿐만 아니라 기존 코드를 영향을 미칠 수 있는 Aspose.PDF for Java의 동작 변경 사항에 대한 설명도 포함되어 있습니다. 회귀로 볼 수 있는 동작이 도입되어 기존 동작을 수정하는 경우 특히 중요하며 여기에 문서화됩니다.

{{% /alert %}}

## 이동됨

com.aspose.pdf.Text.FontSourceCollection이 com.aspose.pdf.FontSourceCollection으로 이동

## 추가됨

- com.aspose.pdf.LoadFormat.MHT
- com.aspose.pdf.SoundSampleData
- com.aspose.pdf.SoundSampleDataEncodingFormat
- com.aspose.security.impl.digests.Sha1
- com.aspose.security.impl.digests.Sha384
- com.aspose.security.impl.digests.HashAlgorithm

## 변경된 클래스

**com.aspose.pdf.facades.AForm**

추가됨:

- java.util.Map getButtonOptionValues(String fieldName)

**com.aspose.pdf.IForm**

추가됨:

- java.util.Map getButtonOptionValues(String fieldName)

**com.aspose.pdf.facades.PdfAnnotationEditor**

추가됨:

- void importAnnotations(InputStream[] annotFileInputStream, int[] annotType)
- void importAnnotations(InputStream[] annotFileInputStream)
- void exportBookmarksToXML(OutputStream output)
- void importBookmarksWithXML(InputStream stream)

**com.aspose.pdf.facades.PdfFileSignature**

추가됨:

- InputStream extractImage(String signName)
- InputStream extractCertificate(String signName)

**com.aspose.pdf.ApsToPdfConverter**

추가됨:

- boolean getShowFieldsBorders()
- void setShowFieldsBorders(boolean value)

**com.aspose.pdf.DocumentInfo**

추가됨:

- String getTrapped()
- void setTrapped(String value)

**com.aspose.pdf.LevelFormat**

추가됨:

- float getSubsequentLinesIndent()
- void setSubsequentLinesIndent(float value)

**com.aspose.pdf.MarkupAnnotation**

추가됨:

- public MarkupAnnotation()


**com.aspose.pdf.TextAnnotation**

추가됨:

- public TextAnnotation()

**com.aspose.pdf.facades.PdfAnnotationEditor**

변경됨:

- void modifyAnnotations(int start, int end, Enum annotType, Annotation annotation) 이 void modifyAnnotations(int start, int end, int annotType, Annotation annotation)로 변경됨
- IList extractAnnotations(int start, int end, String[] annotTypes) 이 Iterable extractAnnotations(int start, int end, String[] annotTypes)로 변경됨
- ArrayList getAttachmentInfo() 이 Iterable PdfExtractor.getAttachmentInfo()로 변경됨

**com.aspose.pdf.Field**

변경됨:

- void recalculate() 이 boolean recalculate()로 변경됨

**com.aspose.pdf.TextState**

변경됨:

- boolean isFontSizeSet() 이 boolean getIsFontSizeSet()로 변경됨
- void isFontSizeSet(boolean value) 이 void setIsFontSizeSet(boolean value)로 변경됨

**com.aspose.pdf.BidiLine**

변경됨:

- static boolean hasRTLChar(String text) 이 static boolean containsRTLChar(String text)로 변경됨

**com.aspose.pdf.Element**

변경됨:

- getStructureType()는 .NET API와 유사하게 내부화됨.

- getgetAttributes()는 .NET API와 유사하게 내부화됨.