---
title: تزيين حقل النموذج في PDF
type: docs
weight: 20
url: /net/decorate-form-field/
description: يشرح هذا القسم كيفية تزيين حقل النموذج في PDF باستخدام فئة FormEditor.
lastmod: "2021-06-05"
draft: false
---

## تزيين حقل نموذج معين في ملف PDF موجود

تسمح لك طريقة [DecorateField](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor/methods/decoratefield) الموجودة في فئة [FormEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor) بتزيين حقل نموذج معين في ملف PDF. إذا كنت تريد تزيين حقل معين، فعليك تمرير اسم الحقل إلى هذه الطريقة. 
ومع ذلك، قبل استدعاء هذه الطريقة، تحتاج إلى إنشاء كائنات من فئات [FormEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor) و[FormFieldFacade](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formfieldfacade).
``` You also need to assign the [FormFieldFacade](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formfieldfacade) object to [Facade](https://reference.aspose.com/pdf/net/aspose.pdf.facades/facade/properties/index) property of the [FormEditor](https://reference.aspose.com/html/net/aspose.html.forms/formeditor) object. After that, you can set any attributes provided by [FormFieldFacade](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formfieldfacade) object. Once you have set the attributes, you can call the [DecorateField](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor/methods/decoratefield) method and finally save the updated PDF using [Save](https://reference.aspose.com/pdf/net/aspose.pdf.facades/form/methods/save/index) method of [FormEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor) class.  
The following code snippet shows you how to decorate a particular form field.

```csharp
public static void DecorateField()
        {
            var editor = new FormEditor();
            editor.BindPdf(_dataDir + "Sample-Form-01.pdf");

            var cityDecoration = new FormFieldFacade
            {
                Font = FontStyle.Courier,
                FontSize = 12,
                BorderColor = System.Drawing.Color.Black,
                BorderWidth = 2
            };

            editor.Facade = cityDecoration;
            editor.DecorateField("City");
            editor.Save(_dataDir + "Sample-Form-02.pdf");
        }
```

تحتاج أيضًا إلى تعيين كائن [FormFieldFacade](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formfieldfacade) إلى خاصية [Facade](https://reference.aspose.com/pdf/net/aspose.pdf.facades/facade/properties/index) لكائن [FormEditor](https://reference.aspose.com/html/net/aspose.html.forms/formeditor). بعد ذلك، يمكنك تعيين أي سمات يوفرها كائن [FormFieldFacade](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formfieldfacade). بمجرد تعيين السمات، يمكنك استدعاء طريقة [DecorateField](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor/methods/decoratefield) وأخيرًا حفظ ملف PDF المحدث باستخدام طريقة [Save](https://reference.aspose.com/pdf/net/aspose.pdf.facades/form/methods/save/index) للفئة [FormEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor).
يوضح لك مقتطف الشيفرة التالي كيفية تزيين حقل نموذج معين.

```csharp
public static void DecorateField()
        {
            var editor = new FormEditor();
            editor.BindPdf(_dataDir + "Sample-Form-01.pdf");

            var cityDecoration = new FormFieldFacade
            {
                Font = FontStyle.Courier,
                FontSize = 12,
                BorderColor = System.Drawing.Color.Black,
                BorderWidth = 2
            };

            editor.Facade = cityDecoration;
            editor.DecorateField("City");
            editor.Save(_dataDir + "Sample-Form-02.pdf");
        }
```
## تزيين جميع الحقول من نوع معين في ملف PDF موجود

طريقة [DecorateField](https://reference.aspose.com/pdf/net/aspose.pdf.facades.formeditor/decoratefield/methods/1) تتيح لك تزيين جميع حقول النموذج من نوع معين في ملف PDF دفعة واحدة. If you want to decorate all fields of a particular type then you need to pass the field type to this method.
إذا كنت تريد تزيين جميع الحقول من نوع معين، فعليك تمرير نوع الحقل إلى هذه الطريقة. ومع ذلك، قبل استدعاء هذه الطريقة، تحتاج إلى إنشاء كائنات من فئات [FormEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor) و [FormFieldFacade](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formfieldfacade). You also need to assign the [FormFieldFacade](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formfieldfacade) object to [Facade](https://reference.aspose.com/pdf/net/aspose.pdf.facades/facade/properties/index) property of the [FormEditor](https://reference.aspose.com/html/net/aspose.html.forms/formeditor) object. After that, you can set any attributes provided by [FormFieldFacade](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formfieldfacade) object. Once you have set the attributes, you can call the [DecorateField](https://reference.aspose.com/pdf/net/aspose.pdf.facades.formeditor/decoratefield/methods/1) method and finally save the updated PDF using [Save](https://reference.aspose.com/pdf/net/aspose.pdf.facades/form/methods/save/index) method of [FormEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor) class. The following code snippet shows you how to decorate all the fields of a particular type.

```csharp
        public static void DecorateField2()
        {
            var editor = new FormEditor();
            editor.BindPdf(_dataDir + "Sample-Form-01.pdf");

            var textFieldDecoration = new FormFieldFacade
            {
                Alignment = FormFieldFacade.AlignCenter,
            };

            editor.Facade = textFieldDecoration;
            editor.DecorateField(FieldType.Text);
            editor.Save(_dataDir + "Sample-Form-01-align-text.pdf");
        }
```

تحتاج أيضًا إلى تعيين كائن [FormFieldFacade](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formfieldfacade) إلى خاصية [Facade](https://reference.aspose.com/pdf/net/aspose.pdf.facades/facade/properties/index) لكائن [FormEditor](https://reference.aspose.com/html/net/aspose.html.forms/formeditor). بعد ذلك، يمكنك ضبط أي سمات يوفرها كائن [FormFieldFacade](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formfieldfacade). بمجرد ضبط السمات، يمكنك استدعاء طريقة [DecorateField](https://reference.aspose.com/pdf/net/aspose.pdf.facades.formeditor/decoratefield/methods/1) وأخيرًا حفظ ملف PDF المحدث باستخدام طريقة [Save](https://reference.aspose.com/pdf/net/aspose.pdf.facades/form/methods/save/index) لفئة [FormEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor). يوضح لك مقتطف الكود التالي كيفية تزيين جميع الحقول من نوع معين.

```csharp
        public static void DecorateField2()
        {
            var editor = new FormEditor();
            editor.BindPdf(_dataDir + "Sample-Form-01.pdf");

            var textFieldDecoration = new FormFieldFacade
            {
                Alignment = FormFieldFacade.AlignCenter,
            };

            editor.Facade = textFieldDecoration;
            editor.DecorateField(FieldType.Text);
            editor.Save(_dataDir + "Sample-Form-01-align-text.pdf");
        }
```