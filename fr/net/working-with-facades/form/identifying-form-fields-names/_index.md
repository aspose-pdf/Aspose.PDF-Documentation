---
title: Identification des noms de champs de formulaire
type: docs
weight: 10
url: /fr/net/identifying-form-fields-names/
description: Aspose.PDF.Facades vous permet d'identifier les noms des champs de formulaire en utilisant la classe Form.
lastmod: "2021-06-05"
draft: false
---

[Aspose.PDF for .NET](/pdf/fr/net/) offre la possibilité de créer, modifier et remplir des formulaires PDF déjà créés. Le namespace [Aspose.Pdf.Facades](https://reference.aspose.com/pdf/net/aspose.pdf.facades) contient la classe [Form](https://reference.aspose.com/pdf/net/aspose.pdf.facades/form), qui contient la fonction nommée [FillField](https://reference.aspose.com/pdf/net/aspose.pdf.facades/form/methods/fillfield/index) et elle prend deux arguments, c'est-à-dire le nom du champ et la valeur du champ. Donc, pour remplir les champs de formulaire, vous devez connaître le nom exact du champ de formulaire.

## Détails de l'implémentation

Nous rencontrons souvent un scénario où nous devons remplir le formulaire qui est créé dans un certain outil c'est-à-dire. Adobe Designer, et nous ne sommes pas sûrs des noms des champs du formulaire. Ainsi, pour remplir les champs du formulaire, nous devons d'abord lire les noms de tous les champs du formulaire Pdf. La classe [Form](https://reference.aspose.com/pdf/net/aspose.pdf.facades/form) fournit la propriété nommée [FieldNames](https://reference.aspose.com/pdf/net/aspose.pdf.facades/form/properties/fieldnames) qui renvoie tous les noms des champs et renvoie null si le PDF ne contient aucun champ. Cependant, lors de l'utilisation de cette propriété, nous obtenons les noms de tous les champs dans le formulaire PDF et nous pourrions ne pas être certains de quel nom correspond à quel champ sur le formulaire.

Comme solution à ce problème, nous utiliserons les attributs d'apparence de chaque champ. La classe Form a une fonction nommée [GetFieldFacade](https://reference.aspose.com/pdf/net/aspose.pdf.facades/form/methods/getfieldfacade) qui renvoie des attributs, y compris l'emplacement, la couleur, le style de bordure, la police, l'élément de liste, etc. Pour enregistrer ces valeurs, nous devons utiliser la classe [FormFieldFacade](https://reference.aspose.com/pdf/net/aspose.pdf.facades/FormFieldFacade), qui est utilisée pour enregistrer les attributs visuels des champs. Une fois que nous avons ces attributs, nous pouvons ajouter un champ de texte sous chaque champ qui afficherait le nom du champ.

{{% alert color="primary" %}}
À ce stade, une question se pose "comment déterminer l'emplacement où ajouter le champ de texte ?"
{{% /alert %}}

{{% alert color="primary" %}}
La solution à ce problème est la propriété Box dans la classe [FormFieldFacade](https://reference.aspose.com/pdf/net/aspose.pdf.facades/FormFieldFacade), qui contient l'emplacement du champ. Nous devons enregistrer ces valeurs dans un tableau de type rectangle et utiliser ces valeurs pour identifier la position où ajouter les nouveaux champs de texte.

{{% /alert %}}

Dans l'espace de noms [Aspose.Pdf.Facades](https://reference.aspose.com/pdf/net/aspose.pdf.facades), nous avons une classe nommée [FormEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/FormEditor) qui offre la capacité de manipuler les formulaires PDF. Ouvrir un formulaire PDF ; ajouter un champ de texte sous chaque champ de formulaire existant et enregistrer le formulaire PDF avec un nouveau nom.

{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-TechnicalArticles-IdentifyFormFields-IdentifyFormFields.cs" >}}