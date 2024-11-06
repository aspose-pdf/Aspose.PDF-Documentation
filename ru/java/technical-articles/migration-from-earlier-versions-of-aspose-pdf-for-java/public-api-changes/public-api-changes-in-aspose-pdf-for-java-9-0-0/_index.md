title: Public API Changes in Aspose.PDF for Java 9.0.0
type: docs
weight: 30
url: ru/java/public-api-changes-in-aspose-pdf-for-java-9-0-0/
lastmod: "2022-01-27"
---

{{% alert color="primary" %}}

На этой странице перечислены изменения в публичном API, введенные в Aspose.PDF for Java 9.0.0. Они включают не только новые и устаревшие публичные методы, но и описание любых изменений в поведении под капотом в Aspose.PDF for Java, которые могут повлиять на существующий код. Любое поведение, которое может рассматриваться как регрессия и модифицирует существующее поведение, особенно важно и документировано здесь.

{{% /alert %}}

## Перемещено

com.aspose.pdf.Text.FontSourceCollection перемещен в com.aspose.pdf.FontSourceCollection

## Добавлено

- com.aspose.pdf.LoadFormat.MHT
- com.aspose.pdf.SoundSampleData
- com.aspose.pdf.SoundSampleDataEncodingFormat
- com.aspose.security.impl.digests.Sha1
- com.aspose.security.impl.digests.Sha384
- com.aspose.security.impl.digests.HashAlgorithm

## Измененные классы

**com.aspose.pdf.facades.AForm**

добавлено:


- java.util.Map получитьЗначенияОпцийКнопки(String fieldName)

**com.aspose.pdf.IForm**

добавлено:

- java.util.Map получитьЗначенияОпцийКнопки(String fieldName)

**com.aspose.pdf.facades.PdfAnnotationEditor**

добавлено:

- void импортироватьАннотации(InputStream[] annotFileInputStream, int[] annotType)
- void импортироватьАннотации(InputStream[] annotFileInputStream)
- void экспортироватьЗакладкиВXML(OutputStream output)
- void импортироватьЗакладкиСXML(InputStream stream)

**com.aspose.pdf.facades.PdfFileSignature**

добавлено:

- InputStream извлечьИзображение(String signName)
- InputStream извлечьСертификат(String signName)

**com.aspose.pdf.ApsToPdfConverter**

добавлено:

- boolean показатьГраницыПолей()
- void установитьПоказГраницПолей(boolean value)

**com.aspose.pdf.DocumentInfo**

добавлено:

- String получитьПойманный()
- void установитьПойманный(String value)

**com.aspose.pdf.LevelFormat**

добавлено:

- float получитьОтступПоследующихСтрок()
- void установитьОтступПоследующихСтрок(float value)

**com.aspose.pdf.MarkupAnnotation**

добавлено:

- public MarkupAnnotation()


**com.aspose.pdf.TextAnnotation**

added:

- public TextAnnotation()

**com.aspose.pdf.facades.PdfAnnotationEditor**

изменено:

- void modifyAnnotations(int start, int end, Enum annotType, Annotation annotation) изменено на void modifyAnnotations(int start, int end, int annotType, Annotation annotation)
- IList extractAnnotations(int start, int end, String[] annotTypes) изменено на Iterable extractAnnotations(int start, int end, String[] annotTypes)
- ArrayList getAttachmentInfo() изменено на Iterable PdfExtractor.getAttachmentInfo()

**com.aspose.pdf.Field**

изменено:

- void recalculate() изменено на boolean recalculate()

**com.aspose.pdf.TextState**

изменено:

- boolean isFontSizeSet() изменено на boolean getIsFontSizeSet()
- void isFontSizeSet(boolean value) изменено на void setIsFontSizeSet(boolean value)

**com.aspose.pdf.BidiLine**

изменено:

- static boolean hasRTLChar(String text) изменено на static boolean containsRTLChar(String text)

**com.aspose.pdf.Element**

изменено:

- getStructureType() интегрировано аналогично .NET API.

- getgetAttributes() интегрировано аналогично .NET API.