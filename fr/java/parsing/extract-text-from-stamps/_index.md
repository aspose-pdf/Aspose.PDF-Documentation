---
title: Extraire le Texte des Tampons
type: docs
weight: 60
url: /fr/java/extract-text-from-stamps/
---

## Extraire le Texte des Annotations de Tampon

Aspose.PDF pour Java vous permet d'extraire du texte à partir des annotations de tampon. Afin d'extraire du texte des annotations de tampon dans un PDF, les étapes suivantes peuvent être utilisées.

1. Créer un objet de la classe Document
1. Obtenir l'annotation souhaitée de la liste des annotations d'une page
1. Définir un nouvel objet de la classe TextAbsorber
1. Utiliser la méthode visit de TextAbsorber pour obtenir le texte

```java
Document doc = new Document(dataDir+"test.pdf");
Annotation item = doc.getPages().get_Item(1).getAnnotations().get_Item(3);
if (item instanceof StampAnnotation ) {
   StampAnnotation annot = (StampAnnotation) item;
   TextAbsorber ta = new TextAbsorber();
   XForm ap = annot.getNormalAppearance();
   ta.visit(ap);
   System.out.println(ta.getText());
}
```