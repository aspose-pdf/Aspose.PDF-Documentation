---
title: Splitter
type: docs
weight: 120
url: ar/net/plugins/splitter/
description: يقسم مستند PDF إلى صفحات منفصلة
lastmod: "2024-01-24"
draft: false
---

هل لديك مستند PDF كبير ترغب في تقسيمه إلى ملفات أصغر وأكثر قابلية للإدارة؟ مع [Aspose.PDF Splitter لـ .NET](https://products.aspose.org/pdf/net/splitter/)، يمكنك تحقيق هذه المهمة بسهولة. في هذا المقال، سنستكشف عملية تقسيم مستند PDF إلى ملفات متعددة باستخدام إضافة Aspose.PDF. دعونا نغوص في الكود ونمر بالخطوات.

## المتطلبات الأساسية

ستحتاج إلى ما يلي:

* Visual Studio 2019 أو أحدث
* Aspose.PDF لـ .NET 24.1 أو أحدث
* ملف PDF نموذجي

بالإضافة إلى ذلك، عليك أن تتعرف على فئة `SplitOptions` وخصائصها. يمكنك العثور على معلومات تفصيلية حول هذه الفئة في [المرجع API](https://reference.aspose.com/pdf/net/aspose.pdf/SplitOptions/). لاحظ أن كل `FileDataSource` للإخراج يمثل صفحة واحدة في الملفات المقسمة لـ PDF.

الآن، دعونا نستكشف الكود المقدم ونفهم كيفية تقسيم مستند PDF.
الآن، دعونا نستكشف الشفرة المقدمة ونفهم كيفية تقسيم مستند PDF.

## شرح الكود

الكود أدناه يوضح عرض توضيحي لتقسيم PDF باستخدام Aspose.PDF.Plugins:

```csharp
using Aspose.Pdf.Plugins;
// ...........

// ضبط مسار المدخلات لمستند PDF الذي سيتم تقسيمه.
using var inputStream = File.OpenRead(Path.Combine(@"C:\Samples\", "sample.pdf"));

// إنشاء نموذج جديد للمقسم.
var splitter = new Splitter();

// إنشاء خيارات لتقسيم المستند.
var options = new SplitOptions();

// إضافة مصادر البيانات المدخلة والمخرجة إلى الخيارات.
options.AddInput(new StreamDataSource(inputStream));

var document = new Aspose.Pdf.Document(inputStream);

for (int i = 1; i <= document.Pages.Count; i++)
{
   var pageNum = string.Format("{0,3}", i.ToString("D3"));
   options.AddOutput(new FileDataSource(Path.Combine(@"C:\Samples\", $"splitter_{pageNum}.pdf")));
}

// معالجة الخيارات لتقسيم المستند.
var result = splitter.Process(options);
Console.WriteLine(result);
```

دعونا نفصل الخطوات الرئيسية:
لنقم بتوضيح الخطوات الرئيسية:

1. **تحديد ملف PDF الإدخال**

   يبدأ الكود بتحديد مسار مستند PDF الذي سيتم تقسيمه. يتم ذلك باستخدام الطريقة `File.OpenRead`.

2. **إنشاء كائن (مقسم وخيارات التقسيم)**

   يقوم الكود بإنشاء نموذج من فئة `Splitter` للتعامل مع عملية التقسيم. بالإضافة إلى ذلك، يتم إنشاء نموذج من فئة `SplitOptions` لتكوين عملية التقسيم.

3. **إضافة مصدر البيانات (الإدخال والإخراج)**

   يتم إضافة مستند PDF الإدخال إلى `SplitOptions` كمصدر بيانات الإدخال باستخدام طريقة `AddInput`. لكل صفحة في المستند، يتم إضافة مسار ملف الإخراج كمصدر بيانات الإخراج باستخدام طريقة `AddOutput`.

4. **تشغيل طريقة العملية**

   يتم بدء عملية التقسيم بالاتصال بطريقة `Process` على فئة `Splitter`، مع تمرير `SplitOptions` المكون. يتم تخزين نتيجة العملية في متغير `result`.

5. **معالجة النتيجة**

   يقوم الكود بطباعة النتيجة إلى وحدة التحكم، مقدمًا معلومات عن عملية التقسيم.
يطبع الكود النتيجة إلى وحدة التحكم، مقدمًا معلومات حول عملية التقسيم.
