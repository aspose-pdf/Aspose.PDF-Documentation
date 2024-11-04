---
title: إنشاء PDF مع علامات
linktitle: إنشاء PDF مع علامات
type: docs
weight: 10
lastmod: "2021-06-05"
url: /java/create-tagged-pdf-documents/
description: يوضح هذا المقال كيفية إنشاء عناصر الهيكل لوثيقة PDF مع علامات برمجيًا باستخدام Aspose.PDF for Java.
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## إنشاء عناصر الهيكل

من أجل إنشاء عناصر الهيكل في مستند PDF مع علامات، يوفر Aspose.PDF طرقًا لإنشاء عنصر هيكل باستخدام واجهة [ITaggedContent](https://reference.aspose.com/pdf/java/com.aspose.pdf.tagged/ITaggedContent). يُظهر مقتطف الكود التالي كيفية إنشاء عناصر الهيكل لوثيقة PDF مع علامات:

```java
// للحصول على أمثلة كاملة وملفات البيانات، يرجى زيارة https://github.com/aspose-pdf/Aspose.PDF-for-Java
// المسار إلى دليل المستندات.
String path = "pathTodir";

// إنشاء مستند PDF
Document document = new Document();

// الحصول على المحتوى للعمل مع TaggedPdf
ITaggedContent taggedContent = document.getTaggedContent();

// تعيين العنوان واللغة للمستند
taggedContent.setTitle("Tagged Pdf Document");
taggedContent.setLanguage("en-US");

// إنشاء عناصر تجمع
PartElement partElement = taggedContent.createPartElement();
ArtElement artElement = taggedContent.createArtElement();
SectElement sectElement = taggedContent.createSectElement();
DivElement divElement = taggedContent.createDivElement();
BlockQuoteElement blockQuoteElement = taggedContent.createBlockQuoteElement();
CaptionElement captionElement = taggedContent.createCaptionElement();
TOCElement tocElement = taggedContent.createTOCElement();
TOCIElement tociElement = taggedContent.createTOCIElement();
IndexElement indexElement = taggedContent.createIndexElement();
NonStructElement nonStructElement = taggedContent.createNonStructElement();
PrivateElement privateElement = taggedContent.createPrivateElement();

// إنشاء عناصر هيكل النص على مستوى الكتلة
ParagraphElement paragraphElement = taggedContent.createParagraphElement();
HeaderElement headerElement = taggedContent.createHeaderElement();
HeaderElement h1Element = taggedContent.createHeaderElement(1);

// إنشاء عناصر هيكل النص على مستوى السطر
SpanElement spanElement = taggedContent.createSpanElement();
QuoteElement quoteElement = taggedContent.createQuoteElement();
NoteElement noteElement = taggedContent.createNoteElement();

// إنشاء عناصر هيكل التوضيح
FigureElement figureElement = taggedContent.createFigureElement();
FormulaElement formulaElement = taggedContent.createFormulaElement();

// الطرق قيد التطوير
ListElement listElement = taggedContent.createListElement();
TableElement tableElement = taggedContent.createTableElement();
ReferenceElement referenceElement = taggedContent.createReferenceElement();
BibEntryElement bibEntryElement = taggedContent.createBibEntryElement();
CodeElement codeElement = taggedContent.createCodeElement();
LinkElement linkElement = taggedContent.createLinkElement();
AnnotElement annotElement = taggedContent.createAnnotElement();
RubyElement rubyElement = taggedContent.createRubyElement();
WarichuElement warichuElement = taggedContent.createWarichuElement();
FormElement formElement = taggedContent.createFormElement();

// حفظ مستند Tagged Pdf
document.save(path + "StructureElements.pdf");
```


## إنشاء شجرة عناصر الهيكل

من أجل إنشاء شجرة عناصر الهيكل في مستند PDF مميز بالعلامات، توفر Aspose.PDF طرقًا لإنشاء شجرة عناصر الهيكل باستخدام واجهة [ITaggedContent](https://reference.aspose.com/pdf/java/com.aspose.pdf.tagged/ITaggedContent). يوضح مقتطف الشيفرة التالي كيفية إنشاء شجرة عناصر الهيكل لمستند PDF مميز بالعلامات:

```java
// للحصول على أمثلة كاملة وملفات البيانات، يرجى زيارة https://github.com/aspose-pdf/Aspose.PDF-for-Java
// المسار إلى دليل المستندات.
String path = "pathTodir";
// إنشاء مستند PDF
Document document = new Document();

// الحصول على المحتوى للعمل مع TaggedPdf
ITaggedContent taggedContent = document.getTaggedContent();

// تعيين عنوان ولغة للمستند
taggedContent.setTitle("Tagged Pdf Document");
taggedContent.setLanguage("en-US");

// الحصول على عنصر الهيكل الجذري (المستند)
StructureElement rootElement = taggedContent.getRootElement();

// إنشاء هيكل منطقي
SectElement sect1 = taggedContent.createSectElement();
rootElement.appendChild(sect1);

SectElement sect2 = taggedContent.createSectElement();
rootElement.appendChild(sect2);

DivElement div11 = taggedContent.createDivElement();
sect1.appendChild(div11);

DivElement div12 = taggedContent.createDivElement();
sect1.appendChild(div12);

ArtElement art21 = taggedContent.createArtElement();
sect2.appendChild(art21);

ArtElement art22 = taggedContent.createArtElement();
sect2.appendChild(art22);

DivElement div211 = taggedContent.createDivElement();
art21.appendChild(div211);

DivElement div212 = taggedContent.createDivElement();
art21.appendChild(div212);

DivElement div221 = taggedContent.createDivElement();
art22.appendChild(div221);

DivElement div222 = taggedContent.createDivElement();
art22.appendChild(div222);

SectElement sect3 = taggedContent.createSectElement();
rootElement.appendChild(sect3);

DivElement div31 = taggedContent.createDivElement();
sect3.appendChild(div31);

// حفظ مستند PDF مميز بالعلامات
document.save(path + "StructureElementsTree.pdf");
```


## تنسيق هيكل النص

من أجل تنسيق هيكل النص في مستند PDF موسوم، تقدم Aspose.PDF خصائص **setFont()**، **setFontSize()**، **setFontStyle()** و**setForegroundColor()** من فئة [StructureTextState](https://reference.aspose.com/pdf/java/com.aspose.pdf.tagged.logicalstructure.elements.class-use/StructureTextState). يظهر مقطع الشيفرة التالي كيفية تنسيق هيكل النص في مستند PDF موسوم:

```java
// للحصول على أمثلة كاملة وملفات البيانات، يرجى الذهاب إلى https://github.com/aspose-pdf/Aspose.PDF-for-Java
// المسار إلى دليل المستندات.
String path = "pathTodir";
// إنشاء مستند PDF
Document document = new Document();

// الحصول على المحتوى للعمل مع TaggedPdf
ITaggedContent taggedContent = document.getTaggedContent();

// تعيين العنوان واللغة للمستند
taggedContent.setTitle("Tagged Pdf Document");
taggedContent.setLanguage("en-US");

ParagraphElement p = taggedContent.createParagraphElement();
taggedContent.getRootElement().appendChild(p);

// تحت التطوير
p.getStructureTextState().setFontSize(18F);
p.getStructureTextState().setForegroundColor(Color.getRed());
p.getStructureTextState().setFontStyle(FontStyles.Italic);

p.setText("نص مائل باللون الأحمر.");

// حفظ مستند PDF موسوم
document.save(path + "StyleTextStructure.pdf");
```


## توضيح عناصر الهيكل

من أجل توضيح عناصر الهيكل في وثيقة PDF معنونة، توفر Aspose.PDF فئة [IllustrationElement](https://reference.aspose.com/pdf/java/com.aspose.pdf.tagged.logicalstructure.elements.class-use/IllustrationElement). يظهر مقطع الشيفرة التالي كيفية توضيح عناصر الهيكل في وثيقة PDF معنونة:

```java
// للحصول على أمثلة كاملة وملفات البيانات، يرجى الذهاب إلى https://github.com/aspose-pdf/Aspose.PDF-for-Java
// المسار إلى دليل المستندات.
String path = "pathTodir";
// إنشاء وثيقة Pdf
Document document = new Document();

// الحصول على المحتوى للعمل مع TaggedPdf
ITaggedContent taggedContent = document.getTaggedContent();

// تعيين العنوان واللغة للوثيقة
taggedContent.setTitle("وثيقة Pdf معنونة");
taggedContent.setLanguage("en-US");

// تحت التطوير
IllustrationElement figure1 = taggedContent.createFigureElement();
taggedContent.getRootElement().appendChild(figure1);
figure1.setActualText("الشكل الأول");
figure1.setTitle("صورة 1");
figure1.setTag("Fig1");
figure1.setImage("image.png");

// حفظ وثيقة Pdf معنونة
document.save(path + "IllustrationStructureElements.pdf");
```


## **إنشاء ملف PDF مع صورة موسومة**

من أجل إنشاء ملف PDF مع صورة موسومة، تقدم Aspose.PDF طريقة [createFigureElement()](https://reference.aspose.com/pdf/java/com.aspose.pdf.tagged/ITaggedContent#createFigureElement--) في واجهة [ITaggedContent](https://reference.aspose.com/pdf/java/com.aspose.pdf.tagged/ITaggedContent). يوضح مقتطف الشيفرة التالي هذه الوظيفة.

```java
// للحصول على أمثلة كاملة وملفات البيانات، يرجى زيارة https://github.com/aspose-pdf/Aspose.PDF-for-Java
Document document = new Document();
ITaggedContent taggedContent = document.getTaggedContent();

taggedContent.setTitle("CreatePDFwithTaggedImage");
taggedContent.setLanguage("en-US");

IllustrationElement figure1 = taggedContent.createFigureElement();
taggedContent.getRootElement().appendChild(figure1);
figure1.setAlternativeText("شعار Aspose");
figure1.setTitle("صورة 1");
figure1.setTag("Fig");
// إضافة صورة بدقة 300 DPI (بشكل افتراضي)
figure1.setImage("aspose-logo.jpg");
// حفظ مستند PDF
document.save("PDFwithTaggedImage.pdf");
```


## إنشاء ملف PDF مع نص موسوم

من أجل إنشاء ملف PDF مع نص موسوم، يوفر Aspose.PDF واجهة [ITaggedContent](https://reference.aspose.com/pdf/java/com.aspose.pdf.tagged/ITaggedContent). يوضح مقتطف الشيفرة التالي هذه الوظيفة.

```java
// للحصول على أمثلة كاملة وملفات البيانات، يرجى الذهاب إلى https://github.com/aspose-pdf/Aspose.PDF-for-Java
// المسار إلى دليل الوثائق.
String dataDir = Utils.getDataDir() + "TaggedPDFs\\";
// إنشاء مستند PDF
Document document = new Document();

// الحصول على المحتوى للعمل مع TaggedPdf
ITaggedContent taggedContent = document.getTaggedContent();

// تعيين العنوان واللغة للمستند
taggedContent.setTitle("مستند Pdf موسوم");
taggedContent.setLanguage("en-US");

// إنشاء عناصر هيكلية على مستوى الكتلة للنص
HeaderElement headerElement = taggedContent.createHeaderElement();
headerElement.setActualText("العنوان 1");
ParagraphElement paragraphElement1 = taggedContent.createParagraphElement();
paragraphElement1.setActualText("اختبار 1");
ParagraphElement paragraphElement2 = taggedContent.createParagraphElement();
paragraphElement2.setActualText("اختبار 2");
ParagraphElement paragraphElement3 = taggedContent.createParagraphElement();
paragraphElement3.setActualText("اختبار 3");
ParagraphElement paragraphElement4 = taggedContent.createParagraphElement();
paragraphElement4.setActualText("اختبار 4");
ParagraphElement paragraphElement5 = taggedContent.createParagraphElement();
paragraphElement5.setActualText("اختبار 5");
ParagraphElement paragraphElement6 = taggedContent.createParagraphElement();
paragraphElement6.setActualText("اختبار 6");
ParagraphElement paragraphElement7 = taggedContent.createParagraphElement();
paragraphElement7.setActualText("اختبار 7");

// حفظ مستند PDF
document.save( dataDir + "PDFwithTaggedText.pdf");
```