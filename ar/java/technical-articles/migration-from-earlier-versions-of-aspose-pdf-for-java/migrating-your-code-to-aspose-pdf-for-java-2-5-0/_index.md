---
title: نقل التعليمات البرمجية الخاصة بك إلى Aspose.PDF لـ Java 2.5.0
type: docs
weight: 10
url: ar/java/migrating-your-code-to-aspose-pdf-for-java-2-5-0/
lastmod: "2022-01-27"
---

{{% alert color="primary" %}}

في هذه المقالة حاولنا تسليط الضوء على بعض المجالات من الكود الحالي لـ Aspose.PDF لـ Java لجعله متوافقًا مع أحدث إصدار.

{{% /alert %}}

## التفاصيل

مع إصدار Aspose.PDF لـ Java 2.5.0، حدثت العديد من التغييرات في هيكل API وبناء الفئات. تم تحديث أسماء معظم أعضاء الفئات، وتم إزالة بعض الأعضاء الحاليين وإضافة بعض الأساليب والخصائص إلى الفئات الموجودة. لإعطائك لمحة عن التغييرات، سنلقي نظرة على الكود البسيط التالي، المستند إلى إصدارات Aspose.PDF لـ Java المنشورة قبل 2.5.0.

في هذا الكود البسيط، سنضيف رابطًا تشعبيًا ورابطًا إلى الصفحة داخل نفس مستند PDF.

```java
import com.aspose.pdf.elements.*;
com.aspose.pdf.License lic = new com.aspose.pdf.License();

try {

lic.setLicense(new FileInputStream(new File("Aspose.Total.Java.lic")));

    } catch (Exception e)

{

System.out.println(e.getMessage());

}


//إنشاء كائن Pdf من خلال استدعاء منشئ فارغ

Pdf pdf1 = new Pdf();

//إنشاء قسم في كائن Pdf

Section sec1 = pdf1.getSections().add();

//إنشاء فقرة نصية مع مرجع إلى القسم

Text text1 = new Text(sec1);

//إضافة الفقرة النصية إلى مجموعة الفقرات في القسم

sec1.getParagraphs().add(text1);

//إضافة جزء نصي إلى الفقرة النصية

Segment segment1 = text1.getSegments().add("this is a local link");

//تعيين النص في الجزء النصي ليكون تحته خط

segment1.getTextInfo().setUnderLine(true);


//تعيين نوع الرابط للجزء النصي ليكون محليًا

//تعيين معرف الفقرة المطلوبة كمعرف هدف للجزء النصي

segment1.setHyperLink(new HyperLinkToLocalPdf("product1"));

//إنشاء فقرة نصية ليتم ربطها بالجزء النصي

Text text3 = new Text(sec1,"product 1 info ...");

//إضافة الفقرة النصية إلى مجموعة الفقرات في القسم

sec1.getParagraphs().add(text3);

//تعيين هذه الفقرة لتكون الأولى بحيث يمكن عرضها في صفحة منفصلة

//في المستند

text3.setFirstParagraph(true);

//تعيين معرف هذا الجزء النصي ليكون "product1"

text3.setID("product1"); 


// حفظ ملف PDF

FileOutputStream out = new FileOutputStream(new File("UpdateOfCode_Test.pdf"));

pdf1.save(out);
```


عند استخدام الإصدارات السابقة لـ Aspose.PDF for Java 2.5.0، يمكن تنفيذ الكود بنجاح وإنشاء مستند PDF يحتوي على رابط تشعبي نحو صفحة داخل نفس المستند. ولكن، عند تجميع نفس الكود مع الإصدار 2.5.0، ستلاحظ عددًا من الأخطاء لأن هناك تغييرات في أعضاء الفئة كما تمت إزالة بعض الأساليب في الفئات. الآن دعونا نبدأ بتعديل الكود للإصدار 2.5.0

استخدم `import aspose.pdf.*` ؛ بدلاً من `import com.aspose.pdf.elements.*`؛ لتضمين الحزمة.

لتهيئة الترخيص، يرجى تحديث الكود الحالي من

{{% alert color="primary" %}}
**com.aspose.pdf.License lic = new com.aspose.pdf.License();**

```java

 try
{
lic.setLicense(new FileInputStream(new File("Aspose.Total.Java.lic")));
}

```

{{% /alert %}}

إلى

{{% alert color="primary" %}}
**aspose.pdf.License lic = new aspose.pdf.License();**

