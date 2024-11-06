---
title: تزيين حقل النموذج في PDF
type: docs
weight: 20
url: ar/java/decorate-form-field/
description: يشرح هذا القسم كيفية تزيين حقل النموذج في PDF باستخدام فئة FormEditor.
lastmod: "2021-06-05"
draft: false
---

## تزيين حقل نموذج معين في ملف PDF موجود

تسمح لك طريقة [decorateField](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/FormEditor#decorateField--) الموجودة في فئة [FormEditor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/FormEditor) بتزيين حقل نموذج معين في ملف PDF.
 إذا كنت ترغب في تزيين حقل معين، فعليك تمرير اسم الحقل إلى هذه الطريقة. ومع ذلك، قبل استدعاء هذه الطريقة، تحتاج إلى إنشاء كائنات من فئات [FormEditor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/FormEditor) و[FormFieldFacade](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/FormFieldFacade). بعد ذلك، يمكنك تعيين أي سمات يوفرها كائن [FormFieldFacade](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/FormFieldFacade). بمجرد تعيين السمات، يمكنك استدعاء طريقة [decorateField](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/FormEditor#decorateField--) وأخيرًا حفظ ملف PDF المحدث باستخدام طريقة Save من فئة [FormEditor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/FormEditor).
يُظهر لك مقتطف الشيفرة التالي كيفية تزيين حقل نموذج معين.

```java
public static void DecorateField() {
        FormEditor editor = new FormEditor();
        editor.bindPdf(_dataDir + "Sample-Form-01.pdf");

        FormFieldFacade cityDecoration = new FormFieldFacade();
        cityDecoration.setFont(FontStyle.Courier);
        cityDecoration.setFontSize(12);
        cityDecoration.setBorderColor(Color.BLACK);
        cityDecoration.setBorderWidth(2);

        editor.setFacade(cityDecoration);
        editor.decorateField("City");
        editor.save(_dataDir + "Sample-Form-02.pdf");
    }
```

## تزيين جميع الحقول من نوع معين في ملف PDF موجود

تتيح لك طريقة [decorateField](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/FormEditor#decorateField--) تزيين جميع حقول النموذج من نوع معين في ملف PDF دفعة واحدة.
 إذا كنت ترغب في تزيين جميع الحقول من نوع معين، فيجب عليك تمرير نوع الحقل إلى هذه الطريقة. ومع ذلك، قبل استدعاء هذه الطريقة، تحتاج إلى إنشاء كائنات من الفئات [FormEditor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/FormEditor) و[FormFieldFacade](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/FormFieldFacade). بعد ذلك، يمكنك تعيين أي سمات يوفرها كائن [FormFieldFacade](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/FormFieldFacade). بمجرد تعيين السمات، يمكنك استدعاء طريقة [decorateField](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/FormEditor#decorateField--) وأخيرًا حفظ ملف PDF المحدث باستخدام طريقة Save من فئة [FormEditor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/FormEditor). يوضح لك جزء الكود التالي كيفية تزيين جميع الحقول من نوع معين.

```java
   public static void DecorateFields() {
        FormEditor editor = new FormEditor();
        editor.bindPdf(_dataDir + "Sample-Form-01.pdf");

        FormFieldFacade textFieldDecoration = new FormFieldFacade();
        textFieldDecoration.setAlignment(FormFieldFacade.ALIGN_CENTER);

        editor.setFacade(textFieldDecoration);
        editor.decorateField(FieldType.Text);
        editor.save(_dataDir + "Sample-Form-01-align-text.pdf");
    }
```