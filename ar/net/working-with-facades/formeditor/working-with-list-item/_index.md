---
title: العمل مع عنصر القائمة
type: docs
weight: 30
url: ar/net/working-with-list-item/
description: يشرح هذا القسم كيفية العمل مع عنصر القائمة باستخدام Aspose.PDF Facades باستخدام فئة FormEditor.
lastmod: "2021-06-05"
draft: false
---

## إضافة عنصر قائمة في ملف PDF موجود

تسمح لك طريقة [AddListItem](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor/methods/addlistitem) بإضافة عنصر في حقل [ListBox](https://reference.aspose.com/pdf/net/aspose.pdf.forms/listboxfield). الحجة الأولى هي اسم الحقل والحجة الثانية هي عنصر الحقل. يمكنك إما تمرير عنصر حقل واحد أو يمكنك تمرير مجموعة من السلاسل تحتوي على قائمة بالعناصر. يتم توفير هذه الطريقة بواسطة فئة [FormEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor). يوضح لك مقتطف الشيفرة التالي كيفية إضافة عناصر قائمة في ملف PDF.

```csharp
  public static void AddListItem()
        {
            var editor = new FormEditor();
            editor.BindPdf(_dataDir + "Sample-Form-01.pdf");
            editor.AddField(FieldType.ListBox, "Country", 1, 232.56f, 476.75f, 352.28f, 514.03f);
            editor.AddListItem("Country", "USA");
            editor.AddListItem("Country", "Canada");
            editor.AddListItem("Country", "France");
            editor.AddListItem("Country", "Spain");
            editor.Save(_dataDir + "Sample-Form-01-mod.pdf");
        }
```

## حذف عنصر قائمة من ملف PDF موجود

تتيح لك طريقة [DelListItem](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor/methods/dellistitem) حذف عنصر معين من [ListBox](https://reference.aspose.com/pdf/net/aspose.pdf.forms/listboxfield). المعامل الأول هو اسم الحقل بينما المعامل الثاني هو العنصر الذي تريد حذفه من القائمة. يتم توفير هذه الطريقة بواسطة فئة [FormEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor). يوضح لك مقطع الشيفرة التالي كيفية حذف عنصر قائمة من ملف PDF.

```csharp
      public static void DelListItem()
        {
            var editor = new FormEditor();
            editor.BindPdf(_dataDir + "Sample-Form-04.pdf");
            //-----
            editor.DelListItem("Country", "France");
            //-----
            editor.Save(_dataDir + "Sample-Form-04-mod.pdf");
        }
```