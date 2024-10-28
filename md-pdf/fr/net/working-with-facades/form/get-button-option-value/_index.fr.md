---
title: Obtenir la Valeur de l'Option de Bouton
type: docs
weight: 40
url: /net/get-button-option-value/
description: Cette section explique comment obtenir la valeur de l'option de bouton avec Aspose.PDF Facades en utilisant la classe Form.
lastmod: "2021-06-05"
draft: false
---

## Obtenir les Valeurs d'Option de Bouton à partir d'un Fichier PDF Existant

Les boutons radio offrent un moyen d'afficher différentes options. La classe [Form](https://reference.aspose.com/pdf/net/aspose.pdf.facades/form) vous permet d'obtenir toutes les valeurs des options de bouton pour un bouton radio particulier. Vous pouvez obtenir ces valeurs en utilisant la méthode [GetButtonOptionValues](https://reference.aspose.com/pdf/net/aspose.pdf.facades/form/methods/getbuttonoptionvalues). Cette méthode nécessite le nom du bouton radio en tant que paramètre d'entrée et renvoie une Hashtable. Vous pouvez parcourir cette Hashtable pour obtenir les valeurs d'option. L'extrait de code suivant vous montre comment obtenir les valeurs d'option de bouton à partir d'un fichier PDF existant.

{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-Forms-GetButtonOptionValue-GetButtonOptionValue.cs" >}}

## Obtenez la Valeur de l'Option Actuelle du Bouton à Partir d'un Fichier PDF Existant

Les boutons radio offrent un moyen de définir des valeurs d'option, cependant, un seul d'entre eux peut être sélectionné à la fois. Si vous souhaitez obtenir la valeur d'option actuellement sélectionnée, vous pouvez utiliser la méthode [GetButtonOptionCurrentValue**. La classe [Form](https://reference.aspose.com/pdf/net/aspose.pdf.facades/form) fournit cette méthode. La méthode [GetButtonOptionCurrentValue](https://reference.aspose.com/pdf/net/aspose.pdf.facades/form/methods/getbuttonoptioncurrentvalue) nécessite le nom du bouton radio en tant que paramètre d'entrée et renvoie la valeur sous forme de chaîne. L'extrait de code suivant vous montre comment obtenir la valeur de l'option actuelle du bouton à partir d'un fichier PDF existant.

{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-Forms-GetButtonOptionValue-GetCurrentValue.cs" >}}