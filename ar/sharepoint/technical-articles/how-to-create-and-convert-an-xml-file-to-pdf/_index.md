---
title: كيفية إنشاء وتحويل ملف XML إلى PDF
linktitle: كيفية إنشاء وتحويل ملف XML إلى PDF
type: docs
weight: 30
url: /ar/sharepoint/how-to-create-and-convert-an-xml-file-to-pdf/
lastmod: "2026-06-18"
description: API PDF لـ SharePoint قادر على إنشاء وتحويل ملفات XML إلى صيغة PDF.
---

{{% alert color="primary" %}}

تم بناء Aspose.PDF لـ SharePoint فوق مكوّن Aspose.PDF لـ .NET الحائز على جوائز. يقدم Aspose.PDF لـ .NET ميزات رائعة بدءًا من إنشاء مستند PDF من الصفر إلى معالجة ملفات PDF الموجودة. من بين هذه الميزات، التحويل من XML إلى PDF هو أحد الميزات الكبيرة التي يدعمها هذا المنتج. لذلك نعتقد أن Aspose.PDF لـ SharePoint سيكون أيضًا قادرًا على تحويل ملفات XML إلى صيغة PDF.

{{% /alert %}}

## **إنشاء ملف XML وتحويله إلى PDF**

{{% alert color="primary" %}}

خطوة بخطوة، يشرح لك هذا المقال عملية إنشاء ملف XML وتحويله إلى PDF:

1. [إنشاء ملف XML](/pdf/ar/sharepoint/how-to-create-and-convert-an-xml-file-to-pdf/#step-1-create-xml-file).
2. [إنشاء قالب PDF](/pdf/ar/sharepoint/how-to-create-and-convert-an-xml-file-to-pdf/#step-2-create-pdf-template).
3. [تحميل قالب XML](/pdf/ar/sharepoint/how-to-create-and-convert-an-xml-file-to-pdf/#step-3-load-xml-template).
4. [تحديد المسار إلى مسار المصدر](/pdf/ar/sharepoint/how-to-create-and-convert-an-xml-file-to-pdf/#step-4-specify-source-file-path).
5. [تحديد خصائص الملف](/pdf/ar/sharepoint/how-to-create-and-convert-an-xml-file-to-pdf/#step-5-specify-file-properties).
6. [تصدير الملف إلى PDF](/pdf/ar/sharepoint/how-to-create-and-convert-an-xml-file-to-pdf/#step-6-export-to-pdf).
7. [حفظ ملف PDF](/pdf/ar/sharepoint/how-to-create-and-convert-an-xml-file-to-pdf/#step-7-save-pdf-document).
#### **الخطوة 1: إنشاء ملف XML**
أولاً، أنشئ ملف XML بناءً على نموذج كائن المستند Aspose.PDF لـ .NET.

وفقًا لنموذج كائن المستند Aspose.PDF لـ .NET، يحتوي مستند PDF على مجموعة من كائنات Section، وتحتوي كل Section على عنصر واحد أو أكثر من Paragraph. النص هو كائن على مستوى Paragraph وقد يحتوي على مقاطع واحدة أو أكثر. أدناه، يتم إضافة سلسلة نصية نموذجية إلى كائن Segment ثم إضافتها إلى كائن Text. أخيرًا، يتم إضافة عنصر Text إلى مجموعة الفقرات الخاصة بكائن Section.

**XML**

{{< highlight csharp >}}



\u003C?xml version=\u00221.0\u0022 encoding=\u0022utf-8\u0022 ?\u003E

  <Pdf xmlns="Aspose.PDF">

   <Section>

    <Text>

            <Segment>مرحبا بالعالم</Segment>

    </Text>

   </Section>

  </Pdf>



{{< /highlight >}}
#### **الخطوة 2: إنشاء قالب PDF**
قبل المتابعة، تأكد من أن خادم SharePoint Foundation 2010 مثبت بشكل صحيح ومُعَد على النظام الذي ستجرى عليه عملية التحويل.

1. سجِّل الدخول إلى موقع SharePoint.
1. اختر **Site Action** و **All Items**.
1. حدد خيار **Create** واختر **PDF Template** من القائمة.
1. أدخل اسم القالب.
1. انقر على **Create**.




![todo:image_alt_text](how-to-create-and-convert-an-xml-file-to-pdf_1.png)
#### **الخطوة 3: تحميل قالب XML**
بمجرد إنشاء القالب، قم بتحميل [ملف XML](/pdf/ar/sharepoint/how-to-create-and-convert-an-xml-file-to-pdf/):

1. في صفحة قالب PDF، حدد **إضافة عنصر جديد**.




![todo:image_alt_text](how-to-create-and-convert-an-xml-file-to-pdf_2.png)
#### **الخطوة 4: تحديد مسار ملف المصدر**
في مربع حوار تحميل المستند:

1. انقر على **Browse** وحدد موقع ملف XML على نظامك. يمكنك تمكين خانة الاختيار لتجاوز خيار الملف الموجود.
1. اضغط زر **OK**.




![todo:image_alt_text](how-to-create-and-convert-an-xml-file-to-pdf_3.png)
#### **الخطوة 5: تحديد خصائص الملف**
عند تحميل الملف، أضف المعلومات إلى الحقول الإلزامية (المعلّمة بنجمة حمراء: *).

في هذا المثال، تمت إضافة وصف تجريبي وتم إكمال الحقول التالية:

1. وصف مختصر للوثيقة.
1. اكتب **AllListTypes** في حقل **Assigned List Types**.
1. اختر **List** من قائمة **Type**.
   تأكد من أن الحالة تظل **Active**.
1. انقر **حفظ** لحفظ الخصائص.




![todo:image_alt_text](how-to-create-and-convert-an-xml-file-to-pdf_4.png)
#### **الخطوة 6: تصدير إلى PDF**
عند إضافة ملف XML إلى قالب PDF:
إما:

1. انقر بزر الماوس الأيمن على ملف test.xml.
1. اختر **تصدير إلى PDF** من القائمة.

أو:

1. حدد **Aspose Tools** من **Library Tools**.
1. انقر **Export**.




![todo:image_alt_text](how-to-create-and-convert-an-xml-file-to-pdf_5.png)
#### **الخطوة 7: حفظ مستند PDF**
1. في مربع حوار تصدير إلى PDF، حدد **Template storage** (الموقع الذي يُخزن فيه ملف المصدر).
1. حدد الملف المراد تصديره من قائمة **Template name**.
1. انقر **Export to PDF** لحفظ مستند PDF النهائي.




![todo:image_alt_text](how-to-create-and-convert-an-xml-file-to-pdf_6.png)
#### **افتح ملف PDF**
تم حفظ مستند PDF ويمكن فتحه. في الصورة أدناه، لاحظ العبارة "Hello World" التي كانت في الوسم {segment] داخل XML. لاحظ أيضًا أن منتج PDF هو Aspose.PDF for SharePoint.




![todo:image_alt_text](how-to-create-and-convert-an-xml-file-to-pdf_7.png)

{{% /alert %}}
