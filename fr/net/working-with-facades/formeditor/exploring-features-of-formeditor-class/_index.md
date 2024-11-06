---
title: Exploration des fonctionnalités de la classe FormEditor
type: docs
weight: 10
url: fr/net/exploring-features-of-formeditor-class/
description: Vous pouvez apprendre les détails de l'exploration des fonctionnalités de la classe FormEditor avec la bibliothèque Aspose.PDF pour .NET
lastmod: "2021-06-05"
draft: false
---

{{% alert color="primary" %}}

Les documents PDF contiennent parfois un formulaire interactif, connu sous le nom d'AcroForm. C'est comme un formulaire utilisé dans les pages web. Ces formulaires contiennent différents types de contrôles, par exemple des zones de texte, des cases à cocher et des boutons, etc. Un développeur travaillant avec des fichiers PDF peut parfois avoir besoin de modifier ces formulaires. Dans cet article, nous examinerons en détail comment le [namespace Aspose.Pdf.Facades](https://reference.aspose.com/pdf/net/aspose.pdf.facades) nous permet de le faire.

{{% /alert %}}

## Détails de l'implémentation

Les développeurs peuvent utiliser le [namespace Aspose.Pdf.Facades](https://reference.aspose.com/pdf/net/aspose.pdf.facades) non seulement pour ajouter de nouveaux formulaires et champs de formulaire dans un document PDF, mais aussi pour vous permettre de modifier les champs existants. L'étendue de cet article est limitée aux fonctionnalités de [Aspose.PDF pour .NET](/pdf/net/) qui traitent de l'édition de formulaires.

[FormEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor) est la classe qui contient la plupart des méthodes et propriétés permettant aux développeurs de modifier les champs de formulaire. Vous pouvez non seulement ajouter de nouveaux champs, mais aussi supprimer des champs existants, déplacer un champ vers une autre position, changer le nom d'un champ ou ses attributs, etc. La liste des fonctionnalités fournies par cette classe est assez complète, et il est très facile de travailler avec les champs de formulaire en utilisant cette classe.

Ces méthodes peuvent être divisées en deux grandes catégories, l'une étant utilisée pour manipuler les champs, et l'autre pour définir les nouveaux attributs de ces champs. Les méthodes que nous pouvons regrouper sous la première catégorie incluent AddField, AddListItem, RemoveListItem, CopyInnerField, CopyOuterField, DelListItem, MoveField, RemoveField, et RenameField etc. Dans la deuxième catégorie des méthodes, SetFieldAlignment, SetFieldAppearance, SetFieldAttribute, SetFieldLimit, SetFieldScript peuvent être incluses. Le fragment de code suivant vous montre certaines des méthodes de la classe FormEditor en action :



{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-TechnicalArticles-FormEditorFeatures-FormEditorFeatures.cs" >}}