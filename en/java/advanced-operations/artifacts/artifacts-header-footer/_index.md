---
title: Manage PDF Headers and Footers using Java
linktitle: Manage PDF Headers and Footers
type: docs
weight: 70
url: /java/artifacts-header-footer/
description: Learn how to add and remove header and footer artifacts in PDF documents using Aspose.PDF for Java.
lastmod: "2026-05-27"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: How to Add, Customize, and Remove PDF Headers and Footers Using Java
Abstract: This article explains how to manage header and footer artifacts in PDF documents using Aspose.PDF for Java. It covers creating reusable `HeaderArtifact` and `FooterArtifact` objects with custom text state and alignment, adding them to a page, and deleting existing header and footer artifacts.
---
## Create reusable header and footer artifacts

1. Initialize the PDF document and any resources required by this example.
2. Build and configure the Aspose.PDF objects needed to create reusable header and footer artifacts.
3. Save the output document or generated file.

```java
public static HeaderArtifact createHeaderArtifact(String text) {
    HeaderArtifact artifact = new HeaderArtifact();
    artifact.setText(text);
    artifact.getTextState().setFontSize(14);
    artifact.getTextState().setFont(FontRepository.findFont("Arial"));
    artifact.getTextState().setForegroundColor(Color.getNavy());
    artifact.setArtifactHorizontalAlignment(HorizontalAlignment.Center);
    return artifact;
}
```

```java
public static FooterArtifact createFooterArtifact(String text) {
    FooterArtifact artifact = new FooterArtifact();
    artifact.setText(text);
    artifact.getTextState().setFontSize(14);
    artifact.getTextState().setFont(FontRepository.findFont("Arial"));
    artifact.getTextState().setForegroundColor(Color.getNavy());
    artifact.setArtifactHorizontalAlignment(HorizontalAlignment.Center);
    return artifact;
}
```


