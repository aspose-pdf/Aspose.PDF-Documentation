---
title: إضافة حقول نموذج PDF
type: docs
weight: 10
url: /ar/net/add-form-fields/
description: يشرح هذا الموضوع كيفية العمل مع حقول النموذج باستخدام Aspose.PDF Facades باستخدام فئة FormEditor.
lastmod: "2021-06-05"
draft: false
---

## إضافة حقل نموذج في ملف PDF موجود

لإضافة حقل نموذج في ملف PDF موجود، تحتاج إلى استخدام طريقة [AddField](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor/methods/addfield/index) من فئة [FormEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor). هذا الأسلوب يتطلب منك تحديد نوع الحقل الذي تريد إضافته مع اسم وموقع الحقل. تحتاج إلى إنشاء كائن من فئة [FormEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor)، واستخدام طريقة [AddField](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor/methods/addfield/index) لإضافة حقل جديد في ملف PDF، كما يمكنك تحديد حد لعدد الأحرف في الحقل الخاص بك باستخدام [SetFieldLimit](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor/methods/setfieldlimit) وأخيرًا استخدام طريقة [Save](https://reference.aspose.com/pdf/net/aspose.pdf.facades/form/methods/save/index) لحفظ ملف PDF المحدث. يظهر الجزء البرمجي التالي كيفية إضافة حقل نموذج في ملف PDF موجود.

```csharp
   public static void AddField()
        {
            var editor = new FormEditor();
            editor.BindPdf(_dataDir+"Sample-Form-01.pdf");
            editor.AddField(FieldType.Text, "Country", 1, 232.56f, 496.75f, 352.28f, 514.03f);
            editor.SetFieldLimit("Country", 20);
            editor.Save(_dataDir + "Sample-Form-01-mod.pdf");
        }
```
## إضافة عنوان URL لزر الإرسال في ملف PDF موجود

تسمح لك طريقة [AddSubmitBtn](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor/methods/addsubmitbtn) بتعيين عنوان URL لزر الإرسال في ملف PDF. هذا هو عنوان URL الذي يتم إرسال البيانات إليه عند النقر على زر الإرسال. في مثال الكود الخاص بنا، نحدد عنوان URL واسم الحقل الخاص بنا ورقم الصفحة التي نريد الإضافة إليها وإحداثيات وضع الزر. تتطلب طريقة [AddSubmitBtn](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor/methods/addsubmitbtn) اسم حقل زر الإرسال وعنوان URL. يتم توفير هذه الطريقة بواسطة فئة [FormEditor](https://reference.aspose.com/html/net/aspose.html.forms/formeditor). يوضح لك مقطع الكود التالي كيفية تعيين عنوان URL لزر الإرسال.

```csharp
public static void AddSubmitBtn()
        {
            var editor = new FormEditor();
            editor.BindPdf(_dataDir + "Sample-Form-01.pdf");
            editor.AddSubmitBtn("Submit", 1, "Submit", "http://localhost:3000", 232.56f, 466.75f, 352.28f, 484.03f);
            editor.Save(_dataDir + "Sample-Form-01-mod.pdf");
        }
```

## إضافة جافا سكريبت لزر الضغط

طريقة [AddFieldScript](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor/methods/addfieldscript) تتيح لك إضافة جافا سكريبت لزر الضغط في ملف PDF. تتطلب هذه الطريقة اسم زر الضغط والجافا سكريبت. يتم توفير هذه الطريقة من قبل فئة [FormEditor](https://reference.aspose.com/html/net/aspose.html.forms/formeditor). يوضح لك مقطع الشيفرة التالي كيفية تعيين جافا سكريبت لزر الضغط.

```csharp
     public static void AddFieldScript()
        {
            var editor = new FormEditor();
            editor.BindPdf(_dataDir + "Sample-Form-01.pdf");
            editor.AddFieldScript("Last Name", "app.alert(\"Only one last name\",3);");
            editor.Save(_dataDir + "Sample-Form-01-mod.pdf");
        }
```