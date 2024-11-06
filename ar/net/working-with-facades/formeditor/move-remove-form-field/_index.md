---
title: نقل وإزالة حقل النموذج
type: docs
weight: 50
url: ar/net/move-remove-form-field/
description: يشرح هذا القسم كيفية نقل وإزالة حقول النموذج باستخدام فئة FormEditor.
lastmod: "2021-06-05"
draft: false
---

## نقل حقل النموذج إلى موقع جديد في ملف PDF موجود

إذا كنت تريد نقل حقل نموذج إلى موقع جديد فيمكنك استخدام طريقة [MoveField](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor/methods/movefield) من فئة [FormEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor). 
أنت فقط بحاجة لتوفير اسم الحقل والموقع الجديد لهذا الحقل إلى طريقة [MoveField](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor/methods/movefield). تحتاج أيضًا إلى حفظ ملف PDF المحدث باستخدام طريقة [Save](https://reference.aspose.com/pdf/net/aspose.pdf.facades/form/methods/save/index) من فئة [FormEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor). يوضح لك مقتطف الشيفرة التالي كيفية نقل حقل نموذج إلى موقع جديد في ملف PDF.

```csharp
public static void MoveField()
        {
            var editor = new FormEditor();
            editor.BindPdf(_dataDir + "Sample-Form-05.pdf");
            editor.MoveField("Last Name", 262.56f, 496.75f, 382.28f, 514.03f);
            editor.Save(_dataDir + "Sample-Form-05-mod.pdf");
        }
```

## حذف حقل نموذج من ملف PDF موجود

من أجل حذف حقل نموذج من ملف PDF موجود، يمكنك استخدام طريقة RemoveField من فئة FormEditor.
``` هذه الطريقة تأخذ وسيطًا واحدًا فقط: اسم الحقل. تحتاج إلى إنشاء كائن من فئة FormEditor، واستدعاء طريقة [RemoveField](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor/methods/removefield) لإزالة حقل معين من ملف PDF ثم استدعاء طريقة Save لحفظ ملف PDF المحدث. يوضح لك مقتطف الشفرة التالي كيفية حذف حقول النموذج من ملف PDF موجود.

```csharp
  public static void RemoveFields()
        {
            var editor = new FormEditor();
            editor.BindPdf(_dataDir + "Sample-Form-01.pdf");
            editor.RemoveField("First Name");
            editor.RemoveField("Last Name");
            editor.Save(_dataDir + "Sample-Form-01-updated.pdf");
        }
```

## إعادة تسمية حقول النموذج في PDF

يمكنك أيضًا إعادة تسمية الحقل الخاص بك باستخدام طريقة [RenameField](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor/methods/renamefield) من فئة [FormEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor).

```csharp

        public static void RenameFields()
        {
            var editor = new FormEditor();
            editor.BindPdf(_dataDir + "Sample-Form-01.pdf");
            editor.RenameField("Last Name", "LastName");
            editor.RenameField("First Name", "FirstName");
            editor.Save(_dataDir + "Sample-Form-01-updated.pdf");
        }
```