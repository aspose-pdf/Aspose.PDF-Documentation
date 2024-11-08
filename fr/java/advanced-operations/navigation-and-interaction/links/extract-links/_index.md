---
title: Extraire les Liens du Fichier PDF
linktitle: Extraire les Liens
type: docs
weight: 30
url: /fr/java/extract-links/
description: Extraire les liens d'un PDF avec Java. Ce sujet vous explique comment extraire des liens en utilisant la classe AnnotationSelector.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Extraire les Liens du Fichier PDF

Les liens sont représentés sous forme d'annotations dans un fichier PDF, donc pour extraire les liens, extrayez tous les objets [LinkAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/linkannotation).

1. Créez un objet [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document).
1. Obtenez la [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page) à partir de laquelle vous souhaitez extraire les liens.
1. Utilisez la classe [AnnotationSelector](https://reference.aspose.com/pdf/java/com.aspose.pdf/annotationselector) pour extraire tous les objets [LinkAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/LinkAnnotation) de la page spécifiée.

1. Passez l'objet [AnnotationSelector](https://reference.aspose.com/pdf/java/com.aspose.pdf/annotationselector) à la méthode Accept de l'objet Page.
1. Obtenez toutes les annotations de lien sélectionnées dans un objet IList en utilisant la méthode [getSelected](https://reference.aspose.com/pdf/java/com.aspose.pdf/AnnotationSelector#getSelected--) de l'objet [AnnotationSelector](https://reference.aspose.com/pdf/java/com.aspose.pdf/annotationselector).

Le code suivant vous montre comment extraire des liens d'un fichier PDF.

```java
    public static void ExtractLinksFromThePDFFile() {        
        // Charger le fichier PDF
        Document document = new Document(_dataDir + "UpdateLinks.pdf");
        Page page = document.getPages().get_Item(1);
           
        AnnotationSelector selector = new AnnotationSelector(new LinkAnnotation(page, Rectangle.getTrivial()));
        page.accept(selector);
        java.util.List<Annotation> list = selector.getSelected();
        for(Annotation annot : list)
        {
            System.out.println("Annotation localisée : " + annot.getRect());
        }
                
        // Enregistrer le document avec le lien mis à jour
        //document.save(_dataDir + "ExtractLinks_out.pdf");
    }
```