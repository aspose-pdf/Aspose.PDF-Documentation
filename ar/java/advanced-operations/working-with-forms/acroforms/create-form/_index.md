---
title: إنشاء AcroForm - إنشاء PDF قابل للتعبئة في Java
linktitle: إنشاء AcroForm
type: docs
weight: 10
url: /ar/java/create-form/
description: إنشاء حقول AcroForm من الصفر في مستندات PDF باستخدام Aspose.PDF for Java.
lastmod: "2026-10-01"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: إنشاء حقول AcroForm تفاعلية في ملفات PDF باستخدام Java.
Abstract: توضح هذه المقالة كيفية إنشاء حقول AcroForm باستخدام Aspose.PDF for Java. وتشمل الشرح صناديق النص، والحقول النصية متعددة الودجات، وأزرار الراديو، وصناديق القوائم المنسدلة، ومربعات الاختيار، وصناديق القوائم، وحقول التوقيع، وحقول الباركود لنماذج PDF التفاعلية.
---
تتيح لك Aspose.PDF for Java إنشاء مجموعة واسعة من أنواع حقول AcroForm من الصفر.

## إنشاء حقل صندوق نص

استخدم هذا المثال عندما تحتاج إلى إضافة حقل إدخال نص أحادي السطر إلى نموذج PDF جديد.

