---
title: Travailler avec les artefacts PDF en Python
linktitle: Travailler avec les artefacts
type: docs
weight: 170
url: /fr/python-net/artifacts/
description: Apprenez comment travailler avec les artefacts PDF en Python pour ajouter des arrière-plans, des filigranes et une numérotation Bates, et compter les types d'artefacts avec Aspose.PDF for Python via .NET.
lastmod: "2026-05-22"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Ajoutez des arrière-plans, des filigranes et des artefacts de numérotation Bates en Python
Abstract: Cet article explique comment travailler avec les artefacts PDF dans Aspose.PDF for Python via .NET. Découvrez ce que sont les artefacts, pourquoi ils sont importants pour l'accessibilité et la mise en page du document, et comment ajouter des images d'arrière-plan, appliquer des filigranes, ajouter une numérotation Bates et examiner les types d'artefacts dans les fichiers PDF avec Python.
---

Les artefacts dans les PDF sont des objets graphiques ou d'autres éléments qui ne font pas partie du contenu réel du document. Ils sont généralement utilisés à des fins de décoration, de mise en page ou d'arrière-plan. Des exemples d'artefacts comprennent les en-têtes de page, les pieds de page, les séparateurs ou les images qui n'ont aucune signification.

Le but des artefacts dans le PDF est de permettre la distinction entre les éléments de contenu et les éléments non contenu. Cela est important pour l'accessibilité, car les lecteurs d'écran et autres technologies d'assistance peuvent ignorer les artefacts et se concentrer sur le contenu pertinent. Les artefacts peuvent également améliorer les performances et la qualité des documents PDF, car ils peuvent être omis lors de l'impression, de la recherche ou de la copie.

Utilisez cette section lorsque vous devez créer ou inspecter des éléments PDF non contenu en Python, tels que les arrière-plans de document, les filigranes de page et les marques de numérotation Bates. Les guides suivants montrent les principaux flux de travail d'artefacts pris en charge par Aspose.PDF for Python via .NET.

Pour créer un élément en tant qu'artefact dans le PDF, vous devez utiliser le [Artefact](https://reference.aspose.com/pdf/python-net/aspose.pdf/artifact/) classe.
Il contient les propriétés utiles suivantes :

- **custom_type** - Obtient le nom du type d'artefact. Peut être utilisé si le type d'artefact n'est pas standard.
- **custom_subtype** - Obtient le nom du sous-type d'artefact. Peut être utilisé si le sous-type d'artefact n'est pas un sous-type standard.
- **type** - Obtient le type d'artefact.
- **subtype** - Obtient le sous-type d'artefact. Si l'artefact possède un sous‑type non standard, le nom du sous‑type peut être lu via CustomSubtype.
- **contents** - Obtient la collection des opérateurs internes de l'artefact.
- **form** - Obtient le XForm de l'artefact (si XForm est utilisé).
- **rectangle** - Obtient le rectangle de l'artifact.
- **position** - Obtient ou définit la position de l'artifact. Si cette propriété est spécifiée, alors les marges et les alignements sont ignorés.
- **right_margin** - Marge droite de l'artifact. Si la position est spécifiée explicitement (dans la propriété Position), cette valeur est ignorée.
- **left_margin** - Marge gauche de l'artifact. Si la position est spécifiée explicitement (dans la propriété Position), cette valeur est ignorée.
- **top_margin** - Marge supérieure de l'artifact. Si la position est spécifiée explicitement (dans la propriété Position), cette valeur est ignorée.
- **bottom_margin** - Marge inférieure de l'artifact. Si la position est spécifiée explicitement (dans la propriété Position), cette valeur est ignorée.
- **artifact_horizontal_alignment** - Alignement horizontal de l'artefact. Si la position est spécifiée explicitement (dans la propriété Position), cette valeur est ignorée.
- **artifact_vertical_alignment** - Alignement vertical de l'artefact. Si la position est spécifiée explicitement (dans la propriété Position), cette valeur est ignorée.
- **rotation** - Obtient ou définit l'angle de rotation de l'artefact.
- **text** - Obtient le texte de l'artefact.
- **image** - Obtient l'image de l'artefact (si présente).
- **opacity** - Obtient ou définit l'opacité de l'artefact. Les valeurs possibles sont dans la plage 0..1.
- **lines** - Lignes de l'artefact de texte multiligne.
- **text_state** - État du texte pour le texte de l'artefact.
- **is_background** - Si vrai, l'artefact est placé derrière le contenu de la page.

Les classes suivantes peuvent également être utiles pour travailler avec les artefacts :

- [ArtifactCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/artifactcollection/)
- [BackgroundArtifact](https://reference.aspose.com/pdf/python-net/aspose.pdf/backgroundartifact/)
- [Artifact d'en-tête](https://reference.aspose.com/pdf/python-net/aspose.pdf/headerartifact/)
- [Artifact de pied de page](https://reference.aspose.com/pdf/python-net/aspose.pdf/footerartifact/)
- [Artifact de filigrane](https://reference.aspose.com/pdf/python-net/aspose.pdf/watermarkartifact/)
- [Artifact BatesN](https://reference.aspose.com/pdf/python-net/aspose.pdf/batesnartifact/)

## Flux de travail d'artefacts couverts dans cette section

Veuillez consulter les sections suivantes de l'article :

- [Ajout d'arrière-plans](/pdf/fr/python-net/add-backgrounds/) - ajouter une image d'arrière-plan à votre fichier PDF avec Python.
- [Ajout de la numérotation Bates](/pdf/fr/python-net/add-bates-numbering/) - ajouter la numérotation Bates au PDF.
- [Ajout de filigrane](/pdf/fr/python-net/add-watermarks/) - comment ajouter un filigrane au PDF avec Python.
- [Comptage des artefacts](/pdf/fr/python-net/counting-artifacts/) - comptage des artefacts dans PDF avec Python.
- [Gérer les en-têtes et pieds de page PDF](/pdf/fr/python-net/artifacts-header-footer/) - gérer les en-têtes et pieds de page dans les documents PDF.

Ces tutoriels sont utiles lorsque vous devez gérer des éléments PDF décoratifs ou structurels sans modifier le flux de contenu principal du document.
