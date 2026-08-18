---
title: استخدم FloatingBox لتخطيط PDF في Java
linktitle: باستخدام FloatingBox
type: docs
weight: 30
url: /java/floating-box/
description: تعرف على كيفية استخدام FloatingBox لتخطيط النص والمحتوى متعدد الأعمدة وتحديد الموضع بدقة في مستندات PDF باستخدام Java.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.5
TechArticle: true
AlternativeHeadline: قم بإنشاء حاويات FloatingBox ووضعها في ملف PDF باستخدام Java
Abstract: تشرح هذه المقالة كيفية استخدام FloatingBox في Aspose.PDF لـ Java. ويغطي وضع النص في حاويات عائمة ذات حدود، وإنشاء تخطيطات متكررة متعددة الأعمدة، باستخدام ألوان الخلفية، والإزاحات المطلقة، وخيارات المحاذاة الأفقية أو الرأسية.
---
يستخدم Aspose.PDF لـ Java `FloatingBox` لإنشاء حاويات نصية قابلة لإعادة الاستخدام وتخطيطات قائمة على الأعمدة.

## إنشاء وإضافة مربع عائم

استخدم هذا المثال عندما يجب وضع النص داخل حاوية عائمة ذات حدود.

1. قم بإنشاء مستند PDF جديد وأضف صفحة.
1. قم بإنشاء `FloatingBox`، وقم بتعيين حجمه وحدوده، وأضف محتوى نصيًا.
1. أضف المربع إلى الصفحة واحفظ المستند.

```java
public static void createAndAddFloatingBox(Path outputFile) {
       try (Document document = new Document()) {
           Page page = document.getPages().add();

           FloatingBox box = new FloatingBox(400, 30);
           box.setBorder(new BorderInfo(BorderSide.All, 1.5f, Color.getDarkGreen()));
           box.setNeedRepeating(false);
           String phrase = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Fusce quam odio, sollicitudin ac mauris vel, suscipit pellentesque nisi.";
           box.getParagraphs().add(new TextFragment(phrase));

           page.getParagraphs().add(box);
           document.save(outputFile.toString());
       }
   }
```

## إنشاء تخطيط متكرر متعدد الأعمدة

استخدم هذا المثال عندما يجب أن يتدفق النص الطويل عبر أعمدة متعددة داخل مربع عائم واحد.

1. إنشاء صفحة وتكوين الهوامش.
1. احسب عرض الأعمدة وقم بتكوين إعدادات العمود `FloatingBox`.
1. أضف أجزاء النص المتكررة إلى المربع واحفظ المستند.

```java
public static void multiColumnLayout(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();
        page.getPageInfo().setMargin(new MarginInfo(36, 18, 36, 18));

        int columnCount = 3;
        int spacing = 10;
        double width = page.getPageInfo().getWidth()
                - page.getPageInfo().getMargin().getLeft()
                - page.getPageInfo().getMargin().getRight()
                - (columnCount - 1) * spacing;
        double columnWidth = width / 3;

        FloatingBox box = new FloatingBox();
        box.setNeedRepeating(true);
        box.getColumnInfo().setColumnWidths(columnWidth + " " + columnWidth + " " + columnWidth);
        box.getColumnInfo().setColumnSpacing(String.valueOf(spacing));
        box.getColumnInfo().setColumnCount(3);

        String phrase = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Fusce quam odio, sollicitudin ac mauris vel, suscipit pellentesque nisi.";
        for (int i = 0; i < 10; i++) {
            box.getParagraphs().add(new TextFragment(phrase));
        }

        page.getParagraphs().add(box);
        document.save(outputFile.toString());
    }
}
```

## ابدأ كل جزء كأول عنصر في العمود

استخدم هذا المثال عندما يبدأ كل جزء مدرج في مقطع تدفق عمود جديد.

1. قم بإنشاء صفحة وتكوين الأعمدة المتعددة `FloatingBox`.
1. قم بإنشاء أجزاء نصية وقم بتمييزها باستخدام `setFirstParagraphInColumn(true)`.
1. أضف المربع إلى الصفحة واحفظ ملف PDF.

