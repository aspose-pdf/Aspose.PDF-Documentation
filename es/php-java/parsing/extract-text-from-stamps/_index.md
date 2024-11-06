---
title: Extraer Texto De Estampillas
type: docs
weight: 60
url: es/php-java/extract-text-from-stamps/
---

## Extraer Texto de Anotaciones de Estampillas

Aspose.PDF para PHP a través de Java te permite extraer texto de anotaciones de estampillas. Para extraer texto de Anotaciones de Estampillas en un PDF, se pueden usar los siguientes pasos.

1. Cargar el documento PDF
1. Obtener la página deseada del documento
1. Crear una nueva instancia de la clase StampAnnotation
1. Crear una nueva instancia de la clase AnnotationSelector y pasar la anotación de estampilla a ella
1. Aceptar el selector de anotaciones en la página
1. Obtener las anotaciones de estampilla seleccionadas
1. Crear una nueva instancia de la clase TextAbsorber
1. Obtener la primera anotación de estampilla
1. Obtener la apariencia normal de la anotación de estampilla
1. Visitar la apariencia usando el absorbedor de texto
1. Obtener el texto extraído del absorbedor de texto
1. Cerrar el documento

```php
    $responseData = "";
    $document = new Document($inputFile);
    $page = $document->getPages()->get_Item(1);
    $stampAnnotation = new StampAnnotation($document);
    $annotationSelector = new AnnotationSelector($stampAnnotation);
    $page->accept($annotationSelector);
    $stampAnnotations = $annotationSelector->getSelected();
    $textAbsorber = new TextAbsorber();
    $stampAnnotation = $stampAnnotations->get(0);    
    $appearance = $stampAnnotation->getNormalAppearance();
    $textAbsorber->visit($appearance);
    $responseData = java_values($textAbsorber->getText());       
    $document->close();
```