---
title: تعديل AcroForms
linktitle: تعديل AcroForms
type: docs
weight: 40
url: /ar/java/modifing-form/
description: توضح هذه القسم كيفية تعديل النماذج في مستند PDF الخاص بك باستخدام Aspose.PDF لـ Java.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## تعيين خط مخصص لحقل النموذج

يمكن تكوين حقول النموذج في ملفات PDF من Adobe لاستخدام خطوط افتراضية محددة. يسمح Aspose.PDF للمطورين بتطبيق أي خط كخط افتراضي للحقل، سواء كان أحد الخطوط الأساسية الـ 14 أو خطًا مخصصًا.
لتعيين وتحديث الخط الافتراضي المستخدم لحقول النموذج، يحتوي Aspose.PDF على فئة DefaultAppearance (Font font, double size, Color color). يمكن الوصول إلى هذه الفئة باستخدام com.aspose.pdf.DefaultAppearance. لاستخدام هذا الكائن، استخدم طريقة setDefaultAppearance(..) للفئة Field.

يوضح لك مقطع الكود التالي كيفية تعيين الخط الافتراضي لحقل نموذج PDF.

```java
package com.aspose.pdf.examples;

import com.aspose.pdf.DefaultAppearance;
import com.aspose.pdf.Document;
import com.aspose.pdf.Field;
import com.aspose.pdf.Font;
import com.aspose.pdf.FontRepository;
import com.aspose.pdf.Rectangle;
import com.aspose.pdf.TextBoxField;

public class ExamplesModifying {

    private static String _dataDir = "/home/aspose/pdf-examples/Samples/Forms/";

    public static void SetFormFieldFontOtherThan14CorePDFFonts() {
        // فتح المستند
        Document pdfDocument = new Document(_dataDir + "FormFieldFont14.pdf");
        // الحصول على حقل نموذج معين من المستند
        Field field = (Field) pdfDocument.getForm().get("textbox1");

        // إنشاء كائن خط
        Font font = FontRepository.findFont("ComicSansMS");

        // تعيين معلومات الخط لحقل النموذج
        field.setDefaultAppearance (new DefaultAppearance(font, 10, java.awt.Color.BLACK));
        
        // حفظ المستند المحدث
        pdfDocument.save(_dataDir + "FormFieldFont14_out.pdf");
    }
```


## الحصول على/تعيين حد الحقل

تسمح لك طريقة SetFieldLimit في فئة FormEditor بتعيين حد للحقل، وهو الحد الأقصى لعدد الأحرف التي يمكن إدخالها في الحقل.

```java
    public static void GettingMaximumFieldLimit()
    {
        // الحصول على الحد الأقصى للحقل باستخدام DOM
        Document doc = new Document(_dataDir + "FieldLimit.pdf");
        TextBoxField field = (TextBoxField)doc.getForm().get("textbox1");
        System.out.println("الحد: " +field.getMaxLen());
    }
```

يمكنك أيضًا الحصول على نفس القيمة باستخدام مساحة الاسم Aspose.PDF.Facades باستخدام مقتطف الشيفرة التالي.

```java
    public static void GettingMaximumFieldLimitFacades()
    {
        // الحصول على الحد الأقصى للحقل باستخدام Facades
        com.aspose.pdf.facades.Form form = new com.aspose.pdf.facades.Form();
        form.bindPdf(_dataDir + "FieldLimit.pdf");
        System.out.println("الحد: " + form.getFieldLimit("textbox1"));
    }
```

وبالمثل، يمتلك Aspose.PDF طريقة تحصل على حد الحقل باستخدام نهج DOM.
 يظهر مقتطف الشيفرة التالي الخطوات.

```java
    public static void SettingMaximumFieldLimit()
    {
        // الحصول على الحد الأقصى للحقل باستخدام DOM
        Document doc = new Document(_dataDir + "FieldLimit.pdf");
        TextBoxField field = (TextBoxField)doc.getForm().get("textbox1");
        field.setMaxLen(10);
        System.out.println("الحد: " +field.getMaxLen());       
    }
```

## حذف حقل نموذج معين من مستند PDF

تُحتوى جميع حقول النماذج في مجموعة النموذج الخاصة بكائن [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document). توفر هذه المجموعة طرقًا مختلفة لإدارة حقول النماذج، بما في ذلك طريقة الحذف. إذا كنت تريد حذف حقل معين، مرر اسم الحقل كمعامل إلى طريقة الحذف ثم احفظ مستند PDF المحدث.

يظهر مقتطف الشيفرة التالي كيفية حذف حقل مسمى من مستند PDF.

```java
    public static void DeleteParticularFormField()
    {    
        // فتح مستند
        Document pdfDocument = new Document("input.pdf");

        // حذف حقل مسمى باستخدام الاسم
        pdfDocument.getForm().delete("textbox1");

        // حفظ ملف PDF المعدل
        pdfDocument.save("output.pdf");
    }
```

## تعديل حقل نموذج في مستند PDF

تسمح لك مجموعة النماذج في كائن [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) بإدارة حقول النماذج في مستند PDF.

لتعديل حقل نموذج، احصل على الحقل من مجموعة النماذج وقم بتعيين خصائصه. ثم احفظ مستند PDF المحدث.

يُظهر مقطع الشيفرة التالي كيفية تعديل حقل نموذج موجود في مستند PDF.

```java
    public static void ModifyFormField()
    {
        Document pdfDocument = new Document("input.pdf");
        // احصل على حقل
        TextBoxField textBoxField = (TextBoxField) pdfDocument.getForm().get("textbox1");

        // تعديل قيمة الحقل
        textBoxField.setValue("Updated Value");

        // تعيين الحقل كـ للقراءة فقط
        textBoxField.setReadOnly(true);

        // حفظ المستند المحدث
        pdfDocument.save("output.pdf");
    }
```

### نقل حقل نموذج إلى موقع جديد في ملف PDF

إذا كنت ترغب في نقل حقل نموذج إلى موقع جديد على صفحة PDF، احصل أولاً على كائن الحقل ثم حدد قيمة جديدة لطريقة setRect الخاصة به.
 A [Rectangle](https://reference.aspose.com/pdf/java/com.aspose.pdf/Rectangle) كائن بإحداثيات جديدة يتم تعيينه إلى طريقة setRect(..). ثم احفظ ملف PDF المحدث باستخدام طريقة الحفظ لكائن [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document).

يُظهر لك مقطع الشيفرة التالي كيفية نقل حقل نموذج إلى موقع جديد.

```java
    public static void ModifyMoveFormFieldNewLocation()
    {    
        // افتح مستند
        Document pdfDocument = new Document(_dataDir+"input.pdf");
        // احصل على حقل
        TextBoxField textBoxField = (TextBoxField) pdfDocument.getForm().get("textbox1");

        // تعديل موقع الحقل
        textBoxField.setRect(new Rectangle(300, 400, 600, 500));

        // احفظ المستند المعدل
        pdfDocument.save("output.pdf");
    }
}
```