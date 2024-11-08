---
title: Preencher AcroForms
linktitle: Preencher AcroForms
type: docs
weight: 20
url: /pt/java/fill-form/
description: Esta seção explica como preencher um campo de formulário em um documento PDF com Aspose.PDF para Java.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

Documentos PDF são maravilhosos e realmente o tipo de arquivo preferido para criar Formulários.

Aspose.PDF para Java permite que você preencha um campo de formulário, obtenha o campo da coleção de Formulários do objeto Documento.

Vamos ver o exemplo a seguir de como resolver essa tarefa:

```java
public class ExamplesFillForm {

    private static String _dataDir = "/home/aspose/pdf-examples/Samples/Forms/";

    public static void FillFormFieldPDFDocument() {
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

    
}
```