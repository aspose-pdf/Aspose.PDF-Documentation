---
title: ما الفرق بين تنسيقات FDF وXML وXFDF
type: docs
weight: 30
url: /net/whats-the-difference-between-xml-fdf-and-xfdf/
description: يوضح هذا القسم الفرق بين نماذج XML وFDF وXFDF باستخدام Aspose.PDF Facades باستخدام فئة Form.
lastmod: "2021-06-05"
draft: false
---

{{% alert color="primary" %}}

لقد خلطنا بين العديد من المصطلحات المختلفة مثل FDF وXML وXFDF. ترتبط جميع هذه المصطلحات ببعضها البعض بطريقة ما. يستكشف هذا المقال هذه المفاهيم وعلاقتها ببعضها البعض.

{{% /alert %}}

## فك تشفير النماذج

يُستخدم Aspose.PDF لـ .NET في معالجة مستندات PDF المعيارية من Adobe. وتحتوي مستندات PDF على نماذج تفاعلية تُسمى AcroForms. تحتوي هذه النماذج التفاعلية على عدد من حقول النماذج، مثل القائمة المنسدلة، مربع النص، وزر الراديو. تعمل النماذج التفاعلية وحقول النماذج من Adobe بنفس طريقة عمل النموذج في HTML وحقول النموذج الخاصة به.

من الممكن تخزين قيم حقول النماذج في ملف منفصل: ملف FDF (تنسيق بيانات النماذج).
``` هذا يحتوي على قيم حقول النموذج بشكل زوج مفتاح/قيمة. لا تزال ملفات FDF تُستخدم لهذا الغرض. ولكن توفر Adobe أيضًا نوعًا مشفرًا من FDF يسمى XFDF. يخزن ملف XFDF قيم حقول النموذج بطريقة هرمية باستخدام علامات XML.

مع Aspose.PDF يمكن للمطورين ليس فقط تصدير قيم حقول النموذج في PDF إلى ملف FDF أو XFDF ولكن أيضًا إلى ملف XML. تستخدم جميع هذه الملفات صيغة مختلفة لحفظ قيم حقول النموذج في PDF. المثال أدناه يوضح الفروقات.

لنفترض أن هناك بعض حقول النموذج في PDF والتي تحتاج قيمها إلى العرض في أشكال FDF وXML وXFDF. تظهر حقول النموذج المفترضة هذه مع أسماء الحقول والقيم أدناه:

|**اسم الحقل**|**قيمة الحقل**|
| :- | :- |
|Company|Aspose.com|
|Address.1|سيدني، أستراليا|
|Address.2|خط عنوان إضافي|
لنرى كيف نمثل هذه القيم في تنسيقات FDF وXML وXFDF.

### ما هو تنسيق FDF؟

كما نعلم أن ملف FDF يخزن البيانات بشكل زوج مفتاح/قيمة حيث يمثل /T مفتاحًا، ويمثل /V القيمة والبيانات بين الأقواس () تمثل محتوى إما مفتاح أو قيمة. /T(Company) /V(Aspose.com) /T(Address.1) /V( سيدني ، أستراليا ) /T(Address.2) /V(سطر عنوان إضافي)

### ما هو تنسيق XML؟

يمكن للمطورين تمثيل كل حقل في نموذج PDF في شكل علامة حقل، `<field>`. تحتوي كل علامة حقل على سمة، الاسم الذي يظهر اسم الحقل وعلامة فرعية، `<value>` تمثل قيمة الحقل كما هو موضح أدناه:

```xml
 <?xml version="1.0" ?>
 <fields>
  <field name="Company">
    <value>Aspose.com</value>
  </field>
  <field name="Address.1">
    <value>Sydney, Australia</value>
  </field>
  <field name="Address.2">
    <value>Additional Address Line</value>
  </field>
 </fields>
