title: تغييرات واجهة برمجة التطبيقات العامة في Aspose.PDF لـ Java 9.0.0
type: docs
weight: 30
url: ar/java/public-api-changes-in-aspose-pdf-for-java-9-0-0/
lastmod: "2022-01-27"
---

{{% alert color="primary" %}}

تسرد هذه الصفحة تغييرات واجهة برمجة التطبيقات العامة التي تم تقديمها في Aspose.PDF لـ Java 9.0.0. لا يتضمن ذلك الطرق العامة الجديدة والمتقادمة فحسب، بل أيضًا وصف لأي تغييرات في السلوك وراء الكواليس في Aspose.PDF لـ Java والتي قد تؤثر على الكود الحالي. أي سلوك تم تقديمه يمكن رؤيته كتراجع ويعدل السلوك الحالي هو مهم بشكل خاص ويتم توثيقه هنا.

{{% /alert %}}

## نقل

تم نقل com.aspose.pdf.Text.FontSourceCollection إلى com.aspose.pdf.FontSourceCollection

## تمت الإضافة

- com.aspose.pdf.LoadFormat.MHT
- com.aspose.pdf.SoundSampleData
- com.aspose.pdf.SoundSampleDataEncodingFormat 
- com.aspose.security.impl.digests.Sha1
- com.aspose.security.impl.digests.Sha384 
- com.aspose.security.impl.digests.HashAlgorithm

## الفصول المتغيرة

**com.aspose.pdf.facades.AForm**

تمت الإضافة:


- java.util.Map getButtonOptionValues(String fieldName)

**com.aspose.pdf.IForm**

تمت الإضافة:

- java.util.Map getButtonOptionValues(String fieldName)

**com.aspose.pdf.facades.PdfAnnotationEditor**

تمت الإضافة:

- void importAnnotations(InputStream[] annotFileInputStream, int[] annotType)
- void importAnnotations(InputStream[] annotFileInputStream)
- void exportBookmarksToXML(OutputStream output)
- void importBookmarksWithXML(InputStream stream)

**com.aspose.pdf.facades.PdfFileSignature**

تمت الإضافة:

- InputStream extractImage(String signName)
- InputStream extractCertificate(String signName)

**com.aspose.pdf.ApsToPdfConverter**

تمت الإضافة:

- boolean getShowFieldsBorders()
- void setShowFieldsBorders(boolean value)

**com.aspose.pdf.DocumentInfo**

تمت الإضافة:

- String getTrapped()
- void setTrapped(String value)

**com.aspose.pdf.LevelFormat**

تمت الإضافة:

- float getSubsequentLinesIndent()
- void setSubsequentLinesIndent(float value)

**com.aspose.pdf.MarkupAnnotation**

تمت الإضافة:

- public MarkupAnnotation()

**com.aspose.pdf.TextAnnotation**

added:

- public TextAnnotation()

**com.aspose.pdf.facades.PdfAnnotationEditor**

تم التغيير:

- void modifyAnnotations(int start, int end, Enum annotType, Annotation annotation) تم تغييرها إلى void modifyAnnotations(int start, int end, int annotType, Annotation annotation)
- IList extractAnnotations(int start, int end, String[] annotTypes) تم تغييرها إلى Iterable extractAnnotations(int start, int end, String[] annotTypes)
- ArrayList getAttachmentInfo() تم تغييرها إلى Iterable PdfExtractor.getAttachmentInfo()

**com.aspose.pdf.Field**

تم التغيير:

- void recalculate() تم تغييرها إلى boolean recalculate()

**com.aspose.pdf.TextState**

تم التغيير:

- boolean isFontSizeSet() تم تغييرها إلى boolean getIsFontSizeSet()
- void isFontSizeSet(boolean value) تم تغييرها إلى void setIsFontSizeSet(boolean value)

**com.aspose.pdf.BidiLine**

تم التغيير:

- static boolean hasRTLChar(String text) تم تغييرها إلى static boolean containsRTLChar(String text)

**com.aspose.pdf.Element**

تم التغيير:

- getStructureType() أصبحت داخلية مشابهة لـ .NET API.

- getgetAttributes() أصبحت داخلية مشابهة لـ .NET API.