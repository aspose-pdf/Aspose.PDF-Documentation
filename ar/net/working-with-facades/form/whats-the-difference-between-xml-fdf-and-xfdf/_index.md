---
title: ما هو الفرق بين تنسيقات FDF و XML و XFDF
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 30
url: /ar/net/whats-the-difference-between-xml-fdf-and-xfdf/
description: يوضح هذا القسم الفرق بين نماذج XML و FDF و XFDF باستخدام واجهات Aspose.PDF من خلال فئة النموذج.
lastmod: "2021-06-05"
draft: false
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Whats is the difference between FDF, XML, and XFDF formats",
    "alternativeHeadline": "Understanding FDF, XML, and XFDF Formats in Aspose.PDF for .NET",
    "abstract": "اكتشف الفروق بين تنسيقات FDF و XML و XFDF في معالجة بيانات نموذج PDF من خلال Aspose.PDF for .NET. تتيح هذه الميزة للمطورين تصدير قيم حقول النموذج التفاعلية بسلاسة في تنسيقات مختلفة، كل منها له بناءه الخاص، مع تعزيز الفهم واستخدام هذه الأنواع الأساسية من الملفات في معالجة PDF. قم بتحسين معالجة نموذج PDF الخاص بك مع رؤى مفصلة حول كيفية تمثيل حقول النموذج عبر تنسيقات بيانات مختلفة.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "1045",
    "proficiencyLevel": "Beginner",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDF for .NET",
        "url": "https://products.aspose.com/pdf",
        "logo": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-net.svg",
        "alternateName": "Aspose",
        "sameAs": [
            "https://facebook.com/aspose.pdf/",
            "https://twitter.com/asposepdf",
            "https://www.youtube.com/channel/UCmV9sEg_QWYPi6BJJs7ELOg/featured",
            "https://www.linkedin.com/company/aspose",
            "https://stackoverflow.com/questions/tagged/aspose",
            "https://aspose.quora.com/",
            "https://aspose.github.io/"
        ],
        "contactPoint": [
            {
                "@type": "ContactPoint",
                "telephone": "+1 903 306 1676",
                "contactType": "sales",
                "areaServed": "US",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+44 141 628 8900",
                "contactType": "sales",
                "areaServed": "GB",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+61 2 8006 6987",
                "contactType": "sales",
                "areaServed": "AU",
                "availableLanguage": "en"
            }
        ]
    },
    "url": "/net/whats-the-difference-between-xml-fdf-and-xfdf/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/whats-the-difference-between-xml-fdf-and-xfdf/"
    },
    "dateModified": "2024-11-25",
    "description": "يمكن لـ Aspose.PDF تنفيذ المهام البسيطة والسريعة وكذلك التعامل مع الأهداف الأكثر تعقيدًا. تحقق من القسم التالي للمستخدمين المتقدمين والمطورين."
}
</script>

{{% alert color="primary" %}}

لقد خلطنا العديد من المصطلحات المختلفة مثل FDF و XML و XFDF. جميع هذه المصطلحات مرتبطة ببعضها البعض بطريقة ما. تستكشف هذه المقالة هذه المفاهيم وعلاقتها ببعضها البعض.

{{% /alert %}}

## فك رموز النماذج

Aspose.PDF for .NET تُستخدم للتلاعب بمستندات PDF المعيارية من قبل Adobe. وتحتوي مستندات PDF على نماذج تفاعلية تُسمى AcroForms. تحتوي هذه النماذج التفاعلية على عدد من حقول النموذج، مثل قائمة منسدلة، مربع نص، وزر اختيار. تعمل نماذج Adobe التفاعلية، وحقول النموذج، بنفس طريقة نموذج HTML وحقوله.

من الممكن تخزين قيم حقول النموذج في ملف منفصل: ملف FDF (تنسيق بيانات النموذج). يحتوي هذا على قيم حقول النموذج بطريقة مفتاح/قيمة. لا تزال تُستخدم ملفات FDF لهذا الغرض. لكن Adobe تقدم أيضًا نوعًا مشفرًا من FDF يُسمى XFDF. يقوم ملف XFDF بتخزين قيم حقول النموذج بطريقة هرمية باستخدام علامات XML.

مع Aspose.PDF، يمكن للمطورين تصدير قيم حقول نموذج PDF إلى ملف FDF أو XFDF، ولكن أيضًا إلى ملف XML. تستخدم جميع هذه الملفات بناءً مختلفًا لحفظ قيم حقول نموذج PDF. يوضح المثال أدناه الفروق.

لنفرض أن هناك بعض حقول نموذج PDF التي تحتاج قيمها إلى أن تُعرض في تنسيقات FDF و XML و XFDF. تُظهر حقول النموذج المفترضة مع أسماء حقولها وقيمها أدناه:

|**اسم الحقل**|**قيمة الحقل**|
| :- | :- |
|الشركة|Aspose.com|
|العنوان.1|سيدني، أستراليا|
|العنوان.2|خط عنوان إضافي|
دعونا نرى كيف يمكن تمثيل هذه القيم في تنسيقات FDF و XML و XFDF.

### ما هو تنسيق FDF؟

كما نعلم، يقوم ملف FDF بتخزين البيانات بطريقة مفتاح/قيمة حيث يمثل /T مفتاحًا، و /V يمثل القيمة والبيانات في الأقواس () تمثل محتوى إما مفتاح أو قيمة. على سبيل المثال، /T(Company) تعني أن Company هو مفتاح الحقل و /V(Aspose.com) مخصص لقيمة الحقل.

/T(Company) /V(Aspose.com)
/T(Address.1) /V( Sydney , Australia )
/T(Address.2) /V(Additional Address Line)

