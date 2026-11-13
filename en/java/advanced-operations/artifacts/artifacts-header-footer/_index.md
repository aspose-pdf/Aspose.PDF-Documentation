---
title: Add PDF Headers and Footers in Java
linktitle: Add Headers and Footers
type: docs
weight: 70
url: /java/artifacts-header-footer/
description: Create styled header and footer artifacts and add them to PDF pages in Java.
lastmod: "2026-11-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Add Headers and Footers in Java
Abstract: Create styled header and footer artifacts and add them to PDF pages in Java.
---
Header and footer artifacts are non-content pagination elements commonly used for repeated labels, page identifiers, and layout framing.

## Create a header artifact

Use this helper when you need a reusable header artifact with consistent text styling and alignment.

1. Create a [HeaderArtifact](https://reference.aspose.com/pdf/java/com.aspose.pdf/headerartifact/).
1. Set its text, font settings, and foreground color.
1. Configure the horizontal alignment and return the artifact.

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

## Create a footer artifact

This helper creates a reusable footer artifact with the same styling pattern as the header artifact.

1. Create a [FooterArtifact](https://reference.aspose.com/pdf/java/com.aspose.pdf/footerartifact/).
1. Set its text, text state, and foreground color.
1. Configure the alignment and return the artifact.

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

## Add a header artifact

Use this example when a page should display a reusable header artifact.

1. Open the source PDF [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Create the header artifact through the helper method.
1. Add the artifact to the page and save the output file.

```java
public static void addHeaderArtifact(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        HeaderArtifact header = createHeaderArtifact("Sample Header");
        document.getPages().get_Item(1).getArtifacts().add(header);
        document.save(outputFile.toString());
    }
}
```

## Add a footer artifact

Use this example when the page should display a footer artifact with reusable formatting.

1. Open the source PDF [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Create the footer artifact through the helper method.
1. Add the artifact to the page and save the output file.

```java
public static void addFooterArtifact(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        FooterArtifact footer = createFooterArtifact("Sample Footer");
        document.getPages().get_Item(1).getArtifacts().add(footer);
        document.save(outputFile.toString());
    }
}
```

## Related artifact topics

- [Remove Headers and Footers](/pdf/java/remove-headers-footers/)
- [Work with PDF Artifacts in Java](/pdf/java/artifacts/)
