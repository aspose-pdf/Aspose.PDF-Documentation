---
title: Arbeiten mit PDF-Artefakten in Python
linktitle: Arbeiten mit Artefakten
type: docs
weight: 170
url: /de/python-net/artifacts/
description: Erfahren Sie, wie Sie in Python mit PDF-Artefakten arbeiten, um Hintergründe, Wasserzeichen und Bates‑Nummerierung hinzuzufügen und Artefakttypen zu zählen, mithilfe von Aspose.PDF for Python via .NET.
lastmod: "2026-05-18"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Hintergründe, Wasserzeichen und Bates‑Nummerierungs‑Artefakte in Python hinzufügen
Abstract: Dieser Artikel erklärt, wie man mit PDF-Artefakten in Aspose.PDF for Python via .NET arbeitet. Erfahren Sie, was Artefakte sind, warum sie für Barrierefreiheit und Dokumentlayout wichtig sind und wie man Hintergrundbilder hinzufügt, Wasserzeichen anwendet, Bates‑Nummerierung hinzufügt und Artefakttypen in PDF-Dateien mit Python prüft.
---

Artefakte in PDF sind Grafikobjekte oder andere Elemente, die nicht Teil des eigentlichen Inhalts des Dokuments sind. Sie werden normalerweise für Dekoration, Layout oder Hintergrundzwecke verwendet. Beispiele für Artefakte sind Seitenkopfzeilen, Fußzeilen, Trennlinien oder Bilder, die keine Bedeutung vermitteln.

Der Zweck von Artefakten in PDF besteht darin, die Unterscheidung zwischen Inhalts- und Nicht-Inhaltselementen zu ermöglichen. Dies ist wichtig für die Barrierefreiheit, da Bildschirmleser und andere unterstützende Technologien Artefakte ignorieren und sich auf den relevanten Inhalt konzentrieren können. Artefakte können auch die Leistung und Qualität von PDF-Dokumenten verbessern, da sie beim Drucken, Suchen oder Kopieren weggelassen werden können.

Verwenden Sie diesen Abschnitt, wenn Sie Nicht-Inhalt-PDF-Elemente in Python erstellen oder untersuchen müssen, beispielsweise Dokumenthintergründe, Seitenwasserzeichen und Bates-Nummerierungsmarken. Die folgenden Anleitungen zeigen die wichtigsten Artefakt-Workflows, die von Aspose.PDF for Python via .NET unterstützt werden.

Um ein Element in PDF als Artefakt zu erstellen, müssen Sie das [Artefakt](https://reference.aspose.com/pdf/python-net/aspose.pdf/artifact/) Klasse.
Es enthält die folgenden nützlichen Eigenschaften:

- **custom_type** – Gibt den Namen des Artefakttyps zurück. Kann verwendet werden, wenn der Artefakttyp nicht standardmäßig ist.
- **custom_subtype** - Gibt den Namen des Artefakt-Subtyps zurück. Kann verwendet werden, wenn der Artefakt-Subtyp kein Standard-Subtyp ist.
- **type** - Gibt den Artefakt‑Typ zurück.
- **subtype** - Gibt den Artefakt-Subtyp zurück. Wenn das Artefakt einen nicht‑standardmäßigen Subtyp hat, kann der Name des Subtyps über CustomSubtype ausgelesen werden.
- **contents** - Gibt die Sammlung der internen Operatoren des Artefakts zurück.
- **form** - Gibt das XForm des Artefakts zurück (falls XForm verwendet wird).
- **rectangle** - Gibt das Rechteck des Artefakts zurück.
- **position** - Ruft die Position des Artefakts ab oder legt sie fest. Wenn diese Eigenschaft angegeben ist, werden Ränder und Ausrichtungen ignoriert.
- **right_margin** - Rechter Rand des Artefakts. Wenn die Position explizit angegeben ist (in der Position‑Eigenschaft), wird dieser Wert ignoriert.
- **left_margin** - Linker Rand des Artefakts. Wenn die Position explizit angegeben ist (in der Position‑Eigenschaft), wird dieser Wert ignoriert.
- **top_margin** - Oberer Rand des Artefakts. Wenn die Position explizit angegeben ist (in der Position‑Eigenschaft), wird dieser Wert ignoriert.
- **bottom_margin** - Unterer Rand des Artefakts. Wenn die Position explizit angegeben ist (in der Position‑Eigenschaft), wird dieser Wert ignoriert.
- **artifact_horizontal_alignment** - Horizontale Ausrichtung des Artefakts. Wenn die Position explizit angegeben ist (in der Position‑Eigenschaft), wird dieser Wert ignoriert.
- **artifact_vertical_alignment** - Vertikale Ausrichtung des Artefakts. Wenn die Position explizit angegeben ist (in der Position-Eigenschaft), wird dieser Wert ignoriert.
- **rotation** - Liest oder setzt den Rotationswinkel des Artefakts.
- **text** - Liest den Text des Artefakts.
- **image** - Liest das Bild des Artefakts (falls vorhanden).
- **opacity** - Liest oder setzt die Deckkraft des Artefakts. Mögliche Werte liegen im Bereich 0..1.
- **lines** - Zeilen des mehrzeiligen Textartefakts.
- **text_state** - Textzustand für Artefakt-Text.
- **is_background** - Wenn true, wird das Artefakt hinter den Seiteninhalten platziert.

Die folgenden Klassen können ebenfalls bei der Arbeit mit Artefakten nützlich sein:

- [ArtifactCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/artifactcollection/)
- [BackgroundArtifact](https://reference.aspose.com/pdf/python-net/aspose.pdf/backgroundartifact/)
- [HeaderArtifact](https://reference.aspose.com/pdf/python-net/aspose.pdf/headerartifact/)
- [FooterArtifact](https://reference.aspose.com/pdf/python-net/aspose.pdf/footerartifact/)
- [WatermarkArtifact](https://reference.aspose.com/pdf/python-net/aspose.pdf/watermarkartifact/)
- [BatesNArtifact](https://reference.aspose.com/pdf/python-net/aspose.pdf/batesnartifact/)

## In diesem Abschnitt behandelte Artifact-Workflows

Bitte überprüfen Sie die folgenden Abschnitte des Artikels:

- [Hintergründe hinzufügen](/pdf/de/python-net/add-backgrounds/) - fügen Sie Ihrem PDF-Dokument ein Hintergrundbild mit Python hinzu.
- [Bates-Nummerierung hinzufügen](/pdf/de/python-net/add-bates-numbering/) - fügen Sie dem PDF Bates-Nummerierung hinzu.
- [Wasserzeichen hinzufügen](/pdf/de/python-net/add-watermarks/) - Wie man ein Wasserzeichen zu einem PDF mit Python hinzufügt.
- [Artefakte zählen](/pdf/de/python-net/counting-artifacts/) - Zählen von Artefakten in PDF mit Python.
- [PDF-Kopf- und Fußzeilen verwalten](/pdf/de/python-net/artifacts-header-footer/) - Verwalten von Headern und Fußzeilen in PDF-Dokumenten.

Diese Tutorials sind nützlich, wenn Sie dekorative oder strukturelle PDF-Elemente verwalten müssen, ohne den Hauptinhalt des Dokuments zu ändern.
