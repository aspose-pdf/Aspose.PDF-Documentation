---
title: Создание AcroForms - Создание заполняемых PDF в Java
linktitle: Создание AcroForms
type: docs
weight: 10
url: ru/java/create-forms/
description: Этот раздел объясняет, как с нуля создать AcroForms в ваших PDF-документах с помощью Aspose.PDF для Java.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Добавление поля формы в PDF-документ

Класс [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) предоставляет коллекцию под названием Form, которая помогает управлять полями формы в PDF-документе.

Чтобы добавить поле формы:

1. Создайте поле формы, которое вы хотите добавить.
2. Вызовите метод add коллекции [Form](https://reference.aspose.com/pdf/java/com.aspose.pdf/Form).

Этот пример показывает, как добавить TextBoxField. Вы можете добавить любое поле формы, используя тот же подход:

1. Сначала создайте объект поля и задайте его свойства.
2. Затем добавьте поле в коллекцию Form.

### Добавление TextBoxField

Текстовое поле - это элемент формы, который позволяет получателю ввести текст в вашу форму.
 Это будет использоваться всякий раз, когда вы хотите предоставить пользователю свободу вводить то, что он хочет.

Следующий фрагмент кода показывает, как добавить TextBoxField в PDF-документ.

```java
public class ExamplesCreateForm {

    private static String _dataDir = "/home/aspose/pdf-examples/Samples/Forms/";

    public static void AddingTextBoxField() {

        // Открыть документ
        Document pdfDocument = new Document(_dataDir + "TextField.pdf");
        Page page = pdfDocument.getPages().get_Item(1);
        // Создать поле
        TextBoxField textBoxField = new TextBoxField(page, new Rectangle(100, 200, 300, 300));
        textBoxField.setPartialName("textbox1");
        textBoxField.setValue("Текстовое поле");

        // TextBoxField.Border = new Border(
        Border border = new Border(textBoxField);
        border.setWidth(5);
        border.setDash(new Dash(1, 1));
        textBoxField.setBorder(border);

        textBoxField.setColor(Color.getGreen());

        // Добавить поле в документ
        pdfDocument.getForm().add(textBoxField, 1);

        // Сохранить измененный PDF
        pdfDocument.save(_dataDir + "TextBox_out.pdf");

    }
```

## Добавление RadioButtonField

Радиокнопка чаще всего используется для вопросов с множественным выбором, в ситуации, когда можно выбрать только один ответ.

Следующие фрагменты кода показывают, как добавить [RadioButtonField](https://reference.aspose.com/pdf/java/com.aspose.pdf/RadioButtonField) в PDF документ.

```java
public static void AddingRadioButton() {
        Document pdfDocument = new Document();
        // добавить страницу в PDF файл
        pdfDocument.getPages().add();

        // создать объект RadioButtonField с номером страницы в качестве аргумента
        RadioButtonField radio = new RadioButtonField(pdfDocument.getPages().get_Item(1));

        // добавить первый вариант радиокнопки и также указать его положение с использованием объекта Rectangle
        radio.addOption("Test", new Rectangle(20, 720, 40, 740));
        // добавить второй вариант радиокнопки
        radio.addOption("Test1", new Rectangle(120, 720, 140, 740));
        // добавить радиокнопку к объекту формы объекта Document
        pdfDocument.getForm().add(radio);
        // сохранить PDF файл
        pdfDocument.save("RadioButtonSample.pdf");

    }
```


Следующий фрагмент кода показывает шаги по добавлению [RadioButtonField](https://reference.aspose.com/pdf/java/com.aspose.pdf/RadioButtonField) с тремя опциями и размещению их внутри ячеек таблицы.

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


## Добавление подписи к RadioButtonField

Следующий фрагмент кода показывает, как добавить подпись, которая будет связана с [RadioButtonField](https://reference.aspose.com/pdf/java/com.aspose.pdf/RadioButtonField):

```java
public static void AddingCaptionToRadioButtonField() {
        // Загрузка исходного PDF формуляра
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

                // Создание объекта TextParagraph
                TextParagraph par = new TextParagraph();

                // Установка позиции параграфа
                par.setPosition(new Position(field0.getRect().getLLX(),
                        field0.getRect().getLLY() + updatedFragment.getTextState().getFontSize()));
                // Указание режима переноса слов
                par.getFormattingOptions().setWrapMode(TextFormattingOptions.WordWrapMode.ByWords);

                // Добавление нового TextFragment в параграф
                par.appendLine(updatedFragment);

                // Добавление TextParagraph с использованием TextBuilder
                TextBuilder textBuilder = new TextBuilder(document.getPages().get_Item(1));
                textBuilder.appendParagraph(par);

                field0.deleteOption("item1");
            }
        }
        document.save(_dataDir + "RadioButtonField_out.pdf");

    }
```


## Добавление поля ComboBox

ComboBox — это поле формы, которое добавит выпадающее меню в ваш документ.

Следующие фрагменты кода показывают, как добавить поле [ComboBox](https://reference.aspose.com/pdf/java/com.aspose.pdf/ComboBoxField) в PDF-документ.

```java
public static void AddingComboboxField() {
        // создать объект документа
        Document doc = new Document();
        // добавить страницу в объект документа
        doc.getPages().add();
        // создать объект поля ComboBox
        ComboBoxField combo = new ComboBoxField(doc.getPages().get_Item(1), new Rectangle(100, 600, 150, 616));
        // добавить опцию в ComboBox
        combo.addOption("Красный");
        combo.addOption("Желтый");
        combo.addOption("Зеленый");
        combo.addOption("Синий");
        // добавить объект combo box в коллекцию полей формы объекта документа
        doc.getForm().add(combo);
        // сохранить PDF-документ
        doc.save("ComboBox_Added.pdf");
    }
```

## Добавление подсказки к форме

Класс Document предоставляет коллекцию с именем Form, которая управляет полями формы в PDF-документе.
 Чтобы добавить всплывающую подсказку к полю формы, используйте класс Field AlternateName. Adobe Acrobat использует «альтернативное имя» как всплывающую подсказку для поля.

В приведенных ниже фрагментах кода показано, как добавить всплывающую подсказку к полю формы с помощью Java.

```java
public static void AddTooltipToFormField() {
        // Загрузить исходную PDF-форму
        Document doc = new Document(_dataDir + "AddTooltipToField.pdf");

        // Получить поле
        TextBoxField textBoxField = (TextBoxField) doc.getForm().get("textbox1");

        // Установить всплывающую подсказку для текстового поля
        textBoxField.setAlternateName("Подсказка для текстового поля");

        // Сохранить измененный документ
        doc.save("output.pdf");
    }
```