---
title: Set Submit Flag
type: docs
weight: 40
url: /java/set-submit-flag/
description: Review the current Java coverage for setting a submit flag on a PDF form button with the FormEditor facade in Aspose.PDF.
lastmod: "2026-06-09"
TechArticle: true
AlternativeHeadline: Submit flag configuration in Java FormEditor examples
Abstract: The current Java sample set does not expose submit-flag configuration as a separate standalone example method. Instead, it is demonstrated together with submit URL configuration in `setSubmitUrl(...)`.
---
The Java `FormEditorExamples.setSubmitUrl(...)` method includes:

## Configure a submit flag

1. Bind the source PDF to the `FormEditor` facade.
2. Set the submit URL for the button field.
3. Set the submit flag for the required format.
4. Save the updated document.

```java
editor.setSubmitUrl("Script_Demo_Button", "http://www.example.com/submit");
editor.setSubmitFlag("Script_Demo_Button", SubmitFormFlag.Xfdf);
```

Use that combined example as the source-backed Java workflow for configuring a submit flag in this repository.
