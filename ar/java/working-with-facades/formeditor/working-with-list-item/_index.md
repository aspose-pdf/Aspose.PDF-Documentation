---
title: العمل مع عنصر القائمة
type: docs
weight: 30
url: /ar/java/working-with-list-item/
description: يوضح هذا القسم كيفية العمل مع عنصر القائمة باستخدام com.aspose.pdf.facades باستخدام فئة FormEditor.
lastmod: "2021-06-05"
draft: false
---

## إضافة عنصر قائمة في ملف PDF موجود

تسمح لك طريقة [addListItem](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/FormEditor#addListItem-java.lang.String-java.lang.String-) بإضافة عنصر في حقل ListBox. الحجة الأولى هي اسم الحقل والثانية هي عنصر الحقل. يمكنك إما تمرير عنصر حقل واحد أو يمكنك تمرير مصفوفة من السلاسل تحتوي على قائمة من العناصر. يتم توفير هذه الطريقة بواسطة فئة [FormEditor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/FormEditor). يظهر لك مقطع الشيفرة التالي كيفية إضافة عناصر قائمة في ملف PDF.

```java
public static void AddListItem() {
        FormEditor editor = new FormEditor();
        editor.bindPdf(_dataDir + "Sample-Form-01.pdf");
        editor.addField(FieldType.ListBox, "Country", 1, 232.56f, 476.75f, 352.28f, 514.03f);
        editor.addListItem("Country", "USA");
        editor.addListItem("Country", "Canada");
        editor.addListItem("Country", "France");
        editor.addListItem("Country", "Spain");
        editor.save(_dataDir + "Sample-Form-01-mod.pdf");
    }
```


## حذف عنصر قائمة من ملف PDF موجود

طريقة [delListItem](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/FormEditor#delListItem-java.lang.String-java.lang.String-) تسمح لك بحذف عنصر معين من ListBox. المعامل الأول هو اسم الحقل بينما المعامل الثاني هو العنصر الذي ترغب في حذفه من القائمة. يتم توفير هذه الطريقة بواسطة فئة [FormEditor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/FormEditor). يوضح لك مقطع الشفرة التالي كيفية حذف عنصر قائمة من ملف PDF.

```java
    public static void DelListItem() {
        FormEditor editor = new FormEditor();
        editor.bindPdf(_dataDir + "Sample-Form-04.pdf");
        // -----
        editor.delListItem("Country", "France");
        // -----
        editor.save(_dataDir + "Sample-Form-04-mod.pdf");
    }
```