---
title: Get Radio Button Options
type: docs
weight: 20
url: /java/get-radio-button-options/
description: Review the current Java support status for reading radio button options with Aspose.PDF Facades.
lastmod: "2026-05-28"
TechArticle: true
AlternativeHeadline: Radio button option inspection status in Java
Abstract: The current Java example set in this repository does not include a dedicated Form facade sample for enumerating radio button options or reading the selected option separately. This page records that scope explicitly and points to the supported general field inspection example.
---
The current `FormExamples.java` source file includes a write example for radio buttons:

```java
form.fillField("gender", 0);
```

It does not include a dedicated Java sample for enumerating available radio button options or reading the selected radio value independently of the general field inspection workflow. Use `inspectFormFields(...)` for the supported Java read path that exists in this repository today.
