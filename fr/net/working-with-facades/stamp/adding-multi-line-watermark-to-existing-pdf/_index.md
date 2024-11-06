---
title: Ajout d'un filigrane multi-lignes
type: docs
weight: 10
url: fr/net/adding-multi-line-watermark-to-existing-pdf/
description: Cette section explique comment ajouter un filigrane multi-lignes à un PDF existant en utilisant la classe FormattedText.
lastmod: "2021-06-05"
draft: false
---

{{% alert color="primary" %}}

Beaucoup d'utilisateurs souhaitent tamponner leurs documents PDF avec du texte multi-lignes. Ils essaient généralement d'utiliser `\n` et `<br>` mais ces types de caractères ne sont pas pris en charge par l'espace de noms Aspose.Pdf.Facades. Donc, pour rendre cela possible, nous avons ajouté une autre méthode nommée [AddNewLineText()](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formattedtext/methods/addnewlinetext/index) dans la classe [FormattedText](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formattedtext) de l'espace de noms Aspose.Pdf.Facades.

{{% /alert %}}

## Implémentation

Veuillez vous référer au fragment de code suivant pour ajouter un filigrane multi-lignes dans un PDF existant.

```csharp

// Instancier un objet de type Stamp
Stamp logoStamp = new Stamp();

// Instancier un objet de la classe FormattedText
FormattedText formatText = new FormattedText("Bonjour le monde!",
System.Drawing.Color.FromArgb(180, 0, 0), FontStyle.TimesItalic, EncodingType.Winansi, false, 50);

// Ajouter une autre ligne pour le Stamp
formatText.AddNewLineText("Bonne chance");
// Liaison du logo au PDF
logoStamp.BindLogo(formatText);
```