 ---
title: استخدام Aspose.Pdf لـ .NET مع Coldfusion
type: docs
weight: 300
url: ar/net/using-aspose-pdf-for-net-with-coldfusion/
description: يجب عليك العمل مع Aspose.Pdf لـ .NET مع Coldfusion باستخدام فئة PdfFileInfo
lastmod: "2021-07-14"
draft: false
---

{{% alert color="primary" %}}

في هذا المقال، سنشرح كيفية استخدام Aspose.PDF لـ .NET مع Coldfusion. سيساعدك ذلك على فهم تفاصيل تكامل Aspose.PDF لـ .Net و Coldfusion. بمساعدة مثال بسيط، سأريكم عملية دمج وظائف Aspose.PDF لـ .Net في تطبيقات Coldfusion الخاصة بك.

{{% /alert %}}

## الخلفية

Aspose.PDF لـ .NET هو مكون يوفر أيضًا القدرة على تحرير ومعالجة ملفات PDF الموجودة.
Aspose.PDF لـ .NET هو مكون يوفر أيضًا القدرة على تحرير ومعالجة ملفات PDF الموجودة.

## المتطلبات الأولية

لكي تتمكن من تشغيل Aspose.PDF لـ .Net مع Coldfusion، ستحتاج إلى IIS، .Net 2.0، وColdfusion. لقد اختبرت المكون باستخدام IIS 5، .Net 2.0، وColfusion 8. هناك شيئان آخران يجب التأكد منهما أثناء تثبيت Coldfusion. أولاً، يجب تحديد أي موقع (مواقع) تحت IIS سيعمل تحته Coldfusion. ثانيًا، ستحتاج إلى اختيار "خدمات تكامل .Net" من مثبت Coldfusion. تسمح لك خدمات تكامل .Net بالوصول إلى تجميع مكونات .Net في تطبيقات Coldfusion؛ في هذه الحالة سيكون المكون هو Aspose.PDF لـ .NET.

## الشرح

أولاً عليك نسخ الملف DLL (Aspose.PDF .dll) إلى موقع ستقوم بالوصول إليه لاستخدامه لاحقًا؛ سيتم تعيين هذا كمسار وتعيينه لسمة التجميع في علامة cfobject كما هو موضح أدناه:

```html
<cfobject type = ".NET" name = "fileinfo" 
        class = "Aspose.PDF.Facades.PdfFileInfo" 
        assembly = "C:/Aspose/Net/Assembly/Aspose.PDF.dll">
```
سمة الفئة في العلامة أعلاه تشير إلى فئة Aspose.PDF. Facades، وفي هذه الحالة هي PdfFileInfo. سمة الاسم هي اسم مثيل الفئة وسيتم استخدامه لاحقًا في الكود للوصول إلى طرق أو خصائص الفئة. سمة النوع تحدد نوع المكون - في حالتنا هو .Net.

نقطة مهمة يجب أن تضعها في اعتبارك أثناء استخدام مكون .Net في Coldfusion هي أنه، عندما تحصل على أي خاصية لكائن الفئة أو تضبطها، يجب عليك اتباع هيكل محدد. لضبط خاصية ستستخدم بناء الجملة مثل Set_propertyname، وللحصول على قيمة خاصية ستستخدم Get_propertyname.

على سبيل المثال

ضبط قيمة خاصية:

```html
<cfset FilePath = ExpandPath("guide.pdf")>
```

الحصول على قيمة خاصية:

```html
<cfoutput>#fileinfo.Get_title()#</cfoutput>
```

مثال أساسي ولكن كامل لمساعدتك على فهم عملية استخدام Aspose.PDF لـ .NET في Coldfusion موضح أدناه.

### دعنا نعرض معلومات ملف PDF

```html
<!--- create an instance of PdfFileInfo class --->

<cfobject type = ".NET" name = "fileinfo" class = "Aspose.PDF.Facades.PdfFileInfo"

assembly = "C:/Aspose/Net/Assembly/Aspose.PDF.dll">

<!--- get pdf file path --->

<cfset FilePath = ExpandPath("guide.pdf")>

<!--- assign pdf file path to the class object by setting its inputfile property--->

<cfset fileinfo.Set_inputfile(FilePath)>

<!--- Show file info --->

<cfoutput><b>Title:</b>#fileinfo.Get_title()#</cfoutput><br/>
<cfoutput><b>Subject:</b>#fileinfo.Get_subject()#</cfoutput><br/>
<cfoutput><b>Author:</b>#fileinfo.Get_author()#</cfoutput><br/>
<cfoutput><b>Creator:</b>#fileinfo.Get_Creator()#</cfoutput><br/>

```
## الخاتمة

{{% alert color="primary" %}}
في هذا المقال، رأينا أنه إذا اتبعنا بعض القواعد الأساسية لتكامل Coldfusion و.Net، يمكننا دمج الكثير من الوظائف والمرونة المتعلقة بتلاعب مستندات PDF، باستخدام Aspose.PDF لـ .NET في تطبيقات Coldfusion الخاصة بنا.
{{% /alert %}}
