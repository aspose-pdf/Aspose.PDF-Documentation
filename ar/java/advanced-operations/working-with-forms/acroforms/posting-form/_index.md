---
title: نشر النماذج في PDF عبر Java
linktitle: نشر النماذج
type: docs
weight: 75
url: /ar/java/posting-form/
description: إضافة أزرار الإرسال وإجراءات الإرسال إلى نماذج PDF AcroForms باستخدام Aspose.PDF for Java.
lastmod: "2026-10-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: إضافة أزرار الإرسال وإجراءات نشر النموذج إلى ملفات PDF باستخدام Java
Abstract: توضح هذه المقالة كيفية إضافة وظيفة الإرسال إلى نماذج PDF باستخدام Aspose.PDF for Java. وتغطي إنشاء زر إرسال باستخدام FormEditor وبناء حقل زر مخصص يستخدم SubmitFormAction لمزيد من التحكم في عنوان URL للإرسال والعلامات.
---
يدعم Aspose.PDF for Java إنشاء أزرار الإرسال القائم على الواجهة (facade) والقائم على DOM.

## إضافة زر إرسال باستخدام FormEditor

1. أنشئ واجهة [FormEditor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/formeditor/) لمستند PDF المصدر.
1. أضف كائن زر الإرسال المكوّن من خلال [FormEditor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/formeditor/) الواجهة.
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

## إضافة إجراء إرسال يدويًا

1. افتح PDF المصدر [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. أنشئ كائنًا من الفئة [SubmitFormAction](https://reference.aspose.com/pdf/java/com.aspose.pdf/submitformaction/) و URL [FileSpecification](https://reference.aspose.com/pdf/java/com.aspose.pdf/filespecification/).
1. أنشئ كائنًا من الفئة [ButtonField](https://reference.aspose.com/pdf/java/com.aspose.pdf/buttonfield/) على الهدف [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) وعيّن إجراء الإرسال.
1. احفظ ملف PDF المحدث [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

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
