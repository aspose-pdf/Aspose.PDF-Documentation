---
title: Timbre rotatif autour du point central
type: docs
weight: 10
url: /net/rotating-stamp-about-the-center-point/
description: Cette section explique comment faire pivoter le timbre autour du point central en utilisant la classe Stamp.
lastmod: "2021-06-05"
draft: false
---

{{% alert color="primary" %}}

Le [namespace Aspose.Pdf.Facades](https://reference.aspose.com/pdf/net/aspose.pdf.facades) dans [Aspose.PDF pour .NET](/pdf/net/) vous permet d'ajouter un timbre dans un fichier PDF existant. Parfois, les utilisateurs ont besoin de faire pivoter le timbre. Dans cet article, nous verrons comment faire pivoter un timbre autour de son point central.

{{% /alert %}}

## Détails de l'implémentation

La classe [Stamp](https://reference.aspose.com/pdf/net/aspose.pdf/stamp) vous permet d'ajouter un filigrane dans un fichier PDF. Vous pouvez spécifier l'image à ajouter comme un tampon en utilisant la méthode [BindImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades.stamp/bindimage/methods/1). La méthode [SetOrigin](https://reference.aspose.com/pdf/net/aspose.pdf.facades/stamp/methods/setorigin) vous permet de définir l'origine du tampon ajouté ; cette origine est les coordonnées inférieures gauche du tampon. Vous pouvez également définir la taille de l'image en utilisant la méthode [SetImageSize](https://reference.aspose.com/pdf/net/aspose.pdf.facades/stamp/methods/setimagesize).

Maintenant, nous voyons comment le tampon peut être tourné autour du centre du tampon. [Stamp](https://reference.aspose.com/pdf/net/aspose.pdf/stamp) classe fournit une propriété nommée Rotation. Cette propriété définit ou obtient la rotation de 0 à 360 du contenu du tampon. Nous pouvons spécifier n'importe quelle valeur de rotation de 0 à 360. En spécifiant la valeur de rotation, nous pouvons faire pivoter le tampon autour de son point central. Si un tampon est un objet de type Stamp, alors la valeur de rotation peut être spécifiée comme aStamp.Rotation = 90. Dans ce cas, le tampon sera pivoté à 90 degrés autour du centre du contenu du tampon. Le snippet de code suivant vous montre comment faire pivoter le tampon autour du point central :



{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-TechnicalArticles-RotatingStamp-RotatingStamp.cs" >}}