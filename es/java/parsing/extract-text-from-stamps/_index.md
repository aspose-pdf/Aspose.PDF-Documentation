---
title: Extraer Texto de Sellos
type: docs
weight: 60
url: es/java/extract-text-from-stamps/
---

## Extraer Texto de Anotaciones de Sello

Aspose.PDF para Java te permite extraer texto de anotaciones de sello. Para extraer texto de las Anotaciones de Sello en un PDF, se pueden usar los siguientes pasos.

1. Crear un objeto de la clase Document
1. Obtener la Anotación deseada de la lista de anotaciones de una página
1. Definir un nuevo objeto de la clase TextAbsorber
1. Usar el método visit del TextAbsorber para obtener el Texto

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