1. إنشاء PDF جديد [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) وأضف صفحةً.
1. إنشاء [TextBoxField](https://reference.aspose.com/pdf/java/com.aspose.pdf/textboxfield/) مع مستطيل هدف وتكوين مظهره.
1. أضف الحقل إلى النموذج واحفظ المستند.

```java
public static void addTextBoxField(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();

        Rectangle rectangle = new Rectangle(10, 600, 110, 620, true);
        TextBoxField textBoxField = new TextBoxField(page, rectangle);
        textBoxField.setPartialName("textbox1");
        textBoxField.setValue("Text Box");
        textBoxField.setDefaultAppearance(new DefaultAppearance("Arial", 10, Color.getDarkBlue().toRgb()));

        Border border = new Border(textBoxField);
        border.setWidth(1);
        border.setStyle(BorderStyle.Dashed);
        border.setDash(new Dash(3, 3));
        textBoxField.setBorder(border);

        textBoxField.getCharacteristics().setBorder(Color.getRed());
        textBoxField.getCharacteristics().setBackground(Color.getYellow().toRgb());

        document.getForm().add(textBoxField, 1);
        document.save(outputFile.toString());
    }
}
```

## إنشاء حقل صندوق نص مع عدة عناصر

استخدم هذا المثال عندما يجب أن يظهر نفس قيمة حقل النص في عدة مواضع على الصفحة.

1. إنشاء PDF جديد [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) وأضف صفحةً.
1. حدد العديد من المستطيلات والمظاهر لعناصر واجهة الحقل.
1. إنشاء [TextBoxField](https://reference.aspose.com/pdf/java/com.aspose.pdf/textboxfield/), قم بتكوين كل أداة، واحفظ المستند.

```java
public static void addTextBoxFieldNt(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();

        Rectangle[] rects = {
                new Rectangle(10, 600, 110, 620, true),
                new Rectangle(10, 630, 110, 650, true),
                new Rectangle(10, 660, 110, 680, true)
        };

        DefaultAppearance[] defaultAppearances = {
                new DefaultAppearance("Arial", 10, Color.getDarkBlue().toRgb()),
                new DefaultAppearance("Helvetica", 12, Color.getDarkGreen().toRgb()),
                new DefaultAppearance(FontRepository.findFont("Calibri"), 14, Color.getDarkMagenta().toRgb())
        };

        TextBoxField textBoxField = new TextBoxField(page, rects);
        textBoxField.setPartialName("textbox1");
        textBoxField.setValue("Some text");

        int index = 0;
        for (WidgetAnnotation widget : textBoxField) {
            widget.setDefaultAppearance(defaultAppearances[index]);
            index++;
        }

        Border border = new Border(textBoxField);
        border.setWidth(1);
        border.setStyle(BorderStyle.Dashed);
        border.setDash(new Dash(3, 3));
        textBoxField.setBorder(border);

        textBoxField.getCharacteristics().setBorder(Color.getRed());
        textBoxField.getCharacteristics().setBackground(Color.getYellow().toRgb());

        document.getForm().add(textBoxField);
        document.save(outputFile.toString());
    }
}
```

## إنشاء حقل زر اختيار

استخدم هذا المثال عندما ينبغي للنموذج أن يتيح للمستخدم اختيار خيار واحد من مجموعة محددة مسبقًا.

1. إنشاء PDF جديد [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) وأضف صفحةً.
1. إنشاء [RadioButtonField](https://reference.aspose.com/pdf/java/com.aspose.pdf/radiobuttonfield/) وأضف الخيارات المطلوبة.
1. أضف الحقل إلى النموذج واحفظ ملف PDF.

```java
public static void addRadioButton(Path outputFile) {
    try (Document document = new Document()) {
        document.getPages().add();

        RadioButtonField radio = new RadioButtonField(document.getPages().get_Item(1));
        radio.addOption("Option 1", new Rectangle(100, 640, 120, 680, true));
        radio.addOption("Option 2", new Rectangle(140, 640, 160, 680, true));

        document.getForm().add(radio);
        document.save(outputFile.toString());
    }
}
```

## إنشاء حقل مربع تجميع

استخدم هذا المثال عندما يجب على المستخدم اختيار قيمة واحدة من قائمة منسدلة.

1. إنشاء PDF جديد [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) وأضف صفحةً.
1. إنشاء [ComboBoxField](https://reference.aspose.com/pdf/java/com.aspose.pdf/comboboxfield/) وأضف خياراته القابلة للتحديد.
1. حدد الاختيار الافتراضي واحفظ المستند.

```java
public static void addComboBox(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();

        ComboBoxField combo = new ComboBoxField(page, new Rectangle(100, 640, 150, 656, true));
        combo.addOption("Red");
        combo.addOption("Yellow");
        combo.addOption("Green");
        combo.addOption("Blue");
        combo.setSelected(3);

        document.getForm().add(combo);
        document.save(outputFile.toString());
    }
}
```

## إنشاء حقل مربع اختيار

استخدم هذا المثال عندما يحتاج النموذج إلى خيار صحيح أو خطأ مثل الموافقة أو اختيار الميزة.

1. إنشاء PDF جديد [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) وأضف صفحةً.
1. إنشاء [CheckboxField](https://reference.aspose.com/pdf/java/com.aspose.pdf/checkboxfield/) وتهيئة مظهره.
1. أضف مربع الاختيار إلى Form واحفظ ملف الإخراج.

```java
public static void addCheckboxFieldToPdf(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();

        CheckboxField checkbox = new CheckboxField(page, new Rectangle(50, 620, 100, 650, true));
        checkbox.getCharacteristics().setBackground(Color.getAqua().toRgb());
        checkbox.setStyle(BoxStyle.Circle);

        document.getForm().add(checkbox);
        document.save(outputFile.toString());
    }
}
```

## إنشاء حقل قائمة

استخدم هذا المثال عندما يجب أن يعرض النموذج اختيارات متعددة متاحة في قائمة مرئية.

1. إنشاء PDF جديد [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) وأضف صفحةً.
1. إنشاء [ListBoxField](https://reference.aspose.com/pdf/java/com.aspose.pdf/listboxfield/) وأضف الخيارات المتاحة.
1. أضف الحقل إلى النموذج واحفظ المستند.

```java
public static void addListBoxFieldToPdf(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();

        ListBoxField listBox = new ListBoxField(page, new Rectangle(50, 650, 100, 700, true));
        listBox.setPartialName("list");
        listBox.addOption("Red");
        listBox.addOption("Green");
        listBox.addOption("Blue");

        document.getForm().add(listBox);
        document.save(outputFile.toString());
    }
}
```

## إنشاء حقل توقيع

استخدم هذا المثال عندما يجب على المستند حجز مساحة مرئية للتوقيع الرقمي.

1. إنشاء PDF جديد [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) وأضف صفحةً.
1. إنشاء [SignatureField](https://reference.aspose.com/pdf/java/com.aspose.pdf/signaturefield/) في المستطيل المطلوب.
1. أضف الحقل إلى Form واحفظ PDF الناتج.

```java
public static void addSignatureField(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();

        SignatureField signatureField = new SignatureField(page, new Rectangle(100, 700, 200, 800, true));
        signatureField.setPartialName("Signature1");
        document.getForm().add(signatureField);
        document.save(outputFile.toString());
    }
}
```

## إنشاء حقل الباركود

استخدم هذا المثال عندما يجب أن يعرض النموذج بيانات قابلة للقراءة آليًا داخل حقل الباركود.

1. إنشاء PDF جديد [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) وأضف صفحةً.
1. إنشاء [BarcodeField](https://reference.aspose.com/pdf/java/com.aspose.pdf/barcodefield/) وأضف قيمة الباركود.
1. أضف الحقل إلى النموذج واحفظ المستند.

```java
public static void addBarcodeField(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();

        BarcodeField barcode = new BarcodeField(page, new Rectangle(100, 700, 200, 740, true));
        barcode.setPartialName("Barcode1");
        barcode.addBarcode("1234567890");
        document.getForm().add(barcode);
        document.save(outputFile.toString());
    }
}
```
