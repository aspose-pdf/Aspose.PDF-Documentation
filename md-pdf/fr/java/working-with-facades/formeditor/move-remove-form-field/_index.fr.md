---
title: Déplacer et Supprimer un Champ de Formulaire
type: docs
weight: 50
url: /java/move-remove-form-field/
description: Cette section explique comment vous pouvez déplacer et supprimer des champs de formulaire avec la classe FormEditor.
lastmod: "2021-06-05"
draft: false
---

## Déplacer un Champ de Formulaire vers un Nouvel Emplacement dans un Fichier PDF Existant

Si vous souhaitez déplacer un champ de formulaire vers un nouvel emplacement, vous pouvez utiliser la méthode [moveField](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/FormEditor#moveField-java.lang.String-float-float-float-float-) de la classe [FormEditor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/FormEditor).
 Vous n'avez besoin de fournir que le nom du champ et le nouvel emplacement de ce champ à la méthode [moveField](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/FormEditor#moveField-java.lang.String-float-float-float-float-). Vous devez également enregistrer le fichier PDF mis à jour en utilisant la méthode Save de la classe [FormEditor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/FormEditor). L'extrait de code suivant vous montre comment déplacer un champ de formulaire à un nouvel emplacement dans un fichier PDF.

```java
 public static void MoveField()
        {
            var editor = new FormEditor();
            editor.BindPdf(_dataDir + "Sample-Form-05.pdf");
            editor.MoveField("Last Name", 262.56f, 496.75f, 382.28f, 514.03f);
            editor.Save(_dataDir + "Sample-Form-05-mod.pdf");
        }
```

## Supprimer un champ de formulaire d'un fichier PDF existant

Pour supprimer un champ de formulaire d'un fichier PDF existant, vous pouvez utiliser la méthode RemoveField de la classe FormEditor. Cette méthode ne prend qu'un seul argument : le nom du champ. Vous devez créer un objet de la classe FormEditor, appeler la méthode [removeField](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/FormEditor#removeField-java.lang.String-) pour supprimer un champ particulier du PDF, puis appeler la méthode Save pour enregistrer le fichier PDF mis à jour. L'extrait de code suivant vous montre comment supprimer des champs de formulaire d'un fichier PDF existant.

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

## Renommer les champs de formulaire dans le PDF

Vous pouvez également renommer votre champ en utilisant la méthode [renameField](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/FormEditor#renameField-java.lang.String-java.lang.String-) de la classe [FormEditor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/FormEditor).
```java
    public static void RenameFields()
        {
            var editor = new FormEditor();
            editor.BindPdf(_dataDir + "Sample-Form-01.pdf");
            // Renommer le champ "Last Name" en "LastName"
            editor.RenameField("Last Name", "LastName");
            // Renommer le champ "First Name" en "FirstName"
            editor.RenameField("First Name", "FirstName");
            editor.Save(_dataDir + "Sample-Form-01-updated.pdf");
        }
```