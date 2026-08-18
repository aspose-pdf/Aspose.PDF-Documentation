---
title: إنشاء AcroForm - إنشاء ملف PDF قابل للتعبئة في Java
linktitle: إنشاء أكروفورم
type: docs
weight: 10
url: /java/create-form/
description: قم بإنشاء حقول AcroForm من البداية في مستندات PDF باستخدام Aspose.PDF لـ Java.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: قم بإنشاء حقول AcroForm تفاعلية في ملفات PDF باستخدام Java
Abstract: تشرح هذه المقالة كيفية إنشاء حقول AcroForm باستخدام Aspose.PDF لـ Java. وهو يغطي مربعات النص، وحقول النص متعددة الأدوات، وأزرار الاختيار، ومربعات التحرير والسرد، ومربعات الاختيار، ومربعات القائمة، وحقول التوقيع، وحقول الباركود لنماذج PDF التفاعلية.
---
يتيح لك Aspose.PDF for Java إنشاء مجموعة واسعة من أنواع حقول AcroForm من البداية.

## إنشاء حقل مربع نص

استخدم هذا المثال عندما تحتاج إلى إضافة حقل إدخال نص من سطر واحد إلى نموذج PDF جديد.

1. قم بإنشاء ملف PDF جديد [مستند](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) وأضف صفحة.
1. قم بإنشاء [TextBoxField](https://reference.aspose.com/pdf/java/com.aspose.pdf/textboxfield/) بمستطيل مستهدف وقم بتكوين مظهره.
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

## قم بإنشاء حقل مربع نص يحتوي على عناصر واجهة مستخدم متعددة

استخدم هذا المثال عندما تظهر نفس قيمة حقل النص في عدة مواضع بالصفحة.

1. قم بإنشاء ملف PDF جديد [مستند](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) وأضف صفحة.
1. حدد مستطيلات ومظاهر متعددة لعناصر واجهة المستخدم الميدانية.
1. قم بإنشاء [TextBoxField](https://reference.aspose.com/pdf/java/com.aspose.pdf/textboxfield/)، وقم بتكوين كل عنصر واجهة مستخدم، واحفظ المستند.

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

## قم بإنشاء حقل زر الاختيار

استخدم هذا المثال عندما يسمح النموذج للمستخدم باختيار خيار واحد من مجموعة محددة مسبقًا.

1. قم بإنشاء ملف PDF جديد [مستند](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) وأضف صفحة.
1. أنشئ [RadioButtonField](https://reference.aspose.com/pdf/java/com.aspose.pdf/radiobuttonfield/) وأضف الخيارات المطلوبة.
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

## إنشاء حقل مربع التحرير والسرد

استخدم هذا المثال عندما يتعين على المستخدم اختيار قيمة واحدة من القائمة المنسدلة.

1. قم بإنشاء ملف PDF جديد [مستند](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) وأضف صفحة.
1. أنشئ [ComboBoxField](https://reference.aspose.com/pdf/java/com.aspose.pdf/comboboxfield/) وأضف خياراته القابلة للتحديد.
1. قم بتعيين التحديد الافتراضي واحفظ المستند.

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

## قم بإنشاء حقل خانة اختيار

استخدم هذا المثال عندما يحتاج النموذج إلى خيار صواب أو خطأ مثل الموافقة أو تحديد الميزة.

1. قم بإنشاء ملف PDF جديد [مستند](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) وأضف صفحة.
1. قم بإنشاء [CheckboxField](https://reference.aspose.com/pdf/java/com.aspose.pdf/checkboxfield/) وقم بتكوين مظهره.
1. أضف خانة الاختيار إلى النموذج واحفظ ملف الإخراج.

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

## إنشاء حقل مربع قائمة

استخدم هذا المثال عندما يجب أن يعرض النموذج اختيارات متعددة متاحة في قائمة مرئية.

1. قم بإنشاء ملف PDF جديد [مستند](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) وأضف صفحة.
1. أنشئ [ListBoxField](https://reference.aspose.com/pdf/java/com.aspose.pdf/listboxfield/) وأضف الخيارات المتاحة.
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

## إنشاء حقل التوقيع

استخدم هذا المثال عندما يتعين على المستند حجز منطقة مرئية للتوقيع الرقمي.

1. قم بإنشاء ملف PDF جديد [مستند](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) وأضف صفحة.
1. قم بإنشاء [SignatureField](https://reference.aspose.com/pdf/java/com.aspose.pdf/signaturefield/) في المستطيل المطلوب.
1. أضف الحقل إلى النموذج واحفظ ملف PDF الناتج.

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

استخدم هذا المثال عندما يجب أن يعرض النموذج بيانات يمكن قراءتها آليًا داخل حقل الرمز الشريطي.

1. قم بإنشاء ملف PDF جديد [مستند](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) وأضف صفحة.
1. أنشئ [BarcodeField](https://reference.aspose.com/pdf/java/com.aspose.pdf/barcodefield/) وأضف قيمة الرمز الشريطي.
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