```

### ### ما هو تنسيق XFDF؟

تمثيل البيانات أعلاه في شكل XFDF مشابه لشكل XML باستثناء بعض الاختلافات. في ملفات XFDF، نضيف مساحة الأسماء الخاصة بهم، وهي <http://ns.adpbe.com/xfdf/> وهناك علامة إضافية، `<f>` التي تُستخدم للإشارة إلى مستند PDF الذي يحتوي على حقول النموذج هذه. مثل XML، يحتوي XFDF أيضًا على حقول في شكل علامات الحقول، `<field>` كما هو موضح أدناه:

```xml

<?xml version="1.0" encoding="UTF-8"?>
<xfdf xmlns="http://ns.adobe.com/xfdf/" xml:space="preserve">   
   <f href="CompanyForm.pdf"/> 
   <fields>
      <field name="Company">
         <value>Aspose.com</value>
      </field>
      <field name="Address">
         <field name="1">
            <value>سيدني، أستراليا</value>
         </field>
         <field name="2">
            <value>سطر عنوان إضافي</value>
         </field>
      </field>
   </fields>
 </xfdf>
```

### تحديد أسماء حقول النموذج

يوفر Aspose.PDF for .NET القدرة على إنشاء وتعديل وملء النماذج PDF التي تم إنشاؤها بالفعل. It contains [Form](https://reference.aspose.com/pdf/net/aspose.pdf.facades/form) class, which has the function named [FillField](https://reference.aspose.com/pdf/net/aspose.pdf.facades/form/methods/fillfield/index) , and it takes two parameters i.e. Field name that needs to be filled, and the field value. So in-order to fill the form fields, you must be aware of the exact form field name.  
نواجه غالبًا السيناريو الذي نحتاج فيه إلى ملء النموذج الذي تم إنشاؤه في أداة معينة أي. 
Adobe Designer، ونحن لسنا متأكدين من أسماء حقول النموذج. لتحقيق متطلباتنا، نحتاج إلى قراءة أسماء جميع حقول النموذج في PDF. توفر فئة [Form](https://reference.aspose.com/pdf/net/aspose.pdf.facades/form) خاصية تسمى [FieldsNames](https://reference.aspose.com/pdf/net/aspose.pdf.facades/form/properties/fieldnames) التي تعيد جميع أسماء الحقول وتعيد قيمة null إذا لم يكن في PDF أي حقل. لكن هذه الخاصية ستعيد جميع أسماء حقول النموذج في PDF ولن نكون متأكدين من الاسم الذي يتوافق مع أي حقل في النموذج.

كحل لهذه المشكلة، سنحتاج إلى سمات المظهر لكل حقل.
``` [Form](http://www.aspose.com/documentation/file-format-components/aspose.pdf.kit-for-.net-and-java/aspose.pdf.kit.form.html) تحتوي على دالة باسم GetFieldFacade والتي تُرجع السمات، بما في ذلك الموقع، اللون، نمط الحدود، الخط، عنصر القائمة وهكذا. لحفظ هذه القيم، سنستخدم فئة [FormFieldFacade](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formfieldfacade)، التي تُستخدم لتسجيل السمات البصرية للحقل. بمجرد الحصول على هذه السمات، يمكننا إضافة حقل نصي تحت كل حقل يعرض اسم الحقل. هنا يبرز سؤال حول كيفية تحديد الموقع الذي سنضيف فيه الحقل النصي؟ الحل لهذه المشكلة هو خاصية Box في فئة [FormFieldFacade](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formfieldfacade)، التي تحتفظ بموقع الحقل. سنقوم بحفظ هذه القيم في مصفوفة من نوع مستطيل واستخدام هذه القيم لتحديد الموقع الذي سنضيف فيه الحقول النصية الجديدة.

في مساحة الاسم Aspose.Pdf.Facades، لدينا فئة باسم [FormEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor) التي توفر القدرة على معالجة نموذج PDF. افتح نموذج PDF وأضف حقل نص أسفل كل حقل نموذج موجود واحفظ نموذج PDF باسم جديد.

{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-TechnicalArticles-DifferenceBetweenFile-DifferenceBetweenFile.cs" >}}