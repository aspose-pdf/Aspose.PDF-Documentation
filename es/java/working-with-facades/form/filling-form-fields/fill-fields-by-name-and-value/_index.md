---
title: Completar campos por nombre y valor
linktitle: Completar campos por nombre y valor
type: docs
weight: 60
url: /java/fill-fields-by-name-and-value/
description: Aprenda cómo adaptar la API de llenado de campos de fachada de formulario en Java para actualizaciones dinámicas de formularios de nombre-valor.
lastmod: "2026-06-09"
TechArticle: true
AlternativeHeadline: Complete varios campos de formulario PDF a partir de pares de nombre-valor en Java
Abstract: El conjunto de muestra de Java actual llena los campos individualmente con llamadas `fillField(...)` repetidas. Este artículo muestra cómo aplicar el mismo patrón API a su propia colección de nombre-valor sin inventar una característica de fachada separada que no está presente en los ejemplos del repositorio.
---
La clase Java `FormExamples` llena campos individuales directamente:


```java
form.fillField("name", "John Doe");
form.fillField("address", "123 Main St, Anytown, USA");
form.fillField("email", "john.doe@example.com");
```


Si su aplicación ya tiene un conjunto dinámico de nombres y valores de campos, aplique la misma llamada `fillField(...)` dentro de su propio bucle:


```java
for (Map.Entry<String, String> entry : values.entrySet()) {
    form.fillField(entry.getKey(), entry.getValue());
}
```


Este es un patrón a nivel de aplicación derivado de la misma API de Java utilizada en `FormExamples.fillTextFields(...)`; El repositorio actual no incluye un método auxiliar dedicado independiente para el llenado basado en mapas.
