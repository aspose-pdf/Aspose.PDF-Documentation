---
title: PDF-Dateien in Python sichern und signieren
linktitle: Sichern und Signieren in PDF
type: docs
weight: 210
url: /de/python-net/securing-and-signing/
description: Erfahren Sie, wie Sie PDF-Dateien in Python signieren, verschlüsseln, entschlüsseln und sichern, einschließlich digitaler Signaturen, Smartcards und Dokumentberechtigungen.
lastmod: "2026-05-18"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: PDF-Dokumente in Python signieren, verschlüsseln, entschlüsseln und schützen
Abstract: Dieser Abschnitt erklärt, wie man PDF-Dokumente mithilfe von Aspose.PDF for Python via .NET sichert und signiert. Erfahren Sie, wie Sie digitale Signaturen anwenden, Smartcards und Zertifikate verwenden, Signaturinformationen extrahieren und die PDF-Verschlüsselung, Passwörter und Zugriffsrechte in Python verwalten.
---

Dieser Abschnitt erklärt, wie man digitale Signaturen sicher auf PDF-Dokumente mit der Python-Bibliothek anwendet. Während die Begriffe elektronische Signatur und digitale Signatur manchmal austauschbar verwendet werden, sind sie nicht dasselbe. Eine digitale Signatur wird unterstützt von einem [Zertifizierungsstelle](https://en.wikipedia.org/wiki/Certificate_authority), Bereitstellung eines vertrauenswürdigen Siegels, das das Dokument vor Manipulation schützt. Im Gegensatz dazu wird eine elektronische Signatur typischerweise verwendet, um die Absicht einer Person, ein Dokument zu unterschreiben, anzuzeigen, ohne das gleiche Maß an Sicherheitsvalidierung.

Verwenden Sie diese Anleitungen, wenn Sie PDF-Inhalte schützen, Dokumentenberechtigungen steuern, Vertrauen überprüfen oder zertifikatsbasierte Signaturen in Python-Workflows anwenden müssen.

## Abgedeckte Sicherheits- und Signaturaufgaben

Aspose.PDF unterstützt digitale Signaturen:

- PKCS1 mit RSA-Signaturalgorithmus und SHA-1-Hash.
- PKCS7 mit RSA-Signaturalgorithmus und SHA-1-Digest.
- PKCS7 detached mit DSA-, RSA- und ECDSA-Signaturalgorithmen. Die unterstützten Digest-Algorithmen hängen vom Signaturalgorithmus ab.
- Timestamp-Signatur.

Digest-Algorithmen für PKCS7 detached:

- DSA - SHA-1.
- RSA - SHA-1, SHA-256, SHA-384, SHA-512.
- ECDSA - SHA-256, SHA-384, SHA-512, SHA3-256, SHA3-384, SHA3-512.

Es wird empfohlen, digitale Signaturen mit dem SHA‑1-Hash‑Algorithmus aufgrund seiner Unsicherheit zu vermeiden.

- [PDF-Datei digital signieren](/pdf/de/python-net/digitally-sign-pdf-file/)
- [Privilegien festlegen, PDF-Datei verschlüsseln und entschlüsseln](/pdf/de/python-net/set-privileges-encrypt-and-decrypt-pdf-file/)
- [Bild- und Signaturinformationen extrahieren](/pdf/de/python-net/extract-image-and-signature-information/)
- [PDF-Dokument mit Smart Card signieren](/pdf/de/python-net/sign-pdf-document-from-smart-card/)
