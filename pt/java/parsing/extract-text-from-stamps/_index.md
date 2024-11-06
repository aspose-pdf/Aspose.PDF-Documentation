---
title: Extrair Texto de Selos
type: docs
weight: 60
url: pt/java/extract-text-from-stamps/
---

## Extrair Texto de Anotações de Selo

Aspose.PDF para Java permite que você extraia texto de anotações de selo. Para extrair texto de Anotações de Selo em um PDF, os seguintes passos podem ser usados.

1. Crie um objeto da classe Document
1. Obtenha a Anotação desejada da lista de anotações de uma página
1. Defina um novo objeto da classe TextAbsorber
1. Use o método visit do TextAbsorber para obter o Texto

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