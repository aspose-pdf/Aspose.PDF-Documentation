---
title: إنشاء AcroForms - إنشاء ملفات PDF قابلة للتعبئة في Java
linktitle: إنشاء AcroForms
type: docs
weight: 10
url: /java/create-forms/
description: يشرح هذا القسم كيفية إنشاء AcroForms من الصفر في مستندات PDF الخاصة بك باستخدام Aspose.PDF for Java.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## إضافة حقل نموذج في مستند PDF

توفر فئة [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) مجموعة تُسمى Form والتي تساعد في إدارة حقول النموذج في مستند PDF.

لإضافة حقل نموذج:

1. قم بإنشاء حقل النموذج الذي تريد إضافته.
2. استدعِ طريقة الإضافة في مجموعة [Form](https://reference.aspose.com/pdf/java/com.aspose.pdf/Form).

يوضح هذا المثال كيفية إضافة TextBoxField. يمكنك إضافة أي حقل نموذج باستخدام نفس النهج:

1. أولاً، قم بإنشاء كائن الحقل وقم بتعيين خصائصه.
2. ثم، أضف الحقل إلى مجموعة Form.

### إضافة TextBoxField

حقل النص هو عنصر نموذج يسمح للمستلم بإدخال نص في النموذج الخاص بك.
 سيتم استخدام هذا في أي وقت تريد فيه السماح للمستخدم بحرية كتابة ما يريد.

تظهر مقتطفات الشيفرة التالية كيفية إضافة حقل TextBoxField إلى مستند PDF.

```java
public class ExamplesCreateForm {

    private static String _dataDir = "/home/aspose/pdf-examples/Samples/Forms/";

    public static void AddingTextBoxField() {

        // فتح المستند
        Document pdfDocument = new Document(_dataDir + "TextField.pdf");
        Page page = pdfDocument.getPages().get_Item(1);
        // إنشاء حقل
        TextBoxField textBoxField = new TextBoxField(page, new Rectangle(100, 200, 300, 300));
        textBoxField.setPartialName("textbox1");
        textBoxField.setValue("مربع النص");

        // TextBoxField.Border = new Border(
        Border border = new Border(textBoxField);
        border.setWidth(5);
        border.setDash(new Dash(1, 1));
        textBoxField.setBorder(border);

        textBoxField.setColor(Color.getGreen());

        // إضافة الحقل إلى المستند
        pdfDocument.getForm().add(textBoxField, 1);

        // حفظ ملف PDF المعدل
        pdfDocument.save(_dataDir + "TextBox_out.pdf");

    }
```

## إضافة RadioButtonField

يُستخدم زر الاختيار بشكل شائع في أسئلة الاختيار من متعدد، في السيناريو الذي يمكن فيه اختيار إجابة واحدة فقط.

توضح مقتطفات الشيفرة التالية كيفية إضافة [RadioButtonField](https://reference.aspose.com/pdf/java/com.aspose.pdf/RadioButtonField) في مستند PDF.

```java
public static void AddingRadioButton() {
        Document pdfDocument = new Document();
        // إضافة صفحة إلى ملف PDF
        pdfDocument.getPages().add();

        // إنشاء كائن RadioButtonField مع رقم الصفحة كوسيطة
        RadioButtonField radio = new RadioButtonField(pdfDocument.getPages().get_Item(1));

        // إضافة الخيار الأول لزر الاختيار وتحديد موقعه باستخدام كائن Rectangle
        radio.addOption("Test", new Rectangle(20, 720, 40, 740));
        // إضافة الخيار الثاني لزر الاختيار
        radio.addOption("Test1", new Rectangle(120, 720, 140, 740));
        // إضافة زر الاختيار إلى كائن النموذج في كائن المستند
        pdfDocument.getForm().add(radio);
        // حفظ ملف PDF
        pdfDocument.save("RadioButtonSample.pdf");

    }
```


يعرض مقطع الشيفرة التالي الخطوات المطلوبة لإضافة [RadioButtonField](https://reference.aspose.com/pdf/java/com.aspose.pdf/RadioButtonField) مع ثلاثة خيارات ووضعها داخل خلايا الجدول.

```java
public static void AddingRadioButtonAdvanced() {
        Document doc = new Document();
        Page page = doc.getPages().add();
        Table table = new Table();
        table.setColumnWidths("120 120 120");
        page.getParagraphs().add(table);
        Row r1 = table.getRows().add();
        Cell c1 = r1.getCells().add();
        Cell c2 = r1.getCells().add();
        Cell c3 = r1.getCells().add();

        RadioButtonField rf = new RadioButtonField(page);
        rf.setPartialName("radio");
        doc.getForm().add(rf, 1);

        RadioButtonOptionField opt1 = new RadioButtonOptionField();
        RadioButtonOptionField opt2 = new RadioButtonOptionField();
        RadioButtonOptionField opt3 = new RadioButtonOptionField();

        opt1.setOptionName("Item1");
        opt2.setOptionName("Item2");
        opt3.setOptionName("Item3");

        opt1.setWidth(15);
        opt1.setHeight(15);
        opt2.setWidth(15);
        opt2.setHeight(15);
        opt3.setWidth(15);
        opt3.setHeight(15);

        rf.add(opt1);
        rf.add(opt2);
        rf.add(opt3);

        opt1.setBorder(new Border(opt1));
        opt1.getBorder().setWidth(1);
        opt1.getBorder().setStyle(BorderStyle.Solid);
        opt1.getCharacteristics().setBorder(Color.getBlack());
        opt1.getDefaultAppearance().setTextColor(java.awt.Color.RED);
        opt1.setCaption(new TextFragment("Item1"));
        opt2.setBorder(new Border(opt2));
        opt2.getBorder().setWidth(1);
        opt2.getBorder().setStyle(BorderStyle.Solid);
        opt2.getCharacteristics().setBorder(java.awt.Color.BLACK);
        opt2.getDefaultAppearance().setTextColor(java.awt.Color.RED);
        opt2.setCaption(new TextFragment("Item2"));
        opt3.setBorder(new Border(opt3));
        opt3.getBorder().setWidth(1);
        opt3.getBorder().setStyle(BorderStyle.Solid);
        opt3.getCharacteristics().setBorder(java.awt.Color.BLACK);
        opt3.getDefaultAppearance().setTextColor(java.awt.Color.RED);
        opt3.setCaption(new TextFragment("Item3"));
        c1.getParagraphs().add(opt1);
        c2.getParagraphs().add(opt2);
        c3.getParagraphs().add(opt3);

        doc.save("RadioButtonField.pdf");
    }
```


## إضافة تسمية إلى RadioButtonField

يوضح مقتطف الشيفرة التالي كيفية إضافة تسمية مرتبطة بـ [RadioButtonField](https://reference.aspose.com/pdf/java/com.aspose.pdf/RadioButtonField):

```java
public static void AddingCaptionToRadioButtonField() {
        // تحميل نموذج PDF المصدر
        com.aspose.pdf.facades.Form form1 = new com.aspose.pdf.facades.Form(_dataDir + "RadioButtonField.pdf");
        Document document = new Document(_dataDir + "RadioButtonField.pdf");
        for (String item : form1.getFieldNames()) {
            System.out.println(item.toString());
            if (item.contains("radio1")) {
                RadioButtonField field0 = (RadioButtonField) document.getForm().get(item);
                RadioButtonOptionField fieldoption = new RadioButtonOptionField();
                fieldoption.setOptionName("Yes");
                fieldoption.setPartialName("Yesname");

                var updatedFragment = new TextFragment("test123");
                updatedFragment.getTextState().setFont(FontRepository.findFont("Arial"));
                updatedFragment.getTextState().setFontSize(10);
                updatedFragment.getTextState().setLineSpacing(6.32f);

                // إنشاء كائن TextParagraph
                TextParagraph par = new TextParagraph();

                // تحديد موضع الفقرة
                par.setPosition(new Position(field0.getRect().getLLX(),
                        field0.getRect().getLLY() + updatedFragment.getTextState().getFontSize()));
                // تحديد وضع التفاف الكلمات
                par.getFormattingOptions().setWrapMode(TextFormattingOptions.WordWrapMode.ByWords);

                // إضافة TextFragment جديد إلى الفقرة
                par.appendLine(updatedFragment);

                // إضافة TextParagraph باستخدام TextBuilder
                TextBuilder textBuilder = new TextBuilder(document.getPages().get_Item(1));
                textBuilder.appendParagraph(par);

                field0.deleteOption("item1");
            }
        }
        document.save(_dataDir + "RadioButtonField_out.pdf");

    }
```


## إضافة حقل ComboBox

Combo Box هو حقل نموذج يضيف قائمة منسدلة إلى المستند الخاص بك.

توضح مقتطفات الشيفرة التالية كيفية إضافة حقل [ComboBox](https://reference.aspose.com/pdf/java/com.aspose.pdf/ComboBoxField) في مستند PDF.

```java
public static void AddingComboboxField() {
        // إنشاء كائن المستند
        Document doc = new Document();
        // إضافة صفحة إلى كائن المستند
        doc.getPages().add();
        // استدعاء كائن حقل ComboBox
        ComboBoxField combo = new ComboBoxField(doc.getPages().get_Item(1), new Rectangle(100, 600, 150, 616));
        // إضافة خيار إلى ComboBox
        combo.addOption("Red");
        combo.addOption("Yellow");
        combo.addOption("Green");
        combo.addOption("Blue");
        // إضافة كائن مربع التحرير والسرد إلى مجموعة حقول النموذج في كائن المستند
        doc.getForm().add(combo);
        // حفظ مستند PDF
        doc.save("ComboBox_Added.pdf");
    }
```

## إضافة تلميح إلى النموذج

توفر فئة المستند مجموعة تُسمى Form والتي تقوم بإدارة حقول النماذج في مستند PDF.
 لإضافة تلميح إلى حقل نموذج، استخدم فئة الحقل AlternateName. يستخدم Adobe Acrobat "الاسم البديل" كتلميح للحقل.

تُظهر مقتطفات الشيفرة التالية كيفية إضافة تلميح إلى حقل نموذج باستخدام Java.

```java
public static void AddTooltipToFormField() {
        // تحميل نموذج PDF المصدر
        Document doc = new Document(_dataDir + "AddTooltipToField.pdf");

        // الحصول على حقل
        TextBoxField textBoxField = (TextBoxField) doc.getForm().get("textbox1");

        // تعيين التلميح لحقل النص
        textBoxField.setAlternateName("تلميح صندوق النص");

        // حفظ المستند المعدل
        doc.save("output.pdf");
    }
```