```java

 try
{
lic.setLicense(new FileInputStream(new File("Aspose.Total.Java.lic")));
}

```


{{% /alert %}}

**TextInfo** لم يعد يحتوي على طريقة **setUnderLine(...)**. الرجاء محاولة استخدام **TextInfo.setIsUnderline(...)** ** بدلاً من **.**

تمت إزالة الفئة المسماة **HyperLinkToLocalPdf**. لذا يرجى تحديث أي كود موجود لديك مثل

{{% alert color="primary" %}}
**// قم بتعيين نوع الرابط لجزء النص إلى محلي**

```java

 // قم بتعيين معرف الفقرة المطلوبة كمعرف الهدف لجزء النص

segment1.setHyperLink(new HyperLinkToLocalPdf("product1"));

```

{{% /alert %}}

إلى

{{% alert color="primary" %}}
**segment1.getHyperlink().setLinkType(HyperlinkType.Local);**

```java

 segment1.getHyperlink().setTargetID("product1");

```

{{% /alert %}}

تمت إزالة اسم الطريقة **setFirstParagraph** من فئة Text.
 من أجل عرض مقطع النص في صفحة جديدة، تحتاج إلى إنشاء كائن Section جديد وإضافة كائن النص إلى القسم الذي تم إنشاؤه حديثًا. حيث أنه بشكل افتراضي يتم عرض كل قسم في صفحة جديدة، لذا لا توجد حاجة لاستدعاء طريقة مثل **sec2.setIsNewPage(true**)**;

## طريقة الحفظ المحدثة

تم إزالة طريقة الحفظ في فئة Pdf التي كانت تأخذ كائن FileOutputStream كمعامل. في الإصدار الجديد، يمكنك استخدام أي من طرق الحفظ المُفرطة التالية.

- save(BasicStream stream)
- save(java.lang.String pdfFile)
- save(java.lang.String fileName, SaveType saveType, aspose.pdf.HttpResponse response)

بعد إجراء جميع التغييرات المحددة أعلاه، عند استخدام Aspose.PDF for Java 2.5.0، سيتم تجميع الشيفرة وتنفيذها دون إظهار أي رسائل خطأ. يتم تحديد الشيفرة المحدثة بالكامل أدناه.

```java
import aspose.pdf.*;
aspose.pdf.License lic = new aspose.pdf.License();

try {

lic.setLicense(new FileInputStream(new File("Aspose.Total.Java.lic")));

    } catch (Exception e)

{

System.out.println(e.getMessage());

}

try {

//Instantiate a Pdf object by calling its empty constructor

Pdf pdf1 = new Pdf();

//Create a section in the Pdf object

Section sec1 = pdf1.getSections().add();

//Create text paragraph with the reference of a section

Text text1 = new Text(sec1);

//Add the text paragraph in the paragraphs collection of the section

sec1.getParagraphs().add(text1);

//Add a text segment in the text paragraph

Segment segment1 = text1.getSegments().add("this is a local link");

//Set the text in the text segment to be underlined

segment1.getTextInfo().setIsUnderline(true);


//Set the link type of the text segment to Local

//Assign the id of the desired paragraph as a target id for the text segment

segment1.getHyperlink().setLinkType(HyperlinkType.Local);

segment1.getHyperlink().setTargetID("product1");

// add a new section which will hold the text object with ID "Product 1"

Section sec2 = pdf1.getSections().add();

//Create a text paragraph to be linked with the text segment

Text text3 = new Text(sec1,"product 1 info ...");

//Add the text paragraph to paragraphs collection of the section

sec2.getParagraphs().add(text3);

//Set the id of this text segment to "product1"

text3.setID("product1");


// save the PDF file

pdf1.save("UpdateOfCode_Test.pdf");


     }catch(Exception e)

{

System.out.println(e.getMessage());

}
```

## الخاتمة

في الموضوع أعلاه قمنا بتوضيح بعض الفئات والطرق التي تم تغييرها في الإصدار الجديد. للحصول على قائمة كاملة بجميع الفئات وأعضائها، يُرجى زيارة [مرجع Aspose.PDF لـ Java API](http://www.aspose.com/documentation/java-components/aspose.pdf-for-java/aspose.pdf-for-java-api-reference.html)

لتعلم المزيد عن Aspose ومنتجاتها، يُرجى النقر هنا <http://www.aspose.com/>