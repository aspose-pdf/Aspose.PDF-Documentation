---
title: DOC Converter
type: docs
weight: 10
url: ar/net/plugins/doc/
description: تحويل PDF إلى Word بسهولة باستخدام إضافة PdfDoc
lastmod: "2024-01-24"
---

هذا المقال يرشدك خلال استخدام [محول Aspose.Pdf DOC لـ .NET](https://products.aspose.org/pdf/net/doc-converter/) لتحويل مستند PDF إلى صيغة Microsoft Word (.doc / .docx).

## متطلبات

ستحتاج إلى الآتي:

* Visual Studio 2019 أو أحدث
* Aspose.PDF لـ .NET 24.1 أو أحدث
* ملف PDF نموذجي يحتوي على بعض حقول النماذج

يمكنك تحميل مكتبة Aspose.PDF لـ .NET من الموقع الرسمي أو تثبيتها باستخدام مدير حزم NuGet في Visual Studio.

## خطوات

### 1. إعداد التحويل (لقطة شاشة لفئة FileDataSource)

تتضمن عملية التحويل ثلاث خطوات رئيسية: تحديد الملفات الداخلية والخارجية، إنشاء كائن `PdfDoc`، وتحديد خيارات التحويل.

#### 1.1. تحديد مصادر البيانات

* **ملف الإدخال:** سنستخدم فئة `FileDataSource` لتحديد موقع ملف PDF الذي تريد تحويله.
* **ملف الإدخال:** سنستخدم فئة `FileDataSource` لتحديد موقع ملف PDF الذي تريد تحويله.

```csharp
  FileDataSource inputDataSource = new(Path.Combine(@"C:\Samples\", "sample.pdf"));
```

  * استبدل `"C:\Samples\sample.pdf"` بالمسار الفعلي لملف PDF الخاص بك.

* **ملف الإخراج:** بالمثل، استخدم كائن `FileDataSource` آخر لتحديد موقع الملف واسم الملف لوثيقة Word الناتجة.

```csharp
  FileDataSource outputDataSource = new(Path.Combine(@"C:\Samples\", "sample.docdocx"));
```

* استبدل `"C:\Samples\sample.docx"` بمسار الإخراج واسم الملف الذي تريده.

### 2. إنشاء كائن الإضافة PdfDoc (لقطة شاشة لفئة PdfDoc)

بعد ذلك، نقوم بإنشاء نسخة من فئة `PdfDoc` لأداء عملية التحويل.

```csharp
  var plugin = new PdfDoc();
```

يعمل هذا الكائن كمحرك لعملية التحويل.

### 3. تكوين خيارات التحويل

تتيح لك فئة `PdfToDocOptions` تعديل عملية التحويل بدقة.
تتيح لك فئة `PdfToDocOptions` تحديد إعدادات عملية التحويل بدقة.

* **صيغة الحفظ:** حدد صيغة الإخراج المطلوبة لمستند الوورد. في هذه الحالة، نستخدم `SaveFormat.DocX` لإنتاج مستند متوافق مع Microsoft Word 2007 أو أحدث (.docx).

* **وضع التحويل:** حدد كيفية تفسير الإضافة لبنية PDF أثناء التحويل. سنستخدم `ConversionMode.EnhancedFlow` لتحسين مستند Word الناتج من حيث التخطيط والتنسيق.

إليك مقتطف الكود لتهيئة الخيارات:

```csharp
  PdfToDocOptions options = new()
  {
      SaveFormat = SaveFormat.DocX,
      ConversionMode = ConversionMode.EnhancedFlow
  };
```

**إضافة المدخلات والمخرجات:**

أخيرًا، نربط مصادر البيانات المحددة سابقًا بخيارات التحويل باستخدام طرق `AddInput` و `AddOutput`:

```csharp
  options.AddInput(inputDataSource);
  options.AddOutput(outputDataSource);
```

هذا يربط ملف PDF المدخل ومستند Word المطلوب كمخرج بعملية التحويل.

### 4.
### 4.

بعد إعداد كل شيء، دعونا نبدأ عملية التحويل بالاستدعاء للدالة `Process` الخاصة بإضافة `PdfDoc` وإرسال الخيارات المُعدة:

```csharp
  var resultContainer = plugin.Process(options);
```

تقوم هذه الطريقة بتنفيذ التحويل وتعيد كائن `ResultContainer` يحتوي على تفاصيل العملية.

**استرجاع النتائج:**

على الرغم من أنه ليس ضروريًا للتحويل الأساسي، يمكنك الوصول إلى النتائج من خلال خاصية `ResultCollection` لكائن `ResultContainer`. قد يكون هذا مفيدًا لتصحيح الأخطاء أو تتبع تفاصيل التحويل المحددة.

```csharp
  var result = resultContainer.ResultCollection[0];

  // طباعة النتيجة (اختياري لأغراض العرض)
  Console.WriteLine(result);
```

مع هذه الخطوة النهائية، سيتم تحويل مستند PDF الخاص بك إلى تنسيق Word المحدد وحفظه في موقع الإخراج المعرف.