### ما هو تنسيق XML؟

يمكن للمطورين تمثيل كل حقل من حقول نموذج PDF في شكل علامة حقل، `<field>`. تحتوي كل علامة حقل على سمة، name تُظهر اسم الحقل وعلامة فرعية، `<value>` تمثل قيمة الحقل كما هو موضح أدناه:

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

### ما هو تنسيق XFDF؟

تمثيل البيانات أعلاه في شكل XFDF مشابه لشكل XML باستثناء بعض الاختلافات. في ملفات XFDF، نضيف مساحة أسماء XML الخاصة بهم، وهي <http://ns.adpbe.com/xfdf/> وهناك علامة إضافية، `<f>` تُستخدم للإشارة إلى مستند PDF الذي يحتوي على هذه الحقول. مثل XML، يحتوي XFDF أيضًا على حقول في شكل علامات حقل، `<field>` كما هو موضح أدناه:

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
            <value>Sydney, Australia</value>
         </field>
         <field name="2">
            <value>Additional Address Line</value>
         </field>
      </field>
   </fields>
 </xfdf>
```

### تحديد أسماء حقول النموذج

Aspose.PDF for .NET توفر القدرة على إنشاء وتحرير وملء نماذج PDF التي تم إنشاؤها مسبقًا. تحتوي على فئة [Form](https://reference.aspose.com/pdf/net/aspose.pdf.facades/form) ، والتي تحتوي على وظيفة تُسمى [FillField](https://reference.aspose.com/pdf/net/aspose.pdf.facades/form/methods/fillfield/index) ، وتأخذ معلمين، أي اسم الحقل الذي يحتاج إلى ملء، وقيمة الحقل. لذا، لملء حقول النموذج، يجب أن تكون على دراية باسم حقل النموذج الدقيق.
غالبًا ما نواجه سيناريو نحتاج فيه إلى ملء النموذج الذي تم إنشاؤه في أداة ما، أي Adobe Designer، ولسنا متأكدين من أسماء حقول النموذج. لتحقيق متطلباتنا، نحتاج إلى قراءة أسماء جميع حقول نموذج PDF. توفر فئة [Form](https://reference.aspose.com/pdf/net/aspose.pdf.facades/form) خاصية تُسمى [FieldsNames](https://reference.aspose.com/pdf/net/aspose.pdf.facades/form/properties/fieldnames) التي تُرجع جميع أسماء الحقول وتُرجع null إذا لم يكن هناك حقل في PDF. لكن هذه الخاصية ستُرجع جميع أسماء حقول نموذج PDF ولن نكون متأكدين من أي اسم يتوافق مع أي حقل في النموذج.

كحل لهذه المشكلة، سنحتاج إلى سمات المظهر لكل حقل. تحتوي فئة [Form](http://www.aspose.com/documentation/file-format-components/aspose.pdf.kit-for-.net-and-java/aspose.pdf.kit.form.html) على وظيفة تُسمى GetFieldFacade التي تُرجع السمات، بما في ذلك الموقع، اللون، نمط الحدود، الخط، عناصر القائمة، وما إلى ذلك. لحفظ هذه القيم، سنستخدم فئة [FormFieldFacade](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formfieldfacade) ، والتي تُستخدم لتسجيل السمات البصرية للحقول. بمجرد أن نحصل على هذه السمات، يمكننا إضافة حقل نصي تحت كل حقل يعرض اسم الحقل. هنا تبرز سؤال حول كيفية تحديد الموقع الذي نضيف فيه حقل النص؟ الحل لهذه المشكلة هو خاصية Box في فئة [FormFieldFacade](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formfieldfacade) ، التي تحتفظ بموقع الحقل. سنقوم بحفظ هذه القيم في مصفوفة من نوع المستطيل واستخدام هذه القيم لتحديد الموضع الذي نضيف فيه حقول النص الجديدة.
في مساحة أسماء Aspose.Pdf.Facades، لدينا فئة تُسمى [FormEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor) التي توفر القدرة على التلاعب بنموذج PDF. افتح نموذج PDF وأضف حقل نصي تحت كل حقل نموذج موجود واحفظ نموذج PDF باسم جديد.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.Pdf-for-.NET
private static void DifferenceBetweenFile()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_TechnicalArticles();

    // First a input pdf file should be assigned
    using (var form = new Aspose.Pdf.Facades.Form(dataDir + "FilledForm.pdf"))
    {
        // Get all field names
        String[] allfields = form.FieldNames;
        // Create an array which will hold the location coordinates of Form fields
        var box = new System.Drawing.Rectangle[allfields.Length];
        for (int i = 0; i < allfields.Length; i++)
        {
            // Get the appearance attributes of each field, consecutively
            var facade = form.GetFieldFacade(allfields[i]);
            // Box in FormFieldFacade class holds field's location.
            box[i] = facade.Box;
        }
        // Save PDF document
        form.Save(dataDir + "DifferenceBetweenFile_out.pdf");
            
        // Open PDF document
        using (var document = new Aspose.Pdf.Document(dataDir + "FilledForm - 2.pdf"))
        {
            // Now we need to add a textfield just upon the original one
            FormEditor editor = new Aspose.Pdf.Facades.FormEditor(document);
            for (int i = 0; i < allfields.Length; i++)
            {
                // Add text field beneath every existing form field
                editor.AddField(Aspose.Pdf.Facades.FieldType.Text, "TextField" + i, allfields[i], 1, box[i].Left, box[i].Top, box[i].Left + 50, box[i].Top + 10);
            }
            // Save PDF document
            editor.Save(dataDir + "DifferenceBetweenFile_out.pdf");
        }
    }
}
```