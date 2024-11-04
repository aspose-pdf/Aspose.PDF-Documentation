---
title: Mover e Remover Campo de Formulário
type: docs
weight: 50
url: /java/move-remove-form-field/
description: Esta seção explica como você pode mover e remover Campos de Formulário com a Classe FormEditor.
lastmod: "2021-06-05"
draft: false
---

## Mover Campo de Formulário para uma Nova Localização em um Arquivo PDF Existente

Se você deseja mover um campo de formulário para uma nova localização, você pode usar o método [moveField](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/FormEditor#moveField-java.lang.String-float-float-float-float-) da classe [FormEditor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/FormEditor).
 Você só precisa fornecer o nome do campo e a nova localização deste campo para o método [moveField](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/FormEditor#moveField-java.lang.String-float-float-float-float-). Você também precisa salvar o arquivo PDF atualizado usando o método Save da classe [FormEditor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/FormEditor). O trecho de código a seguir mostra como mover um campo de formulário para uma nova localização em um arquivo PDF.

```java
 public static void MoveField()
        {
            var editor = new FormEditor();
            editor.BindPdf(_dataDir + "Sample-Form-05.pdf");
            editor.MoveField("Last Name", 262.56f, 496.75f, 382.28f, 514.03f);
            editor.Save(_dataDir + "Sample-Form-05-mod.pdf");
        }
```

## Excluir Campo de Formulário de um Arquivo PDF Existente

Para excluir um campo de formulário de um arquivo PDF existente, você pode usar o método RemoveField da classe FormEditor. Este método leva apenas um argumento: nome do campo. Você precisa criar um objeto da classe FormEditor, chamar o método [removeField](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/FormEditor#removeField-java.lang.String-) para remover um campo específico do PDF e então chamar o método Save para salvar o arquivo PDF atualizado. O trecho de código a seguir mostra como excluir campos de formulário de um arquivo PDF existente.

```java
 public static void RemoveFields()
        {
            var editor = new FormEditor();
            editor.BindPdf(_dataDir + "Sample-Form-01.pdf");
            editor.RemoveField("First Name");
            editor.RemoveField("Last Name");
            editor.Save(_dataDir + "Sample-Form-01-updated.pdf");
        }
```

## Renomear Campos de Formulário em PDF

Você também pode renomear seu campo usando o método [renameField](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/FormEditor#renameField-java.lang.String-java.lang.String-) da classe [FormEditor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/FormEditor).
```java
    public static void RenameFields()
        {
            var editor = new FormEditor();
            // Vincular o PDF
            editor.BindPdf(_dataDir + "Sample-Form-01.pdf");
            // Renomear o campo "Último Nome" para "LastName"
            editor.RenameField("Last Name", "LastName");
            // Renomear o campo "Primeiro Nome" para "FirstName"
            editor.RenameField("First Name", "FirstName");
            // Salvar o PDF atualizado
            editor.Save(_dataDir + "Sample-Form-01-updated.pdf");
        }
```