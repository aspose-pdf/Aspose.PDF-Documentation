---
title: Mudanças na API Pública no Aspose.PDF para Java 9.0.0
type: docs
weight: 30
url: /pt/java/public-api-changes-in-aspose-pdf-for-java-9-0-0/
lastmod: "2022-01-27"
---

{{% alert color="primary" %}}

Esta página lista as mudanças na API pública introduzidas no Aspose.PDF para Java 9.0.0. Inclui não apenas novos métodos públicos e métodos obsoletos, mas também uma descrição de quaisquer alterações no comportamento nos bastidores no Aspose.PDF para Java que podem afetar o código existente. Qualquer comportamento introduzido que possa ser visto como uma regressão e modifique o comportamento existente é especialmente importante e está documentado aqui.

{{% /alert %}}

## Movido

com.aspose.pdf.Text.FontSourceCollection movido para com.aspose.pdf.FontSourceCollection

## Adicionado

- com.aspose.pdf.LoadFormat.MHT
- com.aspose.pdf.SoundSampleData
- com.aspose.pdf.SoundSampleDataEncodingFormat
- com.aspose.security.impl.digests.Sha1
- com.aspose.security.impl.digests.Sha384
- com.aspose.security.impl.digests.HashAlgorithm

## Classes Alteradas

**com.aspose.pdf.facades.AForm**

adicionado:

- java.util.Map getButtonOptionValues(String fieldName)

**com.aspose.pdf.IForm**

adicionado:

- java.util.Map getButtonOptionValues(String fieldName)

**com.aspose.pdf.facades.PdfAnnotationEditor**

adicionado:

- void importAnnotations(InputStream[] annotFileInputStream, int[] annotType)
- void importAnnotations(InputStream[] annotFileInputStream)
- void exportBookmarksToXML(OutputStream output)
- void importBookmarksWithXML(InputStream stream)

**com.aspose.pdf.facades.PdfFileSignature**

adicionado:

- InputStream extractImage(String signName)
- InputStream extractCertificate(String signName)

**com.aspose.pdf.ApsToPdfConverter**

adicionado:

- boolean getShowFieldsBorders()
- void setShowFieldsBorders(boolean value)

**com.aspose.pdf.DocumentInfo**

adicionado:

- String getTrapped()
- void setTrapped(String value)

**com.aspose.pdf.LevelFormat**

adicionado:

- float getSubsequentLinesIndent()
- void setSubsequentLinesIndent(float value)

**com.aspose.pdf.MarkupAnnotation**

adicionado:

- public MarkupAnnotation()


**com.aspose.pdf.TextAnnotation**

adicionado:

- public TextAnnotation()

**com.aspose.pdf.facades.PdfAnnotationEditor**

alterado:

- void modifyAnnotations(int start, int end, Enum annotType, Annotation annotation) alterado para void modifyAnnotations(int start, int end, int annotType, Annotation annotation)
- IList extractAnnotations(int start, int end, String[] annotTypes) alterado para Iterable extractAnnotations(int start, int end, String[] annotTypes)
- ArrayList getAttachmentInfo() alterado para Iterable PdfExtractor.getAttachmentInfo()

**com.aspose.pdf.Field**

alterado:

- void recalculate() alterado para boolean recalculate()

**com.aspose.pdf.TextState**

alterado:

- boolean isFontSizeSet() alterado para boolean getIsFontSizeSet()
- void isFontSizeSet(boolean value) alterado para void setIsFontSizeSet(boolean value)

**com.aspose.pdf.BidiLine**

alterado:

- static boolean hasRTLChar(String text) alterado para static boolean containsRTLChar(String text)

**com.aspose.pdf.Element**

alterado:

- getStructureType() é internalizado similar à API .NET.

- getgetAttributes() é internalizado similar à API .NET.