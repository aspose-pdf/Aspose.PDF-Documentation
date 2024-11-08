---
title: Создание AcroForms - Создание заполняемых PDF в PHP
linktitle: Создание AcroForms
type: docs
weight: 10
url: /ru/php-java/create-forms/
description: Этот раздел объясняет, как создать AcroForms с нуля в ваших PDF-документах с помощью Aspose.PDF для PHP через Java.
lastmod: "2024-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Добавление поля формы в PDF-документ

Класс [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) предоставляет коллекцию с именем Form, которая помогает управлять полями формы в PDF-документе.

Чтобы добавить поле формы:

1. Создайте поле формы, которое вы хотите добавить.
2. Вызовите метод add коллекции [Form](https://reference.aspose.com/pdf/java/com.aspose.pdf/Form).

Этот пример показывает, как добавить TextBoxField. Вы можете добавить любое поле формы, используя тот же подход:

1. Сначала создайте объект поля и установите его свойства.
2. Затем добавьте поле в коллекцию Form.

### Добавление TextBoxField

Текстовое поле - это элемент формы, который позволяет получателю вводить текст в вашу форму.
 Это будет использоваться в любое время, когда вы хотите предоставить пользователю свободу вводить то, что он хочет.

Следующие фрагменты кода показывают, как добавить TextBoxField в PDF документ.

```php

    // Открыть документ
    $colors = new Color();
    $document = new Document($inputFile);
    $page = $document->getPages()->get_Item(1);

    // Создать поле
    $textBoxField = new TextBoxField($page, new Rectangle(110, 300, 310, 320));
    $textBoxField->setPartialName("textbox1");
    $textBoxField->setValue("Некоторое значение в текстовом поле");

    $border = new Border($textBoxField);
    $border->setWidth(5);
    $border->setDash(new Dash(1, 1));
    $textBoxField->setBorder($border);
    $textBoxField->setColor($colors->getGreen());

    // Добавить поле в документ
    $document->getForm()->add($textBoxField, 1);

    // Сохранить измененный PDF
    $document->save($outputFile);
    $document->close();
```

## Добавление RadioButtonField

Радиокнопка чаще всего используется для вопросов с несколькими вариантами ответов, в ситуации, когда может быть выбран только один ответ.
Следующие фрагменты кода показывают, как добавить [RadioButtonField](https://reference.aspose.com/pdf/java/com.aspose.pdf/RadioButtonField) в PDF документ.

```php

    // Открыть документ
    $document = new Document($inputFile);

    // добавить страницу в PDF файл
    $page = $document->getPages()->get_Item(1);

    // создать объект RadioButtonField с номером страницы в качестве аргумента
    $radio = new RadioButtonField($page);

    // добавить первую опцию радио-кнопки и указать ее местоположение 
    // с использованием объекта Rectangle

    $radio->addOption("Test1", new Rectangle(20, 720, 40, 740));

    // добавить вторую опцию радио-кнопки
    $radio->addOption("Test2", new Rectangle(120, 720, 140, 740));

    // добавить радио-кнопку в объект формы объекта Document
    $document->getForm()->add($radio);

    // сохранить PDF файл
    $document->save($outputFile);
    $document->close();
```

Следующий фрагмент кода показывает шаги по добавлению [RadioButtonField](https://reference.aspose.com/pdf/java/com.aspose.pdf/RadioButtonField) с тремя опциями и размещению их внутри ячеек таблицы.

```php

    $colors = new Color();
    $document = new Document();
    $page = $document->getPages()->add();

    $table = new Table();
    $table->setColumnWidths("120 120 120");
    $page->getParagraphs()->add($table);
    $r1 = $table->getRows()->add();
    $c1 = $r1->getCells()->add();
    $c2 = $r1->getCells()->add();
    $c3 = $r1->getCells()->add();

    $rf = new RadioButtonField($page);
    $rf->setPartialName("radio1");
    $document->getForm()->add($rf, 1);

    $opt1 = new RadioButtonOptionField();
    $opt2 = new RadioButtonOptionField();
    $opt3 = new RadioButtonOptionField();

    $opt1->setOptionName("Item1");
    $opt2->setOptionName("Item2");
    $opt3->setOptionName("Item3");

    $opt1->setWidth(15.0);
    $opt1->setHeight(15.0);
    $opt2->setWidth(15.0);
    $opt2->setHeight(15.0);
    $opt3->setWidth(15.0);
    $opt3->setHeight(15.0);

    $rf->add($opt1);
    $rf->add($opt2);
    $rf->add($opt3);

    $border1 = new Border($opt1);
    $opt1->setBorder($border1);
    $opt1->getBorder()->setWidth(1.0);
    $opt1->getBorder()->setStyle(BorderStyle::$Solid);
    $opt1->getCharacteristics()->setBorder($colors->getBlack());
    $opt1->getDefaultAppearance()->setTextColor($colors->getRed()->toRgb());
    $opt1->setCaption(new TextFragment("Элемент1"));

    $border2 = new Border($opt2);
    $opt3->setBorder($border2);
    $opt3->getBorder()->setWidth(1.0);
    $opt3->getBorder()->setStyle(BorderStyle::$Solid);
    $opt2->getCharacteristics()->setBorder($colors->getBlack());
    $opt2->getDefaultAppearance()->setTextColor($colors->getRed()->toRgb());
    $opt2->setCaption(new TextFragment("Элемент2"));

    $border3 = new Border($opt3);
    $opt3->setBorder($border3);
    $opt3->getBorder()->setWidth(1.0);
    $opt3->getBorder()->setStyle(BorderStyle::$Solid);
    $opt3->getCharacteristics()->setBorder($colors->getBlack());
    $opt3->getDefaultAppearance()->setTextColor($colors->getRed()->toRgb());
    $opt3->setCaption(new TextFragment("Элемент3"));

    $c1->getParagraphs()->add($opt1);
    $c2->getParagraphs()->add($opt2);
    $c3->getParagraphs()->add($opt3);

    $document->save($outputFile);
    $document->close();
```


## Добавление поля ComboBox

Combo Box — это поле формы, которое добавит выпадающее меню в ваш документ.

Следующие фрагменты кода показывают, как добавить поле [ComboBox](https://reference.aspose.com/pdf/java/com.aspose.pdf/ComboBoxField) в PDF-документ.

```php

        $document = new Document($inputFile);

        // создать объект поля ComboBox
        $page = $document->getPages()->get_Item(1);
        $combo = new ComboBoxField($page, new Rectangle(100, 600, 150, 616));

        // добавить опцию в ComboBox
        $combo->addOption("Red");
        $combo->addOption("Yellow");
        $combo->addOption("Green");
        $combo->addOption("Blue");

        // добавить объект combo box в коллекцию полей формы объекта документа
        $document->getForm()->add($combo);

        // сохранить PDF-документ
        $document->save($outputFile);
        $document->close();
```

## Добавление подсказки к форме

Класс Document предоставляет коллекцию с именем Form, которая управляет полями формы в PDF-документе.
 Чтобы добавить всплывающую подсказку к полю формы, используйте класс Field AlternateName. Adobe Acrobat использует 'альтернативное имя' как всплывающую подсказку для поля.

Приведенные ниже фрагменты кода показывают, как добавить всплывающую подсказку к полю формы с помощью PHP.

```php

    $document = new Document($inputFile);
    $textBoxField = $document->getForm()->get("textbox1");

    // Установить всплывающую подсказку для текстового поля
    $textBoxField->setAlternateName("Подсказка для текстового поля");

    // сохранить PDF документ
    $document->save($outputFile);
    $document->close();
```