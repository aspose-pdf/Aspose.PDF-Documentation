---
title: Aspose.PDF لـ .NET عبر COM Interop
type: docs
weight: 20
url: /ar/net/use-aspose-pdf-for-net-via-com-interop/
---

{{% alert color="primary" %}}

المعلومات في هذا الموضوع تنطبق على السيناريوهات التي تريد استخدام [Aspose.PDF لـ .NET](/pdf/ar/net/) عبر COM Interop في أي من لغات البرمجة التالية:

- ASP
- Delphi
- JScript
- Perl
- PHP
- PowerBuilder
- Python
- VBScript
- Visual Basic
- C++

{{% /alert %}}

## العمل مع COM Interop

يتم تنفيذ Aspose.PDF لـ .NET تحت إشراف إطار عمل .NET ويُعرف هذا بالكود المُدار. يتم تشغيل الكود المكتوب بكل اللغات المذكورة أعلاه خارج إطار عمل .NET ويُعرف بالكود غير المُدار. التفاعل بين الكود غير المُدار وAspose.PDF يحدث عبر وسيلة .NET المعروفة باسم COM Interop.

تعتبر كائنات Aspose.PDF كائنات .NET، ولكن عند استخدامها عبر COM Interop، تظهر ككائنات COM في لغة البرمجة الخاصة بك.
أشياء Aspose.PDF هي أشياء .NET، ولكن عند استخدامها عبر COM Interop، تظهر كأشياء COM في لغة البرمجة الخاصة بك.

{{% alert color="primary" %}}

