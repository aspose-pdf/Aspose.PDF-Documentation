---
title: Criar AcroForms - Criar PDF Preenchível em Java
linktitle: Criar AcroForms
type: docs
weight: 10
url: /pt/java/create-forms/
description: Esta seção explica como criar AcroForms do zero em seus documentos PDF com Aspose.PDF para Java.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Adicionar Campo de Formulário em um Documento PDF

A classe [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) fornece uma coleção chamada Form, que ajuda a gerenciar campos de formulário em um documento PDF.

Para adicionar um campo de formulário:

1. Crie o campo de formulário que você deseja adicionar.
2. Chame o método add da coleção [Form](https://reference.aspose.com/pdf/java/com.aspose.pdf/Form).

Este exemplo mostra como adicionar um TextBoxField. Você pode adicionar qualquer campo de formulário usando a mesma abordagem:

1. Primeiro, crie um objeto de campo e defina suas propriedades.
2. Em seguida, adicione o campo à coleção Form.

### Adicionando TextBoxField

Um campo de texto é um elemento de formulário que permite que um destinatário insira texto em seu formulário.
 Isso seria usado sempre que você quiser permitir que o usuário tenha a liberdade de digitar o que quiser.

Os seguintes trechos de código mostram como adicionar um TextBoxField a um documento PDF.

```java
public class ExamplesCreateForm {

    private static String _dataDir = "/home/aspose/pdf-examples/Samples/Forms/";

    public static void AddingTextBoxField() {

        // Abrir documento
        Document pdfDocument = new Document(_dataDir + "TextField.pdf");
        Page page = pdfDocument.getPages().get_Item(1);
        // Criar um campo
        TextBoxField textBoxField = new TextBoxField(page, new Rectangle(100, 200, 300, 300));
        textBoxField.setPartialName("textbox1");
        textBoxField.setValue("Caixa de Texto");

        // TextBoxField.Border = new Border(
        Border border = new Border(textBoxField);
        border.setWidth(5);
        border.setDash(new Dash(1, 1));
        textBoxField.setBorder(border);

        textBoxField.setColor(Color.getGreen());

        // Adicionar campo ao documento
        pdfDocument.getForm().add(textBoxField, 1);

        // Salvar PDF modificado
        pdfDocument.save(_dataDir + "TextBox_out.pdf");

    }
```

## Adicionando RadioButtonField

Um botão de opção é mais comumente usado para perguntas de múltipla escolha, no cenário onde apenas uma resposta pode ser selecionada.

Os trechos de código a seguir mostram como adicionar [RadioButtonField](https://reference.aspose.com/pdf/java/com.aspose.pdf/RadioButtonField) em um documento PDF.

```java
public static void AddingRadioButton() {
        Document pdfDocument = new Document();
        // adicionar uma página ao arquivo PDF
        pdfDocument.getPages().add();

        // instanciar objeto RadioButtonField com número de página como argumento
        RadioButtonField radio = new RadioButtonField(pdfDocument.getPages().get_Item(1));

        // adicionar a primeira opção de rádio e também especificar sua origem usando o objeto Rectangle
        radio.addOption("Test", new Rectangle(20, 720, 40, 740));
        // adicionar a segunda opção de rádio
        radio.addOption("Test1", new Rectangle(120, 720, 140, 740));
        // adicionar botão de rádio ao objeto de formulário do objeto Document
        pdfDocument.getForm().add(radio);
        // salvar o arquivo PDF
        pdfDocument.save("RadioButtonSample.pdf");

    }
```


O trecho de código a seguir mostra as etapas para adicionar [RadioButtonField](https://reference.aspose.com/pdf/java/com.aspose.pdf/RadioButtonField) com três opções e colocá-los dentro de células da Tabela.

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


## Adicionando Legenda ao RadioButtonField

O trecho de código a seguir mostra como adicionar uma legenda que será associada ao [RadioButtonField](https://reference.aspose.com/pdf/java/com.aspose.pdf/RadioButtonField):

```java
public static void AddingCaptionToRadioButtonField() {
        // Carregar formulário PDF de origem
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

                // Criar objeto TextParagraph
                TextParagraph par = new TextParagraph();

                // Definir posição do parágrafo
                par.setPosition(new Position(field0.getRect().getLLX(),
                        field0.getRect().getLLY() + updatedFragment.getTextState().getFontSize()));
                // Especificar modo de quebra de linha
                par.getFormattingOptions().setWrapMode(TextFormattingOptions.WordWrapMode.ByWords);

                // Adicionar novo TextFragment ao parágrafo
                par.appendLine(updatedFragment);

                // Adicionar o TextParagraph usando TextBuilder
                TextBuilder textBuilder = new TextBuilder(document.getPages().get_Item(1));
                textBuilder.appendParagraph(par);

                field0.deleteOption("item1");
            }
        }
        document.save(_dataDir + "RadioButtonField_out.pdf");

    }
```


## Adicionando campo ComboBox

Um Combo Box é um campo de formulário que adicionará um menu suspenso ao seu documento.

Os seguintes trechos de código mostram como adicionar um campo [ComboBox](https://reference.aspose.com/pdf/java/com.aspose.pdf/ComboBoxField) em um documento PDF.

```java
public static void AddingComboboxField() {
        // criar objeto Document
        Document doc = new Document();
        // adicionar página ao objeto do documento
        doc.getPages().add();
        // instanciar objeto ComboBox Field
        ComboBoxField combo = new ComboBoxField(doc.getPages().get_Item(1), new Rectangle(100, 600, 150, 616));
        // adicionar opção ao ComboBox
        combo.addOption("Red");
        combo.addOption("Yellow");
        combo.addOption("Green");
        combo.addOption("Blue");
        // adicionar objeto combo box à coleção de campos de formulário do objeto do documento
        doc.getForm().add(combo);
        // salvar o documento PDF
        doc.save("ComboBox_Added.pdf");
    }
```

## Adicionar Tooltip ao Formulário

A classe Document fornece uma coleção chamada Form que gerencia campos de formulário em um documento PDF.
 Para adicionar uma dica de ferramenta a um campo de formulário, use a classe Field AlternateName. O Adobe Acrobat usa o 'nome alternativo' como uma dica de ferramenta do campo.

Os trechos de código a seguir mostram como adicionar uma dica de ferramenta a um campo de formulário com Java.

```java
public static void AddTooltipToFormField() {
        // Carregar o formulário PDF de origem
        Document doc = new Document(_dataDir + "AddTooltipToField.pdf");

        // Obter um campo
        TextBoxField textBoxField = (TextBoxField) doc.getForm().get("textbox1");

        // Definir a dica de ferramenta para o campo de texto
        textBoxField.setAlternateName("Dica de ferramenta da caixa de texto");

        // Salvar documento modificado
        doc.save("output.pdf");
    }
```