---
title: التعليقات التوضيحية التفاعلية باستخدام جافا
linktitle: التعليقات التوضيحية التفاعلية
type: docs
weight: 30
url: /java/pdfannotationeditor-class/interactive-annotations/
description: تعرف على كيفية إضافة التعليقات التوضيحية للارتباط وفحصها وحذفها في مستندات PDF باستخدام Java.
lastmod: "2026-06-09"
TechArticle: true
AlternativeHeadline: العمل مع تعليقات PDF التفاعلية في Java
Abstract: تشرح هذه المقالة كيفية العمل مع التعليقات التوضيحية للارتباط التفاعلي في ملفات PDF باستخدام Java. ويغطي تحديد موقع النص، وإنشاء تعليق توضيحي للرابط فوق منطقة النص المطابق، وقراءة التعليقات التوضيحية للرابط الموجود، وحذفها.
---
## إضافة تعليق توضيحي للارتباط

1. قم بتحميل مستند PDF المصدر وابحث في الصفحة الأولى عن النص المستهدف.
2. استخدم مستطيل النص المطابق لإنشاء `LinkAnnotation` وتعيين URI للوجهة.
3. أضف التعليق التوضيحي إلى الصفحة واحفظ ملف PDF المحدث.

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
