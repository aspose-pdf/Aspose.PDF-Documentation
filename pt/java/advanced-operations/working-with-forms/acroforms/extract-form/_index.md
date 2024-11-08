---
title: Extrair Dados AcroForms
linktitle: Extrair Dados AcroForms
type: docs
weight: 30
url: /pt/java/extract-form/
description: Esta seção explica como extrair formulários do seu documento PDF com Aspose.PDF para Java.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Obter Valor de um Campo Individual de Documento PDF

O método [getValue()](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextBoxField#getValue--) do campo de formulário permite que você obtenha o valor de um campo específico.

Para obter o valor, obtenha o campo de formulário da coleção Form do objeto [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document).

Este exemplo seleciona um [TextBoxField](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextBoxField) e recupera seu valor usando o [método getValue()](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextBoxField#getValue--).

```java
package com.aspose.pdf.examples;

import com.aspose.pdf.Document;
import com.aspose.pdf.Field;
import com.aspose.pdf.TextBoxField;

public class ExamplesExtractFormData {
    private static String _dataDir = "/home/aspose/pdf-examples/Samples/Forms/";

    public static void GetValueFromIndividualFieldPDFDocument() {
        // Abrir um documento
        Document pdfDocument = new Document(_dataDir+"GetValueFromField.pdf");

        // Obter um campo
        TextBoxField textBoxField = (TextBoxField) pdfDocument.getForm().get("textbox1");

        // Obter o nome do campo
        System.out.printf("PartialName :-" + textBoxField.getPartialName());

        // Obter o valor do campo
        System.out.printf("Value :-" + textBoxField.getValue());
    }
```


## Obter Valores de Todos os Campos em um Documento PDF

Para obter valores de todos os campos em um documento PDF, você precisa navegar por todos os campos do formulário e então obter o valor usando o [método getValue()](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextBoxField#getValue--). Obtenha cada campo da coleção Form usando o [método getForm() do objeto Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#getForm--) e obtenha a lista de campos do formulário em um array Field usando getFields() e percorra o array para obter o valor dos campos.

O trecho de código a seguir mostra como obter os valores de todos os campos em um documento PDF.

```java
    public static void GetValuesFromAllFieldsPDFDocument() {
        // Abrir documento
        Document document = new Document(_dataDir + "GetValuesFromAllFields.pdf");

        Field[] fields = document.getForm().getFields();
        for (int i = 0; i < fields.length; i++) {

            System.out.println("Campo do formulário: " + fields[i].getFullName());
            System.out.println("Campo do formulário: " + fields[i].getValue());
        }

    }
}
```


## Obter Campos de Formulário de uma Região Específica de um Arquivo PDF

Em alguns casos, é necessário obter dados não de todo o formulário, mas, por exemplo, apenas do quarto superior esquerdo da folha impressa. Com Aspose.PDF para Java, isso não é um problema. Você pode especificar uma região para filtrar campos que estão fora da região especificada do arquivo PDF. Para obter campos de formulário de uma área específica de um arquivo PDF:

1. Abra o arquivo PDF usando o objeto Document.
1. Obtenha o formulário da coleção Forms do documento.
1. Especifique a região retangular e passe-a para o método [getFieldsInRect](https://reference.aspose.com/pdf/java/com.aspose.pdf/Form#getFieldsInRect-com.aspose.pdf.Rectangle-) do objeto Form. Uma coleção [Fields](https://reference.aspose.com/pdf/java/com.aspose.pdf/Field) é retornada.
1. Use isso para manipular os campos.

O trecho de código a seguir mostra como obter campos de formulário em uma região retangular específica de um arquivo PDF.

```java
public static void GetValuesFromSpecificRegion() {
    // Abrir arquivo pdf
    Document doc = new Document(_dataDir + "GetFieldsFromRegion.pdf");

    // Criar objeto retângulo para obter campos nessa área
    Rectangle rectangle = new Rectangle(35, 30, 500, 500);

    // Obter o formulário PDF
    com.aspose.pdf.Form form = doc.getForm();

    // Obter campos na área retangular
    Field[] fields = form.getFieldsInRect(rectangle);

    // Exibir nomes e valores dos campos
    for (Field field : fields)
    {
        // Exibir propriedades de colocação de imagem para todas as colocações
        System.out.println("Nome do Campo: " + field.getFullName() + "-" + "Valor do Campo: " + field.getValue());
    }
}
```