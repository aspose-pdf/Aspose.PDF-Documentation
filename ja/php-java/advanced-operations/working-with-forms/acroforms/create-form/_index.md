---
title: AcroFormsを作成 - PHPで記入可能なPDFを作成
linktitle: AcroFormsを作成
type: docs
weight: 10
url: ja/php-java/create-forms/
description: このセクションでは、Aspose.PDF for PHP via Javaを使用してPDFドキュメントにAcroFormsをゼロから作成する方法を説明します。
lastmod: "2024-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## PDFドキュメントにフォームフィールドを追加

[Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document)クラスは、PDFドキュメント内のフォームフィールドを管理するのに役立つFormという名前のコレクションを提供します。

フォームフィールドを追加するには：

1. 追加したいフォームフィールドを作成します。
2. [Form](https://reference.aspose.com/pdf/java/com.aspose.pdf/Form)コレクションのaddメソッドを呼び出します。

この例は、TextBoxFieldを追加する方法を示しています。同じアプローチで任意のフォームフィールドを追加できます：

1. 最初に、フィールドオブジェクトを作成し、そのプロパティを設定します。
2. その後、フィールドをFormコレクションに追加します。

### TextBoxFieldを追加

テキストフィールドは、受信者がフォームにテキストを入力できるようにするフォーム要素です。
 これは、ユーザーに自由に入力させたいときに使用されます。

以下のコードスニペットは、PDFドキュメントにTextBoxFieldを追加する方法を示しています。

```php

    // ドキュメントを開く
    $colors = new Color();
    $document = new Document($inputFile);
    $page = $document->getPages()->get_Item(1);

    // フィールドを作成
    $textBoxField = new TextBoxField($page, new Rectangle(110, 300, 310, 320));
    $textBoxField->setPartialName("textbox1");
    $textBoxField->setValue("テキストボックス内の値");

    $border = new Border($textBoxField);
    $border->setWidth(5);
    $border->setDash(new Dash(1, 1));
    $textBoxField->setBorder($border);
    $textBoxField->setColor($colors->getGreen());

    // ドキュメントにフィールドを追加
    $document->getForm()->add($textBoxField, 1);

    // 修正したPDFを保存
    $document->save($outputFile);
    $document->close();
```

## RadioButtonFieldの追加

ラジオボタンは、複数選択質問で最も一般的に使用され、1つの回答のみを選択できるシナリオで使用されます。
以下のコードスニペットは、PDFドキュメントに[RadioButtonField](https://reference.aspose.com/pdf/java/com.aspose.pdf/RadioButtonField)を追加する方法を示しています。

```php

    // ドキュメントを開く            
    $document = new Document($inputFile);

    // PDFファイルにページを追加
    $page = $document->getPages()->get_Item(1);

    // RadioButtonFieldオブジェクトをページ番号を引数としてインスタンス化
    $radio = new RadioButtonField($page);

    // 最初のラジオボタンオプションを追加し、その原点も指定
    // Rectangleオブジェクトを使用

    $radio->addOption("Test1", new Rectangle(20, 720, 40, 740));

    // 2番目のラジオボタンオプションを追加
    $radio->addOption("Test2", new Rectangle(120, 720, 140, 740));

    // ドキュメントオブジェクトのフォームオブジェクトにラジオボタンを追加
    $document->getForm()->add($radio);

    // PDFファイルを保存
    $document->save($outputFile);
    $document->close();
```

以下のコードスニペットは、3つのオプションを持つ[RadioButtonField](https://reference.aspose.com/pdf/java/com.aspose.pdf/RadioButtonField)を追加し、それらをテーブルセル内に配置する手順を示しています。

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
    $opt1->setCaption(new TextFragment("アイテム1"));

    $border2 = new Border($opt2);
    $opt3->setBorder($border2);
    $opt3->getBorder()->setWidth(1.0);
    $opt3->getBorder()->setStyle(BorderStyle::$Solid);
    $opt2->getCharacteristics()->setBorder($colors->getBlack());
    $opt2->getDefaultAppearance()->setTextColor($colors->getRed()->toRgb());
    $opt2->setCaption(new TextFragment("アイテム2"));

    $border3 = new Border($opt3);
    $opt3->setBorder($border3);
    $opt3->getBorder()->setWidth(1.0);
    $opt3->getBorder()->setStyle(BorderStyle::$Solid);
    $opt3->getCharacteristics()->setBorder($colors->getBlack());
    $opt3->getDefaultAppearance()->setTextColor($colors->getRed()->toRgb());
    $opt3->setCaption(new TextFragment("アイテム3"));

    $c1->getParagraphs()->add($opt1);
    $c2->getParagraphs()->add($opt2);
    $c3->getParagraphs()->add($opt3);

    $document->save($outputFile);
    $document->close();
```


## コンボボックスフィールドの追加

コンボボックスは、ドキュメントにドロップダウンメニューを追加するフォームフィールドです。

次のコードスニペットは、PDFドキュメントに[コンボボックス](https://reference.aspose.com/pdf/java/com.aspose.pdf/ComboBoxField)フィールドを追加する方法を示しています。

```php

        $document = new Document($inputFile);

        // コンボボックスフィールドオブジェクトをインスタンス化
        $page = $document->getPages()->get_Item(1);
        $combo = new ComboBoxField($page, new Rectangle(100, 600, 150, 616));

        // コンボボックスにオプションを追加
        $combo->addOption("Red");
        $combo->addOption("Yellow");
        $combo->addOption("Green");
        $combo->addOption("Blue");

        // コンボボックスオブジェクトをドキュメントオブジェクトのフォームフィールドコレクションに追加
        $document->getForm()->add($combo);

        // PDFドキュメントを保存
        $document->save($outputFile);
        $document->close();
```

## フォームへのツールチップの追加

Documentクラスは、PDFドキュメント内のフォームフィールドを管理するFormという名前のコレクションを提供します。
 フォームフィールドにツールチップを追加するには、FieldクラスのAlternateNameを使用します。Adobe Acrobatは、フィールドツールチップとして「代替名」を使用します。

以下のコードスニペットは、PHPでフォームフィールドにツールチップを追加する方法を示しています。

```php

    $document = new Document($inputFile);
    $textBoxField = $document->getForm()->get("textbox1");

    // テキストフィールドのツールチップを設定
    $textBoxField->setAlternateName("テキストボックスのツールチップ");

    // PDFドキュメントを保存
    $document->save($outputFile);
    $document->close();
```