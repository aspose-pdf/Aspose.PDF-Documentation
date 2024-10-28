---
title: Apparence et attributs du champ
type: docs
weight: 20
url: /net/changing-field-appearance-and-attributes/
description: Cette section explique comment vous pouvez changer l'apparence et les attributs des champs avec la classe FormEditor.
lastmod: "2021-06-05"
draft: false
---

{{% alert color="primary" %}}

La classe [FormEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/FormEditor) de l'[espace de noms Aspose.Pdf.Facades](https://reference.aspose.com/pdf/net/aspose.pdf.facades) vous permet non seulement de changer l'apparence du champ de formulaire, mais aussi le comportement du champ. Dans cet article, nous verrons comment nous pouvons utiliser la classe FormEditor pour changer l'apparence du champ, les attributs du champ, et également la limite du champ.

{{% /alert %}}

## Détails de l'implémentation

La méthode [SetFieldAppearance](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor/methods/setfieldappearance) est utilisée pour changer l'apparence d'un champ de formulaire. Il prend AnnotationFlag en paramètre. AnnotationFlag est une énumération qui a différents membres comme Hidden ou NoRotate, etc.

La méthode [SetFieldAttributes](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor/methods/setfieldattribute) est utilisée pour changer l'attribut d'un champ de formulaire. Un paramètre passé à cette méthode est l'énumération PropertyFlag qui contient des membres comme ReadOnly ou Required, etc.

La classe [FormEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/FormEditor) fournit également une méthode pour définir la limite du champ. Elle indique au champ combien de caractères il peut contenir. Le code ci-dessous vous montre comment toutes ces méthodes peuvent être utilisées.



{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-TechnicalArticles-ChangingFieldAppearance-ChangingFieldAppearance.cs" >}}