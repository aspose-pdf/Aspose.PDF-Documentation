---
title: Travailler avec AcroForms dans PDF 
linktitle: AcroForms
type: docs
weight: 10
url: fr/php-java/acroforms/
description: Avec Aspose.PDF pour PHP via Java, vous pouvez créer un formulaire à partir de zéro, remplir le champ de formulaire dans un document PDF, extraire des données du formulaire, ajouter ou supprimer des champs dans le formulaire existant.
lastmod: "2024-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Fondamentaux des AcroForms

**AcroForms** sont la technologie de formulaires PDF originale. AcroForms est un formulaire orienté page. Ils ont été introduits pour la première fois en 1998. Ils acceptent l'entrée au format de données de formulaires ou FDF et au format de données de formulaires XML ou xFDF. Des fournisseurs tiers prennent en charge les AcroForms. Lorsque Adobe a introduit les AcroForms, ils les ont appelés "formulaire PDF créé avec Adobe Acrobat Pro/Standard et qui n'est pas un type spécial de formulaire XFA statique ou dynamique". Les AcroForms sont portables et fonctionnent sur toutes les plateformes.

Vous pouvez utiliser les AcroForms pour ajouter des pages supplémentaires au document de formulaire PDF.
 Grâce au concept de Modèles, vous pouvez utiliser AcroForms pour remplir le formulaire avec plusieurs enregistrements de base de données.

Le PDF 1.7 prend en charge deux méthodes différentes pour intégrer des données et des formulaires PDF.

*AcroForms (également connus sous le nom de formulaires Acrobat)*, introduits et inclus dans la spécification du format PDF 1.2.

*Les formulaires Adobe XML Forms Architecture (XFA)*, introduits dans la spécification du format PDF 1.5 en tant que fonctionnalité optionnelle. La spécification XFA n'est pas incluse dans la spécification PDF, elle est seulement référencée.

Pour comprendre les formulaires **Acroforms** par rapport aux formulaires **XFA**, nous devons d'abord comprendre les bases. Pour commencer, les deux sont des formulaires PDF que vous pouvez utiliser. Acroforms est le plus ancien, créé en 1998, et il est toujours considéré comme le formulaire PDF classique. Les formulaires XFA sont des pages web que vous pouvez enregistrer sous forme de PDF, et sont apparus en 2003. Il a fallu un certain temps avant que le PDF commence à accepter les formulaires XFA.

Les AcroForms ont des capacités non trouvées dans XFA et inversement, XFA a certaines capacités non trouvées dans AcroForms. Par exemple :

- Les AcroForms prennent en charge le concept de "Modèles", permettant d'ajouter des pages supplémentaires au document de formulaire PDF pour remplir le formulaire avec plusieurs enregistrements de base de données.- XFA prend en charge le concept de reformatage de document permettant à un champ de redimensionner si nécessaire pour accueillir les données.

Ainsi, les PDFs sont le meilleur format de fichier pour les formulaires puisqu'ils peuvent être distribués électroniquement et avoir des informations remplies dans le document et renvoyées à l'expéditeur sans avoir besoin d'imprimer ou d'envoyer par courrier traditionnel.

Pour une étude plus détaillée des possibilités de travailler avec des formulaires, étudiez les articles suivants dans la section :

-[Créer AcroForm](/pdf/php-java/create-form/) - créer un formulaire à partir de zéro, ajouter RadioButtonField, TextBoxField, Champ de légende en utilisant PHP.

-[Remplir AcroForm](/pdf/php-java/fill-form/) - pour remplir un champ de formulaire, obtenez le champ de la collection de formulaires de l'objet Document.

-[Extraire les données AcroForm](/pdf/php-java/extract-form/) - obtenir des valeurs de tous et des champs individuels, etc.

-[Modifier AcroForm](/pdf/php-java/modifing-form/) - obtenir/définir FieldLimit, supprimer des champs dans un formulaire existant, définir la police du champ de formulaire en dehors des 14 polices PDF Core avec PHP.