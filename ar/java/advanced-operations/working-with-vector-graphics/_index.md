---
title: العمل مع الرسومات المتجهة في Java
linktitle: العمل مع الرسومات المتجهة
type: docs
weight: 100
url: /java/working-with-vector-graphics/
description: تعرف على كيفية استخراج الرسومات المتجهة ونقلها وإزالتها ونسخها وتصديرها في مستندات PDF باستخدام Java.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: استخدم GraphicsAbsorter لفحص ومعالجة رسومات PDF المتجهة في Java
Abstract: تشرح هذه المقالة كيفية العمل مع الرسومات المتجهة في Aspose.PDF لـ Java باستخدام فئة GraphicsAbsorter. تعرف على كيفية فحص العناصر المتجهة على الصفحة، ونقلها أو إزالتها، ونسخ الرسومات بين الصفحات، وتصدير محتوى المتجه إلى SVG.
---
يعرض Aspose.PDF لـ Java محتوى المتجهات من خلال الكائنات `GraphicsAbsorber` و`GraphicElement`. يتيح لك ذلك فحص العناصر المتجهة ذات المستوى المنخفض في الصفحة ثم تحديثها أو إزالتها أو نسخها أو تصديرها.

## فحص الرسومات المتجهة على الصفحة

استخدم هذا المثال عندما تحتاج إلى تعداد العناصر المتجهة وفحص صفحتها وموضعها وعدد عوامل التشغيل.

