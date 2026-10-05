---
title: استخراج بيانات المتجه من ملف PDF باستخدام Java
linktitle: استخراج بيانات المتجه من PDF
type: docs
weight: 80
url: /ar/java/extract-vector-data-from-pdf/
description: Aspose.PDF يجعل من السهل استخراج بيانات المتجه من ملف PDF. يمكنك الحصول على بيانات المتجه، مثل الموضع، حدود المستطيل، وإنتاج SVG.
lastmod: "2026-10-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
## الوصول إلى بيانات المتجه من مستند PDF

استخدام `GraphicsAbsorber` لفحص عناصر الرسومات المتجهية على صفحة وكتابة هندستها الأساسية إلى ملف نصي.

1. افتح ملف PDF المصدر في كائن [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. أنشئ كائنًا من الفئة [GraphicsAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf.vector/graphicsabsorber/) وزيارة الهدف [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) لجمع عمليات الرسومات المتجهية.
1. مرّ على المستخرجة الكائنات [GraphicElement](https://reference.aspose.com/pdf/java/com.aspose.pdf.vector/graphicelement/) واقرأ مستطيلها، موضعها، ومجموعات المشغلين.
1. ابنِ نص الإخراج مع تفاصيل الهندسة وعدد المشغلات لكل عنصر.
1. اكتب بيانات المتجه المستخرجة إلى ملف الإخراج.

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

## حفظ رسومات الصفحة المتجهة بصيغة SVG

1. افتح ملف PDF المصدر في كائن [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. احصل على الهدف [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) من المستند.
1. استدعِ `page.trySaveVectorGraphics(outputFile.toString())` لتصدير محتوى الرسومات المتجهة لتلك الصفحة مباشرة إلى SVG..

```java
public static void saveVectorGraphicsToSvg(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        Page page = document.getPages().get_Item(1);
        page.trySaveVectorGraphics(outputFile.toString());
    }
}
```

## حفظ كل عنصر مستخرج في ملف SVG منفصل

1. افتح ملف PDF المصدر في كائن [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. أنشئ كائنًا من الفئة [GraphicsAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf.vector/graphicsabsorber/) وزيارة الهدف [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/).
1. أنشئ دليل الإخراج للمسارات الفرعية المستخرجة قبل كتابة أي ملفات.
1. مرّ على المستخرجة الكائنات [GraphicElement](https://reference.aspose.com/pdf/java/com.aspose.pdf.vector/graphicelement/) والاستدعاء `saveToSvg(...)` لكل عنصر.
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

## دمج العناصر المستخرجة في ملف SVG واحد

1. افتح ملف PDF المصدر في كائن [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. أنشئ كائنًا من الفئة [GraphicsAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf.vector/graphicsabsorber/) وزيارة الهدف [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/).
1. أنشئ وسوم تغليف SVG التي ستحتوي على أجزاء المتجه المدمجة.
1. مرّ على المستخرجة الكائنات [GraphicElement](https://reference.aspose.com/pdf/java/com.aspose.pdf.vector/graphicelement/) وأضف كل جزء SVG تم إنشاؤه.
1. اكتب ناتج SVG المدمج إلى الملف الهدف.

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

1. افتح ملف PDF المصدر في كائن [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. أنشئ كائنًا من الفئة [GraphicsAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf.vector/graphicsabsorber/) وزيارة الهدف [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/).
1. احصل على المطلوب [GraphicElement](https://reference.aspose.com/pdf/java/com.aspose.pdf.vector/graphicelement/) من مجموعة العناصر المستخرجة.
1. تحقّق مما إذا كان العنصر المحدد هو [XFormPlacement](https://reference.aspose.com/pdf/java/com.aspose.pdf.vector/xformplacement/) وانزل إلى عناصره المتداخلة عند الحاجة.
1. احفظ العنصر المتجه المحدد إلى ملف SVG الناتج.

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
