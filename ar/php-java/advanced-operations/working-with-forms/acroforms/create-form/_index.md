---
title: إنشاء AcroForms - إنشاء PDF قابل للتعبئة في PHP
linktitle: إنشاء AcroForms
type: docs
weight: 10
url: ar/php-java/create-forms/
description: يوضح هذا القسم كيفية إنشاء AcroForms من البداية في مستندات PDF الخاصة بك مع Aspose.PDF لـ PHP عبر Java.
lastmod: "2024-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## إضافة حقل نموذج في مستند PDF

تقدم فئة [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) مجموعة تسمى Form والتي تساعد في إدارة حقول النماذج في مستند PDF.

لإضافة حقل نموذج:

1. قم بإنشاء حقل النموذج الذي تريد إضافته.
2. استدع طريقة الإضافة لمجموعة [Form](https://reference.aspose.com/pdf/java/com.aspose.pdf/Form).

يوضح هذا المثال كيفية إضافة TextBoxField. يمكنك إضافة أي حقل نموذج باستخدام نفس الطريقة:

1. أولاً، قم بإنشاء كائن الحقل واضبط خصائصه.
2. ثم، أضف الحقل إلى مجموعة Form.

### إضافة TextBoxField

حقل النص هو عنصر نموذج يسمح للمستلم بإدخال نص في النموذج الخاص بك.
 سيتم استخدام هذا في أي وقت تريد فيه السماح للمستخدم بحرية كتابة ما يريد.

توضح مقتطفات الكود التالية كيفية إضافة TextBoxField إلى مستند PDF.

```php

    // افتح المستند
    $colors = new Color();
    $document = new Document($inputFile);
    $page = $document->getPages()->get_Item(1);

    // إنشاء حقل
    $textBoxField = new TextBoxField($page, new Rectangle(110, 300, 310, 320));
    $textBoxField->setPartialName("textbox1");
    $textBoxField->setValue("بعض القيمة في مربع النص");

    $border = new Border($textBoxField);
    $border->setWidth(5);
    $border->setDash(new Dash(1, 1));
    $textBoxField->setBorder($border);
    $textBoxField->setColor($colors->getGreen());

    // إضافة الحقل إلى المستند
    $document->getForm()->add($textBoxField, 1);

    // احفظ ملف PDF المعدل
    $document->save($outputFile);
    $document->close();
```

## إضافة RadioButtonField

يتم استخدام زر الراديو بشكل شائع في أسئلة الاختيار من متعدد، في السيناريو الذي يمكن اختيار إجابة واحدة فقط فيه.
الشفرة التالية توضح كيفية إضافة [RadioButtonField](https://reference.aspose.com/pdf/java/com.aspose.pdf/RadioButtonField) في مستند PDF.

```php

    // فتح المستند
    $document = new Document($inputFile);

    // إضافة صفحة إلى ملف PDF
    $page = $document->getPages()->get_Item(1);

    // إنشاء كائن RadioButtonField مع رقم الصفحة كوسيط
    $radio = new RadioButtonField($page);

    // إضافة الخيار الأول لزر الراديو وتحديد أصله
    // باستخدام كائن Rectangle

    $radio->addOption("Test1", new Rectangle(20, 720, 40, 740));

    // إضافة الخيار الثاني لزر الراديو
    $radio->addOption("Test2", new Rectangle(120, 720, 140, 740));

    // إضافة زر الراديو إلى كائن النموذج في كائن المستند
    $document->getForm()->add($radio);

    // حفظ ملف PDF
    $document->save($outputFile);
    $document->close();
```

الشفرة التالية توضح الخطوات لإضافة [RadioButtonField](https://reference.aspose.com/pdf/java/com.aspose.pdf/RadioButtonField) بثلاث خيارات ووضعها داخل خلايا الجدول.

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
    $opt1->setCaption(new TextFragment("عنصر1"));

    $border2 = new Border($opt2);
    $opt3->setBorder($border2);
    $opt3->getBorder()->setWidth(1.0);
    $opt3->getBorder()->setStyle(BorderStyle::$Solid);
    $opt2->getCharacteristics()->setBorder($colors->getBlack());
    $opt2->getDefaultAppearance()->setTextColor($colors->getRed()->toRgb());
    $opt2->setCaption(new TextFragment("عنصر2"));

    $border3 = new Border($opt3);
    $opt3->setBorder($border3);
    $opt3->getBorder()->setWidth(1.0);
    $opt3->getBorder()->setStyle(BorderStyle::$Solid);
    $opt3->getCharacteristics()->setBorder($colors->getBlack());
    $opt3->getDefaultAppearance()->setTextColor($colors->getRed()->toRgb());
    $opt3->setCaption(new TextFragment("عنصر3"));

    $c1->getParagraphs()->add($opt1);
    $c2->getParagraphs()->add($opt2);
    $c3->getParagraphs()->add($opt3);

    $document->save($outputFile);
    $document->close();
```


## إضافة حقل ComboBox

Combo Box هو حقل نموذج سيضيف قائمة منسدلة إلى مستندك.

توضح مقتطفات الشيفرة التالية كيفية إضافة حقل [ComboBox](https://reference.aspose.com/pdf/java/com.aspose.pdf/ComboBoxField) في مستند PDF.

```php

        $document = new Document($inputFile);

        // إنشاء كائن حقل ComboBox
        $page = $document->getPages()->get_Item(1);
        $combo = new ComboBoxField($page, new Rectangle(100, 600, 150, 616));

        // إضافة خيار إلى ComboBox
        $combo->addOption("Red");
        $combo->addOption("Yellow");
        $combo->addOption("Green");
        $combo->addOption("Blue");

        // إضافة كائن combo box إلى مجموعة حقول النموذج لكائن المستند
        $document->getForm()->add($combo);

        // حفظ مستند PDF
        $document->save($outputFile);
        $document->close();
```

## إضافة تلميح إلى النموذج

توفر فئة Document مجموعة تُدعى Form التي تدير حقول النموذج في مستند PDF.
 لإضافة تلميح إلى حقل نموذج، استخدم فئة الحقل AlternateName. يستخدم Adobe Acrobat "الاسم البديل" كتلميح للحقل.

توضح مقتطفات الشيفرة التالية كيفية إضافة تلميح إلى حقل النموذج باستخدام PHP.

```php

    $document = new Document($inputFile);
    $textBoxField = $document->getForm()->get("textbox1");

    // تعيين التلميح لحقل النص
    $textBoxField->setAlternateName("تلميح مربع النص");

    // حفظ مستند PDF
    $document->save($outputFile);
    $document->close();
```