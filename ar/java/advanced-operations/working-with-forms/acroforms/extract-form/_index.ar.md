---
title: استخراج البيانات من AcroForms
linktitle: استخراج البيانات من AcroForms
type: docs
weight: 30
url: /java/extract-form/
description: يشرح هذا القسم كيفية استخراج النماذج من مستند PDF الخاص بك باستخدام Aspose.PDF لـ Java.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## الحصول على قيمة من حقل فردي في مستند PDF

تسمح لك [طريقة getValue()](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextBoxField#getValue--) الخاصة بحقل النموذج بالحصول على قيمة حقل معين.

للحصول على القيمة، يجب الحصول على حقل النموذج من مجموعة النماذج الخاصة بكائن [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document).

هذا المثال يختار [TextBoxField](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextBoxField) ويسترجع قيمته باستخدام [طريقة getValue()](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextBoxField#getValue--).

```java
package com.aspose.pdf.examples;

import com.aspose.pdf.Document;
import com.aspose.pdf.Field;
import com.aspose.pdf.TextBoxField;

public class ExamplesExtractFormData {
    private static String _dataDir = "/home/aspose/pdf-examples/Samples/Forms/";

    public static void GetValueFromIndividualFieldPDFDocument() {
        // افتح المستند
        Document pdfDocument = new Document(_dataDir+"GetValueFromField.pdf");

        // احصل على حقل
        TextBoxField textBoxField = (TextBoxField) pdfDocument.getForm().get("textbox1");

        // احصل على اسم الحقل
        System.out.printf("PartialName :-" + textBoxField.getPartialName());

        // احصل على قيمة الحقل
        System.out.printf("Value :-" + textBoxField.getValue());
    }
```


## الحصول على القيم من جميع الحقول في مستند PDF

للحصول على القيم من جميع الحقول في مستند PDF، تحتاج إلى التنقل عبر جميع حقول النموذج ثم الحصول على القيمة باستخدام [طريقة getValue()](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextBoxField#getValue--). احصل على كل حقل من مجموعة النموذج باستخدام [كائن المستند](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) وطريقة [getForm()](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#getForm--) واحصل على قائمة حقول النموذج في مصفوفة Field باستخدام getFields() وتصفح المصفوفة للحصول على قيمة الحقول.

يظهر مقطع الشيفرة التالي كيفية الحصول على القيم من جميع الحقول في مستند PDF.

```java
    public static void GetValuesFromAllFieldsPDFDocument() {
        // فتح المستند
        Document document = new Document(_dataDir + "GetValuesFromAllFields.pdf");

        Field[] fields = document.getForm().getFields();
        for (int i = 0; i < fields.length; i++) {

            System.out.println("حقل النموذج: " + fields[i].getFullName());
            System.out.println("حقل النموذج: " + fields[i].getValue());
        }

    }
}
```


## الحصول على حقول النموذج من منطقة محددة في ملف PDF

في بعض الحالات، يكون من الضروري الحصول على البيانات ليس من النموذج بأكمله، ولكن، على سبيل المثال، فقط من الربع العلوي الأيسر من الورقة المطبوعة. مع Aspose.PDF for Java، هذا ليس مشكلة. يمكنك تحديد منطقة لتصفية الحقول التي تقع خارج المنطقة المحددة من ملف PDF. للحصول على حقول النموذج من منطقة معينة من ملف PDF:

1. افتح ملف PDF باستخدام كائن Document.
2. احصل على النموذج من مجموعة Forms الخاصة بالمستند.
3. حدد المنطقة المستطيلة ومررها إلى طريقة [getFieldsInRect](https://reference.aspose.com/pdf/java/com.aspose.pdf/Form#getFieldsInRect-com.aspose.pdf.Rectangle-) الخاصة بكائن Form. يُعاد مجموعة [Fields](https://reference.aspose.com/pdf/java/com.aspose.pdf/Field).
4. استخدم هذا للتلاعب بالحقول.

يعرض مقطع الشيفرة التالي كيفية الحصول على حقول النموذج في منطقة مستطيلة محددة من ملف PDF.

```java
public static void GetValuesFromSpecificRegion() {
    // افتح ملف pdf
    Document doc = new Document(_dataDir + "GetFieldsFromRegion.pdf");

    // إنشاء كائن المستطيل للحصول على الحقول في تلك المنطقة
    Rectangle rectangle = new Rectangle(35, 30, 500, 500);

    // الحصول على نموذج PDF
    com.aspose.pdf.Form form = doc.getForm();

    // الحصول على الحقول في المنطقة المستطيلة
    Field[] fields = form.getFieldsInRect(rectangle);

    // عرض أسماء الحقول والقيم
    for (Field field : fields)
    {
        // عرض خصائص وضع الصور لجميع المواقع
        System.out.println("Field Name: " + field.getFullName() + "-" + "Field Value: " + field.getValue());
    }
}
```