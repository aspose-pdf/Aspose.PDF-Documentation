---
title: Import JSON Data
type: docs
weight: 30
url: /java/import-json-data/
description: Review the current Java support status for importing PDF form data from JSON with Aspose.PDF Facades.
lastmod: "2026-05-28"
TechArticle: true
AlternativeHeadline: JSON import status for the Form facade in Java
Abstract: The current Java example set in this repository does not include a dedicated Form facade sample for importing PDF form data directly from JSON. This page records that scope explicitly and points to the supported XML, FDF, and XFDF import workflows instead.
---
The current `FormExamples.java` source file does not contain a dedicated `importJson(...)` example.

Supported Java import workflows in this section are:

- `importXml(...)`
- `importFdf(...)`
- `importXfdf(...)`

If your application stores form data as JSON, deserialize it first and then either:

- map the values to repeated `fillField(...)` calls
- convert the payload into one of the supported import formats in your own code
