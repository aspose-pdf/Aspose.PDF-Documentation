---
title: Travailler avec les artefacts en Python via .NET
linktitle: Travailler avec les artefacts
type: docs
weight: 170
url: /fr/python-net/artifacts/
description: Aspose.PDF pour Python via .NET vous permet d'ajouter une image d'arrière-plan aux pages PDF et d'obtenir chaque filigrane à l'aide de la classe Artifact.
lastmod: "2025-11-13"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Ajouter des artefacts au PDF avec Python
Abstract: Cet article explore le concept et l'application des artefacts dans les documents PDF, en se concentrant particulièrement sur leur rôle dans l'amélioration de l'accessibilité et des performances. Les artefacts sont des éléments non‑contenus, tels que des composants décoratifs ou de mise en page, qui ne transmettent pas le sens du document. L'article met en avant l'utilisation de la classe `Artifact` dans la bibliothèque Aspose.PDF pour Python via .NET pour gérer ces éléments, offrant des propriétés comme `custom_type`, `contents` et `opacity` pour une personnalisation détaillée. Il présente également les classes associées pour la gestion de types spécifiques d'artefacts. Des exemples pratiques démontrent des opérations telles que la récupération de filigranes, l'ajout d'images d'arrière-plan, le comptage des types d'artefacts et la mise en œuvre de la numérotation Bates.
---

Les artefacts dans les PDF sont des objets graphiques ou d'autres éléments qui ne font pas partie du contenu réel du document. Ils sont généralement utilisés à des fins de décoration, de mise en page ou d'arrière-plan. Des exemples d'artefacts incluent les en-têtes de page, pieds de page, séparateurs ou images qui ne transmettent aucune signification.

Le but des artefacts dans le PDF est de permettre la distinction entre le contenu et les éléments non‑contenus. Cela est important pour l'accessibilité, car les lecteurs d'écran et autres technologies d'assistance peuvent ignorer les artefacts et se concentrer sur le contenu pertinent. Les artefacts peuvent également améliorer les performances et la qualité des documents PDF, car ils peuvent être omis lors de l'impression, de la recherche ou de la copie.

Pour créer un élément en tant qu'artefact dans le PDF, vous devez utiliser la classe [Artifact](https://reference.aspose.com/pdf/python-net/aspose.pdf/artifact/).
Il contient les propriétés utiles suivantes :

- **custom_type** - Obtient le nom du type d'artefact. Peut être utilisé si le type d'artefact n'est pas standard.
- **custom_subtype** - Obtient le nom du sous‑type d'artefact. Peut être utilisé si le sous‑type d'artefact n'est pas standard.
- **type** - Obtient le type d'artefact.
- **subtype** - Obtient le sous‑type d'artefact. Si l'artefact possède un sous‑type non standard, le nom du sous‑type peut être lu via CustomSubtype.
- **contents** - Obtient la collection des opérateurs internes de l'artefact.
- **form** - Obtient le XForm de l'artefact (si un XForm est utilisé).
- **rectangle** - Obtient le rectangle de l'artefact.
- **position** - Obtient ou définit la position de l'artefact. Si cette propriété est spécifiée, les marges et alignements sont ignorés.
- **right_margin** - Marge droite de l'artefact. Si la position est spécifiée explicitement (dans la propriété Position), cette valeur est ignorée.
- **left_margin** - Marge gauche de l'artefact. Si la position est spécifiée explicitement (dans la propriété Position), cette valeur est ignorée.
- **top_margin** - Marge supérieure de l'artefact. Si la position est spécifiée explicitement (dans la propriété Position), cette valeur est ignorée.
- **bottom_margin** - Marge inférieure de l'artefact. Si la position est spécifiée explicitement (dans la propriété Position), cette valeur est ignorée.
- **artifact_horizontal_alignment** - Alignement horizontal de l'artefact. Si la position est spécifiée explicitement (dans la propriété Position), cette valeur est ignorée.
- **artifact_vertical_alignment** - Alignement vertical de l'artefact. Si la position est spécifiée explicitement (dans la propriété Position), cette valeur est ignorée.
- **rotation** - Obtient ou définit l'angle de rotation de l'artefact.
- **text** - Obtient le texte de l'artefact.
- **image** - Obtient l'image de l'artefact (si présente).
- **opacity** - Obtient ou définit l'opacité de l'artefact. Les valeurs possibles sont dans la plage 0..1.
- **lines** - Lignes du texte multiligne de l'artefact.
- **text_state** - État du texte pour le texte de l'artefact.
- **is_background** - Si vrai, l'artefact est placé derrière le contenu de la page.

Les classes suivantes peuvent également être utiles pour travailler avec les artefacts :

- [ArtifactCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/artifactcollection/)
- [BackgroundArtifact](https://reference.aspose.com/pdf/python-net/aspose.pdf/backgroundartifact/)
- [HeaderArtifact](https://reference.aspose.com/pdf/python-net/aspose.pdf/headerartifact/)
- [FooterArtifact](https://reference.aspose.com/pdf/python-net/aspose.pdf/footerartifact/)
- [WatermarkArtifact](https://reference.aspose.com/pdf/python-net/aspose.pdf/watermarkartifact/)
- [Bates Numbering](https://reference.aspose.com/pdf/python-net/aspose.pdf/)

Veuillez consulter les sections suivantes de l'article :

- [Ajout d'arrière-plans](/pdf/python-net/add-backgrounds/) - ajoutez une image d'arrière-plan à votre fichier PDF avec Python.
- [Ajout de la numérotation Bates](/pdf/python-net/add-bates-numbering/) - ajoutez la numérotation Bates au PDF.
- [Ajout de filigrane](/pdf/python-net/add-watermarks/) - comment ajouter un filigrane à un PDF avec Python.
- [Comptage d'artefacts](/pdf/python-net/counting-artifacts/) - comptage des artefacts dans un PDF avec Python.

