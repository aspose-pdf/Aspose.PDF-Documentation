---
title: Rellenar campos por nombre y valor
linktitle: Rellenar campos por nombre y valor
type: docs
weight: 60
url: /es/java/fill-fields-by-name-and-value/
description: Aprenda cómo adaptar la API de relleno de campos de la fachada Form en Java para actualizaciones dinámicas de formularios con pares nombre‑valor.
lastmod: "2026-09-29"
TechArticle: true
AlternativeHeadline: Rellenar varios campos de formulario PDF a partir de pares nombre‑valor en Java
Abstract: El conjunto de ejemplos actual de Java rellena los campos individualmente con llamadas repetidas a `fillField(...)`. Este artículo muestra cómo aplicar el mismo patrón de API a su propia colección de nombre‑valor sin inventar una característica de fachada separada que no está presente en los ejemplos del repositorio.
---
El Java `FormExamples` la clase llena los campos individuales directamente:

```java
form.fillField("name", "John Doe");
form.fillField("address", "123 Main St, Anytown, USA");
form.fillField("email", "john.doe@example.com");
```

Si su aplicación ya tiene un conjunto dinámico de nombres de campo y valores, aplique lo mismo `fillField(...)` llamada dentro de su propio bucle:

```java
for (Map.Entry<String, String> entry : values.entrySet()) {
    form.fillField(entry.getKey(), entry.getValue());
}
```

Este es un patrón a nivel de aplicación derivado de la misma API de Java utilizada en `FormExamples.fillTextFields(...)`; el repositorio actual no incluye un método auxiliar dedicado separado para el llenado basado en mapas.
