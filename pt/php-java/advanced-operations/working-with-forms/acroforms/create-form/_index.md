---
title: Criar AcroForms - Criar PDF Preenchível em PHP
linktitle: Criar AcroForms
type: docs
weight: 10
url: pt/php-java/create-forms/
description: Esta seção explica como criar AcroForms do zero em seus documentos PDF com Aspose.PDF para PHP via Java.
lastmod: "2024-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Adicionar Campo de Formulário em um Documento PDF

A classe [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) fornece uma coleção chamada Form que ajuda a gerenciar campos de formulário em um documento PDF.

Para adicionar um campo de formulário:

1. Crie o campo de formulário que deseja adicionar.
2. Chame o método add da coleção [Form](https://reference.aspose.com/pdf/java/com.aspose.pdf/Form).

Este exemplo mostra como adicionar um TextBoxField. Você pode adicionar qualquer campo de formulário usando a mesma abordagem:

1. Primeiro, crie um objeto de campo e defina suas propriedades.
2. Em seguida, adicione o campo à coleção Form.

### Adicionando TextBoxField

Um campo de texto é um elemento de formulário que permite que um destinatário insira texto em seu formulário.
 Isso seria usado sempre que você quiser permitir que o usuário tenha a liberdade de digitar o que quiser.

Os seguintes trechos de código mostram como adicionar um TextBoxField a um documento PDF.

```php

    // Abrir documento
    $colors = new Color();
    $document = new Document($inputFile);
    $page = $document->getPages()->get_Item(1);

    // Criar um campo
    $textBoxField = new TextBoxField($page, new Rectangle(110, 300, 310, 320));
    $textBoxField->setPartialName("textbox1");
    $textBoxField->setValue("Algum valor na Caixa de Texto");

    $border = new Border($textBoxField);
    $border->setWidth(5);
    $border->setDash(new Dash(1, 1));
    $textBoxField->setBorder($border);
    $textBoxField->setColor($colors->getGreen());

    // Adicionar campo ao documento
    $document->getForm()->add($textBoxField, 1);

    // Salvar PDF modificado
    $document->save($outputFile);
    $document->close();
```

## Adicionando RadioButtonField

Um Botão de Rádio é mais comumente usado para questões de múltipla escolha, no cenário onde apenas uma resposta pode ser selecionada.
Os trechos de código a seguir mostram como adicionar [RadioButtonField](https://reference.aspose.com/pdf/java/com.aspose.pdf/RadioButtonField) em um documento PDF.

```php

    // Abrir documento            
    $document = new Document($inputFile);

    // adicionar uma página ao arquivo PDF
    $page = $document->getPages()->get_Item(1);

    // instanciar objeto RadioButtonField com número da página como argumento
    $radio = new RadioButtonField($page);

    // adicionar primeira opção de botão de rádio e também especificar sua origem
    // usando objeto Rectangle

    $radio->addOption("Test1", new Rectangle(20, 720, 40, 740));

    // adicionar segunda opção de botão de rádio
    $radio->addOption("Test2", new Rectangle(120, 720, 140, 740));

    // adicionar botão de rádio ao objeto formulário do objeto Document
    $document->getForm()->add($radio);

    // salvar o arquivo PDF
    $document->save($outputFile);
    $document->close();
```

O trecho de código a seguir mostra as etapas para adicionar [RadioButtonField](https://reference.aspose.com/pdf/java/com.aspose.pdf/RadioButtonField) com três opções e colocá-las dentro de células da Tabela.

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

    $rf = new CampoDeBotaoRadio($page);
    $rf->setPartialName("radio1");
    $document->getForm()->add($rf, 1);

    $opt1 = new OpcaoDeBotaoRadio();
    $opt2 = new OpcaoDeBotaoRadio();
    $opt3 = new OpcaoDeBotaoRadio();

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

    $border1 = new Borda($opt1);
    $opt1->setBorder($border1);
    $opt1->getBorder()->setWidth(1.0);
    $opt1->getBorder()->setStyle(BorderStyle::$Solid);
    $opt1->getCharacteristics()->setBorder($colors->getBlack());
    $opt1->getDefaultAppearance()->setTextColor($colors->getRed()->toRgb());
    $opt1->setCaption(new FragmentoDeTexto("Item1"));

    $border2 = new Borda($opt2);
    $opt3->setBorder($border2);
    $opt3->getBorder()->setWidth(1.0);
    $opt3->getBorder()->setStyle(BorderStyle::$Solid);
    $opt2->getCharacteristics()->setBorder($colors->getBlack());
    $opt2->getDefaultAppearance()->setTextColor($colors->getRed()->toRgb());
    $opt2->setCaption(new FragmentoDeTexto("Item2"));

    $border3 = new Borda($opt3);
    $opt3->setBorder($border3);
    $opt3->getBorder()->setWidth(1.0);
    $opt3->getBorder()->setStyle(BorderStyle::$Solid);
    $opt3->getCharacteristics()->setBorder($colors->getBlack());
    $opt3->getDefaultAppearance()->setTextColor($colors->getRed()->toRgb());
    $opt3->setCaption(new FragmentoDeTexto("Item3"));

    $c1->getParagraphs()->add($opt1);
    $c2->getParagraphs()->add($opt2);
    $c3->getParagraphs()->add($opt3);

    $document->save($outputFile);
    $document->close();
```


## Adicionando campo ComboBox

Uma Combo Box é um campo de formulário que adicionará um menu suspenso ao seu documento.

Os seguintes trechos de código mostram como adicionar um campo [ComboBox](https://reference.aspose.com/pdf/java/com.aspose.pdf/ComboBoxField) em um documento PDF.

```php

        $document = new Document($inputFile);

        // instanciar objeto ComboBox Field
        $page = $document->getPages()->get_Item(1);
        $combo = new ComboBoxField($page, new Rectangle(100, 600, 150, 616));

        // adicionar opção à ComboBox
        $combo->addOption("Red");
        $combo->addOption("Yellow");
        $combo->addOption("Green");
        $combo->addOption("Blue");

        // adicionar objeto combo box à coleção de campos de formulário do objeto documento
        $document->getForm()->add($combo);

        // salvar o documento PDF
        $document->save($outputFile);
        $document->close();
```

## Adicionar Tooltip ao Formulário

A classe Document fornece uma coleção chamada Form que gerencia campos de formulário em um documento PDF.
 Para adicionar uma dica de ferramenta a um campo de formulário, use a classe Field AlternateName. O Adobe Acrobat usa o 'nome alternativo' como uma dica de ferramenta para o campo.

Os trechos de código a seguir mostram como adicionar uma dica de ferramenta a um campo de formulário com PHP.

```php

    $document = new Document($inputFile);
    $textBoxField = $document->getForm()->get("textbox1");

    // Defina a dica de ferramenta para o campo de texto
    $textBoxField->setAlternateName("Dica de ferramenta da caixa de texto");

    // salve o documento PDF
    $document->save($outputFile);
    $document->close();
```