---
title: الحصول على وتعيين خصائص صفحة PDF في Java
linktitle: الحصول على خصائص الصفحة وتعيينها
type: docs
weight: 90
url: /java/get-and-set-page-properties/
description: تعرف على كيفية فحص خصائص صفحة PDF مثل معلومات العدد والمربعات والتدوير والألوان في Java.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: فحص عدد الصفحات والمربعات ونوع الألوان في ملفات PDF باستخدام Java
Abstract: تشرح هذه المقالة كيفية فحص خصائص الصفحة باستخدام Aspose.PDF لـ Java. ويغطي قراءة عدد الصفحات، وإنشاء الفقرات والتحقق من العدد الناتج قبل الحفظ، وطباعة جميع قيم مربع الصفحة الرئيسية، وتحديد نوع اللون لكل صفحة.
---
يمكن لـ Aspose.PDF لـ Java فحص عدد الصفحات ومربعات الصفحات والتدوير ونوع لون الصفحة.

## الحصول على عدد الصفحات

استخدم هذا المثال عندما تحتاج إلى قراءة العدد الإجمالي للصفحات في ملف PDF.

1. افتح ملف PDF المصدر [المستند](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. اقرأ حجم مجموعة الصفحات.
1. إخراج إجمالي عدد الصفحات.

```java
public static void getPageCount(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        System.out.println("Page Count: " + document.getPages().size());
    }
}
```

## احصل على عدد الصفحات قبل الحفظ

استخدم هذا المثال عندما تحتاج إلى معرفة عدد الصفحات التي سينتجها المحتوى الذي تم إنشاؤه قبل كتابة الملف.

1. قم بإنشاء [مستند] PDF جديد (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) وأضف محتوى إلى الصفحة.
1. معالجة الفقرات لفرض حساب التخطيط.
1. اقرأ عدد الصفحات الناتج وأخرجه.

```java
public static void getPageCountWithoutSaving(Path inputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();
        for (int i = 0; i < 300; i++) {
            page.getParagraphs().add(new TextFragment("Pages count test"));
        }
        document.processParagraphs();
        System.out.println("Number of pages in document = " + document.getPages().size());
    }
}
```

## الحصول على خصائص مربع الصفحة

استخدم هذا المثال عندما تحتاج إلى فحص جميع أبعاد المربع الرئيسية وقيم تدوير الصفحة.

1. افتح ملف PDF المصدر [المستند](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) وقم بالوصول إلى الصفحة المستهدفة.
1. قم بتجميع قيم مربع الصفحة في الخريطة.
1. إخراج الأبعاد ومعلومات دوران الصفحة.

```java
public static void getPageProperties(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        Page page = document.getPages().get_Item(1);
        Map<String, Rectangle> boxes = new LinkedHashMap<>();
        boxes.put("ArtBox", page.getArtBox());
        boxes.put("BleedBox", page.getBleedBox());
        boxes.put("CropBox", page.getCropBox());
        boxes.put("MediaBox", page.getMediaBox());
        boxes.put("TrimBox", page.getTrimBox());
        boxes.put("Rect", page.getRect());

        for (Map.Entry<String, Rectangle> entry : boxes.entrySet()) {
            Rectangle box = entry.getValue();
            System.out.println(entry.getKey() + " : Height=" + box.getHeight()
                    + ",Width=" + box.getWidth()
                    + ",LLX=" + box.getLLX()
                    + ",LLY=" + box.getLLY()
                    + ",URX=" + box.getURX()
                    + ",URY=" + box.getURY());
        }

        System.out.println("Page Number : " + page.getNumber());
        System.out.println("Rotate : " + page.getRotate());
    }
}
```

## احصل على نوع اللون لكل صفحة

استخدم هذا المثال عندما تحتاج إلى تحديد ما إذا كانت الصفحات بالأبيض والأسود، أو بتدرج الرمادي، أو RGB.

1. افتح ملف PDF المصدر [المستند](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. كرر كل الصفحات واقرأ كل صفحة [ColorType](https://reference.aspose.com/pdf/java/com.aspose.pdf/colortype/).
1. تحويل قيمة التعداد إلى نص قابل للقراءة وإخراج النتيجة.

```java
public static void getPageColorType(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        for (int pageNumber = 1; pageNumber <= document.getPages().size(); pageNumber++) {
            ColorType pageColorType = document.getPages().get_Item(pageNumber).getColorType();
            String colorDescription = switch (pageColorType) {
                case BlackAndWhite -> "Black and white";
                case Grayscale -> "Gray Scale";
                case Rgb -> "RGB";
                case Undefined -> "undefined";
            };
            System.out.println("Page # " + pageNumber + " is " + colorDescription + ".");
        }
    }
}
```
