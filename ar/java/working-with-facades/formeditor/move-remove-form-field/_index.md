---
title: نقل وإزالة حقل النموذج
type: docs
weight: 50
url: /ar/java/move-remove-form-field/
description: يشرح هذا القسم كيفية نقل وإزالة حقول النموذج باستخدام فئة FormEditor.
lastmod: "2021-06-05"
draft: false
---

## نقل حقل النموذج إلى موقع جديد في ملف PDF موجود

إذا كنت تريد نقل حقل النموذج إلى موقع جديد، يمكنك استخدام طريقة [moveField](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/FormEditor#moveField-java.lang.String-float-float-float-float-) من فئة [FormEditor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/FormEditor).
 تحتاج فقط إلى توفير اسم الحقل والموقع الجديد لهذا الحقل لطريقة [moveField](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/FormEditor#moveField-java.lang.String-float-float-float-float-). تحتاج أيضًا إلى حفظ ملف PDF المحدث باستخدام طريقة Save لفئة [FormEditor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/FormEditor). يوضح لك مقتطف الشيفرة التالي كيفية نقل حقل نموذج إلى موقع جديد في ملف PDF.

```java
 public static void MoveField()
        {
            var editor = new FormEditor();
            editor.BindPdf(_dataDir + "Sample-Form-05.pdf");
            editor.MoveField("Last Name", 262.56f, 496.75f, 382.28f, 514.03f);
            editor.Save(_dataDir + "Sample-Form-05-mod.pdf");
        }
```

## حذف حقل النموذج من ملف PDF موجود

لحذف حقل من نموذج في ملف PDF موجود، يمكنك استخدام طريقة RemoveField لفئة FormEditor. هذه الطريقة تأخذ وسيطًا واحدًا فقط: اسم الحقل. تحتاج إلى إنشاء كائن من فئة FormEditor، واستدعاء طريقة [removeField](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/FormEditor#removeField-java.lang.String-) لإزالة حقل معين من ملف PDF ثم استدعاء طريقة Save لحفظ ملف PDF المحدث. يوضح لك مقتطف الشيفرة التالي كيفية حذف حقول النموذج من ملف PDF موجود.

```java
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

يمكنك أيضًا إعادة تسمية الحقل الخاص بك باستخدام طريقة [renameField](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/FormEditor#renameField-java.lang.String-java.lang.String-) لفئة [FormEditor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/FormEditor).
```java
    public static void RenameFields()
        {
            // إنشاء محرر النموذج
            var editor = new FormEditor();
            // ربط ملف PDF
            editor.BindPdf(_dataDir + "Sample-Form-01.pdf");
            // إعادة تسمية الحقل "Last Name" إلى "LastName"
            editor.RenameField("Last Name", "LastName");
            // إعادة تسمية الحقل "First Name" إلى "FirstName"
            editor.RenameField("First Name", "FirstName");
            // حفظ ملف PDF المحدث
            editor.Save(_dataDir + "Sample-Form-01-updated.pdf");
        }
```