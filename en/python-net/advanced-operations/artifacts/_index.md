---
title: Work with PDF Artifacts in Python
linktitle: Working with Artifacts
type: docs
weight: 170
url: /python-net/artifacts/
description: Add, inspect, and remove PDF artifacts in Python, including backgrounds, watermarks, headers, footers, and Bates numbering.
lastmod: "2026-11-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Manage PDF page artifacts in Python
Abstract: Find guides for adding and removing PDF artifacts, inspecting watermark details, and counting pagination artifacts by subtype with Aspose.PDF for Python via .NET.
---

PDF artifacts mark page elements such as decorative backgrounds, running headers and footers, and watermarks. In a tagged PDF, assistive technologies can skip artifacts and focus on the document's meaningful content.

## Choose a guide

### Add artifacts

- [Add Backgrounds](/pdf/python-net/add-backgrounds/)
- [Add Watermarks](/pdf/python-net/add-watermarks/)
- [Add Bates Numbering](/pdf/python-net/add-bates-numbering/)
- [Add Headers and Footers](/pdf/python-net/artifacts-header-footer/)

### Inspect artifacts

- [Count Pagination Artifacts by Subtype](/pdf/python-net/counting-artifacts/)
- [Extract Watermark Details](/pdf/python-net/extract-watermarks/)

### Remove artifacts

- [Remove Backgrounds](/pdf/python-net/remove-backgrounds/)
- [Remove Watermarks](/pdf/python-net/remove-watermarks/)
- [Remove Bates Numbering](/pdf/python-net/remove-bates-numbering/)
- [Remove Headers and Footers](/pdf/python-net/remove-headers-footers/)

## Work with the artifact API

Access a page's artifacts through its `artifacts` property, which returns an [`ArtifactCollection`](https://reference.aspose.com/pdf/python-net/aspose.pdf/artifactcollection/). The [`Artifact`](https://reference.aspose.com/pdf/python-net/aspose.pdf/artifact/) class provides the properties shared by specialized classes such as [`BackgroundArtifact`](https://reference.aspose.com/pdf/python-net/aspose.pdf/backgroundartifact/), [`WatermarkArtifact`](https://reference.aspose.com/pdf/python-net/aspose.pdf/watermarkartifact/), [`HeaderArtifact`](https://reference.aspose.com/pdf/python-net/aspose.pdf/headerartifact/), [`FooterArtifact`](https://reference.aspose.com/pdf/python-net/aspose.pdf/footerartifact/), and [`BatesNArtifact`](https://reference.aspose.com/pdf/python-net/aspose.pdf/batesnartifact/).

| Task | Properties |
| --- | --- |
| Identify the artifact | Use `type` and `subtype` for standard classifications and `custom_type` and `custom_subtype` for custom names. |
| Inspect its content | Use `text`, `image`, and `lines` for text and images, or `contents` and `form` for PDF operators and the associated XForm. |
| Position it on the page | Use `rectangle` to inspect its bounds. Set `position` for explicit placement or use `left_margin`, `right_margin`, `top_margin`, `bottom_margin`, `artifact_horizontal_alignment`, and `artifact_vertical_alignment`. An explicit position overrides margins and alignment. |
| Control its appearance | Use `rotation`, `opacity` (from 0 to 1), and `text_state`. Set `is_background` to place the artifact behind page content. |
