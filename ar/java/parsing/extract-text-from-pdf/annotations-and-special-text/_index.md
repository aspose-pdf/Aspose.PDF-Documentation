---
title: التعليقات التوضيحية والنص الخاص باستخدام Java
linktitle: الشروح والنص الخاص
type: docs
weight: 40
url: /java/annotation-and-special-text/
description: تعرف على كيفية استخراج النص من التعليقات التوضيحية للطوابع والنص المميز والمحتوى المرتفع أو المنخفض في مستندات PDF باستخدام Aspose.PDF لـ Java.
lastmod: "2026-06-16"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
## استخراج النص المميز

قم بالتكرار من خلال التعليقات التوضيحية للصفحة وقراءة النص المميز من `HighlightAnnotation`.

1. افتح ملف PDF المصدر في مثيل [المستند](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. قم بالتكرار عبر كائنات [التعليق التوضيحي](https://reference.aspose.com/pdf/java/com.aspose.pdf/annotation/) الموجودة على [الصفحة] المستهدفة(https://reference.aspose.com/pdf/java/com.aspose.pdf/page/).
1. تحقق مما إذا كان كل تعليق توضيحي هو [HighlightAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/highlightannotation/) قبل إرساله إلى فئة التعليق التوضيحي المكتوب.
1. اقرأ النص المحدد من كل تعليق توضيحي مميز وقم بطباعته على وحدة التحكم.

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

## استخراج النص من التعليقات التوضيحية للطوابع

اقرأ تدفق المظهر العادي من تعليق توضيحي للطوابع وقم بتمريره عبر `TextAbsorber`.

1. افتح ملف PDF المصدر في مثيل [المستند](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. قم بالتكرار عبر كائنات [التعليق التوضيحي](https://reference.aspose.com/pdf/java/com.aspose.pdf/annotation/) الموجودة على [الصفحة] المستهدفة(https://reference.aspose.com/pdf/java/com.aspose.pdf/page/).
1. قم بتصفية التعليقات التوضيحية لتلك التي يكون نوعها `Stamp`.
1. قم بإنشاء [TextAbsorter](https://reference.aspose.com/pdf/java/com.aspose.pdf/textabsorber/) واطلب إدخال المظهر العادي من قاموس مظهر التعليقات التوضيحية للختم.
1. قم بزيارة المظهر [XForm](https://reference.aspose.com/pdf/java/com.aspose.pdf/xform/) وقم بطباعة النص المستخرج.

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

## استخراج تفاصيل النص المرتفع والمنخفض

استخدم `TextFragmentAbsorber` عندما تحتاج إلى النص المستخرج والعلامات المرتفعة أو المنخفضة على كل جزء.

1. افتح ملف PDF المصدر في مثيل [المستند](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. قم بإنشاء [TextFragmentAbsorter](https://reference.aspose.com/pdf/java/com.aspose.pdf/textfragmentabsorber/) لتحليل النص على مستوى الجزء.
1. قم بزيارة الهدف [الصفحة](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) وجمع كائنات [TextFragment](https://reference.aspose.com/pdf/java/com.aspose.pdf/textfragment/) الخاصة بها.
1. كرر هذه الأجزاء واقرأ النص مع العلامات المرتفعة والمنخفضة من `fragment.getTextState()`.
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
