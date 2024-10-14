---
title: Fonctionnalités Avancées
type: docs
weight: 210
url: /net/advanced-features/
---

## Envoyer un Pdf au Navigateur pour Téléchargement

Parfois, lorsque vous développez une application ASP.NET, vous devez envoyer des fichiers PDF aux navigateurs web pour téléchargement sans les sauvegarder physiquement. Pour cela, vous pouvez enregistrer le document PDF dans un objet MemoryStream après l'avoir généré et passer les octets de ce MemoryStream à l'objet Response. Ce faisant, le navigateur téléchargera le document PDF généré.

Le fragment de code suivant démontre la fonctionnalité ci-dessus :

{{< gist "aspose-pdf" "7e1330795d76012fcb04248bb81d45b3" "Examples-Examples.Web-SendPdfToBrowserForDownload.aspx-1.cs" >}}

## Extraire des fichiers intégrés d'un fichier PDF

Aspose.PDF se distingue lorsqu'il s'agit de fonctionnalités avancées pour travailler avec des fichiers au format PDF. Il extrait les fichiers intégrés bien mieux que d'autres outils offrant cette fonctionnalité.

Avec Aspose.PDF pour .NET, vous pouvez extraire efficacement tout fichier intégré, qu'il s'agisse d'une police intégrée, d'une image, d'une vidéo ou d'un audio.
Avec Aspose.PDF pour .NET, vous pouvez extraire efficacement tout fichier intégré, qu'il s'agisse d'une police intégrée, d'une image, d'une vidéo ou d'un audio.

Le fragment de code suivant extrait tous les fichiers intégrés d'un fichier PDF :

{{< gist "aspose-pdf" "7e1330795d76012fcb04248bb81d45b3" "Examples-CSharp-AsposePDF-DocumentConversion-PDFToXML-PDFToXML.cs" >}}

## Utilisation du script Latex pour ajouter des expressions mathématiques

Avec Aspose.PDF, vous pouvez ajouter des expressions/formules mathématiques dans un document PDF en utilisant un script latex. Les exemples suivants montrent comment cette fonctionnalité peut être utilisée de deux manières différentes, afin d'ajouter une formule mathématique à l'intérieur d'une cellule de tableau :

### Sans préambule et environnement de document

{{< gist "aspose-pdf" "7e1330795d76012fcb04248bb81d45b3" "Examples-CSharp-AsposePDF-Text-UseLatexScript-WithoutPreambleanddocument.cs" >}}

### Avec préambule et environnement de document

{{< gist "aspose-pdf" "7e1330795d76012fcb04248bb81d45b3" "Examples-CSharp-AsposePDF-Text-UseLatexScript2-WithPreambleanddocument.cs" >}}

### Prise en charge des balises Latex
### Prise en charge des balises Latex

L'environnement align est défini dans le paquet amsmath, et l'environnement proof est défini dans le paquet amsthm. Ainsi, vous devez spécifier ces paquets en utilisant la commande \usepackage dans le préambule du document. Et cela signifie que vous devez inclure le texte LaTeX dans l'environnement document comme indiqué dans l'exemple de code suivant.

{{< gist "aspose-com-gists" "63473b1ba28e09e229cfbf4430eabd8a" "Examples-CSharp-AsposePDF-Text-UseLatexScript3-UseLatexScript3.cs" >}}
