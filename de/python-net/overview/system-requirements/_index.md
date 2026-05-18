---
title: Systemanforderungen
linktitle: Systemanforderungen
type: docs
weight: 30
url: /de/python-net/system-requirements/
description: Dieser Abschnitt listet die unterstützten Betriebssysteme auf, die ein Entwickler benötigt, um erfolgreich mit Aspose.PDF für Python zu arbeiten.
lastmod: "2026-05-18"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Unterstützte Betriebssysteme von Aspose.PDF für Python via .NET
Abstract: Aspose.PDF for Python via .NET ist eine PDF-Verarbeitungs-API, die für Entwickler entwickelt wurde, um PDF‑Dokumente zu verwalten, ohne dass Microsoft Office oder Adobe Acrobat Automation erforderlich sind. Sie unterstützt die Entwicklung von 32‑Bit‑ und 64‑Bit‑Python‑Anwendungen auf verschiedenen Betriebssystemen, einschließlich Windows und Linux, wobei Python 3.5 oder höher installiert ist. Die API ist kompatibel mit mehreren Windows-Versionen, von Windows XP bis Windows 11, sowie den wichtigsten Linux‑Distributionen wie Ubuntu, OpenSUSE und CentOS. Für Linux‑Systeme umfassen die spezifischen Anforderungen GCC‑6 Laufzeitbibliotheken, Abhängigkeiten des .NET Core Runtime (ohne dass das Runtime selbst benötigt wird) und den pymalloc‑Build von Python für die Versionen 3.5‑3.7. Zusätzlich ist eine gemeinsam genutzte libpython‑Bibliothek erforderlich, die möglicherweise Anpassungen in der Konfiguration erfordert, damit der Bibliothekspfad korrekt erkannt wird.
---

## Übersicht

Aspose.PDF for Python via .NET, PDF-Verarbeitungs-API, die es Entwicklern ermöglicht, mit PDF-Dokumenten zu arbeiten, ohne Microsoft Office® oder Adobe Acrobat Automation zu benötigen. Aspose.PDF for Python kann verwendet werden, um 32‑Bit‑ und 64‑Bit‑Python‑Anwendungen für verschiedene Betriebssysteme (wie Windows und Linux) zu entwickeln, bei denen Python 3.5 oder höher installiert ist.

## Unterstütztes Betriebssystem

### Windows

- Windows 2003 Server
- Windows 2008 Server
- Windows 2012 Server
- Windows Server 2012 R2
- Windows Server 2016
- Windows Server 2019
- Windows XP
- Windows Vista
- Windows 7
- Windows 8, 8.1
- Windows 10
- Windows 11

### Linux

- Ubuntu
- OpenSUSE
- CentOS
- und andere

## Systemanforderungen für Ziel-Linux

- GCC-6 Laufzeitbibliotheken (oder neuer).

- Abhängigkeiten der .NET Core Runtime. Die Installation der .NET Core Runtime selbst ist NICHT erforderlich.

- Für Python 3.5-3.7: Der pymalloc-Build von Python ist erforderlich. Die Build-Option --with-pymalloc für Python ist standardmäßig aktiviert. Typischerweise ist der pymalloc-Build von Python im Dateinamen mit dem Suffix m gekennzeichnet.

- libpython gemeinsam genutzte Python-Bibliothek. Die Build-Option --enable-shared für Python ist standardmäßig deaktiviert, einige Python-Distributionen enthalten die libpython gemeinsam genutzte Bibliothek nicht. Für einige Linux-Plattformen kann die libpython gemeinsam genutzte Bibliothek über den Paketmanager installiert werden, zum Beispiel: sudo apt-get install libpython3.7. Das häufige Problem ist, dass die libpython-Bibliothek an einem anderen Ort als dem standardmäßigen Systemstandort für gemeinsam genutzte Bibliotheken installiert ist. Das Problem kann behoben werden, indem man die Python-Build-Optionen verwendet, um beim Kompilieren von Python alternative Bibliothekspfade festzulegen, oder indem man einen symbolischen Link zur libpython-Bibliotheksdatei im standardmäßigen Systemstandort für gemeinsam genutzte Bibliotheken erstellt. Typischerweise lautet der Dateiname der libpython gemeinsam genutzten Bibliothek libpythonX.Ym.so.1.0 für Python 3.5‑3.7 oder libpythonX.Y.so.1.0 für Python 3.8 oder neuer (zum Beispiel: libpython3.7m.so.1.0, libpython3.9.so.1.0).


