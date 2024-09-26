---
title: تحكم تصدير GridView إلى PDF في Visual Studio
type: docs
weight: 10
url: /net/visual-studio-export-gridview-to-pdf-control/
---

## مقدمة

تحكم تصدير GridView إلى PDF هو تحكم خادم ASP.NET يسمح بتصدير محتويات GridView إلى مستند PDF باستخدام [Aspose.PDF](http://www.aspose.com/.net/pdf-component.aspx). يضيف زر **تصدير إلى PDF** في أعلى تحكم GridView. عند النقر على الزر، يقوم تلقائيًا بتصدير محتوى تحكم GridView إلى مستند PDF ثم يقوم تلقائيًا بتنزيل الملف المُصدر إلى موقع القرص الذي يختاره المستخدم في غضون ثوانٍ.

### ميزات الوحدة

توفر هذه النسخة الأولية من التحكم الميزات التالية:

- احصل على نسخة غير متصلة من محتوى GridView المفضل لديك عبر الإنترنت للتحرير والمشاركة والطباعة في مستند PDF الشائع جدًا.
- موروث من تحكم GridView الافتراضي في ASP.NET وبالتالي يمتلك جميع ميزاته وخصائصه.
- يعمل مع جميع إصدارات .NET بدءًا من .NET 2.0.
- القدرة على تخصيص/توطين نص زر التصدير.
- القدرة على تخصيص/تحليل نص زر التصدير.
- خيار التصدير بوضع العرض في حال كان محتوى GridView أوسع ولا يتناسب في وضع الصورة الافتراضي
- تطبيق مظهر وإحساس النمط الخاص بك على زر التصدير باستخدام css.
- خيار إضافة عنوان مخصص في أعلى المستند المصدر
- خيار حفظ كل مستند مُصدر على الخادم في مسار قرص قابل للتكوين
- خيار تصدير الصفحة الحالية أو جميع الصفحات عند تمكين الترقيم

## متطلبات النظام والمنصات المدعومة

### متطلبات النظام

يمكن استخدام تحكم تصدير GridView إلى Pdf لـ Visual Studio على أي نظام يحتوي على IIS و.NET framework 2.0 أو أعلى.

### المنصات المدعومة

يدعم تحكم تصدير GridView إلى Pdf لـ Visual Studio جميع إصدارات ASP.NET التي تعمل على .NET framework 2.0 أو أعلى. يمكنك استخدام أي من إصدارات Visual Studio التالية لاستخدام هذا التحكم في تطبيقات ASP.NET الخاصة بك

- Visual Studio 2005
- Visual Studio 2008
- Visual Studio 2010
- Visual Studio 2012
- Visual Studio 2013

## التنزيل
## تحميل

يمكنك تحميل تحكم تصدير GridView إلى PDF من أحد المواقع التالية

- [CodePlex](https://asposevs.codeplex.com/releases/view/617022)
- [Github](https://github.com/aspose-pdf/Aspose.PDF-for-.NET/releases/tag/AsposeExportGridViewToPdfControl_1.0)

## تثبيت

من السهل جداً وبسيط تثبيت تحكم تصدير GridView إلى PDF، يرجى اتباع هذه الخطوات البسيطة

### **لـ Visual Studio 2010، 2012 و 2013**

1. استخراج ملف zip المحمل، أي Aspose.PDF.GridViewExport_1.0.zip
1. انقر نقراً مزدوجاً على الملف VSIX Aspose.PDF.GridViewExport.vsix
1. ستظهر نافذة تعرض الإصدارات المتوفرة والمدعومة من Visual Studio المثبتة على جهازك
1. اختر الإصدارات التي تريد إضافة تحكم تصدير GridView إلى PDF إليها.
1. انقر على تثبيت

ستحصل على نافذة نجاح بمجرد اكتمال التثبيت.

**ملاحظة:** يُرجى التأكد من إعادة تشغيل Visual Studio لتفعيل التغييرات.

### **لـ Visual Studio 2005، 2008 والإصدارات Express**

يرجى اتباع هذه الخطوات لدمج تحكم تصدير GridView إلى PDF في Visual Studio لسهولة السحب والإفلات تماماً مثل تحكمات ASP.NET الأخرى
يرجى اتباع هذه الخطوات لدمج تحكم تصدير GridView إلى PDF في Visual Studio لسهولة السحب والإفلات مثل باقي عناصر التحكم في ASP.NET

1. استخرج ملف الضغط الذي تم تنزيله أي Aspose.PDF.GridViewExport.NET2.0_1.0.zip
1. تأكد من تشغيل Visual Studio كمسؤول

في قائمة الأدوات، انقر على اختيار عناصر مربع الأدوات.

1. انقر على استعراض.
   سيظهر مربع الحوار فتح.
1. تصفح إلى المجلد المستخرج واختر Aspose.PDF.GridViewExport.dll
1. انقر على موافق.

عند فتح عنصر تحكم aspx أو ascx في مربع الأدوات الجانبي سترى ExportGridViewToPdf تحت علامة التبويب العامة

![todo:image_alt_text](visual-studio-export-gridview-to-pdf-control_2.png)

## الاستخدام

بعد التثبيت، من السهل جدًا البدء في استخدام هذا التحكم في تطبيقاتك ASP.NET

|**لإطار عمل .NET 4.0 وما فوق**|**لإطار عمل .NET 2.0 وما فوق**|** |
| :- | :- | :- |
|للتطبيقات التي تعمل في إطار عمل .NET 4.0 وما فوق في Visual Studio 2010 وما فوق، يجب أن ترى تحكم **ExportGridViewToPdf** في علامة التبويب **Aspose** في شريط الأدوات كما هو موضح أدناه.
| للتطبيقات التي تعمل على إطار .NET الإصدار 4.0 فأعلى في Visual Studio 2010 فأعلى، يجب أن ترى عنصر التحكم **ExportGridViewToPdf** في علامة تبويب **Aspose** في شريط الأدوات كما هو موضح أدناه.

### إضافة عنصر التحكم ExportGridViewToPdf يدويًا

إذا كانت لديك أي مشاكل باستخدام الطرق المذكورة أعلاه التي تستخدم مربع أدوات Visual Studio، يمكنك إضافة هذا العنصر يدويًا إلى تطبيقك ASP.NET الذي يعمل على أي إطار .NET أكبر من 2.0

1. إذا كنت تستخدم Visual Studio تأكد من تشغيله كمسؤول
1. أضف مرجعًا إلى **Aspose.PDF.GridViewExport.dll** المتوفر في حزمة التنزيل المستخرجة في مشروع ASP.NET أو تطبيق الويب الخاص بك. تأكد من أن تطبيق الويب/Visual Studio لديك يمتلك حق الوصول الكامل إلى هذا المجلد وإلا قد تحصل على استثناء بأن الوصول ممنوع.
1. أضف هذا السطر إلى أعلى الصفحة، العنصر أو الصفحة الرئيسية

```csharp
 <%@ Register assembly="Aspose.PDF.GridViewExport" namespace="Aspose.PDF.GridViewExport" tagprefix="aspose" %>
```
```csharp
<aspose:ExportGridViewToPdf ID="ExportGridViewToPdf1" runat="server"></aspose:ExportGridViewToPdf>
```

### الأسئلة الشائعة

الأسئلة والمشاكل الشائعة التي قد تواجهها أثناء استخدام هذا التحكم

<div class="schema-faq-code" itemscope="" itemtype="https://schema.org/FAQPage">
    <div itemscope="" itemprop="mainEntity" itemtype="https://schema.org/Question" class="faq-question">
        <h3 itemprop="name" class="faq-q">1. لا أستطيع رؤية تحكم ExportGridViewToPdf في صندوق الأدوات</h3>
        <div itemscope="" itemprop="acceptedAnswer" itemtype="https://schema.org/Answer">
            <div itemprop="text" class="faq-a">
                <p><strong>Visual Studio 2010 والإصدارات الأحدث</strong></p>
<ol><li>تأكد من أنك قمت بتثبيت هذا التحكم باستخدام ملف امتداد VSIX الموجود في الحزمة التي تم تنزيلها. للتحقق اذهب إلى الأدوات -&gt; الإضافات والتحديثات. تحت القسم المثبت يجب أن ترى 'Aspose Export Export GridView To Pdf Control'. إذا لم تراه يرجى محاولة إعادة تثبيته</li>
<li>تأكد من أن تطبيق الويب الخاص بك يعمل في إطار .NET الإصدار 4.0 أو أعلى، للإصدارات الأقل من إطار .NET يرجى التحقق من الطريقة البديلة أعلاه.

<li>تأكد من أن تطبيق الويب الخاص بك يعمل في إطار .NET الإصدار 4.0 أو أعلى، بالنسبة للإصدارات الأقل من إطار .NET يرجى التحقق من الطريقة البديلة أعلاه.
إصدارات قديمة من Visual Studio</li>
<li>تأكد من أنك قد أضفت هذا العنصر يدويًا إلى مجموعة الأدوات الخاصة بك حسب التعليمات المذكورة أعلاه.</li></ol>
          </div>
        </div>
    </div>

    <div itemscope="" itemprop="mainEntity" itemtype="https://schema.org/Question" class="faq-question">
        <h3 itemprop="name" class="faq-q">2. أتلقى خطأ 'الوصول مرفوض' عند تشغيل التطبيق</h3>
        <div itemscope="" itemprop="acceptedAnswer" itemtype="https://schema.org/Answer">
             <div itemprop="text" class="faq-a">
               <ol>
               <li>إذا كنت تواجه هذه المشكلة على الإنتاج، فتأكد من نسخ كل من Aspose.PDF.dll و Aspose.PDF.GridViewExport.dll إلى مجلد bin الخاص بك.</li>
               <li>إذا كنت تستخدم Visual Studio تأكد من تشغيله كمسؤول حتى لو كنت قد سجلت الدخول بالفعل كمسؤول.</li>
```

<li>إذا كنت تستخدم Visual Studio تأكد من تشغيله كمسؤول حتى لو كنت قد سجلت الدخول بالفعل كمدير.</li>
</ol>
</div>
</div>
</div>
</div>

### **خصائص تحكم تصدير Aspose .NET Export GridView إلى PDF**

الخصائص التالية متاحة لتكوين واستخدام الميزات الرائعة التي يوفرها هذا التحكم

|**اسم الخاصية**|**النوع**|**مثال/القيم الممكنة**|**الوصف**|
| :- | :- | :- | :- |
|ExportButtonText|string|تصدير إلى Pdf|يمكنك استخدام هذه الخاصية لتجاوز النص الافتراضي الموجود|
|ExportButtonCssClass|string|btn btn-primary|فئة Css التي يتم تطبيقها على القسم الخارجي لزر التصدير. لتطبيق css على الزر يمكنك استخدام .yourClass input|
|ExportInLandscape|bool|صحيح أو خطأ|إذا كان صحيحًا فإنه يغير توجه الوثيقة الناتجة إلى الوضع الأفقي. الافتراضي هو العمودي|
| | | | |
|ExportFileHeading|string|تقرير مثال على تصدير GridView|يمكنك استخدام علامات html لإضافة أناقة إلى العنوان الخاص بك|
|ExportOutputPathOnServer|string|c:/temp|مسار القرص المحلي على الخادم حيث يتم حفظ نسخة من التصدير تلقائيًا.|
```
|ExportOutputPathOnServer|string|c:/temp|مسار القرص المحلي على الخادم حيث يتم حفظ نسخة من التصدير تلقائيًا.
|ExportDataSource|object|allRowsDataTable|يحدد الكائن الذي يسترجع منه عنصر التحكم المرتبط بالبيانات قائمة العناصر البيانية. يجب أن يحتوي الكائن على جميع البيانات التي يجب تصديرها. يتم استخدام هذه الخاصية بالإضافة إلى خاصية DataSource العادية وهي مفيدة عند تمكين الترقيم الصفحي المخصص وتقوم الصفحة الحالية فقط بجلب الصفوف التي يتم عرضها على الشاشة.
|LicenseFilePath|string| |المسار المحلي على الخادم لملف الترخيص. على سبيل المثال c:/inetpub/Aspose.PDF.lic|

مثال على التحكم في تصدير GridView إلى Pdf مع استخدام جميع الخصائص موضح أدناه

```csharp
<aspose:ExportGridViewToPdf Width="800px" ID="ExportGridViewToPdf1" ExportButtonText="Export to Pdf"
    CssClass="table table-hover table-bordered" ExportButtonCssClass="myClass" ExportOutputFormat="Doc"
    ExportInLandscape="true" ExportOutputPathOnServer="c:\\temp" ExportFileHeading="<h4>Example Report</h4>"
    OnPageIndexChanging="ExportGridViewToPdf1_PageIndexChanging" PageSize="5" AllowPaging="True"
    LicenseFilePath="c:\\inetpub\\Aspose.PDF.lic"
    runat="server" CellPadding="4" ForeColor="#333333" GridLines="Both">
</aspose:ExportGridViewToPdf>
```
## عرض الفيديو

يرجى التحقق من [الفيديو](https://www.youtube.com/watch?v=WNJ7T8u4JlM) أدناه لرؤية الوحدة وهي تعمل.

### الدعم

منذ الأيام الأولى لـ Aspose، كنا نعلم أن تقديم منتجات جيدة لعملائنا لن يكون كافيًا. كان يجب علينا أيضًا تقديم خدمة جيدة. نحن مطورون بأنفسنا ونفهم مدى الإحباط عندما يمنعك خلل فني أو خصوصية في البرنامج من القيام بما تحتاج إلى القيام به. نحن هنا لحل المشكلات، لا لخلقها.

لهذا السبب نقدم الدعم المجاني. أي شخص يستخدم منتجنا، سواء اشتروه أو يستخدمون تقييمًا، يستحق كامل اهتمامنا واحترامنا.

يمكنك تسجيل أي مشاكل أو اقتراحات متعلقة بهذا الـ Pdf باستخدام أي من المنصات التالية

- [CodePlex](https://asposevs.codeplex.com/workitem/list/basic)
- [Visual Studio Gallery - Q and A](https://visualstudiogallery.msdn.microsoft.com/fb8b9944-cfe5-44a9-8aa7-c785d32d1066)
- [Github](https://github.com/aspose-pdf/Aspose.PDF-for-.NET/issues)
- [Microsoft Developer Network - Q and A](https://code.msdn.microsoft.com/Aspose-NET-Export-GridView-caddbb6d/view/Discussions#content)
- [شبكة مطوري مايكروسوفت - الأسئلة والأجوبة](https://code.msdn.microsoft.com/Aspose-NET-Export-GridView-caddbb6d/view/Discussions#content)

### توسيع والمساهمة

Aspose .NET لتصدير GridView إلى Pdf لـ Visual Studio مفتوح المصدر ورمزه المصدري متاح على مواقع التواصل الاجتماعي الرئيسية المدرجة أدناه. يُشجع المطورون على تنزيل الرمز المصدري وتوسيع وظائفه حسب متطلباتهم الخاصة.

#### رمز المصدر

يمكنك الحصول على أحدث رمز مصدري من إحدى المواقع التالية

- [CodePlex](https://asposevs.codeplex.com/SourceControl/latest#Aspose.PDF.GridViewExport/)
- [Github](https://github.com/aspose-pdf/Aspose.PDF-for-.NET/tree/master/Plugins/Visual%20Studio/Aspose.PDF.GridViewExport)

#### كيفية تكوين الرمز المصدري

يجب أن يكون لديك ما يلي مثبتًا لفتح وتوسيع الرمز المصدري

- Visual Studio 2010

يرجى اتباع هذه الخطوات البسيطة للبدء

1. قم بتنزيل/استنساخ الرمز المصدري.
1.

1. تصفح إلى أحدث شفرة مصدر قمت بتنزيلها وافتح **Aspose.PDF.GridViewExport.sln**

#### نظرة عامة على الشفرة المصدرية

هناك ثلاثة مشاريع في الحل

- Aspose.PDF.GridViewExport - يحتوي على حزمة VSIX و Server Pdf لـ .NET 4.0.
- Aspose.PDF.GridViewExport_DotNet_2.0 - GridView Pdf موسع لـ .NET 2.0
- Aspose.PDF.GridViewExport.Website - مشروع ويب لاختبار GridView Pdf القابل للتصدير إلى Word
```
