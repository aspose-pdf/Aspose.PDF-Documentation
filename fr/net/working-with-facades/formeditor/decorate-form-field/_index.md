---
title: Décorer un Champ de Formulaire dans un PDF
type: docs
weight: 20
url: /fr/net/decorate-form-field/
description: Cette section explique comment décorer un champ de formulaire dans un PDF en utilisant la classe FormEditor.
lastmod: "2021-06-05"
draft: false
---

## Décorer un Champ de Formulaire Particulier dans un Fichier PDF Existant

La méthode [DecorateField](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor/methods/decoratefield) présente dans la classe [FormEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor) permet de décorer un champ de formulaire particulier dans un fichier PDF. If you want to decorate a particular field then you need to pass the field name to this method.  
Si vous souhaitez décorer un champ particulier, vous devez passer le nom du champ à cette méthode. Cependant, avant d'appeler cette méthode, vous devez créer des objets des classes [FormEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor) et [FormFieldFacade](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formfieldfacade). Vous devez également assigner l'objet [FormFieldFacade](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formfieldfacade) à la propriété [Facade](https://reference.aspose.com/pdf/net/aspose.pdf.facades/facade/properties/index) de l'objet [FormEditor](https://reference.aspose.com/html/net/aspose.html.forms/formeditor). Après cela, vous pouvez définir n'importe quel attribut fourni par l'objet [FormFieldFacade](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formfieldfacade). Une fois que vous avez défini les attributs, vous pouvez appeler la méthode [DecorateField](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor/methods/decoratefield) et enfin enregistrer le PDF mis à jour en utilisant la méthode [Save](https://reference.aspose.com/pdf/net/aspose.pdf.facades/form/methods/save/index) de la classe [FormEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor).

Le code suivant vous montre comment décorer un champ de formulaire particulier.

```csharp
public static void DecorateField()
        {
            var editor = new FormEditor();
            editor.BindPdf(_dataDir + "Sample-Form-01.pdf");

            var cityDecoration = new FormFieldFacade
            {
                Font = FontStyle.Courier,
                FontSize = 12,
                BorderColor = System.Drawing.Color.Black,
                BorderWidth = 2
            };

            editor.Facade = cityDecoration;
            editor.DecorateField("City");
            editor.Save(_dataDir + "Sample-Form-02.pdf");
        }
```
## Décorer Tous les Champs d'un Type Particulier dans un Fichier PDF Existant

La méthode [DecorateField](https://reference.aspose.com/pdf/net/aspose.pdf.facades.formeditor/decoratefield/methods/1) vous permet de décorer tous les champs de formulaire d'un type particulier dans un fichier PDF en une seule fois. If you want to decorate all fields of a particular type then you need to pass the field type to this method.

Si vous souhaitez décorer tous les champs d'un type particulier, vous devez passer le type de champ à cette méthode. Cependant, avant d'appeler cette méthode, vous devez créer des objets des classes [FormEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor) et [FormFieldFacade](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formfieldfacade). Vous devez également attribuer l'objet [FormFieldFacade](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formfieldfacade) à la propriété [Facade](https://reference.aspose.com/pdf/net/aspose.pdf.facades/facade/properties/index) de l'objet [FormEditor](https://reference.aspose.com/html/net/aspose.html.forms/formeditor). Après cela, vous pouvez définir n'importe quel attribut fourni par l'objet [FormFieldFacade](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formfieldfacade). Une fois que vous avez défini les attributs, vous pouvez appeler la méthode [DecorateField](https://reference.aspose.com/pdf/net/aspose.pdf.facades.formeditor/decoratefield/methods/1) et enfin sauvegarder le PDF mis à jour en utilisant la méthode [Save](https://reference.aspose.com/pdf/net/aspose.pdf.facades/form/methods/save/index) de la classe [FormEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor). Le code suivant vous montre comment décorer tous les champs d'un type particulier.

```csharp
        public static void DecorateField2()
        {
            var editor = new FormEditor();
            editor.BindPdf(_dataDir + "Sample-Form-01.pdf");

            var textFieldDecoration = new FormFieldFacade
            {
                Alignment = FormFieldFacade.AlignCenter,
            };

            editor.Facade = textFieldDecoration;
            editor.DecorateField(FieldType.Text);
            editor.Save(_dataDir + "Sample-Form-01-align-text.pdf");
        }
```