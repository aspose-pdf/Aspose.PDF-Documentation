---
title: Export to JSON
type: docs
weight: 30
url: /java/export-to-json/
description: Review the current Java support status for exporting PDF form data to JSON with Aspose.PDF Facades.
lastmod: "2026-05-28"
TechArticle: true
AlternativeHeadline: JSON export status for the Form facade in Java
Abstract: The current Java example set in this repository does not include a dedicated Form facade sample for exporting PDF form data directly to JSON. This page records that scope explicitly and points to the supported XML, FDF, XFDF, and field-inspection examples instead.
---
The current `en/java/src/main/java/com/aspose/pdf/examples/facades/form/FormExamples.java` file does not contain a dedicated `exportJson(...)` example.

Supported Java export workflows in this section are:

- `exportXml(...)`
- `exportFdf(...)`
- `exportXfdf(...)`

If you need JSON output in Java, use one of the supported export formats or inspect field names and values with `inspectFormFields(...)`, then map that data to your own JSON serializer in application code.
