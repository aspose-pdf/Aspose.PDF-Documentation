---
title: نسخ الحقل الداخلي والخارجي
type: docs
weight: 40
url: /net/copy-inner-and-outer-field/
description: تشرح هذه القسم كيفية نسخ الحقل الداخلي والخارجي باستخدام Aspose.PDF Facades باستخدام فئة FormEditor.
lastmod: "2021-06-05"
draft: false
---

تسمح لك طريقة [CopyInnerField](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor/methods/copyinnerfield/index) بنسخ حقل في نفس الملف، في نفس الإحداثيات، على الصفحة المحددة. تتطلب هذه الطريقة اسم الحقل الذي تريد نسخه، واسم الحقل الجديد، ورقم الصفحة التي يحتاج الحقل إلى النسخ فيها. توفر فئة [FormEditor](https://reference.aspose.com/html/net/aspose.html.forms/formeditor) هذه الطريقة. يوضح لك مقطع الشيفرة التالي كيفية نسخ الحقل في نفس الموقع في نفس الملف.

```csharp
  public static void CopyInnerField()
        {
            var editor = new FormEditor();
            var document = new Aspose.Pdf.Document(_dataDir + "Sample-Form-01.pdf");
            document.Pages.Add();
            editor.BindPdf(document);
            editor.CopyInnerField("Last Name", "Last Name 2", 2);
            editor.Save(_dataDir + "Sample-Form-01-mod.pdf");
        }
```

## نسخ الحقل الخارجي في ملف PDF موجود

تتيح لك طريقة [CopyOuterField](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor/methods/copyouterfield/index) نسخ حقل نموذج من ملف PDF خارجي ثم إضافته إلى ملف PDF المدخل في نفس الموقع ورقم الصفحة المحدد. تتطلب هذه الطريقة ملف PDF الذي يجب نسخ الحقل منه، واسم الحقل، ورقم الصفحة الذي يجب نسخ الحقل فيه. يتم توفير هذه الطريقة من قبل فئة [FormEditor](https://reference.aspose.com/html/net/aspose.html.forms/formeditor). يُظهر لك مقتطف الكود التالي كيفية نسخ حقل من ملف PDF خارجي.

```csharp
   public static void CopyOuterField()
        {
            var editor = new FormEditor();
            var document = new Aspose.Pdf.Document();
            document.Pages.Add();
            editor.BindPdf(document);
            editor.CopyOuterField(_dataDir + "Sample-Form-01.pdf", "First Name", 1);
            editor.CopyOuterField(_dataDir + "Sample-Form-01.pdf", "Last Name", 1);
            editor.Save(_dataDir + "Sample-Form-02-mod.pdf");
        }
```