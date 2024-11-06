---
title: Limitations de l'API
type: docs
weight: 70
url: fr/net/api-limitations/
---

## **Xsl Fo en Pdf**
Voici les problèmes connus du support XSL-FO.

- SVG n'est pas pris en charge
## **Informations sur le créateur du PDF**
- Veuillez noter que vous ne pouvez pas définir de valeurs pour les champs **Application** et **Producteur**, car Aspose Ltd. et Aspose.PDF pour .NET x.x.x seront affichés dans ces champs
## **Autres**
Voici quelques autres problèmes connus.

- Pdf/X n'est pas pris en charge.
- Le formulaire dynamique XFA n'est pas pris en charge : comme ses pages sont créées/rendues au moment du chargement du PDF, dans Adobe Acrobat/Reader. Nous ne pouvons donc pas extraire et sauvegarder une telle page virtuelle ou plusieurs pages. Au lieu de cela, nous (et Adobe Acrobat) pouvons extraire seulement une véritable page qui contient uniquement un message d'erreur.
- Les symboles spéciaux $p et $P ne fonctionneront pas s'ils ne se terminent pas par un caractère blanc.
- Conversion HTML en PDF : HTML est un langage très vaste et avec chaque nouvelle version de Aspose.PDF pour .NET, nous faisons de notre mieux pour fournir une version meilleure et plus robuste de la conversion HTML en PDF (*en prenant en charge toutes sortes de HTML*) mais comme il existe de nombreux fichiers HTML de nature/structure et complexité différentes, parfois notre composant rencontre des problèmes de mise en forme lors du rendu du contenu HTML au format PDF et cela se produit généralement lors de l'utilisation de documents à structure complexe.
- Conversion HTML vers PDF : HTML est un langage très vaste et avec chaque nouvelle version de Aspose.PDF pour .NET, nous faisons de notre mieux pour livrer une version meilleure et plus robuste de la conversion HTML en PDF (*en prenant en charge tous les types de HTML*). Cependant, comme il existe de nombreux fichiers HTML de nature, structure et complexité différentes, notre composant rencontre parfois des problèmes de formatage lors du rendu des contenus HTML au format PDF, ce qui se produit généralement lors de l'utilisation de documents à structure complexe.
- L'incorporation des polices n'est pas prise en charge dans MS Word pour Macintosh et veuillez également noter que dans MS Word pour Windows, elle est seulement limitée aux polices TrueType. Par conséquent, lors de la visualisation de fichiers word (DOC) générés suite à une conversion PDF en DOC par Aspose.PDF pour .NET, les polices incorporées sont substituées lors de la visualisation des fichiers dans MS Word sur MAC OS. Pour plus de détails, veuillez consulter [macsupportcentral](http://www.macsupportcentral.com/2012/05/embed-fonts-microsoft-office-word-files/).
