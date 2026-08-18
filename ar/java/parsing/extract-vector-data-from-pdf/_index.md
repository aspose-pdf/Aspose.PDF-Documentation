---
title: استخراج بيانات المتجهات من ملف PDF باستخدام Java
linktitle: استخراج بيانات المتجهات من PDF
type: docs
weight: 80
url: /java/extract-vector-data-from-pdf/
description: يسهل Aspose.PDF استخراج البيانات المتجهة من ملف PDF. يمكنك الحصول على بيانات المتجهات، مثل الموضع وحدود المستطيل ومخرجات SVG.
lastmod: "2026-06-16"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
## الوصول إلى بيانات المتجهات من مستند PDF

استخدم `GraphicsAbsorber` لفحص العناصر الرسومية المتجهة على الصفحة وكتابة الشكل الهندسي الأساسي الخاص بها في ملف نصي.

1. افتح ملف PDF المصدر في مثيل [المستند](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. أنشئ [GraphicsAbsorter](https://reference.aspose.com/pdf/java/com.aspose.pdf.vector/graphicsabsorber/) وقم بزيارة [الصفحة] المستهدفة (https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) لتجميع عمليات الرسومات المتجهة.
1. قم بالتكرار عبر كائنات [GraphicElement](https://reference.aspose.com/pdf/java/com.aspose.pdf.vector/graphicelement/) المستخرجة واقرأ مجموعات المستطيل والموضع وعوامل التشغيل الخاصة بها.
1. أنشئ نص الإخراج باستخدام تفاصيل الشكل الهندسي وعدد عوامل التشغيل لكل عنصر.
1. اكتب بيانات المتجهات المستخرجة إلى ملف الإخراج.

```java
public static void extractGraphicsElements(Path inputFile, Path outputFile) throws Exception {
    try (Document document = new Document(inputFile.toString())) {
        GraphicsAbsorber absorber = new GraphicsAbsorber();
        absorber.visit(document.getPages().get_Item(1));

        StringBuilder text = new StringBuilder();
        int index = 1;
        for (GraphicElement element : absorber.getElements()) {
            text.append("Element ").append(index)
                    .append(": Rectangle = ").append(element.getRectangle())
                    .append(", Position = ").append(element.getPosition())
                    .append(", Operators = ").append(element.getOperators().size())
                    .append("\n");
            index++;
        }
        Files.writeString(outputFile, text.toString());
    }
}
```

## حفظ الرسومات المتجهة للصفحة إلى SVG

1. افتح ملف PDF المصدر في مثيل [المستند](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. احصل على الهدف [الصفحة](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) من المستند.
1. اتصل بـ `page.trySaveVectorGraphics(outputFile.toString())` لتصدير محتوى الرسومات المتجهة لتلك الصفحة مباشرة إلى SVG.

```java
public static void saveVectorGraphicsToSvg(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        Page page = document.getPages().get_Item(1);
        page.trySaveVectorGraphics(outputFile.toString());
    }
}
```

## احفظ كل عنصر مستخرج في ملف SVG منفصل

1. افتح ملف PDF المصدر في مثيل [المستند](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. أنشئ [GraphicsAbsorter](https://reference.aspose.com/pdf/java/com.aspose.pdf.vector/graphicsabsorber/) وقم بزيارة [الصفحة] المستهدفة (https://reference.aspose.com/pdf/java/com.aspose.pdf/page/).
1. قم بإنشاء دليل الإخراج للمسارات الفرعية المستخرجة قبل كتابة أي ملفات.
1. قم بالتكرار عبر كائنات [GraphicElement](https://reference.aspose.com/pdf/java/com.aspose.pdf.vector/graphicelement/) المستخرجة واستدعاء `saveToSvg(...)` لكل عنصر.
1. احفظ كل عنصر مستخرج في ملف SVG منفصل.

```java
public static void extractSubpathsToSvgs(Path inputFile, Path outputDir) throws Exception {
    try (Document document = new Document(inputFile.toString())) {
        GraphicsAbsorber absorber = new GraphicsAbsorber();
        absorber.visit(document.getPages().get_Item(1));
        Path subpathsDir = outputDir.resolve("subpaths");
        Files.createDirectories(subpathsDir);

        int index = 1;
        for (GraphicElement element : absorber.getElements()) {
            element.saveToSvg(subpathsDir.resolve("subpath_" + index + ".svg").toString());
            index++;
        }
    }
}
```

## اجمع العناصر المستخرجة في ملف SVG واحد

1. افتح ملف PDF المصدر في مثيل [المستند](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. أنشئ [GraphicsAbsorter](https://reference.aspose.com/pdf/java/com.aspose.pdf.vector/graphicsabsorber/) وقم بزيارة [الصفحة] المستهدفة (https://reference.aspose.com/pdf/java/com.aspose.pdf/page/).
1. قم بإنشاء ترميز غلاف SVG الذي سيحتوي على الأجزاء المتجهة المدمجة.
1. قم بالتكرار عبر كائنات [GraphicElement](https://reference.aspose.com/pdf/java/com.aspose.pdf.vector/graphicelement/) المستخرجة وألحق كل جزء SVG تم إنشاؤه.
1. اكتب مخرجات SVG المدمجة إلى الملف الهدف.

```java
public static void extractListOfElementsToSingleImage(Path inputFile, Path outputFile) throws Exception {
    try (Document document = new Document(inputFile.toString())) {
        GraphicsAbsorber absorber = new GraphicsAbsorber();
        absorber.visit(document.getPages().get_Item(1));

        StringBuilder svg = new StringBuilder();
        svg.append("<svg xmlns=\"http://www.w3.org/2000/svg\">\n");
        for (GraphicElement element : absorber.getElements()) {
            svg.append(element.saveToSvg()).append("\n");
        }
        svg.append("</svg>\n");
        Files.writeString(outputFile, svg.toString());
    }
}
```

## استخراج عنصر متجه واحد

1. افتح ملف PDF المصدر في مثيل [المستند](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. أنشئ [GraphicsAbsorter](https://reference.aspose.com/pdf/java/com.aspose.pdf.vector/graphicsabsorber/) وقم بزيارة [الصفحة] المستهدفة (https://reference.aspose.com/pdf/java/com.aspose.pdf/page/).
1. احصل على [GraphicElement](https://reference.aspose.com/pdf/java/com.aspose.pdf.vector/graphicelement/) المطلوب من مجموعة العناصر المستخرجة.
1. تحقق مما إذا كان العنصر المحدد هو [XFormPlacement](https://reference.aspose.com/pdf/java/com.aspose.pdf.vector/xformplacement/) وانزل إلى عناصره المتداخلة عند الحاجة.
1. احفظ عنصر المتجه المحدد في ملف SVG الناتج.

```java
public static void extractSingleVectorElement(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        GraphicsAbsorber graphicsAbsorber = new GraphicsAbsorber();
        Page page = document.getPages().get_Item(1);
        graphicsAbsorber.visit(page);
        if (graphicsAbsorber.getElements().size() > 1) {
            GraphicElement xformPlacement = graphicsAbsorber.getElements().get_Item(1);
            if (xformPlacement instanceof XFormPlacement) {
                XFormPlacement placement = (XFormPlacement) xformPlacement;
                if (placement.getElements().size() > 2) {
                    placement.getElements().get_Item(2).saveToSvg(outputFile.toString());
                }
            } else {
                xformPlacement.saveToSvg(outputFile.toString());
            }
        }
    }
}
```
