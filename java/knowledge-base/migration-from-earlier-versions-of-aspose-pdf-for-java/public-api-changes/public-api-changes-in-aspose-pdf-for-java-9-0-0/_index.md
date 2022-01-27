---
title: Public API Changes in Aspose.PDF for Java 9.0.0
type: docs
weight: 30
url: /java/public-api-changes-in-aspose-pdf-for-java-9-0-0/
lastmod: "2022-01-27"
---

{{% alert color="primary" %}}

This page lists the public API changes introduced in Aspose.PDF for Java 9.0.0. It includes not only new and obsoleted public methods, but also a description of any changes in the behavior behind the scenes in Aspose.PDF for Java which may affect existing code. Any behavior introduced that could be seen as a regression and modifies existing behavior is especially important and is documented here.

{{% /alert %}}

## Moved

com.aspose.pdf.Text.FontSourceCollection moved to com.aspose.pdf.FontSourceCollection 

## Added

- com.aspose.pdf.LoadFormat.MHT
- com.aspose.pdf.SoundSampleData
- com.aspose.pdf.SoundSampleDataEncodingFormat 
- com.aspose.security.impl.digests.Sha1
- com.aspose.security.impl.digests.Sha384 
- com.aspose.security.impl.digests.HashAlgorithm

## Changed Classes

**com.aspose.pdf.facades.AForm**

added:

- java.util.Map getButtonOptionValues(String fieldName)

**com.aspose.pdf.IForm**

added:

- java.util.Map getButtonOptionValues(String fieldName)

**com.aspose.pdf.facades.PdfAnnotationEditor**

added:

- void importAnnotations(InputStream[] annotFileInputStream, int[] annotType)
- void importAnnotations(InputStream[] annotFileInputStream)
- void exportBookmarksToXML(OutputStream output)
- void importBookmarksWithXML(InputStream stream)

**com.aspose.pdf.facades.PdfFileSignature**

added:

- InputStream extractImage(String signName)
- InputStream extractCertificate(String signName)

**com.aspose.pdf.ApsToPdfConverter**

added:

- boolean getShowFieldsBorders()
- void setShowFieldsBorders(boolean value)

**com.aspose.pdf.DocumentInfo**

added:

- String getTrapped()
- void setTrapped(String value)

**com.aspose.pdf.LevelFormat**

added:

- float getSubsequentLinesIndent()
- void setSubsequentLinesIndent(float value)

**com.aspose.pdf.MarkupAnnotation**

added:

- public MarkupAnnotation()

**com.aspose.pdf.TextAnnotation**

added:

- public TextAnnotation()

**com.aspose.pdf.facades.PdfAnnotationEditor**

changed:

- void modifyAnnotations(int start, int end, Enum annotType, Annotation annotation) changed to void modifyAnnotations(int start, int end, int annotType, Annotation annotation)
- IList extractAnnotations(int start, int end, String[] annotTypes) changed to Iterable extractAnnotations(int start, int end, String[] annotTypes)
- ArrayList getAttachmentInfo() changed to Iterable PdfExtractor.getAttachmentInfo()

**com.aspose.pdf.Field**

changed:

- void recalculate() changed to boolean recalculate()

**com.aspose.pdf.TextState**

changed:

- boolean isFontSizeSet() changed to boolean getIsFontSizeSet()
- void isFontSizeSet(boolean value) changed to void setIsFontSizeSet(boolean value)

**com.aspose.pdf.BidiLine**

changed:

- static boolean hasRTLChar(String text) changed to static boolean containsRTLChar(String text)

**com.aspose.pdf.Element**

changed:

- getStructureType() is internalized similar to the .NET API.
- getgetAttributes() is internalized similar to .NET API.
