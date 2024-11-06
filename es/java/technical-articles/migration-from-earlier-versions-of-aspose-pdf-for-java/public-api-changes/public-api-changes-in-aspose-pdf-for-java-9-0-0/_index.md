---
title: Cambios en la API Pública en Aspose.PDF para Java 9.0.0
type: docs
weight: 30
url: es/java/public-api-changes-in-aspose-pdf-for-java-9-0-0/
lastmod: "2022-01-27"
---

{{% alert color="primary" %}}

Esta página enumera los cambios en la API pública introducidos en Aspose.PDF para Java 9.0.0. Incluye no solo métodos públicos nuevos y obsoletos, sino también una descripción de cualquier cambio en el comportamiento detrás de escena en Aspose.PDF para Java que pueda afectar el código existente. Cualquier comportamiento introducido que pueda ser visto como una regresión y modifique el comportamiento existente es especialmente importante y está documentado aquí.

{{% /alert %}}

## Movido

com.aspose.pdf.Text.FontSourceCollection movido a com.aspose.pdf.FontSourceCollection

## Añadido

- com.aspose.pdf.LoadFormat.MHT
- com.aspose.pdf.SoundSampleData
- com.aspose.pdf.SoundSampleDataEncodingFormat 
- com.aspose.security.impl.digests.Sha1
- com.aspose.security.impl.digests.Sha384 
- com.aspose.security.impl.digests.HashAlgorithm

## Clases Cambiadas

**com.aspose.pdf.facades.AForm**

añadido:

- java.util.Map getButtonOptionValues(String fieldName)

**com.aspose.pdf.IForm**

añadido:

- java.util.Map getButtonOptionValues(String fieldName)

**com.aspose.pdf.facades.PdfAnnotationEditor**

añadido:

- void importAnnotations(InputStream[] annotFileInputStream, int[] annotType)
- void importAnnotations(InputStream[] annotFileInputStream)
- void exportBookmarksToXML(OutputStream output)
- void importBookmarksWithXML(InputStream stream)

**com.aspose.pdf.facades.PdfFileSignature**

añadido:

- InputStream extractImage(String signName)
- InputStream extractCertificate(String signName)

**com.aspose.pdf.ApsToPdfConverter**

añadido:

- boolean getShowFieldsBorders()
- void setShowFieldsBorders(boolean value)

**com.aspose.pdf.DocumentInfo**

añadido:

- String getTrapped()
- void setTrapped(String value)

**com.aspose.pdf.LevelFormat**

añadido:

- float getSubsequentLinesIndent()
- void setSubsequentLinesIndent(float value)

**com.aspose.pdf.MarkupAnnotation**

añadido:

- public MarkupAnnotation()

**com.aspose.pdf.TextAnnotation**

añadido:

- public TextAnnotation()

**com.aspose.pdf.facades.PdfAnnotationEditor**

cambiado:

- void modifyAnnotations(int start, int end, Enum annotType, Annotation annotation) cambiado a void modifyAnnotations(int start, int end, int annotType, Annotation annotation)
- IList extractAnnotations(int start, int end, String[] annotTypes) cambiado a Iterable extractAnnotations(int start, int end, String[] annotTypes)
- ArrayList getAttachmentInfo() cambiado a Iterable PdfExtractor.getAttachmentInfo()

**com.aspose.pdf.Field**

cambiado:

- void recalculate() cambiado a boolean recalculate()

**com.aspose.pdf.TextState**

cambiado:

- boolean isFontSizeSet() cambiado a boolean getIsFontSizeSet()
- void isFontSizeSet(boolean value) cambiado a void setIsFontSizeSet(boolean value)

**com.aspose.pdf.BidiLine**

cambiado:

- static boolean hasRTLChar(String text) cambiado a static boolean containsRTLChar(String text)

**com.aspose.pdf.Element**

cambiado:

- getStructureType() es internalizado de manera similar a la API de .NET.

- getgetAttributes() es internalizado de manera similar a la API de .NET.