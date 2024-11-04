---
title: نسخ الحقل الداخلي والخارجي
type: docs
weight: 40
url: /java/copy-inner-and-outer-field/
description: يوضح هذا القسم كيفية نسخ الحقل الداخلي والخارجي باستخدام com.aspose.pdf.facades باستخدام فئة FormEditor.
lastmod: "2021-06-05"
draft: false
---

تتيح لك طريقة [copyInnerField](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/FormEditor#copyInnerField-java.lang.String-java.lang.String-int-) نسخ حقل في نفس الملف، عند نفس الإحداثيات، في الصفحة المحددة. تتطلب هذه الطريقة اسم الحقل الذي تريد نسخه، واسم الحقل الجديد، ورقم الصفحة التي ينبغي نسخ الحقل فيها. توفر فئة [FormEditor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/FormEditor) هذه الطريقة. يوضح لك المثال البرمجي التالي كيفية نسخ الحقل في نفس الموقع في نفس الملف.

```java
    public static void CopyInnerField() {
        FormEditor editor = new FormEditor();
        Document document = new Document(_dataDir + "Sample-Form-01.pdf");
        document.getPages().add();
        editor.bindPdf(document);
        editor.copyInnerField("Last Name", "Last Name 2", 2);
        editor.save(_dataDir + "Sample-Form-01-mod.pdf");
    }
```


## نسخ الحقل الخارجي في ملف PDF موجود

تسمح لك طريقة [copyOuterField](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/FormEditor#copyOuterField-java.lang.String-java.lang.String-) بنسخ حقل نموذج من ملف PDF خارجي ثم إضافته إلى ملف PDF المدخل في نفس الموقع ورقم الصفحة المحدد. تتطلب هذه الطريقة ملف PDF الذي يجب نسخ الحقل منه، واسم الحقل، ورقم الصفحة الذي يجب نسخ الحقل فيه. يتم توفير هذه الطريقة بواسطة فئة [FormEditor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/FormEditor). يوضح لك جزء الشفرة التالي كيفية نسخ حقل من ملف PDF خارجي.

```java
  public static void CopyOuterField() {
        FormEditor editor = new FormEditor();
        Document document = new Document();
        document.getPages().add();
        editor.bindPdf(document);
        editor.copyOuterField(_dataDir + "Sample-Form-01.pdf", "First Name", 1);
        editor.copyOuterField(_dataDir + "Sample-Form-01.pdf", "Last Name", 1);
        editor.save(_dataDir + "Sample-Form-02-mod.pdf");
    }
```