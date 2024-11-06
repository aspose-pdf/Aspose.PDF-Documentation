---
title: Trabalhando com Item de Lista
type: docs
weight: 30
url: pt/java/working-with-list-item/
description: Esta seção explica como trabalhar com Item de Lista usando com.aspose.pdf.facades com a classe FormEditor.
lastmod: "2021-06-05"
draft: false
---

## Adicionar Item de Lista em um Arquivo PDF Existente

O método [addListItem](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/FormEditor#addListItem-java.lang.String-java.lang.String-) permite que você adicione um item em um campo ListBox. O primeiro argumento é o nome do campo e o segundo argumento é o item do campo. Você pode passar um único item de campo ou pode passar um array de strings que contém uma lista de itens. Este método é fornecido pela classe [FormEditor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/FormEditor). O trecho de código a seguir mostra como adicionar itens de lista em um arquivo PDF.

```java
public static void AddListItem() {
        FormEditor editor = new FormEditor();
        editor.bindPdf(_dataDir + "Sample-Form-01.pdf");
        editor.addField(FieldType.ListBox, "Country", 1, 232.56f, 476.75f, 352.28f, 514.03f);
        editor.addListItem("Country", "USA");
        editor.addListItem("Country", "Canada");
        editor.addListItem("Country", "France");
        editor.addListItem("Country", "Spain");
        editor.save(_dataDir + "Sample-Form-01-mod.pdf");
    }
```


## Excluir Item de Lista de um Arquivo PDF Existente

O método [delListItem](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/FormEditor#delListItem-java.lang.String-java.lang.String-) permite que você exclua um item específico de um ListBox. O primeiro parâmetro é o nome do campo, enquanto o segundo parâmetro é o item que você deseja excluir da lista. Este método é fornecido pela classe [FormEditor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/FormEditor). O trecho de código a seguir mostra como excluir um item de lista do arquivo PDF.

```java
    public static void DelListItem() {
        FormEditor editor = new FormEditor();
        editor.bindPdf(_dataDir + "Sample-Form-04.pdf");
        // -----
        editor.delListItem("Country", "France");
        // -----
        editor.save(_dataDir + "Sample-Form-04-mod.pdf");
    }
```