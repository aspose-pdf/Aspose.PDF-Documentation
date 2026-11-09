---
title: Work with PDF artifacts in C++
linktitle: Working with Artifacts
type: docs
weight: 170
url: /cpp/artifacts/
description: Add, inspect, and remove PDF artifacts in C++, including backgrounds, watermarks, headers, footers, and Bates numbering.
lastmod: "2026-11-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Manage PDF Page Artifacts in C++
Abstract: Choose task guides for adding and removing PDF artifacts, reading watermark details, and counting pagination artifact subtypes. The examples use the native C++ artifact APIs.
---

PDF artifacts represent page elements such as decorative backgrounds, running headers and footers, and watermarks. In a tagged PDF, artifacts distinguish these elements from meaningful document content.

## Choose a guide

### Add artifacts

- [Add Backgrounds](/pdf/cpp/add-backgrounds/)
- [Add Watermarks](/pdf/cpp/add-watermarks/)
- [Add Bates Numbering](/pdf/cpp/add-bates-numbering/)
- [Add Headers and Footers](/pdf/cpp/artifacts-header-footer/)

### Inspect artifacts

- [Count Pagination Artifacts by Subtype](/pdf/cpp/counting-artifacts/)
- [Extract Watermark Details](/pdf/cpp/extract-watermarks/)

### Remove artifacts

- [Remove Backgrounds](/pdf/cpp/remove-backgrounds/)
- [Remove Watermarks](/pdf/cpp/remove-watermarks/)
- [Remove Bates Numbering](/pdf/cpp/remove-bates-numbering/)
- [Remove Headers and Footers](/pdf/cpp/remove-headers-footers/)

## Work with the artifact API

Use [Page::get_Artifacts()](https://reference.aspose.com/pdf/cpp/aspose.pdf/page/get_artifacts/) to access an [ArtifactCollection](https://reference.aspose.com/pdf/cpp/aspose.pdf/artifactcollection/). The [Artifact](https://reference.aspose.com/pdf/cpp/aspose.pdf/artifact/) base class provides common properties for [BackgroundArtifact](https://reference.aspose.com/pdf/cpp/aspose.pdf/backgroundartifact/), [WatermarkArtifact](https://reference.aspose.com/pdf/cpp/aspose.pdf/watermarkartifact/), [HeaderArtifact](https://reference.aspose.com/pdf/cpp/aspose.pdf/headerartifact/), [FooterArtifact](https://reference.aspose.com/pdf/cpp/aspose.pdf/footerartifact/), and [BatesNArtifact](https://reference.aspose.com/pdf/cpp/aspose.pdf/batesnartifact/).

| Task | API properties and methods |
| --- | --- |
| Classify an artifact | Inspect `get_Type()` and `get_Subtype()`. |
| Read watermark details | Use `get_Text()` and `get_Rectangle()`. |
| Configure text | Use `get_TextState()` or `SetTextAndState()`. |
| Configure placement | Set artifact alignment and margins. |
| Configure appearance | Set rotation and opacity; use `set_IsBackground(true)` for placement behind page content. |
| Add or delete an artifact | Call `ArtifactCollection::Add()` or `Delete()`. |

Most examples process the first page. Bates numbering uses the document page collection; both C++ addition examples also append two blank pages. Removal guides state the artifact classifications they delete.
