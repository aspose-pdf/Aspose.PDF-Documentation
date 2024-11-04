---
title: ملء AcroForms
linktitle: ملء AcroForms
type: docs
weight: 20
url: /java/fill-form/
description: يوضح هذا القسم كيفية ملء حقل النموذج في مستند PDF باستخدام Aspose.PDF for Java.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

تُعتبر مستندات PDF رائعة، وهي بالفعل النوع المفضل للملفات لإنشاء النماذج.

يسمح لك Aspose.PDF for Java بملء حقل النموذج، والحصول على الحقل من مجموعة النموذج الخاصة بكائن المستند.

لنلقي نظرة على المثال التالي لكيفية حل هذه المهمة:

```java
public class ExamplesFillForm {

    private static String _dataDir = "/home/aspose/pdf-examples/Samples/Forms/";

    public static void FillFormFieldPDFDocument() {
        // فتح المستند
        Document pdfDocument = new Document(_dataDir + "TextField.pdf");
        Page page = pdfDocument.getPages().get_Item(1);
        // إنشاء حقل
        TextBoxField textBoxField = new TextBoxField(page, new Rectangle(100, 200, 300, 300));
        textBoxField.setPartialName("textbox1");
        textBoxField.setValue("Text Box");

        // TextBoxField.Border = new Border(
        Border border = new Border(textBoxField);
        border.setWidth(5);
        border.setDash(new Dash(1, 1));
        textBoxField.setBorder(border);

        textBoxField.setColor(Color.getGreen());

        // إضافة الحقل إلى المستند
        pdfDocument.getForm().add(textBoxField, 1);

        // حفظ ملف PDF المعدل
        pdfDocument.save(_dataDir + "TextBox_out.pdf");

    }

    
}
```