```java
public static void multiColumnLayout2(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();
        page.getPageInfo().setMargin(new MarginInfo(36, 18, 36, 18));

        int columnCount = 3;
        int spacing = 10;
        double width = page.getPageInfo().getWidth()
                - page.getPageInfo().getMargin().getLeft()
                - page.getPageInfo().getMargin().getRight()
                - (columnCount - 1) * spacing;
        double columnWidth = width / 3;

        FloatingBox box = new FloatingBox();
        box.setNeedRepeating(true);
        box.getColumnInfo().setColumnWidths(columnWidth + " " + columnWidth + " " + columnWidth);
        box.getColumnInfo().setColumnSpacing(String.valueOf(spacing));
        box.getColumnInfo().setColumnCount(3);

        String phrase = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Fusce quam odio, sollicitudin ac mauris vel, suscipit pellentesque nisi.";
        for (int i = 0; i < 10; i++) {
            TextFragment text = new TextFragment(phrase);
            text.setFirstParagraphInColumn(true);
            box.getParagraphs().add(text);
        }

        page.getParagraphs().add(box);
        document.save(outputFile.toString());
    }
}
```

## أضف مربعًا عائمًا بلون الخلفية

استخدم هذا المثال عندما يجب أن تحتوي الحاوية العائمة على تعبئة خلفية مرئية.

1. قم بإنشاء مستند PDF جديد وأضف صفحة.
1. أنشئ `FloatingBox` وعيّن لون خلفيته وأضف نصًا.
1. ضع المربع على الصفحة واحفظ المستند.

```java
public static void backgroundSupport(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();

        FloatingBox box = new FloatingBox(400, 30);
        box.setBackgroundColor(Color.getLightGreen());
        box.setNeedRepeating(false);
        box.getParagraphs().add(new TextFragment("text example"));

        page.getParagraphs().add(box);
        document.save(outputFile.toString());
    }
}
```

## ضع مربعًا عائمًا بإزاحات مطلقة

استخدم هذا المثال عندما يجب أن يظهر المربع العائم بإزاحة دقيقة على الصفحة.

1. إنشاء صفحة وإعداد محتوى النص المحيط بها.
1. قم بإنشاء `FloatingBox`، وقم بتعيين الموضع المطلق، وقم بتعيين الإزاحات العلوية واليسرى.
1. أضف المحتوى إلى الصفحة واحفظ المستند.

```java
public static void offsetSupport(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();

        FloatingBox box = new FloatingBox(400, 30);
        box.setTop(45);
        box.setLeft(15);
        box.setPositioningMode(ParagraphPositioningMode.Absolute);
        box.setBorder(new BorderInfo(BorderSide.All, 1.5f, Color.getDarkGreen()));
        box.getParagraphs().add(new TextFragment("text example 1"));

        page.getParagraphs().add(new TextFragment("text example 2"));
        page.getParagraphs().add(box);
        page.getParagraphs().add(new TextFragment("text example 3"));

        document.save(outputFile.toString());
    }
}
```

## محاذاة النص داخل المربعات العائمة

استخدم هذا المثال عندما تظهر المربعات العائمة محاذاة رأسية مختلفة بنفس المحاذاة الأفقية.

1. قم بإنشاء مستند PDF جديد وأضف صفحة.
1. قم بإنشاء كائنات `FloatingBox` متعددة بإعدادات محاذاة مختلفة.
1. إضافتها إلى الصفحة وحفظ النتيجة.

```java
public static void alignTextToFloat(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();

        FloatingBox floatBox = new FloatingBox(100, 100);
        floatBox.setVerticalAlignment(VerticalAlignment.Bottom);
        floatBox.setHorizontalAlignment(HorizontalAlignment.Right);
        floatBox.getParagraphs().add(new TextFragment("FloatingBox_bottom"));
        floatBox.setBorder(new BorderInfo(BorderSide.All, Color.getBlue()));
        page.getParagraphs().add(floatBox);

        FloatingBox floatBox2 = new FloatingBox(100, 100);
        floatBox2.setVerticalAlignment(VerticalAlignment.Center);
        floatBox2.setHorizontalAlignment(HorizontalAlignment.Right);
        floatBox2.getParagraphs().add(new TextFragment("FloatingBox_center"));
        floatBox2.setBorder(new BorderInfo(BorderSide.All, Color.getBlue()));
        page.getParagraphs().add(floatBox2);

        FloatingBox floatBox3 = new FloatingBox(100, 100);
        floatBox3.setVerticalAlignment(VerticalAlignment.Top);
        floatBox3.setHorizontalAlignment(HorizontalAlignment.Right);
        floatBox3.getParagraphs().add(new TextFragment("FloatingBox_top"));
        floatBox3.setBorder(new BorderInfo(BorderSide.All, Color.getBlue()));
        page.getParagraphs().add(floatBox3);

        document.save(outputFile.toString());
    }
}
```
