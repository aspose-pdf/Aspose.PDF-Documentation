---
title: Work with PDF Artifacts in Python
linktitle: Working with Artifacts
type: docs
weight: 170
url: /python-net/artifacts/
description: Learn how to work with PDF artifacts in Python to add backgrounds, watermarks, and Bates numbering and count artifact types with Aspose.PDF for Python via .NET.
lastmod: "2026-04-15"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true 
AlternativeHeadline: Add backgrounds, watermarks, and Bates numbering artifacts in Python
Abstract: This article explains how to work with PDF artifacts in Aspose.PDF for Python via .NET. Learn what artifacts are, why they matter for accessibility and document layout, and how to add background images, apply watermarks, add Bates numbering, and inspect artifact types in PDF files with Python.
---

Artifacts in PDF are graphics objects or other elements that are not part of the actual content of the document. They are usually used for decoration, layout, or background purposes. Examples of artifacts include page headers, footers, separators, or images that do not convey any meaning.

The purpose of artifacts in PDF is to allow the distinction between content and non-content elements. This is important for accessibility, as screen readers and other assistive technologies can ignore artifacts and focus on the relevant content. Artifacts can also improve the performance and quality of PDF documents, as they can be omitted from printing, searching, or copying.

Use this section when you need to create or inspect non-content PDF elements in Python, such as document backgrounds, page watermarks, and Bates numbering marks. The following guides show the main artifact workflows supported by Aspose.PDF for Python via .NET.

To create an element as an artifact in PDF, you need to use the [Artifact](https://reference.aspose.com/pdf/python-net/aspose.pdf/artifact/) class.
It contains following useful properties:

- **custom_type** - Gets name of artifact type. May be used if artifact type is non standard.
- **custom_subtype** - Gets name of artifact subtype. May be used if artifact subtype is not standard subtype.
- **type** - Gets artifact type.
- **subtype** - Gets artifact subtype. If artifact has non-standard subtype, name of the subtype may be read via CustomSubtype.
- **contents** - Gets collection of artifact internal operators.
- **form** - Gets XForm of the artifact (if XForm is used).
- **rectangle** - Gets rectangle of the artifact.
- **position** - Gets or sets artifact position. If this property is specified, then margins and alignments are ignored.
- **right_margin** - Right margin of artifact.If position is specified explicitly (in Position property) this value is ignored.
- **left_margin** - Left margin of artifact.If position is specified explicitly (in Position property) this value is ignored.
- **top_margin** - Top margin of artifact. If position is specified explicitly (in Position property) this value is ignored.
- **bottom_margin** - Bottom margin of artifact.If position is specified explicitly (in Position property) this value is ignored.
- **artifact_horizontal_alignment** - Horizontal alignment of artifact. If position is specified explicitly (in Position property) this value is ignored.
- **artifact_vertical_alignment** - Vertical alignment of artifact. If position is specified explicitly (in Position property) this value is ignored.
- **rotation** - Gets or sets artifact rotation angle.
- **text** - Gets text of the artifact.
- **image** - Gets image of the artifact (if presents).
- **opacity** - Gets or sets opacity of the artifact. Possible values are in range 0..1.
- **lines** - Lines of multiline text artifact.
- **text_state** - Text state for artifact text.
- **is_background** - If true Artifact is placed behind page contents.

The following classes may also be useful for work with artifacts:

- [ArtifactCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/artifactcollection/)
- [BackgroundArtifact](https://reference.aspose.com/pdf/python-net/aspose.pdf/backgroundartifact/)
- [HeaderArtifact](https://reference.aspose.com/pdf/python-net/aspose.pdf/headerartifact/)
- [FooterArtifact](https://reference.aspose.com/pdf/python-net/aspose.pdf/footerartifact/)
- [WatermarkArtifact](https://reference.aspose.com/pdf/python-net/aspose.pdf/watermarkartifact/)
- [BatesNArtifact](https://reference.aspose.com/pdf/python-net/aspose.pdf/batesnartifact/)

## Artifact Workflows Covered in This Section

Please review the following sections of the article:

- [Adding backgrounds](/pdf/python-net/add-backgrounds/) - add background image to your PDF file with Python.
- [Adding Bates Numbering](/pdf/python-net/add-bates-numbering/) - add Bates Numbering to PDF.
- [Adding Watermark](/pdf/python-net/add-watermarks/) - how to add watermark to PDF with Python.
- [Counting Artifacts](/pdf/python-net/counting-artifacts/) - counting Artifacts in PDF using Python.
- [Manage PDF Headers and Footers](/pdf/python-net/artifacts-header-footer/) - manage headers and footers in PDF documents.
