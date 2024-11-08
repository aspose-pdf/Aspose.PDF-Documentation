---
title: Trabalhando com Item de Lista
type: docs
weight: 30
url: /pt/net/working-with-list-item/
description: Esta seção explica como trabalhar com Item de Lista usando Aspose.PDF Facades com a Classe FormEditor.
lastmod: "2021-06-05"
draft: false
---

## Adicionar Item de Lista em um Arquivo PDF Existente

O método [AddListItem](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor/methods/addlistitem) permite adicionar um item em um campo [ListBox](https://reference.aspose.com/pdf/net/aspose.pdf.forms/listboxfield). O primeiro argumento é o nome do campo e o segundo argumento é o item do campo. Você pode passar um único item de campo ou pode passar um array de strings contendo uma lista de itens. Este método é fornecido pela classe [FormEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor). O trecho de código a seguir mostra como adicionar itens de lista em um arquivo PDF.

```csharp
  public static void AddListItem()
        {
            var editor = new FormEditor();
            editor.BindPdf(_dataDir + "Sample-Form-01.pdf");
            editor.AddField(FieldType.ListBox, "Country", 1, 232.56f, 476.75f, 352.28f, 514.03f);
            editor.AddListItem("Country", "USA");
            editor.AddListItem("Country", "Canada");
            editor.AddListItem("Country", "France");
            editor.AddListItem("Country", "Spain");
            editor.Save(_dataDir + "Sample-Form-01-mod.pdf");
        }
```

## Excluir Item de Lista de um Arquivo PDF Existente

O método [DelListItem](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor/methods/dellistitem) permite que você exclua um item específico do [ListBox](https://reference.aspose.com/pdf/net/aspose.pdf.forms/listboxfield). O primeiro parâmetro é o nome do campo enquanto o segundo parâmetro é o item que você deseja excluir da lista. Este método é fornecido pela classe [FormEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor). O trecho de código a seguir mostra como excluir um item de lista do arquivo PDF.

```csharp
      public static void DelListItem()
        {
            var editor = new FormEditor();
            editor.BindPdf(_dataDir + "Sample-Form-04.pdf");
            //-----
            editor.DelListItem("Country", "France");
            //-----
            editor.Save(_dataDir + "Sample-Form-04-mod.pdf");
        }
```