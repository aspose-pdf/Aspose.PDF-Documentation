---
title: Ajouter des Champs de Formulaire PDF
type: docs
weight: 10
url: /fr/net/add-form-fields/
description: Ce sujet explique comment travailler avec les Champs de Formulaire avec Aspose.PDF Facades en utilisant la Classe FormEditor.
lastmod: "2021-06-05"
draft: false
---

## Ajouter un Champ de Formulaire dans un fichier PDF existant

Pour ajouter un champ de formulaire dans un fichier PDF existant, vous devez utiliser la méthode [AddField](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor/methods/addfield/index) de la classe [FormEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor). Cette méthode nécessite que vous spécifiiez le type du champ que vous souhaitez ajouter ainsi que le nom et l'emplacement du champ. Vous devez créer un objet de la classe [FormEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor), utiliser la méthode [AddField](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor/methods/addfield/index) pour ajouter un nouveau champ dans le PDF. Vous pouvez également spécifier une limite sur le nombre de caractères dans votre champ avec [SetFieldLimit](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor/methods/setfieldlimit) et enfin utiliser la méthode [Save](https://reference.aspose.com/pdf/net/aspose.pdf.facades/form/methods/save/index) pour enregistrer le fichier PDF mis à jour. Le code suivant vous montre comment ajouter un champ de formulaire dans un fichier PDF existant.

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
## Ajouter l'URL du bouton Soumettre dans un fichier PDF existant

La méthode [AddSubmitBtn](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor/methods/addsubmitbtn) vous permet de définir l'URL du bouton de soumission dans un fichier PDF. C'est l'URL où les données sont envoyées lorsque le bouton de soumission est cliqué. Dans notre exemple de code, nous spécifions l'URL, le nom de notre champ, le numéro de page auquel nous voulons ajouter, et les coordonnées de placement du bouton. La méthode [AddSubmitBtn](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor/methods/addsubmitbtn) nécessite le nom du champ du bouton de soumission et l'URL. Cette méthode est fournie par la classe [FormEditor](https://reference.aspose.com/html/net/aspose.html.forms/formeditor). Le code suivant vous montre comment définir l'URL du bouton de soumission.

```csharp
public static void AddSubmitBtn()
        {
            var editor = new FormEditor();
            editor.BindPdf(_dataDir + "Sample-Form-01.pdf");
            editor.AddSubmitBtn("Submit", 1, "Submit", "http://localhost:3000", 232.56f, 466.75f, 352.28f, 484.03f);
            editor.Save(_dataDir + "Sample-Form-01-mod.pdf");
        }
```

## Ajouter JavaScript pour le Bouton-poussoir

La méthode [AddFieldScript](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor/methods/addfieldscript) vous permet d'ajouter du JavaScript à un bouton-poussoir dans un fichier PDF. Cette méthode nécessite le nom du bouton-poussoir et le JavaScript. Cette méthode est fournie par la classe [FormEditor](https://reference.aspose.com/html/net/aspose.html.forms/formeditor). L'extrait de code suivant vous montre comment définir JavaScript pour un bouton-poussoir.

```csharp
     public static void AddFieldScript()
        {
            var editor = new FormEditor();
            editor.BindPdf(_dataDir + "Sample-Form-01.pdf");
            editor.AddFieldScript("Last Name", "app.alert(\"Only one last name\",3);");
            editor.Save(_dataDir + "Sample-Form-01-mod.pdf");
        }
```