---
title: تعيين خصائص عناصر الهيكل في PDF الموسوم
linktitle: تعيين خصائص عناصر الهيكل
type: docs
weight: 30
url: /ar/java/set-tagged-pdfs-element-properties/
description: مع Aspose.PDF for Java، يمكنك تعيين خصائص مختلفة لعناصر الهيكل. هناك تعيين عناصر هيكل النص، تعيين عناصر الهيكل المضمنة، إضافة عنصر هيكل إلى العناصر وما إلى ذلك.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## تعيين خصائص عناصر الهيكل

من أجل تعيين خصائص عناصر الهيكل في مستند PDF موسوم، تقدم Aspose.PDF طريقتي **createSectElement()** و **createHeaderElement()** لواجهة [ITaggedContent](https://reference.aspose.com/pdf/java/com.aspose.pdf.tagged/ITaggedContent). يوضح مقطع الكود التالي كيفية تعيين خصائص عناصر الهيكل لمستند PDF موسوم:

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

// إنشاء عناصر الهيكل
StructureElement rootElement = taggedContent.getRootElement();

SectElement sect = taggedContent.createSectElement();
rootElement.appendChild(sect);

HeaderElement h1 = taggedContent.createHeaderElement(1);
sect.appendChild(h1);
h1.setText("العنوان");

h1.setTitle("العنوان");
h1.setLanguage("en-US");
h1.setAlternativeText("النص البديل");
h1.setExpansionText("نص التوسع");
h1.setActualText("النص الفعلي");

// حفظ مستند PDF الموسوم
document.save(path + "StructureElementsProperties.pdf");
```


## إعداد عناصر هيكل النص

من أجل إعداد عناصر هيكل النص لوثيقة PDF موسومة، تقدم Aspose.PDF فئة [ParagraphElement](https://reference.aspose.com/pdf/java/com.aspose.pdf.tagged.logicalstructure.elements.bls/class-use/ParagraphElement). يوضح مقطع الشيفرة التالي كيفية إعداد عناصر هيكل النص لوثيقة PDF موسومة:

```java
// للحصول على أمثلة كاملة وملفات البيانات، يرجى زيارة https://github.com/aspose-pdf/Aspose.PDF-for-Java
// المسار إلى دليل المستندات.
String path = "pathTodir";

// إنشاء مستند Pdf
Document document = new Document();

// احصل على المحتوى للعمل مع TaggedPdf
ITaggedContent taggedContent = document.getTaggedContent();

// تعيين العنوان واللغة للمستند
taggedContent.setTitle("وثيقة Pdf موسومة");
taggedContent.setLanguage("en-US");

// احصل على عناصر الهيكل الجذرية
StructureElement rootElement = taggedContent.getRootElement();

ParagraphElement p = taggedContent.createParagraphElement();
// تعيين النص إلى عنصر هيكل النص
p.setText("فقرة.");
rootElement.appendChild(p);


// احفظ وثيقة Pdf موسومة
document.save(path + "TextStructureElement.pdf");
```


## إعداد عناصر هيكل كتلة النص

من أجل إعداد عناصر هيكل كتلة النص لوثيقة PDF موسومة، تقدم Aspose.PDF الفئات [HeaderElement](https://reference.aspose.com/pdf/java/com.aspose.pdf.tagged.logicalstructure.elements.bls.class-use/headerelement) و[ParagraphElement](https://reference.aspose.com/pdf/java/com.aspose.pdf.tagged.logicalstructure.elements.bls/class-use/ParagraphElement). يمكنك إضافة كائنات من هذه الفئات كطفل لكائن **StructureElement**. يوضح مقتطف الشيفرة التالي كيفية إعداد عناصر هيكل كتلة النص لوثيقة PDF موسومة:

```java
// للحصول على أمثلة كاملة وملفات البيانات، يرجى زيارة https://github.com/aspose-pdf/Aspose.PDF-for-Java
// المسار إلى دليل الوثائق.
String path = "pathTodir";

// إنشاء مستند PDF
Document document = new Document();

// الحصول على المحتوى للعمل مع TaggedPdf
ITaggedContent taggedContent = document.getTaggedContent();

// تعيين العنوان واللغة للمستند
taggedContent.setTitle("Tagged Pdf Document");
taggedContent.setLanguage("en-US");

// الحصول على عنصر الهيكل الجذري
StructureElement rootElement = taggedContent.getRootElement();

HeaderElement h1 = taggedContent.createHeaderElement(1);
HeaderElement h2 = taggedContent.createHeaderElement(2);
HeaderElement h3 = taggedContent.createHeaderElement(3);
HeaderElement h4 = taggedContent.createHeaderElement(4);
HeaderElement h5 = taggedContent.createHeaderElement(5);
HeaderElement h6 = taggedContent.createHeaderElement(6);
h1.setText("H1. Header of Level 1");
h2.setText("H2. Header of Level 2");
h3.setText("H3. Header of Level 3");
h4.setText("H4. Header of Level 4");
h5.setText("H5. Header of Level 5");
h6.setText("H6. Header of Level 6");
rootElement.appendChild(h1);
rootElement.appendChild(h2);
rootElement.appendChild(h3);
rootElement.appendChild(h4);
rootElement.appendChild(h5);
rootElement.appendChild(h6);

ParagraphElement p = taggedContent.createParagraphElement();
p.setText("P. لوريم إيبسوم دولور سيت أميت، كونسيكتيتور أديبيسسينغ إليت. آنين نيك ليكتوس آك سيم فاوستيبوس ايمبيريديت. سيد أوت إيرات آك ماجنا أولامكوربر هندريريت. كراس بيناتيسكوي ليبرو سيمبر، جرافيدا ماجنا سيد، لوكتوس ليو. فوسسي ليكتوس أوديو، لوريت نيك أولامكوربر أوت، موليسيتي يو إليت. إنترودوم إت ماليسوادا فاميس آك آنتي إيبسوم بريميس إن فاوستيبوس. أليكوام لاتشينيا سيت أميت إليت آك كونسيكتيتور. دونيك كورسوس كونديدوم ليجولا، فيتاي فاولتبوت سيم تريستيكوي إيجيت. نولا إن كونسيكتيتور ماسا. فيستيبولوم فيتاي لوبرتيس آنتي. نولا أولامكوربر بيناتيسكوي جوستو رهنكس أكومسان. موريس أورنار يو أوديو نون لاتشينيا. أليكوام ماسا ليو، رهنكس آك إياكوليس إيجيت، تيمبوس إت ماجنا. سيد نون كونسيكتيتور إليت. سيد فولبوتيت، كوام سيد لاتشينيا لوكتوس، إيبسوم نيب فرينجيلا بورس، فيتاي بوسوير ريسوس أوديو آيد ماسا. كراس سيد فينيناتيس لاكوس.");
rootElement.appendChild(p);

// حفظ وثيقة PDF موسومة
document.save(path + "TextBlockStructureElements.pdf");
```


## إعداد عناصر البنية المضمنة

من أجل إعداد عناصر البنية المضمنة لوثيقة PDF الموسومة، تقدم Aspose.PDF فئات [SpanElement](https://reference.aspose.com/pdf/java/com.aspose.pdf.tagged.logicalstructure.elements.ils/spanelement) و[ParagraphElement](https://reference.aspose.com/pdf/java/com.aspose.pdf.tagged.logicalstructure.elements.bls/class-use/ParagraphElement). يمكنك إلحاق كائنات من هذه الفئات كأطفال لكائن **StructureElement**. يوضح مقتطف الشيفرة التالي كيفية إعداد عناصر البنية المضمنة لوثيقة PDF الموسومة:

```java
// للحصول على أمثلة كاملة وملفات البيانات، يرجى زيارة https://github.com/aspose-pdf/Aspose.PDF-for-Java
// المسار إلى دليل الوثائق.
String path = "pathTodir";
// إنشاء مستند PDF
Document document = new Document();

// الحصول على المحتوى للعمل مع TaggedPdf
ITaggedContent taggedContent = document.getTaggedContent();

// إعداد العنوان واللغة للوثيقة
taggedContent.setTitle("Tagged Pdf Document");
taggedContent.setLanguage("en-US");

// الحصول على عنصر البنية الجذرية
StructureElement rootElement = taggedContent.getRootElement();

HeaderElement h1 = taggedContent.createHeaderElement(1);
HeaderElement h2 = taggedContent.createHeaderElement(2);
HeaderElement h3 = taggedContent.createHeaderElement(3);
HeaderElement h4 = taggedContent.createHeaderElement(4);
HeaderElement h5 = taggedContent.createHeaderElement(5);
HeaderElement h6 = taggedContent.createHeaderElement(6);
rootElement.appendChild(h1);
rootElement.appendChild(h2);
rootElement.appendChild(h3);
rootElement.appendChild(h4);
rootElement.appendChild(h5);
rootElement.appendChild(h6);

SpanElement spanH11 = taggedContent.createSpanElement();
spanH11.setText("H1. ");
h1.appendChild(spanH11);
SpanElement spanH12 = taggedContent.createSpanElement();
spanH12.setText("مستوى 1 العنوان");
h1.appendChild(spanH12);

SpanElement spanH21 = taggedContent.createSpanElement();
spanH21.setText("H2. ");
h2.appendChild(spanH21);
SpanElement spanH22 = taggedContent.createSpanElement();
spanH22.setText("مستوى 2 العنوان");
h2.appendChild(spanH22);

SpanElement spanH31 = taggedContent.createSpanElement();
spanH31.setText("H3. ");
h3.appendChild(spanH31);
SpanElement spanH32 = taggedContent.createSpanElement();
spanH32.setText("مستوى 3 العنوان");
h3.appendChild(spanH32);

SpanElement spanH41 = taggedContent.createSpanElement();
spanH41.setText("H4. ");
h4.appendChild(spanH41);
SpanElement spanH42 = taggedContent.createSpanElement();
spanH42.setText("مستوى 4 العنوان");
h4.appendChild(spanH42);

SpanElement spanH51 = taggedContent.createSpanElement();
spanH51.setText("H5. ");
h5.appendChild(spanH51);
SpanElement spanH52 = taggedContent.createSpanElement();
spanH52.setText("مستوى 5 العنوان");
h5.appendChild(spanH52);

SpanElement spanH61 = taggedContent.createSpanElement();
spanH61.setText("H6. ");
h6.appendChild(spanH61);
SpanElement spanH62 = taggedContent.createSpanElement();
spanH62.setText("مستوى 6 العنوان");
h6.appendChild(spanH62);

ParagraphElement p = taggedContent.createParagraphElement();
p.setText("P. ");
rootElement.appendChild(p);
SpanElement span1 = taggedContent.createSpanElement();
span1.setText("لوريم إيبسوم دولور سيت أميت، كونسيكتيتور أديبيسيكينغ إليت. ");
p.appendChild(span1);
SpanElement span2 = taggedContent.createSpanElement();
span2.setText("أنين نيك لكتس أك سيم فوسيبيس إمبيرديت. ");
p.appendChild(span2);
SpanElement span3 = taggedContent.createSpanElement();
span3.setText("سد أوت إيرات أك ماجنا أولامكوربر هندريت. ");
p.appendChild(span3);
SpanElement span4 = taggedContent.createSpanElement();
span4.setText("كراس بيلينتيسك ليبيرو سيمبر، جرافيدا ماجنا سيد، لوكتوس ليو. ");
p.appendChild(span4);
SpanElement span5 = taggedContent.createSpanElement();
span5.setText("فوس ليكتس أوديو، لاوريت نيك أولامكوربر أوت، موليستي أو إليت. ");
p.appendChild(span5);
SpanElement span6 = taggedContent.createSpanElement();
span6.setText("إنترادوم إت ماليسوادا فاميس أك أنتي إبسم بريميز إن فوسيبيس. ");
p.appendChild(span6);
SpanElement span7 = taggedContent.createSpanElement();
span7.setText("أليكوام لاكينيا سيت أميت إليت أك كونسيكتيتور. دونيك كورسوس كونديمينتوم ليجولا، فيتاي فولبوتات سيم تريستيك إيت. ");
p.appendChild(span7);
SpanElement span8 = taggedContent.createSpanElement();
span8.setText("نولا إن كونسيكتيتور ماسا. فيستيبولم فيتاي لوبورتس أنتي. نولا أولامكوربر بيلينتيسك جوستو رهنكوس أككومسان. ");
p.appendChild(span8);
SpanElement span9 = taggedContent.createSpanElement();
span9.setText("ماوريس أورناري أو أوديو نون لاكينيا. أليكوام ماسا ليو، رهنكوس أك إيكلوس إيت، تمبوس إت ماجنا. سد نون كونسيكتيتور إليت. ");
p.appendChild(span9);
SpanElement span10 = taggedContent.createSpanElement();
span10.setText("سد فولبوتات، كوام سيد لاكينيا لوكتوس، إبسم نيبه فرينجيلا بوروس، فيتاي بوسوير ريسوس أوديو إيد ماسا. كراس سيد فينيناتيس لاكس.");
p.appendChild(span10);

// حفظ وثيقة PDF الموسومة
document.save(path + "InlineStructureElements.pdf");
```


## إعداد اسم علامة مخصص

من أجل تعيين اسم علامة مخصص لعناصر مستند PDF الموسوم، تقدم Aspose.PDF طريقة **setTag()** للعناصر. يوضح مقطع الكود التالي كيفية تعيين اسم علامة مخصص:

```java
// للحصول على أمثلة كاملة وملفات البيانات، يرجى الانتقال إلى https://github.com/aspose-pdf/Aspose.PDF-for-Java
// المسار إلى دليل المستندات.
String path = "pathTodir";
// إنشاء مستند PDF
Document document = new Document();

// الحصول على المحتوى للعمل مع TaggedPdf
ITaggedContent taggedContent = document.getTaggedContent();

// تعيين العنوان واللغة للمستند
taggedContent.setTitle("Tagged Pdf Document");
taggedContent.setLanguage("en-US");

// إنشاء عناصر الهيكل المنطقي
SectElement sect = taggedContent.createSectElement();
taggedContent.getRootElement().appendChild(sect);

ParagraphElement p1 = taggedContent.createParagraphElement();
ParagraphElement p2 = taggedContent.createParagraphElement();
ParagraphElement p3 = taggedContent.createParagraphElement();
ParagraphElement p4 = taggedContent.createParagraphElement();

p1.setText("P1. ");
p2.setText("P2. ");
p3.setText("P3. ");
p4.setText("P4. ");

p1.setTag("P1");
p2.setTag("Para");
p3.setTag("Para");
p4.setTag("Paragraph");

sect.appendChild(p1);
sect.appendChild(p2);
sect.appendChild(p3);
sect.appendChild(p4);

SpanElement span1 = taggedContent.createSpanElement();
SpanElement span2 = taggedContent.createSpanElement();
SpanElement span3 = taggedContent.createSpanElement();
SpanElement span4 = taggedContent.createSpanElement();

span1.setText("Span 1.");
span2.setText("Span 2.");
span3.setText("Span 3.");
span4.setText("Span 4.");

span1.setTag("SPAN");
span2.setTag("Sp");
span3.setTag("Sp");
span4.setTag("TheSpan");

p1.appendChild(span1);
p2.appendChild(span2);
p3.appendChild(span3);
p4.appendChild(span4);

// حفظ مستند PDF الموسوم
document.save(path + "CustomTag.pdf");
```


## إضافة عنصر بنية إلى العناصر

من أجل تعيين عناصر بنية الروابط في مستند PDF الموسوم، تقدم Aspose.PDF طريقة **createLinkElement()** من واجهة [ITaggedContent](https://reference.aspose.com/pdf/java/com.aspose.pdf.tagged/ITaggedContent). يوضح مقطع الشفرة التالي كيفية تعيين عناصر البنية في فقرة تحتوي على نص في مستند PDF الموسوم:

```java
// للحصول على أمثلة كاملة وملفات البيانات، يرجى الانتقال إلى https://github.com/aspose-pdf/Aspose.PDF-for-Java
// المسار إلى دليل المستندات.
String dataDir = Utils.getDataDir() + "TaggedPDFs\\";
String outFile = dataDir + "AddStructureElementIntoElement_Output.pdf";
String logFile = dataDir + "46144_log.xml";

// إنشاء المستند والحصول على محتوى PDF الموسوم
Document document = new Document();
ITaggedContent taggedContent = document.getTaggedContent();


// تعيين العنوان واللغة الطبيعية للمستند
taggedContent.setTitle("Text Elements Example");
taggedContent.setLanguage("en-US");

// الحصول على عنصر البنية الجذرية (عنصر بنية المستند)
StructureElement rootElement = taggedContent.getRootElement();


ParagraphElement p1 = taggedContent.createParagraphElement();
rootElement.appendChild(p1);
SpanElement span11 = taggedContent.createSpanElement();
span11.setText("Span_11");
SpanElement span12 = taggedContent.createSpanElement();
span12.setText(" and Span_12.");
p1.setText("Paragraph with ");
p1.appendChild(span11);
p1.appendChild(span12);


ParagraphElement p2 = taggedContent.createParagraphElement();
rootElement.appendChild(p2);
SpanElement span21 = taggedContent.createSpanElement();
span21.setText("Span_21");
SpanElement span22 = taggedContent.createSpanElement();
span22.setText("Span_22.");
p2.appendChild(span21);
p2.setText(" and ");
p2.appendChild(span22);


ParagraphElement p3 = taggedContent.createParagraphElement();
rootElement.appendChild(p3);
SpanElement span31 = taggedContent.createSpanElement();
span31.setText("Span_31");
SpanElement span32 = taggedContent.createSpanElement();
span32.setText(" and Span_32");
p3.appendChild(span31);
p3.appendChild(span32);
p3.setText(".");


ParagraphElement p4 = taggedContent.createParagraphElement();
rootElement.appendChild(p4);
SpanElement span41 = taggedContent.createSpanElement();
SpanElement span411 = taggedContent.createSpanElement();
span411.setText("Span_411, ");
span41.setText("Span_41, ");
span41.appendChild(span411);
SpanElement span42 = taggedContent.createSpanElement();
SpanElement span421 = taggedContent.createSpanElement();
span421.setText("Span 421 and ");
span42.appendChild(span421);
span42.setText("Span_42");
p4.appendChild(span41);
p4.appendChild(span42);
p4.setText(".");


// حفظ مستند PDF الموسوم
document.save(outFile);
```


## إعداد عنصر هيكل الملاحظة

تتيح لك Aspose.PDF لواجهة برمجة تطبيقات Java أيضًا إضافة **NoteElement** في مستند PDF الموسوم. يوضح مقتطف الشيفرة التالي كيفية إضافة عنصر ملاحظة في مستند PDF الموسوم:

```java
// للحصول على أمثلة كاملة وملفات البيانات، يرجى زيارة https://github.com/aspose-pdf/Aspose.PDF-for-Java
// المسار إلى دليل المستندات.
String dataDir = Utils.getDataDir() + "TaggedPDFs\\";
String outFile = dataDir + "CreateNoteStructureElement.pdf";
String logFile = dataDir + "45929_log.xml";

// إنشاء مستند PDF
Document document = new Document();
ITaggedContent taggedContent = document.getTaggedContent();

taggedContent.setTitle("نموذج لعناصر الملاحظة");
taggedContent.setLanguage("en-US");

// إضافة عنصر فقرة
ParagraphElement paragraph = taggedContent.createParagraphElement();
taggedContent.getRootElement().appendChild(paragraph);

// إضافة NoteElement
NoteElement note1 = taggedContent.createNoteElement();
paragraph.appendChild(note1);
note1.setText("ملاحظة مع توليد تلقائي للمعرف. ");

// إضافة NoteElement
NoteElement note2 = taggedContent.createNoteElement();
paragraph.appendChild(note2);
note2.setText("ملاحظة مع المعرف = 'note_002'. ");
note2.setId("note_002");

// إضافة NoteElement
NoteElement note3 = taggedContent.createNoteElement();
paragraph.appendChild(note3);
note3.setText("ملاحظة مع المعرف = 'note_003'. ");
note3.setId("note_003");
// حفظ مستند PDF الموسوم
document.save(outFile);
```