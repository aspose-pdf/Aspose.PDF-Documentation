---
title: كيفية إنشاء وتحويل ملف XML إلى PDF
type: docs
weight: 30
url: ar/sharepoint/how-to-create-and-convert-an-xml-file-to-pdf/
lastmod: "2020-12-16"
description: PDF SharePoint API قادر على إنشاء وتحويل ملفات XML إلى تنسيق PDF.
---

{{% alert color="primary" %}}

Aspose.PDF لـ SharePoint مبني على مكون Aspose.PDF لـ .NET الحائز على جوائز. يوفر Aspose.PDF لـ .NET ميزات رائعة من إنشاء مستند PDF من البداية إلى التلاعب بملفات PDF الموجودة. من بين هذه الميزات، يعتبر تحويل XML إلى PDF واحدة من الميزات الرائعة التي يدعمها هذا المنتج. لذلك نعتقد أن Aspose.PDF لـ SharePoint سيكون قادرًا أيضًا على تحويل ملفات XML إلى تنسيق PDF.

{{% /alert %}}

## **إنشاء ملف XML وتحويله إلى PDF**

{{% alert color="primary" %}}

خطوة بخطوة، يأخذك هذا المقال خلال عملية إنشاء ملف XML وتحويله إلى PDF:
1. [إنشاء ملف XML](/pdf/sharepoint/how-to-create-and-convert-an-xml-file-to-pdf/#step-1-create-xml-file).
2. [إنشاء قالب PDF](/pdf/sharepoint/how-to-create-and-convert-an-xml-file-to-pdf/#step-2-create-pdf-template).
3. [تحميل قالب XML](/pdf/sharepoint/how-to-create-and-convert-an-xml-file-to-pdf/#step-3-load-xml-template).
4. [تحديد المسار إلى الملف المصدر](/pdf/sharepoint/how-to-create-and-convert-an-xml-file-to-pdf/#step-4-specify-source-file-path).
5. [تحديد خصائص الملف](/pdf/sharepoint/how-to-create-and-convert-an-xml-file-to-pdf/#step-5-specify-file-properties).
6. [تصدير الملف إلى PDF](/pdf/sharepoint/how-to-create-and-convert-an-xml-file-to-pdf/#step-6-export-to-pdf).
7. [حفظ ملف PDF](/pdf/sharepoint/how-to-create-and-convert-an-xml-file-to-pdf/#step-7-save-pdf-document).

#### **الخطوة 1: إنشاء ملف XML**
أولاً، قم بإنشاء ملف XML بناءً على نموذج كائن المستند Aspose.PDF لـ .NET.

وفقاً لنموذج Aspose.PDF لـ .NET، يحتوي مستند PDF على مجموعة من كائنات Section، وتحتوي Section على عنصر فقرة واحد أو أكثر.
 Text هو كائن على مستوى الفقرة وقد يحتوي على مقطع واحد أو أكثر. أدناه، يتم إضافة سلسلة نصية كمثال إلى كائن Segment ويتم إضافتها إلى كائن Text. أخيرًا، يتم إضافة عنصر Text إلى مجموعة الفقرات في كائن Section.

**XML**

{{< highlight csharp >}}



<?xml version="1.0" encoding="utf-8" ?>

  <Pdf xmlns="Aspose.PDF">

   <Section>

    <Text>

            <Segment>مرحبا بالعالم</Segment>

    </Text>

   </Section>

  </Pdf>



{{< /highlight >}}
#### **الخطوة 2: إنشاء قالب PDF**
قبل المتابعة، تأكد من أن خادم SharePoint Foundation 2010 مثبت ومكون بشكل صحيح على النظام حيث ستتم عملية التحويل.

1. قم بتسجيل الدخول إلى موقع SharePoint.
1. حدد **إجراء الموقع** و **جميع العناصر**.
1. حدد خيار **إنشاء** واختر **قالب PDF** من القائمة.
1. أدخل اسمًا للقالب.
1. انقر فوق **إنشاء**.




![todo:image_alt_text](how-to-create-and-convert-an-xml-file-to-pdf_1.png)
#### **الخطوة 3: تحميل قالب XML**

بمجرد إنشاء القالب، قم بتحميل [ملف XML](/pdf/sharepoint/how-to-create-and-convert-an-xml-file-to-pdf/):
1. في صفحة قالب PDF، اختر **إضافة عنصر جديد**.




![todo:image_alt_text](how-to-create-and-convert-an-xml-file-to-pdf_2.png)
#### **الخطوة 4: تحديد مسار الملف المصدر**
في مربع حوار تحميل المستند:

1. انقر على **تصفح** وحدد موقع ملف XML على نظامك. يمكنك تمكين مربع الاختيار لكتابة الملف الحالي.
1. اضغط على زر **موافق**.




![todo:image_alt_text](how-to-create-and-convert-an-xml-file-to-pdf_3.png)
#### **الخطوة 5: تحديد خصائص الملف**
عند تحميل الملف، أضف المعلومات إلى الحقول الإلزامية (المعلمة بنجمة حمراء: *).

في هذا المثال، تمت إضافة وصف نموذجي وتم استكمال الحقول التالية:

1. وصف موجز للمستند.
1. أدخل **AllListTypes** لحقل **قوائم الأنواع المعينة**.
1. اختر **قائمة** من قائمة **النوع**.
   تأكد من أن الحالة تبقى **نشط**.
1. انقر **حفظ** لحفظ الخصائص.




![todo:image_alt_text](how-to-create-and-convert-an-xml-file-to-pdf_4.png)
#### **الخطوة 6: التصدير إلى PDF**

عند إضافة ملف XML إلى قالب PDF:
إما:

1. انقر بزر الماوس الأيمن على ملف test.xml.
1. اختر **تصدير إلى PDF** من القائمة.

أو:

1. اختر **أدوات Aspose** من **أدوات المكتبة**.
1. انقر على **تصدير**.




![todo:image_alt_text](how-to-create-and-convert-an-xml-file-to-pdf_5.png)
#### **الخطوة 7: احفظ مستند PDF**
1. في مربع الحوار "تصدير إلى PDF"، حدد **تخزين القالب** (الموقع الذي تم فيه تخزين الملف المصدر).
1. اختر الملف لتصديره من قائمة **اسم القالب**.
1. انقر على **تصدير إلى PDF** لحفظ مستند PDF النهائي.




![todo:image_alt_text](how-to-create-and-convert-an-xml-file-to-pdf_6.png)
#### **افتح الـ PDF**
تم حفظ مستند الـ PDF ويمكن فتحه. في الصورة أدناه، لاحظ العبارة "Hello World" التي كانت في وسم {segment] في الـ XML. لاحظ أيضًا أن منتج الـ PDF هو Aspose.PDF for SharePoint.




![todo:image_alt_text](how-to-create-and-convert-an-xml-file-to-pdf_7.png)

{{% /alert %}}