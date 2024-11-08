---
title: Move and Remove Form Field
type: docs
weight: 50
url: /pt/net/move-remove-form-field/
description: Esta seção explica como você pode mover e remover Campos de Formulário com a Classe FormEditor.
lastmod: "2021-06-05"
draft: false
---

## Mover Campo de Formulário para um Novo Local em um Arquivo PDF Existente

Se você deseja mover um campo de formulário para um novo local, você pode usar o método [MoveField](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor/methods/movefield) da classe [FormEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor). Você só precisa fornecer o nome do campo e o novo local desse campo para o método [MoveField](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor/methods/movefield). Você também precisa salvar o arquivo PDF atualizado usando o método [Save](https://reference.aspose.com/pdf/net/aspose.pdf.facades/form/methods/save/index) da classe [FormEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor). O trecho de código a seguir mostra como mover um campo de formulário para um novo local em um arquivo PDF.

```csharp
public static void MoveField()
        {
            var editor = new FormEditor();
            editor.BindPdf(_dataDir + "Sample-Form-05.pdf");
            editor.MoveField("Last Name", 262.56f, 496.75f, 382.28f, 514.03f);
            editor.Save(_dataDir + "Sample-Form-05-mod.pdf");
        }
```

## Excluir Campo de Formulário de um Arquivo PDF Existente

Para excluir um campo de formulário de um arquivo PDF existente, você pode usar o método RemoveField da classe FormEditor. Este método aceita apenas um argumento: nome do campo. Você precisa criar um objeto da classe FormEditor, chamar o método [RemoveField](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor/methods/removefield) para remover um campo específico do PDF e, em seguida, chamar o método Save para salvar o arquivo PDF atualizado. O trecho de código a seguir mostra como excluir campos de formulário de um arquivo PDF existente.

```csharp
  public static void RemoveFields()
        {
            var editor = new FormEditor();
            editor.BindPdf(_dataDir + "Sample-Form-01.pdf");
            editor.RemoveField("First Name");
            editor.RemoveField("Last Name");
            editor.Save(_dataDir + "Sample-Form-01-updated.pdf");
        }
```

## Renomear Campos de Formulário no PDF

Você também pode renomear seu campo usando o método [RenameField](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor/methods/renamefield) da classe [FormEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor).

```csharp

        public static void RenameFields()
        {
            var editor = new FormEditor();
            editor.BindPdf(_dataDir + "Sample-Form-01.pdf");
            editor.RenameField("Last Name", "LastName");
            editor.RenameField("First Name", "FirstName");
            editor.Save(_dataDir + "Sample-Form-01-updated.pdf");
        }
```