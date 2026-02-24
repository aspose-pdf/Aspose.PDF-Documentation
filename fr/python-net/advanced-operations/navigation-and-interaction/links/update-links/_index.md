---
title: Mettre à jour les liens dans le PDF avec Python
linktitle: Mettre à jour les liens
type: docs
weight: 20
url: /fr/python-net/update-links/
description: Mettre à jour les liens dans un PDF de manière programmatique. Ce guide porte sur la manière de mettre à jour les liens dans un PDF en langage Python.
lastmod: "2025-07-17"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Comment mettre à jour les liens dans un PDF
Abstract: Le guide Aspose.PDF for Python via .NET sur la mise à jour des liens accompagne les développeurs à travers le processus de modification du comportement des hyperliens dans les documents PDF à l’aide de Python. Il explique comment changer les destinations des liens pour les orienter vers des pages spécifiques, des sites web externes ou même d’autres fichiers PDF. La documentation couvre également comment ajuster l’apparence des annotations de lien, y compris la couleur du texte, et fournit des exemples de code pratiques pour chaque scénario. Que vous corrigiez des URL obsolètes ou amélioriez la navigation, cette ressource offre une approche claire et efficace pour gérer les liens de manière programmatique.
---

## Mettre à jour la couleur du texte de LinkAnnotation

Cet exemple montre comment détecter toutes les annotations de lien sur la première page d’un PDF à l’aide d’Aspose.PDF pour Python, puis mettre en évidence le texte près de chaque lien en changeant la couleur de sa police en rouge. Il utilise TextFragmentAbsorber avec une zone légèrement agrandie autour de chaque rectangle de lien pour trouver et modifier le texte à proximité.

Cela peut être utilisé pour :

- Marquer visuellement les liens dans un document
- Améliorer l’accessibilité en soulignant le contenu lié
- Prétraiter les fichiers PDF avant révision ou exportation

Pour chacune de ces annotations de lien, le script récupère sa frontière rectangulaire et agrandit légèrement cette zone afin d’inclure le texte à proximité, permettant une identification visuelle plus large. Il applique ensuite un TextFragmentAbsorber sur cette zone agrandie pour extraire les fragments de texte qui s’y trouvent. Ces fragments capturés sont modifiés en changeant la couleur de leur police en rouge, marquant ainsi efficacement le texte environnant pour mise en évidence et révision. Après avoir appliqué toutes ces modifications, le document modifié est enregistré dans le chemin de sortie, préservant les annotations mises en surbrillance et le texte qui leur est associé.

```python

    import aspose.pdf as ap
    from os import path

    path_infile = path.join(self.dataDir, infile)
    path_outfile = path.join(self.dataDir, outfile)

    # Load the input PDF document
    document = ap.Document(path_infile)

    # Filter all link annotations on the first page
    link_annotations = [
        a
        for a in document.pages[1].annotations
        if a.annotation_type == ap.annotations.AnnotationType.LINK
    ]

    # Loop through each link annotation found
    for la in link_annotations:
        # Create a text absorber for extracting text fragments
        ta = ap.text.TextFragmentAbsorber()

        # Get the rectangle area of the annotation
        rect = la.rect

        # Expand the rectangle slightly to catch text near the link
        rect.llx -= 2  # Lower-left x
        rect.lly -= 2  # Lower-left y
        rect.urx += 2  # Upper-right x
        rect.ury += 2  # Upper-right y

        # Restrict text search to the adjusted rectangle
        ta.text_search_options = ap.text.TextSearchOptions(rect)

        # Apply the absorber to the first page
        ta.visit(document.pages[1])

        # Iterate through found text fragments and change their color to red
        for textFragment in ta.text_fragments:
            textFragment.text_state.foreground_color = ap.Color.red

    # Save the updated PDF document to the output path
    document.save(path_outfile)
```

## Mettre à jour la bordure

Le script se concentre sur la première page du document et filtre toutes les annotations, ne sélectionnant que celles de type LINK — qui représentent généralement des éléments interactifs, tels que des hyperliens ou des déclencheurs de navigation. Pour chacune de ces annotations de lien, le code les convertit en type LinkAnnotation et met à jour leur propriété de couleur en rouge, les mettant ainsi en évidence visuellement pour qu’elles se démarquent du reste du contenu. Après que toutes les annotations de lien ont été modifiées, le document mis à jour est enregistré à l’emplacement de sortie défini, préservant le nouveau style.

```python

    import aspose.pdf as ap
    from os import path

    path_infile = path.join(self.dataDir, infile)
    path_outfile = path.join(self.dataDir, outfile)

    # Load the PDF document
    document = ap.Document(path_infile)

    # Get all annotations of type LINK on the first page
    link_annotations = [
        a
        for a in document.pages[1].annotations
        if (a.annotation_type == ap.annotations.AnnotationType.LINK)
    ]

    # Loop through each link annotation and change its color to red
    for la in link_annotations:
        link_annotation = cast(ap.annotations.LinkAnnotation, la)
        link_annotation.color = ap.Color.red  # Highlight the link in red

    # Save the modified PDF to the output path
    document.save(path_outfile)
```    

## Mettre à jour la destination Web

Une fois les chemins définis, le document original est chargé à l’aide de la bibliothèque Aspose.PDF, rendant son contenu accessible à la modification. Le script se concentre ensuite sur la première page du document, filtre toutes les annotations et ne sélectionne que celles de type lien, représentant généralement des zones cliquables ou des hyperliens. Pour éviter les erreurs de type et garantir une manipulation sécurisée, chaque annotation est vérifiée avec is_assignable puis convertie en type LinkAnnotation approprié. Si le lien est associé à une GoToURIAction, c’est‑à‑dire qu’il pointe vers une adresse web, le script met à jour cette URI pour rediriger les utilisateurs vers "https://www.google.com". Enfin, après que toutes les modifications souhaitées ont été appliquées, le document modifié est enregistré à l’emplacement de sortie spécifié.

```python

    import aspose.pdf as ap
    from os import path

path_infile = path.join(self.dataDir, infile)
path_outfile = path.join(self.dataDir, outfile)

# Load the PDF document
document = ap.Document(path_infile)

# Find all LINK annotations on the first page
link_annotations = [
    a
    for a in document.pages[1].annotations
    if (a.annotation_type == ap.annotations.AnnotationType.LINK)
]

# Loop through annotations and replace target URI
for la in link_annotations:
    # Ensure the annotation is a LinkAnnotation
    if is_assignable(la, ap.annotations.LinkAnnotation):
        annotation = cast(ap.annotations.LinkAnnotation, la)
        
        # Check if the action is of type GoToURIAction
        if is_assignable(annotation.action, ap.annotations.GoToURIAction):
            action = cast(ap.annotations.GoToURIAction, annotation.action)
            
            # Replace the existing URI with Google
            action.uri = "https://www.google.com"

# Save the modified document to output path
document.save(path_outfile)
```
