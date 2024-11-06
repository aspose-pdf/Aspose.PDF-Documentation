---
title: محرر النماذج
type: docs
weight: 40
url: ar/net/plugins/formeditor/
description: كيفية إضافة، تحديث، وإزالة حقول النماذج في ملفات PDF باستخدام إضافات Aspose.PDF
lastmod: "2024-01-24"
draft: false
---

في هذا المقال، سنوضح لك كيفية استخدام [إضافة محرر النماذج](https://products.aspose.org/pdf/net/form-editor/)، والتي يمكن أن تضيف، تحدث، وتزيل حقول النماذج في ملفات PDF.

## المتطلبات الأساسية

ستحتاج إلى الآتي:

* Visual Studio 2019 أو أحدث
* Aspose.PDF لـ .NET 24.1 أو أحدث
* ملف PDF نموذجي يحتوي على بعض حقول النماذج

يمكنك تحميل مكتبة Aspose.PDF لـ .NET من الموقع الرسمي أو تثبيتها باستخدام مدير حزم NuGet في Visual Studio.

## الخطوات

الخطوات الأساسية لإضافة، تحديث، وإزالة حقول النماذج في ملفات PDF باستخدام إضافة FormEditor هي:

1. إنشاء كائن من فئة FormEditor
1. إنشاء كائن من فئة FormEditorAddOptions، FormEditorSetOptions، أو FormRemoveSelectedFieldsOptions، حسب العملية التي تريد تنفيذها
1.
1.
1. تشغيل طريقة Process لكائن FormEditor

لنرى كيفية تنفيذ هذه الخطوات في كود C# لكل عملية.

### الخطوة 1: إنشاء كائن من فئة FormEditor

فئة FormEditor هي الفئة الرئيسية التي توفر وظائف إضافة وتحديث وإزالة حقول النموذج في ملفات PDF. لاستخدامها، تحتاج إلى إنشاء نموذج منها باستخدام المنشئ الافتراضي:

```cs
// إنشاء نموذج من مكون FormEditor
var plugin = new FormEditor();
```

### الخطوة 2: إنشاء كائن من فئة FormEditorAddOptions، FormEditorSetOptions، أو FormRemoveSelectedFieldsOptions، حسب العملية التي ترغب في تنفيذها

فئات `FormEditorAddOptions`، `FormEditorSetOptions`، و `FormRemoveSelectedFieldsOptions` هي فئات مساعدة تتيح لك تحديد خيارات ومعاملات مختلفة لعمليات تحرير النموذج، مثل أنواع حقول النموذج، القيم، الخصائص، المعايير، إلخ.
الفئات `FormEditorAddOptions`، `FormEditorSetOptions`، و `FormRemoveSelectedFieldsOptions` هي فئات مساعدة تتيح لك تحديد خيارات ومعايير متنوعة لعمليات تحرير النماذج، مثل أنواع حقول النماذج، القيم، الخصائص، المعايير، إلخ.

```cs
    // إنشاء خيارات لإضافة حقول النماذج.
    var options = new FormEditorAddOptions(
        [
            // إنشاء حقل نموذج من نوع checkbox.
            new FormCheckBoxFieldCreateOptions(1, new Rectangle(110, 700, 125, 715))
            {
                Value = "CheckBoxField 1",
                PartialName = "CheckBoxField_1",
                Color = Color.Blue,
            },
            // إنشاء حقل نموذج من نوع combo box.
            new FormComboBoxFieldCreateOptions(1, new Rectangle(310, 600, 350, 615))
            {
                Color = Color.Red,
                Editable = true,
                DefaultAppearance = new DefaultAppearance("Arial Bold", 12, System.Drawing.Color.DarkGreen),
                Options = ["option1", "option2", "option3"],
                Selected = 2
            },
            // إنشاء حقل نموذج من نوع textbox.
            new FormTextBoxFieldCreateOptions(1, new Rectangle(10, 700, 90, 715))
            {
                MaxLen = 10,
                Value = "Some text",
                Color = Color.Chocolate
            }
        ]);
```
لتحديث قيم حقول النموذج التي تكون قيمها "قيمة" أو "قيمة أخرى" إلى "قيمة جديدة"، يمكنك استخدام الكود التالي:

```cs
    var options = new FormEditorSetOptions(
    (field) => { return field.Value == "قيمة" || field.Value == "قيمة أخرى"; },
    new FormFieldSetOptions()
    {
        Value = "قيمة جديدة"
    });
```

لإزالة حقول النموذج التي تكون الإحداثي السفلي الأيسر للسين أكبر من 300، يمكنك استخدام الكود التالي:

```cs
// إنشاء خيارات لإزالة حقول النموذج
var options = new FormRemoveSelectedFieldsOptions((field) => field.Rect.LLX > 300);
```

### الخطوة 3: إضافة مصادر البيانات الإدخالية والناتجة إلى كائن الخيارات

مصادر البيانات الإدخالية والناتجة هي ملفات PDF التي ترغب في تعديلها وحفظها.
مصادر البيانات الإدخالية والإخراجية هي ملفات PDF التي ترغب في تعديلها وحفظها.

```cs
// حدد مسارات ملفات الإدخال والإخراج
string inputPath = $@"C:\Samples\Output\sample_forms.pdf";
string outputPath = $@"C:\Samples\Output\sample_forms2.pdf";

// إنشاء نسخة جديدة من فئة FileDataSource لملفات الإدخال والإخراج
FileDataSource inputData = new(inputPath);
FileDataSource outputData = new(outputPath);

// إضافة مصادر البيانات الإدخالية والإخراجية إلى الخيارات
options.AddInput(inputData);
options.AddOutput(outputData);
```

### الخطوة 4: تشغيل طريقة Process لكائن FormEditor

الخطوة النهائية هي تشغيل طريقة Process لكائن FormEditor، مع تمرير كائن الخيارات كمعامل.
الخطوة النهائية هي تشغيل طريقة Process لكائن FormEditor، مع تمرير كائن الخيارات كمعامل.

```cs
// معالجة عملية تحرير النموذج باستخدام الإضافة والخيارات
ResultContainer result = plugin.Process(options);

// الحصول على النتيجة الأولى من مجموعة النتائج
var result = resultContainer.ResultCollection[0];

// طباعة النتيجة
Console.WriteLine(result);
```

سوف تحتوي النتيجة على معلومات مثل مسارات ملفات الخرج.
