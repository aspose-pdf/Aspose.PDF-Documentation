---
title: Travailler avec les artefacts PDF en Python
linktitle: Travailler avec les artefacts
type: docs
weight: 170
url: /fr/python-net/artifacts/
description: Ajouter, inspecter et supprimer les artefacts PDF en Python, y compris les arrière-plans, les filigranes, les en-têtes, les pieds de page et la numérotation Bates.
lastmod: "2026-11-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Gérer les artefacts de pages PDF en Python
Abstract: Trouvez des guides pour ajouter et supprimer des artefacts PDF, inspecter les détails des filigranes et compter les artefacts de pagination par sous‑type avec Aspose.PDF for Python via .NET.
---

Les artefacts PDF marquent les éléments de page tels que les arrière-plans décoratifs, les en-têtes et pieds de page dynamiques, et les filigranes. Dans un Tagged PDF, les technologies d’assistance peuvent ignorer les artefacts et se concentrer sur le contenu significatif du document.

## Choisir un guide

### Ajouter des artefacts

- [Ajouter des arrière-plans](/pdf/fr/python-net/add-backgrounds/)
- [Ajouter des filigranes](/pdf/fr/python-net/add-watermarks/)
- [Ajouter la numérotation Bates](/pdf/fr/python-net/add-bates-numbering/)
- [Ajouter des en-têtes et des pieds de page](/pdf/fr/python-net/artifacts-header-footer/)

### Inspecter les artefacts

- [Compter les artefacts de pagination par sous‑type](/pdf/fr/python-net/counting-artifacts/)
- [Extraire les détails du filigrane](/pdf/fr/python-net/extract-watermarks/)

### Supprimer des artefacts

- [Supprimer les arrière-plans](/pdf/fr/python-net/remove-backgrounds/)
- [Supprimer les filigranes](/pdf/fr/python-net/remove-watermarks/)
- [Supprimer la numérotation Bates](/pdf/fr/python-net/remove-bates-numbering/)
- [Supprimer les en-têtes et pieds de page](/pdf/fr/python-net/remove-headers-footers/)

## API des artefacts

La propriété `artifacts` renvoie la collection [`ArtifactCollection`](https://reference.aspose.com/pdf/python-net/aspose.pdf/artifactcollection/) de la page. La classe [`Artifact`](https://reference.aspose.com/pdf/python-net/aspose.pdf/artifact/) fournit les propriétés communes aux classes spécialisées [`BackgroundArtifact`](https://reference.aspose.com/pdf/python-net/aspose.pdf/backgroundartifact/), [`WatermarkArtifact`](https://reference.aspose.com/pdf/python-net/aspose.pdf/watermarkartifact/), [`HeaderArtifact`](https://reference.aspose.com/pdf/python-net/aspose.pdf/headerartifact/), [`FooterArtifact`](https://reference.aspose.com/pdf/python-net/aspose.pdf/footerartifact/) et [`BatesNArtifact`](https://reference.aspose.com/pdf/python-net/aspose.pdf/batesnartifact/).

| Tâche | Propriétés |
| --- | --- |
| Identifier l'artefact | Utiliser `type` et `subtype` pour les classifications standard et `custom_type` et `custom_subtype` pour les noms personnalisés. |
| Inspectez son contenu | Utiliser `text`, `image`, et `lines` pour le texte et les images, ou `contents` et `form` pour les opérateurs PDF et le XForm associé. |
| Positionnez-le sur la page | Utiliser `rectangle` pour inspecter ses limites. Définir `position` pour un placement ou une utilisation explicite `left_margin`, `right_margin`, `top_margin`, `bottom_margin`, `artifact_horizontal_alignment`, et `artifact_vertical_alignment`. Une position explicite remplace les marges et l'alignement. |
| Contrôlez son apparence | Utiliser `rotation`, `opacity` (de 0 à 1), et `text_state`. Définir `is_background` pour placer l'artefact derrière le contenu de la page. |