- في عالم COM نميز بين خادم COM وعميل COM. يخزن خادم COM الفئات COM بينما يطلب عميل COM من خادم COM نسخ فئات، أي أشياء COM.
- عميل COM أو ببساطة تطبيق العميل يمكن أن يعرف عن محتويات فئة COM شيئًا ما أو يكون غير مدرك تمامًا لطرقه وخصائصه. لذلك، يمكن لتطبيق العميل اكتشاف هيكل فئة COM أثناء الترجمة/البناء أو فقط أثناء التنفيذ. يُعرف هذا العملية بالربط ولدينا بالتالي **ربط مبكر** و**ربط متأخر**.
- باختصار، فئة COM مثل صندوق أسود وللعمل معها مطلوب مكتبة الأنواع، هذا الملف الثنائي له وصف لطرق فئة COM وخصائصها وأي لغة عالية المستوى تدعم العمل مع أشياء COM غالبًا ما يكون لديها تعبير نحوي لإضافة مكتبة الأنواع، على سبيل المثال هذا هو [**#import**](http://msdn.microsoft.com/en-us/library/8etzzkb6.aspx) في C++.
- باختصار، فئة COM تشبه الصندوق الأسود وللعمل معها يلزم وجود مكتبة أنواع، هذا الملف الثنائي يحتوي على وصف لطرق وخصائص فئة COM، وأي لغة عالية المستوى تدعم العمل مع كائنات COM غالبًا ما تمتلك تعبير بناء جملة لإضافة مكتبة الأنواع، على سبيل المثال هذا هو [**#import**](http://msdn.microsoft.com/en-us/library/8etzzkb6.aspx) في C++.
- تستخدم مكتبة الأنواع للربط المبكر.
- يمكن لكائن COM أن يكشف عن طرقه وخصائصه بطريقتين: من خلال **واجهة الإرسال** (dispinterface) وفي **جدول الوظائف الافتراضي** (vtable).
- داخل **واجهة الإرسال**، يتم التعرف على كل طريقة وخاصية بواسطة عضو فريد؛ هذا العضو هو معرف الإرسال للوظيفة (أو **DispID**).
- **جدول الوظائف الافتراضي** مجرد مجموعة من مؤشرات الوظائف التي تدعمها واجهة فئة COM.
- الكائن الذي يكشف عن طرقه من خلال كلا الواجهتين يدعم **واجهة مزدوجة**.
- هناك مزايا لكلا نوعي الربط.
- هناك مزايا لكلا نوعي الربط.
- آلية الربط المتأخر لها ميزة كبيرة: إذا قرر مُنشئ مكتبة الـ COM DLL إصدار نسخة جديدة بواجهة وظائف مختلفة، فإن أي كود يستدعي هذه الطرق لن يتعطل ما لم تكن الطرق غير متاحة؛ حتى إذا كانت **vtable** مختلفة، فإن الربط المتأخر يتمكن من اكتشاف DISPIDs الجديدة واستدعاء الطرق المناسبة.

{{% /alert %}}

هذه هي الموضوعات التي ستحتاج في نهاية المطاف إلى إتقانها:
{{% alert color="primary" %}}

- استخدام أجسام COM في لغة البرمجة الخاصة بك. راجع توثيق لغة البرمجة الخاصة بك والموضوعات المحددة للغة في هذا التوثيق.

- العمل مع أجسام COM التي يعرضها .NET COM Interop. راجع [التفاعل مع الكود غير المُدار](http://msdn.microsoft.com/en-us/library/sd10k43k.aspx) و[عرض مكونات إطار .NET لـ COM](http://msdn.microsoft.com/en-us/library/zsfww439%28v=vs.110%29.aspx) في MSDN.

- نموذج كائن مستند Aspose.PDF.
- نموذج كائن مستند Aspose.PDF.

{{% /alert %}}

## سجل Aspose.PDF لـ .NET مع COM Interop

تحتاج إلى تثبيت Aspose.PDF لـ .NET والتأكد من تسجيله مع COM Interop (لضمان إمكانية استدعائه من الكود غير المدار).

{{% alert color="primary" %}}

لتسجيل Aspose.PDF لـ .NET لـ COM Interop يدويًا:

1. من قائمة **البداية**، اختر **جميع البرامج**، ثم **Microsoft Visual Studio**، **أدوات Visual Studio** وأخيرًا **موجه أوامر Visual Studio**.
1. أدخل الأمر لتسجيل التجميع:
   1. .NET Framework 2.0
      regasm "C:\Program Files\Aspose\Aspose.PDF for .NET\bin\net2.0\Aspose.PDF.dll" /codebase
   1. .NET Framework 3.5
      regasm "C:\Program Files\Aspose\Aspose.PDF for .NET\bin\net3.5\Aspose.PDF.dll" /codebase
   1. .NET Framework 4.0
      regasm "C:\Program Files\Aspose\Aspose.PDF for .NET\bin\net4.0\Aspose.PDF.dll" /codebase

{{% /alert %}}

انتبه إلى أن /codebase ضروري فقط إذا لم يكن Aspose.PDF.dll في GAC، باستخدام هذا الخيار يجعل regasm يضع مسار التجميع في السجل.
{{% alert color="primary" %}}

regasm.exe هي أداة مضمنة في .NET Framework SDK. جميع أدوات SDK لـ .NET Framework تقع في الدليل *\Microsoft .NET\Framework\<FrameworkVersion>*، على سبيل المثال *C:\Windows\Microsoft .NET\Framework\v4.0.30319*. إذا كنت تستخدم Visual Studio .NET:
من قائمة **البداية**، اختر **البرامج**، ثم **Microsoft Visual Studio .NET**، تليها **أدوات Visual Studio .NET** وأخيراً **موجه أوامر Visual Studio .NET 2003**.
يشغل موجه الأوامر مع تعيين جميع المتغيرات البيئية اللازمة.

{{% /alert %}}

### ProgIDs

ProgID يعني "معرف برمجي". هو اسم لفئة COM التي تُستخدم لإنشاء كائن. يتكون ProgID من اسم المكتبة "Aspose.PDF" واسم الفئة.

### Type Library

{{% alert color="primary" %}}

إذا كان لغتك البرمجية (مثل Visual Basic أو Delphi) تسمح لك بالإشارة إلى مكتبة نوع COM، فأضف إشارة إلى Aspose.PDF.tlb ولرؤية جميع فئات Aspose.PDF لـ .NET، الطرق، الخصائص والتعدادات في متصفح الكائنات لديك.
إذا كانت لغة البرمجة الخاصة بك (مثل Visual Basic أو Delphi) تسمح لك بالإشارة إلى مكتبة نوع COM، فأضف مرجعًا إلى Aspose.PDF.tlb ولرؤية جميع فئات Aspose.PDF لـ .NET والطرق والخصائص والتعدادات في متصفح الكائن الخاص بك.

لتوليد ملف TLB:

- إطار عمل .NET 2.0
  regasm "C:\Program Files\Aspose\Aspose.PDF for .NET\bin\net2.0\Aspose.PDF.dll" /tlb: "C:\Program Files\Aspose\Aspose.PDF for .NET\bin\net2.0\Aspose.PDF.tlb" /codebase
- إطار عمل .NET 3.5
  regasm "C:\Program Files\Aspose\Aspose.PDF for .NET\bin\net3.5\Aspose.PDF.dll" /tlb: "C:\Program Files\Aspose\Aspose.PDF for .NET\bin\net3.5\Aspose.PDF.tlb" /codebase
- إطار عمل .NET 4.0
  regasm "C:\Program Files\Aspose\Aspose.PDF for .NET\bin\net4.0\Aspose.PDF.dll" /tlb: "C:\Program Files\Aspose\Aspose.PDF for .NET\bin\net4.0\Aspose.PDF.tlb" /codebase

{{% /alert %}}

## إنشاء كائنات COM

إنشاء كائن COM يشبه إنشاء كائن .NET عادي:

```vb

'Instantiate Pdf instance by calling its empty constructor

Dim pdf
Set pdf = CreateObject("Aspose.PDF.Generator.Pdf")

```
بمجرد إنشائه، تستطيع الوصول إلى طرق وخصائص الكائن، كما لو كان كائن COM:

```vb
'إضافة قسم إلى كائن Pdf
pdf.Sections.Add(pdfsection)
```

بعض الطرق لها تحميلات متعددة وسيتم الكشف عنها بواسطة COM Interop مع إضافة لاحقة رقمية لها، باستثناء الطريقة الأولى التي تبقى دون تغيير. على سبيل المثال، تصبح تحميلات طريقة Pdf.Save مثل Pdf.Save، Pdf.Save_2، وهكذا.

لمزيد من المعلومات، انظر إلى المقالات المحددة باللغة لاحقًا في هذه المستندات.

## إنشاء تجميعة الغلاف

إذا كنت بحاجة إلى استخدام العديد من الفئات والطرق والخصائص لـ Aspose.PDF لـ .NET، فكر في إنشاء تجميعة غلاف (باستخدام C# أو أي لغة برمجة .NET أخرى). تساعد تجميعات الغلاف على تجنب استخدام Aspose.PDF لـ .NET مباشرة من الكود غير المدار.

منهج جيد هو تطوير تجميعة .NET تشير إلى Aspose.PDF لـ .NET وتقوم بكل العمل معه، وتعرض فقط مجموعة محدودة من الفئات والطرق للكود غير المدار.
طريقة جيدة هي تطوير مكتبة .NET تستخدم Aspose.PDF لـ .NET وتقوم بكل العمل معها، وتعرض فقط مجموعة محدودة من الصفوف والطرق للكود غير المُدار.

تقليل عدد الصفوف والطرق التي تحتاج لاستدعائها عبر COM Interop يبسط المشروع. استخدام صفوف .NET عبر COM Interop غالباً يتطلب مهارات متقدمة.
