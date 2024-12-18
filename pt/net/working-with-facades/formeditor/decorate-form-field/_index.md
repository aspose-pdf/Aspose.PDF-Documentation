---
title: Decorar Campo de Formulário em PDF
type: docs
weight: 20
url: /pt/net/decorate-form-field/
description: Esta seção explica como decorar Campo de Formulário em PDF usando a Classe FormEditor.
lastmod: "2021-06-05"
draft: false
---

## Decorar um Campo de Formulário Particular em um Arquivo PDF Existente

O método [DecorateField](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor/methods/decoratefield) presente na classe [FormEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor) permite decorar um campo de formulário particular em um arquivo PDF. Se você deseja decorar um campo específico, então você precisa passar o nome do campo para este método. 
No entanto, antes de chamar este método, você precisa criar objetos das classes [FormEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor) e [FormFieldFacade](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formfieldfacade). Você também precisa atribuir o objeto [FormFieldFacade](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formfieldfacade) à propriedade [Facade](https://reference.aspose.com/pdf/net/aspose.pdf.facades/facade/properties/index) do objeto [FormEditor](https://reference.aspose.com/html/net/aspose.html.forms/formeditor). Depois disso, você pode definir quaisquer atributos fornecidos pelo objeto [FormFieldFacade](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formfieldfacade). Uma vez que você tenha definido os atributos, você pode chamar o método [DecorateField](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor/methods/decoratefield) e, finalmente, salvar o PDF atualizado usando o método [Save](https://reference.aspose.com/pdf/net/aspose.pdf.facades/form/methods/save/index) da classe [FormEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor).
O trecho de código a seguir mostra como decorar um campo de formulário específico.

```csharp
public static void DecorateField()
        {
            var editor = new FormEditor();
            editor.BindPdf(_dataDir + "Sample-Form-01.pdf");

            var cityDecoration = new FormFieldFacade
            {
                Font = FontStyle.Courier,
                FontSize = 12,
                BorderColor = System.Drawing.Color.Black,
                BorderWidth = 2
            };

            editor.Facade = cityDecoration;
            editor.DecorateField("City");
            editor.Save(_dataDir + "Sample-Form-02.pdf");
        }
```
## Decorar Todos os Campos de um Tipo Particular em um Arquivo PDF Existente

O método [DecorateField](https://reference.aspose.com/pdf/net/aspose.pdf.facades.formeditor/decoratefield/methods/1) permite decorar todos os campos de formulário de um tipo específico em um arquivo PDF de uma só vez. If you want to decorate all fields of a particular type then you need to pass the field type to this method.

Se você deseja decorar todos os campos de um tipo específico, então você precisa passar o tipo de campo para este método. However, before calling this method, you need to create objects of [FormEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor) and [FormFieldFacade](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formfieldfacade) classes.  

No entanto, antes de chamar este método, você precisa criar objetos das classes [FormEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor) e [FormFieldFacade](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formfieldfacade). Você também precisa atribuir o objeto [FormFieldFacade](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formfieldfacade) à propriedade [Facade](https://reference.aspose.com/pdf/net/aspose.pdf.facades/facade/properties/index) do objeto [FormEditor](https://reference.aspose.com/html/net/aspose.html.forms/formeditor). Depois disso, você pode definir quaisquer atributos fornecidos pelo objeto [FormFieldFacade](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formfieldfacade). Uma vez que você tenha definido os atributos, você pode chamar o método [DecorateField](https://reference.aspose.com/pdf/net/aspose.pdf.facades.formeditor/decoratefield/methods/1) e finalmente salvar o PDF atualizado usando o método [Save](https://reference.aspose.com/pdf/net/aspose.pdf.facades/form/methods/save/index) da classe [FormEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor). O trecho de código a seguir mostra como decorar todos os campos de um tipo específico.

```csharp
        public static void DecorateField2()
        {
            var editor = new FormEditor();
            editor.BindPdf(_dataDir + "Sample-Form-01.pdf");

            var textFieldDecoration = new FormFieldFacade
            {
                Alignment = FormFieldFacade.AlignCenter,
            };

            editor.Facade = textFieldDecoration;
            editor.DecorateField(FieldType.Text);
            editor.Save(_dataDir + "Sample-Form-01-align-text.pdf");
        }
```