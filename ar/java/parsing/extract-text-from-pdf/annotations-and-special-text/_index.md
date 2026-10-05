---
title: التعليقات التوضيحية والنص الخاص باستخدام Java
linktitle: التعليقات التوضيحية والنص الخاص
type: docs
weight: 40
url: /ar/java/annotation-and-special-text/
description: تعرّف على كيفية استخراج النص من التعليقات التوضيحية للختم، والنص المظلل، والمحتوى ذو النص الفائق أو النص السفلي في مستندات PDF باستخدام Aspose.PDF for Java.
lastmod: "2026-10-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
## استخراج النص المظلل

التكرار عبر ملاحظات الصفحة وقراءة النص المميز من `HighlightAnnotation`.

1. افتح ملف PDF المصدر في مثيل [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. مرّ على الـ الكائنات [Annotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/annotation/) على الهدف [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/).
1. تحقّق مما إذا كان كل توضيح هو [HighlightAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/highlightannotation/) قبل تحويله إلى فئة التوضيح ذات النوع المحدد.
1. اقرأ النص المحدد من كل توضيح تظليل واطبعه على وحدة التحكم.

```java
public static void extractHighlightedText(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        for (Annotation annotation : document.getPages().get_Item(1).getAnnotations()) {
            if (annotation instanceof HighlightAnnotation) {
                HighlightAnnotation highlightAnnotation = (HighlightAnnotation) annotation;
                System.out.println(highlightAnnotation.getMarkedText());
            }
        }
    }
}
```

## استخراج النص من تعليقات الطوابع

قراءة تدفق المظهر العادي من توضيح الختم وتمريره `TextAbsorber`.

1. افتح ملف PDF المصدر في مثيل [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. مرّ على الـ الكائنات [Annotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/annotation/) على الهدف [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/).
1. صفِّ التعليقات التوضيحية إلى تلك التي يكون نوعها `Stamp`.
1. أنشئ كائنًا من الفئة [TextAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/textabsorber/) وطلب إدخال المظهر العادي من قاموس مظهر التعليق التوضيحي للستامب.
1. زُر المظهر [XForm](https://reference.aspose.com/pdf/java/com.aspose.pdf/xform/) واطبع النص المستخرج.

```java
public static void extractStampText(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        for (Annotation annotation : document.getPages().get_Item(1).getAnnotations()) {
            if (annotation.getAnnotationType() == AnnotationType.Stamp) {
                TextAbsorber absorber = new TextAbsorber();
                Object[] xforms = new Object[1];
                if (annotation.getAppearance().tryGetValue("N", xforms) && xforms[0] instanceof XForm) {
                    absorber.visit((XForm) xforms[0]);
                    System.out.println(absorber.getText());
                }
            }
        }
    }
}
```

## استخراج تفاصيل النص العلوي والنص السفلي

استخدام `TextFragmentAbsorber` عند الحاجة إلى كل من النص المستخرج وعلامات الفوقية أو السفلية لكل جزء.

1. افتح ملف PDF المصدر في مثيل [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. أنشئ كائنًا من الفئة [TextFragmentAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/textfragmentabsorber/) لتحليل النص على مستوى الجزء.
1. زُر الهدف [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) واجمعها الكائنات [TextFragment](https://reference.aspose.com/pdf/java/com.aspose.pdf/textfragment/).
1. مرّ على تلك الأجزاء واقرأ النص مع علامات العلوي والسفلي من `fragment.getTextState()`.
1. اكتب التفاصيل المستخرجة إلى ملف الإخراج.

```java
public static void extractSuperSubDetails(Path inputFile, Path outputFile, int pageNumber) throws Exception {
    try (Document document = new Document(inputFile.toString())) {
        TextFragmentAbsorber absorber = new TextFragmentAbsorber();
        document.getPages().get_Item(pageNumber).accept(absorber);
        StringBuilder details = new StringBuilder();
        for (TextFragment fragment : absorber.getTextFragments()) {
            details.append("Text: '").append(fragment.getText())
                    .append("' | Superscript: ").append(fragment.getTextState().isSuperscript())
                    .append(" | Subscript: ").append(fragment.getTextState().isSubscript())
                    .append(System.lineSeparator());
        }
        Files.writeString(outputFile, details.toString());
    }
}
```
