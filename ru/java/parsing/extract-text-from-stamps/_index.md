---
title: Извлечение текста из штампов
type: docs
weight: 60
url: /ru/java/extract-text-from-stamps/
---

## Извлечение текста из аннотаций штампа

Aspose.PDF для Java позволяет извлекать текст из аннотаций штампа. Чтобы извлечь текст из аннотаций штампа в PDF, можно использовать следующие шаги.

1. Создайте объект класса Document
1. Получите нужную аннотацию из списка аннотаций страницы
1. Определите новый объект класса TextAbsorber
1. Используйте метод visit класса TextAbsorber, чтобы получить текст

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