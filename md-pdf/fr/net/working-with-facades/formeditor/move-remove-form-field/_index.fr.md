---
title: Déplacer et Supprimer un Champ de Formulaire
type: docs
weight: 50
url: /net/move-remove-form-field/
description: Cette section explique comment vous pouvez déplacer et supprimer des Champs de Formulaire avec la Classe FormEditor.
lastmod: "2021-06-05"
draft: false
---

## Déplacer un Champ de Formulaire vers un Nouvel Emplacement dans un Fichier PDF Existant

Si vous souhaitez déplacer un champ de formulaire vers un nouvel emplacement, vous pouvez utiliser la méthode [MoveField](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor/methods/movefield) de la classe [FormEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor). Vous devez seulement fournir le nom du champ et le nouvel emplacement de ce champ à la méthode [MoveField](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor/methods/movefield). Vous devez également enregistrer le fichier PDF mis à jour en utilisant la méthode [Save](https://reference.aspose.com/pdf/net/aspose.pdf.facades/form/methods/save/index) de la classe [FormEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor). L'extrait de code suivant vous montre comment déplacer un champ de formulaire à un nouvel emplacement dans un fichier PDF.

```csharp
public static void MoveField()
        {
            var editor = new FormEditor();
            editor.BindPdf(_dataDir + "Sample-Form-05.pdf");
            editor.MoveField("Last Name", 262.56f, 496.75f, 382.28f, 514.03f);
            editor.Save(_dataDir + "Sample-Form-05-mod.pdf");
        }
```

## Supprimer un champ de formulaire d'un fichier PDF existant

Pour supprimer un champ de formulaire d'un fichier PDF existant, vous pouvez utiliser la méthode RemoveField de la classe FormEditor. Ce méthode prend seulement un argument : le nom du champ. Vous devez créer un objet de la classe FormEditor, appeler la méthode [RemoveField](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor/methods/removefield) pour supprimer un champ particulier du PDF, puis appeler la méthode Save pour enregistrer le fichier PDF mis à jour. Le code suivant vous montre comment supprimer des champs de formulaire d'un fichier PDF existant.

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

## Renommer les champs de formulaire dans le PDF

Vous pouvez également renommer votre champ en utilisant la méthode [RenameField](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor/methods/renamefield) de la classe [FormEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor).

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