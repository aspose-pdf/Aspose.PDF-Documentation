---
title: استخراج النص من الأختام
type: docs
weight: 60
url: ar/java/extract-text-from-stamps/
---

## استخراج النص من التعليقات التوضيحية للأختام

يسمح لك Aspose.PDF for Java باستخراج النص من التعليقات التوضيحية للأختام. لاستخراج النص من التعليقات التوضيحية للأختام في ملف PDF، يمكن استخدام الخطوات التالية.

1. قم بإنشاء كائن من فئة Document
1. الحصول على التعليق التوضيحي المطلوب من قائمة التعليقات التوضيحية لصفحة
1. تعريف كائن جديد من فئة TextAbsorber
1. استخدام طريقة visit الخاصة بـ TextAbsorber للحصول على النص

```java
Document doc = new Document(dataDir+"test.pdf");
Annotation item = doc.getPages().get_Item(1).getAnnotations().get_Item(3);
if (item instanceof StampAnnotation ) {
   StampAnnotation annot = (StampAnnotation) item;
   TextAbsorber ta = new TextAbsorber();
   XForm ap = annot.getNormalAppearance();
   ta.visit(ap);
   System.out.println(ta.getText());
}
```