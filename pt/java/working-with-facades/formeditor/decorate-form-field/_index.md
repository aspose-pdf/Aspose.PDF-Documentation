---
title: Decorar Campo de Formulário em PDF
type: docs
weight: 20
url: pt/java/decorate-form-field/
description: Esta seção explica como decorar Campo de Formulário em PDF usando a Classe FormEditor.
lastmod: "2021-06-05"
draft: false
---

## Decorar um Campo de Formulário Particular em um Arquivo PDF Existente

O método [decorateField](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/FormEditor#decorateField--) presente na classe [FormEditor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/FormEditor) permite decorar um campo de formulário particular em um arquivo PDF.
 Se você deseja decorar um campo específico, então precisa passar o nome do campo para este método. No entanto, antes de chamar este método, você precisa criar objetos das classes [FormEditor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/FormEditor) e [FormFieldFacade](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/FormFieldFacade). Depois disso, você pode definir quaisquer atributos fornecidos pelo objeto [FormFieldFacade](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/FormFieldFacade). Uma vez que você tenha definido os atributos, pode chamar o método [decorateField](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/FormEditor#decorateField--) e, finalmente, salvar o PDF atualizado utilizando o método Save da classe [FormEditor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/FormEditor). 
O trecho de código a seguir mostra como decorar um campo específico de um formulário.

```java
public static void DecorateField() {
        FormEditor editor = new FormEditor();
        editor.bindPdf(_dataDir + "Sample-Form-01.pdf");

        FormFieldFacade cityDecoration = new FormFieldFacade();
        cityDecoration.setFont(FontStyle.Courier);
        cityDecoration.setFontSize(12);
        cityDecoration.setBorderColor(Color.BLACK);
        cityDecoration.setBorderWidth(2);

        editor.setFacade(cityDecoration);
        editor.decorateField("City");
        editor.save(_dataDir + "Sample-Form-02.pdf");
    }
```

## Decorar Todos os Campos de um Tipo Particular em um Arquivo PDF Existente

O método [decorateField](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/FormEditor#decorateField--) permite decorar todos os campos de formulário de um tipo específico em um arquivo PDF de uma só vez.
 Se você deseja decorar todos os campos de um tipo específico, então precisa passar o tipo de campo para este método. No entanto, antes de chamar este método, você precisa criar objetos das classes [FormEditor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/FormEditor) e [FormFieldFacade](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/FormFieldFacade). Depois disso, você pode definir quaisquer atributos fornecidos pelo objeto [FormFieldFacade](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/FormFieldFacade). Uma vez que você tenha definido os atributos, pode chamar o método [decorateField](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/FormEditor#decorateField--) e, finalmente, salvar o PDF atualizado usando o método Save da classe [FormEditor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/FormEditor). O trecho de código a seguir mostra como decorar todos os campos de um tipo específico.

```java
   public static void DecorateFields() {
        FormEditor editor = new FormEditor();
        editor.bindPdf(_dataDir + "Sample-Form-01.pdf");

        FormFieldFacade textFieldDecoration = new FormFieldFacade();
        textFieldDecoration.setAlignment(FormFieldFacade.ALIGN_CENTER);

        editor.setFacade(textFieldDecoration);
        editor.decorateField(FieldType.Text);
        editor.save(_dataDir + "Sample-Form-01-align-text.pdf");
    }
```