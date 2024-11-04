---
title: Justifier le texte dans un champ de zone de texte
type: docs
weight: 20
url: /net/justify-text-in-a-textbox-field/
description: Cet article vous montre comment justifier le texte dans un champ de zone de texte en utilisant la classe Form.
lastmod: "2021-06-05"
draft: false
---

{{% alert color="primary" %}}

Dans cet article, nous vous montrerons comment justifier le texte dans un champ de zone de texte dans un fichier PDF.

{{% /alert %}}

## Détails de l'implémentation

La classe [FormEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor) dans l'[espace de noms Aspose.Pdf.Facades](https://reference.aspose.com/pdf/net/aspose.pdf.facades) offre la capacité de décorer un champ de formulaire PDF. Maintenant, si votre besoin est de justifier le texte dans un champ de zone de texte, vous pouvez facilement y parvenir en utilisant la valeur [AlignJustified](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formfieldfacade/fields/alignjustified) de l'énumération [FormFieldFacade](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formfieldfacade) et en appelant la méthode [FormEditor.DecorateField](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor/methods/decoratefield/index). Dans l'exemple ci-dessous, nous remplirons d'abord un champ de zone de texte en utilisant la méthode [FillField](https://reference.aspose.com/pdf/net/aspose.pdf.facades/form/methods/fillfield/index) de la classe [Form](https://reference.aspose.com/pdf/net/aspose.pdf.facades/form). Après cela, nous utiliserons la classe FormEditor pour justifier le texte dans le champ de zone de texte. Le code ci-dessous vous montre comment justifier le texte dans un champ de zone de texte.

{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-TechnicalArticles-JustifyText-JustifyText.cs" >}}
Veuillez noter que l'alignement justifié n'est pas pris en charge par le PDF, c'est pourquoi le texte sera aligné à gauche lorsque vous saisissez le texte dans le champ de texte. Mais lorsque le champ n'est pas actif, le texte est justifié.