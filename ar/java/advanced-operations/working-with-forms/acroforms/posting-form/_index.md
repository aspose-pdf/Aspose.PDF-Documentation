---
title: نشر النماذج في PDF عبر جافا
linktitle: نماذج النشر
type: docs
weight: 75
url: /java/posting-form/
description: أضف أزرار الإرسال وإجراءات الإرسال إلى PDF AcroForms باستخدام Aspose.PDF لـ Java.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: أضف أزرار الإرسال وإجراءات نشر النموذج إلى ملفات PDF باستخدام Java
Abstract: توضح هذه المقالة كيفية إضافة وظيفة الإرسال إلى نماذج PDF باستخدام Aspose.PDF لـ Java. ويغطي إنشاء زر إرسال باستخدام FormEditor وإنشاء حقل زر مخصص يستخدم SubmitFormAction لمزيد من التحكم في عنوان URL للإرسال والإشارات.
---
يدعم Aspose.PDF for Java إنشاء زر إرسال يعتمد على الواجهة وعلى DOM.

## أضف زر إرسال باستخدام FormEditor

1. قم بإنشاء واجهة [FormEditor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/formeditor/) لمستند PDF المصدر.
1. قم بإضافة كائن زر الإرسال الذي تم تكوينه من خلال الواجهة [FormEditor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/formeditor/).
1. احفظ مستند PDF المحدث.

```java
public static void addSubmitButton(Path inputFile, Path outputFile) {
    FormEditor editor = new FormEditor();
    editor.bindPdf(inputFile.toString());
    try {
        editor.addSubmitBtn("submitbutton", 1, "Submit", "http://localhost/testing/show",
                100, 450, 150, 475);
        editor.save(outputFile.toString());
    } finally {
        editor.close();
    }
}
```

## أضف إجراء إرسال يدويًا

1. افتح ملف PDF المصدر [المستند](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. قم بإنشاء [SubmitFormAction](https://reference.aspose.com/pdf/java/com.aspose.pdf/submitformaction/) وعنوان URL [FileSpecification](https://reference.aspose.com/pdf/java/com.aspose.pdf/filespecification/).
1. قم بإنشاء [ButtonField](https://reference.aspose.com/pdf/java/com.aspose.pdf/buttonfield/) على [الصفحة] المستهدفة(https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) وقم بتعيين إجراء الإرسال.
1. احفظ ملف PDF المحدث [المستند](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

```java
public static void addSubmitAction(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        SubmitFormAction submitAction = new SubmitFormAction();
        submitAction.setUrl(new FileSpecification("http://localhost:3000/submit"));
        submitAction.setFlags(SubmitFormAction.EXPORT_FORMAT | SubmitFormAction.SUBMIT_COORDINATES);

        ButtonField submitButton = new ButtonField(document.getPages().get_Item(1), new Rectangle(10, 10, 100, 40));
        submitButton.setPartialName("SubmitButton");
        submitButton.setValue("Submit");
        submitButton.getPdfActions().add(submitAction);

        document.getForm().add(submitButton, 1);
        document.save(outputFile.toString());
    }
}
```