1. افتح ملف PDF المصدر [المستند](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. قم بإنشاء [GraphicsAbsorter](https://reference.aspose.com/pdf/java/com.aspose.pdf/vector/graphicsabsorber/) وقم بزيارة الصفحة المستهدفة.
1. قم بالتكرار عبر كائنات [GraphicElement](https://reference.aspose.com/pdf/java/com.aspose.pdf/vector/graphicelement/) الممتصة وإخراج خصائصها.

```java
public static void usingGraphicsAbsorber(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        GraphicsAbsorber graphicsAbsorber = new GraphicsAbsorber();
        try {
            Page page = document.getPages().get_Item(1);
            graphicsAbsorber.visit(page);
            for (GraphicElement element : graphicsAbsorber.getElements()) {
                System.out.println("Page Number: " + element.getSourcePage().getNumber());
                System.out.println("Position: (" + element.getPosition().getX() + ", "
                        + element.getPosition().getY() + ")");
                System.out.println("Number of Operators: " + element.getOperators().size());
            }
        } finally {
            graphicsAbsorber.dispose();
        }
    }
}
```

## نقل الرسومات المتجهة على الصفحة

استخدم هذا المثال عندما يجب نقل جميع العناصر المتجهة المكتشفة إلى موضع جديد.

1. افتح ملف PDF المصدر [المستند](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. قم بزيارة الصفحة المستهدفة باستخدام [GraphicsAbsorter](https://reference.aspose.com/pdf/java/com.aspose.pdf/vector/graphicsabsorber/) وقم بمنع التحديثات مؤقتًا.
1. قم بتغيير موضع كل عنصر ممتص، واستأنف التحديثات، واحفظ المستند.

```java
public static void moveGraphics(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        GraphicsAbsorber graphicsAbsorber = new GraphicsAbsorber();
        try {
            Page page = document.getPages().get_Item(1);
            graphicsAbsorber.visit(page);
            graphicsAbsorber.suppressUpdate();
            for (GraphicElement element : graphicsAbsorber.getElements()) {
                Point position = element.getPosition();
                element.setPosition(new Point(position.getX() + 150, position.getY() - 10));
            }
            graphicsAbsorber.resumeUpdate();
        } finally {
            graphicsAbsorber.dispose();
        }
        document.save(outputFile.toString());
    }
    System.out.println("Vector graphics moved in " + outputFile);
}
```

## إزالة الرسومات المتجهة حسب الموضع مع إزالة العنصر

استخدم هذا المثال عندما يجب حذف العناصر المتجهة الموجودة داخل مستطيل معين واحدًا تلو الآخر.

1. افتح ملف PDF المصدر [المستند](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. قم بزيارة الصفحة باستخدام [GraphicsAbsorter](https://reference.aspose.com/pdf/java/com.aspose.pdf/vector/graphicsabsorber/) وحدد الهدف [المستطيل](https://reference.aspose.com/pdf/java/com.aspose.pdf/rectangle/).
1. قم بإزالة العناصر المطابقة، واستأنف التحديثات، واحفظ المستند.

```java
public static void removeGraphicsMethod1(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        GraphicsAbsorber graphicsAbsorber = new GraphicsAbsorber();
        try {
            Page page = document.getPages().get_Item(1);
            Rectangle rectangle = new Rectangle(70, 248, 170, 252, true);
            graphicsAbsorber.visit(page);
            graphicsAbsorber.suppressUpdate();
            for (GraphicElement element : graphicsAbsorber.getElements()) {
                if (rectangle.contains(element.getPosition(), false)) {
                    element.remove();
                }
            }
            graphicsAbsorber.resumeUpdate();
        } finally {
            graphicsAbsorber.dispose();
        }
        document.save(outputFile.toString());
    }
    System.out.println("Vector graphics removed with method 1 in " + outputFile);
}
```

## قم بإزالة الرسومات المتجهة عن طريق حذف المجموعة

استخدم هذا المثال عندما يجب تجميع العناصر المتجهة المطابقة أولاً ثم إزالتها في عملية صفحة واحدة.

1. افتح ملف PDF المصدر [المستند](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. تفضل بزيارة الصفحة التي تحتوي على [GraphicsAbsorter](https://reference.aspose.com/pdf/java/com.aspose.pdf/vector/graphicsabsorber/) واجمع العناصر المطابقة.
1. احذف الرسومات المجمعة من محتويات الصفحة واحفظ المستند المحدث.

```java
public static void removeGraphicsMethod2(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        GraphicsAbsorber graphicsAbsorber = new GraphicsAbsorber();
        try {
            Page page = document.getPages().get_Item(1);
            Rectangle rectangle = new Rectangle(70, 248, 170, 252, true);
            graphicsAbsorber.visit(page);
            GraphicElementCollection removedElements = new GraphicElementCollection();
            for (GraphicElement element : graphicsAbsorber.getElements()) {
                if (rectangle.contains(element.getPosition(), false)) {
                    removedElements.add(element);
                }
            }
            page.getContents().suppressUpdate();
            page.deleteGraphics(removedElements);
            page.getContents().resumeUpdate();
        } finally {
            graphicsAbsorber.dispose();
        }
        document.save(outputFile.toString());
    }
    System.out.println("Vector graphics removed with method 2 in " + outputFile);
}
```

## انسخ الرسومات المتجهة إلى عنصر صفحة آخر حسب العنصر

استخدم هذا المثال عندما يجب إضافة كل عنصر متجه ممتص بشكل فردي إلى صفحة جديدة.

1. افتح ملف PDF المصدر [المستند](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) وأضف صفحة الوجهة.
1. تفضل بزيارة الصفحة المصدر باستخدام [GraphicsAbsorter](https://reference.aspose.com/pdf/java/com.aspose.pdf/vector/graphicsabsorber/).
1. أضف كل [GraphicElement](https://reference.aspose.com/pdf/java/com.aspose.pdf/vector/graphicelement/) إلى الصفحة الوجهة واحفظ المستند.

```java
public static void addToAnotherPageMethod1(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        GraphicsAbsorber graphicsAbsorber = new GraphicsAbsorber();
        try {
            Page page1 = document.getPages().get_Item(1);
            Page page2 = document.getPages().add();
            graphicsAbsorber.visit(page1);
            page2.getContents().suppressUpdate();
            for (GraphicElement element : graphicsAbsorber.getElements()) {
                element.addOnPage(page2);
            }
            page2.getContents().resumeUpdate();
        } finally {
            graphicsAbsorber.dispose();
        }
        document.save(outputFile.toString());
    }
    System.out.println("Vector graphics copied with method 1 in " + outputFile);
}
```

## انسخ الرسومات المتجهة إلى صفحة أخرى كمجموعة

استخدم هذا المثال عندما يجب نسخ مجموعة الرسومات المتجهة الممتصة بالكامل إلى صفحة جديدة في مكالمة واحدة.

1. افتح ملف PDF المصدر [المستند](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) وأضف صفحة الوجهة.
1. تفضل بزيارة الصفحة المصدر باستخدام [GraphicsAbsorter](https://reference.aspose.com/pdf/java/com.aspose.pdf/vector/graphicsabsorber/).
1. أضف مجموعة الرسومات الممتصة إلى الصفحة الوجهة واحفظ المستند.

```java
public static void addToAnotherPageMethod2(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        GraphicsAbsorber graphicsAbsorber = new GraphicsAbsorber();
        try {
            Page page1 = document.getPages().get_Item(1);
            Page page2 = document.getPages().add();
            graphicsAbsorber.visit(page1);
            page2.getContents().suppressUpdate();
            page2.addGraphics(graphicsAbsorber.getElements());
            page2.getContents().resumeUpdate();
        } finally {
            graphicsAbsorber.dispose();
        }
        document.save(outputFile.toString());
    }
    System.out.println("Vector graphics copied with method 2 in " + outputFile);
}
```
