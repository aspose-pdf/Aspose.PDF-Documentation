---
title: استخدام FloatingBox لتخطيط PDF في Java
linktitle: استخدام FloatingBox
type: docs
weight: 30
url: /ar/java/floating-box/
description: تعلم كيفية استخدام FloatingBox لتنسيق النص، المحتوى متعدد الأعمدة، وتحديد المواقع بدقة في مستندات PDF باستخدام Java.
lastmod: "2026-10-05"
sitemap:
    changefreq: "monthly"
    priority: 0.5
TechArticle: true
AlternativeHeadline: إنشاء وتحديد موضع حاويات FloatingBox المُنسقة في PDF باستخدام Java
Abstract: توضح هذه المقالة طريقة استخدام FloatingBox في Aspose.PDF for Java. تغطي وضع النص في حاويات عائمة ذات حدود، إنشاء تخطيطات متعددة الأعمدة متكررة، استخدام ألوان الخلفية، الإزاحات المطلقة، وخيارات المحاذاة الأفقية أو العمودية.
---
يستخدم Aspose.PDF for Java `FloatingBox` لبناء حاويات نصية قابلة لإعادة الاستخدام وتخطيطات تعتمد على الأعمدة.

## إنشاء وإضافة مربع عائم

استخدم هذا المثال عندما يجب وضع النص داخل حاوية عائمة ذات إطار.

1. أنشئ مستند PDF جديد وأضف صفحة.
1. أنشئ `FloatingBox`، ضبط حجمه وحدوده، وأضف محتوى النص.
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

## إنشاء تخطيط متعدد الأعمدة متكرر

استخدم هذا المثال عندما يجب أن يتدفق النص الطويل عبر أعمدة متعددة داخل صندوق عائم واحد.

1. أنشئ صفحة واضبط الهوامش.
1. احسب عرض الأعمدة وقم بتكوين `FloatingBox` إعدادات العمود.
1. أضف مقاطع نصية مكررة إلى الصندوق واحفظ المستند.

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

## ابدأ كل جزء كأول عنصر في عمود

استخدم هذا المثال عندما يجب أن يبدأ كل جزء مُدرج قطاع تدفق عمود جديد.

1. أنشئ صفحة واضبط الأعمدة المتعددة `FloatingBox`.
1. أنشئ مقاطع نصية ووضع علامة عليها بـ `setFirstParagraphInColumn(true)`.
1. أضف الصندوق إلى الصفحة واحفظ ملف PDF..

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

## إضافة صندوق عائم مع لون الخلفية

استخدم هذا المثال عندما يجب أن تحتوي الحاوية العائمة على تعبئة خلفية مرئية.

1. أنشئ مستند PDF جديد وأضف صفحة.
1. أنشئ `FloatingBox`، اضبط لون الخلفية، وأضف نصًا.
1. ضع الصندوق على الصفحة واحفظ المستند.

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

## وضع صندوق عائم باستخدام إزاحات مطلقة

استخدم هذا المثال عندما يجب أن يظهر الصندوق العائم على إزاحة دقيقة في الصفحة.

1. أنشئ صفحة وحضّر المحتوى النصي المحيط.
1. أنشئ `FloatingBox`، اضبط وضعاً مطلقاً، وعيّن إزاحات العلو واليسار.
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

## محاذاة النص داخل الصناديق العائمة

استخدم هذا المثال عندما تحتاج الصناديق العائمة إلى إظهار محاذاة رأسية مختلفة مع نفس المحاذاة الأفقية.

1. أنشئ مستند PDF جديد وأضف صفحة.
1. أنشئ متعدد كائنات `FloatingBox` بإعدادات محاذاة مختلفة.
1. أضفهم إلى الصفحة واحفظ النتيجة.

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
