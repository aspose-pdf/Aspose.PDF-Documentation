---
title: Modifications de l'API Publique dans Aspose.PDF pour Java 9.0.0
type: docs
weight: 30
url: /fr/java/public-api-changes-in-aspose-pdf-for-java-9-0-0/
lastmod: "2022-01-27"
---

{{% alert color="primary" %}}

Cette page répertorie les modifications de l'API publique introduites dans Aspose.PDF pour Java 9.0.0. Elle inclut non seulement les méthodes publiques nouvelles et obsolètes, mais aussi une description de tout changement dans le comportement en coulisses dans Aspose.PDF pour Java qui pourrait affecter le code existant. Tout comportement introduit qui pourrait être perçu comme une régression et qui modifie le comportement existant est particulièrement important et est documenté ici.

{{% /alert %}}

## Déplacé

com.aspose.pdf.Text.FontSourceCollection déplacé vers com.aspose.pdf.FontSourceCollection

## Ajouté

- com.aspose.pdf.LoadFormat.MHT
- com.aspose.pdf.SoundSampleData
- com.aspose.pdf.SoundSampleDataEncodingFormat
- com.aspose.security.impl.digests.Sha1
- com.aspose.security.impl.digests.Sha384
- com.aspose.security.impl.digests.HashAlgorithm

## Classes Modifiées

**com.aspose.pdf.facades.AForm**

ajouté:

- java.util.Map getButtonOptionValues(String fieldName)

**com.aspose.pdf.IForm**

ajouté :

- java.util.Map getButtonOptionValues(String fieldName)

**com.aspose.pdf.facades.PdfAnnotationEditor**

ajouté :

- void importAnnotations(InputStream[] annotFileInputStream, int[] annotType)
- void importAnnotations(InputStream[] annotFileInputStream)
- void exportBookmarksToXML(OutputStream output)
- void importBookmarksWithXML(InputStream stream)

**com.aspose.pdf.facades.PdfFileSignature**

ajouté :

- InputStream extractImage(String signName)
- InputStream extractCertificate(String signName)

**com.aspose.pdf.ApsToPdfConverter**

ajouté :

- boolean getShowFieldsBorders()
- void setShowFieldsBorders(boolean value)

**com.aspose.pdf.DocumentInfo**

ajouté :

- String getTrapped()
- void setTrapped(String value)

**com.aspose.pdf.LevelFormat**

ajouté :

- float getSubsequentLinesIndent()
- void setSubsequentLinesIndent(float value)

**com.aspose.pdf.MarkupAnnotation**

ajouté :

- public MarkupAnnotation()


**com.aspose.pdf.TextAnnotation**

ajouté :

- public TextAnnotation()

**com.aspose.pdf.facades.PdfAnnotationEditor**

modifié :

- void modifyAnnotations(int start, int end, Enum annotType, Annotation annotation) changé en void modifyAnnotations(int start, int end, int annotType, Annotation annotation)
- IList extractAnnotations(int start, int end, String[] annotTypes) changé en Iterable extractAnnotations(int start, int end, String[] annotTypes)
- ArrayList getAttachmentInfo() changé en Iterable PdfExtractor.getAttachmentInfo()

**com.aspose.pdf.Field**

modifié :

- void recalculate() changé en boolean recalculate()

**com.aspose.pdf.TextState**

modifié :

- boolean isFontSizeSet() changé en boolean getIsFontSizeSet()
- void isFontSizeSet(boolean value) changé en void setIsFontSizeSet(boolean value)

**com.aspose.pdf.BidiLine**

modifié :

- static boolean hasRTLChar(String text) changé en static boolean containsRTLChar(String text)

**com.aspose.pdf.Element**

modifié :

- getStructureType() est internalisé de manière similaire à l'API .NET.

- getgetAttributes() est internalisé de manière similaire à l'API .NET.