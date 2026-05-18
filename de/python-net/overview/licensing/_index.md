---
title: Aspose PDF-Lizenz
linktitle: Lizenzierung und Einschränkungen
type: docs
weight: 50
url: /de/python-net/licensing/
description: Aspose.PDF für Python lädt seine Kunden ein, eine Classic-Lizenz zu erwerben. Außerdem kann eine eingeschränkte Lizenz verwendet werden, um das Produkt besser zu erkunden.
lastmod: "2026-05-18"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Lizenzierung von Aspose.PDF für Python
Abstract: Der Artikel behandelt die Einschränkungen und Lizenzierungsoptionen für Aspose.PDF für Python. Er weist darauf hin, dass die Evaluierungsversion das Testen der vollen Funktionalität ermöglicht, jedoch ein Wasserzeichen in den erzeugten PDFs hinzufügt, das "Evaluation Only" zusammen mit Copyright-Informationen anzeigt. Für Benutzer, die ohne diese Einschränkungen testen möchten, steht eine 30-tägige temporäre Lizenz zur Verfügung. Der Artikel erklärt außerdem, wie eine Classic-Lizenz implementiert werden kann, indem sie aus einer Datei oder einem Stream geladen wird. Es wird empfohlen, die Lizenzdatei im selben Verzeichnis wie die Aspose.PDF.dll abzulegen und die Lizenz über die `Aspose.Pdf.License`‑Klasse festzulegen. Code‑Snippets werden bereitgestellt, um den Lizenzierungsprozess zu veranschaulichen.
---

## Einschränkung einer Evaluierungsversion

Wir möchten, dass unsere Kunden unsere Komponenten gründlich testen, bevor sie kaufen, deshalb ermöglicht die Evaluierungsversion, sie wie gewohnt zu verwenden.

- **PDF erstellt mit einem Evaluierungswasserzeichen.** Die Evaluierungsversion von Aspose.PDF for Python bietet die volle Produktfunktionalität, jedoch werden alle Seiten in den erzeugten PDF-Dokumenten mit "Evaluation Only. Created with Aspose.PDF. Copyright 2002-2020 Aspose Pty Ltd" oben versehen.

>Wenn Sie Aspose.PDF ohne die Einschränkungen der Evaluierungsversion testen möchten, können Sie auch eine 30‑tägige temporäre Lizenz anfordern. Bitte beachten Sie [Wie erhält man eine temporäre Lizenz?](https://purchase.aspose.com/temporary-license)

## Klassische Lizenz

Die Lizenz kann aus einer Datei oder einem Stream‑Objekt geladen werden. Der einfachste Weg, eine Lizenz zu setzen, besteht darin, die Lizenzdatei in denselben Ordner wie die Aspose.PDF.dll‑Datei zu legen und den Dateinamen ohne Pfad anzugeben, wie im nachstehenden Beispiel gezeigt.

Wenn Sie ein anderes Aspose‑für‑Python‑Komponente zusammen mit Aspose.PDF für Python verwenden, geben Sie bitte den Namespace für die Lizenz wie folgt an [Aspose.Pdf.License-Klasse]().

```python

    license_file = LICENSE_FILE
    license = ap.License()
    license.set_license(license_file)
```
