---
title: العمل مع إجراءات PDF في Java
linktitle: الإجراءات
type: docs
weight: 20
url: /java/actions/
description: تعرف على كيفية إضافة إجراءات المستندات والصفحات والنماذج وتحديثها وإزالتها في ملفات PDF باستخدام Java.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.5
TechArticle: true
AlternativeHeadline: قم بإضافة إجراءات المستندات والصفحات والنماذج إلى ملفات PDF في Java
Abstract: تشرح هذه المقالة كيفية التعامل مع الإجراءات في مستندات PDF باستخدام Aspose.PDF لـ Java. ويغطي الإجراءات المسماة للطباعة والتنقل في الصفحة، وإخفاء حقول النموذج، وإرسال النماذج، وتعيين إجراءات تشغيل JavaScript، وإضافة أو إزالة إجراءات فتح وإغلاق الصفحة.
---
يتيح لك Aspose.PDF for Java تعيين إجراءات للأزرار والمستندات والصفحات لجعل ملفات PDF تفاعلية.

## أضف إجراء طباعة مسمى

استخدم هذا المثال عندما يؤدي زر موجود على الصفحة إلى تشغيل أمر الطباعة.

1. افتح ملف PDF المصدر [المستند](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) وحدد الصفحة المستهدفة.
1. قم بإنشاء [ButtonField](https://reference.aspose.com/pdf/java/com.aspose.pdf/buttonfield/) وقم بتعيين [NamedAction](https://reference.aspose.com/pdf/java/com.aspose.pdf/namedaction/) للطباعة.
1. أضف الزر إلى النموذج واحفظ المستند.

```java
public static void addNamedActionPrint(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        Page page = document.getPages().get_Item(1);

        Rectangle rect = new Rectangle(10, 10, 100, 40, true);
        ButtonField printButton = new ButtonField(page, rect);
        printButton.setPartialName("printButton");
        printButton.setValue("Print");
        printButton.getAnnotationActions().setOnReleaseMouseBtn(
                new NamedAction(PredefinedAction.File_Print));

        Border border = new Border(printButton);
        border.setWidth(1);
        printButton.setBorder(border);

        document.getForm().add(printButton, 1);
        document.save(outputFile.toString());
    }
}
```

## إضافة إجراء إخفاء

استخدم هذا المثال عندما يجب أن يُظهر الزر أو يخفي مجموعة من حقول النموذج، مثل خانات الاختيار.

1. افتح ملف PDF المصدر [المستند](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) واجمع عناصر واجهة المستخدم للنموذج المستهدف.
1. قم بإنشاء زر وقم بتعيين [HideAction](https://reference.aspose.com/pdf/java/com.aspose.pdf/hideaction/) إليه.
1. أضف الزر إلى النموذج واحفظ المستند المحدث.

```java
public static void addNamedActionHide(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        List<WidgetAnnotation> checkboxes = new ArrayList<>();
        for (WidgetAnnotation field : document.getForm()) {
            if (field instanceof CheckboxField) {
                checkboxes.add(field);
            }
        }

        Rectangle rect = new Rectangle(10, 410, 140, 440, true);
        ButtonField hideButton = new ButtonField(document.getPages().get_Item(1), rect);
        hideButton.setPartialName("HideButton");
        hideButton.setValue("Hide Checkboxes");
        hideButton.getAnnotationActions().setOnReleaseMouseBtn(
                new HideAction(checkboxes.toArray(new WidgetAnnotation[0]), true));

        document.getForm().add(hideButton, 1);
        document.save(outputFile.toString());
    }
}
```

## إضافة أزرار التنقل للصفحة

يقوم هذا المثال بإنشاء أزرار الصفحة الأولى والسابقة والتالية والأخيرة عبر المستند.

1. افتح ملف PDF المصدر [المستند](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. أنشئ أزرار تنقل لكل صفحة وقم بتعيين الإجراء المطابق المحدد مسبقًا.
1. أضف الأزرار إلى النموذج واحفظ المستند.

```java
public static void addNavigationButtons(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        int totalPages = document.getPages().size();

        for (Page page : document.getPages()) {
            ButtonField firstPageButton = new ButtonField(page, new Rectangle(10, 10, 110, 40, true));
            firstPageButton.setPartialName("First Page");
            firstPageButton.setValue("First Page");
            firstPageButton.getCharacteristics().setBorder(com.aspose.pdf.Color.getRed());
            firstPageButton.getCharacteristics().setBackground(com.aspose.pdf.Color.getOrange().toRgb());
            firstPageButton.setReadOnly(document.getPages().indexOf(page) == 1);
            firstPageButton.getAnnotationActions().setOnReleaseMouseBtn(
                    new NamedAction(PredefinedAction.FirstPage));
            document.getForm().add(firstPageButton);

            ButtonField previousPageButton = new ButtonField(page, new Rectangle(120, 10, 220, 40, true));
            previousPageButton.setPartialName("Previous Page");
            previousPageButton.setValue("Previous Page");
            previousPageButton.getCharacteristics().setBorder(com.aspose.pdf.Color.getRed());
            previousPageButton.getCharacteristics().setBackground(com.aspose.pdf.Color.getOrange().toRgb());
            previousPageButton.setReadOnly(document.getPages().indexOf(page) == 1);
            previousPageButton.getAnnotationActions().setOnReleaseMouseBtn(
                    new NamedAction(PredefinedAction.PrevPage));
            document.getForm().add(previousPageButton);

            ButtonField nextPageButton = new ButtonField(page, new Rectangle(230, 10, 330, 40, true));
            nextPageButton.setPartialName("Next Page");
            nextPageButton.setValue("Next Page");
            nextPageButton.getCharacteristics().setBorder(com.aspose.pdf.Color.getRed());
            nextPageButton.getCharacteristics().setBackground(com.aspose.pdf.Color.getOrange().toRgb());
            nextPageButton.setReadOnly(document.getPages().indexOf(page) == totalPages);
            nextPageButton.getAnnotationActions().setOnReleaseMouseBtn(
                    new NamedAction(PredefinedAction.NextPage));
            document.getForm().add(nextPageButton);

            ButtonField lastPageButton = new ButtonField(page, new Rectangle(340, 10, 440, 40, true));
            lastPageButton.setPartialName("Last Page");
            lastPageButton.setValue("Last Page");
            lastPageButton.getCharacteristics().setBorder(com.aspose.pdf.Color.getRed());
            lastPageButton.getCharacteristics().setBackground(com.aspose.pdf.Color.getOrange().toRgb());
            lastPageButton.setReadOnly(document.getPages().indexOf(page) == totalPages);
            lastPageButton.getAnnotationActions().setOnReleaseMouseBtn(
                    new NamedAction(PredefinedAction.LastPage));
            document.getForm().add(lastPageButton);
        }

        document.save(outputFile.toString());
    }
}
```

## أضف إجراء إرسال

استخدم هذا المثال عندما يجب على الزر إرسال بيانات النموذج إلى عنوان URL.

1. افتح ملف PDF المصدر [المستند](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. قم بإنشاء [SubmitFormAction](https://reference.aspose.com/pdf/java/com.aspose.pdf/submitformaction/) باستخدام عنوان URL المستهدف والإشارات.
1. قم بتعيين الإجراء إلى حقل زر واحفظ المستند.

```java
public static void addSubmitAction(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        SubmitFormAction submitAction = new SubmitFormAction();
        FileSpecification submitUrl = new FileSpecification();
        submitUrl.setFileSystem("URL");
        submitUrl.setName("http://localhost:3000/submit");
        submitAction.setUrl(submitUrl);
        submitAction.setFlags(SubmitFormAction.EXPORT_FORMAT | SubmitFormAction.SUBMIT_COORDINATES);

        Rectangle rect = new Rectangle(10, 10, 100, 40, true);
        ButtonField submitButton = new ButtonField(document.getPages().get_Item(1), rect);
        submitButton.setPartialName("SubmitButton");
        submitButton.setValue("Submit");
        submitButton.getAnnotationActions().setOnReleaseMouseBtn(submitAction);

        document.getForm().add(submitButton, 1);
        document.save(outputFile.toString());
    }
}
```

## أضف إجراءات الإطلاق على مستوى المستند

يقوم هذا المثال بتعيين إجراءات JavaScript التي يتم تشغيلها عند فتح المستند أو حفظه أو طباعته.

1. افتح ملف PDF المصدر [المستند](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. قم بإنشاء كائنات [JavascriptAction](https://reference.aspose.com/pdf/java/com.aspose.pdf/javascriptaction/) المطلوبة لأحداث المستند.
1. قم بتعيين الإجراءات وحفظ المستند.

```java
public static void addLaunchActions(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        document.setOpenAction(new JavascriptAction("app.launchURL('http://localhost:3000/open');"));
        document.getActions().setBeforeSaving(
                new JavascriptAction("app.launchURL('http://localhost:3000/save');"));
        document.getActions().setBeforePrinting(
                new JavascriptAction("app.launchURL('http://localhost:3000/print');"));

        document.save(outputFile.toString());
    }
}
```

## إضافة إجراءات فتح وإغلاق الصفحة

استخدم هذا المثال عندما يجب أن تؤدي صفحة معينة إلى تشغيل إجراءات عند الفتح والإغلاق.

1. افتح ملف PDF المصدر [المستند](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) وتأكد من وجود الصفحة المستهدفة.
1. قم بإنشاء التنقل في الصفحة وإجراءات JavaScript.
1. قم بتعيين إجراءات الصفحة وحفظ المستند.

```java
public static void addPageActions(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        if (document.getPages().size() < 3) {
            System.out.println("Error: The document does not have at least 3 pages.");
            return;
        }

        Page page = document.getPages().get_Item(3);
        GoToAction action = new GoToAction(page);
        action.setDestination(new XYZExplicitDestination(page, 0, page.getPageInfo().getHeight(), 1));
        page.getActions().setOnOpen(action);
        page.getActions().setOnClose(
                new JavascriptAction("app.launchURL('http://localhost:3000/page/3');"));

        document.save(outputFile.toString());
    }
}
```

## إزالة إجراءات الصفحة

استخدم هذا الأسلوب عندما يجب مسح إجراءات الفتح والإغلاق المعينة مسبقًا من الصفحة.

1. افتح ملف PDF المصدر [المستند](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) وتأكد من وجود الصفحة المستهدفة.
1. قم بإزالة جميع الإجراءات من تلك الصفحة.
1. احفظ المستند المحدث.

```java
public static void removePageActions(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        if (document.getPages().size() < 3) {
            System.out.println("Error: The document does not have at least 3 pages.");
            return;
        }

        Page page = document.getPages().get_Item(3);
        page.getActions().removeActions();

        document.save(outputFile.toString());
    }
}
```
