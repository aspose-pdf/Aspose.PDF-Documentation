---
title: Fill Fields by Name and Value
type: docs
weight: 60
url: /java/fill-fields-by-name-and-value/
description: Learn how to adapt the Form facade field-filling API in Java for dynamic name-value form updates.
lastmod: "2026-05-28"
TechArticle: true
AlternativeHeadline: Fill multiple PDF form fields from name-value pairs in Java
Abstract: The current Java sample set fills fields individually with repeated `fillField(...)` calls. This article shows how to apply the same API pattern to your own name-value collection without inventing a separate facade feature that is not present in the repository examples.
---
The Java `FormExamples` class fills individual fields directly:

```java
form.fillField("name", "John Doe");
form.fillField("address", "123 Main St, Anytown, USA");
form.fillField("email", "john.doe@example.com");
```

If your application already has a dynamic set of field names and values, apply the same `fillField(...)` call inside your own loop:

```java
for (Map.Entry<String, String> entry : values.entrySet()) {
    form.fillField(entry.getKey(), entry.getValue());
}
```

This is an application-level pattern derived from the same Java API used in `FormExamples.fillTextFields(...)`; the current repository does not include a separate dedicated helper method for map-based filling.
