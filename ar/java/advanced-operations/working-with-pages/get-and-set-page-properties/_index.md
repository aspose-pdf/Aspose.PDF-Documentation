---
title: الحصول على وتعيين خصائص صفحة PDF في Java
linktitle: الحصول على وتعيين خصائص الصفحة
type: docs
weight: 90
url: /ar/java/get-and-set-page-properties/
description: تعلم كيفية فحص خصائص صفحة PDF مثل العدد، الصناديق، الدوران، ومعلومات اللون في Java.
lastmod: "2026-10-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: فحص عدد الصفحات، الصناديق، ونوع اللون في ملفات PDF باستخدام Java
Abstract: تشرح هذه المقالة كيفية فحص خصائص الصفحة باستخدام Aspose.PDF for Java. وتغطي قراءة عدد الصفحات، وإنشاء الفقرات والتحقق من العدد الناتج قبل الحفظ، وطباعة جميع قيم مربع الصفحة الرئيسية، وتحديد نوع لون كل صفحة.
---
يمكن لـ Aspose.PDF for Java فحص عدد الصفحات، ومربعات الصفحات، والدوران، ونوع لون الصفحة.

## احصل على عدد الصفحات

استخدم هذا المثال عندما تحتاج إلى قراءة العدد الكلي للصفحات في ملف PDF.

1. افتح ملف PDF المصدر [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. اقرأ حجم مجموعة الصفحات.
1. أخرج العدد الإجمالي للصفحات.

```java
public static void getPageCount(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        System.out.println("Page Count: " + document.getPages().size());
    }
}
```

## احصل على عدد الصفحات قبل الحفظ

استخدم هذا المثال عندما تحتاج إلى معرفة عدد الصفحات التي سيتولدها المحتوى قبل كتابة الملف.

1. أنشئ PDF جديد [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) وأضف محتوى إلى صفحة.
1. عالج الفقرات لإجبار حساب التخطيط.
1. اقرأ عدد الصفحات الناتج واطبعه.

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

## احصل على خصائص صندوق الصفحة

استخدم هذا المثال عندما تحتاج إلى فحص جميع أبعاد الصناديق الرئيسية وقيم دوران الصفحة.

1. افتح ملف PDF المصدر [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) والوصول إلى الصفحة المستهدفة.
1. اجمع قيم صناديق الصفحة في خريطة.
1. أخرج أبعاد الصفحة ومعلومات دورانها.

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

استخدم هذا المثال عندما تحتاج إلى تحديد ما إذا كانت الصفحات بالأبيض والأسود أو بالتدرج الرمادي أو RGB.

1. افتح ملف PDF المصدر [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. مرّ على جميع الصفحات واقرأ كل صفحة [ColorType](https://reference.aspose.com/pdf/java/com.aspose.pdf/colortype/).
1. حوّل قيمة التعداد إلى نص قابل للقراءة واطبع النتيجة.

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
