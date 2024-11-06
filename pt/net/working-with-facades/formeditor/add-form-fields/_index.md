---
title: Adicionar Campos de Formulário PDF
type: docs
weight: 10
url: pt/net/add-form-fields/
description: Este tópico explica como trabalhar com Campos de Formulário com Aspose.PDF Facades usando a Classe FormEditor.
lastmod: "2021-06-05"
draft: false
---

## Adicionar Campo de Formulário em um Arquivo PDF Existente

Para adicionar um campo de formulário em um arquivo PDF existente, é necessário usar o método [AddField](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor/methods/addfield/index) da classe [FormEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor). Este método requer que você especifique o tipo do campo que deseja adicionar, juntamente com o nome e a localização do campo. Você precisa criar um objeto da classe [FormEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor), usar o método [AddField](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor/methods/addfield/index) para adicionar um novo campo no PDF. Além disso, você pode especificar um limite no número de caracteres no seu campo com [SetFieldLimit](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor/methods/setfieldlimit) e, finalmente, usar o método [Save](https://reference.aspose.com/pdf/net/aspose.pdf.facades/form/methods/save/index) para salvar o arquivo PDF atualizado. O trecho de código a seguir mostra como adicionar um campo de formulário em um arquivo PDF existente.

```csharp
   public static void AddField()
        {
            var editor = new FormEditor();
            editor.BindPdf(_dataDir+"Sample-Form-01.pdf");
            editor.AddField(FieldType.Text, "Country", 1, 232.56f, 496.75f, 352.28f, 514.03f);
            editor.SetFieldLimit("Country", 20);
            editor.Save(_dataDir + "Sample-Form-01-mod.pdf");
        }
```
## Adicionar URL do Botão de Envio em um Arquivo PDF Existente 

O método [AddSubmitBtn](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor/methods/addsubmitbtn) permite definir a URL do botão de envio em um arquivo PDF. Esta é a URL para onde os dados são enviados quando o botão de envio é clicado. Em nosso exemplo de código, especificamos a URL, o nome do nosso campo, o número da página em que queremos adicionar e as coordenadas de posicionamento do botão. O método [AddSubmitBtn](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor/methods/addsubmitbtn) requer o nome do campo do botão de envio e a URL. Este método é fornecido pela classe [FormEditor](https://reference.aspose.com/html/net/aspose.html.forms/formeditor). O trecho de código a seguir mostra como definir a URL do botão de envio.

```csharp
public static void AddSubmitBtn()
        {
            var editor = new FormEditor();
            editor.BindPdf(_dataDir + "Sample-Form-01.pdf");
            editor.AddSubmitBtn("Submit", 1, "Submit", "http://localhost:3000", 232.56f, 466.75f, 352.28f, 484.03f);
            editor.Save(_dataDir + "Sample-Form-01-mod.pdf");
        }
```

## Adicionar JavaScript para Botão de Pressão

O método [AddFieldScript](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor/methods/addfieldscript) permite adicionar JavaScript a um botão de pressão em um arquivo PDF. Este método requer o nome do botão de pressão e o JavaScript. Este método é fornecido pela classe [FormEditor](https://reference.aspose.com/html/net/aspose.html.forms/formeditor). O trecho de código a seguir mostra como definir JavaScript em um botão de pressão.

```csharp
     public static void AddFieldScript()
        {
            var editor = new FormEditor();
            editor.BindPdf(_dataDir + "Sample-Form-01.pdf");
            editor.AddFieldScript("Last Name", "app.alert(\"Only one last name\",3);");
            editor.Save(_dataDir + "Sample-Form-01-mod.pdf");
        }
```