---
title: 创建 AcroForms - 在 PHP 中创建可填写的 PDF
linktitle: 创建 AcroForms
type: docs
weight: 10
url: zh/php-java/create-forms/
description: 本节解释如何使用 Aspose.PDF for PHP via Java 从头开始在 PDF 文档中创建 AcroForms。
lastmod: "2024-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## 在 PDF 文档中添加表单字段

[Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) 类提供了一个名为 Form 的集合，用于帮助管理 PDF 文档中的表单字段。

要添加表单字段：

1. 创建要添加的表单字段。
2. 调用 [Form](https://reference.aspose.com/pdf/java/com.aspose.pdf/Form) 集合的 add 方法。

此示例展示了如何添加一个 TextBoxField。您可以使用相同的方法添加任何表单字段：

1. 首先，创建一个字段对象并设置其属性。
2. 然后，将字段添加到 Form 集合中。

### 添加 TextBoxField

文本字段是一个表单元素，允许接收者在您的表单中输入文本。
 这将用于任何时候你想允许用户自由输入他们想要的内容。

以下代码片段展示了如何向PDF文档添加一个TextBoxField。

```php

    // 打开文档
    $colors = new Color();
    $document = new Document($inputFile);
    $page = $document->getPages()->get_Item(1);

    // 创建一个字段
    $textBoxField = new TextBoxField($page, new Rectangle(110, 300, 310, 320));
    $textBoxField->setPartialName("textbox1");
    $textBoxField->setValue("Text Box中的某个值");

    $border = new Border($textBoxField);
    $border->setWidth(5);
    $border->setDash(new Dash(1, 1));
    $textBoxField->setBorder($border);
    $textBoxField->setColor($colors->getGreen());

    // 将字段添加到文档
    $document->getForm()->add($textBoxField, 1);

    // 保存修改后的PDF
    $document->save($outputFile);
    $document->close();
```

## 添加RadioButtonField

单选按钮最常用于选择题的场景，在这种情况下只能选择一个答案。
以下代码片段展示了如何在 PDF 文档中添加 [RadioButtonField](https://reference.aspose.com/pdf/java/com.aspose.pdf/RadioButtonField)。

```php

    // 打开文档            
    $document = new Document($inputFile);

    // 向 PDF 文件添加页面
    $page = $document->getPages()->get_Item(1);

    // 创建 RadioButtonField 对象，参数为页码
    $radio = new RadioButtonField($page);

    // 添加第一个单选按钮选项并指定其位置
    // 使用 Rectangle 对象

    $radio->addOption("Test1", new Rectangle(20, 720, 40, 740));

    // 添加第二个单选按钮选项
    $radio->addOption("Test2", new Rectangle(120, 720, 140, 740));

    // 将单选按钮添加到 Document 对象的表单对象中
    $document->getForm()->add($radio);

    // 保存 PDF 文件
    $document->save($outputFile);
    $document->close();
```

以下代码片段展示了添加具有三个选项的 [RadioButtonField](https://reference.aspose.com/pdf/java/com.aspose.pdf/RadioButtonField)并将其放置在表格单元格中的步骤。

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
    $opt1->setCaption(new TextFragment("项目1"));

    $border2 = new Border($opt2);
    $opt3->setBorder($border2);
    $opt3->getBorder()->setWidth(1.0);
    $opt3->getBorder()->setStyle(BorderStyle::$Solid);
    $opt2->getCharacteristics()->setBorder($colors->getBlack());
    $opt2->getDefaultAppearance()->setTextColor($colors->getRed()->toRgb());
    $opt2->setCaption(new TextFragment("项目2"));

    $border3 = new Border($opt3);
    $opt3->setBorder($border3);
    $opt3->getBorder()->setWidth(1.0);
    $opt3->getBorder()->setStyle(BorderStyle::$Solid);
    $opt3->getCharacteristics()->setBorder($colors->getBlack());
    $opt3->getDefaultAppearance()->setTextColor($colors->getRed()->toRgb());
    $opt3->setCaption(new TextFragment("项目3"));

    $c1->getParagraphs()->add($opt1);
    $c2->getParagraphs()->add($opt2);
    $c3->getParagraphs()->add($opt3);

    $document->save($outputFile);
    $document->close();
```


## 添加 ComboBox 字段

组合框是一个表单字段，它将在您的文档中添加一个下拉菜单。

以下代码片段展示了如何在 PDF 文档中添加 [ComboBox](https://reference.aspose.com/pdf/java/com.aspose.pdf/ComboBoxField) 字段。

```php

        $document = new Document($inputFile);

        // 实例化 ComboBox 字段对象
        $page = $document->getPages()->get_Item(1);
        $combo = new ComboBoxField($page, new Rectangle(100, 600, 150, 616));

        // 向 ComboBox 添加选项
        $combo->addOption("Red");
        $combo->addOption("Yellow");
        $combo->addOption("Green");
        $combo->addOption("Blue");

        // 将组合框对象添加到文档对象的表单字段集合中
        $document->getForm()->add($combo);

        // 保存 PDF 文档
        $document->save($outputFile);
        $document->close();
```

## 为表单添加工具提示

Document 类提供了一个名为 Form 的集合来管理 PDF 文档中的表单字段。
 要为表单字段添加工具提示，请使用字段类 AlternateName。Adobe Acrobat 使用“备用名称”作为字段工具提示。

以下代码片段展示了如何使用 PHP 为表单字段添加工具提示。

```php

    $document = new Document($inputFile);
    $textBoxField = $document->getForm()->get("textbox1");

    // 为文本字段设置工具提示
    $textBoxField->setAlternateName("文本框工具提示");

    // 保存 PDF 文档
    $document->save($outputFile);
    $document->close();
```