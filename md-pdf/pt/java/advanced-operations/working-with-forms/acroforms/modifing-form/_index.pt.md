---
title: Modificando AcroForms
linktitle: Modificando AcroForms
type: docs
weight: 40
url: /java/modifing-form/
description: Esta seção explica como modificar formulários em seu documento PDF com Aspose.PDF para Java.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Definir Fonte Personalizada para Campos de Formulário

Os campos de formulário em arquivos PDF da Adobe podem ser configurados para usar fontes padrão específicas. Aspose.PDF permite que os desenvolvedores apliquem qualquer fonte como fonte padrão de campo, seja uma das 14 fontes básicas ou uma fonte personalizada. Para definir e atualizar a fonte padrão usada para campos de formulário, Aspose.PDF possui a classe DefaultAppearance (Font font, double size, Color color). Esta classe pode ser acessada usando com.aspose.pdf.DefaultAppearance. Para usar este objeto, utilize o método setDefaultAppearance(..) da classe Field.

O trecho de código a seguir mostra como definir a fonte padrão para o campo de formulário PDF.

```java
package com.aspose.pdf.examples;

import com.aspose.pdf.DefaultAppearance;
import com.aspose.pdf.Document;
import com.aspose.pdf.Field;
import com.aspose.pdf.Font;
import com.aspose.pdf.FontRepository;
import com.aspose.pdf.Rectangle;
import com.aspose.pdf.TextBoxField;

public class ExamplesModifying {

    private static String _dataDir = "/home/aspose/pdf-examples/Samples/Forms/";

    public static void SetFormFieldFontOtherThan14CorePDFFonts() {
        // Abrir documento
        Document pdfDocument = new Document(_dataDir + "FormFieldFont14.pdf");
        // Obter campo de formulário específico do documento
        Field field = (Field) pdfDocument.getForm().get("textbox1");

        // Criar objeto de fonte
        Font font = FontRepository.findFont("ComicSansMS");

        // Definir as informações da fonte para o campo de formulário
        field.setDefaultAppearance (new DefaultAppearance(font, 10, java.awt.Color.BLACK));
        
        // Salvar documento atualizado
        pdfDocument.save(_dataDir + "FormFieldFont14_out.pdf");
    }
```


## Obter/Definir Limite de Campo

O método SetFieldLimit da classe FormEditor permite definir um limite de campo, o número máximo de caracteres que podem ser inseridos em um campo.

```java
    public static void GettingMaximumFieldLimit()
    {
        // Obtendo o limite máximo de campo usando DOM
        Document doc = new Document(_dataDir + "FieldLimit.pdf");
        TextBoxField field = (TextBoxField)doc.getForm().get("textbox1");
        System.out.println("Limite: " +field.getMaxLen());
    }
```

Você também pode obter o mesmo valor usando o namespace Aspose.PDF.Facades com o seguinte trecho de código.

```java
    public static void GettingMaximumFieldLimitFacades()
    {
        // Obtendo o limite máximo de campo usando Facades
        com.aspose.pdf.facades.Form form = new com.aspose.pdf.facades.Form();
        form.bindPdf(_dataDir + "FieldLimit.pdf");
        System.out.println("Limite: " + form.getFieldLimit("textbox1"));
    }
```

Da mesma forma, o Aspose.PDF possui um método que obtém o limite de campo usando a abordagem DOM.
 O trecho de código a seguir mostra as etapas.

```java
    public static void SettingMaximumFieldLimit()
    {
        // Obtendo o limite máximo de campo usando DOM
        Document doc = new Document(_dataDir + "FieldLimit.pdf");
        TextBoxField field = (TextBoxField)doc.getForm().get("textbox1");
        field.setMaxLen(10);
        System.out.println("Limite: " +field.getMaxLen());       
    }
```

## Excluir um Campo de Formulário Específico de um Documento PDF

Todos os campos de formulário estão contidos na coleção Form do objeto [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document). Esta coleção fornece diferentes métodos que gerenciam campos de formulário, incluindo o método delete. Se você deseja excluir um campo específico, passe o nome do campo como parâmetro para o método delete e, em seguida, salve o documento PDF atualizado.

O trecho de código a seguir mostra como excluir um campo nomeado de um documento PDF.

```java
    public static void DeleteParticularFormField()
    {    
        // Abrir um documento
        Document pdfDocument = new Document("input.pdf");

        // Excluir um campo nomeado pelo nome
        pdfDocument.getForm().delete("textbox1");

        // Salvar o PDF modificado
        pdfDocument.save("output.pdf");
    }
```

## Modificar Campo de Formulário em um Documento PDF

A coleção de Formulários do objeto [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) permite que você gerencie campos de formulário em um documento PDF.

Para modificar um campo de formulário, obtenha o campo da coleção de Formulários e defina suas propriedades. Em seguida, salve o documento PDF atualizado.

O trecho de código a seguir mostra como modificar um campo de formulário existente em um documento PDF.

```java
    public static void ModifyFormField()
    {
        Document pdfDocument = new Document("input.pdf");
        // Obter um campo
        TextBoxField textBoxField = (TextBoxField) pdfDocument.getForm().get("textbox1");

        // Modificar o valor do campo
        textBoxField.setValue("Valor Atualizado");

        // Definir o campo como somente leitura
        textBoxField.setReadOnly(true);

        // Salvar o documento atualizado
        pdfDocument.save("output.pdf");
    }
```

### Mover Campo de Formulário para uma Nova Localização em um Arquivo PDF

Se você deseja mover um campo de formulário para uma nova localização em uma página PDF, primeiro obtenha o objeto do campo e, em seguida, especifique um novo valor para seu método setRect.
 Um objeto [Rectangle](https://reference.aspose.com/pdf/java/com.aspose.pdf/Rectangle) com novas coordenadas é atribuído ao método setRect(..). Em seguida, salve o PDF atualizado usando o método save do objeto [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document).

O trecho de código a seguir mostra como mover um campo de formulário para um novo local.

```java
    public static void ModifyMoveFormFieldNewLocation()
    {    
        // Abrir um documento
        Document pdfDocument = new Document(_dataDir+"input.pdf");
        // Obter um campo
        TextBoxField textBoxField = (TextBoxField) pdfDocument.getForm().get("textbox1");

        // Modificar a localização do campo
        textBoxField.setRect(new Rectangle(300, 400, 600, 500));

        // Salvar o documento modificado
        pdfDocument.save("output.pdf");
    }
}
```