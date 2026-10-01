---
title: العمل مع الرسومات المتجهة في Java
linktitle: العمل مع الرسومات المتجهة
type: docs
weight: 100
url: /ar/java/working-with-vector-graphics/
description: تعلم كيفية استخراج وتحريك وإزالة ونسخ وتصدير الرسومات المتجهة في مستندات PDF باستخدام Java.
lastmod: "2026-10-01"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: استخدم GraphicsAbsorber لتفحص وتحريك الرسومات المتجهة في PDF باستخدام Java
Abstract: تشرح هذه المقالة كيفية العمل مع الرسومات المتجهة في Aspose.PDF for Java باستخدام الفئة GraphicsAbsorber. تعلم كيفية فحص عناصر المتجهة على صفحة، نقلها أو إزالتها، نسخ الرسومات بين الصفحات، وتصدير محتوى المتجه إلى SVG.
---
Aspose.PDF for Java يكشف محتوى المتجهات عبر `GraphicsAbsorber` و `GraphicElement` الكائنات. يتيح لك هذا فحص عناصر المتجه منخفضة المستوى على صفحة ثم تحديثها أو إزالتها أو نسخها أو تصديرها.

## فحص الرسومات المتجهية على صفحة

استخدم هذا المثال عندما تحتاج إلى تعداد عناصر المتجه وفحص صفحتها وموقعها وعدد المشغلات.

1. افتح ملف PDF المصدر [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. إنشاء [GraphicsAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/vector/graphicsabsorber/) وزيارة الصفحة المستهدفة.
1. التكرار عبر المستخلص [GraphicElement](https://reference.aspose.com/pdf/java/com.aspose.pdf/vector/graphicelement/) الكائنات وعرض خصائصها.

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

## تحريك الرسوم المتجهة على الصفحة

استخدم هذا المثال عندما يجب إزاحة جميع عناصر المتجه المكتشفة إلى موضع جديد.

1. افتح ملف PDF المصدر [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. زيارة الصفحة المستهدفة باستخدام [GraphicsAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/vector/graphicsabsorber/) وإيقاف التحديثات مؤقتًا
1. غيّر موضع كل عنصر مُمتص، استأنف التحديثات، واحفظ المستند.

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

## إزالة الرسومات المتجهة حسب الموقع مع إزالة العنصر

استخدم هذا المثال عندما يجب حذف العناصر المتجهية داخل مستطيل محدد واحدةً تلو الأخرى.

1. افتح ملف PDF المصدر [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. قم بزيارة الصفحة باستخدام [GraphicsAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/vector/graphicsabsorber/) وحدد الهدف [Rectangle](https://reference.aspose.com/pdf/java/com.aspose.pdf/rectangle/).
1. إزالة العناصر المطابقة، استئناف التحديثات، وحفظ المستند.

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

## إزالة الرسومات المتجهية عن طريق حذف مجموعة

استخدم هذا المثال عندما يجب جمع عناصر المتجه المطابقة أولاً ثم إزالتها في عملية صفحة واحدة.

1. افتح ملف PDF المصدر [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. قم بزيارة الصفحة باستخدام [GraphicsAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/vector/graphicsabsorber/) واجمع العناصر المطابقة.
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

## انسخ الرسومات المتجهة إلى عنصر صفحة آخر عنصرًا بعنصر

استخدم هذا المثال عندما يجب إضافة كل عنصر متجه مُمتص بشكل فردي إلى صفحة جديدة.

1. افتح ملف PDF المصدر [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) وأضف صفحة وجهة.
1. قم بزيارة صفحة المصدر باستخدام [GraphicsAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/vector/graphicsabsorber/).
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

## نسخ الرسومات المتجهية إلى صفحة أخرى كمجموعة

استخدم هذا المثال عندما يجب نسخ مجموعة الرسوم المتجهة الممتصة بالكامل إلى صفحة جديدة في استدعاء واحد.

1. افتح ملف PDF المصدر [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) وأضف صفحة وجهة.
1. قم بزيارة صفحة المصدر باستخدام [GraphicsAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/vector/graphicsabsorber/).
1. أضف مجموعة الرسومات الممتصة إلى صفحة الوجهة واحفظ المستند.

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
