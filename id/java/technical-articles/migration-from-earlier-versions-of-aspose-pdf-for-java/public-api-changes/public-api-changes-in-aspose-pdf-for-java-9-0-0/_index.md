title: Perubahan API Publik di Aspose.PDF untuk Java 9.0.0
type: docs
weight: 30
url: /id/java/public-api-changes-in-aspose-pdf-for-java-9-0-0/
lastmod: "2022-01-27"
---

{{% alert color="primary" %}}

Halaman ini mencantumkan perubahan API publik yang diperkenalkan di Aspose.PDF untuk Java 9.0.0. Ini mencakup tidak hanya metode publik baru dan usang, tetapi juga deskripsi tentang perubahan perilaku di balik layar di Aspose.PDF untuk Java yang dapat mempengaruhi kode yang ada. Setiap perilaku yang diperkenalkan yang dapat dianggap sebagai regresi dan mengubah perilaku yang ada sangat penting dan didokumentasikan di sini.

{{% /alert %}}

## Dipindahkan

com.aspose.pdf.Text.FontSourceCollection dipindahkan ke com.aspose.pdf.FontSourceCollection

## Ditambahkan

- com.aspose.pdf.LoadFormat.MHT
- com.aspose.pdf.SoundSampleData
- com.aspose.pdf.SoundSampleDataEncodingFormat 
- com.aspose.security.impl.digests.Sha1
- com.aspose.security.impl.digests.Sha384 
- com.aspose.security.impl.digests.HashAlgorithm

## Kelas yang Diubah

**com.aspose.pdf.facades.AForm**

ditambahkan:


- java.util.Map getButtonOptionValues(String fieldName)

**com.aspose.pdf.IForm**

ditambahkan:

- java.util.Map getButtonOptionValues(String fieldName)

**com.aspose.pdf.facades.PdfAnnotationEditor**

ditambahkan:

- void importAnnotations(InputStream[] annotFileInputStream, int[] annotType)
- void importAnnotations(InputStream[] annotFileInputStream)
- void exportBookmarksToXML(OutputStream output)
- void importBookmarksWithXML(InputStream stream)

**com.aspose.pdf.facades.PdfFileSignature**

ditambahkan:

- InputStream extractImage(String signName)
- InputStream extractCertificate(String signName)

**com.aspose.pdf.ApsToPdfConverter**

ditambahkan:

- boolean getShowFieldsBorders()
- void setShowFieldsBorders(boolean value)

**com.aspose.pdf.DocumentInfo**

ditambahkan:

- String getTrapped()
- void setTrapped(String value)

**com.aspose.pdf.LevelFormat**

ditambahkan:

- float getSubsequentLinesIndent()
- void setSubsequentLinesIndent(float value)

**com.aspose.pdf.MarkupAnnotation**

ditambahkan:

- public MarkupAnnotation()


**com.aspose.pdf.TextAnnotation**

ditambahkan:

- public TextAnnotation()

**com.aspose.pdf.facades.PdfAnnotationEditor**

diubah:

- void modifyAnnotations(int start, int end, Enum annotType, Annotation annotation) diubah menjadi void modifyAnnotations(int start, int end, int annotType, Annotation annotation)
- IList extractAnnotations(int start, int end, String[] annotTypes) diubah menjadi Iterable extractAnnotations(int start, int end, String[] annotTypes)
- ArrayList getAttachmentInfo() diubah menjadi Iterable PdfExtractor.getAttachmentInfo()

**com.aspose.pdf.Field**

diubah:

- void recalculate() diubah menjadi boolean recalculate()

**com.aspose.pdf.TextState**

diubah:

- boolean isFontSizeSet() diubah menjadi boolean getIsFontSizeSet()
- void isFontSizeSet(boolean value) diubah menjadi void setIsFontSizeSet(boolean value)

**com.aspose.pdf.BidiLine**

diubah:

- static boolean hasRTLChar(String text) diubah menjadi static boolean containsRTLChar(String text)

**com.aspose.pdf.Element**

diubah:

- getStructureType() diinternalisasi mirip dengan .NET API.

- getgetAttributes() diinternalisasi mirip dengan .NET API.