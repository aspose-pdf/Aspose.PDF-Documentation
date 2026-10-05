---
title: التعليقات التوضيحية التفاعلية باستخدام Java
linktitle: التعليقات التوضيحية التفاعلية
type: docs
weight: 30
url: /ar/java/pdfannotationeditor-class/interactive-annotations/
description: تعلم كيفية إضافة وفحص وحذف التعليقات التوضيحية للروابط في مستندات PDF باستخدام Java.
lastmod: "2026-10-05"
TechArticle: true
AlternativeHeadline: العمل مع التعليقات التوضيحية التفاعلية لملفات PDF في Java
Abstract: تشرح هذه المقالة كيفية العمل مع التعليقات التوضيحية التفاعلية للروابط في ملفات PDF باستخدام Java. تغطي المقالة تحديد النص، وإنشاء تعليق توضيحي للربط فوق المنطقة المتطابقة من النص، وقراءة التعليقات التوضيحية للروابط الموجودة، وحذفها.
---
## إضافة تعليق توضيحي للربط

1. حمّل مستند PDF المصدر وابحث في الصفحة الأولى عن النص المستهدف.
2. استخدم مستطيل النص المطابق لإنشاء `LinkAnnotation` وعيّن عنوان URI الوجهة.
3. أضف التعليقة إلى الصفحة واحفظ ملف PDF المحدث.

```java
public static void linkAdd(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        TextFragmentAbsorber textFragmentAbsorber = new TextFragmentAbsorber("file");
        document.getPages().get_Item(1).accept(textFragmentAbsorber);

        TextFragment phoneNumberFragment = textFragmentAbsorber.getTextFragments().get_Item(1);

        LinkAnnotation linkAnnotation = new LinkAnnotation(
                document.getPages().get_Item(1), phoneNumberFragment.getRectangle());
        linkAnnotation.setAction(new GoToURIAction("www.aspose.com"));

        document.getPages().get_Item(1).getAnnotations().add(linkAnnotation);
        document.save(outputFile.toString());
    }
}
```
